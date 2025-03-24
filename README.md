
# API Methods: GET, POST, PUT, DELETE

# Building API Endpoints using Flask 
Flask is a lightweight web framework in Python used to build APIs. It allows handling different HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE` to interact with data in a structured way.

## HTTP Methods and Their Uses
### 1. **GET** - Retrieving Data

- Used to fetch data from the server.
- Can be accessed directly via a browser or API tools.
- Example:
  ```python
  @app.route("/items", methods=["GET"])
  def get_items():
      return jsonify({"items": ["apple", "banana", "cherry"]})
  ```
- **Usage with CURL**:
  ```sh
  curl -X GET http://127.0.0.1:5000/items
  ```

### 2. **POST** - Creating Data

- Used to send data to the server to create a new resource.
- Cannot be used directly in the browser; requires tools like `requests` or `Postman`.
- The data is sent in the request body as JSON.
- Example:
  ```python
  @app.route("/items", methods=["POST"])
  def add_item():
      data = request.json  # Extracts JSON data from the request body
      new_item = data.get("item")
      if new_item:
          return jsonify({"message": f"{new_item} added successfully!"})
      return jsonify({"error": "No item provided"}), 400
  ```
- **Example of JSON Data Sent in the Request Body**:
  ```json
  {
    "item": "orange"
  }
  ```
- **Usage with CURL**:
  ```sh
  curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"item": "orange"}'
  ```

### 3. **PUT** - Updating Data

- Used to update an existing resource.
- The updated data is sent in the request body as JSON.
- Example:
  ```python
  @app.route("/items/<old_item>", methods=["PUT"])
  def update_item(old_item):
      data = request.json  # Extracts JSON data from the request body
      new_item = data.get("new_item")
      if new_item:
          return jsonify({"message": f"{old_item} updated to {new_item}"})
      return jsonify({"error": "No new item provided"}), 400
  ```
- **Example of JSON Data Sent in the Request Body**:
  ```json
  {
    "new_item": "green apple"
  }
  ```
- **Usage with CURL**:
  ```sh
  curl -X PUT http://127.0.0.1:5000/items/apple -H "Content-Type: application/json" -d '{"new_item": "green apple"}'
  ```

### 4. **DELETE** - Removing Data

- Used to delete a resource.
- Example:
  ```python
  @app.route("/items/<item>", methods=["DELETE"])
  def delete_item(item):
      return jsonify({"message": f"{item} deleted successfully!"})
  ```
- **Usage with CURL**:
  ```sh
  curl -X DELETE http://127.0.0.1:5000/items/banana
  ```

## Dependencies and Setup

- Install Flask:
  ```sh
  pip install flask
  ```
- Required imports:
  ```python
  from flask import Flask, jsonify, request
  ```
- Start the Flask server:
  ```sh
  python app.py
  ```

## Using URLs in the Command Line

- The URL specifies which API route is accessed.
- **NB:** This happens in the command line.
- Example command:
  ```sh
  curl -X GET http://127.0.0.1:5000/items
  ```
- For `POST`, `PUT`, and `DELETE`, the URL includes parameters, headers, and data sent in the request body.
  ```sh
  curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"item": "grape"}'
  ```

## Why Use `jsonify`?

- Converts Python objects (`dicts`, `lists`, `tuples`) into JSON responses.
- Ensures proper HTTP response headers.
- Example:
  ```python
  return jsonify({"message": "Hello, world!"})
  ```

## Notes and Best Practices

- `POST`, `PUT`, and `DELETE` **cannot be used in a browser URL**; use `requests` or API testing tools.
- Always use `request.json` to handle JSON input, which is extracted from the request body.
- Define routes clearly and use meaningful endpoints.

## Conclusion

Flask provides an easy way to build APIs with standard HTTP methods. Using `jsonify`, handling requests properly, and using tools like `requests` ensures smooth API functionality.

