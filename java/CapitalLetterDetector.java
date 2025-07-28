public class CapitalLetterDetector {
    public static void main(String[] args) {
        String input = "Hello World! Java is FUN.";
        int capitalCount = 0;

        // for (char ch : input.toCharArray()) {
        //     if (Character.isUpperCase(ch)) {
        //         System.out.println("Capital letter detected: " + ch);
        //         capitalCount++;
        //     }
        // }

        for (int i =0; i < input.length(); i++){
            char ch = input.charAt(i);
            if (Character.isUpperCase(ch)) {
                System.out.println("Capital letter detected: " + ch);
                capitalCount++;
            }
        }

        System.out.println("Total capital letters: " + capitalCount);
    }
}
