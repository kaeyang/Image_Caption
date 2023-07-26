from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
from io import BytesIO


# Using a pretrained BLIP Vision-Language Multimodal model from HuggingFace
# The specific version: BlipForConditionalGeneration, The model consists of a vision encoder and a text decoder
# https://huggingface.co/docs/transformers/model_doc/blip

processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")


def generate_caption(image_data):
    '''
    Using the pretrained BLIP model, it takes in an image and outputs a text caption to describe the image
    since the input from the API request is in bytes, I converted it back into an image before feeding it into the model
    '''
    image = Image.open(BytesIO(image_data))
    text = "A picture of"

    inputs = processor(images=image, text=text, return_tensors="pt")
    pixel_values = inputs.pixel_values
    generated_ids = model.generate(pixel_values=pixel_values, max_length=75)
    generated_caption = processor.batch_decode(
        generated_ids, skip_special_tokens=True)[0]

    return generated_caption
