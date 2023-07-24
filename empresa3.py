valor_fixo_RM = 12324.64
valor_fixo_TC = 12324.64
valor_fixo_MM = 4000
valor_fixo_total = valor_fixo_MM + valor_fixo_RM + valor_fixo_TC
valor_HE_RM = 65
valor_HE_TC = 65
valor_HE_MM = 50
horas_RM = 216
horas_TC = 216
horas_MM = 80

def horas_extras_total(rm, tc, mm):
    he1 = rm * valor_HE_RM
    he2 = tc * valor_HE_TC
    he3 = mm * valor_HE_MM
    het= he1 + he2 + he3
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

horas_hrm = int(input("Ingrese as horas extras de Resonancia sem os minutos ou digite 0: "))
minutos_hrm = int(input("Ingrese os minutos de Resonancia ou digite 0: "))
hrm = mod_horas(horas_hrm, minutos_hrm)

horas_htc = int(input("Ingrese as horas extras de Tomografia sem os minutos ou digite 0: "))
minutos_htc = int(input("Ingrese os minutos de Tomografia ou digite 0: "))
htc = mod_horas(horas_htc, minutos_htc)

horas_hmm = int(input("Ingrese as horas extras de Mamografia sem os minutos ou digite 0: "))
minutos_hmm = int(input("Ingrese os minutos de Mamografia ou digite 0: "))
hmm = mod_horas(horas_hmm, minutos_hmm)

horas_extras = horas_extras_total(hrm, htc, hmm)

horas_extras_1 = hrm * valor_HE_RM
horas_extras_2 = htc * valor_HE_TC
horas_extras_3 = hmm * valor_HE_MM

total_rm = valor_fixo_RM + horas_extras_1
total_tc = valor_fixo_TC + horas_extras_2
total_mm = valor_fixo_MM + horas_extras_3

valor_neto = final(horas_extras, valor_fixo_total)

calc_imp_1 = imposto_647(valor_neto)

calc_imp_2 = imposto_cont(valor_neto)

liquido = valor_neto - (calc_imp_1 + calc_imp_2)

horas_trabalhadas = int(horas_MM + horas_RM + horas_TC + horas_extras)

print(f'''
    Horas trabalhadas no mes {horas_trabalhadas}
    Total de Horas extras R$ {horas_extras: .2f}
    Horas Extras Resonancia R$ {horas_extras_1: .2f}
    Horas Extras Tomografia R$ {horas_extras_2: .2f}
    Horas Extras Mamografia R$ {horas_extras_3: .2f}
    Total Resonancia R$ {total_rm: .2f}
    Total Tomografia R$ {total_tc: .2f}
    Total Mamografia R$ {total_mm: .2f}
    Valor Bruto R$ {valor_neto: .2f}
    Imposto Art. 647 R$ {calc_imp_1: .2f}
    Imposto Contable R$ {calc_imp_2: .2f}
    Valor liquido R$ {liquido: .2f}
    ''')