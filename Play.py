import time
import rtmidi

ADN = [['55586062', '576065', '5057695458', '515866']]
#chordProgression = ['5865705465', '5861655566', '536260', '515967']", "['57546464', '576462', '5565625270', '4864676451']
#chordProgression = ['525964']
def numConcat(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 += num2
    return int(num1)

def playADN(data):
    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    print(available_ports, "\n")

    # Attempt to open the port
    if available_ports:
        midiout.open_port(1)
    else:
        midiout.open_virtual_port("My virtual output")

    for k in range(len(data)):
        print("Iteracion: ", k+1)
        for i in range (len(data[k])):
            #note on
            try:
                a = numConcat(data[k][i][0], data[k][i][1])
                b = numConcat(data[k][i][2], data[k][i][3])
                c = numConcat(data[k][i][4], data[k][i][5])
                d = numConcat(data[k][i][6], data[k][i][7])
                print(a, b, c, d)
            except:
                print(a, b, c)
                pass
            try:
                midiout.send_message([0x90, a, 127])
                midiout.send_message([0x90, b, 127])
                midiout.send_message([0x90, c, 127])
                midiout.send_message([0x90, d, 127])
            except:
                pass
            time.sleep(2.0)
            #note off
            try:
                a = (0x80, a, 0)
                b = (0x80, b, 0)
                c = (0x80, c, 0)
                d = (0x80, d, 0)
            except:
                pass
            try:
                midiout.send_message(a)
                midiout.send_message(b)
                midiout.send_message(c)
                midiout.send_message(d)
            except:
                pass

    del midiout

def playChordProgression(data):

    midiout = rtmidi.MidiOut()
    available_ports = midiout.get_ports()
    print(available_ports, "\n")

    # Attempt to open the port
    if available_ports:
        midiout.open_port(1)
    else:
        midiout.open_virtual_port("My virtual output")
    for j in range(10):
        for i in range(len(data)):
            # note on
            try:
                a = numConcat(data[i][0], data[i][1])
                b = numConcat(data[i][2], data[i][3])
                c = numConcat(data[i][4], data[i][5])
                d = numConcat(data[i][6], data[i][7])
                print(a, b, c, d)
            except:
                print(a, b, c)
                pass
            try:
                midiout.send_message([0x90, a, 127])
                midiout.send_message([0x90, b, 127])
                midiout.send_message([0x90, c, 127])
                midiout.send_message([0x90, d, 127])
            except:
                pass
            time.sleep(2.0)
            # note off
            try:
                a = (0x80, a, 0)
                b = (0x80, b, 0)
                c = (0x80, c, 0)
                d = (0x80, d, 0)
            except:
                pass
            try:
                midiout.send_message(a)
                midiout.send_message(b)
                midiout.send_message(c)
                midiout.send_message(d)
            except:
                pass
    del midiout

playADN(ADN)
#playChordProgression(chordProgression)

