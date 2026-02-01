import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int[] S = new int[N + M];

        for (int i = 0; i < N; i++) {
            S[i] = scanner.nextInt();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N + M; j++) {
                int T = scanner.nextInt();
                S[i] -= T;
                S[j] += T;
            }
        }

        for (int i : S) {
            System.out.print(i + " ");
        }

        scanner.close();
    }
}