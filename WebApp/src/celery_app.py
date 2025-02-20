from celery import Celery
import os

# Configure Celery
celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


# Celery task to process the file
@celery_app.task
def process_file(file_path):
    """
    # d vpnosint_apk_to_file_db
                                            Table "public.vpnosint_apk_to_file_db"
           Column       |            Type             | Collation | Nullable |                       Default
    --------------------+-----------------------------+-----------+----------+-----------------------------------------------------
     id                 | integer                     |           | not null | nextval('vpnosint_apk_to_file_db_id_seq'::regclass)
     apk_id             | integer                     |           |          |
     file_name          | character varying(255)      |           |          |
     file_sha256        | character varying(255)      |           |          |
     file_type          | character varying(255)      |           |          |
     file_extension     | character varying(255)      |           |          |
     file_timestamp     | timestamp without time zone |           |          |
     file_last_modified | timestamp without time zone |           |          |
    Indexes:
        "vpnosint_apk_to_file_db_pkey" PRIMARY KEY, btree (id)
    Foreign-key constraints:
        "vpnosint_apk_to_file_db_apk_id_fkey" FOREIGN KEY (apk_id) REFERENCES vpnosint_vpn_apk_db(id) ON DELETE CASCADE

    1. Get a reference to the company for which the App is associated.


    d vpnosint_vpn_apk_db;
                                             Table "public.vpnosint_vpn_apk_db"
           Column        |            Type             | Collation | Nullable |                     Default
    ---------------------+-----------------------------+-----------+----------+-------------------------------------------------
     id                  | integer                     |           | not null | nextval('vpnosint_vpn_apk_db_id_seq'::regclass)
     apk_name            | character varying(255)      |           | not null |
     apk_sha256          | integer                     |           |          |
     apk_version         | character varying(255)      |           |          |
     apk_added_timestamp | timestamp without time zone |           |          |
     apk_last_modified   | timestamp without time zone |           |          |
    Indexes:
        "vpnosint_vpn_apk_db_pkey" PRIMARY KEY, btree (id)
    Referenced by:
        TABLE "vpnosint_apk_to_file_db" CONSTRAINT "vpnosint_apk_to_file_db_apk_id_fkey" FOREIGN KEY (apk_id) REFERENCES vpnosint_vpn_apk_db(id) ON DELETE CASCADE
        TABLE "vpnosint_apk_to_function_db" CONSTRAINT "vpnosint_apk_to_function_db_apk_id_fkey" FOREIGN KEY (apk_id) REFERENCES vpnosint_vpn_apk_db(id) ON DELETE CASCADE


    """
    # Simulate file processing (replace with your actual processing logic)
    # Example: Count the number of lines in the file
    print(f"process_file. 1 - file_path={file_path}")
    with open(file_path, 'rb') as f:
        line_count = sum([1 for _ in f])
    print(f"process_file. 2 - line_count={line_count}")

    # Clean up the file after processing
    os.remove(file_path)

    return line_count
