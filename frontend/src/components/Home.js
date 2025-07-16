import React, { useState } from "react";
import ChatBox from "./ChatBox"; // adjust the path if needed
import "./Home.css";

function Home() {
  const [showChat, setShowChat] = useState(false);

  const toggleChat = () => setShowChat((prev) => !prev);

  return (
    <div className="home-container">
      <h1>Welcome to SMG EV Portal</h1>

      <button className="chat-toggle-btn" onClick={toggleChat}>
        {showChat ? "Close Chat" : "Chat with SMG-EV Assistant"}
      </button>

      {showChat && (
        <div className="chat-wrapper">
          <ChatBox />
        </div>
      )}
    </div>
  );
}

export default Home;
