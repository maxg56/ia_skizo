import serial
import numpy as np
import pyaudio
import wave

# Configuration du port série
PORT = "/dev/ttyACM0"  # Linux/Mac -> /dev/ttyUSB0 | Windows -> COM3
BAUDRATE = 115200
SAMPLE_RATE = 16000  # 16 kHz
CHUNK_SIZE = 1024  # Nombre d'échantillons par bloc

# Ouvrir le port série
ser = serial.Serial(PORT, BAUDRATE, timeout=1)

# Initialisation PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=SAMPLE_RATE,
                output=True)

print("🎙️ Écoute en direct... (Appuie sur Ctrl+C pour arrêter)")

frames = []
try:
    while True:
        samples = []
        for _ in range(CHUNK_SIZE):
            line = ser.readline().strip()  # Lire une ligne série
            if line.isdigit():  # Vérifier que c'est un nombre
                sample = int(line)
                sample = np.interp(sample, [0, 1023], [-32768, 32767])  # Normalisation
                samples.append(int(sample))

        # Convertir en format audio
        audio_data = np.array(samples, dtype=np.int16).tobytes()
        stream.write(audio_data)  # Émettre le son
        frames.append(audio_data)  # Stocker les données pour l'enregistrement

except KeyboardInterrupt:
    print("🛑 Arrêt du streaming.")

    # Enregistrer le fichier WAV
    wf = wave.open("audio_stream.wav", "wb")
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    # Fermer tout
    stream.stop_stream()
    stream.close()
    p.terminate()
    ser.close()

    print("📁 Fichier enregistré : audio_stream.wav")
