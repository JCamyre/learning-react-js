import React, { Component } from "react";
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom' 

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <Router>
            <Switch>
                {/* Otherwise, any path with '/', which is all urls rn, will go to the homepage */}
                <Route exact path='/'> 
                    <p>This is home page</p>
                </Route>
                <Route path='/join' component = {RoomJoinPage}/>
                <Route path='/create' component = {CreateRoomPage}/>
            </Switch>
        </Router>
    }
}