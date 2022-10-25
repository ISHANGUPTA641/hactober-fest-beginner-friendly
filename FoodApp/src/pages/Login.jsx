import React from 'react'
import Navbar from '../components/Navbar.jsx'
import styled from 'styled-components'
import { mobile } from '../responsive';
import Announcement from '../components/Announcement.jsx';

const Container= styled.div`
    width: 100vw;
height: 88vh;
background:
url(https://images.unsplash.com/photo-1457460866886-40ef8d4b42a0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80) center;
background-size: cover;
display: flex;
align-items: center;
justify-content: center;
`;
const Wrapper= styled.div`
width:20%;
    padding: 20px;
    background-color: orange;
  border-radius: 5px;
  border: 2px solid black;
  ${mobile({width: "60%"})}
`;
const Title= styled.h1`
    font-size:30px;
    font-weight: 600;
`;
const Form= styled.form`
    display: flex;
    flex-direction: column;
`;
const Input= styled.input`
    flex: 1;
    min-width: 40%;
    margin: 10px 0;
    padding: 10px;

`;
const Button= styled.button`
    width: 40%;
    border: none;
    padding: 15px 20px;
    background-color: black;
    color: white;
    margin-bottom: 10px;
`;

const Link= styled.a`
 padding: 5px;
 font-size:12px;
 text-decoration: underline;
 cursor: pointer;

 &:hover {
     color: blue;
 }
`;


function Login() {
  return (
    <>
      <Navbar />
      <Announcement/>
      <Container>
      <Wrapper>
            <Title>Login</Title>
            <Form>
              <Input placeholder="Username"/>
              <Input placeholder="Password"/>
              <Button>Login</Button>
              <Link>Forgot Pssword</Link>
              <Link href="/register">Create a new account.</Link>
            </Form>
          </Wrapper>
      </Container>
    </>

  );
}

export default Login