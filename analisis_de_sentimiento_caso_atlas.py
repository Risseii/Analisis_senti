
# **Análisis de sentimiento Atlas con TextBlob**
"""

# Importar las bibliotecas necesarias
import pandas as pd
from textblob import TextBlob
import re

# Leer el archivo CSV en un dataframe
df = pd.read_csv('Caso_Atlas1.csv')

# Eliminar caracteres especiales de la columna 'Comentario'
df['Comentario'] = df['Comentario'].apply(lambda comentario: re.sub(r'[^\w\s]', '', comentario) if isinstance(comentario, str) else comentario)

# Limpiar los valores vacíos en la columna 'Comentario'
df['Comentario'] = df['Comentario'].fillna('')

# Convertir los valores en la columna 'Comentario' a cadenas de texto
df['Comentario'] = df['Comentario'].astype(str)

# Crear una nueva columna en el dataframe para almacenar los resultados del análisis de sentimiento
df['Sentimiento'] = df['Comentario'].apply(lambda comentario: TextBlob(comentario).sentiment.polarity)

# Imprimir los resultados del análisis de sentimiento
print(df[['Comentario', 'Sentimiento']])

def get_sentiment_category(Sentimiento):
    if Sentimiento > 0:
        return 'positivo'
    elif Sentimiento < 0:
        return 'negativo'
    else:
        return 'neutral'

sentiment_counts = df['sentiment_category'].value_counts()
print(sentiment_counts)

# Importar bibliotecas necesarias
import matplotlib.pyplot as plt

# Crear un gráfico de barras para visualizar los resultados del análisis de sentimientos
plt.bar(['positivo', 'neutral', 'negativo'], sentiment_counts.values)
# Agregar etiquetas de datos
for i, v in enumerate(sentiment_counts):
    plt.text(i, v + 10, str(v), ha='center')
plt.title('Análisis de sentimientos')
plt.xlabel('Sentimiento')
plt.ylabel('Cantidad de textos')
plt.show()

"""# **Prueba con texto**"""

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiobject = SentimentIntensityAnalyzer()

sentiobject.polarity_scores("you are great")

sentiobject.polarity_scores("is not easy")

"""# **Análisis de sentimiento de Atlas** ⚡"""

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

df = pd.read_csv('Caso_Atlas1.csv')

df['Rank'].value_counts()

sia = SentimentIntensityAnalyzer()

def get_sentiment(Comentario):
    sentiment = sia.polarity_scores(Comentario)
    return sentiment['compound']

df['Comentario'] = df['Comentario'].astype(str)
df['sentiment'] = df['Comentario'].apply(get_sentiment)

print(df)

sentiment_counts = df['sentiment'].value_counts()

print(sentiment_counts)

def get_sentiment_category(sentiment):
    if sentiment > 0:
        return 'positivo'
    elif sentiment < 0:
        return 'negativo'
    else:
        return 'neutral'

df['sentiment_category'] = df['sentiment'].apply(get_sentiment_category)
sentiment_counts = df['sentiment_category'].value_counts()
print(sentiment_counts)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar(['positivo', 'neutral', 'negativo'], sentiment_counts)

# Agregar etiquetas de datos
for i, v in enumerate(sentiment_counts):
    ax.text(i, v + 10, str(v), ha='center')

ax.set_title('Distribución de sentimiento')
ax.set_xlabel('Sentimiento')
ax.set_ylabel('Cantidad de comentarios')

plt.show()
