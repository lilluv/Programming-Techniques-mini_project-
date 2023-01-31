import pandas as pd
import argparse
# task 2.2
def main(args):
    concentration = [12,35.5,55.5,150.5,250.5,350.5,550.5]
    aqi_list = [50,100,150,200,300,400,500]
    pollution_list = ['Good', 'Moderate', 'Slightly unhealthy', 'Unhealthy', 'Very unhealthy ', 'Hazardous', 'Extremely hazardous']
    processed_data = [['id','time','values','aqi','pollution']]

    #Read data
    df = pd.read_csv(args.path)
    for id, time, values in zip(df['id'], df['time'], df['values']):
        pred = 0
        pred_aqi = 0
        for idx, V in enumerate(concentration):
            if values < V:
                aqi = round((values - pred)/(V - pred)*(aqi_list[idx]-pred_aqi)+pred_aqi)
                pollution = pollution_list[idx]
                break
            else:
                pred = V
                pred_aqi = aqi_list[idx]
        processed_data.append([id, time, values,aqi,pollution])   
            
    processed_data = pd.DataFrame(processed_data)
    pd.DataFrame.to_csv(processed_data, "dust_aqi.csv", header= False, index= False )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_sensor.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)