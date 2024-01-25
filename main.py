from tkinter import *
from tkinter import ttk
from tkinter import messagebox



alunos = [
    {
        "matricula": 1,
        "nome": "Jonas Lopes",
        "idade": 18,
        "curso": "Javascript",
        "novato": "Não"
    }
]

matricula_atual = 1
index = 0

def atualizarTabela() -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)

    for aluno in alunos:
        tabela.insert("", END, values=(aluno["matricula"],
                                       aluno["nome"],
                                       aluno["idade"],
                                       aluno["curso"],
                                       aluno["novato"]))
def adicionarAluno() -> None:
    global matricula_atual
    matricula_atual += 1
    nome = texNome.get()
    idade = int(texIdade.get())
    curso = comboCursos.get()
    if opcao.get() == True:
        novato = "Sim"
    else:
        novato = "Não"

    aluno = {
        "matricula": matricula_atual,
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "novato": novato
    }
    messagebox.showinfo("Sucesso!", "Aluno adicionado com sucesso!")
    alunos.append(aluno)
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    texNome.delete(0, END)
    texIdade.delete(0, END)
    comboCursos.set("")
    opcao.set(False)

def preencherCampos(event) -> None:
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada)
    aluno = alunos[index]
    limparCampos()
    texMatricula.config(state=NORMAL)
    texMatricula.insert(END, str(aluno["matricula"]))
    texMatricula.config(state=DISABLED)
    texNome.insert(END, aluno["nome"])
    texIdade.insert(END, str(aluno["idade"]))
    comboCursos.set(aluno["curso"])


janela = Tk()

janela.title("Alunos - infinity")


labelMatricula = Label(janela, text="Matricula:", font="Tahoma 18 bold", fg="red")
labelMatricula.grid(row=0, column=0)
labelNome = Label(janela, text="Nome:", font="Tahoma 18 bold", fg="red")
labelNome.grid(row=1, column=0)
labelIdade = Label(janela, text="Idade:", font="Tahoma 18 bold", fg="red")
labelIdade.grid(row=2, column=0)
labelCurso = Label(janela, text="Curso:", font="Tahoma 18 bold", fg="red")
labelCurso.grid(row=3, column=0)
labelNovato = Label(janela, text="Novato?", font="Tahoma 18 bold", fg="red")
labelNovato.grid(row=4, column=0)

texMatricula = Entry(janela, font="Tahoma 18", width=26, state=DISABLED)
texMatricula.grid(row=0, column=1)
texNome = Entry(janela, font="Tahoma 18", width=26)
texNome.grid(row=1, column=1)
texIdade = Entry(janela, font="Tahoma 18", width=26)
texIdade.grid(row=2, column=1)


cursos = ["Javascript", "Python", "React", "NodeJs"]
comboCursos = ttk.Combobox(janela, font="Tahoma 18", values=cursos, width=24)
comboCursos.grid(row=3, column=1, sticky=W)

opcao = BooleanVar(value=False)
checkNovato = ttk.Checkbutton(janela, width=26, variable=opcao)
checkNovato.grid(row=4, column=1, sticky=W)

btnAdicionar = Button(janela, text="Adicionar", font="Tahoma 16", fg="red", height=1, command=adicionarAluno)
btnAdicionar.grid(row=5, column=0)
btnEditar = Button(janela, text="Editar", font="Tahoma 16", fg="red", height=1)
btnEditar.grid(row=5, column=1)
btnExcluir = Button(janela, text="Excluir", font="Tahoma 16", fg="red", height=1)
btnExcluir.grid(row=5, column=2)
btnPdf = Button(janela, text="Salvar PDF", font="Tahoma 16", fg="red", height=1)
btnPdf.grid(row=7, column=1)
btnImprimir = Button(janela, text="Imprimir", font="Tahoma 16", fg="red", height=1)
btnImprimir.grid(row=7, column=2)

colunas = ["Matricula", "Nome", "Idade", "Curso", "Novato"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=110)
tabela.grid(row=6, columnspan=3)
tabela.bind("<ButtonRelease-1>", preencherCampos)

atualizarTabela()
janela.mainloop()