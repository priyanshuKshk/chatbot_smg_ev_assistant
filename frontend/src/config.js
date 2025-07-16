// const config = {
//     API_URL: process.env.REACT_APP_API_URL || "http://localhost:5000",
//   };
  
//   export default config;
  
const isLocalhost = window.location.hostname === "localhost";

const config = {
  API_URL: isLocalhost
    ? "http://localhost:5000"         
    : "https://chatbot-smg-ev-assistant.onrender.com", 
};

export default config;
