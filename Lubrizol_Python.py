import PIconnect as PI
from PIconnect.PIConsts import SummaryType

taglist = ['CDEP158','CDM158','CDT158','SINUSOID','SINUSOIDU']
start_time = '21-Jan-18 20:08:48' #'*-2y'
end_time = '21-Jan-20 20:08:48'
filter_expression="'%tag%' > 100 and '%tag%' < 115" #Multiple tests can be done with OR AND

with PI.PIServer() as server:
    points = server.search('SINUSOID')[0]
    data = points.summary('*-7d', '*', SummaryType.MAXIMUM | SummaryType.MINIMUM |SummaryType.AVERAGE | SummaryType.TOTAL)
    print(data)


#with PI.PIServer() as server:
#    for tagname in taglist:
#        point = server.search(tagname)[0]
#        data = (point.recorded_values(start_time, end_time, filter_expression="'%tag%' > 80 and '%tag%' < 115"))
#        print(tagname)
#        print(data)

    