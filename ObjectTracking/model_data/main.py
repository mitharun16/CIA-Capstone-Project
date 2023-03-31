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
        sThreshold = sThreshold_slider_var
        nmsThreshold = nmsThreshold_slider_var
        bValue = bValue_var
        detector = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, sThreshold, nmsThreshold, bValue)
        detector.onVideo()
	
    elif getModel(model) == "YOLOv3":
        configPath = os.path.join("model_data", "yolov3.cfg")
        modelPath = os.path.join("model_data", "yolov3.weights")
        classesPath = os.path.join("model_data", "cocoYOLO.names")
        modelType = 'YOLOv3'
        bValue = bValue_var
        confThreshold = conf_slider_var
        sThreshold = sThreshold_slider_var
        nmsThreshold = nmsThreshold_slider_var
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, sThreshold, nmsThreshold, bValue)
        detector4.onVideo()

    elif getModel(model) == "Reflective":
        configPath = os.path.join("model_data", "reflective.cfg")
        modelPath = os.path.join("model_data", "reflective.weights")
        classesPath = os.path.join("model_data", "reflective.names")
        modelType = 'Reflective'
        confThreshold = conf_slider_var
        sThreshold = sThreshold_slider_var
        nmsThreshold = nmsThreshold_slider_var
        bValue = bValue_var
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, sThreshold, nmsThreshold, bValue)
        detector4.onVideo()
	
    elif getModel(model) == "YOLOv3-tiny":
        configPath = os.path.join("model_data", "yolov3-tiny.cfg")
        modelPath = os.path.join("model_data", "yolov3-tiny.weights")
        classesPath = os.path.join("model_data", "cocoYOLO.names")
        modelType = 'YOLOv3-tiny'
        confThreshold = conf_slider_var
        sThreshold = sThreshold_slider_var
        nmsThreshold = nmsThreshold_slider_var
        bValue = bValue_var
        detector4 = Detector(vPath, configPath, modelPath, classesPath, modelType, confThreshold, sThreshold, nmsThreshold, bValue)
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

def getBeautify(selected_value):
	print(f"Beautify Selected (Yes/No): {selected_value}")
	global beautify_value
	beautify_value = selected_value

## WINDOW SETTINGS
root.geometry(f"{1190}x{620}")
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

## CHOOSE BEAUTIFY IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Beautify", font=("Helvetica", 14), pady=10)
root.sidebar_frame.model_label.pack(fill="x")

bValue_var = customtkinter.StringVar()
beautify_menu = customtkinter.CTkOptionMenu(root.sidebar_frame, variable=bValue_var, values=["Yes", "No"], command=lambda value: bValue_var.set(value))
beautify_menu.pack(fill="x", padx=10, pady=(0, 10))

## CHOOSE THE MODEL IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Model", font=("Helvetica", 14), pady=10)
root.sidebar_frame.model_label.pack(fill="x")

model_menu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=["SSD MobileNet", "YOLOv3", "YOLOv3-tiny", "Reflective"], command=lambda value: getModel(value))
model_menu.pack(fill="x", padx=10, pady=(0, 10))

## CHOOSE THE CONFIDENCE IN SIDE BAR
conf_label_var = customtkinter.StringVar()
conf_label = customtkinter.CTkLabel(root.sidebar_frame, textvariable=conf_label_var, font=("Helvetica", 14), pady=10)
conf_label.pack(padx=10, pady=(0, 10))

conf_slider_var = customtkinter.DoubleVar(value=0.5)
conf_slider = customtkinter.CTkSlider(root.sidebar_frame, from_=0.1, to=0.99, variable=conf_slider_var, command=lambda value: conf_slider_var.set(float(value)))
conf_slider.pack(padx=10, pady=(0,10))

## CHOOSE THE SCORE THRESHOLD IN SIDE BAR
sThreshold_label_var = customtkinter.StringVar()
sThreshold_label = customtkinter.CTkLabel(root.sidebar_frame, textvariable=sThreshold_label_var, font=("Helvetica", 14), pady=10)
sThreshold_label.pack(padx=10, pady=(0, 10))

sThreshold_slider_var = customtkinter.DoubleVar(value=0.5)
sThreshold_slider = customtkinter.CTkSlider(root.sidebar_frame, from_=0.1, to=0.99, variable=sThreshold_slider_var, command=lambda value: sThreshold_slider_var.set(float(value)))
sThreshold_slider.pack(padx=10, pady=(0,10))

## CHOOSE THE NMS THRESHOLD IN SIDE BAR
nmsThreshold_label_var = customtkinter.StringVar()
nmsThreshold_label = customtkinter.CTkLabel(root.sidebar_frame, textvariable=nmsThreshold_label_var, font=("Helvetica", 14), pady=10)
nmsThreshold_label.pack(padx=10, pady=(0, 10))

nmsThreshold_slider_var = customtkinter.DoubleVar(value=0.5)
nmsThreshold_slider = customtkinter.CTkSlider(root.sidebar_frame, from_=0.1, to=0.99, variable=nmsThreshold_slider_var, command=lambda value: nmsThreshold_slider_var.set(float(value)))
nmsThreshold_slider.pack(padx=10, pady=(0,10))

# set the label text to the initial value of the slider
conf_label_var.set(f"Confidence Value: {conf_slider_var.get():.2f}")

# update the label text whenever the slider value changes
conf_slider_var.trace_add("write", lambda name, index, mode, var=conf_slider_var, lbl=conf_label_var: lbl.set(f"Confidence Value: {var.get():.2f}"))

# set the label text to the initial value of the slider
sThreshold_label_var.set(f"Score Threshold: {sThreshold_slider_var.get():.2f}")

# update the label text whenever the slider value changes
sThreshold_slider_var.trace_add("write", lambda name, index, mode, var=sThreshold_slider_var, lbl=sThreshold_label_var: lbl.set(f"Score Threshold: {var.get():.2f}"))

# set the label text to the initial value of the slider
nmsThreshold_label_var.set(f"NMS Threshold: {nmsThreshold_slider_var.get():.2f}")

# update the label text whenever the slider value changes
nmsThreshold_slider_var.trace_add("write", lambda name, index, mode, var=nmsThreshold_slider_var, lbl=nmsThreshold_label_var: lbl.set(f"NMS Threshold: {var.get():.2f}"))

## CHOOSE INPUT IMAGE SIZE IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Batch Size", font=("Helvetica", 14), pady=10)
root.sidebar_frame.model_label.pack(fill="x")

## CHOOSE INPUT IMAGE SIZE IN SIDE BAR
root.sidebar_frame.model_label = customtkinter.CTkLabel(root.sidebar_frame, text="Input Image Size", font=("Helvetica", 14), pady=10)
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

label_tab_2 = customtkinter.CTkLabel(tabview.tab("Object Tracking Through Input File"), text="Press Q to Stop The Video")
label_tab_2.grid(row=0, column=0, padx=20, pady=20, sticky="")

## ENTRY FOR OBJECT TRACKING THROUGH INPUT FILE
entryBox = customtkinter.CTkEntry(tabview.tab("Object Tracking Through Input File"), placeholder_text="Path To File", width=300)
entryBox.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="")

## BUTTON FOR OBJECT TRACKING THROUGH WEBCAM
buttonClicked = False
myButton = customtkinter.CTkButton(tabview.tab("Object Tracking Through Webcam"), text="Press Button to Enable Webcam", command=clickButtonWebcam)
myButton.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="")
label_tab_3 = customtkinter.CTkLabel(tabview.tab("Object Tracking Through Webcam"), text="Press Q to Stop Webcam")
label_tab_3.grid(row=0, column=0, padx=20, pady=20, sticky="")

## CREATE TABVIEW2 FOR RECOMMENDED SETTINGS
tabview2 = customtkinter.CTkTabview(root, width=900, height = 300)
tabview2.grid(row=1, column=2, padx=20, pady=(20, 0), sticky="")

## SSD Mobilenet recommended settings
tabview2.add("SSD MobileNet")
ssd_settings_label = customtkinter.CTkLabel(tabview2.tab("SSD MobileNet"), text="SSD mobilenet is a powerful object detection algorithm, but it requires some tuning to achieve good results. Here are some recommended settings:\n\n- Confidence threshold: 0.5\n- Non-maximum suppression threshold: 0.5\n- Input image size: 300x300\n- Number of channels: 3\n- Mean values: (127.5, 127.5, 127.5)\n- Scale factor: 0.007843\n\nNote that these settings may vary depending on your specific use case and dataset.", font=("Helvetica", 14), pady=10, padx=10)
ssd_settings_label.pack(fill="x")

## YOLOv3 recommended settings
tabview2.add("YOLOv3")
yolov3_settings_label = customtkinter.CTkLabel(tabview2.tab("YOLOv3"), text="YOLOv3 is a powerful object detection algorithm, but it requires some tuning to achieve good results. Here are some recommended settings:\n\n- Confidence threshold: 0.5\n- Non-maximum suppression threshold: 0.5\n- Input image size: 416x416\n- Number of channels: 3\n- Mean values: (0,0,0)\n- Scale factor: 0.00392\n\nNote that these settings may vary depending on your specific use case and dataset.", font=("Helvetica", 14), pady=10, padx=10)
yolov3_settings_label.pack(fill="x")

## YOLOv3-tiny recommended settings
tabview2.add("YOLOv3-tiny")
yolov3tiny_settings_label = customtkinter.CTkLabel(tabview2.tab("YOLOv3-tiny"), text="YOLOv3-tiny is a powerful object detection algorithm, but it requires some tuning to achieve good results. Here are some recommended settings:\n\n- Confidence threshold: 0.5\n- Non-maximum suppression threshold: 0.5\n- Input image size: 416x416\n- Number of channels: 3\n- Mean values: (0,0,0)\n- Scale factor: 0.00392\n\nNote that these settings may vary depending on your specific use case and dataset.", font=("Helvetica", 14), pady=10, padx=10)
yolov3tiny_settings_label.pack(fill="x")

## Reflective recommended settings
tabview2.add("Reflective")
reflective_settings_label = customtkinter.CTkLabel(tabview2.tab("Reflective"), text="Our Model", font=("Helvetica", 14), pady=10, padx=10)
reflective_settings_label.pack(fill="x")

tabview2.add("Questions")

# Create the questions frame
questions_canvas = Canvas(tabview2.tab("Questions"))
questions_frame = customtkinter.CTkFrame(questions_canvas)
questions_scrollbar = Scrollbar(tabview2.tab("Questions"), orient="vertical", command=questions_canvas.yview)
questions_canvas.configure(yscrollcommand=questions_scrollbar.set)

# Pack the scrollbar and canvas
questions_scrollbar.pack(side="right", fill="y")
questions_canvas.pack(side="left", fill="both", expand=True)
questions_canvas.create_window((0, 0), window=questions_frame, anchor="nw")

# Set the scroll region to limit scrolling range
#questions_canvas.configure(scrollregion=questions_canvas.bbox("all"))

questions_canvas.bind('<Configure>', lambda e: questions_canvas.configure(scrollregion= questions_canvas.bbox("all"))) # ALLOWS USER TO SCROLL UP AND DOWN
# Add some widgets to the questions frame

questions_text = ["Confidence Value: This is the minimum probability score that an object must have in order to be considered a valid detection.A higher value will result in fewer false positives, but may also miss some true positives. A lower value will result in more detections, but may also increase the number of false positives.",
		  "Score Threshold: Increasing the score_threshold can lead to more accurate detections, but may also result in missed detections",
		  "NMS Threshold: The threshold used to suppress overlapping detections of the same object. Higher values will suppress more detections, resulting in fewer false positives, but may also miss some true positives. A lower value will result in more detections, but may also increase the number of false positives.",
		  "Input image size: This is the size of the input image that the algorithm expects. YOLOv3 is designed to work with a fixed input size, which should be a multiple of 32. A larger input size will generally result in better accuracy, but may also be slower to process.",
		  "Number of channels: This is the number of color channels in the input image. Most images are in RGB format, which has three channels.",
		  "Mean values: This is the mean value of each color channel in the input image. Subtracting the mean value from each pixel helps to normalize the input data, making it easier for the algorithm to learn.",
		  "Scale factor: This is the scale factor used to normalize the input image pixel values. Dividing the pixel values by this factor scales the values to the range [0,1], which is more suitable for the neural network to process. This particular scale factor is used because it corresponds to the inverse of 255, which is the maximum value of an 8-bit color channel.",
		  "Batch Processing & Batch Size: When using batch processing in video processing, the frames are processed in batches, rather than individually. In the case of a batch size of 16, the processing is done on groups of 16 frames at a time. This can lead to the impression that frames are being skipped, as the output is being produced at a lower frequency than the input frames. For example, if the input video is 30 frames per second and a batch size of 16 is used, it would take approximately half a second (16/30) to process a batch of frames. During that half-second period, 14 frames would be processed, and 16 frames would be skipped until the next batch is processed. This skipping of frames is typically not noticeable to the human eye, especially when the processing is done quickly and the resulting output video is played back at a normal speed."]
for i in range(len(questions_text)):
    label = customtkinter.CTkLabel(questions_frame, text=f"{questions_text[i]}\n", wraplength=850, anchor="w")
    label.pack(pady=10, padx=10, fill="both")

	
if __name__ == '__main__':
	root.title('Object Tracker GUI')
	root.mainloop()





