# Onboarding
Welcome to our project! This guide will help you get started with setting up the project, understanding the important files, and navigating the project flow.

## Setup
To get started, follow these steps:
1. Clone the repository from https://github.com/HACKWAVE2025/B09.
2. Install the required dependencies by running `npm install` or `yarn install` in the terminal.
3. Set up your development environment by following the instructions in the `README.md` file.

## Important Files
Here are some key files to understand:
* `vercel.json`: Configuration file for Vercel deployment.
* `mobile/app/_layout.tsx`: React component for the RootLayout.
* `backend/routes/userRoutes.js`: Express route for user-related operations (e.g., login, register, complete-level).
* `backend/models/Activity.js` and `backend/models/Image.js`: Mongo database models for Activity and Image.
* `mobile/app/(tabs)/ProfilePage.tsx`: React component for the ProfilePage.
* `mobile/components/external-link.tsx`: React component for external links.

## Project Flow
The project flow is as follows:
1. The user interacts with the mobile application, which is built using React.
2. The mobile application sends requests to the backend server, which is built using Express.
3. The backend server processes the requests, interacts with the database (Mongo), and returns responses to the mobile application.
4. The mobile application updates the UI based on the responses received from the backend server.

## Recent Development Areas
Recent development has focused on:
* Updating `vercel.json` for Vercel deployment.
* Fixing Vercel routing for Single-Page Applications (SPAs).
* Implementing DailyQuest automatic task completion.
* Developing the Activities Drawer EcoCrush Task Done feature for mobile.
* Deploying the backend server.

## Where to Start
If you're new to the project, start by:
1. Familiarizing yourself with the project structure and important files.
2. Setting up your development environment.
3. Reviewing the recent development areas to understand the current state of the project.
4. Starting with small tasks, such as updating a React component or fixing a bug, to get a feel for the project.
5. Reaching out to the team for guidance and support as needed.

Example use cases:
* Update the `ProfilePage.tsx` component to display additional user information.
* Fix a bug in the `userRoutes.js` file to improve login functionality.
* Implement a new feature, such as a leaderboard, by creating a new Express route and updating the mobile application to interact with it.