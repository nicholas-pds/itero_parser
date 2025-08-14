import xml.etree.ElementTree as ET


def extract_patient_data(xml_content):
    """
    Extract patient, doctor, and due date from iTero XML export

    Args:
        xml_content (str): XML content as string

    Returns:
        dict: Dictionary containing extracted data
    """
    try:
        # Parse the XML content
        root = ET.fromstring(xml_content)

        # Find the RxInfo section
        rx_info = root.find("RxInfo")

        if rx_info is None:
            raise ValueError("RxInfo section not found in XML")

        # Extract the required fields
        patient = rx_info.find("Patient")
        doctor = rx_info.find("Doctor")
        due_date = rx_info.find("DueDate")

        # Create result dictionary
        result = {
            "patient": patient.text if patient is not None else None,
            "doctor": doctor.text if doctor is not None else None,
            "due_date": due_date.text if due_date is not None else None,
        }

        return result

    except ET.ParseError as e:
        raise ValueError(f"Invalid XML format: {e}")
    except Exception as e:
        raise ValueError(f"Error processing XML: {e}")


def extract_from_file(file_path):
    """
    Extract patient data from XML file

    Args:
        file_path (str): Path to XML file

    Returns:
        dict: Dictionary containing extracted data
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            xml_content = file.read()
        return extract_patient_data(xml_content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")


# Reading from a local file
if __name__ == "__main__":
    # Specify the path to your XML file
    file_path = r"C:\Users\Partners\Downloads\test_itero_xml.xml"

    try:
        # Extract data from the XML file
        data = extract_from_file(file_path)

        # Print the extracted information
        print("Extracted Information:")
        print(f"Patient: {data['patient']}")
        print(f"Doctor: {data['doctor']}")
        print(f"Due Date: {data['due_date']}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Please make sure the file path is correct and the file exists.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Alternative: You can also use it with different file paths
    # other_files = ["file1.xml", "file2.xml", "file3.xml"]
    # for file_path in other_files:
    #     try:
    #         data = extract_from_file(file_path)
    #         print(f"\nFile: {file_path}")
    #         print(f"Patient: {data['patient']}, Doctor: {data['doctor']}, Due Date: {data['due_date']}")
    #     except Exception as e:
    #         print(f"Error with {file_path}: {e}")
