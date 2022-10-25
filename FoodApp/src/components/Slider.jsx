import React, { useState } from "react";
import styled from 'styled-components'

import { sliderItems } from "../data"
import {mobile} from '../responsive'

const Container= styled.div`
    height:100vh;
    width: 100%;
    display: flex;
    position: relative;
    overflow: hidden;
    background-color: #000;
    color: #fff;
    ${mobile({width: "100%", height: "250px"})}
`;



const Wrapper =styled.div`
    height: 100%;
    display: flex;
    transform: translateX(${(props) => props.slideIndex * -100} vw);
`;

const Slide =styled.div`
width: 100vw;
height: 100vh;
    display: flex;
    align-items: center;
    
`;

const ImgContainer =styled.div`
    flex:1;
    height: 100%;
`;

const InfoContainer =styled.div`
    flex:1;
    padding: 50px;
    ${mobile({display: "none"})}
`;

const Img =styled.img`
    flex:1;
    height: 80%;
    ${mobile({height: "250px", alignItems: "center",justifyContent: "center"})}
`;

const Title =styled.h1`
    font-size: 70px;
`;

const Desc =styled.p`
    margin : 50px;
    font-size: 20px;
    font-weight: 500;
    letter-spacing: 3px;
`;

const Button =styled.button`
    padding: 10px;
    font-size: 20px;
    background-color: transparent;
    cursor: pointer;
    color: white;
`;

function Slider() {

    const[slideIndex, setSlideIndex] = useState( 0 );
    const handleClick = (direction) =>{
        if(direction ==="left"){
            setSlideIndex(slideIndex >0 ? slideIndex - 1 : 2)
        } else{
            setSlideIndex(slideIndex <2 ? slideIndex + 1 : 0)
        }
    };
  return (
    <>
      <Container>
          
          <Wrapper slideIndex={slideIndex}>
            {sliderItems.map((item) =>(
            <Slide bg={item.bg} key={item.id}>
                <ImgContainer>
                    <Img src={item.img}/>
                </ImgContainer>
                <InfoContainer>
                    <Title>{item.title}</Title>
                    <Desc>{item.desc}</Desc>
                    <Button>ORDER NOW</Button>
                </InfoContainer>
            </Slide> 

            ))}
            
          </Wrapper>
          
      </Container>
    </>

  );
}

export default Slider