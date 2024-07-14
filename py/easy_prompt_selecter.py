import os
import csv

def opencsv(file):
    f = open(file, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

def makePromptList(promptCSV):
    promptList = []
    for j in promptCSV:
        promptList.append(j[0])
    promptList.append('None')
    promptList = promptList[1:]
    return promptList

promptCSV = opencsv('../docu/styles.csv')
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
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("Positive_text", "Negative_text",)

    FUNCTION = "read"

    CATEGORY = "Prompt"
    OUTPUT_NODE = True
    def read(self, select_preset,promptCSV, promptList):
        CSVindex = promptList.index(select_preset)
        posiText = promptCSV[CSVindex+1][1]
        negaText = promptCSV[CSVindex+1][2]
        # return [posiText, negaText]
        return {"result": (posiText,negaText,),}


NODE_CLASS_MAPPINGS = {
    "prompt": promptSelecter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "promptSelecter": "easy Prompt Selecter"
}