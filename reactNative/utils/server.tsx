import { SERVER_ADDRESS } from "../app/CONSTANTS";

export interface IWallData {
    "title" : string,
    "notes" : string,
    "rating" : string,
    "grade" : string,
    "isSent" : boolean
}

export function postWall(wallData : IWallData) {
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

export function fetchWallInfo(id:string) : Promise<IWallData> {

    return fetch(SERVER_ADDRESS + "getWallInfo/?id=" + id)
            .then(response => response.json())
            .then(data => {console.log("Data Recieved after posting");
                return(data)} );

}

export function fetchAllWalls() : Promise<IWallData[]> {

    return fetch(SERVER_ADDRESS)
            .then(response => response.json())
            .then(data => {console.log("Data Recieved after posting", data.wallList);
                return(data.wallList)} );

}