import os

class Enigma:
    # Construtor da classe
    def __init__(self, selecao_rotores, posicoes_iniciais):
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # 1. Banco de dados dos 5 rotores históricos (Fiação e a letra de "Notch"/Entalhe)
        # O 'notch' é a letra que, ao ser alcançada, força o próximo rotor a girar.
        self.banco_rotores = {
            1: {"fio": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "notch": "Q"}, # Rotor I
            2: {"fio": "AJDKSIRUXBLHWTMCQGZNPYFVOE", "notch": "E"}, # Rotor II
            3: {"fio": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "notch": "V"}, # Rotor III
            4: {"fio": "ESOVPZJAYQUIRHXLNFTGKDCMWB", "notch": "J"}, # Rotor IV
            5: {"fio": "VZBRGITYUPSDNHLXAWMJQOFECK", "notch": "Z"}  # Rotor V
        }

        # Refletor
        self.refletor = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

        # 2. Configurar os 3 rotores escolhidos
        self.r_esq = self.banco_rotores[selecao_rotores[0]]
        self.r_cen = self.banco_rotores[selecao_rotores[1]]
        self.r_dir = self.banco_rotores[selecao_rotores[2]]

        # 3. Definir posições iniciais (convertendo de 1-26 para índices 0-25)
        self.pos_esq = posicoes_iniciais[0] - 1
        self.pos_cen = posicoes_iniciais[1] - 1
        self.pos_dir = posicoes_iniciais[2] - 1

    def girar_rotores(self):
        """
        Simula a mecânica real de giro dos rotores, incluindo o
        comportamento de 'double-stepping' (dupla rotação) do rotor central.
        """
        # Verifica se os rotores estão nas posições de "notch" (entalhe)
        notch_dir = self.alfabeto[self.pos_dir] == self.r_dir["notch"]
        notch_cen = self.alfabeto[self.pos_cen] == self.r_cen["notch"]

        # Regra de avanço da Enigma:
        # 1. O rotor do centro avança se ele mesmo estiver no notch (Double-stepping)
        #    OU se o rotor da direita avançar e engrenar nele.
        # 2. O rotor da esquerda avança se o do centro estiver no notch.
        # 3. O rotor da direita SEMPRE avança a cada tecla.

        if notch_cen:
            self.pos_esq = (self.pos_esq + 1) % 26
            self.pos_cen = (self.pos_cen + 1) % 26
        elif notch_dir:
            self.pos_cen = (self.pos_cen + 1) % 26

        self.pos_dir = (self.pos_dir + 1) % 26

    def passar_pelo_rotor(self, indice, fiação_rotor, posicao, reverso=False):
        # Passa o sinal elétrico por um rotor considerando sua rotação atual.
        # Deslocamento de entrada
        shift_in = (indice + posicao) % 26

        if not reverso:
            letra_saida = fiação_rotor[shift_in]
            indice_saida = self.alfabeto.index(letra_saida)
        else:
            letra_entrada = self.alfabeto[shift_in]
            indice_saida = fiação_rotor.index(letra_entrada)

        # Deslocamento de saída
        return (indice_saida - posicao) % 26

    def cifrar_letra(self, letra):
        if letra not in self.alfabeto:
            return letra # Proteção caso passe um caractere inválido

        # Os rotores giram ANTES do sinal elétrico passar
        self.girar_rotores()

        # Índice numérico da letra (A=0, B=1...)
        idx = self.alfabeto.index(letra)

        # --- CAMINHO DE IDA (Direita -> Centro -> Esquerda) ---
        idx = self.passar_pelo_rotor(idx, self.r_dir["fio"], self.pos_dir)
        idx = self.passar_pelo_rotor(idx, self.r_cen["fio"], self.pos_cen)
        idx = self.passar_pelo_rotor(idx, self.r_esq["fio"], self.pos_esq)

        # --- REFLETOR ---
        letra_refletida = self.refletor[idx]
        idx = self.alfabeto.index(letra_refletida)

        # --- CAMINHO DE VOLTA (Esquerda -> Centro -> Direita) ---
        idx = self.passar_pelo_rotor(idx, self.r_esq["fio"], self.pos_esq, reverso=True)
        idx = self.passar_pelo_rotor(idx, self.r_cen["fio"], self.pos_cen, reverso=True)
        idx = self.passar_pelo_rotor(idx, self.r_dir["fio"], self.pos_dir, reverso=True)

        return self.alfabeto[idx]

    def cifrar_texto(self, texto):
        return "".join(self.cifrar_letra(letra) for letra in texto)