import { Facebook, Instagram, LinkedIn, MailOutline, Phone, Room, Twitter, YouTube } from '@material-ui/icons';
import React from 'react'
import styled from 'styled-components'
import { mobile } from '../responsive';

const Container= styled.div`
    height:30px;
    background-color:white;
    display: flex;
    ${'' /* align-items: center;
    justify-content: center; */}
    ${'' /* font-size: 14px;
    font-weight: bold; */}
    ${mobile({flexDirection: "column", })}
   
`;
const Left= styled.div`
flex:1;
display: flex;
flex-direction: column;
padding: 20px;
`;

const Logo= styled.h1`
font-size: 30px;
`;

const Desc= styled.p`
margin: 20px 0px;
font-size: 16px;
`;

const SocialContainer= styled.div`
display: flex;
`;

const SocialIcon= styled.div`
width: 40px;
height: 40px;
border-radius: 50%;
color: white;
background-color: #${props=>props.color};
display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 20px;
`;

const Center= styled.div`
flex:1;
padding: 20px;
${mobile({display: "none"})}
`;

const List= styled.ul`
margin: 0px;
padding: 0px;
font-size: 20px;
margin-bottom:40px;
list-style: none;
display: flex;
flex-wrap: wrap;


`;

const ListItem= styled.li`
width: 50%;
font-size: 16px;
margin-bottom: 10px;
`;

const Title= styled.h3`
margin-bottom:30px;
`;

const Right= styled.div`
flex:1;
padding: 20px;
${mobile({backgroundColor: "#eee"})}
`;

const ContactItem= styled.div`
margin-bottom: 20px;
display: flex;
align-items: center;
`;

const Payment= styled.img`
width: 50%
`;

function Footer() {
  return (
    <>
      <Container>
          <Left>
            <Logo>Food App</Logo>
            <Desc>
            Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.Lorem ipsum is a placeholder text commonly used to 
            </Desc>
            <SocialContainer>
                <SocialIcon color="385999">
                    <Facebook/>
                </SocialIcon>
                <SocialIcon color="385999">
                    <LinkedIn/>
                </SocialIcon>
                <SocialIcon color="e4405f">
                    <Instagram/>
                </SocialIcon>
                <SocialIcon color="55acee">
                    <Twitter/>
                </SocialIcon>
                <SocialIcon color="FF0000">
                    <YouTube/>
                </SocialIcon>
            </SocialContainer>
          </Left>
          <Center>
              <Title>Useful Links</Title>
              <List>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
                  <ListItem>Home</ListItem>
              </List>
          </Center>
          <Right>
              <Title >Contact</Title>
              <ContactItem style={{fontSize:"16px"}}><Room style={{marginRight: "10px"}}/>
                  545 South Nagar, India 875873
              </ContactItem>
              <ContactItem style={{fontSize:"16px"}}><Phone style={{marginRight: "10px"}}/>
                  +91 875873564
              </ContactItem>
              <ContactItem style={{fontSize:"16px"}}><MailOutline style={{marginRight: "10px"}}/>
                  contact@gmail.com
              </ContactItem>
              <Payment src="https://i.ibb.co/Qfvn4z6/payment.png"/>
          </Right>
      </Container>
    </>

  );
}

export default Footer