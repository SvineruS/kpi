package svinerus;

import svinerus.Part3.DecodingReader;
import svinerus.Part3.EncodingWriter;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

class Tests {

    @org.junit.jupiter.api.Test
    void part1() {
        try {
            assertEquals(Part1.Main("part1_test.txt"), "1 2 3");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    @org.junit.jupiter.api.Test
    void part3() {
        try {
            String in = "test123";
            int key = 1;

            new EncodingWriter(new FileWriter("part3_test"), key).write(in);

            String out = new Scanner(new DecodingReader(new FileReader("part3_test"), key)).nextLine();

            assertEquals(in, out);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }





}