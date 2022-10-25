import React from 'react'
import styled from 'styled-components'
import { mobile } from '../responsive';

const Container= styled.div`
flex: 1;
    margin: 3px;
    border: 1px solid gray;
    height: 40vh;
    border-radius: 5px;
    ${'' /* positon: relative; */}
`;

const Image =styled.img`
width:100%;
height:100%;
object-fit: cover;
border-radius: 5px;
${mobile({height: "30vh"})}

`;
const Info= styled.div`
${'' /* position: absolute; */}
${'' /* top: 0;
left: 0; */}
${'' /* width:100%;
height:100%; */}
display: flex;
flex-direction: column;
    align-items: center;
    justify-content: center;
    
`;
const Title= styled.h1`
font-size: 26px;
`;
const Button= styled.button`

padding: 10px;
    font-size: 16px;
    background-color: transparent;
    cursor: pointer;
`;


function CategoryItem({item}) {
  return (
    <>
      <Container>
          <Image src={item.img}/>
          <Info>
              <Title>{item.title}</Title>
              <Button>ORDER NOW</Button>
          </Info>
      </Container>
    </>

  );
}

export default CategoryItem