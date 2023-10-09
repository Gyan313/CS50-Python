file_name = input("Enter the file name: ")

ext = file_name.split(".")

match (ext[1]):
    case "gif" | "jpg" | "jpeg" | "png":
        print(f"image/{ext[1]}")

    case "pdf" | "txt" | "zip":
        print(f"document/{ext[1]}")

    case _:
        print("application/octet-stream")
