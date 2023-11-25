import React, { Component } from 'react'
import {Navbar} from 'react-bootstrap'


export default class Header extends Component {
  render() {
    return (
      <Navbar>
        <Container>
            <Navbar.brand href='/'>
                <img
                src=''
                />
            </Navbar.brand>
        </Container>
      </Navbar>
    )
  }
}

