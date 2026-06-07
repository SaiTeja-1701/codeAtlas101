# Onboarding
Welcome to our project! This guide will help you get started with setting up the project, understanding the important files, and navigating the project flow.

## Setup
To get started with the project, follow these steps:

1. Clone the repository from GitHub: `https://github.com/HACKWAVE2025/B09`
2. Install the required dependencies:
	* For the backend: `npm install` in the `backend` directory
	* For the mobile app: `npm install` in the `mobile` directory
3. Set up your development environment:
	* For the backend: start the server with `npm start` in the `backend` directory
	* For the mobile app: start the development server with `npm start` in the `mobile` directory

## Important Files
Here are some key files to understand in the project:

* `vercel.json`: Configuration file for Vercel deployment
* `mobile/app/_layout.tsx`: Root layout component for the mobile app
* `backend/routes/userRoutes.js`: Express routes for user-related endpoints
* `backend/models/Activity.js`: Mongo model for activities
* `mobile/components/external-link.tsx`: React component for external links
* `backend/routes/leaderboardRoutes.js`: Express routes for leaderboard-related endpoints

## Project Flow
The project flow can be broken down into the following components:

1. **Backend**:
	* Handles API requests and sends responses
	* Uses Express.js as the server framework
	* Connects to a MongoDB database using Mongoose
2. **Mobile App**:
	* Built using React Native
	* Uses the backend API for data fetching and manipulation
	* Has multiple screens and components for user interaction
3. **Deployment**:
	* Uses Vercel for deployment and hosting

## Recent Development Areas
Recently, the following areas have seen development:

* **Vercel configuration**: Updated `vercel.json` for improved deployment settings
* **Vite changes**: Updated Vite configuration for improved build and development settings
* **DailyQuest automatic task completion**: Implemented automatic task completion for DailyQuest
* **Index redirects**: Updated index redirects for improved routing
* **Backend deploy**: Deployed backend changes to production
* **Activities Drawer EcoCrush Task Done in Mobile**: Implemented Activities Drawer EcoCrush Task Done feature in the mobile app

## Where to Start
If you're new to the project, here's where you can start:

1. **Familiarize yourself with the codebase**: Take some time to browse through the code and understand the different components and files.
2. **Start with the backend**: Begin by understanding the Express routes and Mongo models in the backend directory.
3. **Work on a feature**: Choose a feature or bug to work on, and start by understanding the relevant code and components.
4. **Join the conversation**: Join the project's communication channels to stay up-to-date with the latest developments and to ask questions.

Remember, this is just a starting point, and you'll learn more as you dive deeper into the project. Good luck, and happy coding!