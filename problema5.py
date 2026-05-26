#johnier alexander restrepo
#cc: 1002865948
#ingenieria electronica
#funadamento de programacion 2026-01
#fase 5 - evaluacion final POA
#Código: 213022
#docente: Yenny Carolina Rodriguez Vargas

equipo = [["Alice",30,4,6,4,7],
          ["alberto",1,2,3,4,5],
          ["maria",2,3,4,5,6],
          ["luis",3,4,50,6,7]
          ]

def horas_persona(matriz):
 print(f"NOMBRE     | TOTAL HORAS SEMANALES  |CLASIFICACION JORNADA  |")
 print("=" * 60)
 for i in range(0, len(matriz)):
  horas = sum(matriz[i][1:])  # Suma las horas de la persona

if horas > 40:
    print(f"{matriz[i][0]:<10} | {horas:<2} horas semanales     | sobretiempo           |")
 else:
    print(f"{matriz[i][0]:<10} | {horas:<2} horas semanales     | horario estandar      |")
  

 
horas_persona(equipo)