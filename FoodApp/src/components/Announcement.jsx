import React from 'react'
import styled from 'styled-components'
import {mobile} from '../responsive'

const Container= styled.div`
    height:30px;
    background-color:orange;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: bold;
    ${mobile({fontSize: "12px"})}
`;


function Announcement() {
  return (
    <>
      <Container>
          Use coupn code NITDGPRECursion2021 to get 50% off on any order.
      </Container>
    </>

  );
}

export default Announcement