
import funções as fnc


fnc.INTiniciar('Digite 1 para iniciar: ')

texto = fnc.MicTexto(microfone_numero=1,talk=False)
if 'OK' in texto or 'JAR' in texto:
    fnc.JARVIS()
else:
    while 'OK' not in texto and 'JAR' not in texto:
        fnc.INTiniciar()
        texto = fnc.MicTexto(1,talk=False)
    fnc.JARVIS()