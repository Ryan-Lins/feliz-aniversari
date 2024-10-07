from IPython.display import display
import pandas as pd

# Para fazer upload de um arquivo
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Inicializa o Tkinter
Tk().withdraw()  # Para não exibir a janela principal

# Abre a janela de seleção de arquivos
file_path = askopenfilename(title='Selecione um arquivo CSV', filetypes=[('CSV files', '*.csv')])

# Carregar o arquivo CSV
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do DataFrame
print(df.head())

