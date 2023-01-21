import requests
from tkinter import *

cor01= "#4682B4"  #azul marinho
cor02= "#F8F8FF"  #Ghostwhite

window = Tk()
window.title('Chuck will tell you!')


chuckimg = PhotoImage(file="imagem/chuckimg.png")
chuckimg = chuckimg.subsample(3,3)

figural = Label(image=chuckimg)



def norris():
    requerimento = requests.get('https://api.chucknorris.io/jokes/random')
    requerimento_dic = requerimento.json()

    

    print(requerimento_dic)    
    texto_live['text'] = requerimento_dic['value']

figural.grid(row = 0, column=0, padx=50, pady=0)

texto_orientacao = Label(window, text = "Search for Wisdom")
texto_orientacao.grid(column=0, row=1, padx=10, pady=10)

texto_orientacao2 = Label(window, text = "whit the master Chuck Norris!")
texto_orientacao2.grid(column=0, row=2, padx=10, pady=10)

botao01 = Button(window, text= "SEARCH NORRIS!", command= norris)
botao01.grid(column=0, row=3, padx=10, pady=10)

texto_live = Label(window, text='')
texto_live.grid(column=0, row=4)




window.mainloop()
