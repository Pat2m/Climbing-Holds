#include <Arduino.h>
#include <painlessMesh.h>
#include <Arduino_JSON.h>


#define   MESH_PREFIX     "ClimbingHoldsTest"
#define   MESH_PASSWORD   "Rowan123"
#define   MESH_PORT       5555

//Number for this node
int nodeNumber = 3;
uint32_t nodeHost;
//String to send to other nodes with sensor readings
String readings;

Scheduler userScheduler; // to control your personal task
painlessMesh  mesh;

// User stub
void sendMessage() ; // Prototype so PlatformIO doesn't complain
String getReadings(); // Prototype for sending sensor readings

//Create tasks: to send messages and get readings;
Task taskSendMessage(TASK_SECOND * 5 , TASK_FOREVER, &sendMessage);

String getReadings () {
  JSONVar jsonReadings;
  jsonReadings["node"] = nodeNumber;
  jsonReadings["time"] = millis();
  readings = JSON.stringify(jsonReadings);
  return readings;
}

void sendMessage() {
  JSONVar jsonReadings;
  jsonReadings["Host"] = int(nodeHost);
  String msg = JSON.stringify(jsonReadings);
  mesh.sendBroadcast(msg);
  Serial.print("Sent Broadcast");
}

void sendMessageHome() {
  mesh.sendSingle(0,getReadings());
}

// Needed for painless library
void receivedCallback( uint32_t from, String &msg ) {
  Serial.printf("Received from %u msg=%s\n", from, msg.c_str());
  JSONVar myObject = JSON.parse(msg.c_str());
  int node = myObject["node"];
  double time = myObject["time"];
  Serial.print("Node: ");
  Serial.println(node);
  Serial.print("Time: ");
  Serial.print(time);
}

void newConnectionCallback(uint32_t nodeId) {
  Serial.printf("New Connection, nodeId = %u\n", nodeId);
}

void changedConnectionCallback() {
  Serial.printf("Changed connections\n");
}

void nodeTimeAdjustedCallback(int32_t offset) {
  Serial.printf("Adjusted time %u. Offset = %d\n", mesh.getNodeTime(),offset);
}

void setup() {
  Serial.begin(115200);
  //mesh.setDebugMsgTypes( ERROR | MESH_STATUS | CONNECTION | SYNC | COMMUNICATION | GENERAL | MSG_TYPES | REMOTE ); // all types on
  mesh.setDebugMsgTypes( ERROR | STARTUP );  // set before init() so that you can see startup messages

  mesh.init( MESH_PREFIX, MESH_PASSWORD, &userScheduler, MESH_PORT );
  mesh.onReceive(&receivedCallback);
  mesh.onNewConnection(&newConnectionCallback);
  mesh.onChangedConnections(&changedConnectionCallback);
  mesh.onNodeTimeAdjusted(&nodeTimeAdjustedCallback);
  nodeHost = mesh.getNodeId();
  sendMessage();
  userScheduler.addTask(taskSendMessage);
  taskSendMessage.enable();
  Serial.println(nodeHost);
}

void loop() {
  // it will run the user scheduler as well
  mesh.update();
  
}