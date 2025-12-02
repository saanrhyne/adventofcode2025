// this actually needs to be named a2.java, but I like having my files nice and neat
import java.io.*;
import java.util.*;

public class a2 {
  public static void main(String[] args) throws FileNotFoundException {
    long sum = 0;
    
    InputStream lines = new FileInputStream("C:/Users/saanv/Downloads/input.txt");
    Scanner input = new Scanner(lines);
    String[] ids = input.nextLine().strip().split(",");
    for (String id : ids) {
      long start = Long.parseLong(id.substring(0, id.indexOf("-")));
      long stop = Long.parseLong(id.substring(id.indexOf("-") + 1));
      for (Long i = start; i <= stop; i++) {
        if ((Long.toString(i)).substring(0, (Long.toString(i)).length() / 2).equals((Long.toString(i)).substring((Long.toString(i)).length() / 2))) {
          sum += i;
        }
      }
    }

    System.out.print(sum);
  }
}
