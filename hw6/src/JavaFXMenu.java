import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

import java.sql.Connection;
import java.sql.DriverManager;

import java.sql.*;


public class JavaFXMenu extends Application{


    private class MenuItem{
        int item_id;
        double price;
        String name;
        String picture;

        MenuItem(double price, String name, String picture){
            this.price = price;
            this.name = name;
            this.picture = picture;
        }

        MenuItem(){};

        void setItem_id(int item_id){
            this.item_id = item_id;
        }
        void setPrice(double price){
            this.price = price;
        }
        void setName(String name){
            this.name = name;
        }
    }
    private Statement stmt;


    private Label title = new Label("Happy Restaurant");
    private TextField menuItem1In = new TextField("" + 0);
    private TextField menuItem2In = new TextField("" + 0);
    private TextField menuItem3In = new TextField("" + 0);

    Button orderBT = new Button("Place Order");

    MenuItem item1 = new MenuItem();
    MenuItem item2 = new MenuItem();
    MenuItem item3 = new MenuItem();


    int orderCounter = 0;

    @Override
    public void start(Stage primaryStage){
        initializeDB();
        updateMenu();

        title.setFont(new Font("Arial", 32));

        //Create labels for each item
        Label menuItem1Label = new Label("" + item1.name + "$ " + item1.price);
        Label menuItem2Label = new Label("" + item2.name + "$ " + item2.price);
        Label menuItem3Label = new Label("" + item3.name + "$ " + item3.price);

        //Image dailySpecialImage = new Image(s1.picture);

        Image item1Image = new Image("/images/1.jpg", 100, 100, false, false);
        Image item2Image = new Image("/images/2.jpg", 100, 100, false, false);
        Image item3Image = new Image("/images/3.jpg", 100, 100, false, false);

        GridPane gridPane = new GridPane();
        gridPane.setVgap(5);
        gridPane.setHgap(5);
        gridPane.add(title, 1, 0);
        gridPane.add(menuItem1In,0, 1);
        gridPane.add(menuItem1Label, 1, 1);
        gridPane.add(new ImageView(item1Image), 2, 1);
        gridPane.add(menuItem2In, 0, 2);
        gridPane.add(menuItem2Label, 1, 2);
        gridPane.add(new ImageView(item2Image), 2, 2);
        gridPane.add(menuItem3In, 0, 3);
        gridPane.add(menuItem3Label, 1, 3);
        gridPane.add(new ImageView(item3Image), 2, 3);
        gridPane.add(orderBT, 0, 4);

        //handler for button
        orderBT.setOnAction(e -> {
            try {
                orderSummary();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
        });



        //set properties for ui
        Scene scene = new Scene(gridPane);
        gridPane.setAlignment(Pos.CENTER);
        primaryStage.setTitle("Menu");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void initializeDB() {
        try {
            // Connect to the local InterBase database

            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection
                    ("jdbc:mysql://localhost/restaurant?serverTimezone=UTC", "root", "password");
            System.out.println("Database connected\n");

            System.out.println("Database connected");

            // Create a statement
            stmt = conn.createStatement();
        }
        catch (Exception ex) {
            System.out.println("Connection failed: " + ex);
        }
    }
    private void updateMenu() {
        // Build a SQL SELECT statement
        String query = "SELECT * FROM menu WHERE item_id = 1";

        try {
            // Execute query
            ResultSet rs = stmt.executeQuery(query);
            loadToMenu(rs, item1);
        }
        catch(SQLException ex) {
            System.out.println("Select 1 failed: " + ex);
        }

        query = "SELECT * FROM menu WHERE item_id = 2";

        try {
            // Execute query
            ResultSet rs = stmt.executeQuery(query);
            loadToMenu(rs, item2);
        }
        catch(SQLException ex) {
            System.out.println("Select 2 failed: " + ex);
        }

        query = "SELECT * FROM menu WHERE item_id = 3";

        try {
            // Execute query
            ResultSet rs = stmt.executeQuery(query);
            loadToMenu(rs, item3);
        }
        catch(SQLException ex) {
            System.out.println("Select 3 failed: " + ex);
        }

    }

    private void loadToMenu(ResultSet rs, MenuItem item) throws SQLException{
        if(rs.next()){
            item.setItem_id((rs.getInt(1)));
            item.setName(rs.getString(2));
            item.setPrice(rs.getDouble(3));
        }
    }



    private void orderSummary() throws SQLException{

            orderCounter++;



            int item1Order = Integer.parseInt(menuItem1In.getText());
            int item2Order = Integer.parseInt(menuItem2In.getText());
            int item3Order = Integer.parseInt(menuItem3In.getText());

            stmt.executeUpdate("insert into orders (item1_qty, item2_qty, item3_qty) values("
                    + item1Order +","+ item2Order +","+ item3Order +");");

            double total = ((item1Order * item1.price) + (item2Order * item2.price) +
                    (item3Order * item3.price));

            Stage stage2 = new Stage();
            stage2.setTitle("Order Summery");
            Pane pane = new Pane();

            pane.setPadding(new Insets(10, 10, 10, 10));
            if(item1Order > 0) {
                Text text1 = new Text(5, 80, String.format("%d %s", item1Order, item1.name));
                pane.getChildren().add(text1);
            }
            if(item2Order > 0) {
                Text text2 = new Text(5, 140, String.format("%d %s", item2Order, item2.name));
                pane.getChildren().add(text2);
            }
            if(item3Order > 0) {
                Text text3 = new Text(5, 200, String.format("%d %s", item3Order, item3.name));
                pane.getChildren().add(text3);
            }

            Text text4=new Text(5, 260, String.format("TOTAL: $%.2f", total));
            pane.getChildren().add(text4);


            Scene scene2 = new Scene(pane, 260, 400);
            stage2.setScene(scene2);
            stage2.show();

    }

}
