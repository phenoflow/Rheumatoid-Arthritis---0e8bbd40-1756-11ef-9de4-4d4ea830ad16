# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N040.00","system":"readv2"},{"code":"14G1.00","system":"readv2"},{"code":"107112.0","system":"readv2"},{"code":"43816.0","system":"readv2"},{"code":"9954.0","system":"readv2"},{"code":"12019.0","system":"readv2"},{"code":"71784.0","system":"readv2"},{"code":"49227.0","system":"readv2"},{"code":"33264.0","system":"readv2"},{"code":"8350.0","system":"readv2"},{"code":"49067.0","system":"readv2"},{"code":"48832.0","system":"readv2"},{"code":"31209.0","system":"readv2"},{"code":"56232.0","system":"readv2"},{"code":"99414.0","system":"readv2"},{"code":"36678.0","system":"readv2"},{"code":"50863.0","system":"readv2"},{"code":"56202.0","system":"readv2"},{"code":"844.0","system":"readv2"},{"code":"63198.0","system":"readv2"},{"code":"44203.0","system":"readv2"},{"code":"70221.0","system":"readv2"},{"code":"46436.0","system":"readv2"},{"code":"107963.0","system":"readv2"},{"code":"63365.0","system":"readv2"},{"code":"49787.0","system":"readv2"},{"code":"18155.0","system":"readv2"},{"code":"93715.0","system":"readv2"},{"code":"37431.0","system":"readv2"},{"code":"51239.0","system":"readv2"},{"code":"44743.0","system":"readv2"},{"code":"21635.0","system":"readv2"},{"code":"23552.0","system":"readv2"},{"code":"5723.0","system":"readv2"},{"code":"100776.0","system":"readv2"},{"code":"31054.0","system":"readv2"},{"code":"70658.0","system":"readv2"},{"code":"31724.0","system":"readv2"},{"code":"27603.0","system":"readv2"},{"code":"30548.0","system":"readv2"},{"code":"59738.0","system":"readv2"},{"code":"107791.0","system":"readv2"},{"code":"6916.0","system":"readv2"},{"code":"42299.0","system":"readv2"},{"code":"21358.0","system":"readv2"},{"code":"62401.0","system":"readv2"},{"code":"28853.0","system":"readv2"},{"code":"41941.0","system":"readv2"},{"code":"56838.0","system":"readv2"},{"code":"106440.0","system":"readv2"},{"code":"23834.0","system":"readv2"},{"code":"53621.0","system":"readv2"},{"code":"9707.0","system":"readv2"},{"code":"32001.0","system":"readv2"},{"code":"73619.0","system":"readv2"},{"code":"51238.0","system":"readv2"},{"code":"100914.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatoid-arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["arthritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["arthritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["arthritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
