import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.text.Font;
import java.time.LocalDate;
import java.util.HashMap;
import java.time.DayOfWeek;
import java.util.*;


public class JavaFXMenu extends Application{
    private class MenuItem{
        double price;
        String name;
        String picture;

        MenuItem(double price, String name, String picture){
            this.price = price;
            this.name = name;
            this.picture = picture;
        }
    }

    LocalDate currentDate = LocalDate.now();
    DayOfWeek day = currentDate.getDayOfWeek();

    HashMap<Integer, MenuItem> regularMenu = new HashMap<Integer, MenuItem>();
    HashMap<Integer, MenuItem> specialMenu = new HashMap<Integer, MenuItem>();

    //create special menu items
    MenuItem s1 = new MenuItem(6.99, "Spring Rolls", "/images/springroll.jpg");
    MenuItem s2 = new MenuItem(4.99, "Steamed Dumplings", "/images/steamed_dumplings.jpg");
    MenuItem s3 = new MenuItem(7.99, "Chicken Wings", "/images/chicken_wings.jpg");
    MenuItem s4 = new MenuItem(4.99, "Fried Dumplings", "/images/fried_dumplings.jpg");
    MenuItem s5 = new MenuItem(6.99, "Crab Rangoon", "/images/crab_rangoon.jpg");
    MenuItem s6 = new MenuItem(11.99, "Calamari", "/images/calamari.jpg");
    MenuItem s7 = new MenuItem(3.99, "Rice Soup", "/images/rice_soup.jpg");

    //create regular menu items
    MenuItem r1 = new MenuItem(13.99, "Pork Noodles", "/images/pork_noodles.jpg");
    MenuItem r2 = new MenuItem(12.99, "Chicken Fried Rice", "/images/fried_rice.jpg");
    MenuItem r3 = new MenuItem(9.99, "Creme Brulee", "/images/creme_brulee.jpg");


    private Label title = new Label("Happy Restaurant");
    private TextField dailySpecialIn = new TextField();
    private TextField menuItem1In = new TextField();
    private TextField menuItem2In = new TextField();
    private TextField menuItem3In = new TextField();

    Button orderBT = new Button("Place Order");



    @Override
    public void start(Stage primaryStage){
        //assign special menu items to a hash map
        specialMenu.put(1, s1);
        specialMenu.put(2,s2);
        specialMenu.put(3, s3);
        specialMenu.put(4, s4);
        specialMenu.put(5, s5);
        specialMenu.put(6,s6);
        specialMenu.put(7, s7);
        //assign regular menu items to a hashmap
        regularMenu.put(1, r1);
        regularMenu.put(2, r2);
        regularMenu.put(3, r3);



        //Create labels for each item
        Label dailySpecialLabel = new Label(String.format("%s $%.2f",specialMenu.get(day.getValue()).name, specialMenu.get(day.getValue()).price));
        Label menuItem1Label = new Label(String.format("%s $%.2f",regularMenu.get(1).name, regularMenu.get(1).price));
        Label menuItem2Label = new Label(String.format("%s $%.2f",regularMenu.get(2).name, regularMenu.get(2).price));
        Label menuItem3Label = new Label(String.format("%s $%.2f",regularMenu.get(3).name, regularMenu.get(3).price));

        //Create images for each item
        Image dailySpecialImage = new Image(specialMenu.get(day.getValue()).picture, 100, 100, false, false);
        //Image dailySpecialImage = new Image(s1.picture);
        Image item1Image = new Image(regularMenu.get(1).picture, 100, 100, false, false);
        Image item2Image = new Image(regularMenu.get(2).picture, 100, 100, false, false);
        Image item3Image = new Image(regularMenu.get(3).picture, 100, 100, false, false);

        GridPane gridPane = new GridPane();
        gridPane.setVgap(5);
        gridPane.setHgap(5);
        gridPane.add(title, 0, 0);
        gridPane.add(dailySpecialIn, 0, 1);
        gridPane.add(dailySpecialLabel, 1, 1);
        gridPane.add(new ImageView(dailySpecialImage), 2, 1);
        gridPane.add(menuItem1In,0, 2);
        gridPane.add(menuItem1Label, 1, 2);
        gridPane.add(new ImageView(item1Image), 2, 2);
        gridPane.add(menuItem2In, 0, 3);
        gridPane.add(menuItem2Label, 1, 3);
        gridPane.add(new ImageView(item2Image), 2, 3);
        gridPane.add(menuItem3In, 0, 4);
        gridPane.add(menuItem3Label, 1, 4);
        gridPane.add(new ImageView(item3Image), 2, 4);
        gridPane.add(orderBT, 0, 5);

        //handler for button

        orderBT.setOnAction(e -> orderSummary());


        //set properties for ui
        Scene scene = new Scene(gridPane);
        gridPane.setAlignment(Pos.CENTER);
        primaryStage.setTitle("Menu");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void orderSummary(){

            int specialOrder = Integer.parseInt(dailySpecialIn.getText());
            int item1Order = Integer.parseInt(menuItem1In.getText());
            int item2Order = Integer.parseInt(menuItem2In.getText());
            int item3Order = Integer.parseInt(menuItem3In.getText());

            double total = (specialOrder * specialMenu.get(day.getValue()).price) + (item1Order * regularMenu.get(1).price) +
                    (item2Order * regularMenu.get(2).price) + (item3Order * regularMenu.get(3).price);

            Stage stage2 = new Stage();
            stage2.setTitle("Order Summery");
            Pane pane = new Pane();

            pane.setPadding(new Insets(10, 10, 10, 10));
            Text newText1=new Text(5, 20, String.format("%d Daily Special", specialOrder));
            Text newText2=new Text(5, 80, String.format("%d %s", item1Order, regularMenu.get(1).name));
            Text newText3=new Text(5, 140, String.format("%d %s", item2Order, regularMenu.get(2).name));
            Text newText4=new Text(5, 200, String.format("%d %s", item3Order, regularMenu.get(3).name));
            Text newText5=new Text(5, 260, String.format("TOTAL: $%.2f", total));
            pane.getChildren().addAll(newText1, newText2, newText3, newText4, newText5);


            Scene scene2 = new Scene(pane, 260, 100);
            stage2.setScene(scene2);
            stage2.show();

    }

}
