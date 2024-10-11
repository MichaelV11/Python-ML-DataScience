import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def scrape_operators(page):
    operators_data = []
    
    # Selecciona todos los operadores en la página
    operators = await page.query_selector_all("div[class*='operator']")

    for operator in operators:
        data = {}

        # Extrae los datos
        data['First Name'] = (await operator.query_selector("div:has-text('operator')")).inner_text().split()[0]
        data['Last Name'] = (await operator.query_selector("div:has-text('operator')")).inner_text().split()[-1]
        data['Position'] = await operator.query_selector("div:has-text('at')").inner_text()
        data['Company Name'] = data['Position'].split('at')[-1].strip()
        data['Information'] = await operator.query_selector("div:has-text('Information')").inner_text() if await operator.query_selector("div:has-text('Information')") else ""
        
        # Extraer las etiquetas
        tags = await operator.query_selector_all("span[class*='label']")
        data['Tags'] = ", ".join([await tag.inner_text() for tag in tags])
        
        operators_data.append(data)
    
    return operators_data

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Abre la página
        await page.goto('https://match.sigma.world/find?filter=operator', timeout=60000)
        await page.wait_for_load_state('networkidle')

        # Extrae la información de los operadores
        operators_data = await scrape_operators(page)

        # Guarda los datos en un archivo Excel
        df = pd.DataFrame(operators_data)
        df.to_excel('operators_data.xlsx', index=False)

        await browser.close()

# Ejecuta la función principal
asyncio.run(main())
