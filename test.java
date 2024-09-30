public ResultSet doQuery(String username, String password) {
	String sql = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
	Statement stmt = conn.createStatement();
	ResultSet rs = stmt.executeQuery(sql);
	return rs;
}
