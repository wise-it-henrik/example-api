# Example API
This repo contains a Flask app with endpoints serving JSON-files. It was created as a resource you make API calls to.

You can make the basic methods GET, POST, PUT and DELETE requests to it.


## Setup
Assuming you have everything to run python code, these are the steps to setting up the API.

##### 1. Cloning
Clone this repository to a diretory of your choice.

##### 2. Virtual environment
Create a python virtual environment.  
```python3 -m venv .venv```
Activate the virtual environment  
- On Windows:  
```venv\Scripts\activate```
- On macOS and Linux:  
```source venv/bin/activate```

##### 3. Installing libraries
Install the required libraries.  
```pip install requirements.txt```

##### 4. Run the API
Start the script  
```python3 app.py```

##### 5. Run the API
You will now be able to make curl requests (or similar) to http://locahost:5000


## API Endpoints
#### 1. Get All JSON Files
Endpoint: /json-files
Method: GET
Description: Returns all JSON files.
Sample Request:
```
curl -X GET http://127.0.0.1:5000/json-files
```
Sample Response:

```
[
    {"id": 1, "content": "Random sentence 1"},
    {"id": 2, "content": "Random sentence 2"},
    {"id": 3, "content": "Random sentence 3"}
]
```
\
#### 2. Get JSON File by ID
Endpoint: /json-files/<int:file_id>
Method: GET
Description: Returns the JSON file with the specified ID.
Sample Request:
```
curl -X GET http://127.0.0.1:5000/json-files/1
```
Sample Response:
```
{
    "id": 1,
    "content": "Random sentence 1"
}
```
\
#### 3. Create JSON File
Endpoint: /json-files
Method: POST
Description: Creates a new JSON file with the provided content.
Sample Request:
```
curl -X POST http://127.0.0.1:5000/json-files -H "Content-Type: application/json" -d '{"content": "New content"}'
```
Sample Response:
```
{
    "id": 4,
    "content": "New content"
}
```
\
#### 4. Update JSON File
Endpoint: /json-files/<int:file_id>
Method: PUT
Description: Updates the JSON file with the specified ID. The request must include a "mode" header with values "overwrite" or "append".
Sample Request (Overwrite):
```
curl -X PUT http://127.0.0.1:5000/json-files/1 -H "Content-Type: application/json" -H "mode: overwrite" -d '{"content": "Updated content"}```

Sample Request (Append):
```
curl -X PUT http://127.0.0.1:5000/json-files/1 -H "Content-Type: application/json" -H "mode: append" -d '{"content": " Appended content"}'
```
Sample Response (Overwrite):
```
{
    "id": 1,
    "content": "Updated content"
}
```
Sample Response (Append):
```
{
    "id": 1,
    "content": "Random sentence 1 Appended content"
}
```
\
#### 5. Delete JSON File
Endpoint: /json-files/<int:file_id>
Method: DELETE
Description: Deletes the JSON file with the specified ID.
Sample Request:
```
curl -X DELETE http://127.0.0.1:5000/json-files/1
```
Sample Response:
```
{
    "message": "File deleted"
}
```
