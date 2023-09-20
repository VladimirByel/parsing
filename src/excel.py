import xlsxwriter


class Excel:

    @classmethod
    def excel(cls, data):
        # Workbook() takes one, non-optional, argument
        # which is the filename that we want to create.
        workbook = xlsxwriter.Workbook('vacancies.xlsx')

        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
        worksheet = workbook.add_worksheet()

        # Use the worksheet object to write
        # data via the write() method.
        excel_list = []
        for i in data['items'][0]:
            excel_list.append(i)
        print(excel_list)
        worksheet.write("A1", "10")

        workbook.close()
