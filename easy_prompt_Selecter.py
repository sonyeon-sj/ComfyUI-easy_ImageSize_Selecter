import os
import csv


global promptCSV, promptList

# PATH = os.getcwd() + '\\custom_nodes\\ComfyUI-easy_ImageSize_Selecter\\doc'
# os.chdir(PATH)

def opencsv(filepath):
    f = open(filepath, 'r',encoding='utf-8')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

def makePromptList(promptCSV):
    promptList = []
    for j in promptCSV:
        promptList.append(j[0])
    promptList = promptList[1:]
    return promptList

promptCSV = opencsv('custom_nodes/ComfyUI-easy_ImageSize_Selecter/doc/styles.csv')
if promptCSV[-1][0] != 'None':
    promptCSV.append(['None','',''])
else:
    pass

promptList = makePromptList(promptCSV)
    


class promptSelecter:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "select_preset": (promptList,{"default": promptList[-1]}),
                # "direction": ([ "Vertical","Horizon"],{"default": "Vertical"})
            },
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("Positive_text", "Negative_text",)

    FUNCTION = "readPrompt"

    CATEGORY = "Prompt"
    OUTPUT_NODE = True
    
    def readPrompt(self, select_preset):
        CSVindex = promptList.index(select_preset)
        posiText = promptCSV[CSVindex+1][1]
        negaText = promptCSV[CSVindex+1][2]
        # return [posiText, negaText]
        return {
            "result": (
                posiText,
                negaText,
                ),
            }


#NODE_CLASS_MAPPINGS = {
#    "promptSelecter": promptSelecter
#}

#NODE_DISPLAY_NAME_MAPPINGS = {
#    "promptSelecter": "easy Prompt Selecter"
#}