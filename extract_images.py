import json
import os
import requests

# Cargar archivo HAR
har_file = 'walworth.com.har'  # Asegúrate de que la ruta del archivo HAR sea correcta

# Leer el archivo HAR
with open(har_file, 'r', encoding='utf-8') as file:
    har_data = json.load(file)

# Crear carpeta para guardar las imágenes
output_folder = 'imagenes_descargadas'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Establecer encabezados (headers) comunes para las solicitudes HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Filtrar entradas de tipo 'image'
for entry in har_data['log']['entries']:
    # Obtener la URL y el tipo de contenido
    url = entry['request']['url']
    mime_type = entry['response']['content']['mimeType']
    
    # Filtrar solo las imágenes (png, jpg, jpeg, gif, etc.)
    if mime_type.startswith('image/'):
        # Obtener el nombre de archivo de la URL
        image_name = url.split('/')[-1].split('?')[0]
        output_path = os.path.join(output_folder, image_name)

        # Descargar la imagen
        try:
            response = requests.get(url, headers=headers)  # Usar los encabezados en la solicitud
            if response.status_code == 200:
                with open(output_path, 'wb') as img_file:
                    img_file.write(response.content)
                print(f'Imagen descargada: {image_name}')
            else:
                print(f'Error al descargar {image_name}: {response.status_code}')
        except Exception as e:
            print(f'Error al descargar {image_name}: {e}')

print('Descarga de imágenes completada.')
