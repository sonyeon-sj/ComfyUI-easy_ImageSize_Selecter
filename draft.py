import csv

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

promptCSV = opencsv('./doc/styles.csv')
if promptCSV[-1][0] != 'None':
    promptCSV.append(['None','',''])
else:
    pass


promptList = makePromptList(promptCSV)


prom = [
    ['\ufeffname', 'prompt', 'negative_prompt'], 
    ['----Positive----', '', ''], 
    ['실사', 'masterpiece, best quality, high quality, 8k, 4k, UHD, photorealistic, realistic, RAW photo, ultra high res, highres, extremely detailed, finely detail, 8k wallpaper,five_finger,(((perfect hands))),', 'watermark, text, signature, logo, drawing, sketch, painting, pixelate, monochrome, grayscale'], 
    ['실사(흑백)', '((monochrome)), ((grayscale)), (b&w, Monochromatic, Film Photography:1.3), film noir, masterpiece, best quality, high quality, 8k, 4k, UHD, photorealistic, realistic, RAW photo, ultra high res, highres, extremely detailed, finely detail, 8k wallpaper, analog style, film photography, soft focus,five_finger,(((perfect hands))),', '((color photo)), watermark, text, signature, logo, drawing, sketch, painting, pixelate,'], 
    ['반실사', 'detailed beautiful eyes and detailed face, elaborate features, physically-based rendering, masterpiece, high quality, best quality, uhd, 8k, ultra-detailed, ', ''], 
    ['웹툰스타일', 'masterpiece,high_quality,five_finger,(((perfect hands))), (best quality, ultra detailed), Webtoon, cartoon style, manga, vivid color, Illustration anime, dynamic pose, trending on pixiv, digital painting, sehele style,', ''], 
    ['스케치', '((monochrome)), ((grayscale)), (greyscale,monochrome,sketch), line drawing, black and white drawing, ((sketching_style)), high_quality,five_finger, (best quality),', 'low contrast, photorealism, geometric patterns, photograph,'], 
    ['----Negative----', '', ''], 
    ['화질(실사) Negative', '', 'watermark, text, signature, logo, drawing, sketch, painting, pixelate, unsharp, bad quality, low quality, weird iris, (worst quality:2), (normal quality:2), low res,'], 
    ['인체 Negative', '', 'mosaic face, deformed face, weird pupil, deformed feet, tattoo, deformed eyes, weird eyes, ugly teeth, bad teeth, bad lips, deformed lips, missing fingers, extra fingers, weird legs, weird feet, weird hand, extra hands, deformed hands, deformed fingers, deformed body parts, heavy makeup, extra limb, ugly,missing limb, floating limbs, disconnected limbs, bad leg anatomy, bad hand anatomy, bad finger anatomy,'], 
    ['NSFW', '', 'NSFW, adult content,'], 
    ['None', '', '']]

def readPrompt(select_preset,promptCSV, promptList):
    CSVindex = promptList.index(select_preset)
    posiText = promptCSV[CSVindex+1][1]
    negaText = promptCSV[CSVindex+1][2]
    # return [posiText, negaText]
    return {"result": (posiText,negaText,),}

select_preset = '스케치'
promptOut = readPrompt(select_preset,promptCSV,promptList)
print(promptOut['result'])
