# Project Overview
The B09 project is a MERN (MongoDB, Express, React, Node) stack application built using the Node framework and following the MVC (Model-View-Controller) architecture. The project consists of a backend API, a frontend web application, and a mobile application. The project aims to provide a platform for users to engage with eco-friendly tasks and activities.

# Features
The project features the following functionalities:
* User profile management
* Eco-task completion and tracking
* Activities and task management
* API integration for backend services
* React components for frontend and mobile applications
* Vite and Vercel integration for development and deployment

# Tech Stack
The project utilizes the following technologies:
* Node.js as the backend framework
* Express.js as the backend framework
* MongoDB as the database management system
* React.js as the frontend framework
* Vite as the development server
* Vercel as the deployment platform
* Render as the backend deployment platform

# Architecture
The project follows the MVC architecture, with the following components:
* **Models**: Define the structure and schema of the data stored in the database
* **Controllers**: Handle API requests and interactions with the database
* **Routes**: Define the API endpoints and mapping to controllers
* **Components**: React components for frontend and mobile applications
* **Utils**: Utility functions for common tasks and operations

# Setup
To set up the project, follow these steps:
1. Clone the repository from GitHub
2. Install the required dependencies using `npm install`
3. Set up the database connection using MongoDB
4. Configure the backend API using environment variables
5. Start the development server using `npm run dev`

# Usage
To use the project, follow these steps:
1. Start the development server using `npm run dev`
2. Access the frontend web application at `http://localhost:3000`
3. Access the mobile application using a mobile device or emulator
4. Interact with the application using the provided features and functionalities

# Risks
The project is subject to the following risks:
* **Security risks**: Potential vulnerabilities in the backend API and database management system
* **Performance risks**: Potential performance issues with the frontend and mobile applications
* **Deployment risks**: Potential issues with deployment and configuration of the Vercel and Render platforms
* **Maintenance risks**: Potential challenges with maintaining and updating the project's dependencies and technologies

Important directories and files:
* `components`: React components for frontend and mobile applications
* `pages`: Frontend pages and routes
* `utils`: Utility functions for common tasks and operations
* `models`: Database schema and models
* `routes`: API endpoints and mapping to controllers
* `server.js`: Backend API server
* `reset-project.js`: Script for resetting the project configuration

Recent developments:
* Updated `vercel.json` configuration
* Fixed Vercel routing for SPA
* Implemented DailyQuest automatic task completion
* Updated index redirects
* Deployed backend API to Render platform
* Completed Activities Drawer EcoCrush task in mobile application