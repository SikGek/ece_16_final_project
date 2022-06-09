/*
 * Global variables
 */
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; int ay = 0; int az = 0;
int ppg = 0;        // PPG from readPhotoSensor() (in Photodetector tab)
int sampleTime = 0; // Time of last sample (in Sampling tab)
bool sending;
const int BUTTON_PIN  = 14;
const int BUTTON_TWO = A5;
int paused = 5;
int fire = 2;

/*
 * Initialize the various components of the wearable
 */
void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupPhotoSensor();
  sending = false;
  Serial.begin(115200);

  writeDisplay("Ready...", 1, true);
  writeDisplay("Set...", 2, false);
  writeDisplay("Play!", 3, false);
}

/*
 * The main processing loop
 */
void loop() {
  // Parse command coming from Python (either "stop" or "start")
  String command = receiveMessage();
  if(command == "stop") {
    sending = false;
    writeDisplay("Controller: Off", 0, true);
  }
  else if(command == "start") {
    sending = true;
    writeDisplay("Controller: On", 0, true);
  }
  // Send the orientation of the board
  if(sending && sampleSensors()) {
    sendMessage(String(getOrientation()));
  }
  if(sampleSensors()) {
  Serial.print(getOrientation());
  }
//  if(command != "") {
//    String msg = "Score:" + String(command);
//    writeDisplay(msg.c_str(), 0, true);
//  }
  while(digitalRead(BUTTON_PIN) == HIGH) {
    sendMessage(String(paused));
    Serial.print("5");
  }
    if((digitalRead(BUTTON_TWO) == HIGH) && sampleSensors()) {
    sendMessage(String(fire));
    Serial.print("2");
  }
//    if(sending && sampleSensors()) {
//    String response = "HEART" + String(sampleTime) + ",";
//    response += String(ppg);
//    sendMessage(response);    
//  }
//  if(command < 4) {
//    String msg = "Lives:" +  String(command);
//    writeDisplay(msg.c_str(), 0, true);
//  }
}
