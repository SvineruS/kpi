package svinerus;

import java.io.*;

public class Serializer {
    static void Save(Shape[] shapes, String filename) throws IOException {
        FileOutputStream f = new FileOutputStream(filename);
        ObjectOutputStream s = new ObjectOutputStream(f);
        s.writeObject(shapes);
        s.close();
    }

    static Shape[] Load(String filename) throws IOException, ClassNotFoundException {
        FileInputStream f = new FileInputStream(filename);
        ObjectInputStream s = new ObjectInputStream(f);
        Shape[] shapes = (Shape[]) s.readObject();
        s.close();
        return shapes;
    }

}
