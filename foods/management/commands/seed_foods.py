from django.core.management.base import BaseCommand
from foods.models import Category, Ingredient, Food

class Command(BaseCommand):
    help = "Puebla la base de datos con categorías, ingredientes y comidas de ejemplo."

    def handle(self, *args, **options):
        # 1️⃣ Crear categorías
        categories = ["Desayuno", "Almuerzo", "Cena", "Snacks", "Postres"]
        category_objs = {}
        for cat in categories:
            category_objs[cat], _ = Category.objects.get_or_create(name=cat)

        # 2️⃣ Crear ingredientes
        ingredients = [
            "Chorizo",
            "Camarón",
            "Langostinos",
            "Papaya verde",
            "Papaya",
            "Aceituna",
            "Ahuyama",
            "Cerveza",
            "Placa de lasaña",
            "Aceitunas",
            "Aceite",
            "Aceite de oliva",
            "Aceite para freír",
            "Aceite vegetal",
            "Aguacate",
            "Agua",
            "Ajo",
            "Ají",
            "Ají costeño",
            "Almidón de yuca",
            "Arepa",
            "Arepa de maíz",
            "Arroz",
            "Arroz blanco",
            "Azúcar",
            "Azúcar morena",
            "Bicarbonato",
            "Bizcocho",
            "Butifarra",
            "Calamar",
            "Canela",
            "Camarones",
            "Carne de cerdo",
            "Carne de res",
            "Carne molida",
            "Cebolla",
            "Champiñones",
            "Chicharrón",
            "Chocolate",
            "Cilantro",
            "Coco",
            "Coco rallado",
            "Comino",
            "Corozo",
            "Costilla de res",
            "Crema de leche",
            "Espaguetis",
            "Espinaca",
            "Especias",
            "Fresas",
            "Frijoles",
            "Fríjol cabecita negra",
            "Gallina",
            "Guandú",
            "Guayaba",
            "Harina de trigo",
            "Hoja de maíz",
            "Huevo",
            "Leche",
            "Leche condensada",
            "Leche de coco",
            "Leche evaporada",
            "Lechuga",
            "Limón",
            "Lisa",
            "Mantequilla",
            "Maíz pelado",
            "Maíz tierno",
            "Masa de maíz",
            "Masa de pizza",
            "Mayonesa",
            "Mostaza",
            "Morcilla",
            "Mojarra",
            "Mondongo de res",
            "Ñame",
            "Orégano",
            "Papa",
            "Pan de hamburguesa",
            "Pan para perro caliente",
            "Panela",
            "Papas chips",
            "Pargo rojo",
            "Pasas",
            "Pepperoni",
            "Pescado",
            "Pimentón",
            "Pimienta",
            "Plátano maduro",
            "Plátano verde",
            "Pollo",
            "Queso",
            "Queso costeño",
            "Queso mozzarella",
            "Queso parmesano",
            "Queso ricotta",
            "Queso rallado",
            "Sal",
            "Salchicha",
            "Salchichas",
            "Salsa",
            "Salsa de tomate",
            "Suero costeño",
            "Tomate",
            "Tripa natural",
            "Vainilla",
            "Verduras",
            "Yuca",
            "Zanahoria",
            "Arvejas",
            
            ]

        ingredient_objs = {}
        for ing in ingredients:
            ingredient_objs[ing], _ = Ingredient.objects.get_or_create(name=ing)

        # 3️⃣ Crear comidas
        foods_data = [
            {
                "title": "Arroz con Pollo",
                "category": "Almuerzo",
                "ingredients": ["Arroz" , "Pollo" , "Zanahoria" , "Arvejas" , "Cebolla" , "Ajo" , "Comino" , "Pimienta" , "Sal" , "Aceite" , "Agua" , "Cilantro"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035288/arroz-pollo_g4szsd.jpg"
            },
            {
                "title": "Arepa de huevo",
                "category": "Desayuno",
                "ingredients": ["Arepa de maíz","Huevo","Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035288/AREPA_HUEVO_lhzbzv.jpg"
            },
            {
                "title": "Arepa e' queso",
                "category": "Desayuno",
                "ingredients": ["Arepa de maíz", "Queso costeño", "Mantequilla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035288/arepas-con-queso_nvujwx.jpg"
            },
            {
                "title": "Bollo limpio",
                "category": "Desayuno",
                "ingredients": ["Masa de maíz", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035288/bollo-limpio_b3b48h.jpg"
            },
            {
                "title": "Bollo de yuca",
                "category": "Desayuno",
                "ingredients": ["Yuca", "Sal", "Hoja de maíz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035289/bollo-yuca_gpd3dp.jpg"
            },
            {
                "title": "Bollo de angelito",
                "category": "Desayuno",
                "ingredients": ["Maíz tierno", "Azúcar", "Hoja de maíz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035288/bollo_de_angelit_sdbwpf.jpg"
            },
            {
                "title": "Carimañola",
                "category": "Desayuno",
                "ingredients": ["Yuca", "Carne molida", "Huevo", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035291/carimannola_p37qtz.jpg"
            },
            {
                "title": "Empanada de carne",
                "category": "Snacks",
                "ingredients": ["Masa de maíz", "Carne molida", "Papa", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035292/empanada-carne_uqadjz.jpg"
            },
            {
                "title": "Empanada de pollo",
                "category": "Snacks",
                "ingredients": ["Masa de maíz", "Pollo", "Papa", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035292/empanada-pollo_une5wh.jpg"
            },
            {
                "title": "Butifarra soledeña",
                "category": "Snacks",
                "ingredients": ["Carne de cerdo", "Tripa natural", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035289/butifarra-soledenna_hkxvua.jpg"
            },
            {
                "title": "Chorizo atollado",
                "category": "Almuerzo",
                "ingredients": ["Chorizo", "Arroz", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Chorizo_atollado_vurne5.jpg"
            },
            {
                "title": "Pescado frito",
                "category": "Almuerzo",
                "ingredients": ["Pescado", "Sal", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Pescado_frito_b3myci.jpg"
            },
            {
                "title": "Pargo rojo frito",
                "category": "Almuerzo",
                "ingredients": ["Pargo rojo", "Limón", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283395/Pargo_rojo_frito_jptxek.jpg"
            },
            {
                "title": "Mojarra frita",
                "category": "Almuerzo",
                "ingredients": ["Mojarra", "Sal", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Mojarra_frita_jjqrqn.jpg"
            },
            {
                "title": "Arroz con coco",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Leche de coco", "Azúcar", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283358/Arroz_con_coco_xtjawy.jpg"
            },
            {
                "title": "Arroz de lisa",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Lisa", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283359/Arroz_de_lisa_cwbbja.png"
            },
            {
                "title": "Patacones",
                "category": "Snacks",
                "ingredients": ["Plátano verde", "Sal", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760284339/Patacones_fjfwhi.jpg"
            },
            {
                "title": "Aborrajado",
                "category": "Snacks",
                "ingredients": ["Plátano maduro", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283357/Aborrajado_jbtyyh.jpg"
            },
            {
                "title": "Mote de queso",
                "category": "Almuerzo",
                "ingredients": ["Ñame", "Queso costeño", "Suero costeño"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Mote_de_queso_zw5b4u.jpg"
            },
            {
                "title": "Sopa de mondongo",
                "category": "Almuerzo",
                "ingredients": ["Mondongo de res", "Papa", "Yuca", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sopa_de_mondongo_ca9cmc.jpg"
            },
            {
                "title": "Sopa de guandú",
                "category": "Almuerzo",
                "ingredients": ["Guandú", "Arroz", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sopa_de_guand%C3%BA_hnsx6h.jpg"
            },
            {
                "title": "Sopa de pescado",
                "category": "Almuerzo",
                "ingredients": ["Pescado", "Yuca", "Plátano verde"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sancocho_de_pescado_xx9p41.jpg"
            },
            {
                "title": "Cazuela de mariscos",
                "category": "Almuerzo",
                "ingredients": ["Camarón", "Calamar", "Pescado", "Leche de coco"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Cazuela_de_mariscos_etezih.jpg"
            },
            {
                "title": "Camarones al ajillo",
                "category": "Almuerzo",
                "ingredients": ["Camarón", "Ajo", "Mantequilla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Camarones_al_ajillo_dscasv.jpg"
            },
            {
                "title": "Langostinos en salsa de coco",
                "category": "Almuerzo",
                "ingredients": ["Langostinos", "Leche de coco", "Especias"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Langostinos_en_salsa_de_coco_qh910n.jpg"
            },
            {
                "title": "Ensalada de aguacate",
                "category": "Almuerzo",
                "ingredients": ["Aguacate", "Cebolla", "Limón"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283369/Ensalada_de_aguacate_fcka9e.jpg"
            },
            {
                "title": "Ensalada de papaya verde",
                "category": "Almuerzo",
                "ingredients": ["Papaya verde", "Limón", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283369/Ensalada_de_papaya_verde_ocnsed.jpg"
            },
            {
                "title": "Arequipe de leche",
                "category": "Postres",
                "ingredients": ["Leche", "Azúcar", "Bicarbonato"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283357/Arequipe_de_leche_li8igx.jpg"
            },
            {
                "title": "Cocada blanca",
                "category": "Postres",
                "ingredients": ["Coco", "Azúcar", "Leche"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Cocada_blanca_gwkgpx.jpg"
            },
            {
                "title": "Cocada negra",
                "category": "Postres",
                "ingredients": ["Coco", "Panela", "Canela"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283361/Cocada_negra_eqvmx8.jpg"
            },
            {
                "title": "Dulce de guayaba",
                "category": "Postres",
                "ingredients": ["Guayaba", "Azúcar"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283366/Dulce_de_guayaba_q6h1as.jpg"
            },
            {
                "title": "Dulce de papaya",
                "category": "Postres",
                "ingredients": ["Papaya", "Azúcar", "Canela"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283366/Dulce_de_papaya_ey59sz.jpg"
            },
            {
                "title": "Dulce de corozo",
                "category": "Postres",
                "ingredients": ["Corozo", "Azúcar"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283362/Dulce_de_coco_b2tjka.jpg"
            },
            {
                "title": "Caballito",
                "category": "Postres",
                "ingredients": ["Papaya verde", "Azúcar", "Canela"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283359/Caballito_tbejly.jpg"
            },
            {
                "title": "Bollo de mazorca",
                "category": "Desayuno",
                "ingredients": ["Maíz tierno", "Sal", "Hoja de maíz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283359/Bollo_de_mazorca_y1dxnv.jpg"
            },
            {
                "title": "Pan de bono costeño",
                "category": "Snacks",
                "ingredients": ["Queso costeño", "Almidón de yuca", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283371/Pan_de_bono_coste%C3%B1o_dca5ds.jpg"
            },
            {
                "title": "Pan de yuca",
                "category": "Snacks",
                "ingredients": ["Almidón de yuca", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283375/Pan_de_yuca_pshfpo.jpg"
            },
            {
                "title": "Peto",
                "category": "Desayuno",
                "ingredients": ["Maíz pelado", "Leche", "Azúcar"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760284918/Peto_y1lfbo.jpg"
            },
            {
                "title": "Bollo de queso",
                "category": "Desayuno",
                "ingredients": ["Masa de maíz", "Queso costeño", "Hoja de maíz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Bollo_de_queso_lfnsr4.jpg"
            },
            {
                "title": "Pastel de arroz",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Carne de cerdo", "Aceituna", "Pasas"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760285026/Pastel_de_arroz_fqztg9.jpg"
            },
            {
                "title": "Pastel de pollo",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Pollo", "Aceituna", "Pasas"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760285137/Pastel_de_pollo_lznfcx.png"
            },
            {
                "title": "Pastel de gallina",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Gallina", "Aceituna", "Pasas"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283417/Pastel_de_gallina_kdhydg.jpg"
            },
            {
                "title": "Tamal costeño",
                "category": "Almuerzo",
                "ingredients": ["Masa de maíz", "Carne de cerdo", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Tamal_coste%C3%B1o_kwyiqv.jpg"
            },
            {
                "title": "Tamal de pollo",
                "category": "Almuerzo",
                "ingredients": ["Masa de maíz", "Pollo", "Verduras"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Tamal_de_pollo_q1nvux.jpg"
            },
            {
                "title": "Sancocho de gallina",
                "category": "Almuerzo",
                "ingredients": ["Gallina", "Yuca", "Plátano verde"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sancocho_de_gallina_jmglhg.jpg"
            },
            {
                "title": "Sancocho de pescado",
                "category": "Almuerzo",
                "ingredients": ["Pescado", "Yuca", "Plátano verde"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sancocho_de_pescado_xx9p41.jpg"
            },
            {
                "title": "Sudado de pollo",
                "category": "Almuerzo",
                "ingredients": ["Pollo", "Papa", "Arroz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Sudado_de_pollo_rmacws.jpg"
            },
            {
                "title": "Sudado de carne",
                "category": "Almuerzo",
                "ingredients": ["Carne de res", "Papa", "Arroz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Sudado_de_carne_ysmij8.jpg"
            },
            {
                "title": "Sudado de costilla",
                "category": "Almuerzo",
                "ingredients": ["Costilla de res", "Papa", "Arroz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Sudado_de_costilla_owfyky.jpg"
            },
            {
                "title": "Arroz con huevo",
                "category": "Desayuno",
                "ingredients": ["Arroz", "Huevo", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283358/Arroz_con_huevo_rstnbh.jpg"
            },
            {
                "title": "Calentado costeño",
                "category": "Desayuno",
                "ingredients": ["Arroz", "Fríjol cabecita negra", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Calentado_coste%C3%B1o_j5cqaq.jpg"
            },
            {
                "title": "Fríjol cabecita negra guisado",
                "category": "Almuerzo",
                "ingredients": ["Fríjol cabecita negra", "Cebolla", "Tomate"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Fr%C3%ADjol_cabecita_negra_guisado_dlrsem.jpg"
            },
            {
                "title": "Arroz con fríjol",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Fríjol cabecita negra", "Suero costeño"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283358/Arroz_con_fr%C3%ADjol_dxdc5a.jpg"
            },
            {
                "title": "Torta de yuca",
                "category": "Postres",
                "ingredients": ["Yuca", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283799/Torta_de_yuca_esxjwb.jpg"
            },
            {
                "title": "Torta de plátano maduro",
                "category": "Postres",
                "ingredients": ["Plátano maduro", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283799/Torta_de_pl%C3%A1tano_maduro_tz0jvr.jpg"
            },
            {
                "title": "Torta de maíz",
                "category": "Postres",
                "ingredients": ["Maíz tierno", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Torta_de_ma%C3%ADz_jdctkr.jpg"
            },
            {
                "title": "Torta de ahuyama",
                "category": "Postres",
                "ingredients": ["Ahuyama", "Queso costeño", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283793/Torta_de_ahuyama_mhywjw.jpg"
            },
            {
                "title": "Torta de queso costeño",
                "category": "Postres",
                "ingredients": ["Queso costeño", "Huevo", "Harina de trigo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760285670/Torta_de_queso_coste%C3%B1o_kowh78.jpg"
            },
            {
                "title": "Arepa dulce",
                "category": "Desayuno",
                "ingredients": ["Arepa de maíz", "Panela", "Queso costeño"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283357/Arepa_dulce_k6xsgf.jpg"
            },
            {
                "title": "Buñuelos costeños",
                "category": "Snacks",
                "ingredients": ["Queso costeño", "Almidón de yuca", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283359/Bu%C3%B1uelos_coste%C3%B1os_jrjdpv.jpg"
            },
            {
                "title": "Pandebono",
                "category": "Snacks",
                "ingredients": ["Queso costeño", "Almidón de yuca", "Huevo"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283375/Pandebono_rqb1ip.jpg"
            },
            {
                "title": "Queso costeño asado",
                "category": "Snacks",
                "ingredients": ["Queso costeño"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Queso_coste%C3%B1o_asado_malymj.jpg"
            },            
            {
                "title": "Ñame guisado",
                "category": "Almuerzo",
                "ingredients": ["Ñame", "Cebolla", "Tomate"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760285910/%C3%91ame_guisado_il2qfd.jpg"
            },
            {
                "title": "Carne en posta negra",
                "category": "Almuerzo",
                "ingredients": ["Carne de res", "Panela", "Cerveza"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760285975/Carne_en_posta_negra_spnapx.jpg"
            },
            {
                "title": "Carne guisada",
                "category": "Almuerzo",
                "ingredients": ["Carne de res", "Tomate", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286040/Arroz_de_coco_con_carne_guisada_jq38ze.jpg"
            },
            {
                "title": "Carne en bistec",
                "category": "Almuerzo",
                "ingredients": ["Carne de res", "Tomate", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286132/Carne_en_bistec_vfscjs.jpg"
            },
            {
                "title": "Carne molida guisada",
                "category": "Almuerzo",
                "ingredients": ["Carne molida", "Cebolla", "Tomate"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286175/Carne_molida_guisada_ymfkvl.jpg"
            },
            {
                "title": "Huevos pericos",
                "category": "Desayuno",
                "ingredients": ["Huevo", "Cebolla", "Tomate"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286234/Huevos_pericos_kr6cty.jpg"
            },
            {
                "title": "Huevos revueltos con cebolla",
                "category": "Desayuno",
                "ingredients": ["Huevo", "Cebolla", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286286/Huevos_revueltos_con_cebolla_jf9pe6.jpg"
            },
           {
                "title": "Bollo de mazorca con queso",
                "category": "Desayuno",
                "ingredients": ["Maíz tierno", "Queso costeño", "Hoja de maíz"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286606/Bollo_de_mazorca_con_queso_mtyqlv.jpg"
            },
            {
                "title": "Bolita de yuca con queso",
                "category": "Snacks",
                "ingredients": ["Yuca", "Queso costeño", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286715/Bolita_de_yuca_con_queso_wgh4fe.jpg"
            },
            {
                "title": "Enyucado costeño",
                "category": "Postres",
                "ingredients": ["Yuca", "Queso costeño", "Coco", "Azúcar"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760286778/Enyucado_coste%C3%B1o_revbl8.jpg"
            },
            {
                "title": "Pan de coco",
                "category": "Postres",
                "ingredients": ["Harina de trigo", "Coco", "Azúcar"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760287166/Pan_de_coco_t9imej.jpg"
            },
            {
                "title": "Chuzo de carne",
                "category": "Snacks",
                "ingredients": ["Carne de res", "Pimentón", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Chuzo_de_carne_lfix18.jpg"
            },
            {
                "title": "Chuzo de pollo",
                "category": "Snacks",
                "ingredients": ["Pollo", "Pimentón", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283360/Chuzo_de_pollo_v2roc1.jpg"
            },
            {
                "title": "Chuzo mixto",
                "category": "Snacks",
                "ingredients": ["Pollo", "Carne de res", "Pimentón", "Cebolla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760287255/Chuzo_mixto_lldrgg.jpg"
            },
            {
                "title": "Sopa de costilla",
                "category": "Almuerzo",
                "ingredients": ["Costilla de res", "Papa", "Zanahoria", "Cebolla", "Ajo", "Cilantro", "Comino", "Sal", "Agua"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Sopa_de_costilla_ui8dyl.jpg"
            },
            {
                "title": "Pizza",
                "category": "Cena",
                "ingredients": ["Masa de pizza", "Salsa de tomate", "Queso mozzarella", "Pepperoni", "Champiñones", "Aceitunas", "Orégano", "Aceite de oliva"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Pizza_frgss0.jpg"
            },
            {
                "title": "Chicharrón con yuca",
                "category": "Almuerzo",
                "ingredients": ["Carne de cerdo", "Yuca", "Sal", "Ajo", "Comino", "Aceite", "Limón", "Ají"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760287387/Chicharr%C3%B3n_con_yuca_tnhxm7.png"
            },
            {
                "title": "Arroz de coco con pescado frito",
                "category": "Almuerzo",
                "ingredients": ["Arroz blanco", "Leche de coco", "Azúcar morena", "Sal", "Agua", "Aceite vegetal", "Mantequilla", "Coco rallado", "Pescado", "Ajo", "Comino", "Pimienta", "Limón", "Harina de trigo", "Aceite para freír", "Plátano verde", "Tomate", "Cebolla", "Lechuga", "Ají costeño", "Suero costeño"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283357/Arroz_de_coco_con_pescado_frito_f3cloe.jpg"
            },
            {
                "title": "Butifarra con bollo de yuca",
                "category": "Almuerzo",
                "ingredients": ["Butifarra", "Yuca", "Sal", "Ajo", "Comino", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760287471/Butifarra_con_bollo_de_yuca_ypkxel.jpg"
            },
            {
                "title": "Espaguetis",
                "category": "Almuerzo",
                "ingredients": ["Espaguetis", "Salsa de tomate", "Carne molida", "Cebolla", "Ajo", "Sal", "Pimienta", "Queso parmesano"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Espaguetis_fdizwr.jpg"
            },
            {
                "title": "Salchipapa",
                "category": "Snacks",
                "ingredients": ["Salchichas", "Papa", "Salsa de tomate", "Mayonesa", "Mostaza", "Queso rallado"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Salchipapa_z5awz1.jpg"
            },
            {
                "title": "Hamburguesas",
                "category": "Cena",
                "ingredients": ["Pan de hamburguesa", "Carne molida", "Lechuga", "Tomate", "Cebolla", "Queso", "Salsa", "Mostaza", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Hamburguesas_kkmuab.jpg"
            },
            {
                "title": "Perro caliente",
                "category": "Snacks",
                "ingredients": ["Pan para perro caliente", "Salchicha", "Salsa de tomate", "Mayonesa", "Mostaza", "Queso rallado", "Papas chips"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283791/Perro_caliente_xp8tcq.jpg"
            },
            {
                "title": "Lasaña",
                "category": "Cena",
                "ingredients": ["Placa de lasaña", "Carne molida", "Salsa de tomate", "Queso ricotta", "Queso mozzarella", "Espinaca", "Sal", "Pimienta"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Lasa%C3%B1a_pdtfh3.png"
            },
            {
                "title": "Arroz de leche",
                "category": "Postres",
                "ingredients": ["Arroz", "Leche", "Azúcar", "Canela", "Pasas", "Mantequilla", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283359/Arroz_de_leche_i1ol1k.jpg"
            },
            {
                "title": "Empanada de queso",
                "category": "Snacks",
                "ingredients": ["Masa de maíz", "Queso", "Sal", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283366/Empanada_de_queso_gksmvc.jpg"
            },
            {
                "title": "Empanada de pollo",
                "category": "Snacks",
                "ingredients": ["Masa de maíz", "Pollo", "Papa", "Cebolla", "Ajo", "Sal", "Aceite"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760035292/empanada-pollo_une5wh.jpg"
            },
            {
                "title": "Bandeja paisa",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Frijoles", "Carne molida", "Chicharrón", "Huevo", "Plátano maduro", "Aguacate", "Arepa", "Chorizo", "Morcilla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283358/Bandeja_paisa_ge1vew.jpg"
            },
            {
                "title": "Dulce de coco",
                "category": "Postres",
                "ingredients": ["Coco rallado", "Leche", "Azúcar", "Canela", "Mantequilla", "Sal"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283362/Dulce_de_coco_b2tjka.jpg"
            },
            {
                "title": "Arroz de coco con carne guisada",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Carne de res", "Leche de coco", "Cebolla", "Ajo", "Comino", "Sal", "Aceite", "Agua"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760287813/Arroz_de_coco_con_carne_guisada_xleg29.jpg"
            },
            {
                "title": "Arroz de camarón",
                "category": "Almuerzo",
                "ingredients": ["Arroz", "Camarones", "Cebolla", "Ajo", "Comino", "Sal", "Aceite", "Agua"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283358/Arroz_de_camar%C3%B3n_ayrtxj.jpg"
            },
            {
                "title": "Fresas con crema",
                "category": "Postres",
                "ingredients": ["Fresas", "Crema de leche", "Azúcar", "Vainilla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283370/Fresas_con_crema_jmj067.jpg"
            },
            {
                "title": "Postre de tres leches",
                "category": "Postres",
                "ingredients": ["Bizcocho", "Leche evaporada", "Leche condensada", "Crema de leche", "Vainilla"],
                "imgUrl": "https://res.cloudinary.com/dqlrqzo1a/image/upload/v1760283792/Postre_de_tres_leches_wwzyj3.jpg"
            },
            
            
            
        ]

        for food in foods_data:
            f, created = Food.objects.get_or_create(
                title=food["title"],
                category=category_objs[food["category"]],
                imgUrl=food["imgUrl"],
            )
            if created:
                f.ingredients.set([ingredient_objs[i] for i in food["ingredients"]])
                self.stdout.write(self.style.SUCCESS(f"✅ {f.title} creada"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ {f.title} ya existía"))

        self.stdout.write(self.style.SUCCESS("✨ Base de datos poblada exitosamente"))
