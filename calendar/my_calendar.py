import calendar as cld

# Hàm in lịch theo năm
def print_year_calendar(year=2025, width=2, lines=1, spacing=6, c=3):
    # Tạo đối tượng lịch
    cal = cld.TextCalendar()
    
    # In lịch theo năm
    print(cal.formatyear(year, width, lines, spacing, c))


# Hàm in lịch theo tháng
def print_month_calendar(year=2025, month=1, width=2, lines=1):
    # Tạo đối tượng lịch
    cal = cld.TextCalendar()
    
    # In lịch theo tháng
    print(cal.formatmonth(year, month, width, lines))


if __name__ == '__main__':
    while True:
        print('Chọn loại lịch:')
        print('1. Lịch năm')
        print('2. Lịch tháng')
        print('0. Thoát')

        choice = input('Nhập lựa chọn: ')

        if choice == '1':
            year = int(input('Nhập năm: '))
            print_year_calendar(year)
        elif choice == '2':
            year = int(input('Nhập năm: '))
            month = int(input('Nhập tháng: '))
            print_month_calendar(year, month)
        elif choice == '0':
            break
        else:
            print('Lựa chọn không hợp lệ.')
