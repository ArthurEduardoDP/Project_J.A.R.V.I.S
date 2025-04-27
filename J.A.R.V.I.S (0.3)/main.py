import speech_recognition as sr
import funções as fnc
reconhecedor = sr.Recognizer()

escolha = -1

while escolha <=0:
    escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
    if escolha >0:
        break

texto = fnc.MicTexto(1)
if 'OK' in texto or 'JAR' in texto:
    print('\033[1;32m<< Jarvis Ativado. >>\033[m')
else:
    while 'OK' not in texto and 'JAR' not in texto:
        print('\033[1;31mNão reconheci seu comando, Fale novamente por favor.\033[m')
        escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
        if escolha == 1:
            texto = fnc.MicTexto(1)
    print('\033[1;32m<< Jarvis Ativado. >>\033[m')