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
	
        detector = Detector(vPath, configPath, modelPath, classesPath, modelType)
        detector.onVideo()
	
    elif getModel(model) == "YOLOv3":
        configPath = os.path.join("model_data", "yolov3.cfg")
        modelPath = os.path.join("model_data", "yolov3.weights")
        classesPath = os.path.join("model_data", "cocoYOLO.names")
        modelType = 'YOLO'
	
        detector2 = Detector(vPath, configPath, modelPath, classesPath, modelType)
        detector2.onVideo()
	
    
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

model_menu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["SSD MobileNet", "YOLOv3"], command=lambda value: getModel(value))
model_menu.pack(fill="x", padx=10, pady=(0, 10))

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



