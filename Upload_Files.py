import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    caminho_arquivo = os.path.abspath(r"C:\Users\pedro.lopes\Downloads\arquivo_testeX.txt")

    # Cria o arquivo se não existir
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("Este é um arquivo de teste de upload via Playwright!")

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=False)
        page = await browser.new_page()

        # Abre o site de upload
        await page.goto("https://the-internet.herokuapp.com/upload")

        # Define o arquivo no input
        await page.set_input_files("input#file-upload", caminho_arquivo)

        # Clica no botão de upload
        await page.click("input#file-submit")

        # Aguarda o texto de confirmação
        await page.wait_for_selector("text=File Uploaded!", timeout=15000)

        print("✅ Upload realizado com sucesso!")

        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(main())
