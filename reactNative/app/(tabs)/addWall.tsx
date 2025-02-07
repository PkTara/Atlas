import { Text, View, StyleSheet, ActivityIndicator, FlatList, ScrollView, Image, Button } from 'react-native';
import { useState } from "react";






export default function DashboardScreen() {
    const [title, setTitle] = useState("")
    const [notes, setNotes] = useState("")
    const [rating, setRating] = useState("")
    const [isSent, setIsSent] = useState(false)
    

    const handleSubmit = (event) => {
        console.log("yay it works!")
        event.preventDefault(); // preventDefault? like, preventing HTML default?
        alert(`You've entered: ${notes} | ${rating}`)

        var wallData = {
            "title" : title,
            "notes" : notes,
            "rating" : rating,
            "isSent" : isSent
        }

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(wallData)
        };
        fetch("http://127.0.0.1:8000/", requestOptions)
            .then(response => response.json())
            .then(data => {console.log("Data Recieved after posting")
                console.log(data)} );

        

        // JSON.stringify(wallData)


    }

    return(<>

        <form onSubmit={handleSubmit}>

    

        <label>Notes: <input
            type="text"
            value={notes}
            id="notes"
            onChange={(e) => {
                setNotes(e.target.value) 
            }} />
             </label>

        <label>Title</label> <input
        type="text"
        value={title}
        id="title"
        onChange={(e) => {
            setTitle(e.target.value) 
        }}></input>

        <label>Rating</label> <input 
            type="text"
            value={rating}
            id="rating"
            onChange={(e) => {
                setRating(e.target.value) 
            }}></input>

        {/* <label>Sent: </label> <input 
        type="checkbox"
        value={isSent}
        id="isSent"
        onChange={(e) => {
            setIsSent(e.target.value) 
        }}></input> */}

        <input type="submit" />

        {/* <Button onClick={handleSubmit} title={"Submit"}/> */}


        </form>


        </>
    )}
