import React from 'react'
import styled from 'styled-components'

import {Search,ShoppingCartOutlined} from "@material-ui/icons"
import Badge from '@material-ui/core/Badge';

import {mobile} from '../responsive'

const Container = styled.div`
    height: 60px;
    ${mobile({height: "50px"})}
    
`;

const Wrapper = styled.div`
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    ${mobile({padding: "10px 0px"})}
`;

const Left = styled.div`
    flex:1;
    display: flex;
    align-items: center;
    ${mobile({flex: 2})}
`;


const SearchComponents = styled.span`
    border: 1px solid #001;
    border-radius:5PX;
    display: flex;
    align-items: center;
    margin-left: 20px;
    padding: 5px;

`;

const Input = styled.input`
    border: none;
    ${mobile({width: "40px"})}
`;

const Center = styled.div`
    flex:1;
    text-align:center;
    ${mobile({flex: 2})}
`;

const Logo = styled.a`
    font-weight: bold;
    font-size: 30px;
    text-decoration: none !important;
    ${mobile({fontSize: "18px" })};
    cursor: pointer;
    color: black;
`;

const Right = styled.div`
    flex:1;
    display:flex;
    align-items:center;
    justify-content: flex-end;
    font-size: 30px;
    ${mobile({justifyContent: "center", flex: 4})}
`;

const MenuItem = styled.a`
font-size:14px;
cursor: pointer;
margin-left:25px;
text-decoration: none !important;
color:black;
${mobile({fontSize: "12px", marginLeft:"10px"})}
`;


function Navbar() {
  return (
    <>
      <Container>
          <Wrapper>
              <Left>
                  <SearchComponents>
                        <Input placeholder="Search"/>
                        <Search style={{color:"gray", fontSize:16}}/>
                  </SearchComponents>
              </Left>
              <Center>
                  <Logo href="/">Food App</Logo>
              </Center>
              <Right>
                <MenuItem href="/register">REGISTER</MenuItem>
                <MenuItem href="/login">SIGN IN</MenuItem>
                <MenuItem href="/cart">
                <Badge color="secondary" badgeContent={4}>
                    <ShoppingCartOutlined />
                </Badge>
                </MenuItem>
              </Right>
          </Wrapper>
      </Container>
    </>

  );
}

export default Navbar