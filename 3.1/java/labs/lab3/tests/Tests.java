import org.junit.jupiter.api.Test;
import svinerus.Shapes.Circle;
import svinerus.Shapes.Rectangle;
import svinerus.Shapes.Triangle;

import static org.junit.jupiter.api.Assertions.*;

class Tests {

    @Test
    void RectangleCalcArea() {
        assertEquals(new Rectangle("green", 2, 3).calcArea(), 6);
    }

    @Test
    void TriangleCalcArea() {
        assertEquals(new Triangle("green", 3, 4, 5).calcArea(), 6);
    }

    @Test
    void CircleCalcArea() {
        assertEquals(new Circle("green", 2).calcArea(), 4*Math.PI);
    }
}