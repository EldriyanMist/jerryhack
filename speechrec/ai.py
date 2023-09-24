import assemblyai as aai

# replace with your API token
aai.settings.api_key = f"1598a0cf76f04535b56b0ec4e0c2da90"

# URL of the file to transcribe
transcriber = aai.Transcriber()
transcript = transcriber.transcribe("./audio-recording.wav")

print(transcript.text)