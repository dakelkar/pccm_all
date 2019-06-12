import modules.ask_y_n_statement as ask
import sql.add_update_sql as sql
import modules.pccm_names as names
import pandas as pd


class BlockInformation:

    def __init__(self, conn, cursor, file_number):
        self.file_number = file_number
        self.cursor = cursor
        self.conn = conn
        self.table_name = 'block_list'

    def get_block_id(self, col_filter_value):
        block_columns = ['file_number'] + names.block_list('all')
        block_list = sql.extract_multiple_value_select_column(self.conn, block_columns, table=self.table_name,
                                                              file_number=self.file_number, col_select='block_id',
                                                              col_filter='block_type',
                                                              col_filter_value=col_filter_value)
        block_id = ask.ask_list(str(col_filter_value) + ' block id information is to be entered for: ', block_list+
                                ['not available', 'Other'])
        block_list = ask.nested_list(block_list)
        if block_id not in set(block_list):
            number_of_blocks = 'not available'
        else:
            number_of_blocks = sql.get_value(col_name='number_of_blocks', table='block_list', pk_name='file_number',
                                             pk=self.file_number, cursor=self.cursor, error_statement="Enter number of "
                                                                                                      "blocks: ")
        return str(block_id), str(number_of_blocks)

    def get_block_pk (self, user_name, col_filter_value):
        from reports.ffpe_db import NewBlock
        new_block = NewBlock(self.conn, self.cursor, user_name)
        block_columns = ['file_number'] + names.block_list('all')
        block_list = sql.extract_multiple_value_select_column(self.conn, block_columns, table=self.table_name,
                                                              file_number=self.file_number, col_select='block_id',
                                                              col_filter='block_type',
                                                              col_filter_value=col_filter_value)
        block_id = ask.ask_list(str(col_filter_value) + ' block id information is to be entered for: ', block_list +
                                ['not available', 'Other'])
        block_list = ask.nested_list(block_list)
        if block_id not in set(block_list):
            new_block.add_new_pk(self.file_number, block_id=block_id)
            pk, number_of_blocks = self.get_block_information(block_id, block_data= ['pk', 'number_of_blocks'])
        else:
            sql_statement = ("SELECT pk FROM block_list WHERE (block_id = '" + block_id + "')")
            self.cursor.execute(sql_statement)
            pk_ = self.cursor.fetchall()
            pk = pk_[0][0]
            number_of_blocks = sql.get_value(col_name='number_of_blocks', table='block_list', pk_name='pk', pk=pk,
                                             cursor=self.cursor, error_statement="Enter number of blocks: ")
        return pk, str(block_id), number_of_blocks

    def get_block_information(self, block_id, block_data):
        if block_id == 'not available':
            search_col = 'file_number'
            search_val = self.file_number
        else:
            search_col = 'block_id'
            search_val = block_id
        sql_statement = ("SELECT DISTINCT " + ', '.join(block_data) + " FROM block_list WHERE " + search_col + "= '"
                         + search_val + "'")
        df = pd.read_sql(sql_statement, self.conn)
        block_details = []
        for col in block_data:
            block_detail = list(pd.unique(df[col].values))
            if len(block_detail) > 1:
                detail = ask.ask_list('Please choose the correct ' + col + ': ', block_detail + ['not available'])
                block_detail = detail
            block_details.append(block_detail)
        return ask.nested_list(block_details)


