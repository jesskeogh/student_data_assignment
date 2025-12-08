#
# def get_number_of_As(df):
#     return len(df[df["grade"] >= 70])
#
# #get number of As from sql (grade >= 70)
# def get_number_of_As_sql(conn):
#     cur = conn.cursor()
#     return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade >= 70").fetchone()[0]