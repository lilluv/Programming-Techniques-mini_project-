# Task 1
Chương trình cho phép người dùng cung cấp số lượng cảm biến, tần số trích mẫu và khoảng thời gian đo bằng cách gõ lệnh trên command-line với cấu trúc câu lệnh như sau: 

```
dust_sim –n [num_sensors] –st [sampling] –si [interval] 
```
## Input
- -n [num_sensors] là cặp tham số đầu vào để cung cấp số lượng cảm biến, 
[num_sensors]cần được thay thế bởi một số cụ thể. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy số lượng cảm biến mặc định là 1. 
- -st [sampling] là cặp tham số để cung cấp thời gian trích mẫu với [sampling]cần được thay thế bởi một số nguyên dương với đơn vị là giây, thời gian trích mẫu nhỏ nhất cho phép là 1 giây. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy tần số trích mẫu mặc định là 30 giây. 
- -si [interval] là cặp tham số để cung cấp khoảng thời gian đo với [interval]cần được thay thế bởi một số nguyên dương đơn vị là giờ, khoảng thời gian mô phỏng nhỏ nhất là 1 giờ. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy tần số trích mẫu mặc định là 24 giờ. 

## Output
Chương trình sẽ xuất ra một tập dữ liệu bao gồm định danh của cảm biến (sensor id), thời điểm đo (timestamp) mô phỏng và giá trị cảm biến mô phỏng (values), với thời điểm bắt đầu mô phỏng là thời 
điểm hiện tại lấy từ giờ của hệ thống (giờ trong máy tính) trừ đi khoảng khoảng thời gian mô phỏng. 
- Số định danh (id) của cảm biến là các số từ 1 đến num_sensors với num_sensors là 
số lượng cảm biến mà người dùng cung cấp trong câu lệnh command-line, ví dụ 
num_sensors = 10 thì chương trình sẽ tạo ra 10 cảm biến có id là 1, 2, 3, …, 10. 
- Thời điểm đo (mô phỏng) có định dạng là YYYY:MM:DD hh:mm:ss, trong đó:
    - YY – năm, MM – tháng , DD – ngày. 
    - hh – giờ, mm – phút, ss – giây. 

    Ví dụ: 2022:12:01 08:30:02 
- Giá trị đo mô phỏng được tạo ra ngẫu nhiên là một số thực, với độ chính xác là 1 chữ số 
sau dấu phẩy. 

Chú ý: thời gian mô phỏng không phải là thời gian thực mà là thời gian mô phỏng tính toán do đó, sinh viên không dùng hàm tạo trễ như sleep() hoặc các vòng lặp tạo trễ. 

Dữ liệu mô phỏng xuất ra sẽ được lưu vào một file có tên là “dust_sensor.csv”, nếu file đã tồn tại thì ghi đè lên file cũ.

# Task 2
Chương trình xử lý dữ liệu trong một file csv có định dạng như ở task 1. Chương trình 
phải được chạy bằng câu lệnh command-line như dưới đây.  
```
C:\\dust_process [data_filename.csv] 
```
Trong đó:
- dust_process: là file chương trình đã biên dịch 
- [data_filename.csv] là file csv chứa dữ liệu cảm biến bụi. Nếu người dùng không cung cấp tên file thì mà chỉ gõ C:\\dust_process thì chương trình sẽ sử dụng tên file mặc định là “dust_sensor.csv”. 

Ví dụ: C:\\dust_process dust_sensor_ee3491.csv 
 Chương trình phải có khả năng xử lý được ít nhất 10000 điểm dữ liệu, tức là file đầu vào data_filename.csv có thể chứa ít nhất 10000 dòng. 
 