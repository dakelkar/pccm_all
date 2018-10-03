import modules.ask_y_n_statement as ask_y_n_statement
from sql.add_update_sql import review_df_row, view_multiple, delete_multiple, delete_rows
from modules.pccm_names import name_follow_up as names
import pandas as pd
from datetime import datetime
from reports.longterm_therapy import patient_status


def follow_up(file_number, user_name):
    follow = True
    follow_index = 0
    col_list = ["File_number"] + names()
    follow_up_data = pd.DataFrame(columns=col_list)
    while follow:
        check = False
        while not check:
            time_follow = ask_y_n_statement.ask_option("Follow-up Period", ["3 months", "6 months", "9 months",
                                                                            "1 year", "1 year, 3 months",
                                                                            "1 year, 6 months", "1 year, 9 months",
                                                                            "2 years", "2 years, 6 months", "3 years",
                                                                            "3 years, 6 months", "4 years",
                                                                            "4 years, 6 months", "5 years", "6 years",
                                                                            "7 years", "8 years", "9 years", "10 years",
                                                                            "Other"])
            follow_status = patient_status()
            follow_mammo, follow_mammo_date, follow_usg, follow_usg_date  = ("NA",)*4
            is_mammo = ask_y_n_statement.ask_y_n('Is follow up mammogramm present?')
            if is_mammo:
                follow_mammo_date = ask_y_n_statement.check_date('Date of follow-up Mammograph? ')
                follow_mammo = input("Results of Mammography (Please enter in the format (Observation(mass/calc/lesion "
                                     "etc)/Location/BIRADs)): ")
            is_usg = ask_y_n_statement.ask_y_n('Is follow up USG abdomen/Pelvis present?')
            if is_usg:
                follow_usg_date = ask_y_n_statement.check_date('Date of follow-up USG abdomen/Pelvis? ')
                follow_usg = input("Results of USG abdomen/Pelvis (Please enter in the format (Observation"
                                   "(mass/calc/lesion etc)/Location/BIRADs)): ")
            other_type_date, other_type, other_result = ("NA",) * 3
            follow_other = ask_y_n_statement.ask_y_n("Are there other reports in follow-up?")
            if follow_other:
                other_type_date_list = []
                other_type_list = []
                other_result_list = []
                while follow_other:
                    other_type_date = ask_y_n_statement.check_date('Date of other test: ')
                    other_type = input("Type of other report: ")
                    other_result = input("Result of "+other_type+": ")
                    other_type_date_list.append(other_type_date)
                    other_type_list.append(other_type)
                    other_result_list.append(other_result)
                    follow_other = ask_y_n_statement.ask_y_n("Add more reports?")
                all_data = [other_type_date_list, other_type_list, other_result_list]
                all_data = ask_y_n_statement.join_lists(all_data, "; ")
                other_type_date, other_type, other_result = all_data
            last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
            data_list = [file_number, time_follow, follow_status, follow_mammo_date, follow_mammo, follow_usg_date,
                         follow_usg, other_type_date,other_type, other_result, user_name, last_update]
            follow_up_data.loc[follow_index] = data_list
            check = review_df_row(follow_up_data)
        follow_index = follow_index + 1
        follow_up_period = list(follow_up_data.loc[:, "Follow_up_Period"])
        print("Follow up periods added: "+"; ".join(follow_up_period))
        follow = ask_y_n_statement.ask_y_n("Add another follow-up period?")
    return follow_up_data


def add_data(conn, file_number, user_name):
    data = follow_up(file_number, user_name)
    data.to_sql("Follow_up_Data", conn, index=False, if_exists="append")


def edit_data(conn, cursor, file_number, user_name):
    table = "Follow_up_Data"
    col_list = names()
    enter = view_multiple(conn, table, col_list, file_number)
    if enter == "Add data":
        data = follow_up(file_number, user_name)
        data.to_sql("Follow_up_Data", conn, index=False, if_exists="append")
    if enter == "Edit data":
        table = "Follow_up_Data"
        col_list = ["File_number"] + names()
        sql = ('SELECT ' + ", ".join(col_list[:-2]) + " FROM '" + table + "' WHERE File_number = '"+file_number+"'")
        df = pd.read_sql(sql, conn)
        sql.print_df(df)
        check_delete = False
        while not check_delete:
            check_delete, df = sql.edit_table(df, id_col='Follow_up_Period', df_col=names())
        delete_rows(cursor, table,"File_number", file_number)
        add_data(conn, file_number, user_name)
