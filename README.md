<h1>🖼️ Descarga de Imágenes desde un Archivo HAR 🖼️</h1>

<p>Este proyecto en Python es para descargar imágenes de un sitio web utilizando archivos HAR. Este proyecto permite extraer automáticamente todas las imágenes desde un archivo .har generado por DevTools del navegador, facilitando la descarga masiva de imágenes.</p>

<h2>📋 Tabla de Contenidos</h2>
<ul>
  <li><a href="#-características">Requisitos</a></li>
  <li><a href="#-instalación">Instalación</a></li>
  <li><a href="#-guía-de-uso">Guía de Uso</a></li>
    <ul>
      <li><a href="#1-generar-el-archivo-har">Generar el Archivo HAR</a></li>
      <li><a href="#2-alternativa-para-guardar-el-archivo-har">Alternativa para Guardar el Archivo HAR</a></li>
      <li><a href="#3-ejecutar-el-script-de-descarga">Ejecutar el Script de Descarga</a></li>
    </ul>
  <li><a href="#%EF%B8%8F-detalles-técnicos-del-script">Detalles Técnicos del Script</a></li>
  <li><a href="#-notas-importantes">Notas Importantes</a></li>
  <li><a href="#-contribuciones">Contribuciones</a></li>
</ul>


<h2>✨ Características</h2>
<ul>
  <li>Descarga automática de imágenes: Extrae y descarga todas las imágenes contenidas en un archivo .har.</li>
  <li>Filtros inteligentes: Solo descarga archivos de imágenes (formatos como .jpg, .png, .gif, etc.).</li>
  <li>Carpeta de destino: Guarda todas las imágenes descargadas en una carpeta organizada.</li>
</ul>

<h2>🛠️ Requisitos</h2>
<p>Antes de comenzar, asegúrate de tener instalado:</p>
  <ul>
    <li>Python 3.x</li>
    <li>Biblioteca requests para Python</li>
    <li>Para instalar requests, ejecuta en la terminal:</li>
  </ul>

    pip install requests

<h2>🚀 Instalación</h2>

<h4>1. Clona este repositorio en tu máquina local:</h4>

      git clone https://github.com/tu-usuario/nombre-del-repositorio.git
      cd nombre-del-repositorio

<h4>2. Asegúrate de que requests está instalado en tu entorno de Python:</h4>

      pip install requests

<h2>📖 Guía de Uso</h2>

<h3>1. Generar el Archivo HAR</h3>
<p>Para capturar las imágenes desde un sitio web, primero necesitas generar un archivo .har con las solicitudes de red de la página.</p>
 <ul> 
    <li>Abre el sitio web desde el que deseas descargar las imágenes.</li>
    <li>Abre DevTools en tu navegador (presiona F12 o Ctrl+Shift+I).</li>
    <li>Ve a la pestaña Network (Red) y selecciona la opción Preserve log (Preservar registro).</li>
    <li>Recarga la página para capturar todas las solicitudes de red.</li>
    <li>Haz clic derecho en cualquier parte del registro de solicitudes y selecciona Save all as HAR with content (Guardar todo como HAR con contenido) para guardar el archivo .har.
      (Nota: Guarda el archivo con un nombre fácil de recordar, como mi_archivo.har.)</li>
 </ul> 

<h3>2. Alternativa para Guardar el Archivo HAR</h3>
<p>Si no tienes la opción de guardar el archivo HAR, aquí tienes un método alternativo:</p>
  <ul>
    <li>Haz clic derecho en la lista de solicitudes en DevTools y selecciona Copy all listed as 'HAR' (with sensitive data).</li>
    <li>Abre un editor de texto (como Visual Studio Code o Notepad).</li>
    <li>Pega el contenido copiado y guárdalo con la extensión .har (por ejemplo, mi_archivo.har).</li>
  </ul>
  
<h3>3. Ejecutar el Script de Descarga</h3>
<p>Con el archivo .har listo, es momento de ejecutar el script para descargar las imágenes:</p>
  <ul>  
    <li>Coloca el archivo .har en la misma carpeta que el script extract_images.py.</li>
    <li>Abre una terminal en esa carpeta y ejecuta el script con: python extract_images.py</li>
  </ul>

<h2>⚙️ Detalles Técnicos del Script</h2>

<p>El script extract_images.py realiza las siguientes funciones:</p>

  <ul>
    <li>Carga el archivo HAR: Lee el archivo .har proporcionado y filtra las solicitudes de tipo image.</li>
    <li>Descarga las imágenes: Utiliza la biblioteca requests para descargar cada imagen a la carpeta imagenes_descargadas.</li>
    <li>Control de errores: Si una imagen no se puede descargar, el script muestra un mensaje de error y continúa con la siguiente.</li>
  </ul>

      import json
      import os
      import requests
      
      har_file = 'mi_archivo.har'  # Asegúrate de que el nombre sea correcto
      
      with open(har_file, 'r', encoding='utf-8') as file:
          har_data = json.load(file)
      
      # Crear la carpeta de destino
      output_folder = 'imagenes_descargadas'
      if not os.path.exists(output_folder):
          os.makedirs(output_folder)
      
      # Filtrar las imágenes y descargarlas
      for entry in har_data['log']['entries']:
          url = entry['request']['url']
          mime_type = entry['response']['content']['mimeType']
          
          if mime_type.startswith('image/'):
              image_name = url.split('/')[-1].split('?')[0]
              output_path = os.path.join(output_folder, image_name)
      
              try:
                  response = requests.get(url)
                  if response.status_code == 200:
                      with open(output_path, 'wb') as img_file:
                          img_file.write(response.content)
                      print(f'Imagen descargada: {image_name}')
                  else:
                      print(f'Error al descargar {image_name}: {response.status_code}')
              except Exception as e:
                  print(f'Error al descargar {image_name}: {e}')

<h2>🔍 Notas Importantes</h2>
  <ul>
    <li>Permisos: Asegúrate de tener los permisos necesarios para descargar las imágenes del sitio web. Respeta siempre los términos y condiciones de cada página.</li>
    <li>Limitaciones del Archivo HAR: Algunos sitios pueden restringir las descargas basadas en cookies o tokens que expiran rápidamente. Si encuentras problemas, intenta generar un archivo HAR nuevo y sigue los pasos de la Guía de Uso.</li>
  </ul>

<h2>🤝 Contribuciones</h2>

<p>¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes una idea para mejorar el proyecto, siéntete libre de abrir un Issue o enviar un Pull Request.
Espero que disfrutes de este proyecto y te sea útil. ¡Feliz descarga de imágenes! 🖼️✨</p>


