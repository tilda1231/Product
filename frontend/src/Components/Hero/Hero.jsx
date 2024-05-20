import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Hero.css';
import arrow_icon from '../Assets/arrowIcon.png';
import hero_img from '../Assets/AccessoriesImage1.jpeg';

const Hero = () => {
  const navigate = useNavigate();

  const handleUploadClick = () => {
    navigate('/upload-outfit');
  };

  return (
    <div className='hero'>
      <div className="hero-left">
        <h2>OVER THE ULTIMATE ACCESSORY MATCHING EXPERIENCE WITH OUR AI-POWERED PLATFORM.</h2>
        <div>
          <p>FIND THE PERFECT</p>
          <p>OUTFIT</p>
        </div>
        <h3>OUR CUTTING-EDGE TECHNOLOGY ANALYSES YOUR CLOTHING AND PROVIDES RECOMMENDATIONS TO GO WITH IT BASED ON THE LATEST FASHION TRENDS. GET READY TO ELEVATE YOUR STYLE EFFORTLESSLY.</h3>
        <div className="hero-upload-btn" onClick={handleUploadClick}> 
          <div>Upload Your Outfit Here</div>
          <img src={arrow_icon} alt="arrow" />
        </div>
      </div>

      <div className="hero-right">
        <img src={hero_img} alt="Accessories" />
      </div>
    </div>
  );
}

export default Hero;
