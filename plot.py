import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Función para representar los datos de una columna en un histograma
def histogram(column, x_label):
    plt.hist(column, bins=10, color="green")
    plt.xlabel(x_label)
    plt.ylabel("Respuestas")
    plt.show()


# Función para representar los datos de una columna en un gráfico de barras
def bar_plot(column, ticks, labels):
    _, ax = plt.subplots()
    bar_container = ax.bar(column.value_counts().index, column.value_counts())
    ax.bar_label(bar_container)

    plt.yticks(range(0, max(column.value_counts() + 2), 5))
    plt.xticks(ticks, labels)
    plt.ylabel("Respuestas")
    plt.show()


# Función para representar datos de dos columnas cruzadas en un gráfico de barras
def cross_plot(
    column1, column2, column1_mapping=None, column2_mapping=None, labels=None
):
    cross_data = pd.crosstab(column1, column2)
    cross_data.plot(
        kind="bar",
        stacked=True,
        rot="horizontal",
    )
    if column1_mapping:
        if labels:
            plt.xticks(labels=labels, ticks=range(len(labels)))
        else:
            plt.xticks(
                labels=column1_mapping.keys(), ticks=range(len(column1_mapping.keys()))
            )

    if column2_mapping:
        plt.legend(column2_mapping.keys())

    plt.xlabel("")
    plt.ylabel("Respuestas")
    plt.show()


# Función para representar datos de una columna en un gráfico de tarta
def pie_chart(column, **kwargs):
    plt.figure(figsize=(8, 5))
    plt.pie(
        x=column.value_counts(),
        labels=column.value_counts(),
        autopct="%1.1f%%",
    )
    plt.legend(
        kwargs.get("labels", None),
        loc="upper left",
        bbox_to_anchor=(0.85, 1),
    )
    plt.show()


# Función para representar datos de una columna en un gráfico de barras múltiple
def multi_bar_plot(data, labels):
    x = np.arange(len(labels))
    width = 0.15
    multiplier = 0

    _, ax = plt.subplots(layout="constrained")
    for key, value in data.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=key)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel("Respuestas")
    ax.set_xticks(x + width, labels)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.show()
