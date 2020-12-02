#!/usr/bin/python3
import pyttsx3
import datetime
import speech_recognition as sr
import os


engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")


engine.setProperty("voice" , voices[67].id)
def speak(speech):
    engine.say(speech)
    engine.runAndWait()


speak(input("input your text here: "))