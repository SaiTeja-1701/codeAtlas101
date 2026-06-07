API Documentation
================

## Endpoints

### User Endpoints

#### 1. Register User
* **Endpoint:** `/api/users/register`
* **Method:** `POST`
* **Purpose:** Create a new user account
* **Flow:**
	1. Client sends a POST request to `/api/users/register` with user registration data
	2. Server processes the request and creates a new user account
	3. Server returns a success response with the newly created user data

#### 2. Login User
* **Endpoint:** `/api/users/login`
* **Method:** `POST`
* **Purpose:** Authenticate a user and return a login token
* **Flow:**
	1. Client sends a POST request to `/api/users/login` with user login credentials
	2. Server processes the request and authenticates the user
	3. Server returns a success response with a login token

#### 3. Complete Level
* **Endpoint:** `/api/users/complete-level`
* **Method:** `POST`
* **Purpose:** Update a user's progress by completing a level
* **Flow:**
	1. Client sends a POST request to `/api/users/complete-level` with user progress data
	2. Server processes the request and updates the user's progress
	3. Server returns a success response with the updated user data

### Activity Endpoints

#### 1. Create Activity
* **Endpoint:** `/api/activities/`
* **Method:** `POST`
* **Purpose:** Create a new activity
* **Flow:**
	1. Client sends a POST request to `/api/activities/` with activity data
	2. Server processes the request and creates a new activity
	3. Server returns a success response with the newly created activity data

#### 2. Get Today's Activities
* **Endpoint:** `/api/activities/today/:name`
* **Method:** `GET`
* **Purpose:** Retrieve a list of activities for a specific user for the current day
* **Flow:**
	1. Client sends a GET request to `/api/activities/today/:name` with the user's name
	2. Server processes the request and retrieves the list of activities for the user
	3. Server returns a success response with the list of activities

### Leaderboard Endpoints

#### 1. Get Leaderboard
* **Endpoint:** `/api/leaderboard/`
* **Method:** `GET`
* **Purpose:** Retrieve the current leaderboard
* **Flow:**
	1. Client sends a GET request to `/api/leaderboard/`
	2. Server processes the request and retrieves the current leaderboard
	3. Server returns a success response with the leaderboard data

### Summarize Endpoints

#### 1. Summarize
* **Endpoint:** `/api/summarize/`
* **Method:** `POST`
* **Purpose:** Summarize user data
* **Flow:**
	1. Client sends a POST request to `/api/summarize/` with user data
	2. Server processes the request and summarizes the user data
	3. Server returns a success response with the summarized data

#### 2. Ask Eco
* **Endpoint:** `/api/summarize/ask-eco`
* **Method:** `POST`
* **Purpose:** Ask eco-related questions
* **Flow:**
	1. Client sends a POST request to `/api/summarize/ask-eco` with the question
	2. Server processes the request and provides an answer to the question
	3. Server returns a success response with the answer

Note: The above endpoints and methods are based on the provided repository context and may not be exhaustive. Additional endpoints and methods may be available.