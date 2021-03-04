import fire
from studentvue import StudentVue
import datetime
import bullet
from configparser import ConfigParser
import os


class SVInfo(object):
    def __init__(self, username="", password="", domain=""):
        cf = ConfigParser()
        p = os.path.join(os.path.dirname(__file__), "config.ini")
        cf.read(p)
        if username == "":
            username = input("Student ID -> ")
        if password == "":
            password = bullet.Password("Password -> ").launch()
        if domain == "":
            if not os.path.exists(p) or cf.get("values", "domain") == "":
                domain = input("District Edupoint Domain -> ")
                if not os.path.exists(p):
                    cf.add_section("values")
                cf.set("values", "domain", domain)
                with open(p, "w+") as configfile:
                    cf.write(configfile)
            else:
                domain = cf.get("values", "domain")
        self.sv = StudentVue(
            username,
            password,
            domain,
        )

    def grades(self, long=False, course="all"):
        courses = self.sv.get_gradebook().get("Gradebook").get("Courses").get("Course")

        grades = []



        for c in courses:
            filtered_assignments = []
            try:
                assignments = (
                    c.get("Marks").get("Mark").get("Assignments").get("Assignment")
                )
                if assignments != None and long:
                    for assignment in assignments:
                        filtered_assignments.append(
                            [assignment.get("@Measure"), assignment.get("@Points")]
                        )
            except:
                pass
            try:
                grades.append(
                    [
                        c.get("@Title"),
                        c.get("Marks").get("Mark").get("@CalculatedScoreRaw"),
                        filtered_assignments,
                    ]
                )
            except:
                grades.append(
                    [
                        c.get("@Title"),
                        "Grade unavailable",
                        filtered_assignments,
                    ]
                )
        fgrades = ""
        i = 0
        for grade in grades:
            add_grade = False
            i += 1
            if course != all:
                if type(course) is list:
                    if i in course or str(i) in course:
                        add_grade = True
                elif type(course) is int or type(course) is str:
                    if str(i) == str(course):
                        add_grade = True
                else:
                    raise TypeError(
                        'Type of "course" expected to be list or int. Got '
                        + type(course).__name__
                    )
            if course == "all" or add_grade:
                fgrades += grade[0].split("(")[0].rstrip() + ":  "
                fgrades += str(grade[1]) + "%\n"
                for assignment in grade[2]:
                    fgrades += "\t" + assignment[0] + ":  "
                    if "Points Possible" in assignment[1].split("/")[0]:
                        fgrades += (
                            str(float(assignment[1].split(" ")[0]))
                            + " "
                            + " ".join(assignment[1].split(" ")[1:])
                            + "\n"
                        )
                    else:
                        fgrades += (
                            str(float(assignment[1].split("/")[0]))
                            + " / "
                            + str(float(assignment[1].split("/")[1]))
                            + "\n"
                        )

        return fgrades.strip()

    def schedule(self):
        times = []
        now = datetime.datetime.now()
        sched = (
            self.sv.get_schedule()
            .get("StudentClassSchedule")
            .get("TodayScheduleInfoData")
            .get("SchoolInfos")
            .get("SchoolInfo")
        )
        if sched != None:
            sched = sched.get("Classes").get("ClassInfo")
            for item in sched:
                start = item.get("@StartTime").split(" ")
                end = item.get("@EndTime").split(" ")
                stimestr = start[0].split(":")
                etimestr = end[0].split(":")
                stime = []
                etime = []
                for item in stimestr:
                    stime.append(int(item))
                for item in etimestr:
                    etime.append(int(item))

                if start[1] == "PM" and stime[0] != 12:
                    stime[0] += 12
                if end[1] == "PM" and etime[0] != 12:
                    etime[0] += 12
                if start[1] == "AM" and stime[0] == 12:
                    stime[0] -= 12
                if end[1] == "AM" and etime[0] == 12:
                    etime[0] -= 12

                times.append([stime, etime])
            fschedule = f"Schedule for {now.month}/{now.day}/{now.year}:\n"
            t = 0
            for item in times:
                fschedule += (
                    "\t"
                    + " ".join(sched[t].get("@ClassName").split(" ")[1:])
                    .split("-")[0]
                    .rstrip()
                    + ":  "
                )
                fschedule += f"{datetime.time(hour=item[0][0],minute=item[0][1])} to {datetime.time(hour=item[1][0],minute=item[1][1])}\n"

                t += 1
            return fschedule.strip()
        else:
            return "No school schedule"


def main():
    # initialize cli
    fire.Fire(SVInfo)


if __name__ == "__main__":
    main()