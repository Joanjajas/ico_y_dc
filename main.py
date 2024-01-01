import pandas as pd
import matplotlib as mpl

from mappings import *
from plot import *


# Leemos los datos del archivo csv
df = pd.read_csv("data.csv")

# Renombramos las columnas para que sean más legibles y nos sea más fácil
# trabajar con ellas
df.rename(columns=COLUMN_MAPPING, inplace=True)

mpl.style.use("ggplot")

################################################################################
# Procesamiento de los datos
################################################################################
edad = df["edad"]
dedos = df["dedos"]
sugerencias = df["sugerencias"]
consideracion = df["consideracion"]
sostenibilidad = df["sostenibilidad"]
importancia_frescura = df["importancia_frescura"]
qr = map_column(df, "qr", IMPORTANCIA_MAPPING)
renta = map_column(df, "renta", RENTA_MAPPING)
genero = map_column(df, "genero", GENERO_MAPPING)
tamaño = map_column(df, "tamaño", TAMAÑO_MAPPING)
creible = map_column(df, "creible", LIKERT_MAPPING)
novedoso = map_column(df, "novedoso", LIKERT_MAPPING)
creativo = map_column(df, "creativo", LIKERT_MAPPING)
atractivo = map_column(df, "atractivo", LIKERT_MAPPING)
pagar_extra = map_column(df, "pagar_extra", SI_NO_MAPPING)
cuanto_extra = map_column(df, "cuanto_extra", PAGAR_MAS_MAPPING)
personalizacion = map_column(df, "personalizacion", IMPORTANCIA_MAPPING)
preocupaciones = map_column(df, "preocupaciones", PREOCUPACIONES_MAPPING)
frecuencia_cocinar = map_column(df, "frecuencia_cocinar", FRECUENCIA_MAPPING)
frecuencia_comer_fuera = map_column(df, "frecuencia_comer_fuera", FRECUENCIA_MAPPING)
busca_reducir_desperdicio = map_column(df, "busca_reducir_desperdicio", SI_NO_MAPPING)
gustaria_reducir_desperdicio = map_column(
    df, "gustaria_reducir_desperdicio", GUSTARIA_MAPPING
)

################################################################################
# Representación de los datos
################################################################################

# ¿Cómo de probable considerarías usar nuestro producto como una opción para
# llevar comida fuera de casa?
bar_plot(
    consideracion,
    range(6),
    ["", "1\nMuy probable", "2", "3", "4", "5\n Muy improbable"],
)

# ¿Cómo de importante es para ti la sostenibilidad medioambiental al elegir
# productos alimenticios?
bar_plot(
    sostenibilidad,
    range(6),
    ["", "1\nMuy importante", "2", "3", "4", "5\n Nada importante"],
)

# ¿Qué tan importante es para ti la frescura de los alimentos que consumes?
bar_plot(
    importancia_frescura,
    range(6),
    ["", "1\nMuy importante", "2", "3", "4", "5\n Nada importante"],
)

# ¿Qué tamaño de envase considerarían más conveniente para sus necesidades?
pie_chart(tamaño, labels=TAMAÑO_MAPPING.keys())

# ¿Tienen preocupaciones sobre la durabilidad o efectividad del indicador de
# frescura?
pie_chart(preocupaciones, labels=PREOCUPACIONES_MAPPING.keys())

# ¿Qué tan importante sería para ustedes poder personalizar el indicador de
# frescura según sus preferencias individuales?
pie_chart(personalizacion, labels=IMPORTANCIA_MAPPING.keys())

# ¿Qué tan importante ve usted la incorporación del código QR para poder
# comprobar la frescura de los alimentos sin necesidad de descargarse la
# aplicación?
pie_chart(qr, labels=IMPORTANCIA_MAPPING.keys())

# ¿Estarías dispuesto/a a pagar un precio ligeramente más alto por un envase de
# alimentos con indicador de frescura en comparación con envases convencionales?
pie_chart(pagar_extra, labels=SI_NO_MAPPING.keys())

# ¿Cuánto dinero extra estarías dispuesto a pagar?
pie_chart(cuanto_extra, labels=PAGAR_MAS_MAPPING.keys())

# ¿Con qué frecuencia cocinas en casa durante la semana?
pie_chart(frecuencia_cocinar, labels=FRECUENCIA_MAPPING.keys())

# ¿Con qué frecuencia consumes alimentos fuera de casa?
pie_chart(frecuencia_comer_fuera, labels=FRECUENCIA_MAPPING.keys())

# ¿Te gustaría utilizar un envase de alimentos con un indicador de frescura para
# reducir el desperdicio?
pie_chart(gustaria_reducir_desperdicio, labels=GUSTARIA_MAPPING.keys())

# ¿Has buscado activamente formas de reducir el desperdicio de alimentos en tu
# vida diaria?
pie_chart(busca_reducir_desperdicio, labels=SI_NO_MAPPING.keys())

# ¿Cuál es tu edad?
histogram(edad, "Edad")

# ¿Cuál es tu género?
pie_chart(genero, labels=GENERO_MAPPING.keys())

# ¿Qué nivel de renta media anual tiene tu hogar? (30.552€ según datos del INE)
pie_chart(renta, labels=RENTA_MAPPING.keys())

# ¿Cuál de estas características específicas valorarías más en un envase de
# alimentos con indicador de frescura?
caracteristicas = []
for row in df["caracteristicas"]:
    split_caracteristicas = row.split(", ")
    for caracteristica in split_caracteristicas:
        if caracteristica in CARACTEIRISTICAS_MAPPING:
            caracteristicas.append(CARACTEIRISTICAS_MAPPING[caracteristica])

caracteristicas = pd.Series(caracteristicas)
cross_plot(
    caracteristicas,
    genero,
    CARACTEIRISTICAS_MAPPING,
    GENERO_MAPPING,
    labels=[
        "Diseño atractivo\ny practico",
        "Capacidad de reutilización\ncomo tupper",
        "Materiales\necoamigables/reciclables",
        "Fácil activación del\nindicador de frescura",
        "Tamaño adecuado para\nporciones individuales",
    ],
)

# Indica el grado de concordancia con respecto a las siguientes características
# sobre nuestro producto:
fields = ["Novedoso", "Creativo", "Atractivo", "Creíble"]
data = {
    "Totalmente de acuerdo": [
        novedoso.value_counts()[1],
        creativo.value_counts()[1],
        atractivo.value_counts()[1],
        creible.value_counts()[1],
    ],
    "Bastante de acuerdo": [
        novedoso.value_counts()[2],
        creativo.value_counts()[2],
        atractivo.value_counts()[2],
        creible.value_counts()[2],
    ],
    "Ni de acuerdo ni en desacuerdo": [
        novedoso.value_counts()[3],
        creativo.value_counts()[3],
        atractivo.value_counts()[3],
        creible.value_counts()[3],
    ],
    "Bastante en desacuerdo": [
        novedoso.value_counts()[4],
        creativo.value_counts()[4],
        atractivo.value_counts()[4],
        creible.value_counts()[4],
    ],
    "Totalmente en desacuerdo": [
        novedoso.value_counts()[5],
        creativo.value_counts()[5],
        atractivo.value_counts()[5],
        creible.value_counts()[5],
    ],
}

multi_bar_plot(data, fields)

################################################################################
# Estadisticas cruzadas
################################################################################

# Separamos por grupos de edad
edad = pd.cut(edad, bins=[0, 24, 35, 60, 80])

# Busca reducir desperdicio por edad
edad_gustaria_reducir_desperdicio = pd.crosstab(
    edad, gustaria_reducir_desperdicio, normalize="index"
)
print(round(edad_gustaria_reducir_desperdicio * 100, 2))
cross_plot(gustaria_reducir_desperdicio, edad, GUSTARIA_MAPPING)

# Esta dispuesto a pagar mas por renta
dinero_extra_renta = pd.crosstab(renta, cuanto_extra, normalize="index")
print(round(dinero_extra_renta * 100, 2))
cross_plot(cuanto_extra, renta, PAGAR_MAS_MAPPING, RENTA_MAPPING)

# Qr por edad
qr_edad = pd.crosstab(edad, qr, normalize="index")
print(round(qr_edad * 100, 2))
cross_plot(qr, edad, IMPORTANCIA_MAPPING)

# Frecuencia cocinar en casa por genero
frecuencia_cocinar_genero = pd.crosstab(genero, frecuencia_cocinar, normalize="index")
print(round(frecuencia_cocinar_genero * 100, 2))
cross_plot(frecuencia_cocinar, genero, FRECUENCIA_MAPPING, GENERO_MAPPING)

# Frecuencia cocinar en casa por edad
frecuencia_cocinar_edad = pd.crosstab(edad, frecuencia_cocinar, normalize="index")
print(round(frecuencia_cocinar_edad * 100, 2))
cross_plot(frecuencia_cocinar, edad, FRECUENCIA_MAPPING)

# Frecuencia cocinar en casa por renta
frecuencia_cocinar_renta = pd.crosstab(renta, frecuencia_cocinar, normalize="index")
print(round(frecuencia_cocinar_renta * 100, 2))
cross_plot(frecuencia_cocinar, renta, FRECUENCIA_MAPPING, RENTA_MAPPING)

# Frecuencia comer fuera por edad
frecuencia_comer_fuera_edad = pd.crosstab(
    edad, frecuencia_comer_fuera, normalize="index"
)
print(round(frecuencia_comer_fuera_edad * 100, 2))
cross_plot(frecuencia_comer_fuera, edad, FRECUENCIA_MAPPING)

# Frecuencia comer fuera por renta
frecuencia_comer_fuera_renta = pd.crosstab(
    renta, frecuencia_comer_fuera, normalize="index"
)
print(round(frecuencia_comer_fuera_renta * 100, 2))
cross_plot(frecuencia_comer_fuera, renta, FRECUENCIA_MAPPING, RENTA_MAPPING)


# Caracteristicas por genero
caracteristicas_genero = pd.crosstab(genero, caracteristicas, normalize="index")
print(round(caracteristicas_genero * 100, 2))
cross_plot(
    caracteristicas,
    genero,
    CARACTEIRISTICAS_MAPPING,
    GENERO_MAPPING,
    [
        "Diseño atractivo\ny practico",
        "Capacidad de reutilización\ncomo tupper",
        "Materiales\necoamigables/reciclables",
        "Fácil activación del\nindicador de frescura",
        "Tamaño adecuado para\nporciones individuales",
    ],
)

# Importancia frescura por edad y genero
importancia_frescura_edad_genero = pd.crosstab(
    [edad, genero], importancia_frescura, normalize="index"
)
print(round(importancia_frescura_edad_genero * 100, 2))

# Consideracion por edad y genero
consideracion_edad_genero = pd.crosstab(
    [edad, genero], consideracion, normalize="index"
)
print(round(consideracion_edad_genero * 100, 2))

# Personalizacion por edad y genero
personalizacion_edad_genero = pd.crosstab(
    [edad, genero], personalizacion, normalize="index"
)
print(round(personalizacion_edad_genero * 100, 2))
