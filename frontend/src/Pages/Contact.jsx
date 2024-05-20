import React from 'react';
import './Contact.css';
import contactImage from '../Components/Assets/contactUs.jpeg'; // Ensure the path to your image is correct

const Contact = () => {
  return (
    <div className="contact-page">
      <div className="contact-content">
        <div className="contact-text">
          <h2>Contact Us</h2>
          <p>If you have any questions or need assistance, please feel free to reach out to us.</p>
          <div className="contact-info">
            <p>Email:  info@fashionhub.co.uk</p>
            <p>Phone: +44 20 7946 0958</p>
            <p>Address: 123 Fashion Street, Trendy Town, London, W1A 1AA, UK</p>
          </div>
        </div>
        <div className="contact-image-container">
          <img src={contactImage} alt="Contact Us" className="contact-image" />
        </div>
      </div>
    </div>
  );
}

export default Contact;
