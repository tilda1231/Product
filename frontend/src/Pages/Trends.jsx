import React, { useState } from 'react';
import './Trends.css';
import trend1 from '../Components/Assets/Jewelry.png';
import trend2 from '../Components/Assets/Hats.png';
import trend3 from '../Components/Assets/FallTrends.png';
import trend4 from '../Components/Assets/SpringTrends.png';
import trend5 from '../Components/Assets/MensFashion.png';

const Trends = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const trends = [
    { img: trend1, title: "The New Boho-Chic—9 Jewelry Trends From the Fall 2024 Runways", url: "https://www.vogue.com/article/fall-2024-jewelry-trend-report" },
    { img: trend2, title: "Sun’s Out! Pick Up a New Summer Hat to Celebrate the Season", url: "https://www.vogue.com/slideshow/best-sun-hats-for-summer" },
    { img: trend3, title: "The Top Fall 2024 Fashion Trends: Designers See the World Through a Soft-Focus Lens", url: "https://www.vogue.com/article/the-top-fall-2024-fashion-trends-designers-see-the-world-through-a-soft-focus-lens" },
    { img: trend4, title: "The Top Spring 2024 Fashion Trends Are Here", url: "https://www.vogue.com/article/spring-2024-fashion-trends" },
    { img: trend5, title: "Is the Menswear More Fun at The Womens Collections?", url: "https://www.vogue.com/article/menswear-trends-at-the-fall-2024-womenswear-collections" }
  ];

  const nextSlide = () => {
    if (currentSlide < trends.length - 3) {
      setCurrentSlide(currentSlide + 1);
    }
  };

  const prevSlide = () => {
    if (currentSlide > 0) {
      setCurrentSlide(currentSlide - 1);
    }
  };

  return (
    <div className="trends-page">
      <div className="trends-title">
        <h2>LATEST TRENDS</h2>
      </div>
      <div className="trends-container">
        <button className="nav-button left" onClick={prevSlide}>◀</button>
        <div className="trends-slider" style={{ transform: `translateX(-${currentSlide * (100 / 3)}%)` }}>
          {trends.map((trend, index) => (
            <div key={index} className="trend-item" onClick={() => window.open(trend.url, "_blank")}>
              <img src={trend.img} alt={`Trend ${index + 1}`} />
              <h3>{trend.title}</h3>
            </div>
          ))}
        </div>
        <button className="nav-button right" onClick={nextSlide}>▶</button>
      </div>
      <div className="explinationText">
        <h2>These are the latest fashion trends from Vogue</h2>
      </div>
    </div>
  );
}

export default Trends;
