import sounddevice as sd
import numpy as np
import simpleaudio as sa
import os
import wave
import tempfile
import threading

def record_audio(filename, duration=None, fs=44100):
    if duration:
        print(f"Recording for {duration} seconds...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float32')
        sd.wait()
    else:
        print("Recording... Press 'Ctrl+C' to stop.")
        # Start an indefinite recording session
        recording = []
        with sd.InputStream(samplerate=fs, channels=2, dtype='float32') as stream:
            try:
                while True:
                    data, overflowed = stream.read(fs)  # Read one second at a time
                    if overflowed:
                        print("Warning: audio buffer overflowed.")
                    recording.append(data)
            except KeyboardInterrupt:
                pass  # Stop recording on Ctrl+C
        # Concatenate all recorded chunks
        recording = np.concatenate(recording, axis=0)
    write_wave(filename, recording, fs)
    print("Recording stopped.")

def write_wave(filename, data, fs):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(np.int16(data * 32767).tobytes())

def play_audio(filename):
    try:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except FileNotFoundError:
        print("File not found. Please check the filename.")

def list_recordings(directory):
    print("Recordings:")
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            print(file)

def delete_recording(directory):
    list_recordings(directory)
    filename = input("Enter the filename to delete (without extension): ") + ".wav"
    path = os.path.join(directory, filename)
    try:
        os.remove(path)
        print(f"Deleted {filename}")
    except FileNotFoundError:
        print("File not found. Please check the filename.")

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
    records_dir = os.path.join(root_dir, "records")
    os.makedirs(records_dir, exist_ok=True)  # Create the records directory if it doesn't exist

    print("KISS Audio Rec")
    print("1. Record Audio for 5 minutes")
    print("2. Record Audio for 10 minutes")
    print("3. Record Audio for 1 hour")
    print("4. Record Audio for 3 hours")
    print("5. Record Audio until stopped")
    print("6. Play Recording")
    print("7. List Recordings")
    print("8. Delete Recording")
    print("9. Exit")
    
    duration_mapping = {
        '1': 300,
        '2': 600,
        '3': 3600,
        '4': 10800,
        '5': None
    }
    
    while True:
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', '4', '5']:
            filename = os.path.join(records_dir, input("Enter filename (without extension): ") + ".wav")
            record_audio(filename, duration=duration_mapping[choice])
        elif choice == '6':
            filename = os.path.join(records_dir, input("Enter filename to play (without extension): ") + ".wav")
            play_audio(filename)
        elif choice == '7':
            list_recordings(records_dir)
        elif choice == '8':
            delete_recording(records_dir)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()