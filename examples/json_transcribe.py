import openai

import oreille

client = openai.OpenAI()

print("Processing wav")
print(
    oreille.transcribe(
        client,
        file=open("examples/test.wav", "rb"),
        model="whisper-1",
        language="fr",
        prompt="Test son",
        response_format="verbose_json",
        audio_format="wav",
    )
)
