


void setup() {
  // initialize serial communication at 9600 bits per second:

    Serial.begin(9600);
    pinMode(13, OUTPUT);

    // Blink light to verify it works 
    Serial.println ("Blinking pin 13");
    digitalWrite (13, HIGH);
    delay(500);
    digitalWrite(13,LOW);
    delay(500);


    Serial.print ("Arduino is ready to talk");
    int PacketIn = 0;
}


void loop() {


// Check for serial input // 
  
  if(Serial.available() > 0) {
        int data = Serial.read();
        Serial.println("");
        Serial.print ("Received packet:");
        
        char datab = data;
        Serial.print (datab);



        // Do stuff based on the input command // 

        // Construct incomming packet // 



        
      
        if (datab == '1' ){
         Serial.println("");
         Serial.print("Blinking lights!");
         digitalWrite (13, HIGH);
         delay(1000);
         digitalWrite(13,LOW);
         delay(1000);
        }
    
  }
}

