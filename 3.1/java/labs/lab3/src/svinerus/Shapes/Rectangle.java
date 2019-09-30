package svinerus.Shapes;

import svinerus.Shape;

public class Rectangle extends Shape {
    double a;
    double b;

    public Rectangle(String shapeColor, double a, double b) {
        super(shapeColor);
        this.a = a;
        this.b = b;
    }

    @Override
    public double calcArea() {
        return a*b;
    }

    @Override
    public String toString() {
        return "Rectangle{" +
                "shapeColor='" + shapeColor + '\'' +
                ", a=" + a +
                ", b=" + b +
                '}';
    }

    @Override
    public void draw() {

    }
}
