from Detector import *
import os
from tkinter import *
from tkinter import filedialog
import customtkinter
 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()

def clickButton():
	vPath = e.get()
	if (vPath == "0"):
		vPath = 0

	videoPath = vPath #"test_videos/carshowTEST2.mp4"
	configPath = os.path.join("model_data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
	modelPath = os.path.join("model_data", "frozen_inference_graph.pb")
	classesPath = os.path.join("model_data", "coco.names")

	detector = Detector(videoPath, configPath, modelPath, classesPath)
	detector.onVideo()

if __name__ == '__main__':
	root.title('Object Tracker GUI')
	window = root.geometry(f"{1100}x{580}")
	e = customtkinter.CTkEntry(root, placeholder_text="Path To File", width=300)
	e.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

	myButton = customtkinter.CTkButton(root, text='Enter', command=clickButton)
	myButton.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

	root.mainloop()

