import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 0; i < T; i++) {
            int N = sc.nextInt();
            long[] arr = new long[2 * N];

            for (int j = 0; j < 2 * N; j++) {
                arr[j] = sc.nextLong();
            }

            Arrays.sort(arr);
            Queue<Long> q = new LinkedList<>();

            System.out.print("Case #" + (i + 1) + ": ");

            for (long item : arr) {
                if (!q.isEmpty() && q.peek() == item) {
                    q.poll();
                } else {
                    System.out.print(item + " ");
                    q.offer(item * 4 / 3);
                }
            }

            System.out.println();
        }

        sc.close();
    }
}