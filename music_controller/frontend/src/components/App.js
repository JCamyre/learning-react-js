import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from './HomePage';


// Functions better than classes for React
export default class App extends Component {
    constructor(props) {
        super(props);
        // this.state = {}, when updated, rerenders the component (rather than entire webpage)
    }

    render() {
        return (
        <div>
            <HomePage />
        </div>
        );
    }
}

const appDiv = document.getElementById('app');
render(<App name='yo'/>, appDiv)
