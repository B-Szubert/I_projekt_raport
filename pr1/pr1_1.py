import click

@click.command()
@click.argument('input_file')
@click.option('--output_file', '-o')
def main(input_file, output_file=''):

    if not output_file:
        output_file=input_file[:input_file.rfind('/')+1] + "duplicates_report.csv"
        
    print("")
    print("opening file " + input_file + "for reading")
    #print("opening file /home/zgm/Pulpit/Bogusia/marked_dup_metrics_N.txt for reading")
    with open(input_file) as f:
        start_reading = False
        read_lines_counter = 0
        for line in f.readlines():
            if line.startswith("## METRICS CLASS"):
                start_reading = True
            if start_reading and read_lines_counter <= 2:
                if read_lines_counter == 1:
                    klucz = line.replace('\n', '').split('\t')

                if read_lines_counter == 2:
                    wartosc = line.replace('\n', '').split('\t')
                read_lines_counter = read_lines_counter + 1

    print("")

    slownik = {}
    for i in range(0, len(klucz), 1):
        slownik[klucz[i]] = wartosc[i]
        print(klucz[i], wartosc[i])

    print("")

    print("selecting data to be saved")
    ilo=int(slownik['READ_PAIR_DUPLICATES'])+int(slownik['UNPAIRED_READ_DUPLICATES'])
    proc=float(slownik['PERCENT_DUPLICATION'].replace(',','.'))
    proc=round(proc*100, 4)

    print("")

    print("writing report to ")
    pli=open(output_file, 'a')
    pli.write("report from " + input_file + "file,\n")
    pli.write("Number of duplicates, ")
    pli.write(str(ilo))
    pli.write(",\n")
    pli.write("Percentage of duplicates,")
    pli.write(str(proc))
    pli.write(",\n")
    pli.close()

    print("saved report to file")


if __name__ == "__main__":
    main()