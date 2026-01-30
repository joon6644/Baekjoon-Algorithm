import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        for (int i = 0; i < input.length(); i += 10) {
            int endIndex = Math.min(i + 10, input.length());

            System.out.println(input.substring(i, endIndex));
        } 
        
        scanner.close();
    }
}