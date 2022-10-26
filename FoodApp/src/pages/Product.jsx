import { Add, Remove } from '@material-ui/icons';
import React from 'react'
import styled from 'styled-components'
import Announcement from '../components/Announcement';
import Footer from '../components/Footer';
import Navbar from '../components/Navbar';
import Newsletter from '../components/Newsletter';
import { mobile } from '../responsive';

const Container= styled.div``;
const Wrapper= styled.div`
padding: 50px;
display: flex;
${mobile({padding: "10px", flexDirection: "column"})}
`;
const ImgContainer= styled.div`
flex:1;
`;
const Img= styled.img`
width: 100%;
height: 90vh;
object-fit: cover;
${mobile({height: "40vh"})}
`;
const InfoContainer= styled.div`
flex:1;
padding: 0px 50px;
${mobile({padding: "10px"})}
`;
const Title= styled.h1`
font-weight: 200;
`;
const Desc= styled.p`
margin:20px 0px;
`;
const Price= styled.span`
font-weight: 100;
font-size: 40px;
`;

const FilterContainer = styled.div` 
  width: 50%;
  margin: 30px 0;
  display:flex; 
  justify-content: space-between;
  ${mobile({width: "100%"})} 
`;

const Filter = styled.div`margin:20px;`;

const FilterText = styled.span`
  font-size: 20px;
  font-weight: 600;
  margin-right: 20px;
`;

const Select = styled.select`
padding: 10px;
margin: 20px;

`;
const Option = styled.option`
padding: 10px;
margin: 20px;
`;

const AddContainer= styled.div`
width: 50%;
display: flex;
align-items: center;
justify-content: space-between;
${mobile({width: "100%"})} 
`;

const AmountContainer= styled.div`
display: flex;
align-items: center;
font-weight: 700;
`;

const Amount= styled.span`
width: 30px;
height: 30px;
border-radius: 10px;
border: 1px solid orange;
display: flex;
align-items: center;
justify-content: center;
margin: 0px 5px;
`;

const Button= styled.button`
padding: 15px;
border: 2px solid orange;
background-color: black;
color: white;
cursor: pointer;
font-weight: 600;

&:hover {
  background-color: #444444;
}
`;


function Product() {
  return (
  <>
  <Container>
    <Navbar />
    <Announcement />
    <Wrapper>
      <ImgContainer>
        <Img src=""/>
      </ImgContainer>
      <InfoContainer>
        <Title></Title>
        <Desc></Desc>
        <Price></Price>
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
      </FilterContainer>
      <AddContainer>
      <AmountContainer>
        <Remove />
        <Amount>1</Amount>
        <Add />
      </AmountContainer>
        <Button>ADD TO CART</Button>
      </AddContainer>
      </InfoContainer>
    </Wrapper>
    <Newsletter />
    <Footer />

  </Container>
  </>
  )
}

export default Product;