__author__ = 'bb820935'

erros = [
   # [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x09, 0xA0, 0x00, 0x20, 0x84], #dsp

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x1B, 0xBC, 0x00, 0x01, 0x84], #BackupAmplifier1 reset 0
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x09, 0xBC, 0x00, 0x01, 0x72], #BackupAmplifier1 set
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x0B, 0xBC, 0x00, 0x01, 0x74], #BackupAmplifier1 ack

       [0x01, 0x81, 0x0A, 0x1F, 0x02, 0x1B, 0xB5, 0x00, 0x01, 0x7E], #amplifier reset 3
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x09, 0xB4, 0x00, 0x01, 0x6A], #amplifier set
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x0B, 0xB4, 0x00, 0x01, 0x6C], #amplifier5 ack

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA0, 0x00, 0x02, 0x65], #Spare_pwer 48 reset 6
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA0, 0x00, 0x02, 0x53], #Spare_pwer 48 set
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA0, 0x00, 0x02, 0x55], #Spare_pwer 48 ack
   
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x16, 0x21, 0x00, 0x40, 0x23], #fp1 mic line 1 error reset 9
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0x21, 0x00, 0x40, 0x12], #fp1 mic line 1 error set
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x06, 0x21, 0x00, 0x40, 0x13], #fp1 mic line 1 error ack

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0x21, 0x00, 0x01, 0xE5], #fp1 mic cap open reset 12
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0x21, 0x00, 0x01, 0xD5], #fp1 mic cap open ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0x21, 0x00, 0x01, 0xD3], #fp1 mic cap open line set

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0x21, 0x00, 0x10, 0xE2], #fp1 com1 error set 15
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x06, 0x21, 0x00, 0x10, 0xE3], #fp1 com1 error ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x16, 0x21, 0x00, 0x10, 0xF3], #fp1 com1 error reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0x29, 0x00, 0x04, 0xDE], #fp9 mic request error set 18
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x06, 0x29, 0x00, 0x04, 0xDF], #fp9 mic request error ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x16, 0x29, 0x00, 0x04, 0xEF], #fp9 mic request error reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0x29, 0x00, 0x01, 0xDB], #fp9 mic cap open set 21
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x06, 0x29, 0x00, 0x01, 0xDB], #fp9 mic cap open ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x16, 0x29, 0x00, 0x01, 0xEC], #fp9 mic cap open reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA0, 0x00, 0x01, 0x52], #230vAC set 24
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA0, 0x00, 0x01, 0x54], #230vAC ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA0, 0x00, 0x01, 0x64], #230vAC reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x09, 0x05, 0x00, 0x04, 0xBE], #speakerline 5a open line set 27
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x0B, 0x05, 0x00, 0x04, 0xC0], #speakerline 5a open line ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x1B, 0x05, 0x00, 0x04, 0xD0], #speakerline 5a open line reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x09, 0x05, 0x00, 0x01, 0xBB], #speakerline 5a short circuit set 30
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x0B, 0x05, 0x00, 0x01, 0xBD], #speakerline 5a short circuit ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x1B, 0x05, 0x00, 0x01, 0xCD], #speakerline 5a short circuit reset

       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA1, 0x08, 0x00, 0x5A], #EPC error open line set 33
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA1, 0x08, 0x00, 0x5C], #EPC error open line ack
       [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA1, 0x08, 0x00, 0x6C], #EPC error open line reset

        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA1, 0x04, 0x00, 0x56], #EPC error short set 36
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA1, 0x04, 0x00, 0x58], #EPC error short ack
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA1, 0x04, 0x00, 0x68], #EPC error short reset

        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA1, 0x02, 0x00, 0x54], #EPC 48v error set 39
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA1, 0x02, 0x00, 0x56], #EPC 48v error ack
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA1, 0x02, 0x00, 0x66], #EPC 48v error reset


        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA1, 0x01, 0x00, 0x53], #ext error input connection set 42
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA1, 0x01, 0x00, 0x55], #ext error input connection ack
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA1, 0x01, 0x00, 0x65], #ext error input connection reset

        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x05, 0xA1, 0x00, 0x20, 0x72], #mains error contact open set 45
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x07, 0xA1, 0x00, 0x20, 0x74], #mains error contact open ack
        [0x01, 0x81, 0x0A, 0x1F, 0x01, 0x17, 0xA1, 0x00, 0x20, 0x84], #mains error contact open reset

        [0x02, 0x81, 0x0A, 0x1F, 0x02, 0x17, 0xA1, 0x00, 0x20, 0x86], #mains error contact open reset 48
        [0x02, 0x81, 0x0A, 0x1F, 0x02, 0x05, 0xA1, 0x00, 0x20, 0x74], #mains error contact open set 49
      ]