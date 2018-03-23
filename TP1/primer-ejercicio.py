import numpy as np

print('')

tiempo_base = 60 * 8

tiempo_llegada = np.random.randint(3, 6, size=5) * 5
tiempo_fin_servicio = np.random.randint(2, 5, size=5) * 10

print('MINUTOS ALEATORIOS DE LLEGADA: ' + str(tiempo_llegada))
print('MINUTOS ALEATORIOS DE FIN DE SERVICIO: ' + str(tiempo_fin_servicio))

print('')

arreglo_fin_servicio = []
arreglo_llegada = []

def transformar_minutos_a_horas(tiempo_minutos):
    tiempo_horas = tiempo_minutos / 60
    tiempo_horas_resto = tiempo_minutos % 60

    resultado_hora = str(tiempo_horas)
    resultado_hora_resto = str(tiempo_horas_resto)

    if tiempo_horas < 10:
        resultado_hora = '0' + str(tiempo_horas) 
    if tiempo_horas_resto < 10:
        resultado_hora_resto = '0' + str(tiempo_horas_resto)

    resultado = resultado_hora + ':' + resultado_hora_resto
    return resultado

ps = 1
q = 3

for i in range(20):
        j = i


def arreglo_horas(tipo_arreglo, minutos_arreglo, minutos_anteriores):
    j = 0
    count = 0
    for i in range(20):
        if i < 5:
            j = i
        else:
            if count == 5:
                count = 0
            j = count
            count += 1

        minutos_nuevos = minutos_anteriores + minutos_arreglo[j]
        tipo_arreglo.append(minutos_nuevos)
        minutos_anteriores = minutos_nuevos

arreglo_horas(arreglo_llegada, tiempo_llegada, tiempo_base)
arreglo_horas(arreglo_fin_servicio, tiempo_fin_servicio, tiempo_base)

def llegada_cliente(i, ps, q):
    if ps == 0:
        ps = 1
    else:
        q += 1
    i += 1
    return ps, q, i

def fin_servicio(i, ps, q):
    ps = 0
    if q > 0:
        ps = 1
        q -= 1
        i += 1
    return ps, q, i

i_fin_servicio = 0
i_llegada = 0

hora_tiempo_base = transformar_minutos_a_horas(tiempo_base)
hora_arreglo_llegada = transformar_minutos_a_horas(arreglo_llegada[i_llegada])
hora_arreglo_fin_servicio = transformar_minutos_a_horas(arreglo_fin_servicio[i_fin_servicio])

print(
    '   HORA ACTUAL      |' +
    '   HORA PROX LLEGADA    |' +
    '   HORA PROX FIN SERVICIO   |' +
    '    q     |'
    '   ps'
)

print('')

print(
    '       ' + hora_tiempo_base + '        | ' +
    '        ' + hora_arreglo_llegada + '          | ' +
    '           ' + hora_arreglo_fin_servicio + '           | ' +
    '   ' + str(q) + '     | ' +
    '   ' + str(ps)
)

while(tiempo_base < 780):
    if arreglo_llegada[i_llegada] <= arreglo_fin_servicio[i_fin_servicio]:
        tiempo_base = arreglo_llegada[i_llegada]
        ps, q, i_llegada = llegada_cliente(i_llegada, ps, q)
    else:
        tiempo_base = arreglo_fin_servicio[i_fin_servicio]
        ps, q, i_fin_servicio = fin_servicio(i_fin_servicio, ps, q)

    print('')

    hora_tiempo_base = transformar_minutos_a_horas(tiempo_base)
    hora_arreglo_llegada = transformar_minutos_a_horas(arreglo_llegada[i_llegada])
    hora_arreglo_fin_servicio = transformar_minutos_a_horas(arreglo_fin_servicio[i_fin_servicio])

    print(
    '       ' + hora_tiempo_base + '        | ' +
    '        ' + hora_arreglo_llegada + '          | ' +
    '           ' + hora_arreglo_fin_servicio + '           | ' +
    '   ' + str(q) + '     | ' +
    '   ' + str(ps)
    )

print('')
