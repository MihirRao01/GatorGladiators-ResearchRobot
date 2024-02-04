#define x A0
#define y A1
#define z A2

int x_val;
int y_val;
int z_val;

int x_val2;
int y_val2;
int z_val2;



void setup() {
  // put your setup code here, to run once:
  pinMode(x,INPUT);
  pinMode(y,INPUT);
  pinMode(z,INPUT);

  Serial.begin(9600);

  x_val2 = analogRead(x);
  y_val2 = analogRead(y);
  z_val2 = analogRead(z);
  

}

void loop() {
  // put your main code here, to run repeatedly:

  x_val = analogRead(x);
  y_val = analogRead(y);
  z_val = analogRead(z);

  int x_change = x_val - x_val2;
  int y_change = y_val - y_val2;
  int z_change = z_val - z_val2;

  if(x_change >= 40)
  {
    Serial.println("Right");
  }
  else if( x_change <= -45 ) 
  {
    Serial.println("Left");
  }
  else if( y_change >= 45)
  {
    Serial.println( "Forward");
  }
  else if(y_change <= -45 ) 
  {
    Serial.println("Backward");
  }
  else
  {
    Serial.println("Stop");
    }
    

//  Serial.print("X: ");
//  Serial.println(x_val);
//  Serial.print("Y: ");
//  Serial.println(y_val);
//  Serial.print("Z: ");
//  Serial.println(z_val);
//  Serial.println();
//  Serial.println("----------------------------------------");
//  Serial.println();
  delay(1000);
  

}
