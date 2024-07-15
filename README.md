# ComfyUI-easy-ImageSize-Selecter

---

First of all, I tell you that I don't know how to programming. I just made it.
However, it works well.

---

**Custom node for ComfyUI**
Select the image size from the preset and select Vertical and Horizontal to output Width and Height.

In comfyUI, there is no use except for the 7 sizes shown here.This is because the models learned at a fixed size.
You just have to decide whether it's horizontal or vertical

### How to use it

![screenshot1](./images/screenshot01.png)
just select presets (size & direction)
Then, it will export the width and height as INT.

In comfyUI, there are a lot of image size input fields. You can use it after pulling it.

![screenshot1](./images/screenshot03.png)
Incase of nodes with built-in width and height inputs:
Right-click the mouse > Convert Widget to Input > Convert width(height) to input
![screenshot1](./images/screenshot04.png)

---

# Bonus features

## ComfyUI-easy-Prompt-Selecter

This is a node that enables you to use the Preset prompt that you used in the A1111 webui.
![screenshot1](./images/screenshot05.png)
![screenshot1](./images/screenshot06.png)
![screenshot1](./images/screenshot07.png)

Overwrite the A1111_webui\styles.csv file that you were using
to the `custom_nodes\ComfyUI-easy_ImageSize_Selecter\doc` folder and restart comfyui
