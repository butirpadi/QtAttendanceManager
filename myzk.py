
from zk import ZK, const
from struct import pack, unpack
import codecs
from datetime import datetime


class MyZK(ZK):
    
    def __init__(self, ip, port=4370, timeout=60, password=0, force_udp=False, ommit_ping=False, verbose=False, encoding='UTF-8'):
        super(MyZK,self).__init__(ip, port, timeout, password, force_udp, ommit_ping, verbose, encoding)
        
    def __decode_time(self, t):
        """
        Decode a timestamp retrieved from the timeclock

        copied from zkemsdk.c - DecodeTime
        """

        t = unpack("<I", t)[0]
        second = t % 60
        t = t // 60

        minute = t % 60
        t = t // 60

        hour = t % 24
        t = t // 24

        day = t % 31 + 1
        t = t // 31

        month = t % 12 + 1
        t = t // 12

        year = t + 2000

        d = datetime(year, month, day, hour, minute, second)

        return d

    def get_attendance_json(self):
        """
        return attendance record

        :return: List of Attendance object
        """
        self.read_sizes()
        if self.records == 0:
            return []
        users = self.get_users()
        if self.verbose:
            print(users)
        attendances = []
        attendance_data, size = self.read_with_buffer(const.CMD_ATTLOG_RRQ)
        if size < 4:
            if self.verbose:
                print("WRN: no attendance data")
            return []
        total_size = unpack("I", attendance_data[:4])[0]
        record_size = total_size/self.records
        if self.verbose:
            print("record_size is ", record_size)
        attendance_data = attendance_data[4:]
        if record_size == 8:
            while len(attendance_data) >= 8:
                uid, status, timestamp, punch = unpack('HB4sB', attendance_data.ljust(8, b'\x00')[:8])
                if self.verbose:
                    print(codecs.encode(attendance_data[:8], 'hex'))
                attendance_data = attendance_data[8:]
                tuser = list(filter(lambda x: x.uid == uid, users))
                if not tuser:
                    user_id = str(uid)
                else:
                    user_id = tuser[0].user_id
                timestamp = self.__decode_time(timestamp)
                # attendance = Attendance(user_id, timestamp, status, punch, uid)
                vals = {
                    'zknumber': user_id,
                    'timestamp': timestamp,
                    'status': status,
                    'punch': punch,
                    'uid': uid,
                }
                attendances.append(vals)
        elif record_size == 16:
            while len(attendance_data) >= 16:
                user_id, timestamp, status, punch, reserved, workcode = unpack('<I4sBB2sI', attendance_data.ljust(16, b'\x00')[:16])
                user_id = str(user_id)
                if self.verbose:
                    print(codecs.encode(attendance_data[:16], 'hex'))
                attendance_data = attendance_data[16:]
                tuser = list(filter(lambda x: x.user_id == user_id, users))
                if not tuser:
                    if self.verbose:
                        print("no uid {}", user_id)
                    uid = str(user_id)
                    tuser = list(filter(lambda x: x.uid == user_id, users))
                    if not tuser:
                        uid = str(user_id)
                    else:
                        uid = tuser[0].uid
                        user_id = tuser[0].user_id
                else:
                    uid = tuser[0].uid
                timestamp = self.__decode_time(timestamp)
                # attendance = Attendance(user_id, timestamp, status, punch, uid)
                vals = {
                    'zknumber': user_id,
                    'timestamp': timestamp,
                    'status': status,
                    'punch': punch,
                    'uid': uid,
                }
                attendances.append(vals)
        else:
            while len(attendance_data) >= 40:
                uid, user_id, status, timestamp, punch, space = unpack('<H24sB4sB8s', attendance_data.ljust(40, b'\x00')[:40])
                if self.verbose:
                    print(codecs.encode(attendance_data[:40], 'hex'))
                user_id = (user_id.split(b'\x00')[0]).decode(errors='ignore')
                timestamp = self.__decode_time(timestamp)

                # attendance = Attendance(user_id, timestamp, status, punch, uid)
                # attendances.append(attendance)
                vals = {
                    'zknumber': user_id,
                    'timestamp': timestamp,
                    'status': status,
                    'punch': punch,
                    'uid': uid,
                }
                attendances.append(vals)
                attendance_data = attendance_data[40:]
        return attendances

    def get_users_json(self):
        """
        :return: list of User on JSON format
        """
        self.read_sizes()
        if self.users == 0:
            self.next_uid = 1
            self.next_user_id = '1'
            return []
        users = []
        max_uid = 0
        userdata, size = self.read_with_buffer(const.CMD_USERTEMP_RRQ, const.FCT_USER)
        if self.verbose:
            print("user size {} (= {})".format(size, len(userdata)))
        if size <= 4:
            print("WRN: missing user data")
            return []
        total_size = unpack("I", userdata[:4])[0]
        self.user_packet_size = total_size / self.users
        if not self.user_packet_size in [28, 72]:
            if self.verbose:
                print("WRN packet size would be  %i" % self.user_packet_size)
        userdata = userdata[4:]
        if self.user_packet_size == 28:
            while len(userdata) >= 28:
                uid, privilege, password, name, card, group_id, timezone, user_id = unpack('<HB5s8sIxBhI', userdata.ljust(28, b'\x00')[:28])
                if uid > max_uid:
                    max_uid = uid
                password = (password.split(b'\x00')[0]).decode(self.encoding, errors='ignore')
                name = (name.split(b'\x00')[0]).decode(self.encoding, errors='ignore').strip()
                group_id = str(group_id)
                user_id = str(user_id)
                # TODO: check card value and find in ver8
                if not name:
                    name = "NN-%s" % user_id
                # user = User(uid, name, privilege, password, group_id, user_id, card)
                user = {
                    "uid": uid,
                    "name": name,
                    "privilege": privilege,
                    "password": password,
                    "group_id": group_id,
                    "user_id": user_id,
                    "card": card
                }
                users.append(user)
                if self.verbose:
                    print("[6]user:", uid, privilege, password, name, card, group_id, timezone, user_id)
                userdata = userdata[28:]
        else:
            while len(userdata) >= 72:
                uid, privilege, password, name, card, group_id, user_id = unpack('<HB8s24sIx7sx24s', userdata.ljust(72, b'\x00')[:72])
                password = (password.split(b'\x00')[0]).decode(self.encoding, errors='ignore')
                name = (name.split(b'\x00')[0]).decode(self.encoding, errors='ignore').strip()
                group_id = (group_id.split(b'\x00')[0]).decode(self.encoding, errors='ignore').strip()
                user_id = (user_id.split(b'\x00')[0]).decode(self.encoding, errors='ignore')
                if uid > max_uid:
                    max_uid = uid
                if not name:
                    name = "NN-%s" % user_id
                # user = User(uid, name, privilege, password, group_id, user_id, card)
                user = {
                    "uid": uid,
                    "name": name,
                    "privilege": privilege,
                    "password": password,
                    "group_id": group_id,
                    "user_id": user_id,
                    "card": card
                }
                users.append(user)
                userdata = userdata[72:]
        max_uid += 1
        self.next_uid = max_uid
        self.next_user_id = str(max_uid)
        while True:
            # if any(u for u in users if u.user_id == self.next_user_id):
            if any(u for u in users if u["user_id"] == self.next_user_id):
                max_uid += 1
                self.next_user_id = str(max_uid)
            else:
                break
        return users
