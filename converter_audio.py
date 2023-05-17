from pybub import AudioSegment

sound = AudioSegment.from_mp3("import.mp3")
sound.export("output.wav", format="wav")