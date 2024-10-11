import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def scrape_operators(page):
    operators_data = []

    # Espera a que los elementos de la clase "card" estén presentes
    await page.wait_for_selector(".card")

    # Selecciona todos los elementos con la clase "card"
    cards = await page.query_selector_all(".card")

    for card in cards:
        data = {}

        # Extrae el nombre del operador
        try:
            name = await card.query_selector(".card-title")
            data['Name'] = await name.inner_text() if name else None
        except:
            data['Name'] = None

        # Extrae la posición y la empresa
        try:
            position_and_company = await card.query_selector(".lead")
            data['Position and Company'] = await position_and_company.inner_text() if position_and_company else None
        except:
            data['Position and Company'] = None

        # Extrae la información del operador
        try:
            info = await card.query_selector(".b-block-partner-text__content")
            data['Information'] = await info.inner_text() if info else None
        except:
            data['Information'] = None

        # Extrae las etiquetas (tags)
        try:
            tags_elements = await card.query_selector_all("div.b-block-badges span.badge")
            tags = [await tag.inner_text() for tag in tags_elements]
            data['Tags'] = ", ".join(tags)
        except:
            data['Tags'] = None

        operators_data.append(data)

    return operators_data

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Usa headless=True para ejecutar sin abrir el navegador
        page = await browser.new_page()

        all_operators_data = []

        # Recorre todas las páginas de la 1 a la 15
        for i in range(1, 16):
            url = f'https://match.sigma.world/find/index?filter=operator&page={i}'
            print(f"Scraping page {i}: {url}")
            
            # Navega a la página objetivo
            await page.goto(url, wait_until='load', timeout=120000)  # 120 segundos
            
            # Extrae la información de los operadores en la página actual
            operators_data = await scrape_operators(page)
            all_operators_data.extend(operators_data)

        # Guarda los datos en un archivo Excel
        df = pd.DataFrame(all_operators_data)
        df.to_excel('all_operators_data_playwright.xlsx', index=False)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
