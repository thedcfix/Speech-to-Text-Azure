import azure.cognitiveservices.speech as speechsdk

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription="YOUR_SUBSCRIPTION", region="westeurope", speech_recognition_language="it-IT")
    audio_input = speechsdk.AudioConfig(filename="audio.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    result = speech_recognizer.recognize_once_async().get()
    print(result.text)

from_file()