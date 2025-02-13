import { Link } from "expo-router";
import { StyleSheet, View, Text, Image, Pressable} from "react-native"

type Props = {
    label: string;
    url: string;
    id: string;
}

export default function WallCard({label, url, id}: Props) {
  // console.log('http://127.0.0.1:8000/getImage/' + id)
    
    return(
        <View style={styles.container}>
          <Link href={{
            pathname: "./individualWallPage/?id=" + id, // The current query params isn't ideal, should eventually switch to dynamic segments. But it works, god damn it, it works!
            // params: {id : id}
          }} asChild>
          <Pressable 
          // onPress={()=>
            // NavigationPreloadManager.navigate("./individualWallPage", {"cool data" : 5})
          // }
          >
            
            <Image style={styles.image}
                // source={require('@/assets/images/climbing2.jpeg')}
                source={{
                  uri: 'http://127.0.0.1:8000/getImage?id=' + id}}
                />
                <Text style={styles.textStyle}>{label}</Text>
                </Pressable>
                </Link>
        </View>
    )
}

const styles = StyleSheet.create({
  container: {
    // justifyContent: "center",
    // alignContent: "center",
    // width: ,
    // height: 500,
    margin: 10,
    backgroundColor: "white",
    width: "90vw",
    // height: "25vh",
   
    
  },
  textStyle: {
    padding:5,
  },
  image: {
    resizeMode: 'resize',
    width: "auto",
    height: "20vh",
  }
  });
  