import io
from PIL import Image
import cairosvg
import torch
from typing import List

def svg_string_to_image(svg_string: str) -> Image.Image:
    png_data = cairosvg.svg2png(bytestring=svg_string.encode('utf-8'))
    return Image.open(io.BytesIO(png_data))

def pil2tensor(image: Image.Image) -> torch.Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class SVGPreview:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "svg_strings": ("LIST", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preview_svg"

    CATEGORY = "💎TOSVG"

    def preview_svg(self, svg_strings: List[str]):
        preview_images = []
        for svg_string in svg_strings:
            image = svg_string_to_image(svg_string)
            tensor_image = pil2tensor(image)
            preview_images.append(tensor_image)
        return (preview_images,)
