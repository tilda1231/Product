import React from 'react';
import './About.css';
import logo from '../Components/Assets/logo.png'; // Ensure the path is correct
import fashion1 from '../Components/Assets/AI.jpeg';
import fashion2 from '../Components/Assets/AccessoriesImage3.jpeg';

const About = () => {
  return (
    <div className="about-page">
      <h2>About Us</h2>
      <img src={logo} alt="Logo" className="about-logo" />
      <p>Struggling to find the perfect outfit? Well, we have got you covered.</p>
      <p>WardrobeWhiz uses advanced AI technology to help you find the perfect item of clothing that complement your outfit, or favourite item. Whether you're looking for the latest trends or timeless classics, we've got something for everyone.</p>
      <div className="fashion-images">
        <img src={fashion1} alt="Fashion 1" />
        <div className="plus-sign">+</div>
        <img src={fashion2} alt="Fashion 2" />
      </div>
    </div>
  );
}

export default About;
