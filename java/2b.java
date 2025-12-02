// this actually needs to be named b2.java, but I like having my files nice and neat
import java.io.*;
import java.util.*;

public class b2 {
  public static void main(String[] args) throws FileNotFoundException {
    long sum = 0;
    
    InputStream lines = new FileInputStream("C:/Users/saanv/Downloads/input.txt");
    Scanner input = new Scanner(lines);
    String[] ids = input.nextLine().strip().split(",");
    for (String id : ids) {
      long start = Long.parseLong(id.substring(0, id.indexOf("-")));
      long stop = Long.parseLong(id.substring(id.indexOf("-") + 1));
      for (Long i = start; i <= stop; i++) {
        for (int j = 1; j <= Long.toString(i).length() / 2; j++) {
          if (Long.toString(i).equals((Long.toString(i)).substring(0, j).repeat(Long.toString(i).length() / j))) {
            sum += i;
            break;
          }
        }
      }
    }
    System.out.print(sum);
  }
}
