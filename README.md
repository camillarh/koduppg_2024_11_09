# Word counting Web-API using FastAPI and Uvicorn

This project is a simple web-API built with FastAPI and Uvicorn that provides a word-counting functionality, following the principles of a RESTful API. 
The user can send an input in the format of a text of choice, via a POST request, and the web-API then returns the frequency of the 10 most occuring unique words in the text. The output is written as a JSON-object, where the words are the keys and their respective values are each words number of occurences. 

This web-API is developed to automatically reload when any changes in the code is made, making it easy to manage and allow for for future updates. 
The application can also handle requests asynchronously, to work with a large number of users simultaneously.

## Frameworks and requirements 
FastAPI is a high-performance web framework for developing APIs with Python3, which is on level with NodeJS. The application runs on Uvicorn, which is an Asynchronous Server Gateway Interface (ASGI) server.

> [!IMPORTANT]
> This project uses Python3 and pip (Python package manager) to install packages and write all the code for the word-counting application. Therefore, Python3 and pip is required in order to install, run and update the web-API.

Other requirements to run this application is specified in [requirements.txt](koduppg_CGI/requirements.txt).


## How to install requirements and build the application
To get started with the the word-counting application, you need to install FastAPI and Uvicorn. This can be done using pip.
Simply clone this repository, open a terminal and set your current location to the directory of the cloned repository. In the terminal then, write

`$ pip install .`

This will install all requirements to run the application, according to [setup.py](koduppg_CGI/setup.py).

## How to run the application
The script [run_api.py](koduppg_CGI/run_api.py) is the file than runs the FastAPI application using Uvicorn, and reloads the application when changes are made. To run the app, in the terminal simply write 

`$ python run_api.py`

This will start the Uvicorn server and run the FastAPI application on port 3000. The web-API is now set up for incoming HTTP requests on this port. The actual word count is performed in the script [word_counting_app.py](koduppg_CGI/word_counting_app.py)


## How to use the application
To use the application, open a separate terminal and write 

`$  curl -H "Content-type: text/plain" -X "POST" -d text_string http://localhost:3000/count`

where _text_string_ is the text the user wants to apply the word counting functionality on. 

> [!WARNING]
> The _text_string_ must be defined in string-format using (" ").

### A simple example
> [!TIP]
> A simple example of using the application is by writing
>
>`$ curl -H "Content-type: text/plain" -X "POST" -d "Banan Äpple Katt Hund Banan Hund Katt Hund" http://localhost:3000/count`
>
> which will generate the web-API to count the occurence of each word in the string "_Banan Äpple Katt Hund Banan Hund Katt Hund_" and return the response
>
>`$ {"Hund":3,"Banan":2,"Katt":2,"Äpple":1}` 
>
