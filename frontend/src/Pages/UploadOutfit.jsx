import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './UploadOutfit.css';
import uploadIcon from '../Components/Assets/upload.jpeg';

const UploadOutfit = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    occasion: '',
    season: '',
    style_theme: '',
    skin_tone: '',
    gender: '',
    clothing_type: '',
    file: null
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: files ? files[0] : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.file) {
      alert('Please select an image to upload.');
      return;
    }

    const uploadData = new FormData();
    uploadData.append('file', formData.file);
    uploadData.append('occasion', formData.occasion);
    uploadData.append('season', formData.season);
    uploadData.append('style_theme', formData.style_theme);
    uploadData.append('skin_tone', formData.skin_tone);
    uploadData.append('gender', formData.gender);
    uploadData.append('clothing_type', formData.clothing_type);

    console.log('Sending request to backend...');

    // Navigate to loading page immediately after submission
    navigate('/loading');

    fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: uploadData
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Response from backend:', data);
        // Navigate to recommendations page with state
        navigate('/recommendations', { state: { recommendations: data.recommendations, advice: data.advice } });
      })
      .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while generating recommendations. Please try again.');
        navigate('/upload-outfit'); // Redirect back to the upload page on error
      });
  };

  return (
    <div className="upload-outfit-page">
      <h2>Upload Your Outfit</h2>
      <form className="upload-form" onSubmit={handleSubmit}>
        <label htmlFor="occasion">Occasion:</label>
        <select id="occasion" name="occasion" value={formData.occasion} onChange={handleChange}>
          <option value="">Select Occasion</option>
          <option value="casual">Casual</option>
          <option value="formal">Formal</option>
          <option value="night out">Night Out</option>
          <option value="office">Office</option>
        </select>

        <label htmlFor="season">Season:</label>
        <select id="season" name="season" value={formData.season} onChange={handleChange}>
          <option value="">Select Season</option>
          <option value="summer">Summer</option>
          <option value="winter">Winter</option>
          <option value="spring">Spring</option>
          <option value="autumn">Autumn</option>
        </select>

        <label htmlFor="style_theme">Style Theme:</label>
        <select id="style_theme" name="style_theme" value={formData.style_theme} onChange={handleChange}>
          <option value="">Select Style Theme</option>
          <option value="elegant">Elegant</option>
          <option value="casual">Casual</option>
          <option value="sporty">Sporty</option>
          <option value="bohemian">Bohemian</option>
          <option value="classic">Classic</option>
        </select>

        <label htmlFor="skin_tone">Skin Tone:</label>
        <select id="skin_tone" name="skin_tone" value={formData.skin_tone} onChange={handleChange}>
          <option value="">Select Skin Tone</option>
          <option value="warm">Warm</option>
          <option value="cool">Cool</option>
          <option value="neutral">Neutral</option>
          <option value="olive">Olive</option>
        </select>

        <label htmlFor="gender">Gender:</label>
        <select id="gender" name="gender" value={formData.gender} onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="men">Men</option>
          <option value="women">Women</option>
          <option value="unisex">Unisex</option>
        </select>

        <label htmlFor="clothing_type">Clothing Type:</label>
        <select id="clothing_type" name="clothing_type" value={formData.clothing_type} onChange={handleChange}>
          <option value="">Select Clothing Type</option>
          <option value="tops">Tops</option>
          <option value="pants">Pants</option>
          <option value="shorts">Shorts</option>
          <option value="skirts">Skirts</option>
          <option value="sweaters">Sweaters</option>
        </select>

        <label htmlFor="outfit-upload" className="custom-file-upload">
          <img src={uploadIcon} alt="Upload Icon" />
        </label>
        <input type="file" id="outfit-upload" name="file" accept="image/*" onChange={handleChange} />

        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadOutfit;
