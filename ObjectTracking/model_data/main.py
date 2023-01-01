from Detector import *
import os
from tkinter import *
from tkinter import filedialog
import customtkinter
 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()

def clickButton():
	vPath = entryBox.get()
	if (vPath == "0"):
		vPath = 0

	videoPath = vPath #"test_videos/carshowTEST2.mp4"
	configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
	modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
	classesPath = os.path.join("model_data", "coco.names")

	detector = Detector(videoPath, configPath, modelPath, classesPath)
	detector.onVideo()

def clickButtonWebcam():
	global buttonClicked
	buttonClicked = not buttonClicked

	videoPath = 0
	configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
	modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
	classesPath = os.path.join("model_data", "coco.names")

	detector = Detector(videoPath, configPath, modelPath, classesPath)
	detector.onVideo()

## WINDOW SETTINGS
root.geometry(f"{500}x{300}")

## TAB SETTINGS
tabview = customtkinter.CTkTabview(root, width=250)
tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
tabview.add("Object Tracking Through Input File")
tabview.add("Object Tracking Through Webcam")
tabview.tab("Object Tracking Through Input File").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Object Tracking Through Webcam").grid_columnconfigure(0, weight=1)
#label_tab_2 = customtkinter.CTkLabel(tabview.tab("Object Tracking Through Webcam"))
#label_tab_2.grid(row=0, column=0, padx=20, pady=20)

## BUTTON FOR OBJECT TRACKING THROUGH INPUT FILE
myButton = customtkinter.CTkButton(tabview.tab("Object Tracking Through Input File"), text="Enter", command=clickButton)
myButton.grid(row=2, column=0, padx=20, pady=(20, 10))

## ENTRY FOR OBJECT TRACKING THROUGH INPUT FILE
entryBox = customtkinter.CTkEntry(tabview.tab("Object Tracking Through Input File"), placeholder_text="Path To File", width=300)
entryBox.grid(row=1, column=0, padx=20, pady=(20, 20))

## BUTTON FOR OBJECT TRACKING THROUGH WEBCAM
buttonClicked = False
myButton = customtkinter.CTkButton(tabview.tab("Object Tracking Through Webcam"), text="Press Button to Enable Webcam", command=clickButtonWebcam)
myButton.grid(row=2, column=0, padx=20, pady=(20, 10))
label_tab_2 = customtkinter.CTkLabel(tabview.tab("Object Tracking Through Webcam"), text="Press Q to Stop Webcam")
label_tab_2.grid(row=0, column=0, padx=20, pady=20)


if __name__ == '__main__':
	root.title('Object Tracker GUI')
	root.mainloop()

