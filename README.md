Utility Calculator
====

 UtilityCalc is a tool to assist in calculating shares when splitting bills

 example power.json
```json
 {
     "name": "Power Bill",
     "startDate": "2013-8-28",
     "endDate": "2013-11-27",
     "total":746.23,
     "shares": {
         "Bill": {},
         "Jim": {},
         "James": {
             "endDate": "2013-10-15"
         },
         "Ben": {
             "endDate": "2013-9-22"
         },
         "John":{}
     }
 }
```

Example run:

    #> utility-calc power.json

            Power Bill:

                 Start Date              : 2013-08-28 00:00:00
                 End Date                : 2013-11-27 00:00:00
                 Bill Total              : 746.23
                 Person Days             : 346
                 Price per person per day: 2.15673410405

                 Shares:

                     James:
                         Start Date: 2013-08-28 00:00:00
                         End Date  : 2013-08-28 00:00:00
                         Days      : 48
                         Share     : $104.0

                     Jim:
                         Start Date: 2013-08-28 00:00:00
                         End Date  : 2013-08-28 00:00:00
                         Days      : 91
                         Share     : $196.0

                     Ben:
                         Start Date: 2013-08-28 00:00:00
                         End Date  : 2013-08-28 00:00:00
                         Days      : 25
                         Share     : $54.0

                     John:
                         Start Date: 2013-08-28 00:00:00
                         End Date  : 2013-08-28 00:00:00
                         Days      : 91
                         Share     : $196.0

                     Bill:
                         Start Date: 2013-08-28 00:00:00
                         End Date  : 2013-08-28 00:00:00
                         Days      : 91
                         Share     : $196.0


            Rounded total:  746.0

