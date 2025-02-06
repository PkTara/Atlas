import { Link } from "expo-router";
import { StyleSheet, View, Text} from "react-native"

type Props = {
    label: string;
    link: string;
}

export default function LinkButton({label, link}: Props) {
    return(
        <View style={styles.buttonContainer}>
            <Link href={link}> THANK YOU, NEXT </Link>
        </View>
    )
}

const styles = StyleSheet.create({
    buttonContainer: {
      width: "auto",
      height: "auto",
      marginHorizontal: 20,
      marginVertical: 10,
      alignItems: 'center',
      justifyContent: 'center',
      padding: 20,
      backgroundColor: "white",
      borderRadius:10,
    },
    button: {
      borderRadius: 10,
      width: '100%',
      height: '100%',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'row',
    },
    buttonIcon: {
      paddingRight: 8,
    },
    buttonLabel: {
      color: 'black',
      fontSize: 16,
    },
  });
  