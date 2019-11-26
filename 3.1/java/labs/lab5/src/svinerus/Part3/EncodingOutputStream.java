package svinerus.Part3;

import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class EncodingOutputStream extends FilterOutputStream {

    private final int key;

    public EncodingOutputStream(OutputStream outputStream, int key) {
        super(outputStream);
        this.key = key;
    }

    public void write(int b) throws IOException {
        super.write(b + key);
    }
}
