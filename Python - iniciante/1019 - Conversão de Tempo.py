tempo_em_segundos = int(input())

horas = (tempo_em_segundos//60)//60

tempo_em_segundos1 = tempo_em_segundos - ((horas*60)*60) 

minutos = (tempo_em_segundos1//60)

tempo_em_segundos2 = tempo_em_segundos1 - (minutos*60)

segundos = tempo_em_segundos2

print(f'{horas}:{minutos}:{segundos}')