package svinerus;

import java.io.*;


class EncodingOutputStream extends FilterOutputStream {

    private final int key;

    public EncodingOutputStream(OutputStream outputStream, int key) {
        super(outputStream);
        this.key = key;
    }

    public void write(int b) throws IOException {
        super.write(b + key);
    }
}

class DecodingOutputStream extends FilterInputStream {

    private final int key;

    public DecodingOutputStream(InputStream inputStream, int key) {
        super(inputStream);
        this.key = key;

    }

    public int read() throws IOException {
        return super.read() - key;
    }
}

class EncodingWriter extends FilterWriter {

    private final int key;

    protected EncodingWriter(Writer writer, int key) {
        super(writer);
        this.key = key;

    }

    public void write(int b) throws IOException {
        super.write(b + key);
    }
}


class DecodingWriter extends FilterReader {

    private final int key;

    protected DecodingWriter(Reader reader, int key) {
        super(reader);
        this.key = key;

    }

    public int read() throws IOException {
        return super.read() - key;
    }
}

