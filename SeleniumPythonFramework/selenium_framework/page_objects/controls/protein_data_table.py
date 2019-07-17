from selenium.webdriver.remote.webelement import WebElement

class ProteinDataTable:
    def __init__(self, table : WebElement ):
        self.__table = table

    def get_table_contents(self, byText):
        cell_list = list()
        all_rows = list(self.__table.find_element_by_tag_name("tr"))
        for row in all_rows:
            cells = list(row.find_element_by_tag_name("td"))
            for cell in cells:
                cell_list.append(cell.Text)
        return cell_list

            




                