from abc import ABC, abstractmethod

class DocumentProcessor(ABC):
    @abstractmethod
    def process(self, document):
        pass

class TextProcessor(DocumentProcessor):
    def process(self, text):
        print("process text for search")

class ImageProcessor(DocumentProcessor):
    def process(self, image):
        print("Compress the image")

class VideoProcessor(DocumentProcessor):
    def process(self, video):
        print("process the video")

class DocumentManager:
    def __init__(self, processor):
        self.processor = processor
    
    def process_document(self, document):
        self.processor.process(document)

