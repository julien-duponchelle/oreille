import ecoute

print("Processing wav")
print(ecoute.transcribe("whisper-1", open("examples/test.wav", "rb"), language="fr",
      prompt="Test son", response_format="verbose_json", audio_format="wav"))

# '{"task": "transcribe", "language": "french", "duration": 2.79, "text": "Ceci est un test de \\u00c9coute, ma biblioth\\u00e8que de transcription.", "segments": [{"id": 0, "seek": 0, "start": 0.0, "end": 2.8000000000000003, "text": " Ceci est un test de \\u00c9coute, ma biblioth\\u00e8que de transcription.", "tokens": [50364, 8257, 537, 871, 517, 1500, 368, 4922, 66, 14040, 11, 463, 272, 11476, 72, 900, 1462, 1077, 368, 35288, 13, 50504], "temperature": 0.0, "avg_logprob": -0.32106150751528534, "compression_ratio": 0.9402985074626866, "no_speech_prob": 0.03250369429588318}]}'