import pandas as pd
from rapidfuzz import process, fuzz

def normalizacion_nombres(lista1, lista2):
    
    lista_1 = lista1
    lista_2 = lista2

    # Copia para gestionar descartes
    lista_2_disponibles = lista_2.copy()
    clubes_unificados = {}

    # Primera pasada (umbral más alto)
    for nombre1 in lista_1:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_sort_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 95:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Segunda pasada (umbral medio)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.partial_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 90:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Tercera pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 85:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Cuarta pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 80:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Quinta pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 75:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None


    # Sexta pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 70:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None


    # Octava pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 65:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Novena pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 60:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Decima pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 55:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None

    # Undecima pasada (umbral más bajo)
    for nombre1 in [k for k, v in clubes_unificados.items() if v is None]:
        if not lista_2_disponibles:
            clubes_unificados[nombre1] = None
            continue
        resultado = process.extractOne(nombre1, lista_2_disponibles, scorer=fuzz.token_set_ratio)
        if resultado:
            match, score, _ = resultado
            if score > 50:
                clubes_unificados[nombre1] = match
                lista_2_disponibles.remove(match)
            else:
                clubes_unificados[nombre1] = None
        else:
            clubes_unificados[nombre1] = None



    # Resultado final
    df_clubes = pd.DataFrame(list(clubes_unificados.items()), columns=["Nombre_original", "Nombre_unificado"])

    return df_clubes
