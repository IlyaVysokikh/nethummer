import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Registration from './pages/Registration'; 
import Login from './pages/Login';
import Header from './components/Header';
import Footer from './components/Footer';



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Header />
    <Registration />
    <Login />
    <Footer />
  </React.StrictMode>
);
reportWebVitals();
