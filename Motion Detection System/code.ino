const int trig = 11;
const int echo = 12;

const int LED1 = 2;
const int LED2 = 3;
const int LED3 = 4;
const int LED4 = 5;
const int LED5 = 6;
const int LED6 = 7;

int duration = 0;
int distance = 0;

int buzzPin=8;
int buzzTime=1;
int buzzTime2=0.9;
int buzzTime3=0.75;
int buzzTime4=0.6;
int buzzTime5=0.45;
int buzzTime6=0.3;
int buzzTime7=0.15;



void setup()
{
  pinMode (buzzPin,OUTPUT);
  
  pinMode(trig , OUTPUT);
  pinMode(echo , INPUT);
 
  pinMode(LED1 , OUTPUT);
  pinMode(LED2 , OUTPUT);
  pinMode(LED3 , OUTPUT);
  pinMode(LED4 , OUTPUT);
  pinMode(LED5 , OUTPUT);
  pinMode(LED6 , OUTPUT);
 
  Serial.begin(9600);

}

void loop()
{
  digitalWrite(trig , HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig , LOW);


  duration = pulseIn(echo , HIGH);
  distance = (duration/2) / 28.5 ;
  Serial.println(distance);
 

  if ( distance <= 5 )
  {
    digitalWrite(LED6, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime2);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime2);
  }
  else
  {
    digitalWrite(LED6, LOW);
  }
  if ( distance <= 15 )
  {
    digitalWrite(LED5, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime3);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime3);
  }
  else
  {
    digitalWrite(LED5, LOW);
  }
  if ( distance <= 20 )
  {
    digitalWrite(LED4, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime4);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime4);
  }   
  else
  {
    digitalWrite(LED4, LOW);
  }
  if ( distance <= 25 )
  {
    digitalWrite(LED3, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime5);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime5);
  }
  else
  {
    digitalWrite(LED3, LOW);
  }
  if ( distance <= 30 )
  {
    digitalWrite(LED2, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime6);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime6);
  }
  else
  {
    digitalWrite(LED2, LOW);
  }
  if ( distance <= 35 )
  {
    digitalWrite(LED1, HIGH);
    digitalWrite(buzzPin, HIGH);
    delay(buzzTime7);
    digitalWrite(buzzPin,LOW);
    delay(buzzTime7);
  }
  else
  {
    digitalWrite(LED1, LOW);
  }
}  