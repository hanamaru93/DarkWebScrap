import asyncio
import argparse
from pyppeteer import launch

async def scrape_onion_site(url, proxy):
    # Configurando o browser com proxy Tor passado como argumento
    browser = await launch(
        headless=True,
        args=[
            f'--proxy-server={proxy}',  # Proxy configurado via linha de comando
            '--no-sandbox'
        ]
    )
    page = await browser.newPage()

    # Configurando o User Agent para evitar detecção
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    
    try:
        print(f"Acessando {url} com o proxy {proxy}...")
        await page.goto(url, timeout=60000)
        content = await page.content()  # Obtém o HTML da página
        print("Conteúdo da página:")
        print(content)
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
    finally:
        await browser.close()

def main():
    # Configurando o argparse para receber argumentos via linha de comando
    parser = argparse.ArgumentParser(description="Web scraping na deep web usando Pyppeteer.")
    parser.add_argument("-u","--url", help="URL do site (ex: http://exemplo.onion)")
    parser.add_argument("-p","--proxy", help="Endereço do proxy Tor (ex: socks5://127.0.0.1:9050)")
    
    args = parser.parse_args()
    
    # Executando o scraping com os argumentos fornecidos
    asyncio.get_event_loop().run_until_complete(scrape_onion_site(args.url, args.proxy))

if __name__ == "__main__":
    main()

