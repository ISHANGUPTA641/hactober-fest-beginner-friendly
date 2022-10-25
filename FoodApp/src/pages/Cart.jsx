import { Add, Remove } from '@material-ui/icons';
import React from 'react'
import styled from 'styled-components'
import Announcement from '../components/Announcement';
import Footer from '../components/Footer';
import Navbar from '../components/Navbar';
import Newsletter from '../components/Newsletter';
import { mobile } from '../responsive';

const Container= styled.div`
   
`;
const Wrapper= styled.div`
   padding: 20px;
   ${mobile({padding: "10px"})} 
`;
const Title= styled.h1`
   font-weight: 300;
   text-align: center;
`;
const Top= styled.div`
   display: flex;
   align-items: center;
   justify-content: space-between;
   padding: 20px;
`;
const TopButton= styled.button`
   padding: 10px;
   font-weight: 500;
   cursor: pointer;
   border: ${props=>props.type === "filled" && "none"};
    background-color: ${props=>props.type === "filled" ? "black" : "transparent"};
    color: ${props=>props.type === "filled" && "white"};
`;

const TopTexts= styled.div`
${mobile({display: "none"})} 
`;
const TopText= styled.span`
    text-decoration: underline;
    cursor: pointer;
    margin: 0 10px;
    
`;

const Bottom= styled.div`
   display: flex;
   justify-content: space-between;
   ${mobile({flexDirection: "column", marginTop: "10px"})} 
`;

const Info= styled.div`
   flex: 3;
`;

const Product= styled.div`
   display: flex;
   justify-content: space-between;
   padding: 2px;
   ${mobile({flexDirection: "column"})} 
`;

const ProductDetail= styled.div`
   flex:2;
   display: flex;
`;
const Image= styled.img`
   width:200px;
   ${mobile({width: "190px"})} 
`;
const Details= styled.div`
   padding: 20px;
   display: flex;
   flex-direction: column;
   justify-content: space-around;
`;
const ProductName= styled.span`
   
`;
const ProductId= styled.span`
   
`;
const PriceDetail= styled.div`
   flex: 1;
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
`;

const ProductAmountContainer= styled.div`
    display: flex;
   align-items: center;
   margin-bottom: 20px;
`;
const ProductAmount= styled.div`
    font-size: 24px;
    margin: 5px;
    ${mobile({ margin: "5px 15px"})} 
`;
const ProductPrice= styled.div`
    font-size: 20px;
    font-weight: 200;
    ${mobile({ marginBottom: " 20px"})}
`;

const Hr= styled.hr`
    background-color: #eee;
    border: none;
    height: 1px;
`;

const Summary= styled.div`
   flex: 1;
   border: 0.5px solid lightgray;
   border-radius: 10px;
   padding :20px;
   height: 50vh;
   ${mobile({marginTop: "10px"})} 
`;

const SummaryTitle= styled.h1`
   font-weight: 200;
`;
const SummaryItem= styled.div`
   margin: 30px 0px;
   display: flex;
   justify-content: space-between;
   font-weight: ${props=>props.type=== "total" && "500"}
   font-size: ${props=>props.type=== "total" && "24px"}
`;
const SummaryItemText= styled.span`
   
`;
const SummaryItemPrice= styled.span`
   
`;
const Button= styled.button`
    width: 100%;
    padding: 10px;
    background-color: black;
    color: white;
    font-weight: 600;
`;


function Cart() {
  return (
    <>
      <Container>
          <Navbar/>
          <Announcement />
          <Wrapper>
              <Title>Your Cart</Title>
              <Top>
                  <TopButton>Add More</TopButton>
                  <TopTexts>
                      <TopText>ShoppingBag(2)</TopText>
                      <TopText>YourWishlist(0)</TopText>
                  </TopTexts>
                  <TopButton type="filled">Proceed to Pay</TopButton>
              </Top>
              <Bottom>
                  <Info>
                      <Product>
                          <ProductDetail>
                              <Image src="https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8cGFuZWVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"/>
                              <Details>
                                  <ProductName><b>Saahi Paneer</b></ProductName>
                                  <ProductName><b>Product</b>Something</ProductName>
                                  <ProductName>Some Resturant</ProductName>
                                  <ProductId><b> OrderID</b> 983749274889237</ProductId>
                              </Details>
                          </ProductDetail>
                          <PriceDetail>
                              <ProductAmountContainer>
                                  <Add />
                                  <ProductAmount>2</ProductAmount>
                                  <Remove />
                              </ProductAmountContainer>
                              <ProductPrice>300 Rs.</ProductPrice>
                          </PriceDetail>
                      </Product>
                      <Hr/>
                      <Product>
                          <ProductDetail>
                              <Image src="https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8cGFuZWVyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"/>
                              <Details>
                                  <ProductName><b>Saahi Paneer</b></ProductName>
                                  <ProductName><b>Product</b>Something</ProductName>
                                  <ProductName>Some Resturant</ProductName>
                                  <ProductId><b> OrderID</b> 983749274889237</ProductId>
                              </Details>
                          </ProductDetail>
                          <PriceDetail>
                              <ProductAmountContainer>
                                  <Add />
                                  <ProductAmount>2</ProductAmount>
                                  <Remove />
                              </ProductAmountContainer>
                              <ProductPrice>300 Rs.</ProductPrice>
                          </PriceDetail>
                      </Product>
                  </Info>
                  <Summary>
                      <SummaryTitle>ORDER SUMMARY</SummaryTitle>
                      <SummaryItem>
                          <SummaryItemText>Subtotal</SummaryItemText>
                          <SummaryItemPrice>600 Rs.</SummaryItemPrice>
                      </SummaryItem>
                      <SummaryItem>
                          <SummaryItemText>Delivery Charges</SummaryItemText>
                          <SummaryItemPrice>50 Rs.</SummaryItemPrice>
                      </SummaryItem>
                      <SummaryItem>
                          <SummaryItemText>GST</SummaryItemText>
                          <SummaryItemPrice>50 Rs.</SummaryItemPrice>
                      </SummaryItem>
                      <SummaryItem>
                          <SummaryItemText>VAT</SummaryItemText>
                          <SummaryItemPrice>50 Rs.</SummaryItemPrice>
                      </SummaryItem>
                      <SummaryItem type="total" style={{fontWeight:"800", fontSize:"24px"}}>
                          <SummaryItemText >Total</SummaryItemText>
                          <SummaryItemPrice>750 Rs.</SummaryItemPrice>
                      </SummaryItem>
                      <Button>CHECKOUT NOW</Button>
                  </Summary>
              </Bottom>
          </Wrapper>
          <Newsletter />
          <Footer />
      </Container>
    </>

  );
}

export default Cart