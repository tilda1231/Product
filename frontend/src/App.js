import React from 'react';
import Navbar from './Components/Navbar/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import About from './Pages/About';
import Trends from './Pages/Trends';
import Contact from './Pages/Contact';
import UploadOutfit from './Pages/UploadOutfit';
import Loading from './Pages/Loading';
import Recommendations from './Pages/Recommendations';
import AccessoryDetail from './Pages/AccessoryDetail';
import './App.css';

function App() {

  const exampleAccessory = {
    img: './Components/Assets/AccessoriesImage2.jpeg',
    title: 'Example Accessory',
    description: 'This is an example accessory description.',
    link: 'https://www.example.com'
  };

  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/trends" element={<Trends />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/upload-outfit" element={<UploadOutfit />} />
          <Route path="/loading" element={<Loading />} />
          <Route path="/recommendations" element={<Recommendations />} />
          <Route path="/accessory-detail" element={<AccessoryDetail accessory={exampleAccessory} />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
