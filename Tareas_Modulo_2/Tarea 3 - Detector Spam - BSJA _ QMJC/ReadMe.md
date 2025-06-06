Tarea 3 - Modulo 2 
Detector de spam

Inteligencia Artificial

Maestro:
Mora Felix Zuriel Dathan

Integrantes:
Baez Sauceda Jesus Arnoldo
Quiñonez Madrid Juan Carlos

Grupo: 11:00 - 12:00 hrs

Objetivo:
Desarrollar un modelo de aprendizaje automático para clasificar correos electrónicos como “Spam” o “No Spam” utilizando el teorema de Bayes.

Requisitos:
Python 3.x
Librerías:
-Numpy
-Pandas
-Sklearn
-Re
-NLTK (Stopwords)

IMPORTANTE:
Checar si agregaste el path al instalar python y agregarla a el entorno virtual (visual studio code)
instalarla desde la terminal con los siguientes comandos

pip install numpy
pip install pandas
pip install scikit-learn  # para sklearn
pip install regex  # para re
pip install nltk

esto instalará todo lo que nescesitamos, ojo son diferentes que las extensiones
si no da error ya estarian bien instalados

Datos:
Conjunto de datos SpamAssassin Public Corpus, que contiene 5827 correos etiquetados como “Spam = 1” o “No Spam = 0”.

Preprocesamiento de Datos:
1.	Eliminar correos electrónicos duplicados.
2.	Convertir todo el texto a minúsculas.
3.	Eliminar caracteres especiales.
4.	Eliminar palabras vacías (stopwords).
5.	Tokenizar el texto.


2. Modelo:
El modelo se basa en el Teorema de Bayes para calcular la probabilidad de que un correo electrónico sea spam dado su conjunto de características.

3. Algoritmo (Código en Python):
-Calcular la probabilidad previa de spam (P(Spam)):
	P_spam = numero_correos_spam / total_correos 
-Calcular la probabilidad de las características del correo electrónico dado que es spam (P(Características|Spam)):
	P_caracteristicas_spam = frecuencia_caracteristicas_spam / total_caracteristicas_spam
-Calcular la probabilidad de las características del correo electrónico dado que no es spam (P(Características|NoSpam)):
	P_caracteristicas_no_spam = frecuencia_caracteristicas_no_spam / total_caracteristicas_no_spam
-Calcular la probabilidad posterior de que el correo electrónico sea spam (P(Spam|Características)):
P_spam_caracteristicas = (P_spam * P_caracteristicas_spam) / (P_spam * P_caracteristicas_spam + P_no_spam * P_caracteristicas_no_spam)

Clasificación:
-Un correo electrónico se clasificará como spam si:
	P(Spam|Características) > P(NoSpam|Características)
Evaluación:

-Precisión:
	precision = np.sum(clasificaciones == data[“target”])/len(clasificaciones)
-Recuperación:
	recuperacion = np.sum(clasificaciones == data[“target”])/data[“target”].sum()
