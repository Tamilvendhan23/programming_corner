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

    
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;
public class Hello {
    public static void execute(Connection conn, Scanner sc) {
        try{
            String SQL_query_string = "SELECT * FROM mobile ORDER BY brandname";            
             PreparedStatement prepared_statement = conn.prepareStatement(SQL_query_string);            
             ResultSet result_set = prepared_statement.executeQuery();  
            while(result_set.next()){
                System.out.println(result_set.getString(1) + " " + result_set.getString(2) + " " + result_set.getString(3) + " " + result_set.getString(4));
                                 }
        }catch(Exception exception){}
    }//end of execute method
}//end of Hello class

