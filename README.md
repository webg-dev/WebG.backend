# WebG.backend


Table of Contents
=================

  * [Description](#description)
  * [Installation](#installation)
  * [Running Webservice](#running-webservice)
    * [Option 1 - Docker:](#option-1---docker)
    * [Optional 2 - Local:](#optional-2---local)
  * [API Specification](#api-specification)
     * [Resources](#resources)
        * [webPage](#webpage)


## Description
This repo houses the WebG backend webservice.
The primary purpose of the backend webservice is to scrape and preprocess both the
HTML DOM and screenshot of a requested web page and return this data in a format that
is suitable for the frontend application. 

## Installation
- Requires Python 3.6+
- Create a virtual environment e.g: `python -m venv venv`
- Activate the virtual environment `source venv/bin/activate` (on Linux)
- Install requirements: `pip install -r requirements.txt`

## Running Webservice

#### Option 1 - Docker:
If you only wish to run and use the webservice then the simplest way is probably
to build and run the Docker image:
1. Ensure you have Docker installed: `docker --version`
2. Run `docker build -t webg-backend .` from the root of the repository.
3. Run `docker run -d --name mycontainer -p 80:80 webg-backend` to start the container.
4. Visit `http://127.0.0.1/docs` in the browser to view the interactive docs.

#### Optional 2 - Local:
If you're going to be making changes to the code then you'll probably want to run the webservice locally:
1. Ensure you have firefox installed `sudo apt install firefox` on Linux
2. Ensure you have xvfb installed if you wish to run the webdriver in a virtual frame buffer `sudo apt-get install xvfb`
3. From the root of the repository run `uvicorn webservice.main:app --reload`
4. Visit `http://localhost:8000/docs` in the browser to view the interactive docs.


## API Specification

### Resources

#### webPage

The webPage resource represents a single scraped web page.


**Endpoint**: `GET /webPage?url=[URL TO SCRAPE]`

**Example Response**:

```json5
{
   "url":"https://nike.com/shoes/1",
   "width":1500,
   "height":3000,
   "html":"<html>...</html>",
   "screenshot":"image/png;base64,wOebnINCNLz3elG1I3g==",
   "graph":{
      "nodes":[
         {
            "id":0,
            "label":"html",
            "attributes":{
               "class":"..."
            },
            "coordinates":{
               "left":0,
               "right":1500,
               "top":0,
               "bottom":3000,
               "width":1500,
               "height":3000
            },
            "isVisible":true
         }
      ],
      "edges":[
         {
            "from":0,
            "to":1
         }
```
