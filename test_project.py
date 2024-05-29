import project as proj
def main():
    test_validate_task()
    test_insert_into_table()
    test_update_table()

def test_validate_task():
    assert proj.validate_task(1) == True
    assert proj.validate_task(2) == True
    assert proj.validate_task(3) == True
    assert proj.validate_task(4) == True
    assert proj.validate_task(5) == True
    assert proj.validate_task(6) == False
    assert proj.validate_task(10) == False

def test_insert_into_table():
    db = proj.connect_database()
    assert proj.insert_into_table(db,"Creating tests","01/01/2023 23:28:30") == "\nTask added successfully!!!"
    assert proj.insert_into_table(db,"Created test successfully","01/01/2023 23:30:00") == "\nTask added successfully!!!"
    proj.close_connection(db)

def test_update_table():
    db = proj.connect_database()
    assert proj.update_table(db,1,"Updating the test task","01/01/2023 23:32:00") == "\nTask updated successfully"
    assert proj.update_table(db,1,"checking the test task updation","01/01/2023 23:33:30") == "\nTask updated successfully"
    proj.close_connection(db)

if __name__ == "__main__":
    main()



