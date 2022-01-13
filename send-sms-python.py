from tkinter import *
from tkinter import messagebox
import os
from tkinter import font
from tkinter.tix import MAIN
from twilio.rest import Client
    
def EnviarSMS():
    # AS INFORMACOES DO TWILIO PODE SER ENCONTRADAS DIRETAMENTE NO SITE https://www.twilio.com/
    account_sid = 'ID DO TWILIO'
    auth_token = 'TOKEN DO TWILIO'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body= txtMensagem.get("1.0",'end-1c'),
                        from_= '+19378822818',
                        to= "+55" + txtNumero.get(),
                    )

    print(message.sid)

main = Tk()
main.title('SMS Envio Python')
BACKGROUND = "#8A0868"
main['background'] = BACKGROUND
main.geometry('600x300')

# Define uma grade de 50 x 50 células na janela principal
rows = 0
while rows < 10:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

txtNumero = Entry(main, width=30, font='bold')
txtNumero.insert(0, 'Digite seu Numero')
txtNumero.grid(row=1, column=5, sticky='NS')

txtMensagem = Text(main, width=50, height=7, font='bold')
txtMensagem.insert('0.0', 'Digite sua Mensagem')
txtMensagem.grid(row=3, column=5, sticky='NS')

btnEnviar = Button(main,bg='limegreen', fg='blue', font='bold 12',text='Enviar',command=EnviarSMS)
btnEnviar.grid(row=5, column=5, sticky='NESW')
main.mainloop()


