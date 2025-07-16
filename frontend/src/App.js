import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Chat from "./pages/Chat";
import Home from "./components/Home";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/chat" element={<Chat />} />
        <Route path="/" element={<Home/>} />
      </Routes>
    
    </Router>
  );
}

export default App;
