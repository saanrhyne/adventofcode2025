// this actually needs to be named a1.java, but I like having my files nice and neat
import java.io.*;
import java.util.*;

public class a1 {
  public static void main(String[] args) throws FileNotFoundException {
    int pos = 50;
    int count = 0;
    
    InputStream lines = new FileInputStream("C:/Users/saanv/Downloads/input.txt");
    Scanner input = new Scanner(lines);
    while (input.hasNextLine()) {
      String next = input.nextLine();
      int val = Integer.parseInt(next.substring(1)) % 100;

      if (next.substring(0, 1).equals("L")) {
        if (pos - val < 0) {
          pos = 100 - Math.abs(pos - val);
        } else {
          pos -= val;
        }
      } else {
        if (pos + val > 99) {
          pos = 0 + Math.abs(100 - (pos + val));
        } else {
          pos += val;
        }
      }

      if (pos == 0) {
        count++;
      }
      
    }
    System.out.print(count);
  }
}
