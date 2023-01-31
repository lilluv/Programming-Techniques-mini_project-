# Chương trình mô phỏng dữ liệu cảm biến bụi PM2.5 đo nồng độ hạt bụi có kích thước < 2.5 microns trong không khí.
#     - Phạm vi đo: 0 ÷ 600 𝜇𝑔/𝑚ଷ
#     - Độ phân giải: 0.1 𝜇𝑔/𝑚ଷ

import argparse
import pandas as pd
import datetime
import random

def convert_sec2time(second):
    h = second//3600
    m = (second - h*3600)//60
    s = second - h*3600 - m*60
    return datetime.time(hour=h, minute=m, second=s)

def main():
    parser = argparse.ArgumentParser(
                    prog = 'Dust sim',
                    description = 'Chương trình nhập liệu'
                    )
    parser.add_argument('-n', '--num_sensors', type= int, default=1, help='number of sensors')
    parser.add_argument('-st', '--sampling', type= int, default=30, help='sampling time (s)') 
    parser.add_argument('-si', '--interval', type= int, default=24, help= 'simulation time (h)' ) 
    opt = parser.parse_args()
    output = [['id','time','values']]
    timestamp = datetime.datetime.now()
    last_hour = timestamp.hour
    si_time = last_hour if last_hour < opt.interval else opt.interval
    total_secs = si_time*3600
    inter = total_secs // opt.sampling
    run_time = 0
    for interval in range(inter):
        run_time+=opt.sampling
        log_time = datetime.datetime.combine(timestamp , convert_sec2time(run_time))
        for id in range(1,opt.num_sensors+1):
            value = round(random.random(),1)
            output.append([id, log_time, value])
    output = pd.DataFrame(output)
    pd.DataFrame.to_csv(output, "dust_sensor.csv", header= False, index= False )

if __name__=='__main__':
    main()
