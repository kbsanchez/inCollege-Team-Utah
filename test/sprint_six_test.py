from .context import main_menu

SAMPLE_USER = "SampleUser"
SAMPLE_TITLE = "Sample Title"
SAMPLE_DESC = "Sample Description"
SAMPLE_EMPLOYER = "Sample Emp"
SAMPLE_LOCATION = "Sample Location"
SAMPLE_SALARY = 100000.00


#checks that all jobs have been printed
def jobs_print_test():
    rows = main_menu.number_job_rows()
    assert rows == len(main_menu.select_all_jobs())


#checks if a job was deleted
def job_deletion_test():
    main_menu.job_entry(SAMPLE_USER, SAMPLE_TITLE, SAMPLE_DESC, SAMPLE_EMPLOYER, SAMPLE_LOCATION, SAMPLE_SALARY)
    rowsBefore = main_menu.number_job_rows()
    main_menu.job_deletion(SAMPLE_USER, SAMPLE_TITLE, SAMPLE_DESC, SAMPLE_EMPLOYER,SAMPLE_LOCATION,SAMPLE_SALARY)
    rowsAfter = main_menu.number_job_rows()
    assert rowsAfter == (rowsBefore - 1)

    