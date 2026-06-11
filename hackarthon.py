staffs = [
    {"id":"NV001",
    "name":"Nguyen Van A",
    "wage":400000,
    "day":25,
    "allowance":1500000,
    "total_income":11500000,
    "income_classification":"Khá"
    }
]

def validate_input(prompt: str, input_type: str = "string"):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("[Lỗi]: Dữ liệu không được để trống! Vui lòng nhập lại.")
            continue
        
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 0:
                    print("[Lỗi]: Số liệu không được âm!")
                    continue
                return value
            except ValueError:
                print("[Lỗi]: Phải nhập vào một số nguyên hợp lệ!")
                continue
                
        if input_type == "match":
            try:
                value = int(user_input)
                if value < 0 or value > 50:
                    print("[Lỗi]: Dữ liệu phải nằm trong khoảng từ 0 đến 50!")
                    continue
                return value
            except ValueError:
                print("[Lỗi]: Phải nhập vào một số nguyên hợp lệ!")
                continue
        return user_input

def display_staff(data_list):
    if not data_list:
        print("\n[Thông báo]: Danh sách hiện tại đang rỗng!")
        return
    print("\n" + "=" * 137)
    print(f"{'ID':<10} | {'Tên nhân viên':<20} | {'Lương ngày cơ bản(VND)':<25} | {'Ngày công làm việc':<20} | {'Tiền phụ cấp':<15} | {'Tổng thu nhập':<15} | {'Phân loại thu nhập':<10}")
    print("-" * 137)
    for item in data_list:
        print(f"{item.get('id').upper():<10} | {item.get('name'):<20} | {item.get('wage'):<25} | {item.get('day'):<20} | {item.get('allowance'):<15} | {item.get('total_income'):<15} | {item.get('income_classification'):<10}")
    print("=" * 137)
    
def add_staff(data_list):
    print("\n--- TIẾP NHẬN NHÂN VIÊN MỚI ---")
    while True:
        search_id = validate_input("Nhập mã ID định danh: ")
        for item in data_list:
            if search_id.lower() == item.get("id").lower():
                print("[Lỗi]: Mã ID này đã tồn tại! Vui lòng nhập lại.")
                break
        else:
            name = validate_input("Nhập tên nhân viên mới: ")
            wage = validate_input("Nhập lương: ", "int")
            day = validate_input("Nhập số ngày công: ", "int")
            allowance = validate_input("Nhập tiền phụ cấp: ", "int")
            total_income = (wage*day)+allowance
            income_classification=""
            if total_income > 30000000:
                income_classification="Cao"
            elif total_income>= 15000000 and total_income < 30000000:
                income_classification="Khá"
            elif total_income>= 9000000 and total_income < 15000000:
                income_classification ="Trung bình"
            else:
                income_classification="Thấp"
                
            new_staff = {
                "id": search_id,
                "name": name,
                "wage": wage,
                "day": day,
                "allowance": allowance,
                "total_income":total_income,
                "income_classification":income_classification                
            }
            data_list.append(new_staff)
            print("[Thành công]: Đã thêm nhân viên mới vào hệ thống!")
            break
        
def update_staff(data_list):
    print("\n--- CẬP NHẬT THÔNG TIN VÀ NGÀY CÔNG ---")
    if not data_list:
        print("[Thông báo]: Danh sách rỗng!")
        return
    search_id = validate_input("Nhập mã ID cần chỉnh sửa: ")
    for item in data_list:
        if search_id.lower() == item.get("id").lower():
            print(f"Tìm thấy nhân viên: {item.get('name')} | Lương: {item.get('wage')}")
            wage = validate_input("Nhập lương: ", "int")
            day = validate_input("Nhập số ngày công: ", "int")
            allowance = validate_input("Nhập tiền phụ cấp: ", "int")
            total_income = (wage*day)+allowance
            income_classification=""
            if total_income > 30000000:
                income_classification="Cao"
            elif total_income>= 15000000 and total_income < 30000000:
                income_classification="Khá"
            elif total_income>= 9000000 and total_income < 15000000:
                income_classification ="Trung bình"
            else:
                income_classification="Thấp"
            item['wage']= wage
            item['day']=day
            item['allowance']=allowance
            item['total_income']=total_income
            item['income_classification']=income_classification
            

            print("[Thành công]: Đã cập nhật trạng thái sang ĐÃ XỬ LÝ!")
            break
    else:
        print("[Lỗi]: Không tìm thấy mã ID yêu cầu!")
def remove_staff(data_list):
    print("\n--- XÓA ĐỐI TƯỢNG KHỎI HỆ THỐNG ---")
    if not data_list:
        print("[Thông báo]: Danh sách rỗng!")
        return
    search_id = validate_input("Nhập mã ID cần xóa: ")
    for item in data_list:
        if search_id.lower() == item.get("id").lower():
            check=validate_input("Bạn có chắc chắn muốn xóa nhân viên này không?(Y/N): ").strip
            if check== 'Y' or check =='y':
                data_list.remove(item)
                print(f"[Thành công]: Đã xóa dữ liệu liên quan đến ID {search_id}!")
                break
            elif check == 'N' or check== 'n' :
                print("Bạn dừng chức năng xóa thành công!")
                break
            else:
                print("Lựa chọn sai!")
                continue
                
    else:
        print("[Lỗi]: Không tìm thấy mã ID yêu cầu để xóa!")
    
def search_item(data_list):
    print("\n--- TÌM KIẾM THÔNG TIN (MÃ HOẶC TÊN) ---")
    if not data_list:
        print("[Thông báo]: Danh sách rỗng!")
        return
    keyword = validate_input("Nhập từ khóa cần tìm (Mã hoặc Tên): ")
    results = []
    for item in data_list:
        if keyword.lower() == item.get("id").lower() or keyword.lower() in item.get("name").lower():
            results.append(item)
    if not results:
        print("[Thông báo]: Không tìm thấy kết quả nào phù hợp!")
    else:
        display_staff(results)
        
def chart_item(data_list):
    print("\n--- PHÂN LOẠI THU NHẬP TỰ ĐỘNG ---")
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    for item in data_list:
        income_classification = item.get("income_classification")
        if  income_classification == "Thấp": count_a += 1
        elif income_classification == "Trung Bình": count_b += 1
        elif income_classification == "Khá": count_c += 1
        elif income_classification == "Cao": count_d += 1
    print(f"Số lượng thuộc Loại Thấp: {count_a}")
    print(f"Số lượng thuộc Loại Trung Bình: {count_b}")
    print(f"Số lượng thuộc Loại Khá: {count_c}")
    print(f"Số lượng thuộc Loại Cao: {count_d}")


def main():
    while True:
        print(" DANH SÁCH CHỨC NĂNG ".center(50,"="))
        print("1.Hiển thị danh sách nhân viên")
        print("2.Tiếp nhận nhân viên mới")
        print("3.Cập nhật thông tin và ngày công")
        print("4.Xóa nhân viên")
        print("5.Tìm kiếm nhân viên")
        print("6.Thống kê quỹ lương và nhân sự")
        print("7.Phân loại thu nhập tự động")
        print("8.Thoát chương trình")
        print("="*50)
        choice = input("Vui lòng nhập chức năng (1-8): ")
        match choice:
            case '1':
                display_staff(staffs)
            case '2':
                add_staff(staffs)
            case '3':
                update_staff(staffs)
            case '4':
                remove_staff(staffs)
            case '5':
                search_item(staffs)
            case '7':
                chart_item(staffs)
            case '8':
                print("Bạn đã thoát chương trình")
            case _:
                print("Lựa chọn không hợp lệ vui lòng nhập lại!")
                



if __name__ == "__main__":
    main()