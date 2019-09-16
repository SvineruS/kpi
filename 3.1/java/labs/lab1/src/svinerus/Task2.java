package svinerus;

public class Task2 {

    public static String makePyramid(int height) {
        StringBuilder output = new StringBuilder();

        for (int row_index=0; row_index<height; row_index++) {

            output.append(" ".repeat(height - 1 - row_index));  // fill with spaces

            for (int i=0; i<row_index; i++) {                   // numbers asc
                output.append(i + 1);
            }
            for (int i=row_index; i>=0; i--) {                  // numbers desc
                output.append(i + 1);
            }

            output.append('\n');
        }

        return output.toString();
    }


}
