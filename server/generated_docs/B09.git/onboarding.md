# Onboarding
================

## Setup
---------

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/HACKWAVE2025/B09.git`
2. Install dependencies:
	* For backend: `cd backend` and `npm install`
	* For mobile: `cd mobile` and `npm install`
3. Set up your development environment:
	* For backend: `npm run dev`
	* For mobile: `npm run start`

## Important Files
------------------

The following files are crucial to the project:

* `vercel.json`: Configuration file for Vercel deployment
* `backend/models/`: Directory containing database models (e.g., `Activity.js`, `Image.js`)
* `backend/routes/`: Directory containing Express routes (e.g., `userRoutes.js`, `activityRoutes.js`)
* `mobile/app/`: Directory containing React components (e.g., `RootLayout.tsx`, `ProfilePage.tsx`)
* `mobile/scripts/`: Directory containing scripts (e.g., `reset-project.js`)

## Project Flow
----------------

The project flow is as follows:

1. User interacts with the mobile application
2. Mobile application sends requests to the backend API
3. Backend API processes requests and interacts with the database
4. Backend API returns responses to the mobile application
5. Mobile application updates the user interface based on the responses

## Recent Development Areas
---------------------------

Recent development efforts have focused on:

* Updating `vercel.json` for Vercel deployment
* Fixing Vercel routing for Single-Page Applications (SPAs)
* Implementing Vite changes
* Completing automatic task completion for DailyQuest
* Implementing index redirects
* Deploying the backend
* Developing the Activities Drawer EcoCrush Task Done feature for mobile

## Where to Start
------------------

If you're new to the project, start by:

1. Reviewing the `backend/models/` and `backend/routes/` directories to understand the database schema and API endpoints
2. Exploring the `mobile/app/` directory to understand the React component hierarchy
3. Running the application locally to see how the different components interact
4. Checking the recent development areas to see where the project is headed and how you can contribute

Some specific files to look at:

* `mobile/app/_layout.tsx`: A good starting point for understanding the React component hierarchy
* `backend/routes/userRoutes.js`: A good example of an Express route
* `backend/models/Activity.js`: A good example of a database model

By following these steps and exploring the codebase, you should be able to get a good understanding of the project and start contributing to it.