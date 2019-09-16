package svinerus;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Task1Test {

    @Test
    void parse() {
        assertArrayEquals(Task1.parse(new String[] {"1", "12", "123", "1234"}), new String[] {"123", "1234"});

    }
}