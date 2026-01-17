from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-base-handwritten"
)
model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-handwritten"
).to(DEVICE)

model.eval()

def extract_handwritten_text(image: Image.Image) -> str:
    pixel_values = processor(
        image, return_tensors="pt"
    ).pixel_values.to(DEVICE)

    with torch.no_grad():
        ids = model.generate(pixel_values)

    return processor.batch_decode(
        ids, skip_special_tokens=True
    )[0]
