import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addPost } from './redux/actions';

const PostForm = () => {
  const [title, setTitle] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(addPost({ title }));
    setTitle('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Add a new post"
        required
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default PostForm;
