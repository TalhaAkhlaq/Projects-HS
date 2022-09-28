package CompSciA;

import java.util.Scanner;

class TimeConversion {
  public static void main(String[] args) {
    try (Scanner scan = new Scanner(System.in)) {
      System.out.println("Enter the time in minutes: ");
      int min = scan.nextInt();

      int y = min / 60;
      int z = min % 60;

      if (z < 10)
        System.out.println("The time is: " + y + ":0" + z);
      else
        System.out.println("The time is: " + y + ":" + z);
    }

  }

}