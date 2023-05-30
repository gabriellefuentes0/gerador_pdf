# Biblioteca FPDF
# Instale a biblioteca exe: pip intall FPDF

from fpdf import FPDF 

# Pojeto
# Gravando Dados

projeto = input("Digite o nome do projeto:")
horas_estimadas = input("Digite o total de horas estimadas:")
valor_horas = input("Digite o total de horas trabalhadas:")
prazo = input("Digite o prazo estimado:")

# Cálculo

valor_total = int(horas_estimadas) * int(valor_horas)

# Gerador FPDF

pdf = FPDF()

pdf.add_page()
pdf.add_font("Arial")
pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_horas)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")