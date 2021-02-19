The goal of the this test assignment is to do some basic Python and Django operations.

The main requirement is to import data via a user-uploaded csv or tsv file.

There are many ways you could spend extra time on this, but please follow the guidelines on what should be done and what should not be done at each stage.

Setup:
    Create or use a Python 3 environment of your choice
    Install Django
    Run migrate

Stage 1 is mandatory and you should do some portion of stage 2 before scheduling a technical interview.

Stage 1:
    Create a view and very simple html template with a form to upload a file. Please do not spend time on making the html look good at this stage.
    Assume the file is tab-separated.
    Allow the user to import good.tsv into the database, creating or updating Things and creating Items.
    If the import was not successful, display a generic error below the upload form.
    If the import was successful, display the created and updated records in two simple tables, one for each model, below the upload form.
    Do not display records that were already in the database and have not been updated.

Stage 2:
    Validate the data before creating any records.
    Inform the user of any errors.
    Besides the data formats and restrictions implied by the characteristics of the models' fields, apply the following restrictions:

    Thing:
        date:
            Should be a parsable date in YYYY-MM-DD (ISO format).
        stat_one:
            Should be one of the STAT_ONE_CHOICE_* literals
        stat_two:
            Should be one of the STAT_TWO_CHOICE_* literals
    Item:
        rating:
            Should be a string representation of a 5 star rating with two significant digits. I.e. '1.0' through '5.0'
        score:
            Should be an integer between 0 and 50, inclusive

    For any field, if the value is invalid but can be unambiguously transformed into a valid value, do so. E.g., you might accept dates in 'YYYY/MM/DD' format. Use your discretion in deciding how ambitious to be here.
    How and where in the code you accomplish the validation is completely up to you.

Stage 3:
    Anything you like that you have time for. Some options are, permitting other file delimiters such as commas, improving the error reporting, improving the result reporting, clever ways to clean up the data, etc.
