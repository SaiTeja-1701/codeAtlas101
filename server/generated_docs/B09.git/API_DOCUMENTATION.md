# API Documentation
## Introduction
This API documentation outlines the endpoints, methods, purposes, and flows of the API.

## Endpoints

### 1. User Login
* **Endpoint:** `/api/users/login`
* **Method:** `POST`
* **Purpose:** Authenticate a user and return a login token.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/login` with the user's credentials.
	2. The server verifies the credentials and returns a login token if they are valid.
	3. The client stores the login token for future use.

### 2. User Registration
* **Endpoint:** `/api/users/register`
* **Method:** `POST`
* **Purpose:** Create a new user account.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/register` with the user's registration details.
	2. The server creates a new user account and returns a confirmation message.
	3. The client redirects the user to the login page.

### 3. Complete Level
* **Endpoint:** `/api/users/complete-level`
* **Method:** `POST`
* **Purpose:** Mark a level as completed for a user.
* **Flow:**
	1. The client sends a `POST` request to `/api/users/complete-level` with the level details.
	2. The server updates the user's progress and returns a confirmation message.
	3. The client updates the user's progress display.

### 4. User Activities
* **Endpoint:** `/api/user`
* **Method:** `POST`
* **Purpose:** Create a new user activity.
* **Flow:**
	1. The client sends a `POST` request to `/api/user` with the activity details.
	2. The server creates a new activity for the user and returns a confirmation message.
	3. The client updates the user's activity display.

### 5. Today's Activities
* **Endpoint:** `/api/user/today/:name`
* **Method:** `GET`
* **Purpose:** Retrieve a user's activities for the current day.
* **Flow:**
	1. The client sends a `GET` request to `/api/user/today/:name` with the user's name.
	2. The server returns the user's activities for the current day.
	3. The client displays the activities.

### 6. Leaderboard
* **Endpoint:** `/api/`
* **Method:** `GET`
* **Purpose:** Retrieve the leaderboard data.
* **Flow:**
	1. The client sends a `GET` request to `/api/`.
	2. The server returns the leaderboard data.
	3. The client displays the leaderboard.

### 7. Summarize
* **Endpoint:** `/api/`
* **Method:** `POST`
* **Purpose:** Summarize data.
* **Flow:**
	1. The client sends a `POST` request to `/api/` with the data to summarize.
	2. The server summarizes the data and returns the result.
	3. The client displays the summarized data.

### 8. Ask Eco
* **Endpoint:** `/api/ask-eco`
* **Method:** `POST`
* **Purpose:** Ask an eco-related question.
* **Flow:**
	1. The client sends a `POST` request to `/api/ask-eco` with the question.
	2. The server responds with an answer to the question.
	3. The client displays the answer.

## API Call Examples

* **Login:** `https://b09-backend.onrender.com/api/users/login`
* **Register:** `https://b09-backend.onrender.com/api/users/register`
* **Complete Level:** `http://localhost:5000/api/users/complete-level`

Note: The API endpoints and methods are subject to change. It's recommended to check the API documentation regularly for updates.