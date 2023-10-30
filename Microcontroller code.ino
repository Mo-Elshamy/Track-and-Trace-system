

#define Detect0 26
#define Detect1 27
#define red 3
#define green 4
#define blue 5
#define sw0 21
#define sw1 20
#define sw2 19
#define sw3 18

int num = 0 ;
String x ;


void start ();

void setup ()
{
  Serial.begin(9600);

  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(sw0, OUTPUT);
  pinMode(sw1, OUTPUT);
  pinMode(sw2, OUTPUT);
  pinMode(sw3, OUTPUT);

  pinMode(Detect0, INPUT);
  pinMode(Detect1, INPUT);
}

void loop(){

  start();

  Serial.print("xx");

  while(Serial.available()>=0){
    // Serial.println("connected");
    if(digitalRead(Detect1) == 0){
      while(digitalRead(Detect1) == 0){
      Serial.println("cap");    
      x =Serial.readStringUntil('\n');
        if (x== "rejected"){
          digitalWrite(sw2, 1);
          delay(100);
          digitalWrite(sw2, 0);
        }
        
        else if (x=="error"){
          digitalWrite(sw1, 1);
          delay(100);
          digitalWrite(sw1, 0);
        }
        else if (x =="accepted"){
          digitalWrite(sw0, 1);
          delay(100);
          digitalWrite(sw0, 0);
        }
        else{
         // Serial.println("Error");
        }
      
       while(digitalRead(Detect1) == 0){}
      }
    }
  }
}


void start (){
  digitalWrite(red, 1);
  digitalWrite(green, 1);
  digitalWrite(blue, 1);
  digitalWrite(sw0, 0);
  digitalWrite(sw1, 0);
  digitalWrite(sw2, 0);
  digitalWrite(sw3, 0);
}
