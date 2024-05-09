import os
import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Frame, Checkbutton, IntVar, Scrollbar, Canvas

class ExcelFilterApp:
    def __init__(self, master):
        self.master = master
        master.title("nLOGxtractor by forense.io")
        master.geometry("800x570")  # Ajuste do tamanho da janela
        master.configure(bg='gray')  # Cor de fundo cinza

        self.frame = Frame(master, bg='gray')
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Label e Entry na mesma linha
        self.label = Label(self.frame, text="Selecione o arquivo (xlsx):", bg='gray', fg='white', font=("Helvetica", 12))
        self.label.grid(row=0, column=0, sticky='w', padx=(0, 10))
        
        self.entry = Entry(self.frame, width=58, state='readonly', font=("Helvetica", 10))
        self.entry.grid(row=0, column=1, sticky='ew')

        # Botão Procurar
        self.browse_button = Button(self.frame, text="Procurar", command=self.browse_file, font=("Helvetica", 12,"bold"), bg='black', fg='white', height=1, width=12)
        self.browse_button.grid(row=0, column=2, padx=10, sticky='ew')

        # Scrollable Canvas for Checkbuttons
        self.canvas = Canvas(self.frame, borderwidth=0, background="#ffffff")
        self.vsb = Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=1, column=3, sticky='ns', pady=(20, 0))
        self.canvas.grid(row=1, column=0, columnspan=3, sticky='nsew', pady=(20, 0))
        
        self.inner_frame = Frame(self.canvas, bg='white')
        self.canvas.create_window((4,4), window=self.inner_frame, anchor="nw", width=740)
        self.inner_frame.bind("<Configure>", self.on_frame_configure)

        # Status box
        self.status_box = Label(self.frame, text="Status: Aguardando arquivo...", bg='gray', fg='white', font=("Helvetica", 10))
        self.status_box.grid(row=3, column=0, columnspan=3, sticky='ew', pady=(10, 0))

       # Botão Executar - ajustado para ter o mesmo tamanho do botão Procurar
        self.execute_button = Button(self.frame, text="Executar", command=self.filter_excel, font=("Helvetica", 12, "bold"), bg='black', fg='white', height=2, width=10)
        self.execute_button.grid(row=4, column=0, columnspan=3, pady=20, sticky='ew')

        # Botão Sair - ajustado para ter o mesmo tamanho do botão Procurar
        self.exit_button = Button(self.frame, text="Sair", command=self.master.quit, font=("Helvetica", 12, "bold"), bg='black', fg='white', height=2, width=1)
        self.exit_button.grid(row=5, column=0, columnspan=3, sticky='ew')


        # Footer label
        self.footer_label = Label(self.frame, text="nLOGxtractor by forense.io", bg='gray', fg='white', font=("Helvetica", 8, "bold"))
        self.footer_label.grid(row=6, column=0, columnspan=3, sticky='ew', pady=(10, 5))

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def browse_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
        if self.filename:
            self.entry.config(state='normal')
            self.entry.delete(0, "end")
            self.entry.insert(0, self.filename)
            self.entry.config(state='readonly')
            self.show_processing()
            self.load_eventids()

    def show_processing(self):
        self.status_box.config(text="Status: Processando...")

    def load_eventids(self):
        try:
            df = pd.read_excel(self.filename)
            self.event_ids = df['EventId'].unique()
            self.check_vars = {}
            for widget in self.inner_frame.winfo_children():
                widget.destroy()
            for event_id in self.event_ids:
                var = IntVar()
                chk = Checkbutton(self.inner_frame, text=str(event_id), variable=var, bg='white')
                chk.pack(anchor='w')
                self.check_vars[event_id] = var
            self.status_box.config(text="Status: Arquivo carregado. Selecione os EventIDs.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar arquivo: {e}")
            self.status_box.config(text="Status: Erro ao carregar arquivo.")

    def filter_excel(self):
        if not self.filename:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo!")
            return

        try:
            df = pd.read_excel(self.filename)
            selected_ids = [id for id, var in self.check_vars.items() if var.get() == 1]
            if not selected_ids:
                messagebox.showinfo("Informação", "Nenhum EventID selecionado. Operação de filtro cancelada.")
                return
            filtered_df = df[df['EventId'].isin(selected_ids)]

            output_file_name = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])
            filtered_df.to_excel(output_file_name, index=False)
            messagebox.showinfo("Sucesso", f"Os dados filtrados foram escritos em {output_file_name}")

            # Reset do programa para nova execução
            self.reset_application()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao filtrar dados: {e}")

    def reset_application(self):
        self.entry.config(state='normal')
        self.entry.delete(0, "end")
        self.entry.config(state='readonly')
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        self.browse_button.config(state='normal')
        self.status_box.config(text="Status: Aguardando arquivo...")

if __name__ == "__main__":
    root = Tk()
    app = ExcelFilterApp(root)
    root.mainloop()

