# Función para asignar un valor numérico a cada una de las respuestas de una columna
def map_column(df, column, mapping):
    return df[column].map(lambda x: mapping[x] if type(x) == str else None)


COLUMN_MAPPING = {
    "¿Cómo de probable considerarías usar nuestro producto como una opción para llevar comida fuera de casa?": "consideracion",
    "¿Cuál de estas características específicas valorarías más en un envase de alimentos con indicador de frescura?": "caracteristicas",
    "Indica el grado de concordancia con respecto a las siguientes características sobre nuestro producto: [Novedoso]": "novedoso",
    "Indica el grado de concordancia con respecto a las siguientes características sobre nuestro producto: [Creativo]": "creativo",
    "Indica el grado de concordancia con respecto a las siguientes características sobre nuestro producto: [Atractivo]": "atractivo",
    "Indica el grado de concordancia con respecto a las siguientes características sobre nuestro producto: [Creíble]": "creible",
    "¿Estarías dispuesto/a a pagar un precio ligeramente más alto por un envase de alimentos con indicador de frescura en comparación con envases convencionales?": "pagar_extra",
    "¿Cuánto dinero extra estarías dispuesto a pagar?": "cuanto_extra",
    "¿Con qué frecuencia cocinas en casa durante la semana?": "frecuencia_cocinar",
    "¿Con qué frecuencia consumes alimentos fuera de casa?": "frecuencia_comer_fuera",
    "¿Te gustaría utilizar un envase de alimentos con un indicador de frescura para reducir el desperdicio?": "gustaria_reducir_desperdicio",
    "¿Cómo de importante es para ti la sostenibilidad medioambiental al elegir productos alimenticios?": "sostenibilidad",
    "¿Qué tan importante es para ti la frescura de los alimentos que consumes?": "importancia_frescura",
    "¿Has buscado activamente formas de reducir el desperdicio de alimentos en tu vida diaria?": "busca_reducir_desperdicio",
    "¿Cuál es tu edad?": "edad",
    "¿Cuál es tu género?": "genero",
    "¿Qué nivel de renta media anual tiene tu hogar? (30.552€ según datos del INE)": "renta",
    "¿Tienes alguna sugerencia o comentario adicional sobre un envase de alimentos con indicador de frescura?": "sugerencias",
    "¿Cuántos dedos tiene por lo general una persona en una mano?": "dedos",
    "¿Qué tamaño de envase considerarían más conveniente para sus necesidades?": "tamaño",
    "¿Tienen preocupaciones sobre la durabilidad o efectividad del indicador de frescura?": "preocupaciones",
    "¿Qué tan importante sería para ustedes poder personalizar el indicador de frescura según sus preferencias individuales?": "personalizacion",
    "¿Qué tan importante ve usted la incorporación del código QR para poder comprobar la frescura de los alimentos sin necesidad de descargarse la aplicación?": "qr",
}

CARACTEIRISTICAS_MAPPING = {
    "Diseño atractivo y practico": 1,
    "Capacidad de reutilización como tupper": 2,
    "Materiales ecoamigables/reciclables": 3,
    "Fácil activación del indicador de frescura": 4,
    "Tamaño adecuado para porciones individuales": 5,
}

LIKERT_MAPPING = {
    "Totalmente de acuerdo": 1,
    "Bastante de acuerdo": 2,
    "Ni de acuerdo ni en desacuerdo": 3,
    "Bastante en desacuerdo": 4,
    "Totalmente en desacuerdo": 5,
}

SI_NO_MAPPING = {
    "Sí": 1,
    "No": 2,
}

PAGAR_MAS_MAPPING = {
    "Entre 0€ y 2,99€": 1,
    "Entre 3€ y 4,99€": 2,
    "Entre 5€ y 6,99€": 3,
    "Más de 7€": 4,
}

FRECUENCIA_MAPPING = {
    "Diariamente": 1,
    "Varias veces a la semana": 2,
    "Pocas veces a la semana": 3,
    "Nunca": 4,
}

GUSTARIA_MAPPING = {
    "Sí, definitivamente": 1,
    "Sí, probablemente": 2,
    "No estoy seguro/a": 3,
    "No, probablemente": 4,
    "No, definitivamente": 5,
}

GENERO_MAPPING = {
    "Masculino": 1,
    "Femenino": 2,
}

RENTA_MAPPING = {
    "Por debajo de la media": 1,
    "Alrededor de la media": 2,
    "Por encima de la media": 3,
}

TAMAÑO_MAPPING = {
    "Pequeño (500ml)": 1,
    "Mediano (1000ml)": 2,
    "Grande (2000ml)": 3,
}

PREOCUPACIONES_MAPPING = {
    "Mucha preocupación": 1,
    "Alguna preocupación": 2,
    "No me importa": 3,
}

IMPORTANCIA_MAPPING = {
    "Muy importante": 1,
    "Algo importante": 2,
    "Poco importante": 3,
}
