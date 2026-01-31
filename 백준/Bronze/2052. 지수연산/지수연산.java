import java.util.Scanner;
import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        BigDecimal base = new BigDecimal("0.5");

        BigDecimal ans = base.pow(N);

        System.out.println(ans.toPlainString());

        scanner.close();
    }
}