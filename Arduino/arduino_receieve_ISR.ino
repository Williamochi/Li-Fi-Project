const byte interrupt = 2;
volatile boolean Potential = true;
volatile boolean a = false;
float Interval = 1000;
volatile unsigned long int Last_time = 0;
volatile int count;
String CodeBook = "";
String copyofPotential;
char buf[500];

void setup (){
    attachInterrupt(digitalPinToInterrupt(interrupt), InterruptChange, CHANGE);
    Serial.begin(115200);
}

void loop (){
    if(a == true){
      Counting_Signal();
      Potential = !Potential;
      if(count < 21 && count > 0){
        //Serial.println(count);

       if(count == 20)
          Serial.print('3');
//        Serial.print(' ');
//        Serial.println(count);
      
       else{
        copyofPotential = Potential;
        for(int i=1 ; i<=count ; i++){
          //CodeBook.concat(copyofPotential);
          Serial.print(copyofPotential);
        }
       }
      }
      a = false;       
    }
    
//    if(count >= 20){
////      //Serial.print(CodeBook.length());
////      //Serial.println(CodeBook);
////      char buf[CodeBook.length()-1];
////      CodeBook.toCharArray(buf,CodeBook.length());
////      //Serial.print(buf);
////      CodeBook = "";
////
////      
//////      exit(0);
////    }
//    if(CodeBook.length() == 100){
//      //Serial.print(CodeBook.length());
//      //Serial.println(CodeBook);
//      CodeBook.toCharArray(buf,CodeBook.length());
//      //Serial.print(buf);
//    }
}

void InterruptChange(){  
    //Potential = !Potential;
    a = true;
}

void Counting_Signal(){
  count = round((micros() - Last_time)/Interval);
  //Serial.println(count);
  if(count != 1){
  //Serial.println((micros() - Last_time)/Interval);
  }
  Last_time = micros();
}
