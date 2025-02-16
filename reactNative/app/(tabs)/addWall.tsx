import { Text, View, StyleSheet, ActivityIndicator, FlatList, ScrollView, Image, Button } from 'react-native';
import { useState } from "react";
import { SERVER_ADDRESS} from '../CONSTANTS';
import { postWall } from '../../utils/server';






export default function DashboardScreen() {
    const [title, setTitle] = useState("")
    const [notes, setNotes] = useState("")
    const [rating, setRating] = useState("")
    const [isSent, setIsSent] = useState(false)
    const [grade, setGrade] = useState("")
    

    const handleSubmit = (event) => {
        console.log("yay it works!")
        event.preventDefault(); // preventDefault? like, preventing HTML default?
        alert(`You've entered: ${notes} | ${rating} | ${title}`)

        var wallData = {
            "title" : title,
            "notes" : notes,
            "rating" : rating,
            "grade" : grade,
            "isSent" : isSent
        }

        postWall(wallData);
        // const requestOptions = {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(wallData)
        // };
        // // fetch("http://127.0.0.1:8000/upload/", requestOptions)
        // fetch(SERVER_ADDRESS + "upload/", requestOptions)
        //     .then(response => response.json())
        //     .then(data => {console.log("Data Recieved after posting")
        //         console.log(data)} );

        

        // JSON.stringify(wallData)


    }

    return(<View style={styles.container}>

        <form style={styles.box} onSubmit={handleSubmit}>

    
    

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

        <label>Grade: <input
            type="text"
            value={grade}
            id="grade"
            onChange={(e) => {
                setGrade(e.target.value) 
            }} />
             </label>

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


        </View>
    )}

    const styles = StyleSheet.create({
        container: {
          flex: 1,
          // backgroundColor: '#25292e',
          backgroundImage: "linear-gradient( #9B7EBD, #4C3D5C)",
          justifyContent: 'center',
          alignItems: 'stretch',
        },
        text: {
          color: '#fff',
        },
        box: {
            flex: 1,
            justifyContent: 'center',
          alignItems: 'stretch',
        }
      });
