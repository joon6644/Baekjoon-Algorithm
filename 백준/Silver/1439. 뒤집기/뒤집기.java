import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();
        S += 'x';

        int cntZero = 0;
        int cntOne = 0;

        for (int i = 1; i < S.length(); i++) {
            int pastNum = S.charAt(i - 1) - '0';
            int currNum = S.charAt(i) - '0';

            if (pastNum != currNum) {
                if (pastNum == 0) {
                    cntZero += 1;
                } else {
                    cntOne += 1;
                }
            }
        }

        System.out.println(Math.min(cntZero, cntOne));
        
        sc.close();
    }
}
