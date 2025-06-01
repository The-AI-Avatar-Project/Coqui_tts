import subprocess
import os

def generiere_stimme(text, dateiname="ausgabe.wav"):
    """
    Diese Funktion ruft das Docker-Image von Coqui TTS auf, um eine Audioausgabe aus einem Text zu erzeugen.

    :param text: Der einzusprechende Text
    :param dateiname: Name der Ausgabedatei im Ordner 'output'
    """
    pfad = os.getcwd()
    output_pfad = os.path.join(pfad, "output")

    os.makedirs(output_pfad, exist_ok=True)

    befehl = [
        "docker", "run", "--rm",
        "-v", f"{output_pfad}:/output",
        "synesthesiam/coqui-tts",
        "--text", text,
        "--out_path", f"/output/{dateiname}"
    ]

    print(f"[INFO] Erzeuge Audio: '{text}' → output/{dateiname}")
    subprocess.run(befehl)

# Beispielaufruf
if __name__ == "__main__":
    generiere_stimme("Hallo! Willkommen im KI-Avatar-Projekt.", "willkommen.wav")