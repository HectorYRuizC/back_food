from django.contrib import admin
from django.shortcuts import render
from .models import User,Food,Rating,RecommendationHistory
import csv
from django.http import HttpResponseRedirect
from django.urls import path
from django import forms
from io import StringIO

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    change_list_template = "admin/food_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            if not csv_file.name.endswith('.csv'):
                self.message_user(request, "El archivo no es CSV", level='error')
                return HttpResponseRedirect(request.path_info)

        # Leer CSV
            try:
                
                file_data = StringIO(csv_file.read().decode("utf-8-sig"))
                reader = csv.DictReader(file_data)
                reader.fieldnames = [field.strip() for field in reader.fieldnames]

            except Exception as e:
                self.message_user(request, f"Error al leer el archivo: {str(e)}", level='error')
                return HttpResponseRedirect(request.path_info)

            added = 0
            for i, row in enumerate(reader, start=1):
                try:
                    name = row["name"].strip()
                    ingredients = row["ingredients"].strip()
                    if name and ingredients:
                        Food.objects.create(name=name, ingredients=ingredients)
                        added += 1
                except KeyError as e:
                    self.message_user(request, f"Fila {i}: falta la columna {e}", level='error')
                    continue
                except Exception as e:
                    self.message_user(request, f"Fila {i}: error inesperado: {str(e)}", level='error')
                    continue

            self.message_user(request, f"{added} comidas importadas correctamente")
            return HttpResponseRedirect("../")

        form = CsvImportForm()
        context = {
         "form": form,
        }
        return render(request, "admin/csv_form.html", context)



class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

admin.site.register(User)
admin.site.register(Rating)
admin.site.register(RecommendationHistory)