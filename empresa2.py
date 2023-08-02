valor_fixo = 58838.85
valor_HE_SEM = 125.00
valor_HE_FDS = 130.00

def horas_extras_semanais(horas):
    het= horas * valor_HE_SEM
    return het
    
def horas_extras_sabatinas(horas):
    het1= horas * valor_HE_FDS
    return het1

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

horas_hrs = int(input("Ingrese as horas extras de semanais sem os minutos ou digite 0: "))
minutos_hrs = int(input("Ingrese os minutos semanais ou digite 0: "))
hrs = mod_horas(horas_hrs, minutos_hrs)

horas_hrf = int(input("Ingrese as horas extras de Final de Semana sem os minutos ou digite 0: "))
minutos_hrf = int(input("Ingrese os minutos de Final de Semana ou digite 0: "))
hrf = mod_horas(horas_hrf, minutos_hrf)

horas_trabalhadas = int(horas_hrf + horas_hrs)
minutos_trab = minutos_hrs + minutos_hrf

if minutos_trab > 60:
    hh1 = int(minutos_trab / 60)
    mm1 = int(minutos_trab % 60)

horas_extras_1 = horas_extras_semanais(hrs)
horas_extras_2 = horas_extras_sabatinas(hrf)
horas_extras = horas_extras_1 + horas_extras_2 

valor_neto = final(horas_extras, valor_fixo)

calc_imp_1 = imposto_647(valor_neto)

calc_imp_2 = imposto_cont(valor_neto)

liquido = valor_neto - (calc_imp_1 + calc_imp_2)

htotal = horas_trabalhadas + hh1

print(f'''
    Total horas extras trabalhadas no mes {htotal}{":"}{mm1}
    Total de Horas extras semanais R$ {horas_extras_1: .2f}
    Total de Horas extras sabatinas R$ {horas_extras_2: .2f}
    Valor Bruto R$ {valor_neto: .2f}
    Imposto Art. 647 R$ {calc_imp_1: .2f}
    Imposto Contable R$ {calc_imp_2: .2f}
    Valor liquido R$ {liquido: .2f}
    ''')
