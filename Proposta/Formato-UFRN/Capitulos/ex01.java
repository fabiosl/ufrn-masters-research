package ufrn;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

class Util {
	static Random rand = new Random();
	static int[] array;

	public static int[] generateRandomNumbers(int startNumber, int endNumber,
			int size) {
		array = new int[size];
		for (int i = 0; i < size; i++) {
			array[i] = rand.nextInt((endNumber - startNumber) + 1)
					+ startNumber;

		}
		return array;
	}

}

class RunnableDemo implements Runnable {
	private Thread t;
	private String threadName;
	private int numberOfIds;

	static ArrayList<Long> executionArray = new ArrayList<Long>();

	static int idealThreshold = 1000; // 1 sec
	static int tolerableThreshold = 4000; // 4 sec
	static float max_rofr = 0.30f; // 30%

	static void addExecutionToArray(long executionTime) {
		synchronized (executionArray) {
			executionArray.add(executionTime);
		}
		
		checkSLAisBroken();
	}

	static void checkSLAisBroken() {
		ArrayList<Long> executionsAboveIdealTheshold = new ArrayList<Long>();
		synchronized (executionsAboveIdealTheshold) {
			for (Long executionTime : executionArray) {
				if (executionTime > idealThreshold) {
					executionsAboveIdealTheshold.add(executionTime);
				}
				if (executionTime > tolerableThreshold) {
					System.out.println("Execution time over tolerable Threshold");
					System.exit(1);

				}
			}
			if ((executionsAboveIdealTheshold.size() / executionArray.size()) > max_rofr
					&& executionArray.size() > 10) {
				System.out.println("ROFR Exceeded");
				System.exit(1);
			}
		}
		

	}

	RunnableDemo(String name, int numberOfIds) {
		this.threadName = name;
		this.numberOfIds = numberOfIds;
	}

	public void run() {
		try {
			host= "54.186.38.180"
			port=""
			schema=""
			user=""
			password=""
			Class.forName("com.mysql.jdbc.Driver");
			Connection con = DriverManager.getConnection(
					"jdbc:mysql://" + host + ":" + port + "/" + schema, user,
					password);

			Statement st = con.createStatement();
			String idList = Arrays
					.toString(Util.generateRandomNumbers(1, 3000000, numberOfIds))
					.replace("[", "(").replace("]", ")");
			String query = ("select * from post_all_pages_portugal_globo_pt where id in " + idList);

			long startTime = System.currentTimeMillis();
			ResultSet result = st.executeQuery(query);
			long estimatedTime = System.currentTimeMillis() - startTime;
			System.out.println((estimatedTime));
			addExecutionToArray(estimatedTime);
			con.close();
			
		} catch (ClassNotFoundException ex) {
			System.out.println("Driver not found");
		} catch (SQLException ex2) {
			ex2.printStackTrace();
		}
	}

	public void start() {
		if (t == null) {
			t = new Thread(this, threadName);
			t.start();

		}
	}

}

public class Ex01 {
	public static void main(String[] args) {
		int numExperiments = 10;
		int numberOfPostsToRetrieve = 100;
		for (int i = 0; i < numExperiments; i++) {
			for (int j = 0; j < numExperiments; j++) {
				RunnableDemo R1 = new RunnableDemo("Thread",
						numberOfPostsToRetrieve);
				R1.start();
				try {
					Thread.sleep(Util.generateRandomNumbers(30, 300, 1)[0]);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		

		

	}

}