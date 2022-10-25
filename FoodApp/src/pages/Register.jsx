
import React from 'react'
import styled from 'styled-components'
import { mobile } from '../responsive';
import Navbar from '../components/Navbar.jsx'
import Announcement from '../components/Announcement';

const Container= styled.div`
    width: 100vw;
height: 88vh;
background:
url(https://images.unsplash.com/photo-1551782450-17144efb9c50?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80) center;
display: flex;
align-items: center;
justify-content: center;
`;
const Wrapper= styled.div`
width:40%;
    padding: 20px;
    background-color: orange;
  border-radius: 5px;
  ${mobile({width: "65%"})}
`;
const Title= styled.h1`
    font-size:30px;
    font-weight: 600;
`;
const Form= styled.form`
    display: flex;
    flex-wrap: wrap;
`;
const Input= styled.input`
    flex: 1;
    min-width: 40%;
    margin: 20px 10px 0px 0px;
    padding: 10px;

`;
const Agreement= styled.div`
    font-size:14px;
    margin: 20px 0;
`;
const Button= styled.button`
    width: 40%;
    border: none;
    padding: 15px 20px;
    background-color: black;
    color: white;
`;




function Register() {
  return (
    <>
      <Navbar />
      <Announcement />
      <Container>
          <Wrapper>
            <Title>CREATE AN ACCOUNT</Title>
            <Form>
              <Input placeholder="First Name"/>
              <Input placeholder="Last Name"/>
              <Input placeholder="Username"/>
              <Input placeholder="Email"/>
              <Input placeholder="Password"/>
              <Input placeholder="Confirm Password"/>
              <Agreement>By creating an account, I consent to the processing of my personal data in accordance with the <b>PRIVACY POLICY</b></Agreement>
              <Button>CREATE</Button>
            </Form>
          </Wrapper>
      </Container>
    </>

  );
}

export default Register