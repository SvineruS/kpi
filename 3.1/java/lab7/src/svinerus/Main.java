package svinerus;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
    }

    public static String[] Task1(String[] strings) {
        final int avg_len = Arrays.stream(strings).mapToInt(String::length).sum() / strings.length;
        return Arrays.stream(strings).filter(s -> s.length() > avg_len).toArray(String[]::new);
    }

}
