import React from 'react';

import Product from './pages/Product';
import Home from './pages/Home'
import ProductList from './pages/ProductList';
import Register from './pages/Register';
import Login from './pages/Login';
import Cart from './pages/Cart';

import {BrowserRouter, Route, Routes} from 'react-router-dom';

function App() {
  return (
  <>
    {/* <Home/> */}
    {/* <ProductList/> */}
    {/* <Product /> */}
    {/* <Register/> */}
    {/* <Login/> */}
    {/* <Cart /> */}
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/product-list" element={<ProductList/>}/>
        <Route path="/product" element={<Product/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/cart" element={<Cart/>}/>
      </Routes>

    </BrowserRouter>
  </>
  );
}

export default App;
