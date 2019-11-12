package svinerus;

import org.junit.jupiter.api.Test;
import svinerus.Animal.Zebra;

import static org.junit.jupiter.api.Assertions.*;

class Tests {


    @Test
    void oneBigTestBecauseIamLazyPig() {
        Cage<Zebra> zebraCage = new Cage<>(1);


        // добавить когда есть место

        try {
            zebraCage.addAnimal(new Zebra());
        } catch (Cage.CageFullException e) {
            fail();
        }

        assertEquals(zebraCage.busyCount(), 1);

        // добавить когда нет места

        assertThrows(
                Cage.CageFullException.class,
                () -> {
                    zebraCage.addAnimal(new Zebra());
                }
        );

        assertEquals(zebraCage.busyCount(), 1);


        // убрать когда есть кого убирать

        try {
            zebraCage.removeAnimal(0);
        } catch (Cage.CageNotContainAnimal ignored) {
            fail();
        }

        assertEquals(zebraCage.busyCount(), 0);

        // убрать когда нет кого убирать

        assertThrows(
                Cage.CageNotContainAnimal.class,
                () -> {
                    zebraCage.removeAnimal(0);
                }
        );

//        compilation error
//        zebraCage.addAnimal(new Eagle());


    }
}