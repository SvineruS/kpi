package svinerus;

import svinerus.Animal.Animal;

import java.util.ArrayList;

public class Cage<T extends Animal> {
    public Cage(int maxCount) {
        this.maxCount = maxCount;
    }

    private int maxCount;
    private ArrayList<T> animals = new ArrayList<>();

    public int maxCount() {
        return maxCount;
    }

    public int busyCount() {
        return animals.size();
    }

    public void addAnimal(T animal) throws CageFullException {
        if (busyCount()+1 > maxCount())
            throw new CageFullException("Cage is full");

        animals.add(animal);
    }

    public void removeAnimal(int index) throws CageNotContainAnimal {
        if (busyCount() <= index)
            throw new CageNotContainAnimal("Cage not contain animal " + index);

        animals.remove(index);
    }


    public static class CageException extends Exception{}
    public static class CageFullException extends CageException {
        CageFullException(String s) {
            super();
        }
    }
    public static class CageNotContainAnimal extends CageException {
        CageNotContainAnimal(String s) {
            super();
        }
    }


}
