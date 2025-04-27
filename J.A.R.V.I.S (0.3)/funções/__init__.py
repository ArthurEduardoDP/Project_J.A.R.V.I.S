def listaMicrofones():
    import speech_recognition as sr
    lista = sr.Microphone.list_microphone_names()
    for i,mics in enumerate(lista):
        print(f'{i}: {mics}')
def MicTexto(microfone_numero=1):
    """
    :param microfone_numero: usado para conectar o microfone certo ao sr.Microphone. se nenhum parâmetro for digitado, o microfone padrão será o 1. para saber qual a número do microfone basta usar a função ListaMicrofones.
    """
    import speech_recognition as sr

    tentativas = 0
    max_tentativas = 3
    reconhecedor = sr.Recognizer()
    with sr.Microphone(microfone_numero) as mic:
        while True:
            print('\033[1;33m<< Pode falar: >>\033[m')
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
                    break
            except sr.RequestError:
                print(f'\033[1;31m<< Houve um erro na conexão com o serviço de reconhecimento de voz, tente novamente. ({tentativas}/{max_tentativas}) >>')
                if tentativas<max_tentativas:
                    tentativas+=1
                    continue
                else:
                    print(f'\033[1;31m<< O número de tentavias máximas foi alcançada, volte mais tarde! >>')
                    break
            else:
                return texto