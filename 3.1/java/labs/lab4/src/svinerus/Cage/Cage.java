package svinerus.Cage;

import svinerus.Animal.Animal;

import java.util.ArrayList;

public class Cage {

    private int maxCount;
    private ArrayList<Animal> animals = new ArrayList<>();

    public int maxCount() {
        return maxCount;
    }

    public int busyCount() {
        return animals.size();
    }

    public void addAnimal(Animal animal) throws Exception {
        if (busyCount() > maxCount())
            throw new Exception("Cage is full");

        animals.add(animal);
    }

    public void removeAnimal(int index) throws Exception {
        if (busyCount() <= index)
            throw new Exception("Cage not contain animal " + index);

        animals.remove(index);
    }


}
