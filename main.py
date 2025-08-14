# main.py

# Import the functions you need from the src module
from src.xml_parser import extract_from_file


def main():
    # Path to your XML file (adjust as needed; consider making this configurable via args or env vars)
    file_path = r"C:\Users\Partners\Downloads\test_itero_xml.xml"

    try:

        info_from_itero = extract_from_file(file_path)

        print("Extracted from file:")
        print(f"Patient: {info_from_itero['patient']}")
        print(f"Doctor: {info_from_itero['doctor']}")
        print(f"Due Date: {info_from_itero['due_date']}")

    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
