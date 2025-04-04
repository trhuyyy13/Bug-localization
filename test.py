import os

def delete_non_java_files_recursive(folder_path):
    # Duyệt qua tất cả các thư mục và tệp con trong thư mục lớn
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # Kiểm tra nếu không phải là file .java, thì xoá
            if not filename.endswith('.java'):
                os.remove(file_path)
                print(f"Đã xoá: {file_path}")

# Gọi hàm với đường dẫn thư mục của bạn
folder_path = './data/source files'
delete_non_java_files_recursive(folder_path)
