# Project Overview
This project is a MERN (MongoDB, Express, React, Node) application, utilizing the MVC (Model-View-Controller) architecture. It provides a comprehensive framework for managing eco-friendly tasks and activities, with a robust backend API and a user-friendly frontend interface.

# Features
- User profiling and authentication
- EcoTask management and completion tracking
- Activities dashboard with summaries and updates
- Responsive design for mobile and web applications
- Integration with Vercel for seamless deployment and routing

# Tech Stack
- **Backend:** Node.js, Express.js, MongoDB
- **Frontend:** React, JavaScript, CSS
- **Deployment:** Vercel
- **Database:** MongoDB

# Architecture
The application follows the MVC architecture, with the following components:
- **Models:** Define the structure and schema of the data stored in the database (Located in `models/` directory)
- **Controllers:** Handle API requests, interact with models, and return responses (Located in `routes/` directory)
- **Views:** Render the user interface and display data to the user (Located in `components/` and `pages/` directories)

# Setup
To set up the project locally:
1. Clone the repository: `git clone https://github.com/HACKWAVE2025/B09.git`
2. Install dependencies: `npm install`
3. Start the backend server: `node backend/server.js`
4. Start the frontend development server: `npm run start`

# Usage
- Access the application at `http://localhost:3000`
- Use the navigation menu to explore different features and pages
- Complete eco-tasks and track progress on the Activities dashboard

# Risks
- **Database Security:** Ensure proper security measures are in place to protect sensitive user data stored in the database.
- **API Routing:** Be cautious when updating Vercel routing configurations to avoid disruptions to the application's functionality.
- **Dependency Updates:** Regularly review and update dependencies to prevent vulnerabilities and ensure compatibility with the latest versions of Node.js and React.
- **Mobile Application Performance:** Optimize the mobile application for better performance, considering factors such as network latency and device capabilities.