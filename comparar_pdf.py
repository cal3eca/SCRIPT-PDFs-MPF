import PyPDF2
import difflib

def extrair_texto(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo)
        texto = ''
        for pagina in range(leitor_pdf.numPages):
            texto += leitor_pdf.getPage(pagina).extractText()
    return texto

# COLOCAR CAMINHO PARA ARQUIVOS
caminho_arquivo1 = r'#COLOQUE O CAMINHO PARA SEU ARQUIVO PDF'
caminho_arquivo2 = r'#COLOQUE O CAMINHO PARA SEU ARQUIVO PDF'

# EXTRAÇÃO DOS TEXTOS DOS ARQUIVOS
texto_arquivo1 = extrair_texto(caminho_arquivo1)
texto_arquivo2 = extrair_texto(caminho_arquivo2)

# COMPARAÇÃO DOS TEXTOS DOS ARQUIVOS
diff = difflib.unified_diff(texto_arquivo1.splitlines(), texto_arquivo2.splitlines(), lineterm='')

# DIFERENÇAS
for linha in diff:
    print(linha)
