""" 
    This script is a web-API that:
    - Accepts a plain text as a POST request using FastAPI.
    - Parses the text to split it into words by symbols, spaces and line breaks, excluding apostrophes and hypens.
    - Counts the frequency of occurrence for each unique word in the text.
    - Returns the results as a JSON-object, with the words as keys and the word frequency as their resp. values.

    In this script FastAPI is used to build the API with Python, according to the principles of RESTful.
"""

from fastapi import FastAPI, Request
from collections import Counter
import re

app = FastAPI() # create the FastAPI instance

@app.post("/count") # define the POST method
async def word_count(request: Request):
    text = await request.body() # await the data payload before continuing
    text = text.decode("utf-8") # decode text using utf-8

    text = re.findall(r"[a-zA-ZåäöÅÄÖ0-9'-]+", text) # sort out symbols from the text, keeping apostrophes and hypens
    
    ten_most_common_words = Counter(text).most_common(10) # count words and get the 10 most common
    
    return dict(ten_most_common_words) # return the words in a dict as JSON
