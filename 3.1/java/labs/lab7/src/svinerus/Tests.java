package svinerus;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;
import static svinerus.Main.Task1;

class Tests {

    @org.junit.jupiter.api.Test
    void task1() {
        assertArrayEquals(Task1(new String[]{"1", "12", "123", "1234"}), new String[]{"123", "1234"});
    }
}