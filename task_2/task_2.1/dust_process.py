import pandas as pd
import argparse
# task 2.1
## Ignore Outlier
def main(args):
    min_value = 5
    max_value =550.5
    outlier_data = [['id','time','values']]
    clean_data = [['id','time','values']]
    n_outlier = 0
    #Read data
    df = pd.read_csv(args.path)
    for id, time, values in zip(df['id'], df['time'], df['values']):
        if values>max_value or values<min_value:
            n_outlier +=1
            outlier_data.append([id, time, values])
        else:
            clean_data.append([id, time, values])
            
    print('number of outliers: ', n_outlier) 
    outlier_data = pd.DataFrame(outlier_data)
    pd.DataFrame.to_csv(outlier_data, "dust_outlier.csv", header= False, index= False )

    clean_data = pd.DataFrame(clean_data)
    pd.DataFrame.to_csv(clean_data, args.path, header= False, index= False )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process.')
    parser.add_argument('--path', '-p', type=str, nargs='+', default= "dust_sensor.csv",
                        help='path to csv file')
    args = parser.parse_args()
    main(args)