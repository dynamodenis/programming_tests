public class ReverseString {

    public static void main(String [] args){
        String str = "Hello World";
        reverseUsingStringBuilder(str);
        String reversedStr = reverseString(str);
        System.out.println("Reversed String: " + reversedStr);
    }

    public static void reverseUsingStringBuilder(String str) {
        StringBuilder sb = new StringBuilder(str);
        sb.reverse();
        System.out.println("Reversed String: " + sb.toString());
    }

    public static String reverseString(String str) {
        // StringBuilder reversed = new StringBuilder();

        // for (int i = str.length() -1; i >= 0; i--){
        //     reversed.append(str.charAt(i));
        // }

        // return reversed.toString();
        // OR

        // Using For Loop
        String reversed = "";
        for (int i = str.length() - 1; i >= 0; i--){
            reversed += str.charAt(i);
        }
        return reversed;

    }

}
