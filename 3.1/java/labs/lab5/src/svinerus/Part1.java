package svinerus;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {

    static String Main(String filename) throws FileNotFoundException {
        BufferedReader reader= new BufferedReader(new FileReader(filename));

        String max_string = null;
        int max_count = 0;

        try {
            while (true) {
                String s = reader.readLine();
                if (s == null)
                    break;

                int c = s.split(" ").length;
                if (c > max_count) {
                    max_count = c;
                    max_string = s;
                }
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return max_string;
    }
}
