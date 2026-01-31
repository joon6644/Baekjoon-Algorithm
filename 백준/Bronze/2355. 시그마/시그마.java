import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long A = scanner.nextLong();
        long B = scanner.nextLong();

        System.out.println((A + B) * (Math.abs(B - A) + 1) / 2);

        scanner.close();
    }
}