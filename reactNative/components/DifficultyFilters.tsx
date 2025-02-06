import { StyleSheet, View, Text, Button } from "react-native";



export default function DifficultyFilters() {
    const buttons = Array.from({length: 10}, (_, index) => `V${index}`);
    return(
        <View style={[
                  styles.container,
                  
                ]}>
                    {buttons.map((label, index) => (
                        <View key={index} style={styles.buttonContainer}>
                            <Button title={label} onPress={() => alert(`${label} pressed`)} />
                                </View>
                    ))}
                </View>

    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: "row",
        flexWrap: "wrap",
        alignContent: "center",
    },
    buttonContainer: {
      width: '18%', 
      margin: 2, 
      
    },
  });

