import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();
        int k = sc.nextInt();

        int t = (k - 1) / n;
        System.out.println((t / b + 1) + " " + (t % b + 1));

        sc.close();
    }
}