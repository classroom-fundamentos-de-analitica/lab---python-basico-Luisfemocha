"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""

def pregunta_01():
    """Retorne la suma de la segunda columna. Rta/ 214"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    res= sum(int(i[1]) for i in datos)   # suma de la segunda columna for i in datos: res+= int(i[1])
    archivo.close()
    return res

def pregunta_02():
    """Retorne la cantidad de registros por cada letra de la primera columna como la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif2={}
    for aux in datos:
        if aux[0] not in dif2.keys():
            dif2[aux[0]]= 1
        else:
            dif2[aux[0]]+=1

    res=[]
    for a in sorted(dif2):
        res.append((a,dif2[a]))
    archivo.close()
    return res

def pregunta_03():
    """ Retorne la suma de la columna 2 por cada letra de la primera columna como una lista de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif3={}         # letras diferentes dif3 = list(set(i[0] for i in datos))
    for aux in datos:
        if aux[0] not in dif3.keys():
            dif3[aux[0]]= int(aux[1])
        else:
            dif3[aux[0]]+= int(aux[1])

    res=[]
    for a in sorted(dif3):
        res.append((a,dif3[a]))
    archivo.close()
    return res

def pregunta_04():
    """ La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    meses4={}   # meses diferentes
    res= '['    # string a devolver...
    for aux in datos:
        mes= aux[2][5:7]   # 1999-02-28
        if mes not in meses4.keys():
            meses4[mes]= 1
        else:
            meses4[mes]+= 1

    res=[]
    for mes in sorted(meses4):
        res.append((mes,meses4[mes]))
    archivo.close()
    return res

def pregunta_05():
    """ Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    max5={}     # maximos
    min5={}     # minimos
    for aux in datos:
        if aux[0] not in max5.keys():
            max5[aux[0]]= int(aux[1])
            min5[aux[0]]= int(aux[1])
        else:
            if max5[aux[0]]< int(aux[1]):
                max5[aux[0]]= int(aux[1])

            if min5[aux[0]]> int(aux[1]):
                min5[aux[0]]= int(aux[1])

    res=[]
    for a in sorted(max5):
        res.append((a,max5[a],min5[a]))
    archivo.close()
    return res

def pregunta_06():
    """ La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a una clave y el valor despues del caracter `:` corresponde al valor asociado a la clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    max6={}     # maximos
    min6={}     # minimos
    res= '['    # string a devolver...
    for aux in datos:   # jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        for elemento in aux[4].split(','):
            clave= elemento[:3]
            valor= elemento[4:]
            if clave not in max6.keys():
                max6[clave]= int(valor)
                min6[clave]= int(valor)
            else:
                if max6[clave]< int(valor):
                    max6[clave]= int(valor)

                if min6[clave]> int(valor):
                    min6[clave]= int(valor)

    res=[]
    for a in sorted(max6):
        res.append((a,min6[a],max6[a]))
    archivo.close()
    return res

def pregunta_07():
    """ Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1) a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif7={}     # numeros diferentes
    for aux in datos:
        if aux[1] not in dif7.keys():
            dif7[aux[1]]= [aux[0]]
        else:
            dif7[aux[1]].append(aux[0])

    res=[]
    for a in sorted(dif7):
        res.append((a,dif7[a]))
    archivo.close()
    return res

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor de la segunda columna; la segunda parte de la tupla es una lista con las letras (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif8={}     # numeros diferentes
    for aux in datos:
        if aux[1] not in dif8.keys():
            dif8[aux[1]]= [aux[0]]
        elif aux[0] not in dif8[aux[1]]:
            dif8[aux[1]].append(aux[0])
            dif8[aux[1]].sort()

    res=[]
    for a in sorted(dif8):
        res.append((a,dif8[a]))
    archivo.close()
    return res

def pregunta_09():
    """ Retorne un diccionario que contenga la cantidad de registros en que aparece cada clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]
    dif9={}     # claves diferentes
    for aux in datos:   # jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        for elemento in aux[4].split(','):
            if elemento[:3] not in dif9.keys():
                dif9[elemento[:3]]= 1
            else:
                dif9[elemento[:3]]+= 1
    archivo.close()
    return dif9

def pregunta_10():
    """ Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    res= []
    for aux in datos:   # E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        q4= len(aux[3].split(','))
        q5= len(aux[4].split(','))
        res.append((aux[0],q4,q5))
    archivo.close()
    return res

def pregunta_11():
    """ Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    } """
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif11={}     # claves diferentes
    for aux in datos:   # E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        for elemento in aux[3].split(','):
            if elemento not in dif11.keys():
                dif11[elemento]= int(aux[1])
            else:
                dif11[elemento]+= int(aux[1])
    archivo.close()
    return dif11

def pregunta_12():
    """ Genere un diccionario que contengan como clave la columna 1 y como valor la suma de los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }"""
    archivo= open("data.csv","r")
    datos= [i.split() for i in archivo.read().split("\n")]

    dif12={}     # claves diferentes
    for aux in datos:   # E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
        valores=0
        for elemento in aux[4].split(','):
            valores+= int(elemento[4:])

        if aux[0] not in dif12.keys():
            dif12[aux[0]]= valores
        else:
            dif12[aux[0]]+= valores
    archivo.close()
    return dif12
