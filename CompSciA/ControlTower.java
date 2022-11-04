package CompSciA;
import java.util.Scanner;
import CompSciA.Airplane.Airplane;
public class ControlTower{
    public static void main(String[] args) {
        Airplane a1 = new Airplane();

        Airplane a2 = new Airplane("AAA02", 15.8, 128, 30000);
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the details of the third Airplane(call-sign, distance, bearing and altitude):");

        String cs = scanner.nextLine().toUpperCase();
        double distance = scanner.nextDouble();
        int bearing = scanner.nextInt();
        int altitude = scanner.nextInt();

        Airplane a3 = new Airplane(cs, distance, bearing, altitude);

        System.out.println();
        System.out.println("Initial Positions:");
        System.out.println("\"Airplane 1\": " + a1);
        System.out.println("\"Airplane 2\": " + a2);
        System.out.println("\"Airplane 3\": " + a3);

        System.out.println();
        System.out.println("Initial Distance:");
        System.out.println("The distance between Airplane 1 and Airplane 2 is " + a1.distTo(a2) + " miles.");
        System.out.println("The distance between Airplane 1 and Airplane 3 is " + a1.distTo(a3) + " miles.");
        System.out.println("The distance between Airplane 2 and Airplane 3 is " + a2.distTo(a3) + " miles.");

        System.out.println();
        System.out.println("Initial Height Difference:");
        System.out.println("The height difference between Airplane 1 and Airplane 2 is " + Math.abs(a1.getAlt() - a2.getAlt()) + " feet.");
        System.out.println("The height difference between Airplane 1 and Airplane 3 is " + Math.abs(a1.getAlt() - a3.getAlt()) + " feet.");
        System.out.println("The height difference between Airplane 2 and Airplane 3 is " + Math.abs(a2.getAlt() - a3.getAlt()) + " feet.");

        a1.move(a2.distTo(a3), 65);
        a1.gainAlt();
        a1.gainAlt();
        a1.gainAlt();

        a2.move(8, 135);
        a2.loseAlt();
        a2.loseAlt();

        a3.move(5.0, 55);
        a3.loseAlt();
        a3.loseAlt();
        a3.loseAlt();
        a3.loseAlt();

        System.out.println();
        System.out.println("New Positions: ");
        System.out.println("\"Airplane 1\": " + a1);
        System.out.println("\"Airplane 2\": " + a2);
        System.out.println("\"Airplane 3\": " + a3);

        System.out.println();
        System.out.println("New Distance:");
        System.out.println("The distance between Airplane 1 and Airplane 2 is " + a1.distTo(a2) + " miles.");
        System.out.println("The distance between Airplane 1 and Airplane 3 is " + a1.distTo(a3) + " miles.");
        System.out.println("The distance between Airplane 2 and Airplane 3 is " + a2.distTo(a3) + " miles.");

        System.out.println();
        System.out.println("New Height Difference:");
        System.out.println("The height difference between Airplane 1 and Airplane 2 is " + Math.abs(a1.getAlt() - a2.getAlt()) + " feet.");
        System.out.println("The height difference between Airplane 1 and Airplane 3 is " + Math.abs(a1.getAlt() - a3.getAlt()) + " feet.");
        System.out.println("The height difference between Airplane 2 and Airplane 3 is " + Math.abs(a2.getAlt() - a3.getAlt()) + " feet.");
    }

}

