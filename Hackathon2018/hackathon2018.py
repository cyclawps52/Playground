import speech_recognition as sr
import pyaudio
import os
import wave

def clearScreen():
    os.system('clear')

def transcribe():
    filePath = "speech.wav"
    r = sr.Recognizer()

    audioFile = sr.AudioFile(filePath)
    with audioFile as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
    except:
        text = "nothing"
    return text

def record():
    outputPath = "speech.wav"
    secondsToRecord = 5
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024

    audio = pyaudio.PyAudio()
 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Starting recording for {0} seconds...".format(secondsToRecord))
    frames = []
    counter = 4
    for i in range(0, int(RATE / CHUNK * secondsToRecord)):
        data = stream.read(CHUNK)
        frames.append(data)
        if(i % 43 == 0):
            print("Seconds left: {0}".format(counter))
            counter -= 1
    print("Finished recording, processing text...")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(outputPath, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def main():
    while True:
        clearScreen()
        record()
        text = transcribe()
        print("You said: {0}".format(text))
        for word in text.split(" "):
            if "starfish" == word:
                print("STARFISH FOUND")
                os.system("chrome tinyurl.com/hackStarfish &")
                break
            if "star" == word:
                print("STAR FOUND")
                os.system("chrome tinyurl.com/hackTomStar &")
                break
            if "fish" == word:
                print("FISH FOUND")
                os.system("chrome tinyurl.com/hackTomFish &")
                break

        print("Press ENTER to record again or type 'quit' to exit.")
        quitStr = str(input())
        os.system("killall chromium-browser")
        if quitStr == "quit":
            return

if __name__ == "__main__":
    main()
