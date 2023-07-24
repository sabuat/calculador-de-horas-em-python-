# Este programa é para fazer calculos na modificação de horas e minutos em decimais
# Principal utilidade é para estudos com horas extras a ser utilizado em outros programas

# Aqui se convierten las Horas Extras en decimales
def mod_horas(horas, minutos):
    hora_m = horas + (minutos / 60)
    return hora_m

# Aqui se calculan las Horas Extras
def horas_extras(hora_modificada, he_valor):
    hora_extra = hora_modificada * he_valor
    return hora_extra

# Aqui esta el centro de el código, donde se aplican las funciones
horas = int(input("Ingrese as horas extras sem os minutos: "))
minutos = int(input("Ingrese os minutos: "))
he_valor = float(input("Ingrese o valor da Hora Extra: "))

hora_mod = mod_horas(horas, minutos)

hora_valor_final = horas_extras(hora_mod, he_valor)

# Resultado final 
print(f'''
    As horas trabalhadas foram {horas}:{minutos}
    Valor da Hora Extra R$ {he_valor}
    Total de Horas extras R$ {hora_valor_final: .2f}
    ''')
    