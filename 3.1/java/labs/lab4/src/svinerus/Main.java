package svinerus;

import svinerus.Animal.Eagle;
import svinerus.Animal.Giraffe;
import svinerus.Animal.Lion;

public class Main {

    public static void main(String[] args) throws Exception {
	    Zoo zoo = new Zoo();

	    Cage<Eagle> eagleCage = new Cage<>(2);
        eagleCage.addAnimal(new Eagle());

	    zoo.addCage(eagleCage);
	    zoo.addCage(new Cage<Lion>(1));
	    zoo.addCage(new Cage<Giraffe>(1));

	    System.out.println("Тварин в зоопарку: " + zoo.getCountOfAnimals());
	    System.out.println("Тварин в клiтцi для орлiв: " + eagleCage.busyCount() + "/" + eagleCage.maxCount());
    }
}
