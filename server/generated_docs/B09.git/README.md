# Project Overview
The B09 project is a MERN (MongoDB, Express, React, Node) application built using the MVC (Model-View-Controller) architecture. It consists of a backend API server and a frontend client application, with a mobile application component. The project aims to provide a comprehensive platform for eco-friendly tasks and activities.

# Features
* User authentication and authorization
* Eco-task completion and tracking
* Profile management and summarization
* Daily quest automatic task completion
* Activities drawer and themed view
* Responsive design for mobile and web applications

# Tech Stack
* **Backend:**
	+ Node.js (framework)
	+ Express.js (web framework)
	+ MongoDB (database)
* **Frontend:**
	+ React.js (library)
	+ Vite (build tool)
* **Mobile:**
	+ React Native (framework)

# Architecture
The project follows the MVC architecture, with the following components:
* **Models:** Define the structure and organization of data
* **Controllers:** Handle API requests and interact with models
* **Views:** Render the user interface and display data
* **Routes:** Define the API endpoints and navigation

# Setup
To get started with the project, follow these steps:
1. Clone the repository: `git clone https://github.com/HACKWAVE2025/B09.git`
2. Install dependencies: `npm install`
3. Set up the environment variables: `cp .env.example .env` and update the values as needed
4. Start the backend server: `npm run start:server`
5. Start the frontend development server: `npm run start:client`
6. Start the mobile application: `npm run start:mobile`

# Usage
1. Access the web application: `http://localhost:3000`
2. Access the mobile application: `http://localhost:19000`
3. Use the API documentation to interact with the backend server: `http://localhost:8080/api/docs`

# Risks
* **Security:** The project uses authentication and authorization to protect user data, but there is always a risk of vulnerabilities and exploits.
* **Scalability:** The project is designed to handle a moderate number of users, but may require additional infrastructure and optimization to handle large-scale traffic.
* **Dependency management:** The project uses multiple dependencies, which can lead to compatibility issues and conflicts if not managed properly.
* **Data consistency:** The project uses a MongoDB database, which can be prone to data inconsistencies and corruption if not properly maintained.

Note: The recent development updates, such as the addition of `vercel.json` and fixes to Vercel routing, are not explicitly mentioned in this README as they are assumed to be part of the project's ongoing development and maintenance. If you'd like to highlight these updates, you can add a separate section, such as "Recent Updates" or "Changelog", to document these changes.