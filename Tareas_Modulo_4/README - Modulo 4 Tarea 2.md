# Tarea 2 - Unidad 4  
## Procesamiento y Detección de Imágenes: Emociones Humanas  

### Integrantes:
- **Baez Sauceda Jesús Arnoldo**  
- **Quiñonez Madrid Juan Carlos**  

---

Este proyecto implementa un sistema en Python que utiliza redes neuronales convolucionales (CNN) para detectar emociones humanas a partir de imágenes faciales.

### 🧠 Descripción del Proyecto

El sistema trabaja con imágenes preprocesadas (escaladas, en escala de grises, con reducción de ruido y ajuste de contraste) para entrenar un modelo que puede reconocer emociones como:

- 😄 Feliz  
- 😢 Triste  
- 😠 Enojado  
- 😮 Sorprendido  
- 😐 Neutral  
- 😟 Temeroso  
- 🤢 Disgustado  

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
