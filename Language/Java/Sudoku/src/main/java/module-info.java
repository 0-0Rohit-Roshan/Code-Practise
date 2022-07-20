module com.ro.sudoku {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.ro.sudoku to javafx.fxml;
    exports com.ro.sudoku;
}