A table called mobile is created with the following DDL command:

create table mobile (id int, brandname varchar(20), modelname varchar(20), price int);     


Write the Java code using JDBC APIs to select the id, brandname, modelname and price from the table mobile.

Note:
The order of the columns in the result set must be id, brandname, modelname and price. The result set must be ordered by the column brandname in ascending order.

IMPORTANT:
1. Place your code inside the execute method. You need not code/implement the main method.
2. DO NOT close the Database Connection conn in your code.
1 / 3



------------------------------solution-------------------------------
import java.sql.*;

public class MobileDataRetriever {
    
    public void execute(Connection conn) throws SQLException {
        String query = "SELECT id, brandname, modelname, price FROM mobile ORDER BY brandname ASC";
        
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        
        while (rs.next()) {
            int id = rs.getInt("id");
            String brandname = rs.getString("brandname");
            String modelname = rs.getString("modelname");
            int price = rs.getInt("price");
            
            // Process retrieved data here
        }
        
        rs.close();
        stmt.close();
    }
}

