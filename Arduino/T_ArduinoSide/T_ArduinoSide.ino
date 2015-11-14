
char inMessage [8];
int packetSwitch = 0;
int packetCount = 0;
int receivePin = 13;

void setup() {
  // initialize serial communication at 9600 bits per second:

    Serial.begin(9600);
    pinMode(receivePin, OUTPUT);




    Serial.print ("Arduino is ready to talk");
    int PacketIn = 0;
}


void loop() {

// Check incomming Serial data // 
serialIn();



}



int serialIn(){

// Check for serial input // 
  if(Serial.available() > 0) {
        char data = Serial.read();
        //Serial.println("");
        //Serial.print ("Received a Byte:");

        // Convert data to Asci caracter 
        
        char dataAsci = data;
        //Serial.print (dataAsci);

        // Check for opening byte 

        if (dataAsci ='O'){
          packetSwitch = 1;
          char Inmessage [8];
         // Serial.println("");
          //Serial.print("Started receiving packet");
          digitalWrite (receivePin, HIGH); 
        }
         // Check for closing byte or if the packet is too long, then print the fineshed message
        if (dataAsci = 'C' || packetCount>8){
          
          packetSwitch = 0;
          packetCount = 0;
         // Serial.println("Packet received");
          //digitalWrite (receivePin, LOW);
         // Serial.print (inMessage);
          // Print finished packet //           
        }
    

       // If the packet is being received, start logging bytes

       if (packetSwitch == 1){
          inMessage[packetCount] = dataAsci;
         // Serial.print (" PacketCount:");
         // Serial.print(packetCount);          
          packetCount++;         
       }    
  }

}

