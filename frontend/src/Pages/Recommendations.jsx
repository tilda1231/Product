import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './Recommendations.css';

const Recommendations = () => {
  const location = useLocation();
  const { recommendations, advice } = location.state || { recommendations: [], advice: [] };

  useEffect(() => {
    console.log('Recommendations:', recommendations);
    console.log('Advice:', advice);
  }, [recommendations, advice]);

  return (
    <div className="recommendations-page">
      <h2>Recommended Pieces</h2>
      {recommendations.length === 0 ? (
        <div className="no-recommendations">
          <h4>Sadly, we don't have any items in our system that fit your requirements, but here's some advice that may help you find the perfect thing:</h4>
          <div className="advice-list">
            {advice.map((item, index) => (
              <p key={index}>{item}</p>
            ))}
          </div>
        </div>
      ) : (
        <>
          <h4>Based on the clothing you have uploaded, here are some possible options you could pair with it:</h4>
          <div className="recommendations-list">
            {recommendations.map((item, index) => (
              <div key={index} className="recommendation-item">
                <h3>{item.title}</h3>
                <img src={item.img} alt={item.title} />
                <p>{item.description}</p>
              </div>
            ))}
          </div>
          <h2>Advice</h2>
          <div className="advice-list">
            {advice.map((item, index) => (
              <p key={index}>{item}</p>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default Recommendations;
