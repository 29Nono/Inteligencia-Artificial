# Tarea 1 - Módulo 4

## Objetivo
Encontrar un dataset de imágenes de rostros humanos clasificados por emociones, apto para entrenar un modelo de IA que detecte la emoción de una cara enviada por el usuario.

## Dataset seleccionado
**FER-2013**  
🔗 [Enlace al dataset en Kaggle](https://www.kaggle.com/datasets/msambare/fer2013/data)  
- Contiene más de **7,000 imágenes** etiquetadas.  
- Resolución: **48x48 píxeles** (ideal para preprocesamiento eficiente).  

## Emociones clasificadas
El dataset incluye 7 categorías de emociones:  
1. 😠 Enojado  
2. 🤢 Disgustado  
3. 😨 Miedoso  
4. 😃 Feliz  
5. 😐 Neutral  
6. 😢 Triste  
7. 😲 Sorprendido  

## Preprocesamiento de imágenes
Para mejorar la robustez del modelo, se aplicarán las siguientes transformaciones a las imágenes:  

### 1. Cambios de intensidad de luz  
- Ajuste de brillo y contraste para simular diferentes condiciones de iluminación.  
- Ejemplo de código (OpenCV):  
  ```python
  adjusted = cv2.convertScaleAbs(image, alpha=1.5, beta=30)  # Aumentar brillo y contraste
