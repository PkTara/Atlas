import { StyleSheet, View, Text } from "react-native";

type Props = {
    text: string;
};

export default function TextBox({text}: Props) {
    return(
        <View
                style={[
                  styles.textContainer,
                  
                ]}>
                    <Text style={[styles.textStyle, { color: '#25292e' }]}>{text}</Text>
                </View>

    )
}

TextBox.defaultProps = {
  text: 'Default Text',
  width: "auto",
  height: "auto"
};

const styles = StyleSheet.create({
    textContainer: {
        marginHorizontal: 20,
        marginVertical: 10,
        backgroundColor: "white",
        borderRadius: "10px",
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
      },
      textStyle: {
        color: '#fff',
        fontSize: 16,
      },
})

