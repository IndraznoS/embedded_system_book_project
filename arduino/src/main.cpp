/*
 * Blink Example
 * 
 * This is a basic Arduino sketch that demonstrates digital output
 * by blinking the built-in LED on pin 13.
 * 
 * Hardware:
 * - Arduino Uno, Mega, or compatible board
 * - Built-in LED on pin 13
 * 
 * This example corresponds to Chapter 1 of the book.
 */

#include <Arduino.h>

// Pin definitions
const int LED_PIN = LED_BUILTIN;  // Built-in LED (usually pin 13)

// Timing constants
const unsigned long BLINK_INTERVAL = 1000;  // milliseconds

void setup() {
    // Initialize serial communication
    Serial.begin(9600);
    Serial.println("Blink Example Started");
    
    // Configure LED pin as output
    pinMode(LED_PIN, OUTPUT);
    
    // Initialize LED to OFF state
    digitalWrite(LED_PIN, LOW);
}

void loop() {
    // Turn LED on
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED: ON");
    
    // Wait for specified interval
    delay(BLINK_INTERVAL);
    
    // Turn LED off
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED: OFF");
    
    // Wait for specified interval
    delay(BLINK_INTERVAL);
}
