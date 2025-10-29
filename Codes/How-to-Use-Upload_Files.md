# Here, I'll explain how to use the code: <a href="Upload_Files.py">Upload_Files.py</a> <br>


## 1. Requirements
First of all, you need to install a little things:
  - Of curse, you need to have: `python` and `pip` installed.
  - Next, in your console, run:
  - `pip install playwright`
  - `playwright install`

## 2. The Code Structure: The function main
We define the `main` function as `async def`, because this allows other functions to run (if necessary), without stopping the code, while waiting for operations,that might take some time. 
- First line:
  - `caminho_arquivo = os.path.abspath(r"C:\Users\pedro.lopes\Downloads\arquivo_testeX.txt")`
Here, we put the variable "caminho_arquivo" (of curse, if you want, you can change the name), and use the function os.path.abspath, to return an absolute path.

 


