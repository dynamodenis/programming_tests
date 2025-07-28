public class IntegerToRomans {
    public static void main(String[] args) {
        // int num = 104;
        // String result = intToRoman(num);
        // System.out.println("The Roman numeral for " + num + " is: " + result);

        String roman = "CIV";
        int intResult = romanToInt(roman);
        System.out.println("The integer for Roman numeral " + roman + " is: " + intResult);

    }

    public static String intToRoman(int num) {
        StringBuilder roman = new StringBuilder();
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                System.out.println("Value: " + values[i] + ", Symbol: " + symbols[i] + ", Remaining: " + num);

                roman.append(symbols[i]);
                num -= values[i];
            }
        }
        return roman.toString();
    }

    public static int romanToInt(String roman) {
        int result = 0;
        int prevValue = 0;

        for (int i = roman.length() - 1; i >= 0; i--) {
            char c = roman.charAt(i);
            System.out.println("Processing character: " + c);
            int value = getRomanValue(c);

            if (value < prevValue) {
                result -= value;
            } else {
                result += value;
            }
            prevValue = value;
            System.out.println("Value " +  value + "Current result: " + result);
        }
        return result;
    }

    private static int getRomanValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: throw new IllegalArgumentException("Invalid Roman numeral: " + c);
        }
    }

}
