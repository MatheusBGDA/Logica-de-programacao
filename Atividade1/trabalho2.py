
linha_dia_inicio = input().split()
dia_inicio = int(linha_dia_inicio[1])


linha_hora_inicio = input().split(' : ')
hora_inicio = int(linha_hora_inicio[0])
minuto_inicio = int(linha_hora_inicio[1])
segundo_inicio = int(linha_hora_inicio[2])



linha_dia_fim = input().split()
dia_fim = int(linha_dia_fim[1])


linha_hora_fim = input().split(' : ')
hora_fim = int(linha_hora_fim[0])
minuto_fim = int(linha_hora_fim[1])
segundo_fim = int(linha_hora_fim[2])



total_segundos_inicio = segundo_inicio + minuto_inicio * 60 + hora_inicio * 3600 + dia_inicio * 86400
total_segundos_fim = segundo_fim + minuto_fim * 60 + hora_fim * 3600 + dia_fim * 86400


duracao_segundos = total_segundos_fim - total_segundos_inicio


dias = duracao_segundos // 86400
resto_segundos = duracao_segundos % 86400

horas = resto_segundos // 3600
resto_segundos = resto_segundos % 3600

minutos = resto_segundos // 60
segundos = resto_segundos % 60



print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")