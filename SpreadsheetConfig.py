import os  # {New}

import openpyxl  # {New}


class SpreadsheetConfig:  # {New}
    """Read the image source root from an Excel spreadsheet."""  # {New}

    def __init__(self, spreadsheet_path):  # {New}
        self.spreadsheet_path = spreadsheet_path  # {New}

    def get_pic_drive(self):  # {New}
        """Return the source root stored in cell C2."""  # {New}
        if not os.path.isfile(self.spreadsheet_path):  # {New}
            raise FileNotFoundError(  # {New}
                f"Source base spreadsheet not found: {self.spreadsheet_path}"  # {New}
            )  # {New}

        workbook = openpyxl.load_workbook(  # {New}
            filename=self.spreadsheet_path, read_only=True, data_only=True  # {New}
        )  # {New}
        try:  # {New}
            source_base = workbook.active["C2"].value  # {New}
        finally:  # {New}
            workbook.close()  # {New}

        if not isinstance(source_base, str) or not source_base.strip():  # {New}
            raise ValueError(  # {New}
                "Cell A1 in the source base spreadsheet must contain a path"  # {New}
            )  # {New}

        return os.path.normpath(source_base.strip())  # {New}
