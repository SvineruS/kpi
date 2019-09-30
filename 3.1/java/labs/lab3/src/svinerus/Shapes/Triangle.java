package svinerus.Shapes;

import svinerus.Shape;

public class Triangle extends Shape {
    double a;
    double b;
    double c;

    public Triangle(String shapeColor, double a, double b, double c) {
        super(shapeColor);
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public double calcArea() {
        double p = (a+b+c) / 2;
        return Math.sqrt(p*(p-a)*(p-b)*(p-c));
    }

    @Override
    public String toString() {
        return "Triangle{" +
                "shapeColor='" + shapeColor + '\'' +
                ", a=" + a +
                ", b=" + b +
                ", c=" + c +
                '}';
    }

    @Override
    public void draw() {

    }
}
