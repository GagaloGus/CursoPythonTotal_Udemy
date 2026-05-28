from playwright.sync_api import sync_playwright
import snscrape.modules.twitter as sntwitter

# Hecho totalmente con la IA
# Este código intenta obtener los últimos 10 tweets de la cuenta de NASA en X (antes Twitter) utilizando Playwright para simular la navegación y extracción de contenido. 
# Si por alguna razón no se pueden obtener los tweets con Playwright (por ejemplo, debido a cambios en la estructura de la página o requerimientos de inicio de sesión), 
# el código hace un fallback utilizando snscrape para obtener los tweets directamente desde la API de Twitter.

url = "https://x.com/NASA"

def extraer_texto_tweet(articulo):
    partes = articulo.locator('div[lang]').all_text_contents()
    if not partes:
        partes = articulo.locator('div[dir="ltr"]').all_text_contents()
    texto = "\n".join([parte.strip() for parte in partes if parte.strip()])
    return texto


def obtener_tweets_desde_x(url, cantidad=10):
    tweets = []
    tweet_texts = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/126.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
        )
        page = context.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector('[data-testid="tweet"]', timeout=15000)

        for _ in range(15):
            articulos = page.locator('[data-testid="tweet"]')
            total = articulos.count()
            for i in range(total):
                articulo = articulos.nth(i)
                texto = extraer_texto_tweet(articulo)
                if texto and texto not in tweet_texts:
                    tweet_texts.add(texto)
                    tweets.append(texto)
                    if len(tweets) >= cantidad:
                        break
            if len(tweets) >= cantidad:
                break
            page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            page.wait_for_timeout(1200)

        browser.close()

    return tweets[:cantidad]


def obtener_tweets_snscrape(username, cantidad=10):
    tweets = []
    try:
        for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
            if i >= cantidad:
                break
            tweets.append(tweet.content) # type: ignore
    except Exception as exc:
        print(f"snscrape fallback failed: {exc}")
    return tweets


def obtener_ultimos_tweets(url, cantidad=10):
    tweets = obtener_tweets_desde_x(url, cantidad)
    if len(tweets) < cantidad:
        twitter_username = url.rstrip("/").split("/")[-1]
        tweets = obtener_tweets_snscrape(twitter_username, cantidad)
    return tweets[:cantidad]


def main():
    tweets = obtener_ultimos_tweets(url, cantidad=10)
    if not tweets:
        print("No se encontraron tweets. Es posible que la página requiera inicio de sesión o que haya cambiado la estructura.")
        return

    print(f"Últimos {len(tweets)} tweets de NASA desde {url}:\n")
    for index, tweet in enumerate(tweets, start=1):
        print(f"Tweet {index}:\n{tweet}\n{'-' * 80}")


if __name__ == "__main__":
    main()
