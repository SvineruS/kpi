package svinerus.Part3;

import java.io.*;


public class EncodingWriter extends FilterWriter {

    private final int key;

    public EncodingWriter(Writer writer, int key) {
        super(writer);
        this.key = key;

    }

    public void write(int b) throws IOException {
        super.write(b + key);
    }
}


