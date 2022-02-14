import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Extra_Long_Factorials {
    
    private static BigInteger factorial(int n) {
        BigInteger fact = BigInteger.valueOf(1);
        for (int i=n; i >= 1; --i) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        BigInteger fact = factorial(n);
        System.out.println(fact.toString());
    }
}