float val;
int tempPin = 1;
int photocellPin = 0; 
int photocellReading;
int LEDpin = 11;     
int LEDbrightness;
int x=1;
void setup() 
  {
    Serial.begin(9600);
  }
void loop()
  {
    val = 450*analogRead(tempPin)/512.0+32;
    float mv = ( val/1024.0)*500; 
    float farh = (mv*9)/5 + 32;
    int scale = val;
    if(x<24){
      Serial.print(val);
      Serial.print(" ");
      photocellReading = analogRead(photocellPin); 
      Serial.println(photocellReading); 
    }
delay(1000);
x=x+1;
}
