import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;

        for (int i = 0; i < 5; i++) {
            int val = scanner.nextInt();

            if (val < 40) {
                val = 40;
            }

            sum += val;
        }

        System.out.println(sum / 5);
        
        scanner.close();
    }
}