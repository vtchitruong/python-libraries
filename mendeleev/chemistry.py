import mendeleev as mdl

# Hàm lấy thông tin nguyên tố bằng ký hiệu hoặc tên nguyên tố
def get_by_symbol(symbol):
    try:
        e = mdl.element(symbol)

        print(f'- Tên nguyên tố: {e.name}')
        print(f'- Ký hiệu hoá học: {e.symbol}')
        print(f'- Số hiệu nguyên tử: {e.atomic_number}')
        print(f'- Khối lượng nguyên tử: {e.atomic_weight:.2f} u')
        print(f'- Cấu hình electron: {e.econf}')
        print(f'- Nhóm: {e.group_id}')
        print(f'- Chu kỳ: {e.period}')
        
    except Exception as e:
        print(f'Lỗi: {e}')


# Hàm lấy thông tin nguyên tố bằng số hiệu nguyên tử
def get_by_number(number):
    try:
        e = mdl.element(number)

        print(f'- Tên nguyên tố: {e.name}')
        print(f'- Ký hiệu hoá học: {e.symbol}')
        print(f'- Số hiệu nguyên tử: {e.atomic_number}')
        print(f'- Khối lượng nguyên tử: {e.atomic_weight:.2f} u')
        print(f'- Cấu hình electron: {e.econf}')
        print(f'- Nhóm: {e.group_id}')
        print(f'- Chu kỳ: {e.period}')
        
    except Exception as e:
        print(f'Lỗi: {e}')


# Hàm in ra các nguyên tố cùng nhóm
def get_by_group(group):
    if group < 1 or group > 18:
        print('Không có nhóm này')
    else:
        print(f'Các nguyên tố thuộc nhóm {group}:')

        # Lấy tất cả nguyên tố
        all_elements = mdl.get_all_elements()

        try:
            # Duyệt từng nguyên tố
            for e in all_elements:
                if e.group_id == group:
                    print(f'{e.name} ({e.symbol})')
                    print(f'- Số hiệu: {e.atomic_number}')
                    print(f'- Nguyên tử khối: {e.atomic_weight}')
        except Exception as e:
            print(f'Lỗi: {e}')


if __name__ == '__main__':
    while True:
        print('\nChọn một chức năng:')
        print('1. Tìm nguyên tố theo ký hiệu hoặc tên')
        print('2. Tìm nguyên tố theo số hiệu nguyên tử')
        print('3. Liệt kê các nguyên tố cùng nhóm')
        print('0. Thoát')

        choice = input('Nhập lựa chọn: ')

        if choice == '1':
            user_input = input('Nhập ký hiệu hoặc tên nguyên tố: ').strip()
            get_by_symbol(user_input)
        elif choice == '2':
            user_input = int(input('Nhập số hiệu nguyên tử của nguyên tố: '))
            get_by_number(user_input)
        elif choice == '3':
            user_input = int(input('Nhập nhóm: '))
            get_by_group(user_input)
        elif choice == '0':
            break
        else:
            print('Lựa chọn không hợp lệ.')
