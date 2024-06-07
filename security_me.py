import cv2
import datetime
import time
import os  

# Konstanta
SECONDS_TO_RECORD_AFTER_DETECTION = 5
FOURCC = cv2.VideoWriter_fourcc(*"mp4v") 

# Memuat Haarcascades
FACE_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
BODY_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Inisialisasi variabel
DETECTION = False
DETECTION_STOPPED_TIME = None
OUT = None
CAP = None

def create_video_folder():
    """
    Membuat folder untuk menyimpan video dengan nama yang sesuai dengan tanggal saat video dibuat.

    Returns:
        str: Nama folder yang dibuat.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    folder_name = f"video_{current_date}"

    # Membuat folder jika belum ada
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    return folder_name

def start_recording(current_time):
    """
    Memulai perekaman video saat terdeteksi gerakan.

    Args:
        current_time (str): Timestamp saat ini diformat sebagai string, digunakan sebagai nama file video.

    Returns:
        None
    """
    global OUT, FRAME_WIDTH, FRAME_HEIGHT, CAP

    folder_name = create_video_folder()  # Membuat folder untuk menyimpan video
    file_path = os.path.join(folder_name, f"{current_time}.mp4")  # Path lengkap ke file video
    
    FRAME_WIDTH = int(CAP.get(3))
    FRAME_HEIGHT = int(CAP.get(4))
    OUT = cv2.VideoWriter(file_path, FOURCC, 20.0, (FRAME_WIDTH, FRAME_HEIGHT))
    print("Perekaman Dimulai!")

def stop_recording():
    """
    Menghentikan perekaman video.

    Returns:
        None
    """
    global OUT
    if OUT is not None:
        OUT.release()
        OUT = None
        print("Perekaman Berhenti!")

def main():
    """
    Fungsi utama yang menjalankan sistem deteksi gerakan.

    Returns:
        None
    """
    global DETECTION, DETECTION_STOPPED_TIME, CAP

    # Membuka perangkat tangkap video
    CAP = cv2.VideoCapture(0)

    # Memeriksa apakah kamera berhasil dibuka
    if not CAP.isOpened():
        print("Error membuka aliran video atau file")
        return

    while CAP.isOpened():
        ret, frame = CAP.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Mendeteksi wajah dan tubuh
            faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
            bodies = BODY_CASCADE.detectMultiScale(gray, 1.3, 5)

            # Menghandle kejadian deteksi
            if len(faces) + len(bodies) > 0:
                if not DETECTION:
                    DETECTION = True
                    current_time = datetime.datetime.now().strftime("%H-%M-%S")
                    start_recording(current_time)
            elif DETECTION:
                if DETECTION_STOPPED_TIME is not None:
                    if time.time() - DETECTION_STOPPED_TIME >= SECONDS_TO_RECORD_AFTER_DETECTION:
                        DETECTION = False
                        DETECTION_STOPPED_TIME = None
                        stop_recording()
                else:
                    DETECTION_STOPPED_TIME = time.time()

            # Merekam frame jika deteksi aktif
            if DETECTION:
                OUT.write(frame)

            # Menampilkan persegi panjang di sekitar wajah yang terdeteksi
            for (x, y, width, height) in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    # Melepaskan sumber daya
    stop_recording()
    CAP.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
