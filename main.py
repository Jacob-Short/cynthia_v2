import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3



def main():
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english_rp+f3')
    engine.say('Hello my name is cynthia, how can I be of assistance?')
    engine.runAndWait()
    client = wolframalpha.Client("U442R6-LJ7XH3X756")




    sg.theme("DarkRed")
    layout = [[sg.Text("Ask me a question")], [sg.Input()], [sg.Button("Search")]]
    window = sg.Window("Cynthia", layout, margins=(100,50))

    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            break
        try:
            wiki_res = wikipedia.summary(values[0], sentences=2)
            res = client.query(values[0])
            wolf_res = next(res.results).text
            engine.say(wolf_res)
            sg.PopupNonBlocking(f'Wolfram Results: {wolf_res}\n Wikipedia Results: {wiki_res}')
        except wikipedia.exceptions.DisambiguationError:
            res = client.query(values[0])
            wolf_res = next(res.results).text
            engine.say(wolf_res)
            sg.PopupNonBlocking(f'Wolfram Results: {wolf_res}')
        except wikipedia.exceptions.PageError:
            res = client.query(values[0])
            wolf_res = next(res.results).text
            engine.say(wolf_res)
            sg.PopupNonBlocking(f'Wolfram Results: {wolf_res}')
        except:
            wiki_res = wikipedia.summary(values[0], sentences=2)
            engine.say(wiki_res)
            sg.PopupNonBlocking(f'Wikipedia Results: {wiki_res}')

        engine.runAndWait()
        


    window.close()

if __name__=='__main__':
    main()
