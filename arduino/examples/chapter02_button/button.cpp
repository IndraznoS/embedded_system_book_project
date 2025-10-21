/*
 * Chapter 2: Button Input Example
 * 
 * Demonstrates digital input by reading a button and controlling an LED.
 * 
 * Hardware:
 * - Button connected to pin 2 (with internal pull-up)
 * - LED connected to pin 13
 */

#include <Arduino.h>

const int BUTTON_PIN = 2;
const int LED_PIN = 13;

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    pinMode(LED_PIN, OUTPUT);
    
    Serial.begin(9600);
    Serial.println("Button Example Started");
}

void loop() {
    int buttonState = digitalRead(BUTTON_PIN);
    
    if (buttonState == LOW) {  // Button pressed (active LOW with pull-up)
        digitalWrite(LED_PIN, HIGH);
        Serial.println("Button pressed - LED ON");
    } else {
        digitalWrite(LED_PIN, LOW);
    }
    
    delay(10);  // Small delay for debouncing
}
