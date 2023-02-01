import pandas as pd
import argparse
import datetime
# task 2.4
def main(args):
    summary = [['id', 'pollution', 'duration']]
    #Read data
    df = pd.read_csv(args.path)
    sensors = list(set(df['id']))
    logs = {x: [] for x in sensors}
    for id, pol in zip(df['id'], df['pollution']):
        logs[id].append(pol)
    for sensor in sensors:
        pollution_list = ['Good', 'Moderate', 'Slightly unhealthy', 'Unhealthy', 'Very unhealthy ', 'Hazardous', 'Extremely hazardous']
        log_times = [0 for x in pollution_list]
        pollutions = logs[sensor]
        for pol in pollutions:
            idx = pollution_list.index(pol)
            log_times[idx] += 1 
        for pol, times in zip(pollution_list, log_times):
            summary.append([sensor, pol, times])
    # summary     
    summary = pd.DataFrame(summary)
    pd.DataFrame.to_csv(summary, "dust_statistics.csv", header= False, index= False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_aqi.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)