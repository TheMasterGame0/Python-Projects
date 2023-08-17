import PySimpleGUI as sg

sg.theme("Dark")  # Define o tema que será usado pelas janelas

#######################################
## Definindo um Layout para uma tela ##
#######################################
# O layout irá definir a aparência da tela a ser criada
# Cada lista na lista é uma linha dentro da página
# Cada item dentro de uma linha indica uma coluna
layout=[
   [sg.Text("Um texto de exemplo:")],
   [sg.In(key="Entrada")],                                        # Exemplo de Input
   [sg.B("Mostrar Texto"), sg.B("Abrir gráfico"), sg.B("Close")], # Exemplo de botões
   [sg.Text("",key="Saida")]                                      # Texto usado para dar um retorno
]

janela = sg.Window("Titulo",layout)


##############################################################
## Criando um layout para uma tela com um gráfico de linhas ##
##############################################################
Tamanho_Grafico = (500, 500)     # O tamanho é dado em pixels
Tamanho_Dados   = (200, 200)     # Representa o valor máximo que os dados podem chegar (x,y)

# O sg.Graph() tem como parâmetros, respectivamente:
# - canvas_size = Tamanho da área do Canvas;
# - graph_bottom_left = Valor fixo no canto esquerdo inferior;
# - graph_top_right = Valor fixo no canto direito superior;

# Ao usar o nome do campo é possível mudar a posição e quais valores serão utilizados para a criação
# - k = É a chave que identifica este elemento, deve ser único em uma janela;

layout_Grafico = [
   [sg.Text('Gráfico gerado com os dados informados:')],
   [sg.Graph(Tamanho_Grafico, (0,0), Tamanho_Dados, k='-GRAPH-')],
   [sg.Button('OK'), sg.T('Click to display more data'), sg.Exit()]
]

# O loop irá manter a página aberta
while True:
   evento, valores = janela.read()
   if evento == sg.WIN_CLOSED or evento == "Close":   # Cria uma condição para sair do loop
      break

   elif evento == "Mostrar Texto":
      texto = valores["Entrada"]
      janela["Saida"].update(f"O texto '{texto}' foi salvo")

   elif evento == "Abrir gráfico":
      tela = sg.window("Gráfico", layout_Grafico)
      grafico = tela['-GRAPH-']                       # Tipo: sg.Graph

      tela.close()


janela.close()