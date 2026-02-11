import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int ans = 0;
        int M = sc.nextInt();

        for (int i = 0; i < M; i++) {
            ans += A[sc.nextInt() - 1];
        }

        System.out.println(ans);

        sc.close();
    }
}
