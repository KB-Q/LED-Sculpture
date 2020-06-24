#include <SD.h>
#include <SPI.h>
char a[29];  
File A;                       //Define Files
int pinCS = 53;         //Used to access data from SD card
int latchPin = 8;        //Pin connected to ST_CP of 74HC595
int clockPin = 7;       //Pin connected to SH_CP of 74HC595  

int dataPin[] = {14,15,16,17,18,19,20,21,37,36,35,34,33,32}; 
   
// First two data pins are for  cathodes, next 12 data pins are for anodes
                                                               
void setup()
{  
  Serial.begin(9600);
  pinMode(pinCS, OUTPUT); 
  pinMode(clockPin, OUTPUT);
  pinMode(latchPin, OUTPUT);  
  for (int i=0 ; i<15;i++) 
  {
    pinMode(dataPin[i], OUTPUT);
  }
  
  // SD Card Initialization
  if (SD.begin())
  {
    Serial.println("SD card is ready to use.");
  } 
  else 
  {
    Serial.println("SD card initialization failed");
    return;
  }
   // Reading the file
   A = SD.open("text.txt");      //'text' is the name of the file to be read and send to Arduino.                                 
}

void loop() 
{
  byte datastr[14];
  char ch;
  int b[27];

  for(int k=0;k<14;k++)                                     
  {
    datastr[k]=0;
  }
  for (int p=0;p<27;p++)
  {
    b[p]=0;
  }
  if (A) 
  {
     Serial.println("Read:");
     while (A.available())                                     
       { 
            ch = A.read(a,29);
            Serial.println(a);
            for (int i=0;i<27;i++)
             {
                if (a[i]>='0' && a[i]<='9') 
                {
                    b[i]=(a[i]-'0');
                }
                else if (a[i]>='A' && a[i]<='F')
                {
                   b[i]=(a[i]-'A'+10);
                }
                Serial.print(b[i]);
             }
             datastr[0]=(int)((b[0]<<4)+b[1]);
             datastr[1]=(int)b[2];
             
             for(int s=2;s<14;s++)
             {
              datastr[s]=(int)((b[(2*s)-1]<<4) +(b[(2*s)])) ;
             }
             Serial.println();
                   
            //lighting the leds
            digitalWrite(latchPin,LOW);   
            ShiftOut(dataPin,clockPin,datastr);
            digitalWrite(latchPin,HIGH); 
            Serial.println("file closed once"); 
       }
    } 
    else                                                              
    {
      Serial.println("error opening file");
    }
     A.close();       
}

 // This is a Shiftout function which shifts data to all the output pins of 12 anode shift registers (12x8= 96 bits) in one call. It shifts all the LSB bits first.

void ShiftOut(int myDataPin[], int myClockPin, byte myDataOut[])        
{                                                                    
   digitalWrite(myClockPin, LOW);
  for (int i=0; i<=7; i++)
  {
    for (int j=0;j<=13;j++)
    {
      digitalWrite(myDataPin[j],(((1<<(7-i)) & (myDataOut[j]))>>(7-i)));
    }
      digitalWrite(myClockPin, HIGH);
      digitalWrite(myClockPin, LOW);
  }   
}
