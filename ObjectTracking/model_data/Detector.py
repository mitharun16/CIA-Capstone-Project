import cv2
import numpy as np
import time

# Set a random seed for numpy
np.random.seed(20)

class Detector:
	def __init__(self, videoPath, configPath, modelPath, classesPath, modelType, confThreshold, bValue):

		# Initialize instance variables
		self.videoPath = videoPath
		self.configPath = configPath
		self.modelPath = modelPath
		self.classesPath = classesPath
		self.modelType = modelType
		self.confThreshold = confThreshold
		self.bValue = bValue

		# Load the DNN model from the specified paths
		self.net = cv2.dnn_DetectionModel(self.modelPath, self.configPath)

		# Set the input size for the model and configure the input
		self.net.setInputSize(320, 320)		#  lowest fps 320, 320 // 224, 224 // 128, 128 highest fps
		self.net.setInputScale(1.0/127.5)
		self.net.setInputMean((127.5, 127.5, 127.5))
		self.net.setInputSwapRB(True)

		# Call the readClasses function to load the class labels and colors
		self.readClasses()

	def readClasses(self):

		# Read the class labels from the specified path
		with open(self.classesPath, 'r') as f:
			self.classesList = f.read().splitlines()
		
		# Modify the classesList based on the model type
		if self.modelType == 'SSD':
			self.classesList.insert(0, '__Background__')

		elif self.modelType == 'YOLOv3':
			if '__Background__' in self.classesList:
				self.classesList.remove('__Background__')
		
		elif self.modelType == 'YOLOv3-tiny':
			if '__Background__' in self.classesList:
				self.classesList.remove('__Background__')

		# Generate random colors for each class label
		self.colorList = np.random.uniform(low=0, high=255, size=(len(self.classesList), 3))

		#print(self.classesList)
	
	# Function to run object detection on a video
	def onVideo(self):
		cap = cv2.VideoCapture(self.videoPath)

		# Open the video file
		if (cap.isOpened()==False):
			print("Error")
			return
		
		# Read the first frame from the video
		(success, image) = cap.read()

		# Initialize variables for calculating FPS
		startTime = 0

		# Loop through all frames in the video
		while success:
			# Calculate FPS for the current frame
			currentTime = time.time()
			fps = 1/(currentTime - startTime)
			startTime = currentTime

			# Run object detection on the current frame
			classLabelIDs, confidences, bboxs = self.net.detect(image, self.confThreshold.get())

			# Convert the bounding boxes and confidence values to lists
			bboxs = list(bboxs)
			confidences = list(np.array(confidences).reshape(1, -1)[0])
			confidences = list(map(float, confidences))

			# Performs non-maximum suppression(NMS) on the detected bounding boxes to remove overlapping boxes with lower confidence scores.
			# The default values for score_threshold and nms_threshold in many pre-trained object detection models are often set 
			# to 0.5 and 0.45, respectively. These values are generally a good starting point and should work well for many applications. 
			# However, the optimal values of these parameters can vary depending on the specific use case and the characteristics 
			# of the objects being detected. In some cases, you may need to adjust these parameters to improve the accuracy of the 
			# object detection. It's also worth noting that changing the values of these parameters can have trade-offs between 
			# accuracy and speed. Increasing the score_threshold can lead to more accurate detections, but may also result 
			# in missed detections, while decreasing the nms_threshold can lead to more overlapping bounding boxes and 
			# slower processing times.
			bboxIdx = cv2.dnn.NMSBoxes(bboxs, confidences, score_threshold = 0.5, nms_threshold = 0.45)

			# Draws bounding boxes around the detected objects in the image, along with the class labels and confidence scores.
			if len(bboxIdx) != 0:
				for i in range(0, len(bboxIdx)):

					bbox = bboxs[np.squeeze(bboxIdx[i])]
					classConfidence = confidences[np.squeeze(bboxIdx[i])]
					classLabelID = np.squeeze(classLabelIDs[np.squeeze(bboxIdx[i])])
					classLabel = self.classesList[classLabelID]
					classColor = [int(c) for c in self.colorList[classLabelID]]

					displayText = "{}:{:.2f}".format(classLabel, classConfidence)

					x,y,w,h = bbox

					cv2.rectangle(image, (x,y), (x+w, y+h), color = classColor, thickness = 2)
					cv2.putText(image, displayText, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 1, classColor, 2)
					
					lineWidth = min(int(w * .3), int(h * .3))

					if self.bValue == True:
						# TOP LEFT CORNER OF BOUNDING BOX
						cv2.line(image, (x,y), (x+lineWidth,y), classColor, thickness=4)
						cv2.line(image, (x,y), (x,y+lineWidth), classColor, thickness=4)

						# TOP RIGHT CORNER OF BOUNDING BOX
						cv2.line(image, (x+w,y), (x+w-lineWidth,y), classColor, thickness=4)
						cv2.line(image, (x+w,y), (x+w,y+lineWidth), classColor, thickness=4)

						# BOTTOM LEFT CORNER OF BOUNDING BOX
						cv2.line(image, (x,y+h), (x+lineWidth,y+h), classColor, thickness=4)
						cv2.line(image, (x,y+h), (x,y+h-lineWidth), classColor, thickness=4)

						# BOTTOM RIGHT CORNER OF BOUNDING BOX
						cv2.line(image, (x+w,y+h), (x+w-lineWidth,y+h), classColor, thickness=4)
						cv2.line(image, (x+w,y+h), (x+w,y+h-lineWidth), classColor, thickness=4)

			cv2.putText(image, "FPS: " + str(int(fps)), (20,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
			cv2.imshow("Result", image)

			# CHECKS TO SEE IF WEBCAM IS ENABLED
			if self.videoPath == 0:
				key = cv2.waitKey(1) & 0xFF
				if key == ord("q"):
					break
			
			# CHECKS TO SEE IF INPUT FILE IS VIDEO
			elif self.videoPath.endswith('.mp4'):
				key = cv2.waitKey(1) & 0xFF
				if key == ord("q"):
					break
			
			# INPUT FILE IS A PICTURE
			else:
				key = cv2.waitKey(0) & 0xFF
				if key == ord("q"):
					break

			(success, image) = cap.read()
		cv2.destroyAllWindows()
				
