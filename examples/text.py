import ecoute

print("Processing wav")
print(ecoute.transcribe("whisper-1", open("examples/test.wav", "rb"), language="fr",
      prompt="Test son", response_format="text", audio_format="wav"))
