# main.py

from src.zip_handler import process_zip_folder

def main():
    """
    Main function to orchestrate the zip file processing workflow.
    """
    # Configure the folder containing your zip files
    zip_folder = "data"  # Change this to your zip files folder path
    
    try:
        # Process all zip files and extract patient data
        all_patient_data = process_zip_folder(zip_folder)
        
        if all_patient_data:
            print(f"\n{'='*60}")
            print("FINAL RESULTS - All Extracted Patient Data:")
            print(f"{'='*60}")
            
            for i, data in enumerate(all_patient_data, 1):
                print(f"\nRecord {i} (from {data['source_file']}):")
                print(f"  Patient: {data['patient']}")
                print(f"  Doctor: {data['doctor']}")
                print(f"  Due Date: {data['due_date']}")
            
            # You can now use all_patient_data for further processing
            # For example, save to CSV, database, etc.
            print(f"\nTotal records extracted: {len(all_patient_data)}")
            
        else:
            print("No patient data was successfully extracted.")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please create the folder and add your zip files, or update the zip_folder path in main().")
    except ImportError as e:
        print(f"Import Error: {e}")
        print("Please check that all required modules exist in the src folder.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()