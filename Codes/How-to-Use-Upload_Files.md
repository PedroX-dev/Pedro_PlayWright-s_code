# Here, I'll explain how to use the code: <a href="Upload_Files.py">Upload_Files.py</a> <br>


## 1. Requirements
First of all, you need to install a little things:
  - Of curse, you need to have: `python` and `pip` installed.
  - Next, in your console, run:
  - `pip install playwright`
  - `playwright install`
Next, we go to The Code Structure

## 2. The function main
We define the `main` function as `async def`, because this allows other functions to run (if necessary), without stopping the code, while waiting for operations,that might take some time. 
- First line:
  - `caminho_arquivo = os.path.abspath(r"C:\Users\pedro.lopes\Downloads\arquivo_testeX.txt")`
Here, we put the variable "caminho_arquivo" (of curse, if you want, you can change the name), and use the function os.path.abspath, to return an absolute path.
Also, you need to specify the name of the file you want to upload.
But, don't worry, if the file doesn't exist, I put a `if`, to create the file in this case:

> if not os.path.exists(caminho_arquivo): <br>
        with open(caminho_arquivo, "w", encoding="utf-8") as f: <br>
            f.write("Este é um arquivo de teste de upload via Playwright!") 


