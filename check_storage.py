import requests
import json

# Cấu hình thông tin ứng dụng E5 Developer
TENANT_ID = 'qfkb.onmicrosoft.com'
# Thay access_token bằng token lấy từ Azure AD (nếu chạy thật)
ACCESS_TOKEN = 'nhap_token_cua_anh_vao_day'

def check_onedrive_quota():
    """
    Hàm gọi Microsoft Graph API để lấy thông tin dung lượng OneDrive
    Được viết cho mục đích backup dữ liệu thiết kế từ Mac Mini.
    """
    url = 'https://graph.microsoft.com/v1.0/me/drive'
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    print(f"Đang kết nối đến tenant: {TENANT_ID}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        quota = data.get('quota', {})
        
        # Chuyển đổi byte sang GB
        total_gb = quota.get('total', 0) / (1024**3)
        used_gb = quota.get('used', 0) / (1024**3)
        remaining_gb = quota.get('remaining', 0) / (1024**3)
        
        print(f"--- Báo cáo dung lượng OneDrive ---")
        print(f"Tổng dung lượng: {total_gb:.2f} GB")
        print(f"Đã sử dụng: {used_gb:.2f} GB")
        print(f"Còn trống: {remaining_gb:.2f} GB")
        print(f"Trạng thái tài khoản: {quota.get('state', 'Unknown')}")
    else:
        print(f"Lỗi kết nối API. Mã lỗi: {response.status_code}")
        print("Vui lòng kiểm tra lại token xác thực OIDC.")

if __name__ == '__main__':
    check_onedrive_quota()
