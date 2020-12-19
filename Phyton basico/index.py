import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout da tela
        layout = [
            [sg.Text('Nome',size=(5,5)),sg.Input(size=('70',0),key='nome')],
            [sg.Text('Idade',size=(5,5)),sg.Input(size=(70,0),key='idade')],
            [sg.Text('Quais os provedores de email são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'),sg.Checkbox('Outlook', key='outlook'),sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('Enviar dados')]
        ]
        #Janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        #Extrair os dados da tela 
        self.button, self.values = janela.Read()    

    def Iniciar(self):
        nome = self.values['nome'],
        idade = self.values['idade'],
        aceita_gmail = self.values['gmail'],
        aceita_outlook = self.values['outlook'],
        aceita_yahoo = self.values['yahoo'],
        print(f'nome:   {nome}'),
        print(f'idade: {idade}'),
        print(f'Aceita Gmail: {aceita_gmail}'),
        print(f'Aceita Outlook: {aceita_outlook}'),
        print(f'Aceita Yahoo: {aceita_yahoo}'),

tela = TelaPython()
tela.Iniciar()