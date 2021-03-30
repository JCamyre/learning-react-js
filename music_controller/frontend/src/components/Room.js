import React, { Component } from 'react';

export default class Room extends Component {
    constructor(props) {
        super(props);
        this.state = {
            votesToSkip: 2,
            guestCanPause: false,
            isHost: false,
        };
        // Match stores all the info related to how we got to this component (Room.js) from the React router. Get params from the url it received.
        this.roomCode = this.props.match.params.roomCode;
        // Force update of information
        this.getRoomDetails();
    }

    // Use api.views, localhost:8000/api/get-room?code=. We are basically using the api.views to fetch information from database
    getRoomDetails() {
        fetch('/api/get-room' + '?code=' + this.roomCode).then((response) => 
         response.json()
        ).then((data) => {
            // If, using the provided room code, gets a 200 response from the api url, set the following states equal to the room's parameters.
            this.setState({
                votesToSkip: data.votes_to_skip,
                guestCanPause: data.guest_can_pause,
                isHost: data.is_host,
            })
        });
    }

    render() {
        return <div>
                <h3>{this.roomCode}</h3>
            <p>Votes: {this.state.votesToSkip}</p>
            <p>Guest Can Pause: {this.state.guestCanPause.toString()}</p>
            <p>Is Host: {this.state.isHost.toString()}</p>
        </div>
    }
}
