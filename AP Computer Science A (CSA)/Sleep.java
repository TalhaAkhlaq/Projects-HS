package CompSciA;

import java.util.Scanner;

public class Sleep {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter your birthdate: ");
        System.out.print("Year: ");
        int year1 = scan.nextInt();
        System.out.print("Month: ");
        int month1 = scan.nextInt();
        System.out.print("Day: ");
        int day1 = scan.nextInt();

        System.out.println();
        System.out.println("\nEnter today's date: ");
        System.out.print("Year: ");
        int year2 = scan.nextInt();
        System.out.print("Month: ");
        int month2 = scan.nextInt();
        System.out.print("Day: ");
        int day2 = scan.nextInt();

        int alive = (year2 - year1) * 365 + (month2 - month1) * 30 + (day2 - day1);
        int sleep = alive * 8;

        if (alive>=1000)
            System.out.println("You have been alive for " + (int) alive/1000 + "," + alive%1000 + " days.");
        else
            System.out.println("You have been alive for " + alive + " days.");

        if (sleep>=1000)
            System.out.println("You have slept " + (int) sleep/1000 +"," + "0" +sleep%1000 + " hours.");
        else
            System.out.println("You have slept  " + sleep + " hours.");

    }

}
