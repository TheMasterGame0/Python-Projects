import PySimpleGUI as sg
import random as r      # Será utilizado apenas para testar funcionalidades

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


############################################################
## Criando a tela com um gráfico de linhas reaproveitável ##
############################################################
Tamanho_Grafico = (500, 500)     # O tamanho é dado em pixels
Tamanho_Dados   = (200, 200)     # Representa o valor máximo que os dados podem chegar (x,y)
Espaco = 25                      # Será usado como espaço entre os pontos do gráfico
Offset = 10                      # Distancia inicial da barra de início

def CriarTelacomGrafico():
   # O sg.Graph() tem como parâmetros, respectivamente:
   # - canvas_size = Tamanho da área do Canvas;
   # - graph_bottom_left = Valor fixo no canto esquerdo inferior;
   # - graph_top_right = Valor fixo no canto direito superior;

   # Ao usar o nome do campo é possível mudar a posição e quais valores serão utilizados para a criação
   # - k = É a chave que identifica este elemento, deve ser único em uma janela;

   layout_Grafico = [
      [sg.Text('Gráfico gerado com os dados informados:')],
      [sg.Graph(Tamanho_Grafico, (0,0), Tamanho_Dados, k='-GRAPH-')],
      [sg.B('Atualizar'), sg.Exit()]
   ]

   return sg.Window("Gráfico", layout_Grafico, finalize=True)

#################################
## Função para gerar o gráfico ##
#################################
def gerarGrafico():
   # Loop que manterá o gráfico aberto
   while True:
      grafico.erase()     # Limpa o gráfico já existente na tela
      # Para testar o funcionamento serão utilizados valores aleatórios
      for i in range(7):
         # O valor máximo escolhido é menor que o máximo do gráfico para sobrar espaço para a label 
         graph_value = r.randint(0, Tamanho_Dados[1]-25) 
         # Desenha o ponto informado 
         # Formato (Coordenada, Tamanho, Cor)
         grafico.draw_point((i*Espaco + Offset, graph_value), 2, "black")

         grafico.draw_text(text=graph_value, location=(i*Espaco + Offset, graph_value+10), font='_ 14')

      # Colocado no final para escrever o gráfico primeiro
      event, values = tela.read()

      if event in (sg.WIN_CLOSED, 'Exit'):
         break


########################################
## Loop principal para todas as telas ##
########################################

# O loop irá manter a página aberta
while True:
   evento, valores = janela.read()
   if evento == sg.WIN_CLOSED or evento == "Close":   # Cria uma condição para sair do loop
      break

   elif evento == "Mostrar Texto":
      texto = valores["Entrada"]
      janela["Saida"].update(f"O texto '{texto}' foi salvo")

   elif evento == "Abrir gráfico":
      tela = CriarTelacomGrafico()
      grafico = tela['-GRAPH-']     # Tipo: sg.Graph
      gerarGrafico()                # Gera o gráfico
      tela.close()                  # Finaliza a tela do gráfico


janela.close()