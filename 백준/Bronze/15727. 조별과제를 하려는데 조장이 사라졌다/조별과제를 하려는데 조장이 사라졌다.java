import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double L = sc.nextDouble();

        System.out.println((int) Math.ceil(L / 5));

        sc.close();
    }
}