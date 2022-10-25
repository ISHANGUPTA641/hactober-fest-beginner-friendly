import { FavoriteBorder, SearchOutlined, ShoppingCartOutlined } from '@material-ui/icons';
import React from 'react'
import styled from 'styled-components'
import { mobile } from '../responsive';

const Info= styled.div`
opacity: 0;
width: 100%;
height: 100%;
position: absolute;
top: 0;left :0;
z-index: 3;
background-color: rgba(0, 0, 0, 0.2);
display: flex;
align-items: center;
justify-content: center;
transition: all 0.5s ease;

`;
const Container= styled.div`
    flex:1;
    margin: 50px;
    min-width: 200px;
    height: 350px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 20px;
    position: relative;
    transition: all 0.5s ease;

    &:hover ${Info}{
        opacity: 1;
        border-radius: 20px;
    }

    ${mobile({margin: "10px"})}
`;

const Circle= styled.div``;
const Image= styled.img`
height: 100%;
border-radius: 20px;
`;

const Icon= styled.div`
width: 40px;
height: 40px;
border-radius: 50%;
background-color: white;
display: flex;
align-items: center;
justify-content: center;
margin: 5px;
transition: all 0.5s ease;
cursor: pointer;

&:hover{
    background-color: #e9f5f5;
    transform: scale(1.2);
}
`;



function Product({item}) {
  return (
    <>
      <Container>
          <Circle />
          <Image src={item.img}/>
          <Info>
              <Icon>
                  <ShoppingCartOutlined />
              </Icon>
              <Icon>
                  <SearchOutlined />
              </Icon>
              <Icon>
                  <FavoriteBorder />
              </Icon>
          </Info>
      </Container>
    </>

  );
}

export default Product