#include<map>
#include<string>
#include<vector>
#include<iostream>
#include<ctime>
#include <fstream>
// #include<cmath>

using namespace std;

float round(float var)
{
    // 37.66666 * 10 =376.666
    // 376.666 + .5 =377.166    for rounding off value
    // then type cast to int so value is 377
    // then divided by 100 so the value converted into 37.7
    float value = (int)(var * 10 + .5);
    return (float)value / 10;
}

bool is_number(string s)
{
    // Tất cả các tham số đều nguyên dương nên không cần check số âm. Nếu âm là giá trị không hợp lệ
    for(auto x: s) if(!isdigit(x)) return false;
    return true;
}

void write_csv(std::string filename, std::vector<std::pair<std::string, std::vector<int>>> dataset){
    // Make a CSV file with one or more columns of integer values
    // Each column of data is represented by the pair <column name, column data>
    //   as std::pair<std::string, std::vector<int>>
    // The dataset is represented as a vector of these columns
    // Note that all columns should be the same size
    
    // Create an output filestream object
    std::ofstream myFile(filename);
    
    // Send column names to the stream
    for(int j = 0; j < dataset.size(); ++j)
    {
        myFile << dataset.at(j).first;
        if(j != dataset.size() - 1) myFile << ","; // No comma at end of line
    }
    myFile << "\n";
    
    // Send data to the stream
    for(int i = 0; i < dataset.at(0).second.size(); ++i)
    {
        for(int j = 0; j < dataset.size(); ++j)
        {
            myFile << dataset.at(j).second.at(i);
            if(j != dataset.size() - 1) myFile << ","; // No comma at end of line
        }
        myFile << "\n";
    }
    
    // Close the file
    myFile.close();
}

int main(int argc, char* argv[])
{
    // Ta thấy số arg luôn là số lẻ => sẽ sinh lỗi
    if(argc % 2 == 0)
    {
        // sinh lỗi
    }

    int n = 1;
    int st = 30;
    int si = 24;

    // Parse
    for(int i = 0; i < argc; ++i)
    {
        string arg(argv[i]);
        if(arg == "-n" || arg == "-st" || arg == "-si")
        {
            if(i+1 >= argc)
            {
                cout << "Biến đầu vào cho tham số " + arg + " không hợp lệ. " + arg + " cần theo sau là 1 số nguyên dương trong khoảng ...";
            }
            else if (!is_number(string(argv[i+1])))
            {
                cout << "Biến đầu vào cho tham số " + arg + " không hợp lệ. " + arg + " cần theo sau là 1 số nguyên dương trong khoảng ...";
            }
            else
            {
                if(arg == "-n") n = stoi(string(argv[i+1]));
                if(arg == "-st") st = stoi(string(argv[i+1]));
                if(arg == "-si") si = stoi(string(argv[i+1]));
            }

        }   

    }
    // Process
    // output = [['id','time','values']];
    // fstream fout;
    std::ofstream fout("dust_sensor.csv");
    time_t timestamp = time(0);
    tm *ltm = localtime(&timestamp);
    int year =  1900 + ltm->tm_year;
    int last_hour = 5+ltm->tm_hour;
    int si_time;
    if (last_hour < si){
        si_time = last_hour ;
    }
    else{
        si_time = si;
    } 

    int si_time = si;
    int total_secs = si_time*3600;
    int inter = total_secs / st;
    int run_time = 0;
    for (size_t i = 0; i < inter; i++)
    {
        run_time+= st;
        // tm logtime;
        int log_time = 1;
        for (size_t id = 0; i < n; i++)
        {
            double value = round(((double)rand()) / RAND_MAX*1000);
            std::vector<std::pair<std::string, std::vector<int>>> vals = {{"id", id}, {"time", log_time}, {"values", value}};
            write_csv("dust_sensor.csv", vals);
        }
    
    }
    
}

// -n [num_sensors] là cặp tham số đầu vào để cung cấp số lượng cảm biến, [num_sensors]cần được thay thế bởi một số cụ thể. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy số lượng cảm biến mặc định là 1.
// -st [sampling] là cặp tham số để cung cấp thời gian trích mẫu với [sampling]cần được thay thế bởi một số nguyên dương với đơn vị là giây, thời gian trích mẫu nhỏ nhất cho phép là 1 giây. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy tần số trích mẫu mặc định là 30 giây.
// -si [interval] là cặp tham số để cung cấp khoảng thời gian đo với [interval]cần được thay thế bởi một số nguyên dương đơn vị là giờ, khoảng thời gian mô phỏng nhỏ nhất là 1 giờ. Chương trình cần đưa ra thông báo lỗi nếu chỉ một trong 2 tham số này xuất hiện. Nếu cả 2 thông số này không xuất hiện trong câu lệnh command-line thì chương trình sẽ lấy tần số trích mẫu mặc định là 24 giờ.