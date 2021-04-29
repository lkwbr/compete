public class MyClass {

  private static int sNumIntBits = 32;

  public static void main(String args[]) {
    System.out.println(addWithoutPlus(20, 15));
    System.out.println(addWithoutPlus(0, 0));
    System.out.println(addWithoutPlus(100, 549));
  }

  public static int addWithoutPlus(int a, int b) {
    int c = 0, o = 0, x = 0;
    for (int i = 0; i < sNumIntBits; i++) {
      int a_i = (a >> i) & 1;
      int b_i = (b >> i) & 1;
      if ((a_i ^ b_i) == 1) {             // Only one 1
        if (c == 1) { x = 0; c = 1; }
        else x = 1;
      } else if ((a_i & b_i) == 1) {      // Both 1
        if (c == 1) x = 1;
        else { x = 0; c = 1; }
      } else {                            // No 1
        if (c == 1) { x = 1; c = 0; }
        else x = 0;
      }
      o = o | (x << i);
    }
    return o;
  }
}
