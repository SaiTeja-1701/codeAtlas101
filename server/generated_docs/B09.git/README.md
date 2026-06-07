# Project Overview
This project is a MERN (MongoDB, Express.js, React, Node.js) application with an MVC (Model-View-Controller) architecture. It is designed to provide a comprehensive solution for eco-friendly tasks and activities. The project includes a backend API built with Node.js and Express.js, and a frontend interface built with React.

# Features
* User authentication and authorization
* Eco-task management and completion tracking
* Activities management and tracking
* Profile page with user information and eco-task summary
* Eco-task page with task details and completion functionality
* Responsive design for both web and mobile applications

# Tech Stack
* Frontend: React, JavaScript
* Backend: Node.js, Express.js, MongoDB
* Deployment: Vercel
* Build Tool: Vite

# Architecture
The project follows an MVC architecture, with the following components:
* **Models**: Define the structure and organization of data in the database (e.g. user, eco-task, activity)
* **Controllers**: Handle requests and responses, and interact with models to perform business logic (e.g. user authentication, eco-task completion)
* **Views**: Render the user interface and display data to the user (e.g. profile page, eco-task page)
* **Routes**: Define the mapping between URLs and controllers (e.g. /api/summarize, /api/users/complete-level)

# Setup
To set up the project, follow these steps:
1. Clone the repository: `git clone https://github.com/HACKWAVE2025/B09.git`
2. Install dependencies: `npm install`
3. Start the backend server: `node backend/server.js`
4. Start the frontend development server: `npm run dev`
5. Build and deploy the application: `npm run build` and `npm run deploy`

# Usage
To use the application, follow these steps:
1. Open the application in a web browser or on a mobile device
2. Navigate to the profile page to view user information and eco-task summary
3. Navigate to the eco-task page to view task details and complete tasks
4. Use the activities drawer to view and manage activities

# Risks
* **Security risks**: The application uses user authentication and authorization to protect user data, but there is still a risk of unauthorized access or data breaches.
* **Scalability risks**: The application is designed to handle a large number of users and requests, but there is still a risk of performance issues or downtime if the application is not properly scaled.
* **Maintenance risks**: The application requires regular maintenance and updates to ensure that it remains secure and stable, but there is still a risk of technical debt or outdated dependencies if maintenance is not prioritized.

Important directories:
* `components`: Contains reusable React components
* `pages`: Contains React pages for the application
* `utils`: Contains utility functions for the application
* `models`: Contains database models for the application
* `routes`: Contains route definitions for the application
* `components`: Contains React components for the mobile application

Recent developments:
* Updated `vercel.json` to improve deployment and routing
* Added `vercel.json` to enable Vercel deployment
* Merged changes from `main` branch to integrate latest features and fixes
* Fixed Vercel routing for single-page application
* Updated Vite configuration for improved build and development performance
* Completed DailyQuest automatic task completion feature
* Implemented index redirects for improved navigation
* Deployed backend application to Render
* Completed Activities Drawer EcoCrush task for mobile application