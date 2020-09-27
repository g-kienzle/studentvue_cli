# studentvue_cli
Simple command line interface for StudentVUE grades and schedules

## Installation:
`pip install studentvue-cli`

## Usage:
The first time the command is run, the edupoint domain for the district that will be used is needed to continue. Every time the command is run, username and password are needed. These will be asked for in runtime unless the corresponding flags are specified, and in the case of domain, it has not been previously given:
`--username='uname'
--password='password'
--domain='domain'`.
Domain only neeeds to be entered once per installation.


studentvue_cli can be used to access grades and the day's schedule. For grades, use
`svue grades`
To get a detailed grade report with all assignments, use the flag
`--long`
and to specify certain courses, use
`--course=courses`.
Courses can be in the format of either an integer, for one course, or a list, for multiple courses.

Example:
`svue --username='example' grades --long --course=[1,4,6]`
will ask for a password on running and a domain if not previously given, and the detailed grade report for periods 1, 4, and 6 will be outputted.

For schedule, use
`svue schedule`.
