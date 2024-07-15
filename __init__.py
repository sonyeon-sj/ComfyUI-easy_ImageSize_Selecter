from .easy_ImageSize_Selecter import *
from .easy_prompt_Selecter import *


    
NODE_CLASS_MAPPINGS = {
    "ImageSizer": ImageSizer,
    "promptSelecter": promptSelecter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSizer": "easy ImageSize Selecter",
    "promptSelecter": "easy Prompt Selecter",
}