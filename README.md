# Python_User_Interface

## Task
design a user interface supporting selection/entry of data collection facilities

## Description
Diffraction data sets are primarily collected a synchrotron beamline, with a minor fraction collected at home sources. There are a limited number of synchrotron facilities, each with a limited number of beamlines (for order of magnitude estimates, 10 synchrotrons each with 8-12 beamlines).

The facilities all around the world are listed in below page
https://en.wikipedia.org/wiki/List_of_synchrotron_radiation_facilities

## Technical Background
Users interface with the databank through a django web front-end, backed by a postgresql database.

I took below listed data that user will input

1) Serial number

2) Facility Name

3) Country

4) Number of Synchrotron

5) Number of Beamline

To create web front end I have used Django and to store the database ( back end ) I have used PostgreSQL.
There are 3 pages.

1) Data Entry for user

2) Data retrieve and display to user

3) Admin

Please view the jpeg images
