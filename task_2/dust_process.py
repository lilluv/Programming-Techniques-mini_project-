import pandas as pd
import argparse

def main(args):
    concentration = [12,35.5,55.5,150.5,250.5,350.5,550.5]
    aqi_list = [50,100,150,200,300,400,500]
    pollution_list = ['Good', 'Moderate', 'Slightly unhealthy', 'Unhealthy', 'Very unhealthy ', 'Hazardous', 'Extremely hazardous']

    min_value = 5
    max_value =550.5
    outlier_data = [['id','time','values']] #task2.1
    processed_data = [['id','time','values','aqi','pollution']] #task2.2
    summary = [['id', 'parameters', 'time', 'values']]  #task2.3
    statistics = [['id', 'pollution', 'duration']]  #task2.4

    #Read data
    df = pd.read_csv(args.path)
    sensors = list(set(df['id']))
    logs = {x: [] for x in sensors}
    
    ## Ignore Outlier
    n_outlier = 0
    for id, time, value in zip(df['id'], df['time'], df['values']):
        if value>max_value or value<min_value:
            n_outlier +=1
            outlier_data.append([id, time, value])
        else:
            pred = 0
            pred_aqi = 0
            
            for idx, V in enumerate(concentration):
                if value < V:
                    aqi = round((value - pred)/(V - pred)*(aqi_list[idx]-pred_aqi)+pred_aqi)
                    pollution = pollution_list[idx]
                    logs[id].append([value,time,pollution])
                    break
                else:
                    pred = V
                    pred_aqi = aqi_list[idx]
            processed_data.append([id, time, value,aqi,pollution])   
    print('number of outliers: ', n_outlier) 
    outlier_data = pd.DataFrame(outlier_data)
    pd.DataFrame.to_csv(outlier_data, "dust_outlier.csv", header= False, index= False)         
    processed_data = pd.DataFrame(processed_data)
    pd.DataFrame.to_csv(processed_data, "dust_aqi.csv", header= False, index= False)        

    for sensor in sensors:
        #Init val
        values = logs[sensor]
        max_value = 0
        time_max = 0
        min_value = 551 # >550.5 is outlier
        time_min = 0
        sum_val = 0 
        num_rec = 0
        log_times = [0 for x in pollution_list]

        for value in values:
            num_rec+=1
            sum_val+=value[0]
            if value[0] > max_value:
                max_value = value[0]
                time_max = value[1]
            if value[0] < min_value:
                min_value = value[0]
                time_min = value[1]
            idx = pollution_list.index(value[2])
            log_times[idx] += 1 
        # Task 2.3
        mean_value = sum_val/num_rec
        record_time = values[-1][1]
        summary.append([sensor, 'max', time_max, max_value])
        summary.append([sensor, 'min', time_min, min_value])
        summary.append([sensor, 'mean', record_time, mean_value])
        # Task 2.4          
        for pol, times in zip(pollution_list, log_times):
            statistics.append([sensor, pol, times])
    # summary     
    summary = pd.DataFrame(summary)
    pd.DataFrame.to_csv(summary, "dust_summary.csv", header= False, index= False)
    statistics = pd.DataFrame(statistics)
    pd.DataFrame.to_csv(statistics, "dust_statistics.csv", header= False, index= False)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_sensor.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)