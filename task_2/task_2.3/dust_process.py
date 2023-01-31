import pandas as pd
import argparse
# task 2.3
def main(args):
    summary = [['id', 'parameters', 'time', 'values']]
    #Read data
    df = pd.read_csv(args.path)
    sensors = list(set(df['id']))
    log = {x: [] for x in sensors}
    for id, time, value in zip(df['id'], df['time'], df['values']):
        log[id].append(value)
    for sensor in sensors:
        values = log[sensor]
        min_value = min(values)
        max_value = max(values)
        mean_value = sum(values)/len(values)
        summary.append([sensor, 'max', 'none', max_value])
        summary.append([sensor, 'min', 'none', min_value])
        summary.append([sensor, 'mean', 'none', mean_value])
    # summary     
    summary = pd.DataFrame(summary)
    pd.DataFrame.to_csv(summary, "dust_summary.csv", header= False, index= False )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_sensor.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)