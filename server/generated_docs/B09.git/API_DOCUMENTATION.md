# API Documentation
## Introduction
This API documentation outlines the available endpoints, methods, purposes, and flows for the application.

## Endpoints
### User Endpoints

#### 1. Login
* **Endpoint:** `/api/users/login`
* **Method:** `POST`
* **Purpose:** Authenticate a user and return a login token.
* **Flow:**
	1. Client sends a `POST` request to `/api/users/login` with username and password.
	2. Server verifies the credentials and returns a login token if valid.

#### 2. Register
* **Endpoint:** `/api/users/register`
* **Method:** `POST`
* **Purpose:** Create a new user account.
* **Flow:**
	1. Client sends a `POST` request to `/api/users/register` with user details.
	2. Server creates a new user account and returns a success message.

#### 3. Complete Level
* **Endpoint:** `/api/users/complete-level`
* **Method:** `POST`
* **Purpose:** Update a user's level completion status.
* **Flow:**
	1. Client sends a `POST` request to `/api/users/complete-level` with level details.
	2. Server updates the user's level completion status and returns a success message.

### Activity Endpoints

#### 1. Create Activity
* **Endpoint:** `/api/activities/`
* **Method:** `POST`
* **Purpose:** Create a new activity.
* **Flow:**
	1. Client sends a `POST` request to `/api/activities/` with activity details.
	2. Server creates a new activity and returns a success message.

#### 2. Get Today's Activities
* **Endpoint:** `/api/activities/today/:name`
* **Method:** `GET`
* **Purpose:** Retrieve a user's activities for the current day.
* **Flow:**
	1. Client sends a `GET` request to `/api/activities/today/:name` with the user's name.
	2. Server returns a list of activities for the current day.

### Leaderboard Endpoints

#### 1. Get Leaderboard
* **Endpoint:** `/api/leaderboard/`
* **Method:** `GET`
* **Purpose:** Retrieve the leaderboard data.
* **Flow:**
	1. Client sends a `GET` request to `/api/leaderboard/`.
	2. Server returns the leaderboard data.

### Summarize Endpoints

#### 1. Summarize
* **Endpoint:** `/api/summarize/`
* **Method:** `POST`
* **Purpose:** Summarize data.
* **Flow:**
	1. Client sends a `POST` request to `/api/summarize/` with data to summarize.
	2. Server summarizes the data and returns a success message.

#### 2. Ask Eco
* **Endpoint:** `/api/summarize/ask-eco`
* **Method:** `POST`
* **Purpose:** Ask an eco-related question.
* **Flow:**
	1. Client sends a `POST` request to `/api/summarize/ask-eco` with the question.
	2. Server returns an answer to the question.

## API Call Examples
* **Login:** `https://b09-backend.onrender.com/api/users/login`
* **Register:** `https://b09-backend.onrender.com/api/users/register`
* **Complete Level:** `http://localhost:5000/api/users/complete-level`