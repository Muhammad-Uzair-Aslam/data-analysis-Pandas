# import pandas as pd
# className=pd.DataFrame({
#     "Name":["ali","usman","sohail","uzair"],
#     "class":[8,9,7,6],
#     "rollno":[1,2,3,4]
#
# })
# className["Age"]=[32,32,55,31]
# print(className)
#
# pd.Series([1,2,3,4],name="abc")
#
# print(className)
# print("**********max value")
# print(className.max())
# print(className.describe())
# titanic=pd.read_csv("titanic.csv")
# print(titanic.head(10))
# print(titanic.dtypes)
# titanic.to_excel("titanic.xlsx",sheet_name="passengers",index=False)
# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
# print(titanic)
# print(titanic.info())
# import  pandas as pd
# titanic=pd.read_csv("titanic.csv")
# print(titanic["Pclass"])
# print(type(titanic["Pclass"]))
# print(titanic[["Pclass","Name","Sex","Age"]])
# print(type(titanic[["Pclass","Name","Sex","Age"]]))
# above35=titanic[titanic["Age"]>35]
# print(above35)
# print(above35.shape)
# print(titanic[titanic["Pclass"].isin([2,3])])
# print(titanic[(titanic["Pclass"]==2)|(titanic["Pclass"]==3)])
# # i want to find the data whose age is known
# print(titanic[titanic["Age"].notna()])
# print(titanic.loc[titanic["Age"]>35,["Name","Pclass"]])
# print(titanic.iloc[9:25,2:5])
# titanic.iloc[0:6,0:2]="anomyous"
# print(titanic.head(10))
# print(titanic[(titanic["Pclass"]==2)|(titanic["Pclass"]==3)])
# titanic.iloc[1:2,1:2]="usman"
# print(titanic)
# titanic["umer"]=titanic["Age"]
# print(titanic[["umer"]])
# print(titanic)
# airQuality=pd.read_csv("air_quality_no2.csv",parse_dates=True,index_col=0)
# airQuality["london wala"]=airQuality["station_london"]*123
# print(airQuality)
# airQuality["ration"]=airQuality["station_paris"]/airQuality["station_antwerp"]
# print(airQuality)
# airQuality.rename(columns=str.upper)
# print(airQuality)


import pandas as pd
import matplotlib.pyplot as plt
# airquality=pd.read_csv("air_quality_no2.csv",parse_dates=True,index_col=0)
# # airquality.plot()
# # print(airquality.plot())
# # plt.show()
# # airquality["station_paris"].plot()
# # plt.show()
# # airquality.plot.scatter(x="station_london",y="station_paris",alpha=0.5)
# # plt.show()
# # print([method_name
# #        for method_name in dir(airquality.plot)
# #        if not method_name.startswith("_")])
# # airquality.plot.box()
# # plt.show()
# #
# #
# #
# #
# # axs=airquality.plot.area(figsize=(12,4),subplots=True)
# # plt.show()
# #
# # fig,axc=plt.subplots(figsize=(12,4))
# # airquality.plot.area(ax=axc)
# # axc.set_ylabel("NO $_2$ concentration")
# # fig.savefig("no2_concentration.png")
# # plt.show()
#
#
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # airquality = pd.read_csv("air_quality_no2.csv", parse_dates=True, index_col=0)
# # airquality["newColumn"]=airquality["station_london"]*1.33
# # print(airquality)
# # airquality["ratio_of_two_columns"]=airquality["station_paris"]/airquality["station_london"]
# # print(airquality)
# #
# #
# # airquality_renamed=airquality.rename(
# #     columns={
# #         "station_antwerp":"first",
# #         "station_paris":"second",
# #         "station_london":"third"
# #     }
# # )
# # print(airquality_renamed)
# # airquality.plot()
# # plt.show()
# # airquality.plot.scatter(x="newColumn",y="ratio_of_two_columns",alpha=0.5)
# # plt.show()
# # print(airquality[airquality["newColumn"].notna()])
# # airquality.plot.box()
# # plt.show()
# # airquality.plot.area(figsize=(12,5),subplots=True)
# # plt.show()
# # print([method_name
# #        for method_name in dir(airquality.plot)
# #        if not method_name.startswith("_")])
# # fig,axs=plt.subplots(figsize=(12,4))
# # airquality.plot.area(ax=axs)
# # axs.set_ylabel("NO $_2$ concentration")
# # fig.savefig("no_pic.png")
# # plt.show()
#
#
#
# # import pandas as pd
# # titanic=pd.read_csv("titanic.csv")
# # print("**** Mean of Age is **** ")
# # print(titanic["Age"].mean())
# # Med=titanic[["Age","Fare"]].median()
# # print("**** Median of Two Columns are ****")
# # print(Med)
# # print(titanic[["Age","Fare"]].describe())
# # print(titanic.agg({
# #     "Age":["count","max","min"],
# #     "Fare":["count","mean","median","std"]
# # }))
# # print(titanic[["Age","Sex"]].groupby("Sex").mean())
# # print(titanic.groupby("Sex").mean(numeric_only=True))
# # print(titanic.groupby("Sex")[["Age","Fare"]].mean())
# # print(titanic[["Age","Fare","Sex"]].groupby("Sex").mean())
# # print(titanic.groupby(["Sex","Pclass"])["Fare"].mean())
# # print(titanic[["Sex","Pclass","Fare"]].groupby(["Sex","Pclass"])["Fare"].mean())
# # print(titanic["Pclass"].value_counts())
# # print(titanic.groupby("Pclass")["Pclass"].count())
#
#
#
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # titanic=pd.read_csv("titanic.csv")
# # airquality=pd.read_csv("air_quality_long.csv",index_col="date.utc",parse_dates=True)
# # print(airquality)
# # print(titanic.sort_values(by=["Pclass","Age"], ascending=False))
#
# # no2=airquality[airquality["parameter"]=="no2"]
# # no2_subset=no2.sort_index().groupby(["location"]).head(2)
# # print(no2_subset)
# #
# # print(no2_subset.pivot(columns="location",values="value"))
# # airquality1=airquality.pivot(columns="location",values="value")
# # print(airquality1)
# # airquality=pd.melt(airquality,id_vars="date.utc")
# # print(airquality)
# # titanic1=titanic.pivot(columns=["Pclass"], values="Fare",index="PassengerId")
# # print(titanic1)
# # print(titanic1.melt(id_vars=["Pclass"]))
# #
# # no2=airquality[airquality["parameter"]=="no2"]
# # # print(no2)
# # no2_subset=no2.sort_index().groupby("location").head(2)
# # # print(no2_subset)
# # print(no2_subset.pivot(columns="location",values="value"))
# #
# #
# #
# #
# # no2.pivot(columns="location", values="value").plot()
# # plt.show()
# # print(airquality.pivot_table(values="value",index="parameter",columns="location",aggfunc="mean"))
# # print(airquality.pivot_table(values="value",index="parameter",columns="location",aggfunc="mean",margins=True))
# # no2_pivoted=no2.pivot(columns="location", values="value").reset_index()
# # print(no2_pivoted.head())
# # print(no2_pivoted.melt(id_vars="date.utc",value_vars=["BETR801", "FR04014", "London Westminster"],
# #     value_name="NO_2",
# #     var_name="id_location"))
# #
# # airqualityNo=pd.read_csv("air_quality_no2_long (1).csv",parse_dates=True)
# # airqualityNo=airqualityNo[["date.utc","location","parameter","value"]]
# # airqualitypm25=pd.read_csv("air_quality_pm25_long (1).csv",parse_dates=True)
# # airqualitypm25=airqualitypm25[["date.utc","location","parameter","value"]]
# # combineTable=pd.concat([ airqualityNo , airqualitypm25 ],axis=0)
# # print(combineTable)
# # airCombine=pd.concat([airqualityNo,airqualitypm25],keys=["no2","pm25"])
# # print(airCombine)
# # airStation=pd.read_csv("air_quality_stations.csv")
# # print(airStation.head())
# # combineTable=combineTable.sort_values("date.utc")
# # print(combineTable.head())
# # data=pd.merge(combineTable,airStation,how="left",on="location")
# # print(data)
# # airQualityParameters=pd.read_csv("air_quality_parameters.csv")
# # print(airQualityParameters)
# # dataset=pd.merge(combineTable,airQualityParameters,how="left" ,left_on="parameter",right_on="id")
# # print(dataset)
# # import pandas as pd
# # airqualityStation=pd.read_csv("air_quality_stations.csv")
# # print(airqualityStation)
# # airQualityParameter=pd.read_csv("air_quality_parameters.csv")
# # print(airQualityParameter)
# # airQualityNo=pd.read_csv("air_quality_no2_long (1).csv")
# # airQualityNo=airQualityNo[["date.utc","location","parameter","value"]]
# # print(airQualityNo)
# # airQualityPm=pd.read_csv("air_quality_pm25_long (1).csv")
# # airQualityPm=airQualityPm[["date.utc","location","parameter","value"]]
# # print(airQualityPm)
# # airQuality=pd.read_csv("air_quality_long.csv")
# # print(airQuality)
# # concat=pd.concat([airQualityNo,airQualityPm],axis=0)
# # print("****** CONCATING *****",concat)
# # airQualityMerge=pd.merge(airqualityStation,airQualityParameter,how="left" ,left_on="location",right_on="id")
# # print(airQualityMerge)
# # concat=concat.sort_values("date.utc")
# # print(concat.head())
# # print(pd.merge(concat,airqualityStation,how="left" , on="location"))
#
#
#
#
#
#
#
# import pandas as pd
# import matplotlib.pyplot as plt
# airqualityno2long=pd.read_csv("air_quality_no2_long (1).csv")
# airqualityno2long=airqualityno2long.rename(columns={"date.utc":"dateTime"})
# print(airqualityno2long.head())
# # print(airqualityno2long.country.unique())
#
#
# airqualityno2long["dateTime"]=pd.to_datetime(airqualityno2long["dateTime"])
# print(airqualityno2long["dateTime"])
# print(airqualityno2long.dateTime.min())
# print(airqualityno2long.dateTime.max())
# print(airqualityno2long.dateTime.max()-airqualityno2long.dateTime.min())
# airqualityno2long["month"]=airqualityno2long["dateTime"].dt.month
# print(airqualityno2long)
# abcd=airqualityno2long.groupby([airqualityno2long["dateTime"].dt.weekday,"location"])["value"].mean()
# print(abcd)
# fig,axs=plt.subplots(figsize=(12,5))
# airqualityno2long.groupby(airqualityno2long["dateTime"].dt.hour)["value"].mean().plot(kind="bar",rot=0,ax=axs)
# plt.xlabel("Hour of the Day")
# plt.ylabel("$NO_2 (mg/m^3)$")
# fig.savefig("hours.png")
# plt.show()
# no_2=airqualityno2long.pivot(index="dateTime",columns="location",values="value")
# print(no_2)
# print(no_2.index.weekday,no_2.index.month,no_2.index.year)
# no_2["2019-05-20":"2019-05-21"].plot()
# plt.show()
# monthly_max=no_2.resample("M").max()





# print(monthly_max)
# import pandas as pd
# titanic=pd.read_csv("titanic.csv")
# print(titanic.describe())
# print(titanic.head())
# print(titanic.dtypes)
#
# print(titanic["Age"].min())
# print(titanic["Age"].max())
# print(titanic["Name"].str.upper())
# print(titanic["Name"].str.split(",").get(0))
# no_2.resample("D").mean().plot(style="-o",figsize=(10,5))
# plt.show()


