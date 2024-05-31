import requests
import pandas as pd
import time

def fetch_items(search_term, limit=50):
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={search_term}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return []

def fetch_item_details(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ejemplo de uso
search_terms = ['Google Home', 'Apple TV', 'Amazon Fire TV']
data = []

for term in search_terms:
    results = fetch_items(term)
    for item in results:
        item_details = fetch_item_details(item['id'])
        if item_details:
            data.append({
                'id': item_details.get('id'),
                'site_id': item_details.get('site_id'),
                'title': item_details.get('title'),
                'seller_id': item_details.get('seller_id'),
                'category_id': item_details.get('category_id'),
                'official_store_id': item_details.get('official_store_id'),
                'price': item_details.get('price'),
                'base_price': item_details.get('base_price'),
                'original_price': item_details.get('original_price'),
                'currency_id': item_details.get('currency_id'),
                'initial_quantity': item_details.get('initial_quantity'),
                'buying_mode': item_details.get('buying_mode'),
                'listing_type_id': item_details.get('listing_type_id'),
                'condition': item_details.get('condition'),
                'permalink': item_details.get('permalink'),
                'thumbnail_id': item_details.get('thumbnail_id'),
                'thumbnail': item_details.get('thumbnail'),
                'video_id': item_details.get('video_id'),
                'accepts_mercadopago': item_details.get('accepts_mercadopago'),
                'warranty': item_details.get('warranty'),
                'catalog_product_id': item_details.get('catalog_product_id'),
                'domain_id': item_details.get('domain_id'),
                'date_created': item_details.get('date_created'),
                'last_updated': item_details.get('last_updated'),
                'status': item_details.get('status'),
                'catalog_listing': item_details.get('catalog_listing')
            })
        time.sleep(1)  # Pausa para evitar exceder el límite de solicitudes a la API

df = pd.DataFrame(data)
print(df.head())

# Guardar el DataFrame en un archivo CSV
df.to_csv('mercadolibre_items.csv', index=False, encoding='utf-8-sig')

print("Datos guardados en mercadolibre_items.csv")
