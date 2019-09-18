import com.google.gson.Gson;
import nl.jqno.equalsverifier.EqualsVerifier;

import static org.junit.jupiter.api.Assertions.*;

class Tests {

    @org.junit.jupiter.api.Test
    void testEquals() {
        EqualsVerifier.forClass(Person.class).verify();

    }


    @org.junit.jupiter.api.Test
    void testJson() {
        Gson gson = new Gson();

        Person person_input = new Person("Kek", 228);

        String json = gson.toJson(person_input);
        Person person_output = gson.fromJson(json, Person.class);

        assertTrue(person_input.equals(person_output));
        assertEquals(person_input, person_output);


    }
}