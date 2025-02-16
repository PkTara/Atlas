import { SERVER_ADDRESS } from "../CONSTANTS";

interface IWallData {
    "title" : string,
    "notes" : string,
    "rating" : string,
    "grade" : string,
    "isSent" : boolean
}

function postWall(wallData : IWallData) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(wallData)
    };

    fetch(SERVER_ADDRESS + "upload/", requestOptions)
        .then(response => response.json())
        .then(data => {console.log("Data Recieved after posting")
            console.log(data)} );
}

function fetchWallInfo(id:string) {

    fetch(SERVER_ADDRESS + "getWallInfo/?id=" + id)
            .then(response => response.json())
            .then(data => {console.log("Data Recieved after posting");
                return(data)} );

}

function fetchAllWalls() {

    fetch(SERVER_ADDRESS)
            .then(response => response.json())
            .then(data => {console.log("Data Recieved after posting");
                return(data)} );

}