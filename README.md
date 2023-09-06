# FarmBot

## Table of Contents

* [Authors](#Authors)
* [Overview](#Overview)
* [Execution](#Execution)
* [Installation](#Instalation)
* [Key Topics](#Key_Topics)
* [Helpful Links](#Helpful_Links)

## Authors

- Hunter VanEttan
- Parth Parikh

## Overview

This project was developed in response too individuals who are interested in learning more about Agronomy and training your own chatbot. Currently FarmBot is a simple chatbot that can answer basic questions about 10 different crops. These questions are can be viewed in the intents.json file as well as their different variations. Despite training and having the bot learn, it also has the abilities of an AI Assistant where it can navigate the web, wikipedia various information, compute equations, take notes, and play songs.    

## Execution

- Run main.py in terminal 
- Say activation word ("FarmBot") followed by what action you want to run:
  - Ex: Say Hi - FarmBot hello
  - Ex: Navigate the web - Farmbot go to google.com
  - Ex: Play a song - FarmBot play Don't Stop Believing
  - Ex: Learn more about a topic - FarmBot wikipedia Python chatbots
  - Ex: Take notes - Farmbot log (this will require you to wait a second and once it is "ready" you can finish saying what you want)
  - Ex: Compute equations - FarmBot compute 1 + 2 * 3 - 4 / 5
  - Ex: Ask Agronomy questions - FarmBot information (this will require you to wait a second and then TYPE your question)
  - Ex: Stop the Program - FarmBot exit

## Installation

- Visit this link to install the Conda virtual environment: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
- Make sure you have PYTHON 3.6 installed in your Conda virtual environment
- Inside your virtual environment, install these packages using **pip install (package_name)**:
  - numpy
  - nltk
  - tensorflow
  - tflearn
  - speech_recognition
  - pyttsx3
  - webbrowser
  - wikipedia
  - wolframalpha
  - pywhatkit

## Key_Topics

- Deep Learning 
- Python Programming


## Helpful_Links

These links were used to setup this project and as a guide to building the code.

- Python Chatbot tutorial: https://youtu.be/wypVcNIH6D4

- Python AI_Assistant: https://youtu.be/OqFI_g8vAoc
