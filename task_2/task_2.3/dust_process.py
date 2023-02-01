import pandas as pd
import argparse
import datetime
# task 2.3
def main(args):
    summary = [['id', 'parameters', 'time', 'values']]
    #Read data
    df = pd.read_csv(args.path)
    sensors = list(set(df['id']))
    logs = {x: [] for x in sensors}
    for id, time, value in zip(df['id'], df['time'], df['values']):
        logs[id].append([value,time])
    for sensor in sensors:
        values = logs[sensor]
        max_value = 0
        time_max = 0
        min_value = 551 # >550.5 is outlier
        time_min = 0
        sum_val = 0 
        num_rec = 0
        for value in values:
            num_rec+=1
            sum_val+=value[0]
            if value[0] > max_value:
                max_value = value[0]
                time_max = value[1]
            if value[0] < min_value:
                min_value = value[0]
                time_min = value[1]
        mean_value = sum_val/num_rec
        record_time = values[-1][1]
        summary.append([sensor, 'max', time_max, max_value])
        summary.append([sensor, 'min', time_min, min_value])
        summary.append([sensor, 'mean', record_time, mean_value])
    # summary     
    summary = pd.DataFrame(summary)
    pd.DataFrame.to_csv(summary, "dust_summary.csv", header= False, index= False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_sensor.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)