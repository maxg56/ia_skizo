from ai import generate_response
from speak import speak
from son import record_audio, transcribe_audio
import re

def get_last_question(text: str) -> str:
    sentences = re.findall(r'[^.!?]*\?', text)
    return sentences[-1].strip() if sentences else ""


def main():
    while True:

        for i in range(-4,4):
            p =  i
            print(f"Personnalité : {p}")
            # if p not in [1, 2]:
            #     continue
            # record_audio()
            # pronpt = transcribe_audio()
            # if pronpt.lower() in ["stop", "quitte", "exit"]:
            #     print("Fin du programme.")
            #     break
            # print(f"Prompt : {pronpt}")
            cont = "tu réponds a la question  et tu pose toujours par une question"
            pronpt = "comnent vois tu l'immensité de l'espace"
            while True:
                response = generate_response(pronpt, cont)
                speak(response)
                pronpt = get_last_question(response)
            


main()