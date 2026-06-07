API Documentation
================

## Endpoints

The following endpoints are available:

### 1. Login

* **Endpoint:** `/api/users/login`
* **Method:** `POST`
* **Purpose:** Authenticate a user and return a login token.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/login` with username and password in the request body.
	2. The server verifies the credentials and returns a login token if successful.

### 2. Register

* **Endpoint:** `/api/users/register`
* **Method:** `POST`
* **Purpose:** Create a new user account.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/register` with user information in the request body.
	2. The server creates a new user account and returns a success message.

### 3. Complete Level

* **Endpoint:** `/api/users/complete-level`
* **Method:** `POST`
* **Purpose:** Update a user's level completion status.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/complete-level` with level information in the request body.
	2. The server updates the user's level completion status and returns a success message.

### 4. Activities

* **Endpoint:** `/api/activities/`
* **Method:** `POST`
* **Purpose:** Create a new activity.
* **Flow:**
	1. The client sends a `POST` request to `/api/activities/` with activity information in the request body.
	2. The server creates a new activity and returns a success message.

### 5. Today's Activities

* **Endpoint:** `/api/activities/today/:name`
* **Method:** `GET`
* **Purpose:** Retrieve a user's activities for the current day.
* **Flow:**
	1. The client sends a `GET` request to `/api/activities/today/:name` with the user's name in the URL parameter.
	2. The server returns the user's activities for the current day.

### 6. Leaderboard

* **Endpoint:** `/api/leaderboard/`
* **Method:** `GET`
* **Purpose:** Retrieve the leaderboard.
* **Flow:**
	1. The client sends a `GET` request to `/api/leaderboard/`.
	2. The server returns the leaderboard.

### 7. Summarize

* **Endpoint:** `/api/summarize/`
* **Method:** `POST`
* **Purpose:** Summarize user data.
* **Flow:**
	1. The client sends a `POST` request to `/api/summarize/` with user data in the request body.
	2. The server summarizes the user data and returns a success message.

### 8. Ask Eco

* **Endpoint:** `/api/summarize/ask-eco`
* **Method:** `POST`
* **Purpose:** Ask eco-related questions.
* **Flow:**
	1. The client sends a `POST` request to `/api/summarize/ask-eco` with the question in the request body.
	2. The server responds with an answer to the eco-related question.

## API Call Examples

* Login: `https://b09-backend.onrender.com/api/users/login`
* Register: `https://b09-backend.onrender.com/api/users/register`
* Complete Level: `http://localhost:5000/api/users/complete-level` (for mobile app)

Note: The API call examples are for demonstration purposes only and may need to be modified based on the actual API endpoint and environment.