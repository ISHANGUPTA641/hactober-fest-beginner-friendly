import React from 'react'
import Navbar from '../components/Navbar.jsx'
import Announcement from '../components/Announcement.jsx'
import Slider from '../components/Slider.jsx'
import Categories from '../components/Categories.jsx';
import Products from '../components/Products.jsx';
import Newsletter from '../components/Newsletter.jsx';
import Footer from '../components/Footer.jsx';


function Home() {
  return (
    <>
      <Navbar />
      <Announcement />
      <Slider/>
      <Categories />
      <Products />
      <Newsletter />
      <Footer />
    </>

  );
}

export default Home