import { Text, View, StyleSheet } from 'react-native';

type Props = {
  title: string;
  url: string;
  id: string;
  grade: string;
  notes: string;

}

export default function invididualWallPage() {
    return(
        <View style={styles.container}>
            <Text style={styles.text}>Wall Page!</Text>
        </View>
    );
}

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
  });