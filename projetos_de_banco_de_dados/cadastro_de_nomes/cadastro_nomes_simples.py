import tkinter as tk
from tkinter import messagebox

#===================================================================
#manipulação de dados. (pesquisar mais sobre tkinter. linha #10, 18, 22 e 24 com erros, não estão com atribuição.)

#erros corrigidos mas a linha 26 e 33 ainda não estão atribuídas... :C

banco_d_dados = {}

def adicionar_usuario():
    usuario = entry_nome.get().strip
    if usuario in banco_d_dados:
        messagebox.showerror('Erro!', 'Nome de usuário já existe. Escolha outro.')
    elif usuario == '':
        messagebox.showwarning('Atenção!', 'A área de nome de usuário está vazia.')
    else:
        banco_d_dados[usuario] = 'Usuário cadastrado.'
        messagebox.showinfo('Sucesso!', f'Usuário "{usuario}" cadastrado.')
        entry_nome.delete(0, tk.END)


def alterar_usuario():
    usuario = entry_nome.get().strip
    if usuario in banco_d_dados:
        novo_usuario = entry_novo_nome.get().strip()
        if novo_usuario == '':
            messagebox.showwarning('Atenção!','A área de nome de usuário está vazia.' )
        elif novo_usuario in banco_d_dados:
            messagebox.showerror('Erro!', 'O novo nome de usuário já existe. Escolha outro.')
        else:
            banco_d_dados[novo_usuario] = banco_d_dados.pop(usuario)
            messagebox.showinfo('Sucesso!', f'Nome de usuário alterado para "{novo_usuario}"')
            entry_nome.delete(0, tk.END)
            entry_novo_nome.delete(0, tk.END)
    else:
        messagebox.showerror('Erro!', 'Nome de usuário não encontrado.')

def visualizar_usuario():
    if banco_d_dados:
        usuarios = '\n'.join(banco_d_dados.keys())
        messagebox.showinfo('Usuários Cadastrados', usuarios)
    else:
        messagebox.showinfo('Nenhum Usuário', 'Nenhum usuário cadastrado.')

def excluir_usuario():
    usuario = entry_nome.get().strip()
    if usuario in banco_d_dados:
        del banco_d_dados[usuario]
        messagebox.showinfo('Sucesso!', f'Usuário "{usuario}" excluído.')
        entry_nome.delete(0, tk.END)
    else:
        messagebox.showerror('Erro!', 'Nome de usuário não encontrado.')

#===================================================================

#criação de anela principal, labels,. entrys, botoões, etc

root = tk.Tk()
root.title('Sistema de Cadastro de Usuários')

label_nome = tk.Label(root, text='Nome de usuário:')
label_nome.grid(row=0, column=0, padx=10, pady=5)

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_novo_nome = tk.Label(root, text='Novo Nome (para alteração):')
label_novo_nome.grid(row=1, column= 0, padx=10, pady=5)

entry_novo_nome = tk.Entry(root)
entry_novo_nome.grid(row=1, column=1, padx=10, pady=5)

btn_adicionar = tk.Button(root, text='Adicionar Usuário', command=adicionar_usuario)
btn_adicionar.grid(row=2, column=0, padx=10, pady=5)

btn_alterar = tk.Button(root, text='Alterar Usuário', command=alterar_usuario)
btn_alterar.grid(row=2, column=1, padx=10, pady=5)

btn_visualizar = tk.Button(root, text='Visualizar Usuários', command=visualizar_usuario)
btn_visualizar.grid(row=3, column=0, padx=10, pady=5)

btn_excluir = tk.Button(root, text='Excluir Usuário', command=excluir_usuario)
btn_excluir.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
