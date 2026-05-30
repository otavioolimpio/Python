import tkinter as tk
from tkinter import messagebox
# Importa a classe Enigma do seu arquivo enigma.py
from enigma import Enigma

class EnigmaInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Máquina Enigma")
        self.root.geometry("500x550")
        self.root.configure(bg="#2c3e50")

        # Título Principal
        titulo = tk.Label(root, text="MÁQUINA ENIGMA HISTÓRICA", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
        titulo.pack(pady=15)

        # --- SEÇÃO DE CONFIGURAÇÃO DOS ROTORES ---
        frame_config = tk.LabelFrame(root, text=" Configurações de Entrada (Rotores 1-5 e Posições 1-26) ", bg="#2c3e50", fg="#f1c40f", pady=10)
        frame_config.pack(pady=10, padx=20, fill="x")

        # Labels de cabeçalho
        tk.Label(frame_config, text="Rotores (Ex: 5, 4, 1)", bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(frame_config, text="Posições (Ex: 7, 10, 11)", bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=2, padx=10, pady=5)

        # Rotor Esquerdo
        tk.Label(frame_config, text="Rotor Esq:", bg="#2c3e50", fg="#ecf0f1").grid(row=1, column=0, sticky="w")
        self.txt_rot_esq = tk.Entry(frame_config, width=5, justify="center")
        self.txt_rot_esq.insert(0, "5")
        self.txt_rot_esq.grid(row=1, column=1, pady=5)
        self.txt_pos_esq = tk.Entry(frame_config, width=5, justify="center")
        self.txt_pos_esq.insert(0, "7")
        self.txt_pos_esq.grid(row=1, column=2, pady=5)

        # Rotor Central
        tk.Label(frame_config, text="Rotor Cen:", bg="#2c3e50", fg="#ecf0f1").grid(row=2, column=0, sticky="w")
        self.txt_rot_cen = tk.Entry(frame_config, width=5, justify="center")
        self.txt_rot_cen.insert(0, "4")
        self.txt_rot_cen.grid(row=2, column=1, pady=5)
        self.txt_pos_cen = tk.Entry(frame_config, width=5, justify="center")
        self.txt_pos_cen.insert(0, "10")
        self.txt_pos_cen.grid(row=2, column=2, pady=5)

        # Rotor Direito
        tk.Label(frame_config, text="Rotor Dir:", bg="#2c3e50", fg="#ecf0f1").grid(row=3, column=0, sticky="w")
        self.txt_rot_dir = tk.Entry(frame_config, width=5, justify="center")
        self.txt_rot_dir.insert(0, "1")
        self.txt_rot_dir.grid(row=3, column=1, pady=5)
        self.txt_pos_dir = tk.Entry(frame_config, width=5, justify="center")
        self.txt_pos_dir.insert(0, "11")
        self.txt_pos_dir.grid(row=3, column=2, pady=5)

        # --- SEÇÃO DE ENTRADA E SAÍDA DE TEXTO ---
        tk.Label(root, text="Texto de Entrada (Apenas Letras):", bg="#2c3e50", fg="#ecf0f1").pack(anchor="w", padx=20, pady=(10,0))
        self.txt_entrada = tk.Entry(root, font=("Helvetica", 12), width=45)
        self.txt_entrada.insert(0, "MEUNOMEEOTAVIOSOUESTUDANTEDELICENCIATURAEMCOMPUTACAO")
        self.txt_entrada.pack(pady=5, padx=20)

        # Botão de Ação
        btn_processar = tk.Button(root, text="🔒 PROCESSAR TEXTO (Cifrar / Decifrar)", font=("Helvetica", 11, "bold"), bg="#27ae60", fg="white", command=self.processar_enigma)
        btn_processar.pack(pady=15)

        tk.Label(root, text="Resultado (Saída):", bg="#2c3e50", fg="#ecf0f1").pack(anchor="w", padx=20, pady=(10,0))
        self.txt_saida = tk.Entry(root, font=("Helvetica", 12, "bold"), width=45, fg="#d35400", bg="#eee")
        self.txt_saida.pack(pady=5, padx=20)

        # Nota informativa histórica
        nota = tk.Label(root, text="Nota: Como a Enigma é perfeitamente simétrica, o mesmo processo\ne as mesmas configurações servem tanto para codificar quanto decodificar.", 
                        font=("Helvetica", 9, "italic"), bg="#2c3e50", fg="#bdc3c7")
        nota.pack(pady=20)

    def processar_enigma(self):
        try:
            # 1. Coleta e valida os rotores escolhidos
            rotores = [
                int(self.txt_rot_esq.get()),
                int(self.txt_rot_cen.get()),
                int(self.txt_rot_dir.get())
            ]
            
            # 2. Coleta e valida as posições iniciais
            posicoes = [
                int(self.txt_pos_esq.get()),
                int(self.txt_pos_cen.get()),
                int(self.txt_pos_dir.get())
            ]

            # 3. Coleta o texto e trata para maiúsculas (padrão da Enigma)
            texto_puro = self.txt_entrada.get().upper().replace(" ", "")

            # Validação simples para evitar quebras se o usuário digitar números nos rotores fora do escopo
            for r in rotores:
                if r < 1 or r > 5:
                    raise ValueError("Os rotores devem ser de 1 a 5.")

            # 4. Instancia a sua classe Enigma com os dados da tela
            maquina = Enigma(rotores, posicoes)
            
            # 5. Cifra o texto
            resultado = maquina.cifrar_texto(texto_puro)

            # 6. Exibe o resultado no campo de saída
            self.txt_saida.delete(0, tk.END)
            self.txt_saida.insert(0, resultado)

        except ValueError as e:
            messagebox.showerror("Erro de Entrada", f"Por favor, verifique as configurações.\nDetalhe: {e}")
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

# Inicialização da janela principal
if __name__ == "__main__":
    janela = tk.Tk()
    app = EnigmaInterface(janela)
    janela.mainloop()