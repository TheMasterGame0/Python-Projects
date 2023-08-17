import PySimpleGUI as sg

sg.theme("Dark")  # Define o tema que será usado pelas janelas

# O layout irá definir a aparência da tela a ser criada
# Cada lista na lista é uma linha dentro da página
# Cada item dentro de uma linha indica uma coluna
layout=[
   [sg.Text("Um texto de exemplo:")],
   [sg.In(key="Entrada")],          # Exemplo de Input
   [sg.B("Save"), sg.B("Close")],   # Exemplo de botões
   [sg.Text("",key="Saida")]        # Texto usado para dar um retorno
]

janela = sg.Window("Titulo",layout)

# O loop irá manter a página aberta
while True:
   evento, valores = janela.read()
   if evento == sg.WIN_CLOSED or evento == "Close":   # Cria uma condição para sair do loop
      break
   elif evento == "Save":
      texto = valores["Entrada"]
      janela["Saida"].update(f"O texto '{texto}' foi salvo")


janela.close()