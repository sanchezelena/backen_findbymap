from django.http import JsonResponse
from django.conf import settings
import openai
from supermarket.models.product import Product

# Configura la clave API para OpenAI
openai.api_key = settings.OPENAI_API_KEY

def generate_route_image(request, product_id):
    # Definir la ubicación del monitor (estático)
    monitor_aisle = 2
    monitor_shelf = 3

    try:
        # Obtener el producto de la base de datos
        product = Product.objects.get(id=product_id)
        # Obtener la ubicación del producto
        product_aisle = product.ubication_id.aisle
        product_shelf = product.ubication_id.shelf
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    # Generar el prompt para la API de OpenAI
    prompt = (f"Supermarket map with 15 aisles and 25 shelves. Show a route from Aisle {monitor_aisle}, "
              f"Shelf {monitor_shelf} to Aisle {product_aisle}, Shelf {product_shelf}. Display the route "
              "clearly with arrows indicating the path.")

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return JsonResponse({"image_url": image_url})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
