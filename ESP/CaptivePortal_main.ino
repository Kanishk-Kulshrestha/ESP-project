#include <ESP8266WiFi.h>
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
#include "index.h"
#define LED 2
#define ServoPin 14 // D5 is GPIO14

const byte DNS_PORT = 53;
IPAddress apIP(172, 217, 28, 1);
DNSServer dnsServer;

Servo myservo;
ESP8266WebServer server(80);

void handleServo() {
  String POS = server.arg("servoPOS");
  int pos = POS.toInt();
  myservo.write(pos); // tell servo to go to position
  delay(15);
  Serial.print("Servo Angle:");
  Serial.println(pos);
  digitalWrite(LED, !(digitalRead(LED))); // Toggle LED
  server.send(200, "text/plane", "");
}

String s = MAIN_page;

void setup() {

  delay(1000);
  Serial.begin(115200);
  Serial.println();

  pinMode(LED, OUTPUT);
  myservo.attach(ServoPin);
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(apIP, apIP, IPAddress(255, 255, 255, 0));
  WiFi.softAP("SureLock","servo1234");
  Serial.println("Access Point Started");
  Serial.print("IP address: ");
  Serial.println(WiFi.softAPIP()); // IP address assigned to your ESP

  // if DNSServer is started with "*" for domain name, it will reply with
  // provided IP to all DNS request
  dnsServer.start(DNS_PORT, "*", apIP);

  // replay to all requests with same HTML
  server.onNotFound([]() {
    server.send(200, "text/html",s);
  }); 
  server.on("/setPOS", handleServo);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  dnsServer.processNextRequest();
  server.handleClient();
}
