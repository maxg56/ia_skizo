import whisper
import pyaudio
import wave

# Load the Whisper model
model = whisper.load_model("base")



def record_audio(fichier_sortie="output.wav", duree=10, taux_echantillonnage=44100, canaux=1, taille_bloc=1024):
    """
    Enregistre un fichier audio en format WAV.

    :param fichier_sortie: Nom du fichier de sortie (par défaut "enregistrement.wav").
    :param duree: Durée de l'enregistrement en secondes (par défaut 5 secondes).
    :param taux_echantillonnage: Taux d'échantillonnage en Hz (par défaut 44100).
    :param canaux: Nombre de canaux (1 pour mono, 2 pour stéréo, par défaut 1).
    :param taille_bloc: Taille du bloc d'échantillons pour chaque lecture (par défaut 1024).
    """
    # Initialisation de PyAudio
    p = pyaudio.PyAudio()

    # Ouverture du flux d'entrée audio
    stream = p.open(format=pyaudio.paInt16,
                    channels=canaux,
                    rate=taux_echantillonnage,
                    input=True,
                    frames_per_buffer=taille_bloc)

    print("Enregistrement en cours...")

    frames = []

    # Enregistrement de l'audio
    for _ in range(0, int(taux_echantillonnage / taille_bloc * duree)):
        data = stream.read(taille_bloc)
        frames.append(data)

    # Arrêt de l'enregistrement
    print("Enregistrement terminé.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Sauvegarder l'audio dans un fichier WAV
    with wave.open(fichier_sortie, 'wb') as wf:
        wf.setnchannels(canaux)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(taux_echantillonnage)
        wf.writeframes(b''.join(frames))

    print(f"Fichier audio sauvegardé sous '{fichier_sortie}'")



def transcribe_audio(filename="output.wav"):
    print("🎧 Transcription de l'audio en cours...")
    result = model.transcribe(filename)
    text = result["text"].strip()
    print(f"🔍 Transcription détectée : '{text}'")
    return text



