""" 
    This is the script that runs the FastAPI application using Uvicorn,
    and reloads the app when changes are made.
"""

import uvicorn

# Start running the uvicorn server and set up the app for incoming HTTP requests on port 3000
def main():
    uvicorn.run("word_counting_app:app", port=3000, reload=True) # reload app when changes are made

if __name__ == "__main__":
    main()