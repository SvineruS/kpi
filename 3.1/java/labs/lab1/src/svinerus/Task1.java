package svinerus;

import java.util.ArrayList;
import java.util.List;

public class Task1 {


    public static String[] parse(String[] strings) {
        float avg_len = 0;
        List<String> output = new ArrayList<>();

        for (String s: strings) {
            avg_len += s.length();
        }
        avg_len /= strings.length;

        for (String s: strings) {
            if (s.length() > avg_len)
                output.add(s);
        }

        return output.toArray(new String[0]);
    }

}
