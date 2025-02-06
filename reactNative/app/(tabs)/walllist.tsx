import { Text, View, StyleSheet, ActivityIndicator, FlatList, ScrollView, Image, Button } from 'react-native';
import { useState, useEffect } from 'react';
import DropDownPicker from 'react-native-dropdown-picker';
import DifficultyFilters from '@/components/DifficultyFilters';
import WallCard from '@/components/WallCard';
// import Button from '@/components/Button';

type Wall = {
  id: string;
  title: string;
  releaseYear: string;
};

export default function WallList() {
  // const [value, setValue] = useState([]);
  const [isLoading, setLoading] = useState(true)
  const [data, setData] = useState<Wall[]>([])

  const getWalls = async () => {
    try {
      // const response = await fetch("https://reactnative.dev/movies.json");
      const response = await fetch("http://127.0.0.1:8000/");
      const json = await response.json();
      // console.log(json)
      setData(json.wallList);
    } catch (error) {
      console.error(error)
    }
    finally {
      setLoading(false);
    }
    };
  
    useEffect(() => {
      getWalls();
    }, [])

    const walls = [];
    for (let item of data) {
      walls.push(<WallCard url={'@/assets/images/climbing2.jpeg'} id={item.id} label={item.grade + " " + item.title } />)
    }
    


    return(
      <>
      
        <ScrollView style={styles.container}>
            <Text style={styles.text}>Choose A Wall:</Text>

            <DifficultyFilters />

            <View>
              <Text style={styles.text}>Tags:</Text>
              {/* <DropDownPicker
  multiple={true}
  min={0}
  max={5}
  value={value}
  setValue={setValue}
/> */}
            </View>
            
            {(walls) ?    walls : <Text>walls is empty. Is fastapi running?</Text> }

              </ScrollView>

              <Button title={"+"} />
            </>
    );
}

const styles = StyleSheet.create({
    container: {
      // flex: 1,
      // height:"100%",
      padding:20,
      backgroundColor: '#25292e',
      backgroundImage: "linear-gradient( #9B7EBD, #4C3D5C)",
      // justifyContent: 'center',
      // alignItems: 'center',
    },
    text: {
      color: '#fff',
    },
  });