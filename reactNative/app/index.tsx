import { Text, View, StyleSheet } from 'react-native';
import TextBox from '@/components/TextBox'; 
import LinkButton from "@/components/LinkButton"
import { Link } from "expo-router"


export default function IndexScreen() {
    return(
      <>
        <View style={styles.container}>
            <TextBox text="Welcome To ClimbLog!"></TextBox>
            <TextBox text="ClimbLog is a climbing log where you can keep track of your attempts, see what others have to say, and even compete against eachother!"></TextBox>
            <TextBox text="This guide is open source, meaning you can help contribute to it! In fact, we rely on contributions - all walls are user submitted and tagged, so if you see something missing, add it!"></TextBox>
        <LinkButton label="THANK YOU, NEXT" link="/walllist"></LinkButton>
        </View>
        
        </>
    );
}

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
  });