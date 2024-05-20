// src/Pages/AccessoryDetail.js - didnt get round to implementing this page
import React from 'react';
import './AccessoryDetail.css';

const AccessoryDetail = ({ accessory }) => {
  return (
    <div className="accessory-detail-page">
      <img src={accessory.img} alt={accessory.title} />
      <h2>{accessory.title}</h2>
      <p>{accessory.description}</p>
      <a href={accessory.link} target="_blank" rel="noopener noreferrer">
        View Similar Items
      </a>
    </div>
  );
}

export default AccessoryDetail;
