// nrf24_client

#include <SPI.h>
#include <RH_NRF24.h>
#include <dht.h>

// Singleton instance of the radio driver
RH_NRF24 nrf24;
dht DHT;
// RH_NRF24 nrf24(8, 7); // use this to be electrically compatible with Mirf
// RH_NRF24 nrf24(8, 10);// For Leonardo, need explicit SS pin
// RH_NRF24 nrf24(8, 7); // For RFM73 on Anarduino Mini

#define DHT22_PIN 2

struct DataHolder {
    float temp[10]; // Room for 9 characters + NULL
    float hum[10]; // Room for 9 characters + NULL
}myData;

void setup() 
{
  Serial.begin(9600);
  while (!Serial) 
    ; // wait for serial port to connect. Needed for Leonardo only
  if (!nrf24.init())
    Serial.println("init failed");
  // Defaults after init are 2.402 GHz (channel 2), 2Mbps, 0dBm
  if (!nrf24.setChannel(1))
    Serial.println("setChannel failed");
  if (!nrf24.setRF(RH_NRF24::DataRate2Mbps, RH_NRF24::TransmitPower0dBm))
    Serial.println("setRF failed");    
}


void loop()
{
  int chk = DHT.read22(DHT22_PIN);
  struct DataHolder data;

  strncpy(data.name, "Fred", 10); // Maximum 10 bytes
  strncpy(data.skill, "ClassA", 10); // Again, max 10 bytes.


  nrf24.send((uint8_t *)&data, sizeof(struct DataHolder));
//  String temp = "T: ";
  // Send a message to nrf24_server
  //  uint8_t header[] = "DATA";
  //  uint8_t tData = DHT.temperature;
  //  uint8_t hData = DHT.humidity;
// send data header
//  Serial.println(header);
//  nrf24.send(header,sizeof(header));
//  nrf24.waitPacketSent();
//send temp data
//  Serial.println(tData);
//  nrf24.send(tData, sizeof(tData));
//  nrf24.waitPacketSent();
//send humidity data
//  Serial.println(hData);
//  nrf24.send(hData, sizeof(hData));
//  nrf24.waitPacketSent();
  // Now wait for a reply
//  uint8_t buf[RH_NRF24_MAX_MESSAGE_LEN];
//  uint8_t len = sizeof(buf);

  nrf24.send((uint8_t *)&myData, sizeof(struct DataHolder));


  if (nrf24.waitAvailableTimeout(500))
  { 
    // Should be a reply message for us now   
    if (nrf24.recv(buf, &len))
    {
      Serial.print("got reply: ");
      Serial.println((char*)buf);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  else
  {
    Serial.println("No reply, is nrf24_server running?");
  }
  delay(400);
}
