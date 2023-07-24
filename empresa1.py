valor_fixo = 12448.31
valor_HE = 45.47
horas_fixas = 200

def horas_extras_total(horas):
    het= horas * valor_HE
    return het

def final(valor1, valor2):
    final = valor1 + valor2
    return final

def imposto_647(final):
    imposto_1 = final * 0.015
    return imposto_1

def imposto_cont(final_2):
    imposto_2 = final_2 * 0.0465
    return imposto_2

def mod_horas(horas, minutos):
    hora_m = horas + (minutos / 60)
    return hora_m

horas = int(input("Ingrese as horas extras sem os minutos: "))
minutos = int(input("Ingrese os minutos: "))
hrm = mod_horas(horas, minutos)

horas_extras = horas_extras_total(hrm)

valor_neto = final(horas_extras, valor_fixo)

calc_imp_1 = imposto_647(valor_neto)

calc_imp_2 = imposto_cont(valor_neto)

liquido = valor_neto - (calc_imp_1 + calc_imp_2)

horas_trabalhadas = int(horas_fixas + hrm)

print(f'''
    Horas trabalhadas no mes {horas_trabalhadas}
    Total de Horas extras R$ {horas_extras}
    Valor Bruto R$ {valor_neto}
    Imposto Art. 647 R$ {calc_imp_1: .2f}
    Imposto Contable R$ {calc_imp_2: .2f}
    Valor liquido R$ {liquido: .2f}
    ''')