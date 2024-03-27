import random
import tkinter as tk
from tkinter import messagebox

class JogoDaForca:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Forca")
        self.master.geometry("500x200")

        self.palavras_dicas = {
            'banana': 'Uma fruta amarela e alongada',
            'computador': 'Dispositivo eletrônico usado para processamento de dados',
            'sorriso': 'Expressão facial que indica felicidade',
            'carro': 'Meio de transporte com quatro rodas',
            'futebol': 'Esporte jogado com uma bola redonda',
            'cachorro': 'Um animal de estimação comum',
            'gato': 'Outro animal de estimação comum',
            'praia': 'Local onde a terra encontra o mar',
            'livro': 'Conjunto de páginas encadernadas',
            'escola': 'Local de aprendizado para crianças',
            'amigo': 'Alguém próximo e querido',
            'sol': 'Estrela que é o centro do nosso sistema solar',
            'lua': 'Satélite natural da Terra',
            'sábado': 'O sexto dia da semana',
            'domingo': 'O sétimo dia da semana',
            'leão': 'Um grande felino',
            'filme': 'Obra cinematográfica',
            'pipoca': 'Lanche comum em cinemas',
            'coração': 'Órgão vital do corpo humano',
            'chocolate': 'Doce feito do cacau',
            'bicicleta': 'Veículo de duas rodas impulsionado por pedais',
            'esporte': 'Atividade física competitiva',
            'música': 'Combinação de sons harmoniosos',
            'piano': 'Instrumento musical de teclas',
            'guitarra': 'Instrumento musical de cordas',
            'cama': 'Móvel para dormir',
            'sonho': 'Experiência mental durante o sono',
            'viagem': 'Jornada para um lugar distante',
            'aventura': 'Experiência emocionante e arriscada',
            'família': 'Grupo de pessoas relacionadas por laços sanguíneos ou afetivos',
            'trabalho': 'Atividade realizada em troca de dinheiro',
            'dinheiro': 'Meio de troca para bens e serviços',
            'felicidade': 'Estado emocional de contentamento',
            'tristeza': 'Estado emocional de melancolia',
            'amor': 'Sentimento profundo de afeição',
            'ódio': 'Sentimento de aversão intenso',
            'chuva': 'Precipitação de água do céu',
            'vento': 'Movimento do ar',
            'verão': 'Estação do ano caracterizada por dias quentes',
            'inverno': 'Estação do ano caracterizada por dias frios',
            'outono': 'Estação do ano caracterizada por queda de folhas',
            'primavera': 'Estação do ano caracterizada pelo florescimento das plantas',
            'café': 'Bebida quente feita de grãos torrados',
            'chá': 'Bebida quente ou gelada feita da infusão de folhas',
        }
        self.palavras_disponiveis = list(self.palavras_dicas.keys())

        self.novo_jogo()

    def novo_jogo(self):
        # Limpa a interface gráfica removendo todos os widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Verifica se há palavras disponíveis
        if not self.palavras_disponiveis:
            messagebox.showinfo("Fim de Jogo", "Você esgotou todas as palavras disponíveis.")
            self.master.destroy()
            return

        self.palavra_secreta = random.choice(self.palavras_disponiveis)
        self.palavras_disponiveis.remove(self.palavra_secreta)
        
        self.letras_corretas = []
        self.tentativas_restantes = 6

        self.label_palavra = tk.Label(self.master, text=self.mostrar_palavra_secreta(), font=("Arial", 20))
        self.label_palavra.pack()

        self.label_tentativas = tk.Label(self.master, text=f"Tentativas restantes: {self.tentativas_restantes}", font=("Arial", 12))
        self.label_tentativas.pack()

        self.entry_letra = tk.Entry(self.master, font=("Arial", 14))
        self.entry_letra.pack()

        self.botao_jogar = tk.Button(self.master, text="Jogar", command=self.verificar_letra)
        self.botao_jogar.pack()

        self.botao_chutar = tk.Button(self.master, text="Chutar", command=self.chutar_palavra)
        self.botao_chutar.pack()

        self.frame_alfabeto = tk.Frame(self.master)
        self.frame_alfabeto.pack()

        self.letras_tentadas = []

        for letra in "abcdefghijklmnopqrstuvwxyz":
            button = tk.Button(self.frame_alfabeto, text=letra.upper(), command=lambda l=letra: self.tentar_letra(l))
            button.grid(row=0, column=ord(letra) - ord('a'))

        self.botao_dica = tk.Button(self.master, text="Dica", command=self.exibir_dica)
        self.botao_dica.pack()

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
        self.tentar_letra(letra)

    def tentar_letra(self, letra):
        if letra in self.letras_tentadas:
            messagebox.showinfo("Aviso", f"A letra '{letra}' já foi tentada.")
            return

        self.letras_tentadas.append(letra)

        if letra in self.palavra_secreta:
            self.letras_corretas.append(letra)
            self.label_palavra.config(text=self.mostrar_palavra_secreta())
        else:
            self.tentativas_restantes -= 1
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restantes}")
            if self.tentativas_restantes == 0:
                self.finalizar_jogo("Game over! A palavra secreta era: " + self.palavra_secreta)

        if '_' not in self.mostrar_palavra_secreta():
            self.finalizar_jogo("Parabéns! Você venceu! A palavra era: " + self.palavra_secreta)

        self.atualizar_botao(letra)

    def atualizar_botao(self, letra):
        if letra in self.palavra_secreta:
            cor = "green"
        else:
            cor = "red"
        button = self.frame_alfabeto.winfo_children()[ord(letra) - ord('a')]
        button.config(state="disabled", bg=cor)

    def exibir_dica(self):
        dica = self.palavras_dicas[self.palavra_secreta]
        messagebox.showinfo("Dica", dica)

    def chutar_palavra(self):
        palavra_chute = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)
        
        if palavra_chute == self.palavra_secreta:
            self.finalizar_jogo("Parabéns! Você acertou! A palavra era: " + self.palavra_secreta)
        else:
            self.finalizar_jogo("Você errou! A palavra secreta era: " + self.palavra_secreta)

    def finalizar_jogo(self, mensagem):
        resposta = messagebox.askquestion("Fim de Jogo", mensagem + "\nDeseja jogar novamente?")
        if resposta == 'yes':
            self.novo_jogo()
        else:
            self.master.destroy()

def main():
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()

if __name__ == "__main__":
    main()