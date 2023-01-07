import java.util.Scanner; // import the Scanner class 

public class lecture01{
  // main method entry point of execution
  public static void main(String[] args){
    // 1. Set up the input AND CLOSE INPUT
    Scanner userinput = new Scanner(System.in);

    // 2. print out prompt for user
    System.out.println("Enter a radius of circle: ");
    // 3. variables set
    double radius1 = userinput.nextDouble();
    double area = radius1 * radius1 * 3.14;

    // 4. Format the string so that the double isnt spitting out crazy values
    String areaformatted = String.format("%.2f",area);

    // 5. Print out resulting prompt
    System.out.println("The area of the only circle is: " + areaformatted);

    // close input
    userinput.close();
  }
}
