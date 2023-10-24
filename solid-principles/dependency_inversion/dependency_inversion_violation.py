class TextProcessor:
    def process_text(self, text):
        # Index the text for search
        pass

class ImageProcessor:
    def process_image(self, image):
        # Compress the image
        pass

class VideoProcessor:
    def process_video(self, video):
        # Transcode the video into different formats
        pass

class DocumentManager:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.image_processor = ImageProcessor()
        self.video_processor = VideoProcessor()
    
    def process_document(self, document):
        if isinstance(document, str):
            self.text_processor.process_text(document)
        elif isinstance(document, bytes):
            self.image_processor.process_image(document)
        elif isinstance(document, bytearray):
            self.video_processor.process_video(document)
