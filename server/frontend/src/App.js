import React from 'react';
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Dealers from "./components/Dealers/Dealers";
import Dealer from "./components/Dealers/Dealer";
import PostReview from "./components/Dealers/PostReview";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
      {/* Route to list all dealers */}
      <Route path="/dealers" element={<Dealers />} />
      {/* Route to view a single dealer's details and reviews */}
      <Route path="/dealer/:id" element={<Dealer />} />
      {/* Route to post a review for a dealer */}
      <Route path="/postreview/:id" element={<PostReview />} />
      {/* Add additional routes (home, about, etc.) as needed */}
    </Routes>
  );
}

export default App;
