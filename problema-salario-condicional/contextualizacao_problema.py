from tkinter import Entry, Tk, Label, Button


def checka_salario():
    salario = int(salario_entrada.get())
    salario_minimo = 1200
    mensagem = ""

    if salario < salario_minimo:
        mensagem = "Seu salário tá abaixo do minimo"
    elif salario == salario_minimo:
        mensagem = "Seu salário é igual ao salário mínimo"
    else:
        mensagem = "Seu salário é maior do que o salário minimo"
    label_resultado.configure(text=mensagem)


janela = Tk()
janela.title('Checagem de Salário - v1.0')
janela.geometry("600x400")

quanto_eh_seu_salario_label = Label(
    janela, text="Quanto é seu salário?", font=("Arial", 18)
)
quanto_eh_seu_salario_label.place(x=180, y=100)


salario_label = Label(janela, text="Salário: ")
salario_label.place(x=240, y=160)

salario_entrada = Entry(janela, width=20)
salario_entrada.place(x=240, y=180)

check_salario_button = Button(
    janela, text="checar", bg="#87CEEB", width=16, command=checka_salario
)
check_salario_button.place(x=240, y=220)

label_resultado = Label(janela, text="")
label_resultado.place(x=240, y=260)

janela.mainloop()
