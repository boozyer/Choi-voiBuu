import os

def batch_rename_sequence(directory, prefix="Render_Octane_"):
    try:
        # Lọc các file ảnh render phổ biến
        files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.exr', '.tiff'))]
        files.sort()
        
        for index, filename in enumerate(files):
            extension = os.path.splitext(filename)[1]
            # Đánh số thứ tự 4 chữ số (ví dụ: Render_Octane_0001.exr)
            new_name = f"{prefix}{str(index + 1).zfill(4)}{extension}"
            
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            os.rename(old_file, new_file)
            print(f"Đã đổi: {filename} -> {new_name}")
            
        print("Xong! Đã xử lý toàn bộ sequence.")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    # Đường dẫn giả định tới thư mục chứa ảnh render
    folder_path = "./renders_output"
    # batch_rename_sequence(folder_path)
