Ihyun Park A16605545
William Lynch A14588777

Space Invaders:

Design Project:

For our design project, we created a prototype of a home-alarm system that uses MQTT protocol in order to send messages to the server. We chose this project as we believed the MQTT protocol would allow for faster and more consistent transfer of data and messages while being lightweight and putting less strain on power. 

We used the YOLO (You Only Look Once) algorithm to train our model for face and gesture detection. We chose this method as YOLO is the most consistent and accurate open source object detection method. Using the provided method, we trained our own model to detect a specific face and gestures. For demonstration purposes, we chose to train the model specifically for Ihyun's face and a thumbs up gesture, so that we can show how it treats undetected face and gestures. In the future, if we were to develop this project further than a simple prototype, we could implement a system that allows a user to take photos of their own face and gestures and have it trained within the system or our server in order to automatically add it to a list of detected faces and gestures for commercial use.

We chose to implement a button through our MCU to activate the home alarm system, so that the face detection method is not active 24/7 and the user can activate it only when they need to access it. A use case for this would be if we create a smart home system that connects the home security to one server. Here, if the user presses the button in the front door, it will activate the face detection system, and when an authorized face is detected, they can gesture to either open or lock the door etc. which will send a message to the server using the MQTT protocol and perform the according command. This is where the MQTT protocol would come in handy, as it will allow for the server to be up consistently due to its lightweightness and save power thanks to its subscribe/publish model. This problem is worth addressing, as many

Specifically for our prototype, when the button is pressed on the MCU, it sends a message to our Python code that tells it to start its face detection, and when it detects an authorized face, it begins to scan for hand gestures, and when it detects a proper hand gesture, it sends a message to our server.

While Ihyun worked primarily on implementing the button, communication between the MCU and the python code, the face/gesture detection using the YOLO algorithm and training our own model, William worked on developing and adding improvements on the controller and implementing the MQTT protocol when sending message to the server.