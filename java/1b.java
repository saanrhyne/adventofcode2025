// this actually needs to be named b1.java, but I like having my files nice and neat

import java.io.*;
import java.util.*;

public class b1 {
  public static void main(String[] args) throws FileNotFoundException {
    int pos = 50;
    int count = 0;
    
    InputStream lines = new FileInputStream("C:/Users/saanv/Downloads/input.txt");
    Scanner input = new Scanner(lines);
    while (input.hasNextLine()) {
      String next = input.nextLine();
      int val = Integer.parseInt(next.substring(1));

      if (next.substring(0, 1).equals("R")) {
        for (int i = 0; i < val; i++) {
          pos++;
          if (pos == 100) {
            pos = 0;
            count++;
          }
        }
      } else {
        for (int i = 0; i < val; i++) {
          pos--;
          if (pos == -1) {
            pos = 99;
          }
          if (pos == 0) {
            count++;
          }
        }
      }
      
    }
    System.out.print(count);
  }
}
