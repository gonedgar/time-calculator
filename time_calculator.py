import re    
    
def add_time(start_time:str, duration_time:str, day:str):
    # Primero verifica que start_time tenga el formato: hora de 1 a 12, dos puntos, minutos 00-59, espacio, AM o PM
    if not re.search("^([1-9]|1[0-2]):([0-5][0-9])\s[AP]M$", start_time):
        return print("The start time is not valid")
    # Después verifica que duration_time tenga el formato: hora de 0 a cualquier número entero, dos puntos, minutos de 00-59
    if not re.search("^[0-9]+:([0-5][0-9])$", duration_time):
        return print("The duration time is not valid")
    # Se verifica que el day sea correcto
    if not re.search("monday|tuesday|wednesday|thursday|friday|saturday|sunday|none", day.lower()):
        return print("They day is not valid")
    
    # Se guarda si AM o PM
    ampm = start_time[-2:]
    # Se obtienen las horas y mintutos de inicio
    # Aquí se obtienen las horas de inicio.
    horas1 = int(start_time.split()[0].split(":")[0])
    # Y aquí los minutos de inicio
    minutos1 = int(start_time.split()[0].split(":")[1])
    # Ahora se obtienen las horas y minutos de duración
    # Primero las horas de duración
    horas2 = int(duration_time.split(":")[0])
    # Después se obtienen los minutos
    minutos2 = int(duration_time[-2:])
    
    # Ahora se hacen los cálculos
    dias_transcurridos = 0
    # Se suman los minutos
    mtotal = minutos1 + minutos2
    # Si la suma de los minutos pasa de 59, se restan 60 minutos y se aumenta 1 a las horas
    if mtotal > 59:
        mtotal = mtotal - 60
        horas1 = horas1 + 1
    # Se suman las horas    
    htotal = horas1 + horas2
    # Si las horas son mayores a 12 (porque AM PM), entonces se resta 12
    while htotal > 11:
        htotal = htotal - 12
        if ampm == "PM":
            ampm = "AM"
            dias_transcurridos = dias_transcurridos + 1
        else:
            ampm = "PM"

    #Se convierten las horas y los minutos a string para imprimirlos más fácilmente
    if htotal == 0:
        htotal = 12
    htotal = str(htotal)
    
    if mtotal < 10:
        mtotal = "0" + str(mtotal)
    else:
        mtotal = str(mtotal)
    
    # Variable para mostrar el día. Si no se puso el día, la variable queda como ""
    show_day = ""
    # Si se pone un día como argumento
    if not day.lower() == "none":
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        dia = 0
        dia = weekdays.index(day.lower())
        for x in range(dias_transcurridos):
            dia = dia + 1
            if dia == 7:
                dia = 0
        show_day = ", " + (weekdays[dia])[0].upper() +  (weekdays[dia])[1:]
    
    # Imprimir el resultado
    if dias_transcurridos == 0:
        return print(htotal + ":" + mtotal + " " + ampm + show_day)
    elif dias_transcurridos == 1:
        return print(htotal + ":" + mtotal + " " + ampm + show_day + " (next day)")
    else:
        return print(htotal + ":" + mtotal + " " + ampm + show_day + " (" + str(dias_transcurridos) + " days later)")