def MicTexto():
    import speech_recognition as sr
    reconhecedor = sr.Recognizer()
    with sr.Microphone(1) as mic:
        print('\033[1;33m<< Pode falar: >>\033[m')
        audio = reconhecedor.listen(mic)
        # reconhece a fala
        texto = (str(reconhecedor.recognize_google(audio, language='pt-BR'))).upper()
    return texto