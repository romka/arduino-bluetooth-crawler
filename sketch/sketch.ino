#include <AFMotor.h>
#include <Servo.h>

int incomingByte = 0;   // for incoming serial data
int collectedBytes = 0;

int leftEngineSpeed = 0;
int rightEngineSpeed = 0;
int maxSpeed = 5;

int speed_multiplier = 20;

AF_DCMotor left_motor(1);
AF_DCMotor right_motor(2);

Servo panServo, tiltServo;
Servo servo;

long interval = 15;    // interval at which to control servo
long previousMillis = 0;   
unsigned long currentMillis;
int pan = 90;
int tilt = 90;
int servo_max = 180;
int servo_min = 0;
int angle = 0;


void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  panServo.attach(10);	//Pan servo on pin D10
  tiltServo.attach(5);	//Tilt servo on pin D5
  
  panServo.write(pan);
  tiltServo.write(tilt);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
                
    if(incomingByte != 255) {
      collectedBytes = collectedBytes + incomingByte;
    } else if (incomingByte == 255) {
      Serial.println(collectedBytes);
      
      switch(collectedBytes) {
        case 1:
          updateEngine(0, 1);
          break;
        case 2:
          updateEngine(0, 0);
          break;
        case 3:
          updateEngine(0, -1);
          break;
        case 4:
          updateEngine(0, 1);
          updateEngine(1, 1);
          break;
        case 5:
          updateEngine(0, 0);
          updateEngine(1, 0);
          break;
        case 6:
          updateEngine(0, -1);
          updateEngine(1, -1);
          break;
        case 7:
          updateEngine(1, 1);
          break;
        case 8:
          updateEngine(1, 0);
          break;
        case 9:
          updateEngine(1, -1);
          break;
        case 10:
          updateServo(1, -6);
          break;
        case 11:
          updateServo(1, 6);
          break;
        case 12:
          updateServo(2, -6);
          break;
        case 13:
          updateServo(2, 6);
          break;
        //default:
        //  Serial.println('def');
      }

      
      collectedBytes = 0;
    }
  }
  
  updateSpeed();
}

void updateServo(int type, int act) {
  // type = 1 - pan
  // type = 2 = tilt
  if(type == 1) {
    servo = panServo;
    angle = pan;
  } else {
    servo = tiltServo;
    angle = tilt;
  }
  if((act > 0 && angle < servo_max) || (act < 0 && angle > servo_min)) {
    //Rotate camera
    currentMillis = millis();
    if(currentMillis - previousMillis > interval) {
      angle = angle + act;
      previousMillis = currentMillis;
      servo.write(angle);	     // tell pan servo to go to position
      
      if(type == 1) {
        pan = angle;
      } else {
        tilt = angle;
      }
    }
  }
}

void updateEngine(int engine, int value) {
  // 
  // engine = 0 - left engine
  // engine = 1 - right engine
  //
  int tmpEngine;
  if(!engine) {
    tmpEngine = leftEngineSpeed;
  } else {
    tmpEngine = rightEngineSpeed;
  }
  
  if(value == 0) {
    tmpEngine = 0;
  } else {
    if((value > 0 && tmpEngine < maxSpeed) || (value < 0 && tmpEngine > -maxSpeed)) {
      tmpEngine += value;
    }
  }

  if(!engine) {
    leftEngineSpeed = tmpEngine;
    Serial.print("Left speed ");
    Serial.print(leftEngineSpeed);
    Serial.println();
  } else {
    rightEngineSpeed = tmpEngine;
    Serial.print("Right speed ");
    Serial.print(rightEngineSpeed);
    Serial.println();
  }

}

void updateSpeed() {
  if(leftEngineSpeed == 0) {
    left_motor.run(RELEASE);
  } else {
    if(leftEngineSpeed > 0) {
      left_motor.run(FORWARD);
      left_motor.setSpeed(speed_multiplier * leftEngineSpeed);
    } else {
      left_motor.run(BACKWARD);
      left_motor.setSpeed(-speed_multiplier * leftEngineSpeed);
    }
  }
  
  if(rightEngineSpeed == 0) {
    right_motor.run(RELEASE);
  } else {
    if(rightEngineSpeed > 0) {
      // this motor connected reversely, in this reason here I switched sign of multiplier
      right_motor.run(BACKWARD);
      right_motor.setSpeed(speed_multiplier * rightEngineSpeed);
    } else {
      right_motor.run(FORWARD);
      right_motor.setSpeed(-speed_multiplier * rightEngineSpeed);
    }
  }
}
