# Tarea 2 - Unidad 4  
## Procesamiento y Detección de Imágenes: Emociones Humanas  

### Integrantes:
- **Baez Sauceda Jesús Arnoldo**  
- **Quiñonez Madrid Juan Carlos**  

---

Este proyecto implementa un sistema en Python que utiliza redes neuronales convolucionales (CNN) para detectar emociones humanas a partir de imágenes faciales.

### 🧠 Descripción del Proyecto

El sistema trabaja con imágenes preprocesadas (ajustes de zoom, escaladas, en escala de grises,  con reducción de ruido y ajuste de contraste) para entrenar un modelo que puede reconocer emociones como:

- 😄 Feliz  (Happy)
- 😢 Triste  (Sad)
- 😠 Enojado  (Angry)
- 😮 Sorprendido  (Sorprise)
- 😐 Neutral  (Neutral)
- 😟 Temeroso  (Fear)

## Al momento de ejecutar el programa se abre una pequeña interfaz desde la consola, con un boton para entrenar el modelo, probar con una imagen y para probarlo desde la webcam

## La emocion detectada aparece en la parte superior izquierda de la pantalla (La emocion viene en ingles)

## El dataset esta adjunto, se llama entrenamiento_preprocesado.rar 
## Este archivo comprimido debe descomprimirse (con la herramienta WinRAR)
## Se debe de poner este archivo en la misma carpeta que el programa .py 
## 👀 ¡¡IMPORTANTE!! Se debe verificar que la version de python sea compatible con tensorflow y activar la webcam (si es una laptop la detecta automaticamente asegurate de que no este bloqueda, si lo esta dale F10 en mi caso pero puede variar, y si es webcam asegurate de que este activa).


### 🚀 Funcionalidades

- 📁 **Entrenamiento del modelo:**  
  Usa un conjunto de imágenes clasificadas por emoción para entrenar la red neuronal.

- 🖼️ **Predicción sobre imágenes externas:**  
  Permite cargar una imagen y predecir la emoción detectada en el rostro.

- 🎥 **Detección en tiempo real con cámara web:**  
  Captura la imagen en vivo desde la webcam y muestra la emoción detectada al instante.

---

### 📌 Requisitos

- Python 3.x  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Matplotlib (opcional para visualización)
