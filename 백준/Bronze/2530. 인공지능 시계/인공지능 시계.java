import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int D = scanner.nextInt();
        
        int s = (C + D) % 60;
        int t1 = (C + D) / 60;

        int m = (B + t1) % 60;
        int t2 = (B + t1) / 60;

        int h = (A + t2) % 24;

        System.out.println(h + " " + m + " " + s);

        scanner.close();
    }
}