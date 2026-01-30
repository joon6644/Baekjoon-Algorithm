import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String input = scanner.next();

        int endIndex = 0;
        int startIndex = 0;

        for (int i = 0; i <= input.length() / 10; i++) {
            startIndex = i * 10;
            if (startIndex + 10 > input.length()) {
                endIndex = input.length();
            } else {
                endIndex = startIndex + 10;
            }
            System.out.println(input.substring(startIndex, endIndex));
        } 
    }
}