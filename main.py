from tkinter import*
from tkinter import StringVar, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import backend
import os
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def carregar_imagem(nome_arquivo, tamanho=None):
    """Carrega imagem da pasta /img e retorna um PhotoImage redimensionado."""
    caminho = os.path.join(BASE_DIR, "img", nome_arquivo)
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")
    img = Image.open(caminho)
    if tamanho:
        img = img.resize(tamanho)
    return ImageTk.PhotoImage(img)





# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

janela = Tk()
janela.title("")
janela.geometry('820x610')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# dividindo a janela
frameCima = Frame(janela, width=1043, height=50, bg=co1)
frameCima.grid(row=0, column=0)    

frameMeio = Frame(janela, width=1043, height=290, bg=co1, padx=10)
frameMeio.grid(row=1, column=0)

frame_esquerdo = Frame(frameMeio, width=250, height=290, bg=co9, pady=0, relief='raised')
frame_esquerdo.place(x=0, y=5)

frame_direito = Frame(frameMeio, width=630, height=290, bg=co1, pady=0)
frame_direito.place(x=250, y=5)

frameBaixo = Frame(janela, width=820, height=300, bg=co1)
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

#logo
app_ = Label(frameCima, text="Orçamento de viagem", compound=LEFT, padx=5, anchor=NW, font=('Verdana 20'), bg=co1, fg=co4)
app_.place(x=0, y=0)


# Caminho base do arquivo main.py

app_img = carregar_imagem("log.png", (45, 45))
app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=320, y=0)


#frame esquerdo

def Totais():
    l_nome = Label(frame_esquerdo, text="Meu orçamento e despesas", width=31, anchor=NW, font=('Verdana 10'), bg=co3, fg=co1)
    l_nome.place(x=0, y=0)

#Orçamento total
l_orcamento = Label(frame_esquerdo, text="Orçamento total:", width=31, anchor=NW, font=('Verdana 10'), bg=co9, fg=co4)
l_orcamento.place(x=5, y=40)
e_orcamento = Entry(frame_esquerdo, width=15, font=('Verdana 10'), justify='left', bg=co1, fg=co4)
e_orcamento.place(x=5, y=70)

#Despesas totais
l_despesas = Label(frame_esquerdo, text="Despesas totais:", width=20, anchor=NW, font=('Verdana 10'), bg=co9, fg=co4)
l_despesas.place(x=5, y=110)
e_despesas = Entry(frame_esquerdo, width=15, font=('Verdana 10'), justify='left', bg=co1, fg=co4)
e_despesas.place(x=5, y=140)

#Saldo final
l_saldo = Label(frame_esquerdo, text="Saldo final:", width=20, anchor=NW, font=('Verdana 10'), bg=co9, fg=co4)
l_saldo.place(x=5, y=180)
e_saldo = Entry(frame_esquerdo, width=15, font=('Verdana 10'), justify='left', bg=co1, fg=co4)
e_saldo.place(x=5, y=210)

#gráfico
def grafico():
    figura = plt.Figure(figsize=(7,4), dpi=87)
    ax = figura.add_subplot(111)
    
    lista_valores = [56,8,5,2]
    lista_categorias = ['Transporte','Hospedagem','Alimentação','Lazer']
    
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc='center right', bbox_to_anchor=(1.55, 0.50))

#frame para pie 
    frame_meio_pie = Frame(frame_direito,width=600, height=290,bg=co11, pady=0, relief="raised")
    frame_meio_pie.place(x=-140, y=-25)
    l_nome = Label(frame_direito, text="Para onde estão indo minhas despesas totais?", width=60,anchor=CENTER,padx=2, font=('Verdana 10 '), bg=co10, fg=co1)
    l_nome.place(x=0, y=0)

    canva_categoria = FigureCanvasTkAgg(figura, frame_meio_pie)
    canva_categoria.get_tk_widget().grid(row=0,column=0,padx=0)

#frame para tabela
l_nome = Label(frameBaixo, text="Quais são as suas despesas", width=87, anchor=NW, padx=6, font=('Verdana 11'), bg=co10, fg=co1)  
l_nome.grid(row=0, column=0, pady=0, columnspan=6)

frame_tabela = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_tabela.grid(row=1, column=0, pady=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=1, column=1, pady=0, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_configuracao.grid(row=1, column=2, pady=0, padx=5)

#função mostrar renda
def mostrar_renda():
    
    tabela_head = ['id','Tipo','Descrição','Total']

    lista_itens = [['1','Transporte','Combustível e pedágios',150.00],]

    global tree
    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky=NSEW)
    vsb.grid(column=1, row=0, sticky=NS)
    hsb.grid(column=0, row=1, sticky=EW)

    hd=["nw","nw","center", "e", "e"]  
    h = [20, 90, 120, 80, 70]
    n=0 

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

#funções banco de dados

def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)

    dados = backend.listar()
    for item in dados:
        tree.insert('', 'end', values=item)

def atualizar_totais():
    total_despesas = backend.total()
    e_despesas.delete(0, 'end')
    e_despesas.insert(0, f"R$ {total_despesas:.2f}")

    try:
        orcamento_texto = e_orcamento.get().replace("R$", "").strip()
        orcamento = float(orcamento_texto)
    except ValueError:
        orcamento = 0.0

    saldo = orcamento - total_despesas
    e_saldo.delete(0, 'end')
    e_saldo.insert(0, f"R$ {saldo:.2f}")

def adicionar_despesa():
    categoria = combo_categoria_despesas.get()
    descricao = e_descricao.get()
    valor = e_valor_despesas.get()

    if categoria == "" or descricao == "" or valor == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos antes de adicionar.")
        return

    try:
        valor = float(valor)
        backend.inserir(categoria, descricao, valor)
        e_descricao.delete(0, 'end')
        e_valor_despesas.delete(0, 'end')
        atualizar_tabela()
        atualizar_grafico()
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "O valor deve ser numérico.")

def deletar_despesa():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Atenção", "Selecione um item para deletar.")
        return

    id_item = tree.item(item_selecionado)['values'][0]
    backend.deletar(id_item)
    atualizar_tabela()
    atualizar_grafico()
    messagebox.showinfo("Sucesso", "Despesa excluída com sucesso!")

# Atualizar o valor do orçamento total

def atualizar_orcamento():
    novo_valor = e_valor_quantia.get()
    try:
        valor = float(novo_valor)
        backend.atualizar_orcamento(valor)
        e_valor_quantia.delete(0, 'end')

        # Atualiza o campo do orçamento total na lateral esquerda
        e_orcamento.delete(0, 'end')
        e_orcamento.insert(0, f"R$ {valor:.2f}")

        # Atualiza também os totais e o gráfico
        atualizar_totais()
        atualizar_grafico()

        messagebox.showinfo("Sucesso", "Orçamento atualizado com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")


def atualizar_grafico():
    # Atualiza o gráfico com base nos dados atuais do banco
    dados = backend.listar()
    categorias = {}
    for _, categoria, _, valor in dados:
        categorias[categoria] = categorias.get(categoria, 0) + valor

    if not categorias:
        return

    figura = plt.Figure(figsize=(7, 4), dpi=87)
    ax = figura.add_subplot(111)
    lista_categorias = list(categorias.keys())
    lista_valores = list(categorias.values())
    explode = [0.05] * len(lista_categorias)
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
    ax.legend(lista_categorias, loc='center right', bbox_to_anchor=(1.55, 0.50))

    frame_meio_pie = Frame(frame_direito, width=600, height=290, bg=co11, pady=0, relief="raised")
    frame_meio_pie.place(x=-140, y=-25)
    l_nome = Label(frame_direito, text="Para onde estão indo minhas despesas totais?", width=60, anchor=CENTER, padx=2, font=('Verdana 10 '), bg=co10, fg=co1)
    l_nome.place(x=0, y=0)

    canva_categoria = FigureCanvasTkAgg(figura, frame_meio_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0, padx=0)

def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)

    dados = backend.listar()
    for item in dados:
        tree.insert('', 'end', values=item)
    
    atualizar_totais()
mostrar_renda()

#configurações despesas
l_info = Label(frame_operacoes, text="Insira novas despesas", anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

l_categoria = Label(frame_operacoes, text="Categoria:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

#definindo categorias
categorias = ['Transporte','Hospedagem','Alimentação','Lazer','Outros']
combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=12, font=('Ivy 10'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=80, y=41)

l_descricao = Label(frame_operacoes, text="Descrição:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frame_operacoes, width=16, font=('Ivy 10'), justify='left', relief='solid', bg=co1, fg=co4)
e_descricao.place(x=80, y=71)

l_valor_quantia = Label(frame_operacoes, text="Valor:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_valor_quantia.place(x=10, y=120)
e_valor_despesas = Entry(frame_operacoes, width=16, font=('Ivy 10'), justify='left', relief='solid', bg=co1, fg=co4)
e_valor_despesas.place(x=80, y=121)

#botão inserir 
img_add_despesas = carregar_imagem('add.png', (17, 17))
botao_inserir_despesas = Button(
    frame_operacoes, text="  Adicionar".upper(), image=img_add_despesas,
    width=94, compound=LEFT, anchor=NW, font=('Ivy 7 bold'),
    bg=co1, fg=co0, relief=RAISED, overrelief=RIDGE,
    command=adicionar_despesa
)

botao_inserir_despesas.place(x=80, y=151)

#configurações quantia total
l_descricao = Label(frame_configuracao, text="Atualizar Valor disponível", anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=10)

l_valor_quantia = Label(frame_configuracao, text="Novo valor:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_valor_quantia.place(x=10, y=40)
e_valor_quantia = Entry(frame_configuracao, width=14, font=('Ivy 10'), justify='left', relief='solid', bg=co1, fg=co4)
e_valor_quantia.place(x=110, y=41)

#botao atualizar
img_update_quantia = carregar_imagem('update.png', (17, 17))
botao_inserir_quantia = Button(
    frame_configuracao,
    text="  Atualizar".upper(),
    image=img_update_quantia,
    width=80,
    compound=LEFT,
    anchor=NW,
    font=('Ivy 7 bold'),
    bg=co1,
    fg=co0,
    relief=RAISED,
    overrelief=RIDGE,
    command=atualizar_orcamento
)
botao_inserir_quantia.place(x=110, y=70)

#operação excluir
img_delete_quantia = carregar_imagem('delete.png', (17, 17))
botao_delete_quantia = Button(
    frame_configuracao, text="  Deletar".upper(), image=img_delete_quantia,
    width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'),
    bg=co1, fg=co0, relief=RAISED, overrelief=RIDGE,
    command=deletar_despesa
)
botao_delete_quantia.place(x=110, y=120)



# Preencher campo de orçamento com o valor salvo no banco
orcamento_salvo = backend.pegar_orcamento()
e_orcamento.insert(0, str(orcamento_salvo))


grafico()
Totais()
style.theme_use("clam")
style.configure("Treeview",highlightthickness=0, bd=0, font=('Calibri', 9))
atualizar_tabela()
atualizar_grafico()
janela.mainloop()
