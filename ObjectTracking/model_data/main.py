from Detector import *
import os
from tkinter import *
from tkinter import filedialog
import customtkinter
 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()

def modelData(videoPath, model):
    vPath = videoPath
    configPath = None
    modelPath = None
    classesPath = None
    
    if getModel(model) == "SSD MobileNet":
        configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
        modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
        classesPath = os.path.join("model_data", "coco.names")
        modelType = 'SSD'
        confThreshold = conf_slider_var
        bValue = True
        detector = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, bValue)
        detector.onVideo()
	
    elif getModel(model) == "YOLOv3":
        configPath = os.path.join("model_data", "yolov3.cfg")
        modelPath = os.path.join("model_data", "yolov3.weights")
        classesPath = os.path.join("model_data", "cocoYOLO.names")
        modelType = 'YOLOv3'
        bValue = True
        confThreshold = conf_slider_var
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, bValue)
        detector4.onVideo()

    elif getModel(model) == "Reflective":
        configPath = os.path.join("model_data", "reflective.cfg")
        modelPath = os.path.join("model_data", "reflective.weights")
        classesPath = os.path.join("model_data", "reflective.names")
        modelType = 'Reflective'
        confThreshold = conf_slider_var
        bValue = True
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, bValue)
        detector4.onVideo()
	
    elif getModel(model) == "YOLOv3-tiny":
        configPath = os.path.join("model_data", "yolov3-tiny.cfg")
        modelPath = os.path.join("model_data", "yolov3-tiny.weights")
        classesPath = os.path.join("model_data", "cocoYOLO.names")
        modelType = 'YOLOv3-tiny'
        confThreshold = conf_slider_var
        bValue = False
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, bValue)
        detector4.onVideo()
    
def clickButton():
	videoPath = entryBox.get()
	if (videoPath == "0"):
		videoPath = 0

	model = model_menu.get()
	modelData(videoPath, model)

def clickButtonWebcam():
	global buttonClicked
	buttonClicked = not buttonClicked

	videoPath = 0
	model = model_menu.get()

	modelData(videoPath, model)

def change_appearance_mode_event(new_appearance_mode: str):
	customtkinter.set_appearance_mode(new_appearance_mode)
	print(new_appearance_mode)

def getModel(selected_value):
	print(f"Selected model: {selected_value}")
	return selected_value

## WINDOW SETTINGS
root.geometry(f"{720}x{320}")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure((2, 3), weight=1)
root.grid_rowconfigure((0,1,2), weight=1)

# SIDE BAR W/ OPTION MENU
root.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
root.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
root.sidebar_frame.grid_rowconfigure(4, weight=1)

sidebar_label = customtkinter.CTkLabel(root.sidebar_frame, text="Settings", font=("Helvetica", 14), pady=10)
sidebar_label.pack(fill="x")

root.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["Dark", "Light", "System"], command=change_appearance_mode_event)
root.appearance_mode_optionemenu.pack(fill="x", padx=10, pady=(0, 10))

## CHOOSE THE MODEL IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Model", font=("Helvetica", 14), pady=10)
root.sidebar_frame.model_label.pack(fill="x")

model_menu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["SSD MobileNet", "YOLOv3", "YOLOv3-tiny", "Reflective"], command=lambda value: getModel(value))
model_menu.pack(fill="x", padx=10, pady=(0, 10))

## CHOOSE THE CONFIDENCE IN SIDE BAR
conf_label_var = customtkinter.StringVar()
conf_label = customtkinter.CTkLabel(root.sidebar_frame, textvariable=conf_label_var, font=("Helvetica", 14), pady=10)
conf_label.pack(padx=10, pady=(0, 10))

conf_slider_var = customtkinter.DoubleVar(value=0.4)
conf_slider = customtkinter.CTkSlider(root.sidebar_frame, from_=0.1, to=0.99, variable=conf_slider_var, command=lambda value: conf_slider_var.set(float(value)))
conf_slider.pack(padx=10, pady=(0,10))

# set the label text to the initial value of the slider
conf_label_var.set(f"Confidence Value: {conf_slider_var.get():.2f}")

# update the label text whenever the slider value changes
conf_slider_var.trace_add("write", lambda name, index, mode, var=conf_slider_var, lbl=conf_label_var: lbl.set(f"Confidence Value: {var.get():.2f}"))

## CHOOSE BEAUTIFY IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Beautify", font=("Helvetica", 14), pady=10)
root.sidebar_frame.model_label.pack(fill="x")


## TAB SETTINGS
tabview = customtkinter.CTkTabview(root, width=250)
tabview.grid(row=0, column=2, padx=20, pady=(20, 0), sticky="")
tabview.add("Object Tracking Through Input File")
tabview.add("Object Tracking Through Webcam")
tabview.tab("Object Tracking Through Input File").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Object Tracking Through Webcam").grid_columnconfigure(0, weight=1)

## BUTTON FOR OBJECT TRACKING THROUGH INPUT FILE
myButton = customtkinter.CTkButton(tabview.tab("Object Tracking Through Input File"), text="Enter", command=clickButton)
myButton.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="")

## ENTRY FOR OBJECT TRACKING THROUGH INPUT FILE
entryBox = customtkinter.CTkEntry(tabview.tab("Object Tracking Through Input File"), placeholder_text="Path To File", width=300)
entryBox.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="")

## BUTTON FOR OBJECT TRACKING THROUGH WEBCAM
buttonClicked = False
myButton = customtkinter.CTkButton(tabview.tab("Object Tracking Through Webcam"), text="Press Button to Enable Webcam", command=clickButtonWebcam)
myButton.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="")
label_tab_2 = customtkinter.CTkLabel(tabview.tab("Object Tracking Through Webcam"), text="Press Q to Stop Webcam")
label_tab_2.grid(row=0, column=0, padx=20, pady=20, sticky="")


if __name__ == '__main__':
	root.title('Object Tracker GUI')
	root.mainloop()




