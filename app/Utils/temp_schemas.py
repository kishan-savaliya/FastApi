from datetime import date

class TempSchema(object):
    created_at : date
    updated_at : date
    is_active : bool
    is_delete : bool
