# Onboarding
=====================================

## Setup
------------

To get started with the project, follow these steps:

1. Clone the repository from GitHub: `https://github.com/HACKWAVE2025/B09`
2. Install the required dependencies:
	* For the backend: `npm install` in the `backend` directory
	* For the mobile app: `npm install` in the `mobile` directory
3. Set up your environment variables:
	* Create a `.env` file in the `backend` directory with your database credentials and other sensitive information
4. Start the development servers:
	* For the backend: `npm run dev` in the `backend` directory
	* For the mobile app: `npm run dev` in the `mobile` directory

## Important Files
-------------------

The following files are crucial to understanding the project:

* `backend/routes/userRoutes.js`: contains Express routes for user authentication and management
* `backend/models/Activity.js`: defines the MongoDB model for activities
* `backend/models/Image.js`: defines the MongoDB model for images
* `mobile/app/_layout.tsx`: the root layout component for the mobile app
* `mobile/app/(tabs)/ProfilePage.tsx`: the profile page component for the mobile app
* `mobile/components/external-link.tsx`: a reusable external link component
* `vercel.json`: configuration file for Vercel deployment

## Project Flow
-----------------

The project consists of a backend API built with Express and a mobile app built with React. The flow is as follows:

1. Users interact with the mobile app, which sends requests to the backend API.
2. The backend API processes the requests, interacts with the database, and returns responses to the mobile app.
3. The mobile app renders the responses to the user.

## Recent Development Areas
---------------------------

Recent developments in the project include:

* Updates to `vercel.json` for Vercel deployment
* Fixes to Vercel routing for single-page applications (SPAs)
* Changes to the Vite configuration
* Implementation of daily quest automatic task completion
* Index redirects and backend deployment
* Activities drawer EcoCrush task completion on mobile

## Where to Start
------------------

To get started with contributing to the project, we recommend the following:

1. Familiarize yourself with the codebase by exploring the important files listed above.
2. Set up your local development environment by following the setup instructions.
3. Start with small tasks, such as fixing bugs or implementing new features in the mobile app or backend API.
4. Reach out to the team for guidance and feedback on your contributions.

Some potential starting points for new contributors include:

* Implementing new features in the mobile app, such as a new tab or component
* Fixing bugs in the backend API or mobile app
* Improving the performance or security of the application
* Adding new tests to the existing test suite