import sounddevice as sd
from scipy.io.wavfile import write

def ses_kayit_edici(dosya_adi="kayit.wav", sure=5, ornekleme_orani=44100):
    print(f"{sure} saniye boyunca ses kaydediliyor...")

    try:
        # Mikrofonun desteklediği kanal sayısını kontrol edin
        device_info = sd.query_devices(sd.default.device[0], 'input')
        max_channels = device_info['max_input_channels']

        # Mikrofonun desteklediği kanallara uygun olarak ayar yap
        channels = 1 if max_channels == 1 else 2

        # Ses kaydı başlat
        kayit = sd.rec(int(sure * ornekleme_orani), samplerate=ornekleme_orani, channels=channels, dtype="int16")
        sd.wait()  # Kayıt işlemini tamamla
        write(dosya_adi, ornekleme_orani, kayit)
        print(f"Ses başarıyla '{dosya_adi}' olarak kaydedildi!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Kullanım
if __name__ == "__main__":
    ses_kayit_edici()
