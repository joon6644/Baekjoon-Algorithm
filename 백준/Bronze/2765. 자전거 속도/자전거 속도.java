import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        final double PI = 3.1415927;

        int i = 1;
        while (true) {
            double d = sc.nextDouble();
            int r = sc.nextInt();
            double t = sc.nextDouble();

            if (r == 0) { break; }

            double dist = (d * PI * r) / 63360;

            double speed = (dist / t) * 3600;

            System.out.printf("Trip #%d: %.2f %.2f\n", i++, dist, speed);
        }

        sc.close();
    }
}
