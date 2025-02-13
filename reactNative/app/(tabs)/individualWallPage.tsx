import { Text, View, StyleSheet } from 'react-native';
import { useSearchParams } from 'expo-router/build/hooks';
import { useLocalSearchParams } from 'expo-router/build/hooks';
import { useState, useEffect } from 'react';
import { Image } from 'react-native';
import { Dimensions } from 'react-native';
import { SERVER_ADDRESS } from '../CONSTANTS';

// type Props = {
//   title: string;
//   url: string;
//   id: string;
//   grade: string;
//   notes: string;

// }

type Props = {
  route: {
    params: {
      id: string;
    }
  }
}

export default function InvididualWallPage() {
  const {id} = useLocalSearchParams(); 

  const [isLoading, setLoading] = useState(true)
  const [data, setData] = useState()

  const getWalls = async () => {
    try {
      const response = await fetch(SERVER_ADDRESS + "getWallInfo/?id=" + id);
      const json = await response.json();
      // console.log(json)
      setData(json);
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


    if (data == undefined || data.title == undefined) {
      return (
      <View style={styles.container}>
            <Text style={styles.text}> Sorry, that wall couldn't be found</Text>
          </View>
      )
    }


    return(
        <View style={styles.container}>
          <Text style={styles.text}>Title: {data.title}</Text>
          
          <Image style={styles.image}
                          // source={require('@/assets/images/climbing2.jpeg')}
                          source={{
                            uri: SERVER_ADDRESS + 'getImage?id=' + id}}
                          />

          <Text style={styles.text}>Grade: {data.grade}</Text>
          <Text style={styles.text}>Rating: {data.rating}</Text>
          <Text style={styles.text}>Notes: {data.notes}</Text>

            
        </View>
    );
}


const { width} = Dimensions.get("window")
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#25292e',
      justifyContent: 'center',
      alignItems: 'center',
    },
    text: {
      color: '#fff',
    },
    image: {
      // resizeMode: 'resize',
      // width: "auto",
      // height: "20vh",
      width: width * 0.9,
      height: 200,
      resizeMode: "cover"
    },
    box: {
      
    }

  });