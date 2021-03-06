import pm25_simpletest

def main():
        f = open("AirQuality_09FEB2021.log", "a+")
        for i in range(2):
                f.write("--------- %d\r\n" % (i+1) + pm25_simpletest)
        f.close()

if __name__=="__main__":
    main()
