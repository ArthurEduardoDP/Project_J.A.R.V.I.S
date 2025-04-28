def listaMicrofones():
    import speech_recognition as sr
    lista = sr.Microphone.list_microphone_names()
    for i,mics in enumerate(lista):
        print(f'{i}: {mics}')

def MicTexto(microfone_numero=1,texto='Pode falar:',mostrar=False,talk=True):
    """
    :param microfone_numero: usado para conectar o microfone certo ao sr.Microphone. se nenhum parâmetro for digitado, o microfone padrão será o 1. para saber qual a número do microfone basta usar a função ListaMicrofones.
    """
    import speech_recognition as sr
    import pyttsx3 as pfla
    from funções import diga


    tentativas = 0
    max_tentativas = 3
    reconhecedor = sr.Recognizer()
    jarvis = pfla.init()
    voices = jarvis.getProperty('voices')
    jarvis.setProperty('voice',voices[0].id)
    with sr.Microphone(microfone_numero) as mic:
        while True:
            print(f'\033[1;33m<< {texto} >>\033[m')
            if talk:
                diga(texto)
            try:
                # ativa o microfone
                audio = reconhecedor.listen(mic)
                # reconhece a fala
                texto = (str(reconhecedor.recognize_google(audio, language='pt-BR'))).upper()
            except sr.UnknownValueError:
                print(f'\033[1;31m<< Não foi possível entender, tente novamente. ({tentativas}/{max_tentativas}) >>')
                if tentativas<max_tentativas:
                    tentativas+=1
                    continue
                else:
                    print(f'\033[1;31m<< O número de tentavias máximas foi alcançada, volte mais tarde! >>')
                    return None
                    break
            except sr.RequestError:
                print(f'\033[1;31m<< Houve um erro na conexão com o serviço de reconhecimento de voz, tente novamente. ({tentativas}/{max_tentativas}) >>')
                if tentativas<max_tentativas:
                    tentativas+=1
                    continue
                else:
                    print(f'\033[1;31m<< O número de tentavias máximas foi alcançada, volte mais tarde! >>')
                    return None
                    break
            else:
                if mostrar:
                    print(f'\033[34m<< Você disse: \033[1;37m{texto}\033[1;34m >>\033[m'.replace('JAR','Jarvis'))
                return texto

def JARVIS(mostrar=False):
    from funções import MicTexto
    from playsound import playsound
    print('\033[1;32m<< Jarvis Ativado. >>\033[m')
    playsound(r'C:\Users\arthu_p\Desktop\projetos\J.A.R.V.I.S (0.5)\jarvisativado.wav')
    texto = MicTexto(microfone_numero=1,texto='Olá mestre, o que deseja fazer hoje?',mostrar=True)
    comandos(texto)
    while True:
        texto = MicTexto(microfone_numero=1,texto='O que deseja agora?',mostrar=True,talk=False)
        comandos(texto=texto)
        if texto == 'DESLIGAR' or texto == 'DESLIGUE-SE':
            print('\033[1;32m<< Ok mestre, Irei me desligar. >>\033[m')
            break

def INTiniciar(texto='Aperte 1 para iniciar'):
    escolha = -1

    while escolha <=0 and escolha != 832012:
        while True:
            try:
                escolha = int(input(f'\033[1;36m {texto} \033[m'))
            except ValueError:
                print('\033[1;31m<< ERRO, tente novamente. >>')
                continue
            else:
                if escolha >0:
                    break   

def diga(texto='Jarvis é foda'):
    import pyttsx3 as fal
    jarvis = fal.init()
    jarvis.say(texto)
    jarvis.runAndWait()

def comandos(texto='entrar no vs code'):
    from funções import diga
    import pyautogui as pag
    from time import sleep
    indice = 0
    texto.upper()
    acessos = ['ENTRAR','ABRIR','ACESSAR','ENTRE'] # 8 - 10
    apps = ['RELÓGIO','SPOTFY','APLICATIVO DE MÚSICA','VISUAL ESTÚDIO CODE','VS CODE','VSCODE','BLOCO DE NOTAS','PAINT','GOOGLE','NAVEGADOR','CHROME']
    if any(acesso in texto for acesso in acessos) and any(app in texto for app in apps):
        for app in apps:
            if app in texto: # pra pegar o nome do app
                break
            indice+=1
        diga(f'ok mestre,abrindo o {apps[indice]}') 
        pag.press('win') #aperta windows
        sleep(0.5)
        pag.write(message=apps[indice]) # digita o nome do app
        pag.press('enter')
        sleep(1)
        pag.hotkey('alt','enter') # ativa a tela cheia
        if apps[8] in texto or apps[9] in texto or apps[10] in texto: # se o app for navegador.
            pag.click(x=902,y=508)
            pesquisa = MicTexto(microfone_numero=1,texto='O que deseja pesquisar, mestre?',talk=True)
            pag.write(message=pesquisa)
            pag.press('enter')
    elif 'FECHAR' in texto:
        diga('Fechando..')
        pag.hotkey('alt','f4')