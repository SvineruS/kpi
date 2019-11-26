package svinerus.Part3;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;

public class DecodingInputStream extends FilterInputStream {

    private final int key;

    public DecodingInputStream(InputStream inputStream, int key) {
        super(inputStream);
        this.key = key;

    }

    public int read() throws IOException {
        return super.read() - key;
    }
}
