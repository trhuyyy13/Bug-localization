import os

def count_java_files_recursive(folder_path):
    java_file_count = 0

    # Duyệt qua tất cả các thư mục và tệp con trong thư mục lớn
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.java'):
                java_file_count += 1

    return java_file_count

# Gọi hàm với đường dẫn thư mục của bạn
folder_path = './data/source files'
java_file_count = count_java_files_recursive(folder_path)
print(f"Tổng số file .java: {java_file_count}")
