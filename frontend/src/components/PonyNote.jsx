import React, { Component } from 'react';
import { Link } from 'react-router-dom';


export default class PonyNote extends Component {
    render() {
        return (
            <div>
                <h2>Bienvenido a PonyNote!</h2>
                <p>
                    <Link to="/contact">Click Aquí</Link> para contactarnos!
                </p>
            </div>
        )
    }
}