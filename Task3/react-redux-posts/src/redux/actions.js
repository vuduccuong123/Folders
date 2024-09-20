// src/redux/actions.js
import axios from 'axios';

export const FETCH_POSTS = 'FETCH_POSTS';
export const ADD_POST = 'ADD_POST';

// Fetch posts action
export const fetchPosts = () => async (dispatch) => {
  const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
  dispatch({
    type: FETCH_POSTS,
    payload: response.data,
  });
};

// Add a new post action
export const addPost = (post) => async (dispatch) => {
  const response = await axios.post('https://jsonplaceholder.typicode.com/posts', post);
  dispatch({
    type: ADD_POST,
    payload: response.data,
  });
};
