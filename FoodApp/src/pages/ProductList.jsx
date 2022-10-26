import React from 'react'
import Navbar from '../components/Navbar.jsx'
import Announcement from '../components/Announcement.jsx'
import styled from 'styled-components'
import Products from '../components/Products.jsx';
import Newsletter from '../components/Newsletter';
import Footer from '../components/Footer.jsx';
import { mobile } from '../responsive.js';

const Container = styled.div``;
const Title = styled.h1` margin:20px;`;
const FilterContainer = styled.div` 
  display:flex; 
  justify-content: space-between; 
`;

const Filter = styled.div`
margin:20px;
${mobile({margin: "0 20px", display: "flex", flexDirection: "column"})}
`;

const FilterText = styled.span`
  font-size: 20px;
  font-weight: 600;
  margin-right: 20px;
`;

const Select = styled.select`
padding: 10px;
margin: 20px;

`;
const Option = styled.option``;

function ProductList() {
  return (
    <>
    <Container>
      <Navbar />
      <Announcement />
      <Title>Menu</Title>
      <FilterContainer>
        <Filter>
          <FilterText>Filter Products:</FilterText>
          <Select>
            <Option disabled selected>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
          </Select>
          <Select>
            <Option disabled selected>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
            <Option>Color</Option>
          </Select>
        </Filter>
        <Filter><FilterText>Sort Products:</FilterText>
        <Select>
            <Option selected>Newest</Option>
            <Option>Price</Option>
            <Option>Color</Option>
          </Select>
        </Filter>
      </FilterContainer>

      <Products />
      <Newsletter />
      <Footer />
    </Container>
    </>
  );
}

export default ProductList