import { Send } from '@material-ui/icons';
import React from 'react'
import styled from 'styled-components'
import { mobile } from '../responsive';

const Container= styled.div`
    height:60vh;
    background-color:black;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    ${mobile({height: "40vh"})}
`;

const Title= styled.h1`
font-size: 70px;
${mobile({textAlign: "center", fontSize:"40px", margin: "5px 20px"})}
`;
const Description= styled.div`
font-size: 24px;
font-weight: 300;
margin-bottom: 20px;
${mobile({textAlign: "center", fontSize:"16px", margin: "5px 20px"})}
`;
const InputContainer= styled.div`
width: 50%;
height: 40px;
background-color:orange;
display: flex;
justify-content: space-between;
border: 2px solid white;
${mobile({width: "80%", marginTop: " 20px"})}
`;
const Input= styled.input`
border:none;
flex: 8;
padding-left: 20px;
`;
const Button= styled.button`

flex: 1;
background-color:orange;
`;


function Newsletter() {
  return (
    <>
      <Container>
          <Title>Contact Us</Title>
          <Description>Lorem ipsum is a placeholder text commonly used to demonstrate.</Description>
          <InputContainer>
              <Input placeholder="Your Mail"/>
              <Button>
                  <Send/>
              </Button>
          </InputContainer>
      </Container>
    </>

  );
}

export default Newsletter