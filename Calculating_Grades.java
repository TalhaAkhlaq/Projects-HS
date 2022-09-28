import java.util.Scanner;

class Assignment1 
{
  public static void main(String[] args) 
  {
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Please enter the course name.");
    String courseName = scan.nextLine();
    
    System.out.println("Please enter the average time spent in a week for this course in minutes.");
    int avgTime = scan.nextInt();
    int timeHours = (avgTime / 60); 
    int timeMinutes = (avgTime % 60); 
    
    System.out.println("Please enter the homework grades for this course.");
    int homeWorkGrade1 = scan.nextInt(); 
    int homeWorkGrade2 = scan.nextInt();
    int homeWorkGrade3 = scan.nextInt();
    int homeWorkGrade4 = scan.nextInt();
    double homeWorkGrades = ((homeWorkGrade1 + homeWorkGrade2 + homeWorkGrade3 + homeWorkGrade4) / 4.0);
    
    System.out.println("Please enter the quiz grades for this course.");
    double quizGrade1 = scan.nextDouble();
    double quizGrade2 = scan.nextDouble();
    double quizAvg = ((quizGrade1 + quizGrade2)/ 2);
    
    System.out.println("Please enter the final exam grade for this course.");
    double finalExam = scan.nextDouble(); 
    
    System.out.println("Course name: " + courseName);
    System.out.println("Weekly time spent: " + timeHours + "h" + timeMinutes);
    System.out.println("Average homework grade: " + homeWorkGrades);
    System.out.println("Average quiz grade: " + quizAvg);
    System.out.println("Final exam grade: " + finalExam);
    
    double overall = (((homeWorkGrades * 0.35) + (quizAvg * 0.15) + (finalExam * 0.5)) +0.5);
    System.out.println("Overall grade: " + (int)(overall));
    
    
    
  }
}


    
