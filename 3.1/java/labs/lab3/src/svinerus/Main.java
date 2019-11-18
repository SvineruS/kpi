package svinerus;

import svinerus.Shapes.Circle;
import svinerus.Shapes.Rectangle;
import svinerus.Shapes.Triangle;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        Shape[] shapes = createData();

        System.out.println("DATA: ");
        printData(shapes);


        double area = calcArea(shapes);
        System.out.println("\n\nAREA: " + area);

        sortByArea(shapes);
        System.out.println("\n\nDATA SORTED BY AREA: ");
        printData(shapes);

        sortByColor(shapes);
        System.out.println("\n\nDATA SORTED BY COLOR: ");
        printData(shapes);
    }

    static Shape[] createData() {
        Shape[] shapes = new Shape[12];
        Random rnd = new Random(System.currentTimeMillis());

        for (int i=0; i<4; i++) {
            shapes[i*3+0] = new Rectangle("color"+rnd.nextInt(10), rnd.nextInt(10), rnd.nextInt(10));
            int temp = rnd.nextInt(10);
            shapes[i*3+1] = new Triangle("color"+rnd.nextInt(10), 3*temp, 4*temp, 5*temp);
            shapes[i*3+2] = new Circle("color"+rnd.nextInt(10), rnd.nextInt(10));
        }
        return shapes;
    }

    static void printData(Shape[] shapes) {
        for (Shape shape : shapes)
            System.out.println(shape.toString());
    }

    static double calcArea(Shape[] shapes) {
        double area = 0;
        for (Shape shape : shapes)
            area += shape.calcArea();

        return area;
    }

    static void sortByArea(Shape[] shapes) {
        Comparator<Shape> comparator = Comparator.comparing(Shape::calcArea);
        Arrays.sort(shapes, comparator);
    }

    static void sortByColor(Shape[] shapes) {
        Comparator<Shape> comparator = Comparator.comparing(obj -> obj.shapeColor);
        Arrays.sort(shapes, comparator);
    }

}
