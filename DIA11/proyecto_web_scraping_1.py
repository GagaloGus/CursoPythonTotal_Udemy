from bs4 import BeautifulSoup
import requests

# URL base del sitio
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista para almacenar los libros con rating 4 o 5 estrellas
libros_destacados = []

# Contador de páginas
page_counter = 1

# Bucle para recorrer todas las paginas empezando desde la página 1 hasta que de error al acceder a una página (status code != 200)
while True:
    try:
        url = base_url.format(page_counter)
        request = requests.get(url)
        if request.status_code != 200:
            print(f"Error al acceder a la página {page_counter}: Status code {request.status_code}")
            break

        # Crear la sopa de BeautifulSoup
        sopa = BeautifulSoup(request.content, 'html.parser')

        # Encontrar todos los libros (articles con class="product_pod")
        libros = sopa.find_all('article', class_='product_pod')

        # Recorrer cada libro de la página
        for libro in libros:
            # Encontrar el div con la clase star-rating
            rating_div = libro.find('p', class_='star-rating')

            # Verificar si el rating es Four o Five
            if rating_div and any(rating in str(rating_div.get('class', [])) for rating in ['Four', 'Five']):
                # Extraer el título del libro
                h3 = libro.find('h3')
                titulo_link = h3.find('a') if h3 else None
                titulo = titulo_link.get('title') if titulo_link else None

                # Agregar a la lista si se encontró el título
                if titulo:
                    libros_destacados.append(titulo)
                    print(f"[OK] {titulo}")

        page_counter += 1
        print(f"Página {page_counter - 1} procesada\n")
    except Exception as e:
        print(f"Ocurrió un error: {e}.")
        break

# Mostrar resumen
print(f"\n{'='*50}")
print(f"Total de libros con 4 o 5 estrellas: {len(libros_destacados)}")
print(f"{'='*50}")