package calc;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CalcTest {
    @Test
    void add_test() {
        int actual = new Calc().Add(1, 2);
        assertEquals(3, actual);
    }
}