import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float[] prices = {350.34f, 230.90f, 190.55f, 125.30f, 180.90f};
        int T = sc.nextInt();
        
        for (int i = 0; i < T; i++) {
            float ans = 0;

            for (int j = 0; j < 5; j++) {
                ans += sc.nextInt() * prices[j];
            }

            System.out.printf("$%.2f\n", ans);
        }

        sc.close();
    }
}