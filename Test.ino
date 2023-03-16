// Read data from Serial
#define ledPin 13
#define RLED  37
#define GLED 36
int incomingByte;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(RLED, OUTPUT);
  pinMode(GLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin, HIGH);

  if(Serial.available() > 0){
    incomingByte = Serial.read();

    if (incomingByte == '1'){
      digitalWrite(GLED,LOW);
      digitalWrite(RLED, HIGH);
    }

    else if(incomingByte == '0'){
      digitalWrite(RLED, LOW);
      digitalWrite(GLED,HIGH);
    }

    else{
      digitalWrite(ledPin, LOW);
      delay(1000);
      digitalWrite(ledPin, HIGH);
    }
  }
}
