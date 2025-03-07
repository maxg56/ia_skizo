

def lire_arduino():
    try:
        with open("/dev/ttyACM0", "r") as device:
            for line in device:
                print(line)
    except Exception as e:
        print(f"Erreur : {e}")

