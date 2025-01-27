import sounddevice as sd
from scipy.io.wavfile import write
import os


def ses_kayit_edici(dosya_adi="kayit.wav", sure=5, ornekleme_orani=44100):
    """
    Ses kaydedici işlevi.

    :param dosya_adi: Kaydedilecek dosyanın adı
    :param sure: Kaydetme süresi (saniye)
    :param ornekleme_orani: Sesin örnekleme oranı (Hz)
    """
    print(f"{sure} saniye boyunca ses kaydediliyor...")

    try:
        # Ses kaydı al
        kayit = sd.rec(int(sure * ornekleme_orani), samplerate=ornekleme_orani, channels=2, dtype="int16")
        sd.wait()  # Kayıt işleminin tamamlanmasını bekle
        write(dosya_adi, ornekleme_orani, kayit)
        print(f"Ses başarıyla '{dosya_adi}' olarak kaydedildi!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


# Kullanım
if __name__ == "__main__":
    # Dosya adı ve süresi kullanıcıdan alınabilir
    dosya = input("Kaydedilecek dosya adını (ör: ses_kayit.wav) girin: ") or "kayit.wav"
    sure = int(input("Kaç saniye kayıt yapmak istiyorsunuz?: ") or 5)
    ses_kayit_edici(dosya_adi=dosya, sure=sure)
