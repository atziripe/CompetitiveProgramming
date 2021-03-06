import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the isBalanced function below.
    static String isBalanced(String s) {
        LinkedList<Character> stack = new LinkedList();
        for(char c: s.toCharArray()){
            if(stack.size() > s.length()/2){
                return "NO";
            }
            else{
                if(c == '{' || c=='[' || c=='('){
                    stack.push(c);
                } else{
                    if(stack.isEmpty()){
                        return "NO";
                    }
                    if(esCerrado(stack.pop())!= c){
                        return "NO";
                    }
                }
            }
        }
        if(stack.isEmpty()){
            return "YES";
        } else{
            return "NO";
        }

    }

    private static char esCerrado(char bracket){
        switch(bracket){
            case '{':
                return '}';
            case '[':
                return ']';
            case '(':
                return ')';
            default:
                return ' ';
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String s = scanner.nextLine();

            String result = isBalanced(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
