import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from foods.models import Food
from ratings.models import Rating

# === Dataset personalizado ===
class RatingDataset(Dataset):
    def __init__(self, ratings):
        self.user_ids = list(ratings.values_list("user_id", flat=True))
        self.food_ids = list(ratings.values_list("food_id", flat=True))
        self.ratings = list(ratings.values_list("rating", flat=True))

        self.user2idx = {u: i for i, u in enumerate(set(self.user_ids))}
        self.food2idx = {f: i for i, f in enumerate(set(self.food_ids))}
        self.idx2food = {v: k for k, v in self.food2idx.items()}
        self.idx2user = {v: k for k, v in self.user2idx.items()}

        self.x = torch.tensor(
            [[self.user2idx[u], self.food2idx[f]] for u, f in zip(self.user_ids, self.food_ids)],
            dtype=torch.long
        )
        self.y = torch.tensor(self.ratings, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


# === Modelo de factorización matricial ===
class MatrixFactorization(torch.nn.Module):
    def __init__(self, n_users, n_items, n_factors=16):
        super().__init__()
        self.user_factors = torch.nn.Embedding(n_users, n_factors)
        self.item_factors = torch.nn.Embedding(n_items, n_factors)
        self.user_factors.weight.data.uniform_(0, 0.05)
        self.item_factors.weight.data.uniform_(0, 0.05)

    def forward(self, x):
        users, items = x[:, 0], x[:, 1]
        return (self.user_factors(users) * self.item_factors(items)).sum(1)


# === Entrenamiento ===
def train_model(num_epochs=150, lr=1e-3):
    ratings = Rating.objects.all()
    if not ratings.exists():
        return None, None, None, None

    dataset = RatingDataset(ratings)
    loader = DataLoader(dataset, batch_size=64, shuffle=True)

    model = MatrixFactorization(len(dataset.user2idx), len(dataset.food2idx))
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(num_epochs):
        total_loss = 0
        for x, y in loader:
            optimizer.zero_grad()
            preds = model(x)
            loss = loss_fn(preds, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}/{num_epochs} - Loss: {total_loss / len(loader):.4f}")

    return model, dataset.user2idx, dataset.food2idx, dataset


# === Recomendaciones ===
def recommend_for_user(user, model, dataset, n_recommendations=4):
    if user.id not in dataset.user2idx:
        return []

    user_idx = dataset.user2idx[user.id]
    all_items = torch.tensor([[user_idx, i] for i in range(len(dataset.food2idx))], dtype=torch.long)
    predictions = model(all_items).detach().numpy()

    # top N
    top_indices = np.argsort(predictions)[::-1][:n_recommendations]
    results = []

    for i in top_indices:
        food_id = dataset.idx2food[i]
        food = Food.objects.get(id=food_id)
        results.append({
            "id": food.pk,
            "title": food.title,
            "category": food.category.name if hasattr(food, "category") else None,
            "image": food.imgUrl,
            "predicted_rating": float(np.clip(predictions[i], 1.0, 5.0)),  # asegura rango 1–5
        })

    return results
