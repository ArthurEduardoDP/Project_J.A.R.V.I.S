import speech_recognition as sr
import funções as fnc
reconhecedor = sr.Recognizer()

escolha = -1

while escolha <=0:
    escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
    if escolha >0 and escolha <832012:
        break
    if escolha == 832012:
        fnc.JARVIS()

texto = fnc.MicTexto(1)
if 'OK' in texto or 'JAR' in texto:
    fnc.JARVIS()
else:
    while 'OK' not in texto and 'JAR' not in texto:
        escolha = int(input('\033[1;36mAperte 1 para iniciar: \033[m'))
        if escolha == 1:
            texto = fnc.MicTexto(1)
    fnc.JARVIS()