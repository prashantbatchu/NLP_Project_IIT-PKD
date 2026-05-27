import soundfile as sf
import librosa

def convert_webm_to_wav(webm_path: str,wav_path: str,start_time: float = None,end_time: float = None):
    try:
        print(f"\n[CONVERT] Loading: {webm_path}")

        audio_data, sample_rate=librosa.load(
            str(webm_path),
            sr=16000,
            mono=True
        )

        print(f"Sample Rate: {sample_rate}")
        print(f"Total Samples: {len(audio_data)}")

        if start_time is not None and end_time is not None:

            print(f"\nTRIM From {start_time}s to {end_time}s")
            start_sample = int(start_time * sample_rate)
            end_sample = int(end_time * sample_rate)

            audio_data = audio_data[start_sample:end_sample]

            print(f"Trimmed Samples: {len(audio_data)}")

        print(f"\nSaving WAV to: {wav_path}")

        sf.write(
            str(wav_path),
            audio_data,
            sample_rate,
            subtype='PCM_16'
        )

        print("[SUCCESS] Conversion completed!")

    except Exception as e:
        print(f"[ERROR] Conversion failed: {e}")


if __name__ == "__main__":

    input_webm = "data/raw_audios/Mahagathbandhan/TejashwiYadavkarakat.webm"
    output_wav = "data/raw_audios/Mahagathbandhan/TejashwiYadavkarakat.wav"

    convert_webm_to_wav( webm_path=input_webm,wav_path=output_wav,start_time=3057,end_time=8990)