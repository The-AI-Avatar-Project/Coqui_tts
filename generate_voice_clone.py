import subprocess
import os

def generiere_stimme(speaker_name, text, dateiname="ausgabe.wav"):
    """
    Generiert eine synthetisierte Sprache mit einer geklonten Stimme.
    """
    pfad = os.getcwd()
    samples_pfad = os.path.join(pfad, "samples")
    output_pfad = os.path.join(pfad, "output")

    os.makedirs(output_pfad, exist_ok=True)

    befehl = [
        "docker", "run", "--rm",
        "-v", f"{output_pfad}:/output",
        "-v", f"{samples_pfad}:/samples",
        "coqui-tts-custom",  # <-- Nom réel de ton image Docker
        "--text", text,
        "--speaker_wav", f"/samples/{speaker_name}.wav",
        "--out_path", f"/output/{dateiname}"
    ]

    print(f"[INFO] Erzeuge geklonte Stimme von '{speaker_name}': '{text}' → output/{dateiname}")
    subprocess.run(befehl)

# Beispiel
if __name__ == "__main__":
    generiere_stimme("prof1", "Guten Morgen, Klasse!", "prof1_morgen.wav")