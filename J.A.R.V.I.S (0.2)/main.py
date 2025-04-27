import speech_recognition as sr
from funções import *
reconhecedor = sr.Recognizer()

escolha = -1

while escolha <=0:
    escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
    if escolha >0:
        break

# inicia o uso com microfone
with sr.Microphone(1) as mic:
    # remove os ruídos
    reconhecedor.adjust_for_ambient_noise(mic)
    print('\033[1;33m<< Pode falar: >>\033[m')
    # ativa o microfone
    audio = reconhecedor.listen(mic)
    # reconhece a fala
    texto = (str(reconhecedor.recognize_google(audio, language='pt-BR'))).upper()
    if 'OK' in texto or 'JAR' in texto:
        print('\033[1;32m<< Jarvis Ativado. >>\033[m')
    else:
        while 'OK' not in texto or 'JAR' not in texto:
            print('\033[1;31mNão reconheci seu comando, Fale novamente por favor.\033[m')
            escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
            if escolha == 1:
                print('\033[1;33m<< Pode falar: >>\033[m')
                audio = reconhecedor.listen(mic)
                texto = (str(reconhecedor.recognize_google(audio, language='pt-BR'))).upper()
        print('\033[1;32m<< Jarvis Ativado. >>\033[m')