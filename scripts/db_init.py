#!/usr/bin/env python3

import shutil
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, db
from recipe import initRecipe

def backup_database(db_uri, backup_uri):
    if backup_uri:
        db_path = db_uri.replace('sqlite:///', 'instance/')
        backup_path = backup_uri.replace('sqlite:///', 'instance/')
        shutil.copyfile(db_path, backup_path)
        print(f"Database backed up to {backup_path}")
    else:
        print("Backup not supported for production database.")

def main():
    with app.app_context():
        try:
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            
            if tables:
                print("Warning, you are about to lose all data in the database!")
                print("Do you want to continue? (y/n)")
                response = input()
                if response.lower() != 'y':
                    print("Exiting without making changes.")
                    sys.exit(0)
                    
            backup_database(app.config['SQLALCHEMY_DATABASE_URI'], app.config['SQLALCHEMY_BACKUP_URI'])
           
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
        
    try:
        with app.app_context():
            db.drop_all()
            print("All tables dropped.")
            initRecipe()
                        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
    print("Database initialized!")
 
if __name__ == "__main__":
    main()