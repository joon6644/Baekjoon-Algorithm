import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();

        for (int i = 1; i <= N; i++) {
            String S = scanner.nextLine();

            System.out.println(i + ". " + S);
        }
        
        scanner.close();
    }
}