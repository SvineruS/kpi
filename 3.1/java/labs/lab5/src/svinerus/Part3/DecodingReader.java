package svinerus.Part3;

import java.io.FilterReader;
import java.io.IOException;
import java.io.Reader;

public class DecodingReader extends FilterReader {

    private final int key;

    public DecodingReader(Reader reader, int key) {
        super(reader);
        this.key = key;

    }

    public int read() throws IOException {
        return super.read() - key;
    }
}
