import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QRadioButton, QButtonGroup, QMessageBox, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from pytube import YouTube
from pydub import AudioSegment

class DownloadThread(QThread):
    progress = pyqtSignal(int)
    error_signal = pyqtSignal(str)

    def __init__(self, url, path, file_format):
        super().__init__()
        self.url = url
        self.path = path
        self.file_format = file_format

    def run(self):
        try:
            yt = YouTube(self.url, on_progress_callback=self.progress_callback)
            if self.file_format == 'mp4':
                video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
                if not video_stream:
                    self.error_signal.emit('Video bulunamadı veya indirilemedi.')
                    return
                video_stream.download(self.path)
            elif self.file_format == 'mp3':
                audio_stream = yt.streams.filter(only_audio=True).first()
                if not audio_stream:
                    self.error_signal.emit('Ses dosyası bulunamadı veya indirilemedi.')
                    return
                audio_path = audio_stream.download(self.path)
                audio = AudioSegment.from_file(audio_path)
                audio.export(os.path.join(self.path, yt.title + '.mp3'), format='mp3')
                os.remove(audio_path)
            self.progress.emit(100)
        except Exception as e:
            self.error_signal.emit(str(e))

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress.emit(int(percentage_of_completion))

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Video ve Ses İndirici')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # YouTube Linki Girişi
        self.link_label = QLabel('YouTube Linki:', self)
        layout.addWidget(self.link_label)

        self.link_input = QLineEdit(self)
        layout.addWidget(self.link_input)

        # Kayıt Yeri Seçimi
        self.path_label = QLabel('Kayıt Yeri:', self)
        layout.addWidget(self.path_label)

        self.path_input = QLineEdit(self)
        layout.addWidget(self.path_input)

        self.browse_button = QPushButton('Gözat', self)
        self.browse_button.clicked.connect(self.browse_folder)
        layout.addWidget(self.browse_button)

        # Format Seçimi
        self.format_label = QLabel('Format Seçimi:', self)
        layout.addWidget(self.format_label)

        self.mp4_radio = QRadioButton('MP4', self)
        self.mp3_radio = QRadioButton('MP3', self)
        self.mp4_radio.setChecked(True)

        self.format_group = QButtonGroup(self)
        self.format_group.addButton(self.mp4_radio)
        self.format_group.addButton(self.mp3_radio)

        layout.addWidget(self.mp4_radio)
        layout.addWidget(self.mp3_radio)

        # İlerleme Çubuğu
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # İndirme Butonu
        self.download_button = QPushButton('İndir', self)
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Kayıt Yeri Seç')
        if folder:
            self.path_input.setText(folder)

    def start_download(self):
        url = self.link_input.text()
        path = self.path_input.text()
        file_format = 'mp4' if self.mp4_radio.isChecked() else 'mp3'

        if not url or not path:
            QMessageBox.warning(self, 'Hata', 'Lütfen tüm alanları doldurun!')
            return

        self.progress_bar.setValue(0)
        self.download_thread = DownloadThread(url, path, file_format)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.error_signal.connect(self.show_error)
        self.download_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        if value == 100:
            QMessageBox.information(self, 'Başarılı', 'İndirme tamamlandı!')

    def show_error(self, error_message):
        QMessageBox.critical(self, 'Hata', f'İndirme sırasında bir hata oluştu: {error_message}')
        self.progress_bar.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YouTubeDownloader()
    ex.show()
    sys.exit(app.exec_())
