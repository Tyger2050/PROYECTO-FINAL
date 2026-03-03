
def emotion_detector(text_to_analyse):
    """
    Analiza el texto recibido y retorna un diccionario simulando la detección de emociones.
    Este ejemplo devuelve siempre 'anger' como emoción dominante, con puntuaciones para cada emoción.
    """
    return {
        'dominant_emotion': 'anger',
        'anger': 0.95,
        'joy': 0.01,
        'fear': 0.02,
        'sadness': 0.01,
        'disgust': 0.01
    }
