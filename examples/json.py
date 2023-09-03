import oreille

print("Processing wav")
print(
    oreille.transcribe(
        "whisper-1",
        open("examples/test.wav", "rb"),
        language="fr",
        prompt="Test son",
        response_format="verbose_json",
        audio_format="wav",
    )
)
