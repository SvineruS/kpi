package svinerus;

import java.util.ArrayList;

public class Mid {

    public static String Task3(int height) {
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


    public static int[][] Task4(int[][] matrix) {
        int size = matrix.length;
        int[][] newMatrix = new int[size][size];
        for (int i=0; i<size; i++) {
            for (int j=0; j<size; j++) {
                newMatrix[size-1-i][j] = matrix[j][i];
            }
        }
        return newMatrix;
    }




}
