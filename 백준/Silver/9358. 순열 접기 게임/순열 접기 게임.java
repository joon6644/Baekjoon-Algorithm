import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 1; i <= T; i++) {
            int N = sc.nextInt();

            int[] arr = new int[N];

            for (int j = 0; j < N; j++) {
                arr[j] = sc.nextInt();
            }

            int half = N;

            while (half > 2) {
                for (int k = 0; k < half; k++) {
                    arr[k] += arr[half - 1 - k];
                }

                half = (half + 1) / 2;
            }

            if (arr[0] > arr[1]) {
                System.out.println("Case #" + i + ": Alice");
            } else {
                System.out.println("Case #" + i + ": Bob");
            }
        }

        sc.close();
    }
}