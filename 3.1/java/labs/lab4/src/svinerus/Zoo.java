package svinerus;

import java.util.ArrayList;
import java.util.List;

public class Zoo {

    public List<Cage> cages = new ArrayList<>();


    public int getCountOfAnimals() {
        int sum = 0;
        for (Cage c: cages) {
            sum += c.busyCount();
        }
        return sum;
    }

    public void addCage(Cage cage) {
        cages.add(cage);
    }
}
