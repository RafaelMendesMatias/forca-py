import random
import tkinter as tk
from tkinter import messagebox

class JogoDaForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        self.master.geometry("400x300")

        self.palavras = ['python', 'programacao', 'computador', 'algoritmo', 'desenvolvimento']
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_corretas = []
        self.tentativas_restantes = 6

        self.label_palavra = tk.Label(master, text=self.mostrar_palavra_secreta(), font=("Arial", 20))
        self.label_palavra.pack()

        self.label_tentativas = tk.Label(master, text=f"Tentativas restantes: {self.tentativas_restantes}", font=("Arial", 12))
        self.label_tentativas.pack()

        self.entry_letra = tk.Entry(master, font=("Arial", 14))
        self.entry_letra.pack()

        self.botao_jogar = tk.Button(master, text="Jogar", command=self.verificar_letra)
        self.botao_jogar.pack()

    def mostrar_palavra_secreta(self):
        secreto = ''
        for letra in self.palavra_secreta:
            if letra in self.letras_corretas:
                secreto += letra
            else:
                secreto += ' _ '
        return secreto

    def verificar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if letra in self.palavra_secreta:
            self.letras_corretas.append(letra)
            self.label_palavra.config(text=self.mostrar_palavra_secreta())
        else:
            self.tentativas_restantes -= 1
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restantes}")
            if self.tentativas_restantes == 0:
                messagebox.showinfo("Fim de Jogo", f"Game over! A palavra secreta era: {self.palavra_secreta}")
                self.master.destroy()
        
        if '_' not in self.mostrar_palavra_secreta():
            messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era: {self.palavra_secreta}")
            self.master.destroy()

def main():
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()

if __name__ == "__main__":
    main()