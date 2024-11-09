# Word counting Web-API using FastAPI and Uvicorn

This project is a simple web-API built with FastAPI and Uvicorn that provides a word-counting functionality, following the principles of a RESTful API. 
The user can send an input in the format of a text of choice, via a POST request, and the web-API then returs the frequency of each unique word in the text in JSON format. 

This application is developed to automatically reload on code changes, making it easy to manage and compatible for future updates. 
The application can also handle requests asynchronously, to be able to handle large number of users simultaneously.

## Technologies used
FastAPI is a high-performance web framework for developing APIs with Python3, and is on level with NodeJS. The app runs on Uvicorn, which is an Asynchronous Server Gateway Interface (ASGI) server.

## Requirements
The requirements to run this application is specified in _requirements.txt_.

## How to install requirements and build the app
To get started with the app, you need to install FastAPI and Uvicorn. This can be done using pip.
Simply open the terminal and write
    **$** pip install .
This will install all requirements to run the app, accoring to _setup.py_.


## How to run the app
The script _run_api.py_ is the file than runs the FastAPI application using Uvicorn, and reloads the app when changes are made.
To run the app, simply write 
    **$** python run_api.py 
in the terminal. This will run the FastAPI application on port 3000, and the app is now set up for incoming HTTP requests on this port.

## How to use the app
To use the app, the user simply has to write 
    **$**  curl -H "Content-type: text/plain" -X "POST" -d _text_string_ http://localhost:3000/count 
where text_string is the input text the user wants to apply the word counting functionality on, in string format using ("").
