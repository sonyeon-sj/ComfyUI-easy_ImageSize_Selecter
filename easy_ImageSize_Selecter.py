
class ImageSizer:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_type": (["SD_1:1_512*512", "SD_2:3_512*768",
                                "XL_1:1_1024*1024", "XL_2:3_832*1216", "XL_16:9_1344*768", "XL_21:9_1536*640",
                                "flux1MP_1:1_1024*1024", "flux1MP_2:3_836*1254", "flux1MP_3:4_887*1182", "flux1MP_16:9_1356*768", "flux1MP_21:9_1564*670",
                                "flux2MP_1:1_1448*1448", "flux2MP_2:3_1182*1773", "flux2MP_3:4_1254*1672", "flux2MP_16:9_1936*1089", "flux2MP_21:9_2212*948",
                                "SVD_1024*576"], {"default": "XL_2:3_832*1216"}),
                "direction": (["Vertical", "Horizon"], {"default": "Vertical"})
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("Width", "Height",)

    FUNCTION = "run"

    CATEGORY = "SizeFromPresets"
    OUTPUT_NODE = True

    def run(self, model_type, direction):
        find_indexList = ["SD_1:1_512*512", "SD_2:3_512*768",
                          "XL_1:1_1024*1024", "XL_2:3_832*1216", "XL_16:9_1344*768", "XL_21:9_1536*640",
                          "flux1MP_1:1_1024*1024", "flux1MP_2:3_836*1254", "flux1MP_3:4_887*1182", "flux1MP_16:9_1356*768", "flux1MP_21:9_1564*670",
                          "flux2MP_1:1_1448*1448", "flux2MP_2:3_1182*1773", "flux2MP_3:4_1254*1672", "flux2MP_16:9_1936*1089", "flux2MP_21:9_2212*948",
                          "SVD_1024*576"]
        find_resolList = [(512, 512), (512, 768),
                          (1024, 1024), (832, 1216), (1344, 768), (1536, 640),
                          (1024, 1024), (836, 1254), (887,
                                                      1182), (1356, 768), (1564, 670),
                          (1448, 1448), (1182, 1773), (1254,
                                                       1672), (1936, 1089), (2212, 948),
                          (1024, 576)]
        width, height = find_resolList[find_indexList.index(model_type)]
        if direction == "Vertical":
            if width > height:
                new_width = height
                height = width
                width = new_width
            else:
                pass
        else:  # horizon
            if width < height:
                new_width = height
                height = width
                width = new_width
            else:
                pass
        text1 = str(width)+' x '+str(height)
        # return (int(round(width)), int(round(height)),{"ui": {"text": text, f"SetResolution: {text}"})
        return {
            "ui": {"value": [text1]
                   },
            "result": (
                int(round(width)),
                int(round(height)),
            ),
        }

# NODE_CLASS_MAPPINGS = {
#    "ImageSizer": ImageSizer
# }

# NODE_DISPLAY_NAME_MAPPINGS = {
#    "ImageSizer": "easy ImageSize Selecter"
# }
