# React-Redux Posts Application
This project is a React-Redux application that fetches posts from an API and allows the user to add new posts. It uses Redux for state management and redux-thunk for handling asynchronous API calls.

## Overview
This is a simple React-Redux application that fetches and displays posts from the JSONPlaceholder API. It also allows users to add new posts through a form.

## Features
Fetch posts from a public API (https://jsonplaceholder.typicode.com/posts)
Display a list of posts
Add new posts using a form
Uses Redux for state management
Async API calls with redux-thunk


## Technologies Used
React: Frontend library for building user interfaces
Redux: State management
Redux-Thunk: Middleware for handling async actions
Axios: For making API calls
Redux DevTools: For easy state debugging in development

## Installation
1. Clone the repository: git clone https://github.com/yourusername/react-redux-posts.git
2. Navigate to the project directory: cd react-redux-posts
3. Run `npm install` to install dependencies
4. Run `npm start` to start the application

## Folder Structure
react-redux-posts/
├── public/
├── src/
│   ├── components/
│   │   ├── PostForm.js
│   │   ├── PostList.js
│   ├── redux/
│   │   ├── actions.js
│   │   ├── reducers.js
│   │   ├── store.js
│   ├── App.js
│   ├── index.js
│   └── ...
├── README.md
└── package.json

## Key Files
src/redux/actions.js: Defines Redux actions for fetching and adding posts.
src/redux/reducers.js: Handles state updates based on dispatched actions.
src/redux/store.js: Sets up the Redux store and applies redux-thunk middleware.
src/components/PostForm.js: Component for adding new posts.
src/components/PostList.js: Component for displaying the list of posts.

## API Integration
The application uses the following API endpoint:
JSONPlaceholder Posts API

## Fetching Posts
The posts are fetched when the PostList component mounts by dispatching the fetchPosts action.

## Adding Posts
You can add a new post using the PostForm component. When the form is submitted, the addPost action is dispatched to send the new post to the API and update the Redux state.

## How to Use
View Posts: The app automatically fetches and displays a list of posts when it loads.
Add a Post: Use the "Add a new post" form to add a post by providing a title and body.