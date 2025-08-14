import os
import zipfile
import glob
from src.xml_parser import extract_patient_data


def find_v30_xml_files(zip_folder_path):
    """
    Loop through all zip files in the specified folder and extract XML files ending with 'v30'.

    Args:
        zip_folder_path (str): Path to the folder containing zip files

    Returns:
        list: List of tuples containing (xml_filename, xml_content)
    """
    xml_files = []

    # Get all zip files in the folder
    zip_pattern = os.path.join(zip_folder_path, "*.zip")
    zip_files = glob.glob(zip_pattern)

    print(f"Found {len(zip_files)} zip files to process...")

    for zip_path in zip_files:
        print(f"Processing: {os.path.basename(zip_path)}")

        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                # Get list of all files in the zip
                file_list = zip_ref.namelist()

                # Find XML files ending with 'v30'
                v30_xml_files = [f for f in file_list if f.lower().endswith("v30.xml")]

                for xml_file in v30_xml_files:
                    print(f"  Found XML file: {xml_file}")

                    # Read the XML content
                    with zip_ref.open(xml_file) as xml_content:
                        xml_data = xml_content.read().decode("utf-8")
                        xml_files.append((xml_file, xml_data))

        except zipfile.BadZipFile:
            print(f"Error: {zip_path} is not a valid zip file")
        except Exception as e:
            print(f"Error processing {zip_path}: {str(e)}")

    return xml_files


def process_extracted_xml_files(xml_files):
    """
    Process extracted XML files using the extract_patient_data function.

    Args:
        xml_files (list): List of tuples containing (xml_filename, xml_content)

    Returns:
        list: List of dictionaries containing extracted patient data
    """
    all_patient_data = []
    successful_count = 0
    error_count = 0

    print(f"\nProcessing {len(xml_files)} XML files...")

    for xml_filename, xml_content in xml_files:
        try:
            print(f"Processing: {xml_filename}")

            # Use the existing function to extract patient data
            patient_data = extract_patient_data(xml_content)

            # Add the source filename to the data
            patient_data["source_file"] = xml_filename

            all_patient_data.append(patient_data)
            successful_count += 1

            # Print extracted data for this file
            print(f"  ✓ Patient: {patient_data['patient']}")
            print(f"  ✓ Doctor: {patient_data['doctor']}")
            print(f"  ✓ Due Date: {patient_data['due_date']}")

        except Exception as e:
            print(f"  ✗ Error processing {xml_filename}: {str(e)}")
            error_count += 1

    print(f"\nProcessing Summary:")
    print(f"  Total files: {len(xml_files)}")
    print(f"  Successfully processed: {successful_count}")
    print(f"  Errors: {error_count}")

    return all_patient_data


def process_zip_folder(zip_folder_path):
    """
    Main function to handle the entire zip processing workflow.

    Args:
        zip_folder_path (str): Path to the folder containing zip files

    Returns:
        list: List of dictionaries containing all extracted patient data
    """
    # Check if the folder exists
    if not os.path.exists(zip_folder_path):
        raise FileNotFoundError(f"Folder '{zip_folder_path}' does not exist.")

    # Find and extract all v30 XML files
    print("Starting XML extraction process...")
    xml_files = find_v30_xml_files(zip_folder_path)

    if not xml_files:
        print("No XML files ending with 'v30' were found in the zip files.")
        return []

    print(f"\nExtracted {len(xml_files)} XML files ending with 'v30'")

    # Process the XML files
    all_patient_data = process_extracted_xml_files(xml_files)

    return all_patient_data
