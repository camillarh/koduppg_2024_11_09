""" 
    This is the script that runs the FastAPI application using Uvicorn,
    and reloads the application when changes are made.
"""

import uvicorn

# Start running the uvicorn server and set up the API for incoming HTTP requests on port 3000
def main():
    uvicorn.run("word_counting_app:app", port=3000, reload=True) # reload application when changes are made

if __name__ == "__main__":
    main()