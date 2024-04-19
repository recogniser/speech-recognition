import os
wav_files = [file for file in os.listdir() if file.endswith('.wav')]

if wav_files:
    print("WAV file(s) available. Select which one to use:")
    
    for index, file_name in enumerate(wav_files, start=1):
        print(f"{index}. {file_name}")
    choice = input(f"Enter your choice (1 to {len(wav_files)}): ")
    
    try:
        choice_index=int(choice)-1
        selected_file=wav_files[choice_index]
        print(f"WAV file: {selected_file} is selected!")
        
        import speech_recognition as sr
        print("Processing...")
        r = sr.Recognizer()
        with sr.AudioFile(selected_file) as source:
            audio = r.record(source)
        try:
            print(r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))

    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")
else:
    print("No WAV files are available in the current directory.")
    input("--- Press ENTER To Exit ---")
