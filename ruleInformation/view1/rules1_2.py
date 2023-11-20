def rule0(X):
    if X['1662'].values <= 0.882589191198349 :
        if X['1361'].values <= -0.5067234486341476 :
            if X['986'].values > -0.4742501229047775 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule1(X):
    if X['1662'].values <= 0.882589191198349 :
        if X['1361'].values > -0.5067234486341476 :
            if X['1533'].values <= -0.3218894898891449 :
                if X['1029'].values <= -0.2707812041044235 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule2(X):
    if X['1662'].values <= 0.882589191198349 :
        if X['1361'].values > -0.5067234486341476 :
            if X['1533'].values <= -0.3218894898891449 :
                if X['1029'].values > -0.2707812041044235 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule3(X):
    if X['1662'].values <= 0.882589191198349 :
        if X['1361'].values > -0.5067234486341476 :
            if X['1533'].values > -0.3218894898891449 :
                if X['1188'].values <= 0.30492250621318817 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule4(X):
    if X['1172'].values > -0.4848650246858597 :
        if X['1408'].values <= -0.43629656732082367 :
            if X['1100'].values <= 0.14059099927544594 :
                if X['1642'].values <= 1.4843263626098633 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule5(X):
    if X['1662'].values > 0.882589191198349 :
        if X['1415'].values <= 2.0285335183143616 :
            return 0
        else:
            return -1
    else:
        return -1
def rule6(X):
    if X['1618'].values <= -0.3479182869195938 :
        if X['1067'].values <= 0.6142584383487701 :
            if X['959'].values <= 0.3748582601547241 :
                if X['1796'].values > -0.32378894090652466 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule7(X):
    if X['1618'].values <= -0.3479182869195938 :
        if X['1067'].values <= 0.6142584383487701 :
            if X['959'].values > 0.3748582601547241 :
                if X['1128'].values <= 0.365673303604126 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule8(X):
    if X['1618'].values <= -0.3479182869195938 :
        if X['1067'].values > 0.6142584383487701 :
            return 1
        else:
            return -1
    else:
        return -1
def rule9(X):
    if X['1618'].values > -0.3479182869195938 :
        if X['1522'].values <= 0.5555765926837921 :
            if X['1329'].values <= -0.3182881027460098 :
                if X['1395'].values <= 0.5329448282718658 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule10(X):
    if X['1774'].values <= 0.08726129680871964 :
        if X['1603'].values > 0.11379846185445786 :
            if X['1295'].values > -0.3927091509103775 :
                if X['1107'].values > -0.589615136384964 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule11(X):
    if X['1618'].values > -0.3479182869195938 :
        if X['1522'].values <= 0.5555765926837921 :
            if X['1329'].values > -0.3182881027460098 :
                if X['1813'].values > -0.08741900324821472 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule12(X):
    if X['1618'].values > -0.3479182869195938 :
        if X['1522'].values > 0.5555765926837921 :
            if X['1508'].values > -0.3161522075533867 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule13(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values <= 0.560950517654419 :
            if X['1665'].values <= 0.46131518483161926 :
                if X['1516'].values <= 0.2095966786146164 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule14(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values <= 0.560950517654419 :
            if X['1665'].values <= 0.46131518483161926 :
                if X['1516'].values > 0.2095966786146164 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule15(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values <= 0.560950517654419 :
            if X['1665'].values > 0.46131518483161926 :
                if X['1626'].values <= 0.16842251271009445 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule16(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values <= 0.560950517654419 :
            if X['1665'].values > 0.46131518483161926 :
                if X['1626'].values > 0.16842251271009445 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule17(X):
    if X['956'].values <= 0.5430828332901001 :
        if X['1023'].values > 0.2946911156177521 :
            if X['1401'].values <= -0.40008221566677094 :
                if X['1417'].values > -0.9097087681293488 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule18(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values > 0.560950517654419 :
            if X['910'].values <= 0.7284314632415771 :
                if X['1529'].values > -0.38625413179397583 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule19(X):
    if X['1798'].values <= 0.6918289661407471 :
        if X['1784'].values > 0.560950517654419 :
            if X['910'].values > 0.7284314632415771 :
                if X['1806'].values > -0.0852852389216423 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule20(X):
    if X['1798'].values > 0.6918289661407471 :
        if X['1615'].values <= 0.23548981547355652 :
            return 0
        else:
            return -1
    else:
        return -1
def rule21(X):
    if X['1798'].values > 0.6918289661407471 :
        if X['1615'].values > 0.23548981547355652 :
            return 1
        else:
            return -1
    else:
        return -1
def rule22(X):
    if X['1559'].values <= 0.3107806444168091 :
        if X['982'].values <= -0.8544550538063049 :
            return 0
        else:
            return -1
    else:
        return -1
def rule23(X):
    if X['1348'].values > 0.18832623213529587 :
        if X['1417'].values > 0.12665515765547752 :
            if X['1759'].values > -0.05430402792990208 :
                if X['1115'].values > 0.29723672568798065 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule24(X):
    if X['1559'].values <= 0.3107806444168091 :
        if X['982'].values > -0.8544550538063049 :
            if X['1496'].values <= 0.6652329862117767 :
                if X['1146'].values > 0.14287365227937698 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule25(X):
    if X['1559'].values <= 0.3107806444168091 :
        if X['982'].values > -0.8544550538063049 :
            if X['1496'].values > 0.6652329862117767 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule26(X):
    if X['1559'].values > 0.3107806444168091 :
        if X['1662'].values <= -0.14926441758871078 :
            if X['1548'].values <= 0.010803364217281342 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule27(X):
    if X['1559'].values > 0.3107806444168091 :
        if X['1662'].values > -0.14926441758871078 :
            if X['1201'].values <= 0.3943992853164673 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule28(X):
    if X['1071'].values <= 0.1741170436143875 :
        if X['1559'].values > 0.5708272308111191 :
            return 0
        else:
            return -1
    else:
        return -1
def rule29(X):
    if X['1105'].values <= 0.030609574168920517 :
        if X['1522'].values <= -0.13757827132940292 :
            if X['1483'].values <= -0.06834710203111172 :
                if X['1243'].values > -0.04585595428943634 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule30(X):
    if X['1105'].values <= 0.030609574168920517 :
        if X['1522'].values <= -0.13757827132940292 :
            if X['1483'].values > -0.06834710203111172 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule31(X):
    if X['1193'].values > 0.6866239905357361 :
        return 0
    else:
        return -1
def rule32(X):
    if X['1105'].values <= 0.030609574168920517 :
        if X['1522'].values > -0.13757827132940292 :
            if X['1785'].values <= 0.1996638923883438 :
                if X['1509'].values > 0.1730566918849945 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule33(X):
    if X['1105'].values <= 0.030609574168920517 :
        if X['1522'].values > -0.13757827132940292 :
            if X['1785'].values > 0.1996638923883438 :
                if X['1168'].values <= 0.4189361035823822 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule34(X):
    if X['1105'].values > 0.030609574168920517 :
        if X['1666'].values <= 0.4605405479669571 :
            if X['1265'].values <= 0.01822319347411394 :
                if X['1022'].values <= 0.6684580445289612 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule35(X):
    if X['1086'].values <= -0.5627769231796265 :
        if X['1037'].values <= 0.7512421309947968 :
            if X['1116'].values > 0.4520832598209381 :
                if X['1251'].values <= 0.19383380934596062 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule36(X):
    if X['1105'].values > 0.030609574168920517 :
        if X['1666'].values <= 0.4605405479669571 :
            if X['1265'].values > 0.01822319347411394 :
                if X['1150'].values <= -0.5654209554195404 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule37(X):
    if X['1546'].values <= 0.28609512746334076 :
        if X['1376'].values <= 0.06118115037679672 :
            if X['1444'].values > -0.14607463777065277 :
                if X['1615'].values > 0.8008772134780884 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule38(X):
    if X['1105'].values > 0.030609574168920517 :
        if X['1666'].values > 0.4605405479669571 :
            if X['1601'].values <= 0.9384637773036957 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule39(X):
    if X['1012'].values <= 0.3052668124437332 :
        if X['1573'].values <= -0.24752362072467804 :
            if X['1595'].values <= 0.09737827256321907 :
                if X['1009'].values > -0.24832619726657867 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule40(X):
    if X['1012'].values <= 0.3052668124437332 :
        if X['1573'].values <= -0.24752362072467804 :
            if X['1595'].values > 0.09737827256321907 :
                if X['1168'].values <= 0.17220543324947357 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule41(X):
    if X['1166'].values <= -0.6067337989807129 :
        if X['1578'].values <= 0.13857148215174675 :
            if X['1134'].values <= 0.26817984506487846 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule42(X):
    if X['1012'].values <= 0.3052668124437332 :
        if X['1573'].values > -0.24752362072467804 :
            if X['1171'].values <= 0.36322906613349915 :
                if X['1725'].values <= 0.45127134025096893 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule43(X):
    if X['1546'].values <= 0.28609512746334076 :
        if X['1376'].values > 0.06118115037679672 :
            if X['1408'].values <= -0.17494741827249527 :
                if X['1424'].values > -0.3994188606739044 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule44(X):
    if X['1730'].values > -0.4748941957950592 :
        if X['1085'].values > 0.05076029896736145 :
            if X['1145'].values <= -0.15654096752405167 :
                if X['1069'].values > 0.05674227140843868 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule45(X):
    if X['1012'].values > 0.3052668124437332 :
        if X['1319'].values <= 0.02771892584860325 :
            if X['936'].values <= 0.06364910118281841 :
                if X['1761'].values <= -0.3644866943359375 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule46(X):
    if X['1405'].values > -0.016455632634460926 :
        if X['1466'].values > -0.5317347645759583 :
            if X['964'].values > -1.3411948084831238 :
                if X['1784'].values > -0.13622380048036575 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule47(X):
    if X['1012'].values > 0.3052668124437332 :
        if X['1319'].values <= 0.02771892584860325 :
            if X['936'].values > 0.06364910118281841 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule48(X):
    if X['1012'].values > 0.3052668124437332 :
        if X['1319'].values > 0.02771892584860325 :
            if X['1050'].values <= -0.42144373059272766 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule49(X):
    if X['1012'].values > 0.3052668124437332 :
        if X['1319'].values > 0.02771892584860325 :
            if X['1050'].values > -0.42144373059272766 :
                if X['1066'].values <= 0.25762832164764404 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule50(X):
    if X['1071'].values > 0.1741170436143875 :
        if X['1755'].values > 0.053674595430493355 :
            if X['1415'].values <= 0.2549638971686363 :
                if X['1434'].values > -0.4745222181081772 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule51(X):
    if X['1633'].values <= 0.5386286675930023 :
        if X['1011'].values <= 0.9113863408565521 :
            if X['944'].values <= -0.6181944906711578 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule52(X):
    if X['1035'].values <= 0.1232370100915432 :
        if X['1417'].values > -0.21825718879699707 :
            if X['898'].values <= -0.020045855082571507 :
                if X['1578'].values <= 0.6154966652393341 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule53(X):
    if X['1633'].values <= 0.5386286675930023 :
        if X['1011'].values > 0.9113863408565521 :
            return 0
        else:
            return -1
    else:
        return -1
def rule54(X):
    if X['1633'].values > 0.5386286675930023 :
        if X['1642'].values <= 0.5320603251457214 :
            if X['1518'].values <= 0.45164409279823303 :
                if X['1697'].values > -0.06741796806454659 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule55(X):
    if X['1633'].values > 0.5386286675930023 :
        if X['1642'].values > 0.5320603251457214 :
            if X['1704'].values > -0.27670320868492126 :
                if X['1622'].values <= 0.4794907718896866 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule56(X):
    if X['1534'].values > 0.21067752689123154 :
        if X['1700'].values > 0.19715777784585953 :
            if X['1717'].values <= 0.5089736878871918 :
                if X['1840'].values > -0.21706686168909073 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule57(X):
    if X['1145'].values <= 0.32205066084861755 :
        if X['887'].values <= -0.07922368496656418 :
            if X['1010'].values <= 0.013793372083455324 :
                if X['1601'].values > 0.06291607394814491 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule58(X):
    if X['1145'].values <= 0.32205066084861755 :
        if X['887'].values <= -0.07922368496656418 :
            if X['1010'].values > 0.013793372083455324 :
                if X['1366'].values <= 0.2174973338842392 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule59(X):
    if X['1145'].values <= 0.32205066084861755 :
        if X['887'].values <= -0.07922368496656418 :
            if X['1010'].values > 0.013793372083455324 :
                if X['1366'].values > 0.2174973338842392 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule60(X):
    if X['1145'].values <= 0.32205066084861755 :
        if X['887'].values > -0.07922368496656418 :
            if X['982'].values <= -0.8544550538063049 :
                if X['1373'].values > -0.4385155290365219 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule61(X):
    if X['1145'].values <= 0.32205066084861755 :
        if X['887'].values > -0.07922368496656418 :
            if X['982'].values > -0.8544550538063049 :
                if X['1510'].values <= 0.043355656787753105 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule62(X):
    if X['1405'].values <= -0.016455632634460926 :
        if X['1069'].values > -0.23523180931806564 :
            if X['1326'].values <= -0.1657092198729515 :
                if X['1616'].values <= -0.5212206542491913 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule63(X):
    if X['1145'].values > 0.32205066084861755 :
        if X['1456'].values <= 0.031106396578252316 :
            if X['1580'].values <= 0.14740654453635216 :
                if X['979'].values <= 0.3120199143886566 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule64(X):
    if X['1145'].values > 0.32205066084861755 :
        if X['1456'].values <= 0.031106396578252316 :
            if X['1580'].values > 0.14740654453635216 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule65(X):
    if X['1145'].values > 0.32205066084861755 :
        if X['1456'].values > 0.031106396578252316 :
            if X['934'].values > -0.09163245558738708 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule66(X):
    if X['1735'].values <= -0.24762563407421112 :
        if X['1776'].values <= 0.23746207356452942 :
            if X['921'].values <= -0.0925540141761303 :
                if X['1515'].values > -0.3514406532049179 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule67(X):
    if X['1735'].values <= -0.24762563407421112 :
        if X['1776'].values <= 0.23746207356452942 :
            if X['921'].values > -0.0925540141761303 :
                if X['1480'].values <= 0.6689154505729675 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule68(X):
    if X['1735'].values <= -0.24762563407421112 :
        if X['1776'].values <= 0.23746207356452942 :
            if X['921'].values > -0.0925540141761303 :
                if X['1480'].values > 0.6689154505729675 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule69(X):
    if X['1735'].values <= -0.24762563407421112 :
        if X['1776'].values > 0.23746207356452942 :
            if X['1200'].values <= -0.2831018269062042 :
                if X['1640'].values <= 0.5641361773014069 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule70(X):
    if X['1735'].values <= -0.24762563407421112 :
        if X['1776'].values > 0.23746207356452942 :
            if X['1200'].values > -0.2831018269062042 :
                if X['1664'].values <= -0.08049195632338524 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule71(X):
    if X['1193'].values <= 0.586669534444809 :
        if X['1578'].values > -0.05365712754428387 :
            if X['1502'].values <= 0.30082640051841736 :
                if X['1782'].values <= -0.3102843761444092 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule72(X):
    if X['1735'].values > -0.24762563407421112 :
        if X['1294'].values <= -0.773376077413559 :
            return 0
        else:
            return -1
    else:
        return -1
def rule73(X):
    if X['1160'].values <= 0.7501197159290314 :
        if X['1734'].values > -0.08429931849241257 :
            if X['1585'].values > 0.6495382785797119 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule74(X):
    if X['1735'].values > -0.24762563407421112 :
        if X['1294'].values > -0.773376077413559 :
            if X['1525'].values <= 0.12553180381655693 :
                if X['1658'].values > 0.15056230872869492 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule75(X):
    if X['1735'].values > -0.24762563407421112 :
        if X['1294'].values > -0.773376077413559 :
            if X['1525'].values > 0.12553180381655693 :
                if X['1381'].values > -1.8241170644760132 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule76(X):
    if X['1321'].values <= 1.4911638498306274 :
        if X['1250'].values <= -0.42183057963848114 :
            if X['1853'].values > -0.4371795505285263 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule77(X):
    if X['1321'].values <= 1.4911638498306274 :
        if X['1250'].values > -0.42183057963848114 :
            if X['1620'].values <= -0.4522664248943329 :
                if X['1341'].values <= 0.23489704728126526 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule78(X):
    if X['1321'].values <= 1.4911638498306274 :
        if X['1250'].values > -0.42183057963848114 :
            if X['1620'].values <= -0.4522664248943329 :
                if X['1341'].values > 0.23489704728126526 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule79(X):
    if X['1534'].values <= 0.21067752689123154 :
        if X['1537'].values > 1.5543000102043152 :
            if X['1416'].values <= 0.5464289337396622 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule80(X):
    if X['1321'].values <= 1.4911638498306274 :
        if X['1250'].values > -0.42183057963848114 :
            if X['1620'].values > -0.4522664248943329 :
                if X['919'].values > -0.03046989906579256 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule81(X):
    if X['1321'].values > 1.4911638498306274 :
        if X['985'].values <= 0.20811745524406433 :
            return 0
        else:
            return -1
    else:
        return -1
def rule82(X):
    if X['1166'].values > -0.6067337989807129 :
        if X['1060'].values > -0.30132895708084106 :
            if X['947'].values <= -0.06567694619297981 :
                if X['1178'].values > 0.09016067534685135 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule83(X):
    if X['1605'].values <= 0.2507947236299515 :
        if X['1479'].values <= 0.17343087494373322 :
            if X['1671'].values <= 0.3581368029117584 :
                if X['1156'].values > 0.005155656370334327 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule84(X):
    if X['1605'].values <= 0.2507947236299515 :
        if X['1479'].values <= 0.17343087494373322 :
            if X['1671'].values > 0.3581368029117584 :
                if X['1807'].values <= 0.02754092402756214 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule85(X):
    if X['1605'].values <= 0.2507947236299515 :
        if X['1479'].values <= 0.17343087494373322 :
            if X['1671'].values > 0.3581368029117584 :
                if X['1807'].values > 0.02754092402756214 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule86(X):
    if X['1605'].values <= 0.2507947236299515 :
        if X['1479'].values > 0.17343087494373322 :
            if X['1747'].values <= 0.38139763474464417 :
                if X['1004'].values <= -0.5121245086193085 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule87(X):
    if X['1035'].values <= 0.1232370100915432 :
        if X['1417'].values <= -0.21825718879699707 :
            if X['1039'].values > -0.5726355090737343 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule88(X):
    if X['1605'].values <= 0.2507947236299515 :
        if X['1479'].values > 0.17343087494373322 :
            if X['1747'].values > 0.38139763474464417 :
                if X['1534'].values > -0.30638884007930756 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule89(X):
    if X['1605'].values > 0.2507947236299515 :
        if X['1427'].values <= 0.37962310016155243 :
            if X['1621'].values <= 0.7026707231998444 :
                if X['1683'].values <= 0.5465856343507767 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule90(X):
    if X['1605'].values > 0.2507947236299515 :
        if X['1427'].values <= 0.37962310016155243 :
            if X['1621'].values > 0.7026707231998444 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule91(X):
    if X['1605'].values > 0.2507947236299515 :
        if X['1427'].values > 0.37962310016155243 :
            return 1
        else:
            return -1
    else:
        return -1
def rule92(X):
    if X['1740'].values <= 0.1652301847934723 :
        if X['976'].values <= 0.7762827575206757 :
            if X['897'].values <= -0.1555067002773285 :
                if X['1164'].values <= -0.03823412931524217 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule93(X):
    if X['969'].values <= 0.2253270447254181 :
        if X['1581'].values > -0.04873348027467728 :
            if X['1464'].values > -0.901723325252533 :
                if X['1447'].values > -0.14214200526475906 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule94(X):
    if X['1130'].values > -0.48629245162010193 :
        if X['1553'].values <= -0.06097067520022392 :
            if X['942'].values > -0.46272018551826477 :
                if X['1534'].values <= 0.1636609435081482 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule95(X):
    if X['1740'].values <= 0.1652301847934723 :
        if X['976'].values <= 0.7762827575206757 :
            if X['897'].values > -0.1555067002773285 :
                if X['1673'].values > -0.5629792809486389 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule96(X):
    if X['1740'].values <= 0.1652301847934723 :
        if X['976'].values > 0.7762827575206757 :
            if X['1480'].values > -0.33788543939590454 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule97(X):
    if X['1740'].values > 0.1652301847934723 :
        if X['1065'].values <= -0.09344038367271423 :
            if X['1593'].values > -0.4197946786880493 :
                if X['1640'].values <= 0.21910188347101212 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule98(X):
    if X['1740'].values > 0.1652301847934723 :
        if X['1065'].values > -0.09344038367271423 :
            if X['1553'].values <= 0.05725089833140373 :
                if X['1498'].values <= -0.13932327553629875 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule99(X):
    if X['1740'].values > 0.1652301847934723 :
        if X['1065'].values > -0.09344038367271423 :
            if X['1553'].values <= 0.05725089833140373 :
                if X['1498'].values > -0.13932327553629875 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule100(X):
    if X['1740'].values > 0.1652301847934723 :
        if X['1065'].values > -0.09344038367271423 :
            if X['1553'].values > 0.05725089833140373 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule101(X):
    if X['1304'].values <= 0.3181399703025818 :
        if X['1041'].values <= -0.01324018882587552 :
            if X['1647'].values <= -0.06343036331236362 :
                if X['1342'].values <= 0.25510700792074203 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule102(X):
    if X['1510'].values <= 0.04307365044951439 :
        if X['1289'].values > -0.1472807228565216 :
            if X['1811'].values <= -0.7304685413837433 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule103(X):
    if X['1304'].values <= 0.3181399703025818 :
        if X['1041'].values <= -0.01324018882587552 :
            if X['1647'].values > -0.06343036331236362 :
                if X['1831'].values <= -0.2652900218963623 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule104(X):
    if X['1304'].values <= 0.3181399703025818 :
        if X['1041'].values <= -0.01324018882587552 :
            if X['1647'].values > -0.06343036331236362 :
                if X['1831'].values > -0.2652900218963623 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule105(X):
    if X['1304'].values <= 0.3181399703025818 :
        if X['1041'].values > -0.01324018882587552 :
            if X['1820'].values <= 0.019132832065224648 :
                if X['948'].values > -0.4974868595600128 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule106(X):
    if X['1774'].values <= 0.08726129680871964 :
        if X['1603'].values > 0.11379846185445786 :
            if X['1295'].values <= -0.3927091509103775 :
                if X['963'].values > 0.0010343696922063828 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule107(X):
    if X['1304'].values <= 0.3181399703025818 :
        if X['1041'].values > -0.01324018882587552 :
            if X['1820'].values > 0.019132832065224648 :
                if X['1185'].values > -0.0981416143476963 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule108(X):
    if X['1304'].values > 0.3181399703025818 :
        if X['1129'].values <= -0.0017271433025598526 :
            if X['1405'].values > -0.36346256732940674 :
                if X['1775'].values <= 0.2038273960351944 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule109(X):
    if X['1304'].values > 0.3181399703025818 :
        if X['1129'].values > -0.0017271433025598526 :
            if X['1434'].values > -0.6014828979969025 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule110(X):
    if X['904'].values <= -0.8264907598495483 :
        return 0
    else:
        return -1
def rule111(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values <= 0.09332776442170143 :
            if X['1569'].values <= -0.1193004660308361 :
                if X['1115'].values <= -0.09350601211190224 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule112(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values <= 0.09332776442170143 :
            if X['1569'].values <= -0.1193004660308361 :
                if X['1115'].values > -0.09350601211190224 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule113(X):
    if X['956'].values > 0.5430828332901001 :
        if X['1436'].values <= 0.33634379506111145 :
            if X['1219'].values <= 0.41893504559993744 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule114(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values <= 0.09332776442170143 :
            if X['1569'].values > -0.1193004660308361 :
                if X['1504'].values > -0.06549374759197235 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule115(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values > 0.09332776442170143 :
            if X['1287'].values <= -0.2840747684240341 :
                if X['917'].values <= 0.21091175079345703 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule116(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values > 0.09332776442170143 :
            if X['1287'].values > -0.2840747684240341 :
                if X['1297'].values <= 0.19059976190328598 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule117(X):
    if X['904'].values > -0.8264907598495483 :
        if X['1510'].values > 0.09332776442170143 :
            if X['1287'].values > -0.2840747684240341 :
                if X['1297'].values > 0.19059976190328598 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule118(X):
    if X['1573'].values <= -0.249587282538414 :
        if X['1752'].values <= 0.6308285892009735 :
            if X['1834'].values <= -0.7342194318771362 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule119(X):
    if X['1166'].values > -0.6067337989807129 :
        if X['1060'].values > -0.30132895708084106 :
            if X['947'].values > -0.06567694619297981 :
                if X['1478'].values <= 0.15388163924217224 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule120(X):
    if X['1035'].values <= 0.1232370100915432 :
        if X['1417'].values > -0.21825718879699707 :
            if X['898'].values > -0.020045855082571507 :
                if X['964'].values <= -0.03201816137880087 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule121(X):
    if X['1573'].values <= -0.249587282538414 :
        if X['1752'].values > 0.6308285892009735 :
            return 0
        else:
            return -1
    else:
        return -1
def rule122(X):
    if X['1573'].values > -0.249587282538414 :
        if X['1668'].values <= 0.30235855281352997 :
            if X['1836'].values <= -1.2978249788284302 :
                if X['1717'].values <= 0.9670789241790771 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule123(X):
    if X['969'].values > 0.2253270447254181 :
        if X['1601'].values <= 0.03931504674255848 :
            if X['1288'].values <= 0.039172224467620254 :
                if X['1619'].values > -0.7367392182350159 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule124(X):
    if X['1573'].values > -0.249587282538414 :
        if X['1668'].values > 0.30235855281352997 :
            if X['1718'].values <= -0.002423768164590001 :
                if X['1043'].values <= 0.08874068409204483 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule125(X):
    if X['1573'].values > -0.249587282538414 :
        if X['1668'].values > 0.30235855281352997 :
            if X['1718'].values <= -0.002423768164590001 :
                if X['1043'].values > 0.08874068409204483 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule126(X):
    if X['1573'].values > -0.249587282538414 :
        if X['1668'].values > 0.30235855281352997 :
            if X['1718'].values > -0.002423768164590001 :
                if X['978'].values <= -0.2255658283829689 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule127(X):
    if X['1292'].values <= -0.2687876522541046 :
        if X['1431'].values <= -0.6749187111854553 :
            return 0
        else:
            return -1
    else:
        return -1
def rule128(X):
    if X['1774'].values > 0.08726129680871964 :
        if X['1299'].values <= -0.2870655953884125 :
            if X['1396'].values > -0.2989876866340637 :
                if X['1332'].values <= 0.4165498614311218 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule129(X):
    if X['1292'].values <= -0.2687876522541046 :
        if X['1431'].values > -0.6749187111854553 :
            if X['1176'].values <= 0.5571598708629608 :
                if X['1397'].values > -0.435648113489151 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule130(X):
    if X['1292'].values > -0.2687876522541046 :
        if X['1456'].values <= -0.14313887804746628 :
            if X['1809'].values <= 0.8024996817111969 :
                if X['1617'].values > -0.5625531375408173 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule131(X):
    if X['1292'].values > -0.2687876522541046 :
        if X['1456'].values <= -0.14313887804746628 :
            if X['1809'].values > 0.8024996817111969 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule132(X):
    if X['1292'].values > -0.2687876522541046 :
        if X['1456'].values > -0.14313887804746628 :
            if X['896'].values <= -0.04448355361819267 :
                if X['1853'].values <= 0.7501630783081055 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule133(X):
    if X['1292'].values > -0.2687876522541046 :
        if X['1456'].values > -0.14313887804746628 :
            if X['896'].values <= -0.04448355361819267 :
                if X['1853'].values > 0.7501630783081055 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule134(X):
    if X['1413'].values > 0.4179270714521408 :
        if X['1383'].values > -0.2564472481608391 :
            if X['1314'].values > -0.17295297607779503 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule135(X):
    if X['1292'].values > -0.2687876522541046 :
        if X['1456'].values > -0.14313887804746628 :
            if X['896'].values > -0.04448355361819267 :
                if X['1096'].values > 0.4171946197748184 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule136(X):
    if X['1287'].values <= -0.005961760180070996 :
        if X['1527'].values <= -0.16036108136177063 :
            if X['1703'].values <= 0.055397551506757736 :
                if X['1771'].values > -0.9310118556022644 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule137(X):
    if X['1287'].values <= -0.005961760180070996 :
        if X['1527'].values <= -0.16036108136177063 :
            if X['1703'].values > 0.055397551506757736 :
                if X['1573'].values > -0.6321974694728851 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule138(X):
    if X['892'].values > -0.23184429854154587 :
        if X['1642'].values <= 0.7493916153907776 :
            if X['1809'].values > 0.6284122169017792 :
                if X['1043'].values > 0.12012064829468727 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule139(X):
    if X['1287'].values <= -0.005961760180070996 :
        if X['1527'].values > -0.16036108136177063 :
            if X['1746'].values <= 0.07987398654222488 :
                if X['881'].values > -0.05720684863626957 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule140(X):
    if X['1348'].values <= 0.18832623213529587 :
        if X['1806'].values <= 0.9110192656517029 :
            if X['1078'].values <= -0.020727090537548065 :
                if X['1535'].values <= -0.226338729262352 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule141(X):
    if X['1287'].values <= -0.005961760180070996 :
        if X['1527'].values > -0.16036108136177063 :
            if X['1746'].values > 0.07987398654222488 :
                if X['1010'].values > -0.026718543842434883 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule142(X):
    if X['1287'].values > -0.005961760180070996 :
        if X['927'].values <= 0.38985230028629303 :
            if X['1105'].values <= 0.09681914746761322 :
                if X['1699'].values <= -0.12959647551178932 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule143(X):
    if X['1287'].values > -0.005961760180070996 :
        if X['927'].values <= 0.38985230028629303 :
            if X['1105'].values <= 0.09681914746761322 :
                if X['1699'].values > -0.12959647551178932 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule144(X):
    if X['1287'].values > -0.005961760180070996 :
        if X['927'].values <= 0.38985230028629303 :
            if X['1105'].values > 0.09681914746761322 :
                if X['1326'].values <= -0.3352247178554535 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule145(X):
    if X['1287'].values > -0.005961760180070996 :
        if X['927'].values <= 0.38985230028629303 :
            if X['1105'].values > 0.09681914746761322 :
                if X['1326'].values > -0.3352247178554535 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule146(X):
    if X['1287'].values > -0.005961760180070996 :
        if X['927'].values > 0.38985230028629303 :
            return 0
        else:
            return -1
    else:
        return -1
def rule147(X):
    if X['1041'].values <= -0.016109599266201258 :
        if X['1032'].values <= -0.0713096559047699 :
            if X['941'].values <= 0.040622806176543236 :
                if X['1007'].values <= -0.002421872690320015 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule148(X):
    if X['1071'].values <= 0.1741170436143875 :
        if X['1559'].values <= 0.5708272308111191 :
            if X['1668'].values <= 0.3041306138038635 :
                if X['1579'].values <= -0.8414548337459564 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule149(X):
    if X['1041'].values <= -0.016109599266201258 :
        if X['1032'].values <= -0.0713096559047699 :
            if X['941'].values > 0.040622806176543236 :
                if X['1697'].values <= 0.4415910094976425 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule150(X):
    if X['1041'].values <= -0.016109599266201258 :
        if X['1032'].values > -0.0713096559047699 :
            if X['1795'].values <= -0.1686769798398018 :
                if X['1771'].values <= -0.20464690774679184 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule151(X):
    if X['1041'].values <= -0.016109599266201258 :
        if X['1032'].values > -0.0713096559047699 :
            if X['1795'].values <= -0.1686769798398018 :
                if X['1771'].values > -0.20464690774679184 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule152(X):
    if X['1041'].values <= -0.016109599266201258 :
        if X['1032'].values > -0.0713096559047699 :
            if X['1795'].values > -0.1686769798398018 :
                if X['969'].values > -0.4405817836523056 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule153(X):
    if X['1086'].values <= -0.5627769231796265 :
        if X['1037'].values > 0.7512421309947968 :
            if X['1490'].values <= -0.7437475025653839 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule154(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values <= -0.2148151397705078 :
            if X['1396'].values <= -0.12393629178404808 :
                if X['938'].values > -0.19855915009975433 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule155(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values <= -0.2148151397705078 :
            if X['1396'].values > -0.12393629178404808 :
                if X['1051'].values <= -0.1127063911408186 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule156(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values <= -0.2148151397705078 :
            if X['1396'].values > -0.12393629178404808 :
                if X['1051'].values > -0.1127063911408186 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule157(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values > -0.2148151397705078 :
            if X['1068'].values <= 0.4385979622602463 :
                if X['937'].values <= -0.1048915833234787 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule158(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values > -0.2148151397705078 :
            if X['1068'].values <= 0.4385979622602463 :
                if X['937'].values > -0.1048915833234787 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule159(X):
    if X['1041'].values > -0.016109599266201258 :
        if X['1784'].values > -0.2148151397705078 :
            if X['1068'].values > 0.4385979622602463 :
                if X['1508'].values <= 0.35245494544506073 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule160(X):
    if X['1730'].values > -0.4748941957950592 :
        if X['1085'].values > 0.05076029896736145 :
            if X['1145'].values > -0.15654096752405167 :
                if X['1341'].values <= 0.07896862924098969 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule161(X):
    if X['1809'].values <= 0.6284122169017792 :
        if X['1740'].values <= 0.11564906314015388 :
            if X['1152'].values <= 0.061794381588697433 :
                if X['1654'].values > -1.0867515802383423 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule162(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values > -0.14834225922822952 :
            if X['1364'].values > 0.2182706817984581 :
                if X['1415'].values > -0.008741214871406555 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule163(X):
    if X['1809'].values <= 0.6284122169017792 :
        if X['1740'].values <= 0.11564906314015388 :
            if X['1152'].values > 0.061794381588697433 :
                if X['1832'].values > 0.289991557598114 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule164(X):
    if X['1546'].values <= 0.28609512746334076 :
        if X['1376'].values > 0.06118115037679672 :
            if X['1408'].values > -0.17494741827249527 :
                if X['979'].values > 0.1946951225399971 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule165(X):
    if X['1809'].values <= 0.6284122169017792 :
        if X['1740'].values > 0.11564906314015388 :
            if X['1447'].values <= -0.008489894215017557 :
                if X['997'].values > -0.14414194971323013 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule166(X):
    if X['1166'].values <= -0.6067337989807129 :
        if X['1578'].values > 0.13857148215174675 :
            if X['1388'].values <= 1.2684122920036316 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule167(X):
    if X['1516'].values > -0.1886221095919609 :
        if X['1087'].values > -0.40369677543640137 :
            if X['1472'].values <= 0.12528225407004356 :
                if X['1411'].values > 0.2961541712284088 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule168(X):
    if X['1809'].values > 0.6284122169017792 :
        if X['1244'].values <= -0.8172289133071899 :
            return 1
        else:
            return -1
    else:
        return -1
def rule169(X):
    if X['1809'].values > 0.6284122169017792 :
        if X['1244'].values > -0.8172289133071899 :
            if X['1721'].values <= 0.25615768134593964 :
                if X['904'].values > -0.36440274119377136 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule170(X):
    if X['1279'].values <= -0.20372708141803741 :
        if X['1267'].values <= -0.346200630068779 :
            if X['1247'].values <= 0.12345991283655167 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule171(X):
    if X['1279'].values <= -0.20372708141803741 :
        if X['1267'].values > -0.346200630068779 :
            if X['1696'].values <= 0.07262641936540604 :
                if X['1632'].values <= 0.30863459408283234 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule172(X):
    if X['1279'].values <= -0.20372708141803741 :
        if X['1267'].values > -0.346200630068779 :
            if X['1696'].values <= 0.07262641936540604 :
                if X['1632'].values > 0.30863459408283234 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule173(X):
    if X['1279'].values <= -0.20372708141803741 :
        if X['1267'].values > -0.346200630068779 :
            if X['1696'].values > 0.07262641936540604 :
                if X['1598'].values > -0.8351075947284698 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule174(X):
    if X['1279'].values > -0.20372708141803741 :
        if X['1198'].values <= -0.22153349965810776 :
            if X['1153'].values <= 0.1589939147233963 :
                if X['1753'].values <= 0.29894885420799255 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule175(X):
    if X['1279'].values > -0.20372708141803741 :
        if X['1198'].values <= -0.22153349965810776 :
            if X['1153'].values <= 0.1589939147233963 :
                if X['1753'].values > 0.29894885420799255 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule176(X):
    if X['1279'].values > -0.20372708141803741 :
        if X['1198'].values <= -0.22153349965810776 :
            if X['1153'].values > 0.1589939147233963 :
                if X['1588'].values <= 0.6797303557395935 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule177(X):
    if X['1279'].values > -0.20372708141803741 :
        if X['1198'].values > -0.22153349965810776 :
            if X['1479'].values <= -0.6239975988864899 :
                if X['1001'].values <= -0.06159325037151575 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule178(X):
    if X['1279'].values > -0.20372708141803741 :
        if X['1198'].values > -0.22153349965810776 :
            if X['1479'].values > -0.6239975988864899 :
                if X['1668'].values <= 0.3013627827167511 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule179(X):
    if X['1740'].values <= 0.07314072176814079 :
        if X['1193'].values <= -0.4380180090665817 :
            if X['1409'].values <= -0.10180927067995071 :
                if X['1619'].values <= 0.8997723907232285 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule180(X):
    if X['1097'].values <= 0.06102407164871693 :
        if X['1496'].values <= -0.6474807560443878 :
            if X['1827'].values > -0.9977008998394012 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule181(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values <= -0.14834225922822952 :
            if X['1141'].values <= 0.0015800948604010046 :
                if X['1590'].values <= -0.8901332020759583 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule182(X):
    if X['1097'].values <= 0.06102407164871693 :
        if X['1496'].values > -0.6474807560443878 :
            if X['1016'].values <= 0.27925923466682434 :
                if X['892'].values > -0.19477514922618866 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule183(X):
    if X['1097'].values <= 0.06102407164871693 :
        if X['1496'].values > -0.6474807560443878 :
            if X['1016'].values > 0.27925923466682434 :
                if X['1120'].values <= -0.2197991982102394 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule184(X):
    if X['1097'].values <= 0.06102407164871693 :
        if X['1496'].values > -0.6474807560443878 :
            if X['1016'].values > 0.27925923466682434 :
                if X['1120'].values > -0.2197991982102394 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule185(X):
    if X['1097'].values > 0.06102407164871693 :
        if X['1487'].values <= 0.22813880443572998 :
            if X['1255'].values <= -0.359515517950058 :
                if X['1775'].values <= -0.015157511457800865 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule186(X):
    if X['1546'].values > 0.28609512746334076 :
        if X['1441'].values > -0.7323593497276306 :
            if X['1035'].values <= -0.005000709556043148 :
                if X['1165'].values <= -0.22470077127218246 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule187(X):
    if X['1097'].values > 0.06102407164871693 :
        if X['1487'].values <= 0.22813880443572998 :
            if X['1255'].values > -0.359515517950058 :
                if X['1114'].values <= 0.22234713286161423 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule188(X):
    if X['1510'].values <= 0.04307365044951439 :
        if X['1289'].values > -0.1472807228565216 :
            if X['1811'].values > -0.7304685413837433 :
                if X['1516'].values > 0.1831469088792801 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule189(X):
    if X['1097'].values > 0.06102407164871693 :
        if X['1487'].values > 0.22813880443572998 :
            if X['912'].values <= 0.6074291169643402 :
                if X['1201'].values <= 0.2733164131641388 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule190(X):
    if X['1097'].values > 0.06102407164871693 :
        if X['1487'].values > 0.22813880443572998 :
            if X['912'].values > 0.6074291169643402 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule191(X):
    if X['1760'].values <= 0.18525467067956924 :
        if X['1791'].values <= -0.8502563238143921 :
            if X['1353'].values > -0.7771152853965759 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule192(X):
    if X['969'].values > 0.2253270447254181 :
        if X['1601'].values > 0.03931504674255848 :
            if X['962'].values <= 1.2282938361167908 :
                if X['1202'].values > -0.0854422077536583 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule193(X):
    if X['1760'].values <= 0.18525467067956924 :
        if X['1791'].values > -0.8502563238143921 :
            if X['1619'].values > 0.8860809803009033 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule194(X):
    if X['1760'].values > 0.18525467067956924 :
        if X['1835'].values <= -0.4845263957977295 :
            if X['1850'].values > 0.18083350360393524 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule195(X):
    if X['1760'].values > 0.18525467067956924 :
        if X['1835'].values > -0.4845263957977295 :
            if X['1272'].values <= 0.2841021418571472 :
                if X['1072'].values <= 0.20433498173952103 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule196(X):
    if X['1172'].values > -0.4848650246858597 :
        if X['1408'].values <= -0.43629656732082367 :
            if X['1100'].values > 0.14059099927544594 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule197(X):
    if X['1760'].values > 0.18525467067956924 :
        if X['1835'].values > -0.4845263957977295 :
            if X['1272'].values > 0.2841021418571472 :
                if X['1509'].values <= 0.501838356256485 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule198(X):
    if X['1711'].values <= -0.5458879470825195 :
        if X['1554'].values <= -0.5109055638313293 :
            if X['1653'].values <= -0.5338162183761597 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule199(X):
    if X['1711'].values <= -0.5458879470825195 :
        if X['1554'].values > -0.5109055638313293 :
            if X['1364'].values <= 0.64688840508461 :
                if X['1594'].values > -1.0958219468593597 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule200(X):
    if X['1711'].values > -0.5458879470825195 :
        if X['1228'].values <= -0.6255327761173248 :
            return 0
        else:
            return -1
    else:
        return -1
def rule201(X):
    if X['1711'].values > -0.5458879470825195 :
        if X['1228'].values > -0.6255327761173248 :
            if X['1147'].values <= 0.005461958469823003 :
                if X['1753'].values <= 0.4912278652191162 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule202(X):
    if X['1711'].values > -0.5458879470825195 :
        if X['1228'].values > -0.6255327761173248 :
            if X['1147'].values > 0.005461958469823003 :
                if X['1348'].values <= -0.24955198168754578 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule203(X):
    if X['1811'].values > 0.05955618619918823 :
        if X['1478'].values > -0.509835958480835 :
            if X['1820'].values <= 0.24870947748422623 :
                if X['1647'].values > -0.19518399983644485 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule204(X):
    if X['1405'].values <= -0.016455632634460926 :
        if X['1069'].values > -0.23523180931806564 :
            if X['1326'].values <= -0.1657092198729515 :
                if X['1616'].values > -0.5212206542491913 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule205(X):
    if X['1492'].values <= -0.11617078259587288 :
        if X['1820'].values <= 0.5808486342430115 :
            if X['1723'].values <= 0.7384560406208038 :
                if X['1518'].values > -0.22697929292917252 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule206(X):
    if X['1492'].values <= -0.11617078259587288 :
        if X['1820'].values <= 0.5808486342430115 :
            if X['1723'].values > 0.7384560406208038 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule207(X):
    if X['1492'].values <= -0.11617078259587288 :
        if X['1820'].values > 0.5808486342430115 :
            if X['1012'].values <= 0.4702361971139908 :
                if X['1801'].values <= 0.25894881784915924 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule208(X):
    if X['1071'].values > 0.1741170436143875 :
        if X['1755'].values > 0.053674595430493355 :
            if X['1415'].values > 0.2549638971686363 :
                if X['1623'].values <= -0.5115970224142075 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule209(X):
    if X['1492'].values <= -0.11617078259587288 :
        if X['1820'].values > 0.5808486342430115 :
            if X['1012'].values > 0.4702361971139908 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule210(X):
    if X['1492'].values > -0.11617078259587288 :
        if X['1658'].values <= -0.07995247468352318 :
            if X['1023'].values <= -0.41753368079662323 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule211(X):
    if X['1166'].values > -0.6067337989807129 :
        if X['1060'].values <= -0.30132895708084106 :
            if X['988'].values <= 0.17419978976249695 :
                if X['1409'].values > 0.1658008024096489 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule212(X):
    if X['1492'].values > -0.11617078259587288 :
        if X['1658'].values <= -0.07995247468352318 :
            if X['1023'].values > -0.41753368079662323 :
                if X['1589'].values > -0.3581867516040802 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule213(X):
    if X['1492'].values > -0.11617078259587288 :
        if X['1658'].values > -0.07995247468352318 :
            if X['1770'].values <= 0.24474743008613586 :
                if X['1412'].values > -0.5639990270137787 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule214(X):
    if X['1492'].values > -0.11617078259587288 :
        if X['1658'].values > -0.07995247468352318 :
            if X['1770'].values > 0.24474743008613586 :
                if X['1203'].values <= -0.2725946307182312 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule215(X):
    if X['1492'].values > -0.11617078259587288 :
        if X['1658'].values > -0.07995247468352318 :
            if X['1770'].values > 0.24474743008613586 :
                if X['1203'].values > -0.2725946307182312 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule216(X):
    if X['1680'].values <= -0.021309847943484783 :
        if X['944'].values <= -0.23748890310525894 :
            if X['1743'].values <= -0.008613535203039646 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule217(X):
    if X['1680'].values <= -0.021309847943484783 :
        if X['944'].values > -0.23748890310525894 :
            if X['1615'].values <= -0.06860361061990261 :
                if X['1046'].values > -0.25614605844020844 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule218(X):
    if X['1680'].values <= -0.021309847943484783 :
        if X['944'].values > -0.23748890310525894 :
            if X['1615'].values > -0.06860361061990261 :
                if X['1469'].values > -0.44844260811805725 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule219(X):
    if X['1680'].values > -0.021309847943484783 :
        if X['1427'].values <= -0.22099659591913223 :
            if X['1768'].values <= -0.10980164632201195 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule220(X):
    if X['1680'].values > -0.021309847943484783 :
        if X['1427'].values <= -0.22099659591913223 :
            if X['1768'].values > -0.10980164632201195 :
                if X['1513'].values <= 0.23922248929738998 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule221(X):
    if X['1680'].values > -0.021309847943484783 :
        if X['1427'].values <= -0.22099659591913223 :
            if X['1768'].values > -0.10980164632201195 :
                if X['1513'].values > 0.23922248929738998 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule222(X):
    if X['1680'].values > -0.021309847943484783 :
        if X['1427'].values > -0.22099659591913223 :
            if X['1573'].values <= 0.6358416378498077 :
                if X['1488'].values <= 0.12035510689020157 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule223(X):
    if X['1510'].values <= 0.04307365044951439 :
        if X['1289'].values <= -0.1472807228565216 :
            if X['1725'].values > 0.4405781179666519 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule224(X):
    if X['1680'].values > -0.021309847943484783 :
        if X['1427'].values > -0.22099659591913223 :
            if X['1573'].values > 0.6358416378498077 :
                if X['1126'].values <= -0.09063743986189365 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule225(X):
    if X['1193'].values <= 0.6866239905357361 :
        if X['1104'].values > 1.1607000827789307 :
            if X['1138'].values <= 0.3122282549738884 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule226(X):
    if X['956'].values <= 0.5819397270679474 :
        if X['927'].values <= 0.7488552927970886 :
            if X['1096'].values <= 0.4207317382097244 :
                if X['985'].values > -0.1030019260942936 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule227(X):
    if X['956'].values <= 0.5819397270679474 :
        if X['927'].values <= 0.7488552927970886 :
            if X['1096'].values > 0.4207317382097244 :
                if X['1309'].values <= 0.06355064176023006 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule228(X):
    if X['956'].values <= 0.5819397270679474 :
        if X['927'].values <= 0.7488552927970886 :
            if X['1096'].values > 0.4207317382097244 :
                if X['1309'].values > 0.06355064176023006 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule229(X):
    if X['956'].values <= 0.5819397270679474 :
        if X['927'].values > 0.7488552927970886 :
            return 0
        else:
            return -1
    else:
        return -1
def rule230(X):
    if X['956'].values > 0.5819397270679474 :
        if X['1695'].values <= 0.3834402859210968 :
            if X['978'].values > -0.2659570351243019 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule231(X):
    if X['956'].values > 0.5819397270679474 :
        if X['1695'].values > 0.3834402859210968 :
            if X['1823'].values > -0.4729180559515953 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule232(X):
    if X['1436'].values <= 0.05182897672057152 :
        if X['1224'].values <= 0.01410852326080203 :
            if X['1567'].values <= 0.3021250516176224 :
                if X['1723'].values <= 0.10995630919933319 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule233(X):
    if X['1160'].values <= 0.7501197159290314 :
        if X['1734'].values <= -0.08429931849241257 :
            if X['1530'].values <= -0.5605514943599701 :
                if X['1831'].values <= 1.217969000339508 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule234(X):
    if X['1071'].values > 0.1741170436143875 :
        if X['1755'].values > 0.053674595430493355 :
            if X['1415'].values > 0.2549638971686363 :
                if X['1623'].values > -0.5115970224142075 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule235(X):
    if X['1436'].values <= 0.05182897672057152 :
        if X['1224'].values <= 0.01410852326080203 :
            if X['1567'].values > 0.3021250516176224 :
                if X['1746'].values > -0.27606530487537384 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule236(X):
    if X['1166'].values > -0.6067337989807129 :
        if X['1060'].values <= -0.30132895708084106 :
            if X['988'].values > 0.17419978976249695 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule237(X):
    if X['1436'].values <= 0.05182897672057152 :
        if X['1224'].values > 0.01410852326080203 :
            if X['1744'].values <= -0.11326088756322861 :
                if X['1216'].values > 0.3617410212755203 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule238(X):
    if X['1436'].values <= 0.05182897672057152 :
        if X['1224'].values > 0.01410852326080203 :
            if X['1744'].values > -0.11326088756322861 :
                if X['1174'].values <= 0.40705499053001404 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule239(X):
    if X['1436'].values <= 0.05182897672057152 :
        if X['1224'].values > 0.01410852326080203 :
            if X['1744'].values > -0.11326088756322861 :
                if X['1174'].values > 0.40705499053001404 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule240(X):
    if X['1436'].values > 0.05182897672057152 :
        if X['1573'].values <= -0.1506575495004654 :
            if X['1303'].values <= -0.20122230052947998 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule241(X):
    if X['1436'].values > 0.05182897672057152 :
        if X['1573'].values <= -0.1506575495004654 :
            if X['1303'].values > -0.20122230052947998 :
                if X['1849'].values <= 0.2099331095814705 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule242(X):
    if X['1546'].values > 0.28609512746334076 :
        if X['1441'].values > -0.7323593497276306 :
            if X['1035'].values <= -0.005000709556043148 :
                if X['1165'].values > -0.22470077127218246 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule243(X):
    if X['1436'].values > 0.05182897672057152 :
        if X['1573'].values > -0.1506575495004654 :
            if X['921'].values <= -0.34404951333999634 :
                if X['1694'].values <= 0.04470295459032059 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule244(X):
    if X['1436'].values > 0.05182897672057152 :
        if X['1573'].values > -0.1506575495004654 :
            if X['921'].values <= -0.34404951333999634 :
                if X['1694'].values > 0.04470295459032059 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule245(X):
    if X['1436'].values > 0.05182897672057152 :
        if X['1573'].values > -0.1506575495004654 :
            if X['921'].values > -0.34404951333999634 :
                if X['1539'].values <= 0.32798604667186737 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule246(X):
    if X['1294'].values <= -0.773376077413559 :
        if X['1812'].values <= 0.5384489893913269 :
            return 0
        else:
            return -1
    else:
        return -1
def rule247(X):
    if X['1348'].values > 0.18832623213529587 :
        if X['1417'].values > 0.12665515765547752 :
            if X['1759'].values <= -0.05430402792990208 :
                if X['1374'].values > -0.09861533343791962 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule248(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values <= -0.302200049161911 :
            if X['1470'].values <= -0.1210859902203083 :
                if X['1699'].values > -0.06891179457306862 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule249(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values <= -0.302200049161911 :
            if X['1470'].values > -0.1210859902203083 :
                if X['1652'].values <= -0.41466014087200165 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule250(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values <= -0.302200049161911 :
            if X['1470'].values > -0.1210859902203083 :
                if X['1652'].values > -0.41466014087200165 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule251(X):
    if X['1193'].values > 0.586669534444809 :
        if X['1800'].values <= 0.6660206019878387 :
            if X['1792'].values <= 0.07306412793695927 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule252(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values > -0.302200049161911 :
            if X['1035'].values <= 0.15897387266159058 :
                if X['1440'].values > 0.11721811443567276 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule253(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values > -0.302200049161911 :
            if X['1035'].values > 0.15897387266159058 :
                if X['1314'].values <= 0.637191891670227 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule254(X):
    if X['1294'].values > -0.773376077413559 :
        if X['1514'].values > -0.302200049161911 :
            if X['1035'].values > 0.15897387266159058 :
                if X['1314'].values > 0.637191891670227 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule255(X):
    if X['1016'].values <= 0.31172412633895874 :
        if X['1656'].values <= -0.44925037026405334 :
            if X['1473'].values <= -0.37773241102695465 :
                if X['1515'].values <= 0.3710041493177414 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule256(X):
    if X['1016'].values <= 0.31172412633895874 :
        if X['1656'].values <= -0.44925037026405334 :
            if X['1473'].values > -0.37773241102695465 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule257(X):
    if X['1016'].values <= 0.31172412633895874 :
        if X['1656'].values > -0.44925037026405334 :
            if X['1701'].values <= -0.3320546895265579 :
                if X['1154'].values <= 0.18622541427612305 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule258(X):
    if X['969'].values <= 0.2253270447254181 :
        if X['1581'].values <= -0.04873348027467728 :
            if X['1027'].values > -0.2311115562915802 :
                if X['1066'].values > -0.27603040635585785 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule259(X):
    if X['1016'].values <= 0.31172412633895874 :
        if X['1656'].values > -0.44925037026405334 :
            if X['1701'].values > -0.3320546895265579 :
                if X['1299'].values <= -0.6476370394229889 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule260(X):
    if X['1016'].values > 0.31172412633895874 :
        if X['1101'].values <= 0.022125051822513342 :
            if X['1157'].values <= -0.5016895681619644 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule261(X):
    if X['1016'].values > 0.31172412633895874 :
        if X['1101'].values <= 0.022125051822513342 :
            if X['1157'].values > -0.5016895681619644 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule262(X):
    if X['1016'].values > 0.31172412633895874 :
        if X['1101'].values > 0.022125051822513342 :
            if X['1780'].values > -0.38127417862415314 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule263(X):
    if X['1740'].values <= 0.07314072176814079 :
        if X['1193'].values <= -0.4380180090665817 :
            if X['1409'].values > -0.10180927067995071 :
                if X['1506'].values <= -0.3966534286737442 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule264(X):
    if X['1627'].values <= 0.21037500351667404 :
        if X['1588'].values <= 0.027653560042381287 :
            if X['896'].values <= -0.051698001101613045 :
                if X['910'].values > 0.15115121752023697 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule265(X):
    if X['1627'].values <= 0.21037500351667404 :
        if X['1588'].values <= 0.027653560042381287 :
            if X['896'].values > -0.051698001101613045 :
                if X['1774'].values <= 0.23031766712665558 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule266(X):
    if X['1627'].values <= 0.21037500351667404 :
        if X['1588'].values <= 0.027653560042381287 :
            if X['896'].values > -0.051698001101613045 :
                if X['1774'].values > 0.23031766712665558 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule267(X):
    if X['1627'].values <= 0.21037500351667404 :
        if X['1588'].values > 0.027653560042381287 :
            if X['1806'].values <= 0.26222531497478485 :
                if X['1756'].values <= 0.29747113585472107 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule268(X):
    if X['1774'].values > 0.08726129680871964 :
        if X['1299'].values > -0.2870655953884125 :
            if X['1784'].values <= -0.2339148372411728 :
                if X['1746'].values <= 0.15306952595710754 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule269(X):
    if X['1627'].values <= 0.21037500351667404 :
        if X['1588'].values > 0.027653560042381287 :
            if X['1806'].values > 0.26222531497478485 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule270(X):
    if X['1627'].values > 0.21037500351667404 :
        if X['1384'].values <= -0.12747373431921005 :
            if X['888'].values <= -0.27364955842494965 :
                if X['1401'].values <= 0.08143254928290844 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule271(X):
    if X['1627'].values > 0.21037500351667404 :
        if X['1384'].values <= -0.12747373431921005 :
            if X['888'].values <= -0.27364955842494965 :
                if X['1401'].values > 0.08143254928290844 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule272(X):
    if X['1627'].values > 0.21037500351667404 :
        if X['1384'].values <= -0.12747373431921005 :
            if X['888'].values > -0.27364955842494965 :
                if X['1418'].values <= 0.46374621987342834 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule273(X):
    if X['1627'].values > 0.21037500351667404 :
        if X['1384'].values > -0.12747373431921005 :
            if X['1673'].values <= 0.5032964795827866 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule274(X):
    if X['956'].values <= 0.5430828332901001 :
        if X['1023'].values <= 0.2946911156177521 :
            if X['1321'].values <= 1.3844929933547974 :
                if X['1730'].values <= -0.5133714377880096 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule275(X):
    if X['1463'].values <= 0.012233572080731392 :
        if X['914'].values <= 0.25664985179901123 :
            if X['1470'].values <= 0.1642487421631813 :
                if X['1607'].values > -0.029373849742114544 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule276(X):
    if X['1463'].values <= 0.012233572080731392 :
        if X['914'].values <= 0.25664985179901123 :
            if X['1470'].values > 0.1642487421631813 :
                if X['1323'].values <= 0.49153895676136017 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule277(X):
    if X['1463'].values <= 0.012233572080731392 :
        if X['914'].values > 0.25664985179901123 :
            if X['1374'].values > -0.40093226730823517 :
                if X['1347'].values <= 0.20318301767110825 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule278(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values <= -0.14834225922822952 :
            if X['1141'].values <= 0.0015800948604010046 :
                if X['1590'].values > -0.8901332020759583 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule279(X):
    if X['1463'].values > 0.012233572080731392 :
        if X['1823'].values <= 0.3311362862586975 :
            if X['1556'].values <= -0.335096150636673 :
                if X['1335'].values <= -0.015331570524722338 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule280(X):
    if X['1463'].values > 0.012233572080731392 :
        if X['1823'].values <= 0.3311362862586975 :
            if X['1556'].values <= -0.335096150636673 :
                if X['1335'].values > -0.015331570524722338 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule281(X):
    if X['1463'].values > 0.012233572080731392 :
        if X['1823'].values <= 0.3311362862586975 :
            if X['1556'].values > -0.335096150636673 :
                if X['1528'].values <= 0.22028640657663345 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule282(X):
    if X['1740'].values <= 0.07314072176814079 :
        if X['1193'].values <= -0.4380180090665817 :
            if X['1409'].values > -0.10180927067995071 :
                if X['1506'].values > -0.3966534286737442 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule283(X):
    if X['1463'].values > 0.012233572080731392 :
        if X['1823'].values > 0.3311362862586975 :
            return 0
        else:
            return -1
    else:
        return -1
def rule284(X):
    if X['1735'].values <= -0.2548443377017975 :
        if X['1398'].values <= -0.46906909346580505 :
            if X['1551'].values <= 0.3052182048559189 :
                if X['886'].values > -0.34759385883808136 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule285(X):
    if X['1735'].values <= -0.2548443377017975 :
        if X['1398'].values > -0.46906909346580505 :
            if X['1013'].values <= -0.21355468034744263 :
                if X['1260'].values <= -0.26937583088874817 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule286(X):
    if X['1735'].values <= -0.2548443377017975 :
        if X['1398'].values > -0.46906909346580505 :
            if X['1013'].values <= -0.21355468034744263 :
                if X['1260'].values > -0.26937583088874817 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule287(X):
    if X['1735'].values <= -0.2548443377017975 :
        if X['1398'].values > -0.46906909346580505 :
            if X['1013'].values > -0.21355468034744263 :
                if X['1842'].values > -0.16451150923967361 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule288(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values <= -0.1362350806593895 :
            if X['1246'].values <= 0.07223209366202354 :
                if X['1575'].values <= 0.45728346705436707 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule289(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values <= -0.1362350806593895 :
            if X['1246'].values <= 0.07223209366202354 :
                if X['1575'].values > 0.45728346705436707 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule290(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values <= -0.1362350806593895 :
            if X['1246'].values > 0.07223209366202354 :
                if X['1228'].values <= 0.031689515337347984 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule291(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values <= -0.1362350806593895 :
            if X['1246'].values > 0.07223209366202354 :
                if X['1228'].values > 0.031689515337347984 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule292(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values > -0.1362350806593895 :
            if X['1674'].values <= -0.7951794862747192 :
                if X['1136'].values <= -0.10951852798461914 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule293(X):
    if X['1510'].values > 0.04307365044951439 :
        if X['1672'].values <= 0.3931408226490021 :
            if X['1114'].values <= 0.12630541622638702 :
                if X['1305'].values > -0.26246626675128937 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule294(X):
    if X['1735'].values > -0.2548443377017975 :
        if X['1078'].values > -0.1362350806593895 :
            if X['1674'].values > -0.7951794862747192 :
                if X['1409'].values <= 0.13507572561502457 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule295(X):
    if X['892'].values > -0.23184429854154587 :
        if X['1642'].values <= 0.7493916153907776 :
            if X['1809'].values > 0.6284122169017792 :
                if X['1043'].values <= 0.12012064829468727 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule296(X):
    if X['1348'].values > 0.18832623213529587 :
        if X['1417'].values <= 0.12665515765547752 :
            if X['1739'].values <= 0.7949975728988647 :
                if X['1315'].values > -0.28419772535562515 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule297(X):
    if X['1068'].values <= 0.4275039732456207 :
        if X['1569'].values <= -0.12332960218191147 :
            if X['1210'].values <= -0.10430929437279701 :
                if X['1284'].values > -0.27863918244838715 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule298(X):
    if X['1068'].values <= 0.4275039732456207 :
        if X['1569'].values <= -0.12332960218191147 :
            if X['1210'].values > -0.10430929437279701 :
                if X['1449'].values > -0.51885586977005 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule299(X):
    if X['1035'].values > 0.1232370100915432 :
        if X['967'].values <= 0.13804049044847488 :
            if X['1076'].values <= 0.2248997688293457 :
                if X['1408'].values > -0.2035047709941864 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule300(X):
    if X['1068'].values <= 0.4275039732456207 :
        if X['1569'].values > -0.12332960218191147 :
            if X['1827'].values <= 0.33654481172561646 :
                if X['1191'].values > 0.20759377628564835 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule301(X):
    if X['1068'].values <= 0.4275039732456207 :
        if X['1569'].values > -0.12332960218191147 :
            if X['1827'].values > 0.33654481172561646 :
                if X['1587'].values <= -0.13134977221488953 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule302(X):
    if X['1068'].values <= 0.4275039732456207 :
        if X['1569'].values > -0.12332960218191147 :
            if X['1827'].values > 0.33654481172561646 :
                if X['1587'].values > -0.13134977221488953 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule303(X):
    if X['1068'].values > 0.4275039732456207 :
        if X['1854'].values > -0.7646317780017853 :
            if X['1024'].values > -0.8494897186756134 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule304(X):
    if X['1690'].values <= -0.5683086812496185 :
        if X['1208'].values <= -0.03719882294535637 :
            if X['960'].values > -0.10632361099123955 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule305(X):
    if X['1690'].values <= -0.5683086812496185 :
        if X['1208'].values > -0.03719882294535637 :
            return 0
        else:
            return -1
    else:
        return -1
def rule306(X):
    if X['1690'].values > -0.5683086812496185 :
        if X['1009'].values <= -0.32507947087287903 :
            if X['1150'].values <= 0.4568197578191757 :
                if X['1528'].values <= 0.32840438187122345 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule307(X):
    if X['1690'].values > -0.5683086812496185 :
        if X['1009'].values <= -0.32507947087287903 :
            if X['1150'].values > 0.4568197578191757 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule308(X):
    if X['1690'].values > -0.5683086812496185 :
        if X['1009'].values > -0.32507947087287903 :
            if X['1670'].values <= -0.07067076861858368 :
                if X['1772'].values <= -0.27583345770835876 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule309(X):
    if X['1811'].values > 0.05955618619918823 :
        if X['1478'].values > -0.509835958480835 :
            if X['1820'].values > 0.24870947748422623 :
                if X['1578'].values <= 0.6642657518386841 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule310(X):
    if X['1690'].values > -0.5683086812496185 :
        if X['1009'].values > -0.32507947087287903 :
            if X['1670'].values > -0.07067076861858368 :
                if X['1621'].values <= 0.546337366104126 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule311(X):
    if X['1361'].values <= -0.45906655490398407 :
        if X['1685'].values <= 0.16758941113948822 :
            return 0
        else:
            return -1
    else:
        return -1
def rule312(X):
    if X['1361'].values > -0.45906655490398407 :
        if X['896'].values <= -0.05297652445733547 :
            if X['1483'].values <= 0.44066792726516724 :
                if X['1716'].values <= -0.08786826580762863 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule313(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values <= -0.14834225922822952 :
            if X['1141'].values > 0.0015800948604010046 :
                if X['1360'].values <= -0.17605017125606537 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule314(X):
    if X['1361'].values > -0.45906655490398407 :
        if X['896'].values <= -0.05297652445733547 :
            if X['1483'].values > 0.44066792726516724 :
                if X['1124'].values > -0.2359664887189865 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule315(X):
    if X['1740'].values <= 0.07314072176814079 :
        if X['1193'].values > -0.4380180090665817 :
            if X['1333'].values <= 1.0032313466072083 :
                if X['1380'].values <= 0.4693813621997833 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule316(X):
    if X['1361'].values > -0.45906655490398407 :
        if X['896'].values > -0.05297652445733547 :
            if X['1584'].values > 0.43953633308410645 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule317(X):
    if X['1097'].values <= 0.06546211987733841 :
        if X['1818'].values <= -0.13366997241973877 :
            if X['958'].values <= -0.1853528916835785 :
                if X['1550'].values <= -0.1868571639060974 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule318(X):
    if X['969'].values > 0.2253270447254181 :
        if X['1601'].values > 0.03931504674255848 :
            if X['962'].values > 1.2282938361167908 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule319(X):
    if X['1097'].values <= 0.06546211987733841 :
        if X['1818'].values <= -0.13366997241973877 :
            if X['958'].values > -0.1853528916835785 :
                if X['1735'].values > -1.1927841305732727 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule320(X):
    if X['1097'].values <= 0.06546211987733841 :
        if X['1818'].values > -0.13366997241973877 :
            if X['1742'].values <= 0.2937531918287277 :
                if X['1015'].values <= 0.5850287079811096 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule321(X):
    if X['1774'].values > 0.08726129680871964 :
        if X['1299'].values > -0.2870655953884125 :
            if X['1784'].values > -0.2339148372411728 :
                if X['1711'].values > -0.10797202587127686 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule322(X):
    if X['1097'].values <= 0.06546211987733841 :
        if X['1818'].values > -0.13366997241973877 :
            if X['1742'].values > 0.2937531918287277 :
                if X['1140'].values <= -0.14523810148239136 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule323(X):
    if X['1160'].values > 0.7501197159290314 :
        return 0
    else:
        return -1
def rule324(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values <= -0.14834225922822952 :
            if X['1141'].values > 0.0015800948604010046 :
                if X['1360'].values > -0.17605017125606537 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule325(X):
    if X['1097'].values > 0.06546211987733841 :
        if X['1822'].values <= 0.1892431676387787 :
            if X['1329'].values <= -0.14028165861964226 :
                if X['1436'].values > -0.03170011518523097 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule326(X):
    if X['1097'].values > 0.06546211987733841 :
        if X['1822'].values <= 0.1892431676387787 :
            if X['1329'].values > -0.14028165861964226 :
                if X['1700'].values <= 0.08659837767481804 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule327(X):
    if X['1035'].values <= 0.1232370100915432 :
        if X['1417'].values > -0.21825718879699707 :
            if X['898'].values <= -0.020045855082571507 :
                if X['1578'].values > 0.6154966652393341 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule328(X):
    if X['1097'].values > 0.06546211987733841 :
        if X['1822'].values > 0.1892431676387787 :
            if X['1855'].values <= -0.2992355078458786 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule329(X):
    if X['1097'].values > 0.06546211987733841 :
        if X['1822'].values > 0.1892431676387787 :
            if X['1855'].values > -0.2992355078458786 :
                if X['1766'].values <= 0.9821227788925171 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule330(X):
    if X['1228'].values <= -0.19522958248853683 :
        if X['1517'].values <= 0.1539703905582428 :
            if X['1627'].values <= 0.019058861769735813 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule331(X):
    if X['1228'].values <= -0.19522958248853683 :
        if X['1517'].values <= 0.1539703905582428 :
            if X['1627'].values > 0.019058861769735813 :
                if X['1665'].values <= -0.03871040418744087 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule332(X):
    if X['1228'].values <= -0.19522958248853683 :
        if X['1517'].values <= 0.1539703905582428 :
            if X['1627'].values > 0.019058861769735813 :
                if X['1665'].values > -0.03871040418744087 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule333(X):
    if X['1228'].values <= -0.19522958248853683 :
        if X['1517'].values > 0.1539703905582428 :
            if X['1302'].values <= 0.2380594238638878 :
                if X['1015'].values > -0.5810126662254333 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule334(X):
    if X['1228'].values <= -0.19522958248853683 :
        if X['1517'].values > 0.1539703905582428 :
            if X['1302'].values > 0.2380594238638878 :
                if X['1575'].values > 0.03421789966523647 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule335(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values > -0.14834225922822952 :
            if X['1364'].values <= 0.2182706817984581 :
                if X['895'].values <= 0.35143494606018066 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule336(X):
    if X['1172'].values <= -0.4848650246858597 :
        if X['1685'].values <= 0.7254676669836044 :
            if X['973'].values <= 0.6695645153522491 :
                if X['1737'].values > -2.137048065662384 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule337(X):
    if X['1228'].values > -0.19522958248853683 :
        if X['1250'].values <= 0.5345847606658936 :
            if X['1505'].values > 0.07237522304058075 :
                if X['1282'].values > -0.09018829092383385 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule338(X):
    if X['1228'].values > -0.19522958248853683 :
        if X['1250'].values > 0.5345847606658936 :
            return 0
        else:
            return -1
    else:
        return -1
def rule339(X):
    if X['1632'].values <= -0.07305720821022987 :
        if X['1660'].values <= -0.00670415663626045 :
            if X['1672'].values <= 0.35357166826725006 :
                if X['1623'].values <= 0.6204581558704376 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule340(X):
    if X['1632'].values <= -0.07305720821022987 :
        if X['1660'].values <= -0.00670415663626045 :
            if X['1672'].values > 0.35357166826725006 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule341(X):
    if X['1559'].values <= 0.2724491357803345 :
        if X['1587'].values <= -0.28243719041347504 :
            if X['936'].values <= 0.023608227260410786 :
                if X['1388'].values <= -0.07132188975811005 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule342(X):
    if X['1632'].values <= -0.07305720821022987 :
        if X['1660'].values > -0.00670415663626045 :
            if X['1442'].values <= -0.4654507339000702 :
                if X['1085'].values > 0.06636635959148407 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule343(X):
    if X['1632'].values <= -0.07305720821022987 :
        if X['1660'].values > -0.00670415663626045 :
            if X['1442'].values > -0.4654507339000702 :
                if X['1102'].values <= -0.4185712933540344 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule344(X):
    if X['1632'].values <= -0.07305720821022987 :
        if X['1660'].values > -0.00670415663626045 :
            if X['1442'].values > -0.4654507339000702 :
                if X['1102'].values > -0.4185712933540344 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule345(X):
    if X['1172'].values <= -0.4848650246858597 :
        if X['1685'].values > 0.7254676669836044 :
            return 1
        else:
            return -1
    else:
        return -1
def rule346(X):
    if X['1632'].values > -0.07305720821022987 :
        if X['1180'].values <= 0.2629270702600479 :
            if X['1280'].values <= 0.2792455703020096 :
                if X['1019'].values > -0.1666509285569191 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule347(X):
    if X['1632'].values > -0.07305720821022987 :
        if X['1180'].values <= 0.2629270702600479 :
            if X['1280'].values > 0.2792455703020096 :
                if X['1496'].values <= -0.23377199470996857 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule348(X):
    if X['1546'].values > 0.28609512746334076 :
        if X['1441'].values > -0.7323593497276306 :
            if X['1035'].values > -0.005000709556043148 :
                if X['920'].values <= -0.20607272535562515 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule349(X):
    if X['1632'].values > -0.07305720821022987 :
        if X['1180'].values > 0.2629270702600479 :
            if X['1103'].values <= 0.08200760930776596 :
                if X['1494'].values <= 0.2891383767127991 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule350(X):
    if X['1559'].values <= 0.2724491357803345 :
        if X['1587'].values <= -0.28243719041347504 :
            if X['936'].values <= 0.023608227260410786 :
                if X['1388'].values > -0.07132188975811005 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule351(X):
    if X['1632'].values > -0.07305720821022987 :
        if X['1180'].values > 0.2629270702600479 :
            if X['1103'].values > 0.08200760930776596 :
                if X['1438'].values > -0.14603571966290474 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule352(X):
    if X['1512'].values <= 0.7980414628982544 :
        if X['1823'].values <= 0.23980090022087097 :
            if X['1455'].values <= 0.18269654363393784 :
                if X['1528'].values <= 0.2851852476596832 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule353(X):
    if X['1405'].values <= -0.016455632634460926 :
        if X['1069'].values <= -0.23523180931806564 :
            if X['1134'].values > -1.523268699645996 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule354(X):
    if X['1512'].values <= 0.7980414628982544 :
        if X['1823'].values <= 0.23980090022087097 :
            if X['1455'].values > 0.18269654363393784 :
                if X['1482'].values <= 0.3390226513147354 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule355(X):
    if X['1516'].values > -0.1886221095919609 :
        if X['1087'].values > -0.40369677543640137 :
            if X['1472'].values > 0.12528225407004356 :
                if X['1041'].values <= -0.14502554386854172 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule356(X):
    if X['1512'].values <= 0.7980414628982544 :
        if X['1823'].values > 0.23980090022087097 :
            if X['1811'].values <= -0.34404291212558746 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule357(X):
    if X['1512'].values <= 0.7980414628982544 :
        if X['1823'].values > 0.23980090022087097 :
            if X['1811'].values > -0.34404291212558746 :
                if X['918'].values <= 0.03266645595431328 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule358(X):
    if X['1559'].values <= 0.2724491357803345 :
        if X['1587'].values <= -0.28243719041347504 :
            if X['936'].values > 0.023608227260410786 :
                if X['1369'].values > -0.19123321026563644 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule359(X):
    if X['1512'].values > 0.7980414628982544 :
        if X['1740'].values > -0.5949006378650665 :
            if X['1588'].values <= 0.1928127221763134 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule360(X):
    if X['1673'].values <= -0.591812252998352 :
        if X['1393'].values <= -0.047489766497164965 :
            return 0
        else:
            return -1
    else:
        return -1
def rule361(X):
    if X['1673'].values <= -0.591812252998352 :
        if X['1393'].values > -0.047489766497164965 :
            if X['1068'].values <= -0.11701679602265358 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule362(X):
    if X['1673'].values <= -0.591812252998352 :
        if X['1393'].values > -0.047489766497164965 :
            if X['1068'].values > -0.11701679602265358 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule363(X):
    if X['1673'].values > -0.591812252998352 :
        if X['1097'].values <= 0.05689382366836071 :
            if X['1294'].values <= -0.7964145243167877 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule364(X):
    if X['1673'].values > -0.591812252998352 :
        if X['1097'].values > 0.05689382366836071 :
            if X['1027'].values <= -0.09035604819655418 :
                if X['1093'].values <= 0.9051268994808197 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule365(X):
    if X['1673'].values > -0.591812252998352 :
        if X['1097'].values > 0.05689382366836071 :
            if X['1027'].values > -0.09035604819655418 :
                if X['1012'].values <= 0.3587073087692261 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule366(X):
    if X['1673'].values > -0.591812252998352 :
        if X['1097'].values > 0.05689382366836071 :
            if X['1027'].values > -0.09035604819655418 :
                if X['1012'].values > 0.3587073087692261 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule367(X):
    if X['1305'].values <= 0.6613623201847076 :
        if X['1451'].values <= -0.11140647158026695 :
            if X['1771'].values <= -0.5290951728820801 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule368(X):
    if X['1305'].values <= 0.6613623201847076 :
        if X['1451'].values <= -0.11140647158026695 :
            if X['1771'].values > -0.5290951728820801 :
                if X['1776'].values <= 0.2727428078651428 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule369(X):
    if X['1305'].values <= 0.6613623201847076 :
        if X['1451'].values <= -0.11140647158026695 :
            if X['1771'].values > -0.5290951728820801 :
                if X['1776'].values > 0.2727428078651428 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule370(X):
    if X['892'].values > -0.23184429854154587 :
        if X['1642'].values > 0.7493916153907776 :
            if X['1514'].values <= -0.9416533708572388 :
                if X['1838'].values > 0.1784044411033392 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule371(X):
    if X['1305'].values <= 0.6613623201847076 :
        if X['1451'].values > -0.11140647158026695 :
            if X['1161'].values <= -0.14783930033445358 :
                if X['1695'].values > 0.25128354132175446 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule372(X):
    if X['1035'].values > 0.1232370100915432 :
        if X['967'].values <= 0.13804049044847488 :
            if X['1076'].values > 0.2248997688293457 :
                if X['1157'].values > -0.26072270423173904 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule373(X):
    if X['1305'].values <= 0.6613623201847076 :
        if X['1451'].values > -0.11140647158026695 :
            if X['1161'].values > -0.14783930033445358 :
                if X['1320'].values > -0.07853835821151733 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule374(X):
    if X['1305'].values > 0.6613623201847076 :
        if X['1794'].values <= 0.5616863369941711 :
            if X['1094'].values > -1.1271705627441406 :
                if X['1045'].values > -0.6029950380325317 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule375(X):
    if X['1305'].values > 0.6613623201847076 :
        if X['1794'].values > 0.5616863369941711 :
            return 1
        else:
            return -1
    else:
        return -1
def rule376(X):
    if X['1361'].values <= -0.34174664318561554 :
        if X['1104'].values <= -0.02494062576442957 :
            if X['1708'].values <= 0.7447223365306854 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule377(X):
    if X['1361'].values <= -0.34174664318561554 :
        if X['1104'].values > -0.02494062576442957 :
            if X['1488'].values <= -0.1539316028356552 :
                if X['1692'].values <= 0.07246431894600391 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule378(X):
    if X['1361'].values <= -0.34174664318561554 :
        if X['1104'].values > -0.02494062576442957 :
            if X['1488'].values > -0.1539316028356552 :
                if X['1325'].values <= 0.10741659253835678 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule379(X):
    if X['1740'].values <= 0.07314072176814079 :
        if X['1193'].values > -0.4380180090665817 :
            if X['1333'].values > 1.0032313466072083 :
                if X['1857'].values <= 0.33973201364278793 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule380(X):
    if X['1361'].values > -0.34174664318561554 :
        if X['1606'].values <= 0.11599013954401016 :
            if X['1048'].values <= -0.1084006205201149 :
                if X['961'].values <= 0.12751827016472816 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule381(X):
    if X['1361'].values > -0.34174664318561554 :
        if X['1606'].values <= 0.11599013954401016 :
            if X['1048'].values <= -0.1084006205201149 :
                if X['961'].values > 0.12751827016472816 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule382(X):
    if X['1130'].values <= -0.48629245162010193 :
        return 0
    else:
        return -1
def rule383(X):
    if X['1361'].values > -0.34174664318561554 :
        if X['1606'].values <= 0.11599013954401016 :
            if X['1048'].values > -0.1084006205201149 :
                if X['1605'].values > -0.19365194439888 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule384(X):
    if X['1361'].values > -0.34174664318561554 :
        if X['1606'].values > 0.11599013954401016 :
            if X['1566'].values <= -0.39567936956882477 :
                if X['1079'].values <= -0.046990491449832916 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule385(X):
    if X['1130'].values > -0.48629245162010193 :
        if X['1553'].values <= -0.06097067520022392 :
            if X['942'].values <= -0.46272018551826477 :
                if X['1682'].values <= -0.32596616446971893 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule386(X):
    if X['1361'].values > -0.34174664318561554 :
        if X['1606'].values > 0.11599013954401016 :
            if X['1566'].values > -0.39567936956882477 :
                if X['1714'].values > -0.23235295712947845 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule387(X):
    if X['1546'].values <= 0.28609512746334076 :
        if X['1376'].values <= 0.06118115037679672 :
            if X['1444'].values <= -0.14607463777065277 :
                if X['1584'].values <= 0.12346063181757927 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule388(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values <= 0.17797519266605377 :
            if X['1399'].values <= -0.3357475697994232 :
                if X['1550'].values > -0.014155378332361579 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule389(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values <= 0.17797519266605377 :
            if X['1399'].values > -0.3357475697994232 :
                if X['909'].values <= -0.6153547763824463 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule390(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values <= 0.17797519266605377 :
            if X['1399'].values > -0.3357475697994232 :
                if X['909'].values > -0.6153547763824463 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule391(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values > 0.17797519266605377 :
            if X['1661'].values <= 0.33768226206302643 :
                if X['1684'].values <= 0.3187038153409958 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule392(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values > 0.17797519266605377 :
            if X['1661'].values <= 0.33768226206302643 :
                if X['1684'].values > 0.3187038153409958 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule393(X):
    if X['1532'].values <= 0.37424980103969574 :
        if X['1488'].values > 0.17797519266605377 :
            if X['1661'].values > 0.33768226206302643 :
                if X['1134'].values <= 0.15002040937542915 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule394(X):
    if X['1532'].values > 0.37424980103969574 :
        if X['1806'].values <= -0.17097660899162292 :
            if X['1684'].values > -2.2230209708213806 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule395(X):
    if X['1532'].values > 0.37424980103969574 :
        if X['1806'].values > -0.17097660899162292 :
            if X['980'].values <= 0.18838252872228622 :
                if X['1318'].values <= -0.2810126766562462 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule396(X):
    if X['1559'].values <= 0.2724491357803345 :
        if X['1587'].values > -0.28243719041347504 :
            if X['884'].values <= -0.17674176394939423 :
                if X['1386'].values <= 0.10812646895647049 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule397(X):
    if X['1532'].values > 0.37424980103969574 :
        if X['1806'].values > -0.17097660899162292 :
            if X['980'].values > 0.18838252872228622 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule398(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values <= 0.2930496335029602 :
            if X['891'].values <= 0.23057081550359726 :
                if X['959'].values <= 0.12256622314453125 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule399(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values <= 0.2930496335029602 :
            if X['891'].values <= 0.23057081550359726 :
                if X['959'].values > 0.12256622314453125 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule400(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values <= 0.2930496335029602 :
            if X['891'].values > 0.23057081550359726 :
                if X['1139'].values <= -0.055756811052560806 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule401(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values <= 0.2930496335029602 :
            if X['891'].values > 0.23057081550359726 :
                if X['1139'].values > -0.055756811052560806 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule402(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values > 0.2930496335029602 :
            if X['1234'].values <= 0.14284352213144302 :
                if X['1681'].values <= -0.022941450588405132 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule403(X):
    if X['956'].values <= 0.5430828332901001 :
        if X['1023'].values > 0.2946911156177521 :
            if X['1401'].values > -0.40008221566677094 :
                if X['1707'].values <= 0.03734876401722431 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule404(X):
    if X['1559'].values <= 0.2724491357803345 :
        if X['1587'].values > -0.28243719041347504 :
            if X['884'].values <= -0.17674176394939423 :
                if X['1386'].values > 0.10812646895647049 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule405(X):
    if X['1828'].values <= 0.7313120067119598 :
        if X['952'].values > 0.2930496335029602 :
            if X['1234'].values > 0.14284352213144302 :
                if X['995'].values > 0.033235878217965364 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule406(X):
    if X['1828'].values > 0.7313120067119598 :
        if X['1151'].values <= -0.28419265151023865 :
            if X['1055'].values > -0.198553204536438 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule407(X):
    if X['1828'].values > 0.7313120067119598 :
        if X['1151'].values > -0.28419265151023865 :
            return 0
        else:
            return -1
    else:
        return -1
def rule408(X):
    if X['1571'].values <= -1.1267082691192627 :
        return 0
    else:
        return -1
def rule409(X):
    if X['1571'].values > -1.1267082691192627 :
        if X['1095'].values <= -0.18271463364362717 :
            if X['1553'].values <= 0.8671496212482452 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule410(X):
    if X['1071'].values > 0.1741170436143875 :
        if X['1755'].values > 0.053674595430493355 :
            if X['1415'].values <= 0.2549638971686363 :
                if X['1434'].values <= -0.4745222181081772 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule411(X):
    if X['1348'].values > 0.18832623213529587 :
        if X['1417'].values > 0.12665515765547752 :
            if X['1759'].values > -0.05430402792990208 :
                if X['1115'].values <= 0.29723672568798065 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule412(X):
    if X['1740'].values > 0.07314072176814079 :
        if X['1626'].values <= -0.45415909588336945 :
            return 0
        else:
            return -1
    else:
        return -1
def rule413(X):
    if X['1571'].values > -1.1267082691192627 :
        if X['1095'].values > -0.18271463364362717 :
            if X['1035'].values > 0.14994215965270996 :
                if X['1569'].values > -0.12312113121151924 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule414(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values <= -0.0522276870906353 :
            if X['1654'].values <= -0.219225212931633 :
                if X['1557'].values <= 0.30084339529275894 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule415(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values <= -0.0522276870906353 :
            if X['1654'].values <= -0.219225212931633 :
                if X['1557'].values > 0.30084339529275894 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule416(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values <= -0.0522276870906353 :
            if X['1654'].values > -0.219225212931633 :
                if X['965'].values <= 0.2978109046816826 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule417(X):
    if X['1534'].values > 0.21067752689123154 :
        if X['1700'].values > 0.19715777784585953 :
            if X['1717'].values > 0.5089736878871918 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule418(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values > -0.0522276870906353 :
            if X['1804'].values <= -0.08104617148637772 :
                if X['1372'].values > -0.2908226549625397 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule419(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values > -0.0522276870906353 :
            if X['1804'].values > -0.08104617148637772 :
                if X['1484'].values <= 0.013427454978227615 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule420(X):
    if X['1632'].values <= 0.17050549387931824 :
        if X['939'].values > -0.0522276870906353 :
            if X['1804'].values > -0.08104617148637772 :
                if X['1484'].values > 0.013427454978227615 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule421(X):
    if X['1632'].values > 0.17050549387931824 :
        if X['1406'].values <= 0.2951793521642685 :
            if X['1499'].values <= -0.42563074827194214 :
                if X['914'].values > -0.19307885318994522 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule422(X):
    if X['1632'].values > 0.17050549387931824 :
        if X['1406'].values <= 0.2951793521642685 :
            if X['1499'].values > -0.42563074827194214 :
                if X['1570'].values > -0.5162115693092346 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule423(X):
    if X['1632'].values > 0.17050549387931824 :
        if X['1406'].values > 0.2951793521642685 :
            if X['1403'].values <= -0.1718229502439499 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule424(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values <= -0.05860229954123497 :
            if X['1131'].values <= 0.4954347312450409 :
                if X['1233'].values <= -0.480156809091568 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule425(X):
    if X['1246'].values <= 0.2591703087091446 :
        if X['1547'].values <= -0.5136916935443878 :
            if X['1792'].values <= 0.31844407320022583 :
                if X['1360'].values > 0.10545640625059605 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule426(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values <= -0.05860229954123497 :
            if X['1131'].values <= 0.4954347312450409 :
                if X['1233'].values > -0.480156809091568 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule427(X):
    if X['1246'].values <= 0.2591703087091446 :
        if X['1547'].values <= -0.5136916935443878 :
            if X['1792'].values > 0.31844407320022583 :
                if X['1067'].values > 0.05732277035713196 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule428(X):
    if X['1246'].values <= 0.2591703087091446 :
        if X['1547'].values > -0.5136916935443878 :
            if X['991'].values <= -0.8977497816085815 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule429(X):
    if X['1534'].values <= 0.21067752689123154 :
        if X['1537'].values <= 1.5543000102043152 :
            if X['1316'].values <= 0.3903924524784088 :
                if X['1833'].values > 0.3484857380390167 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule430(X):
    if X['1246'].values <= 0.2591703087091446 :
        if X['1547'].values > -0.5136916935443878 :
            if X['991'].values > -0.8977497816085815 :
                if X['900'].values > -0.2692718803882599 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule431(X):
    if X['1246'].values > 0.2591703087091446 :
        if X['1174'].values <= 0.8138917684555054 :
            if X['1833'].values <= -0.38081343472003937 :
                if X['1761'].values > -1.039657935500145 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule432(X):
    if X['1246'].values > 0.2591703087091446 :
        if X['1174'].values <= 0.8138917684555054 :
            if X['1833'].values > -0.38081343472003937 :
                if X['1109'].values <= -0.157852441072464 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule433(X):
    if X['1246'].values > 0.2591703087091446 :
        if X['1174'].values <= 0.8138917684555054 :
            if X['1833'].values > -0.38081343472003937 :
                if X['1109'].values > -0.157852441072464 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule434(X):
    if X['1246'].values > 0.2591703087091446 :
        if X['1174'].values > 0.8138917684555054 :
            return 1
        else:
            return -1
    else:
        return -1
def rule435(X):
    if X['1822'].values <= 0.03600536473095417 :
        if X['1296'].values <= 0.8821878135204315 :
            if X['1489'].values <= -0.19563139975070953 :
                if X['1347'].values <= -0.10421553254127502 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule436(X):
    if X['1348'].values <= 0.18832623213529587 :
        if X['1806'].values <= 0.9110192656517029 :
            if X['1078'].values > -0.020727090537548065 :
                if X['1440'].values <= 0.5853632092475891 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule437(X):
    if X['1822'].values <= 0.03600536473095417 :
        if X['1296'].values <= 0.8821878135204315 :
            if X['1489'].values > -0.19563139975070953 :
                if X['1601'].values <= 0.868121474981308 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule438(X):
    if X['1822'].values <= 0.03600536473095417 :
        if X['1296'].values <= 0.8821878135204315 :
            if X['1489'].values > -0.19563139975070953 :
                if X['1601'].values > 0.868121474981308 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule439(X):
    if X['1822'].values <= 0.03600536473095417 :
        if X['1296'].values > 0.8821878135204315 :
            return 0
        else:
            return -1
    else:
        return -1
def rule440(X):
    if X['1822'].values > 0.03600536473095417 :
        if X['1749'].values <= 0.36220021545886993 :
            if X['1015'].values <= -0.030447139404714108 :
                if X['998'].values <= -0.30857616662979126 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule441(X):
    if X['1822'].values > 0.03600536473095417 :
        if X['1749'].values <= 0.36220021545886993 :
            if X['1015'].values <= -0.030447139404714108 :
                if X['998'].values > -0.30857616662979126 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule442(X):
    if X['1774'].values > 0.08726129680871964 :
        if X['1299'].values <= -0.2870655953884125 :
            if X['1396'].values <= -0.2989876866340637 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule443(X):
    if X['1822'].values > 0.03600536473095417 :
        if X['1749'].values <= 0.36220021545886993 :
            if X['1015'].values > -0.030447139404714108 :
                if X['1254'].values > 0.19401080906391144 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule444(X):
    if X['1822'].values > 0.03600536473095417 :
        if X['1749'].values > 0.36220021545886993 :
            if X['1772'].values > -1.2919374704360962 :
                if X['1405'].values > -0.35003843903541565 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule445(X):
    if X['1081'].values <= -0.6198840737342834 :
        if X['1397'].values <= 0.0007755053229629993 :
            if X['1130'].values <= -0.17599622160196304 :
                if X['1325'].values > -0.5730149745941162 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule446(X):
    if X['1081'].values <= -0.6198840737342834 :
        if X['1397'].values <= 0.0007755053229629993 :
            if X['1130'].values > -0.17599622160196304 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule447(X):
    if X['1081'].values <= -0.6198840737342834 :
        if X['1397'].values > 0.0007755053229629993 :
            if X['1506'].values > -0.4518992602825165 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule448(X):
    if X['1172'].values > -0.4848650246858597 :
        if X['1408'].values > -0.43629656732082367 :
            if X['1239'].values > 0.23923051357269287 :
                if X['1594'].values > 0.06497613713145256 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule449(X):
    if X['1081'].values > -0.6198840737342834 :
        if X['1295'].values <= -0.0037625079276040196 :
            if X['1393'].values <= -0.13729260116815567 :
                if X['1768'].values > -0.38006584346294403 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule450(X):
    if X['1534'].values > 0.21067752689123154 :
        if X['1700'].values <= 0.19715777784585953 :
            if X['1774'].values <= 0.40091918408870697 :
                if X['1420'].values <= 0.1975194811820984 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule451(X):
    if X['1081'].values > -0.6198840737342834 :
        if X['1295'].values <= -0.0037625079276040196 :
            if X['1393'].values > -0.13729260116815567 :
                if X['1750'].values > 0.053422220051288605 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule452(X):
    if X['1081'].values > -0.6198840737342834 :
        if X['1295'].values > -0.0037625079276040196 :
            if X['1704'].values <= 1.156018316745758 :
                if X['980'].values <= 0.014186613261699677 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule453(X):
    if X['1510'].values <= 0.04307365044951439 :
        if X['1289'].values <= -0.1472807228565216 :
            if X['1725'].values <= 0.4405781179666519 :
                if X['1031'].values > -0.5003008842468262 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule454(X):
    if X['1768'].values <= 0.34652532637119293 :
        if X['1439'].values <= -0.6502474248409271 :
            if X['1650'].values <= -0.2718030735850334 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule455(X):
    if X['1768'].values <= 0.34652532637119293 :
        if X['1439'].values <= -0.6502474248409271 :
            if X['1650'].values > -0.2718030735850334 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule456(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values <= -0.05860229954123497 :
            if X['1131'].values > 0.4954347312450409 :
                if X['1755'].values <= 0.023876729421317577 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule457(X):
    if X['1768'].values <= 0.34652532637119293 :
        if X['1439'].values > -0.6502474248409271 :
            if X['924'].values > 0.3507953882217407 :
                if X['990'].values <= -0.015721248171757907 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule458(X):
    if X['1768'].values <= 0.34652532637119293 :
        if X['1439'].values > -0.6502474248409271 :
            if X['924'].values > 0.3507953882217407 :
                if X['990'].values > -0.015721248171757907 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule459(X):
    if X['1768'].values > 0.34652532637119293 :
        if X['1163'].values <= 0.030170726589858532 :
            return 0
        else:
            return -1
    else:
        return -1
def rule460(X):
    if X['1768'].values > 0.34652532637119293 :
        if X['1163'].values > 0.030170726589858532 :
            if X['1709'].values <= 0.017333066556602716 :
                if X['1112'].values > -1.0046095997095108 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule461(X):
    if X['1768'].values > 0.34652532637119293 :
        if X['1163'].values > 0.030170726589858532 :
            if X['1709'].values > 0.017333066556602716 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule462(X):
    if X['1181'].values <= 0.35218915343284607 :
        if X['1140'].values <= 1.4111226797103882 :
            if X['1099'].values <= -0.5791052281856537 :
                if X['1133'].values > -0.19249044731259346 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule463(X):
    if X['1086'].values <= -0.5627769231796265 :
        if X['1037'].values <= 0.7512421309947968 :
            if X['1116'].values <= 0.4520832598209381 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule464(X):
    if X['1181'].values <= 0.35218915343284607 :
        if X['1140'].values > 1.4111226797103882 :
            return 0
        else:
            return -1
    else:
        return -1
def rule465(X):
    if X['1181'].values > 0.35218915343284607 :
        if X['1203'].values <= 0.05042189359664917 :
            if X['1608'].values <= -0.08417429402470589 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule466(X):
    if X['1181'].values > 0.35218915343284607 :
        if X['1203'].values <= 0.05042189359664917 :
            if X['1608'].values > -0.08417429402470589 :
                if X['1144'].values <= 0.2943265736103058 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule467(X):
    if X['1181'].values > 0.35218915343284607 :
        if X['1203'].values > 0.05042189359664917 :
            if X['1517'].values <= 0.275823637843132 :
                if X['1773'].values > -0.23001015186309814 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule468(X):
    if X['1181'].values > 0.35218915343284607 :
        if X['1203'].values > 0.05042189359664917 :
            if X['1517'].values > 0.275823637843132 :
                if X['1130'].values <= 0.2364971935749054 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule469(X):
    if X['1140'].values <= 0.23431429266929626 :
        if X['913'].values <= -0.4554780423641205 :
            if X['1654'].values <= 0.5273192673921585 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule470(X):
    if X['1140'].values <= 0.23431429266929626 :
        if X['913'].values > -0.4554780423641205 :
            if X['1047'].values <= 0.5004448294639587 :
                if X['921'].values > 0.3751637041568756 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule471(X):
    if X['1140'].values <= 0.23431429266929626 :
        if X['913'].values > -0.4554780423641205 :
            if X['1047'].values > 0.5004448294639587 :
                if X['1560'].values <= -0.03347775246948004 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule472(X):
    if X['1140'].values <= 0.23431429266929626 :
        if X['913'].values > -0.4554780423641205 :
            if X['1047'].values > 0.5004448294639587 :
                if X['1560'].values > -0.03347775246948004 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule473(X):
    if X['1140'].values > 0.23431429266929626 :
        if X['1688'].values <= 0.22051860392093658 :
            if X['1562'].values <= -0.8208250403404236 :
                if X['1740'].values <= 0.07850561290979385 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule474(X):
    if X['1140'].values > 0.23431429266929626 :
        if X['1688'].values <= 0.22051860392093658 :
            if X['1562'].values > -0.8208250403404236 :
                if X['1549'].values <= 0.44865231215953827 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule475(X):
    if X['1140'].values > 0.23431429266929626 :
        if X['1688'].values > 0.22051860392093658 :
            if X['1010'].values <= 0.3618787080049515 :
                if X['1018'].values <= 0.36571772396564484 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule476(X):
    if X['1140'].values > 0.23431429266929626 :
        if X['1688'].values > 0.22051860392093658 :
            if X['1010'].values > 0.3618787080049515 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule477(X):
    if X['1138'].values <= -0.19945959746837616 :
        if X['1556'].values <= 0.005670079495757818 :
            if X['1576'].values <= -0.1720575913786888 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule478(X):
    if X['1138'].values <= -0.19945959746837616 :
        if X['1556'].values <= 0.005670079495757818 :
            if X['1576'].values > -0.1720575913786888 :
                if X['1479'].values <= 0.1631447970867157 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule479(X):
    if X['1546'].values > 0.28609512746334076 :
        if X['1441'].values > -0.7323593497276306 :
            if X['1035'].values > -0.005000709556043148 :
                if X['920'].values > -0.20607272535562515 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule480(X):
    if X['1138'].values <= -0.19945959746837616 :
        if X['1556'].values > 0.005670079495757818 :
            if X['1522'].values <= 0.2944277226924896 :
                if X['1567'].values <= 0.3436189591884613 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule481(X):
    if X['1138'].values <= -0.19945959746837616 :
        if X['1556'].values > 0.005670079495757818 :
            if X['1522'].values > 0.2944277226924896 :
                if X['1241'].values > -0.3687211126089096 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule482(X):
    if X['1138'].values > -0.19945959746837616 :
        if X['1618'].values <= 1.0678736567497253 :
            if X['1777'].values <= 0.04027131199836731 :
                if X['1250'].values <= 0.45729807019233704 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule483(X):
    if X['1138'].values > -0.19945959746837616 :
        if X['1618'].values <= 1.0678736567497253 :
            if X['1777'].values > 0.04027131199836731 :
                if X['1220'].values > 0.09460020437836647 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule484(X):
    if X['1138'].values > -0.19945959746837616 :
        if X['1618'].values > 1.0678736567497253 :
            return 0
        else:
            return -1
    else:
        return -1
def rule485(X):
    if X['1409'].values <= 0.1361597776412964 :
        if X['1768'].values <= 0.5089247226715088 :
            if X['1126'].values <= -0.038425138220191 :
                if X['965'].values <= -0.09255518391728401 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule486(X):
    if X['1774'].values <= 0.08726129680871964 :
        if X['1603'].values <= 0.11379846185445786 :
            if X['1505'].values <= 0.0848839096724987 :
                if X['1095'].values <= 0.11367477104067802 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule487(X):
    if X['1409'].values <= 0.1361597776412964 :
        if X['1768'].values <= 0.5089247226715088 :
            if X['1126'].values > -0.038425138220191 :
                if X['1472'].values <= 0.19026582688093185 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule488(X):
    if X['1413'].values <= 0.4179270714521408 :
        if X['1725'].values <= 0.43804405629634857 :
            if X['1399'].values <= -0.5761023461818695 :
                if X['1340'].values <= 0.5198839753866196 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule489(X):
    if X['1409'].values <= 0.1361597776412964 :
        if X['1768'].values > 0.5089247226715088 :
            if X['1128'].values > -0.1145944744348526 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule490(X):
    if X['1409'].values > 0.1361597776412964 :
        if X['1744'].values <= -0.10639174655079842 :
            if X['1142'].values > -0.7432001531124115 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule491(X):
    if X['1409'].values > 0.1361597776412964 :
        if X['1744'].values > -0.10639174655079842 :
            if X['1213'].values <= 0.24517590552568436 :
                if X['1543'].values <= 0.4870196729898453 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule492(X):
    if X['1409'].values > 0.1361597776412964 :
        if X['1744'].values > -0.10639174655079842 :
            if X['1213'].values <= 0.24517590552568436 :
                if X['1543'].values > 0.4870196729898453 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule493(X):
    if X['1409'].values > 0.1361597776412964 :
        if X['1744'].values > -0.10639174655079842 :
            if X['1213'].values > 0.24517590552568436 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule494(X):
    if X['1287'].values <= 0.44492101669311523 :
        if X['921'].values <= -0.38202203810214996 :
            if X['1686'].values <= 0.04605033993721008 :
                if X['953'].values <= -0.15041608735919 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule495(X):
    if X['1287'].values <= 0.44492101669311523 :
        if X['921'].values <= -0.38202203810214996 :
            if X['1686'].values <= 0.04605033993721008 :
                if X['953'].values > -0.15041608735919 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule496(X):
    if X['1287'].values <= 0.44492101669311523 :
        if X['921'].values <= -0.38202203810214996 :
            if X['1686'].values > 0.04605033993721008 :
                if X['1231'].values <= -0.061055365949869156 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule497(X):
    if X['1413'].values <= 0.4179270714521408 :
        if X['1725'].values <= 0.43804405629634857 :
            if X['1399'].values <= -0.5761023461818695 :
                if X['1340'].values > 0.5198839753866196 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule498(X):
    if X['1287'].values <= 0.44492101669311523 :
        if X['921'].values > -0.38202203810214996 :
            if X['1633'].values <= 0.21588249504566193 :
                if X['1012'].values <= 0.2690918892621994 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule499(X):
    if X['1193'].values <= 0.586669534444809 :
        if X['1578'].values <= -0.05365712754428387 :
            if X['1499'].values > 0.04754476808011532 :
                if X['1163'].values > -0.25939519703388214 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule500(X):
    if X['1287'].values <= 0.44492101669311523 :
        if X['921'].values > -0.38202203810214996 :
            if X['1633'].values > 0.21588249504566193 :
                if X['1650'].values <= -0.3449133336544037 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule501(X):
    if X['1730'].values > -0.4748941957950592 :
        if X['1085'].values <= 0.05076029896736145 :
            if X['1092'].values <= -0.15722880512475967 :
                if X['1034'].values > -0.4626612961292267 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule502(X):
    if X['1287'].values > 0.44492101669311523 :
        if X['1219'].values > -1.0510188341140747 :
            if X['1311'].values > -0.3895033299922943 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule503(X):
    if X['1725'].values <= 0.4464806467294693 :
        if X['976'].values <= 1.1840279698371887 :
            if X['1033'].values <= 0.24492350220680237 :
                if X['1038'].values > 0.22558605670928955 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule504(X):
    if X['1725'].values <= 0.4464806467294693 :
        if X['976'].values <= 1.1840279698371887 :
            if X['1033'].values > 0.24492350220680237 :
                if X['1528'].values <= 0.30574920773506165 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule505(X):
    if X['1413'].values <= 0.4179270714521408 :
        if X['1725'].values <= 0.43804405629634857 :
            if X['1399'].values > -0.5761023461818695 :
                if X['1496'].values <= 0.005745569942519069 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule506(X):
    if X['1725'].values <= 0.4464806467294693 :
        if X['976'].values > 1.1840279698371887 :
            return 0
        else:
            return -1
    else:
        return -1
def rule507(X):
    if X['1725'].values > 0.4464806467294693 :
        if X['1257'].values <= 1.3353984355926514 :
            if X['1172'].values <= 0.4479369521141052 :
                if X['1758'].values <= -0.044533029198646545 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule508(X):
    if X['1725'].values > 0.4464806467294693 :
        if X['1257'].values > 1.3353984355926514 :
            return 1
        else:
            return -1
    else:
        return -1
def rule509(X):
    if X['1028'].values <= -0.20650968700647354 :
        if X['1073'].values <= 0.10190504416823387 :
            if X['1431'].values <= -0.18396367877721786 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule510(X):
    if X['1193'].values <= 0.586669534444809 :
        if X['1578'].values <= -0.05365712754428387 :
            if X['1499'].values <= 0.04754476808011532 :
                if X['1334'].values > -0.15867619961500168 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule511(X):
    if X['1028'].values <= -0.20650968700647354 :
        if X['1073'].values <= 0.10190504416823387 :
            if X['1431'].values > -0.18396367877721786 :
                if X['1257'].values > 0.030169875361025333 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule512(X):
    if X['1028'].values <= -0.20650968700647354 :
        if X['1073'].values > 0.10190504416823387 :
            if X['1057'].values > -0.23504198342561722 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule513(X):
    if X['1730'].values <= -0.4748941957950592 :
        if X['1642'].values <= 0.49571022391319275 :
            return 0
        else:
            return -1
    else:
        return -1
def rule514(X):
    if X['1028'].values > -0.20650968700647354 :
        if X['996'].values <= -0.3483694791793823 :
            if X['1720'].values <= 0.38515791296958923 :
                if X['1412'].values > -0.04901442117989063 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule515(X):
    if X['1028'].values > -0.20650968700647354 :
        if X['996'].values <= -0.3483694791793823 :
            if X['1720'].values > 0.38515791296958923 :
                if X['1379'].values <= 0.10187605209648609 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule516(X):
    if X['1028'].values > -0.20650968700647354 :
        if X['996'].values > -0.3483694791793823 :
            if X['1837'].values <= -0.11718963831663132 :
                if X['910'].values <= -0.016157870995812118 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule517(X):
    if X['1516'].values > -0.1886221095919609 :
        if X['1087'].values > -0.40369677543640137 :
            if X['1472'].values <= 0.12528225407004356 :
                if X['1411'].values <= 0.2961541712284088 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule518(X):
    if X['1028'].values > -0.20650968700647354 :
        if X['996'].values > -0.3483694791793823 :
            if X['1837'].values > -0.11718963831663132 :
                if X['1683'].values <= 0.18877013027668 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule519(X):
    if X['1130'].values > -0.48629245162010193 :
        if X['1553'].values > -0.06097067520022392 :
            if X['959'].values > 0.11360132694244385 :
                if X['1838'].values > 0.0641180444508791 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule520(X):
    if X['1496'].values <= -0.6474807560443878 :
        if X['1391'].values <= 0.6306971609592438 :
            if X['1125'].values <= 0.47207656502723694 :
                if X['1108'].values <= 0.41379740834236145 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule521(X):
    if X['1496'].values <= -0.6474807560443878 :
        if X['1391'].values <= 0.6306971609592438 :
            if X['1125'].values > 0.47207656502723694 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule522(X):
    if X['1496'].values > -0.6474807560443878 :
        if X['1101'].values <= 0.2548104301095009 :
            if X['1201'].values <= -0.011284206993877888 :
                if X['1237'].values <= -0.04349799454212189 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule523(X):
    if X['1405'].values <= -0.016455632634460926 :
        if X['1069'].values > -0.23523180931806564 :
            if X['1326'].values > -0.1657092198729515 :
                if X['901'].values > -0.07365717366337776 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule524(X):
    if X['1496'].values > -0.6474807560443878 :
        if X['1101'].values <= 0.2548104301095009 :
            if X['1201'].values > -0.011284206993877888 :
                if X['1651'].values <= 0.3812161386013031 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule525(X):
    if X['892'].values <= -0.23184429854154587 :
        if X['1714'].values <= -0.1425430290400982 :
            if X['1170'].values > -0.28980090736877173 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule526(X):
    if X['1496'].values > -0.6474807560443878 :
        if X['1101'].values > 0.2548104301095009 :
            if X['1013'].values <= -0.28537242114543915 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule527(X):
    if X['1496'].values > -0.6474807560443878 :
        if X['1101'].values > 0.2548104301095009 :
            if X['1013'].values > -0.28537242114543915 :
                if X['1636'].values <= -0.26578032970428467 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule528(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values <= -0.05860229954123497 :
            if X['1131'].values > 0.4954347312450409 :
                if X['1755'].values > 0.023876729421317577 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule529(X):
    if X['1265'].values <= 0.9137217700481415 :
        if X['1502'].values <= 0.30082640051841736 :
            if X['1354'].values <= -0.48597660660743713 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule530(X):
    if X['1130'].values > -0.48629245162010193 :
        if X['1553'].values > -0.06097067520022392 :
            if X['959'].values <= 0.11360132694244385 :
                if X['1175'].values > 0.079616479575634 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule531(X):
    if X['1265'].values <= 0.9137217700481415 :
        if X['1502'].values <= 0.30082640051841736 :
            if X['1354'].values > -0.48597660660743713 :
                if X['1412'].values > 0.13589981943368912 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule532(X):
    if X['1265'].values <= 0.9137217700481415 :
        if X['1502'].values > 0.30082640051841736 :
            if X['1420'].values <= 0.8454959094524384 :
                if X['1402'].values <= 0.6727140247821808 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule533(X):
    if X['1265'].values > 0.9137217700481415 :
        if X['1028'].values <= 1.2332849502563477 :
            return 0
        else:
            return -1
    else:
        return -1
def rule534(X):
    if X['1160'].values <= 0.7501197159290314 :
        if X['1734'].values <= -0.08429931849241257 :
            if X['1530'].values > -0.5605514943599701 :
                if X['888'].values > -0.30727510154247284 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule535(X):
    if X['984'].values <= -0.1567612662911415 :
        if X['1749'].values <= 0.2957743704319 :
            if X['1295'].values <= -0.07116403989493847 :
                if X['1807'].values > -0.23569883406162262 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule536(X):
    if X['984'].values <= -0.1567612662911415 :
        if X['1749'].values <= 0.2957743704319 :
            if X['1295'].values > -0.07116403989493847 :
                if X['1416'].values <= 0.06391150131821632 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule537(X):
    if X['1740'].values > 0.07314072176814079 :
        if X['1626'].values > -0.45415909588336945 :
            if X['937'].values > -0.24592851847410202 :
                if X['1664'].values > 0.4352871775627136 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule538(X):
    if X['984'].values <= -0.1567612662911415 :
        if X['1749'].values > 0.2957743704319 :
            if X['1467'].values <= 0.8178748190402985 :
                if X['1660'].values > -0.708124577999115 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule539(X):
    if X['984'].values > -0.1567612662911415 :
        if X['1124'].values <= -0.34450919926166534 :
            if X['1672'].values <= 0.3250098079442978 :
                if X['1147'].values > -0.4338190034031868 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule540(X):
    if X['984'].values > -0.1567612662911415 :
        if X['1124'].values <= -0.34450919926166534 :
            if X['1672'].values > 0.3250098079442978 :
                if X['1250'].values <= -0.19731657579541206 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule541(X):
    if X['984'].values > -0.1567612662911415 :
        if X['1124'].values > -0.34450919926166534 :
            if X['892'].values <= -0.19830407947301865 :
                if X['1842'].values <= -0.48802995681762695 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule542(X):
    if X['984'].values > -0.1567612662911415 :
        if X['1124'].values > -0.34450919926166534 :
            if X['892'].values <= -0.19830407947301865 :
                if X['1842'].values > -0.48802995681762695 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule543(X):
    if X['1193'].values <= 0.586669534444809 :
        if X['1578'].values <= -0.05365712754428387 :
            if X['1499'].values > 0.04754476808011532 :
                if X['1163'].values <= -0.25939519703388214 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule544(X):
    if X['951'].values <= 0.012675183359533548 :
        if X['1677'].values <= -0.2373080551624298 :
            if X['891'].values <= -0.045442577451467514 :
                if X['1162'].values <= 0.7655799388885498 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule545(X):
    if X['951'].values <= 0.012675183359533548 :
        if X['1677'].values <= -0.2373080551624298 :
            if X['891'].values > -0.045442577451467514 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule546(X):
    if X['956'].values <= 0.5430828332901001 :
        if X['1023'].values <= 0.2946911156177521 :
            if X['1321'].values > 1.3844929933547974 :
                if X['1313'].values > -0.3053155541419983 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule547(X):
    if X['951'].values <= 0.012675183359533548 :
        if X['1677'].values > -0.2373080551624298 :
            if X['945'].values <= -0.08567241951823235 :
                if X['1153'].values > -0.014602384995669127 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule548(X):
    if X['951'].values <= 0.012675183359533548 :
        if X['1677'].values > -0.2373080551624298 :
            if X['945'].values > -0.08567241951823235 :
                if X['933'].values <= 0.30297277867794037 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule549(X):
    if X['1035'].values > 0.1232370100915432 :
        if X['967'].values > 0.13804049044847488 :
            if X['1847'].values > -0.3909848779439926 :
                if X['976'].values <= 1.3335776925086975 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule550(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values <= -0.06341632269322872 :
            if X['1855'].values <= -0.36831606924533844 :
                if X['901'].values <= 0.1837792992591858 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule551(X):
    if X['1559'].values > 0.2724491357803345 :
        if X['1328'].values <= -0.1790270432829857 :
            if X['1736'].values <= 0.5458156317472458 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule552(X):
    if X['1413'].values <= 0.4179270714521408 :
        if X['1725'].values > 0.43804405629634857 :
            if X['934'].values <= 0.036390192806720734 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule553(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values <= -0.06341632269322872 :
            if X['1855'].values > -0.36831606924533844 :
                if X['1406'].values > -0.4249430447816849 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule554(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values > -0.06341632269322872 :
            if X['1321'].values <= 0.01713102823123336 :
                if X['1065'].values <= 0.12547488138079643 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule555(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values > -0.06341632269322872 :
            if X['1321'].values <= 0.01713102823123336 :
                if X['1065'].values > 0.12547488138079643 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule556(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values > -0.06341632269322872 :
            if X['1321'].values > 0.01713102823123336 :
                if X['1537'].values <= 0.7143559157848358 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule557(X):
    if X['951'].values > 0.012675183359533548 :
        if X['1437'].values > -0.06341632269322872 :
            if X['1321'].values > 0.01713102823123336 :
                if X['1537'].values > 0.7143559157848358 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule558(X):
    if X['1293'].values <= 0.03606150858104229 :
        if X['1145'].values <= -0.2801477164030075 :
            return 1
        else:
            return -1
    else:
        return -1
def rule559(X):
    if X['1405'].values > -0.016455632634460926 :
        if X['1466'].values <= -0.5317347645759583 :
            if X['1740'].values <= -0.2387869954109192 :
                if X['1641'].values > -0.5491490066051483 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule560(X):
    if X['1293'].values <= 0.03606150858104229 :
        if X['1145'].values > -0.2801477164030075 :
            if X['1568'].values <= 0.12698452919721603 :
                if X['1485'].values > 0.08155012875795364 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule561(X):
    if X['1293'].values <= 0.03606150858104229 :
        if X['1145'].values > -0.2801477164030075 :
            if X['1568'].values > 0.12698452919721603 :
                if X['1036'].values <= -0.2993765026330948 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule562(X):
    if X['1293'].values <= 0.03606150858104229 :
        if X['1145'].values > -0.2801477164030075 :
            if X['1568'].values > 0.12698452919721603 :
                if X['1036'].values > -0.2993765026330948 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule563(X):
    if X['1293'].values > 0.03606150858104229 :
        if X['1408'].values <= -0.20122668147087097 :
            if X['1583'].values <= 0.03881315514445305 :
                if X['1094'].values <= 0.16119036078453064 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule564(X):
    if X['1510'].values > 0.04307365044951439 :
        if X['1672'].values <= 0.3931408226490021 :
            if X['1114'].values > 0.12630541622638702 :
                if X['1706'].values <= 0.12027590349316597 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule565(X):
    if X['1293'].values > 0.03606150858104229 :
        if X['1408'].values <= -0.20122668147087097 :
            if X['1583'].values > 0.03881315514445305 :
                if X['1540'].values > -0.5878057181835175 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule566(X):
    if X['1293'].values > 0.03606150858104229 :
        if X['1408'].values > -0.20122668147087097 :
            if X['1611'].values > -0.4955500066280365 :
                if X['1547'].values <= 0.195780910551548 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule567(X):
    if X['1193'].values <= 0.586669534444809 :
        if X['1578'].values > -0.05365712754428387 :
            if X['1502'].values > 0.30082640051841736 :
                if X['1726'].values <= 1.2928810715675354 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule568(X):
    if X['1405'].values > -0.016455632634460926 :
        if X['1466'].values <= -0.5317347645759583 :
            if X['1740'].values > -0.2387869954109192 :
                if X['1459'].values > -0.3390531688928604 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule569(X):
    if X['930'].values <= 0.15734881162643433 :
        if X['1408'].values <= -0.09503864124417305 :
            if X['1242'].values <= 0.0074236884247511625 :
                if X['1072'].values > -0.1565912961959839 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule570(X):
    if X['1413'].values <= 0.4179270714521408 :
        if X['1725'].values > 0.43804405629634857 :
            if X['934'].values > 0.036390192806720734 :
                if X['1791'].values > -2.029867708683014 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule571(X):
    if X['930'].values <= 0.15734881162643433 :
        if X['1408'].values <= -0.09503864124417305 :
            if X['1242'].values > 0.0074236884247511625 :
                if X['1022'].values > 0.4613949805498123 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule572(X):
    if X['930'].values <= 0.15734881162643433 :
        if X['1408'].values > -0.09503864124417305 :
            if X['1534'].values <= 0.500227764248848 :
                if X['1270'].values <= 0.40038077533245087 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule573(X):
    if X['1071'].values <= 0.1741170436143875 :
        if X['1559'].values <= 0.5708272308111191 :
            if X['1668'].values > 0.3041306138038635 :
                if X['1636'].values > 0.04432367533445358 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule574(X):
    if X['930'].values <= 0.15734881162643433 :
        if X['1408'].values > -0.09503864124417305 :
            if X['1534'].values > 0.500227764248848 :
                if X['1361'].values <= -0.1710745468735695 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule575(X):
    if X['930'].values > 0.15734881162643433 :
        if X['1099'].values <= -0.1244487352669239 :
            if X['1827'].values <= -0.2863628715276718 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule576(X):
    if X['930'].values > 0.15734881162643433 :
        if X['1099'].values <= -0.1244487352669239 :
            if X['1827'].values > -0.2863628715276718 :
                if X['921'].values > -0.6679799556732178 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule577(X):
    if X['930'].values > 0.15734881162643433 :
        if X['1099'].values > -0.1244487352669239 :
            if X['1534'].values <= 0.062308309599757195 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule578(X):
    if X['1714'].values <= -0.3651835322380066 :
        if X['884'].values <= 0.48985640704631805 :
            if X['1286'].values <= 0.5050480663776398 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule579(X):
    if X['1714'].values <= -0.3651835322380066 :
        if X['884'].values <= 0.48985640704631805 :
            if X['1286'].values > 0.5050480663776398 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule580(X):
    if X['1714'].values <= -0.3651835322380066 :
        if X['884'].values > 0.48985640704631805 :
            return 1
        else:
            return -1
    else:
        return -1
def rule581(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values > -0.05860229954123497 :
            if X['1845'].values <= -0.41631849110126495 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule582(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values <= -0.2722768038511276 :
            if X['947'].values <= -0.02628846000880003 :
                if X['1559'].values > -0.009079375304281712 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule583(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values <= -0.2722768038511276 :
            if X['947'].values > -0.02628846000880003 :
                if X['1444'].values <= -0.24785877764225006 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule584(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values <= -0.2722768038511276 :
            if X['947'].values > -0.02628846000880003 :
                if X['1444'].values > -0.24785877764225006 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule585(X):
    if X['1413'].values > 0.4179270714521408 :
        if X['1383'].values <= -0.2564472481608391 :
            if X['1208'].values <= -0.5841862559318542 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule586(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values > -0.2722768038511276 :
            if X['1039'].values <= -0.25297776609659195 :
                if X['1599'].values > 0.4263124167919159 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule587(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values > -0.2722768038511276 :
            if X['1039'].values > -0.25297776609659195 :
                if X['1723'].values <= -0.5969893783330917 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule588(X):
    if X['1714'].values > -0.3651835322380066 :
        if X['1008'].values > -0.2722768038511276 :
            if X['1039'].values > -0.25297776609659195 :
                if X['1723'].values > -0.5969893783330917 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule589(X):
    if X['1671'].values <= -0.31397172808647156 :
        if X['1332'].values <= 0.3264671266078949 :
            if X['971'].values <= -0.04022470908239484 :
                if X['901'].values > -0.6047254540026188 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule590(X):
    if X['1671'].values <= -0.31397172808647156 :
        if X['1332'].values <= 0.3264671266078949 :
            if X['971'].values > -0.04022470908239484 :
                if X['1186'].values > -0.5784661173820496 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule591(X):
    if X['1671'].values <= -0.31397172808647156 :
        if X['1332'].values > 0.3264671266078949 :
            return 1
        else:
            return -1
    else:
        return -1
def rule592(X):
    if X['1671'].values > -0.31397172808647156 :
        if X['951'].values <= 0.32189756631851196 :
            if X['886'].values <= 0.9142868518829346 :
                if X['1069'].values <= -0.42196351289749146 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule593(X):
    if X['1671'].values > -0.31397172808647156 :
        if X['951'].values <= 0.32189756631851196 :
            if X['886'].values > 0.9142868518829346 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule594(X):
    if X['1671'].values > -0.31397172808647156 :
        if X['951'].values > 0.32189756631851196 :
            if X['1765'].values <= -0.07206334359943867 :
                if X['1218'].values > -0.15536174550652504 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule595(X):
    if X['1671'].values > -0.31397172808647156 :
        if X['951'].values > 0.32189756631851196 :
            if X['1765'].values > -0.07206334359943867 :
                if X['1151'].values > -0.7645861506462097 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule596(X):
    if X['1321'].values <= 0.8996874988079071 :
        if X['1166'].values <= -0.6067337989807129 :
            if X['933'].values <= -0.7534090876579285 :
                if X['925'].values <= 0.12403856590390205 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule597(X):
    if X['1321'].values <= 0.8996874988079071 :
        if X['1166'].values <= -0.6067337989807129 :
            if X['933'].values <= -0.7534090876579285 :
                if X['925'].values > 0.12403856590390205 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule598(X):
    if X['1321'].values <= 0.8996874988079071 :
        if X['1166'].values <= -0.6067337989807129 :
            if X['933'].values > -0.7534090876579285 :
                if X['940'].values <= 1.0671148300170898 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule599(X):
    if X['1413'].values > 0.4179270714521408 :
        if X['1383'].values > -0.2564472481608391 :
            if X['1314'].values <= -0.17295297607779503 :
                if X['1849'].values > -0.00469464436173439 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule600(X):
    if X['1321'].values <= 0.8996874988079071 :
        if X['1166'].values > -0.6067337989807129 :
            if X['1472'].values <= 0.17905890941619873 :
                if X['915'].values > -0.018820870667696 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule601(X):
    if X['1321'].values <= 0.8996874988079071 :
        if X['1166'].values > -0.6067337989807129 :
            if X['1472'].values > 0.17905890941619873 :
                if X['1489'].values <= -0.10517805814743042 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule602(X):
    if X['1730'].values > -0.4748941957950592 :
        if X['1085'].values <= 0.05076029896736145 :
            if X['1092'].values > -0.15722880512475967 :
                if X['1009'].values <= -0.15427321195602417 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule603(X):
    if X['1321'].values > 0.8996874988079071 :
        if X['1079'].values > -0.41839806735515594 :
            return 0
        else:
            return -1
    else:
        return -1
def rule604(X):
    if X['1138'].values <= -0.3604079335927963 :
        if X['1274'].values <= 0.5768122673034668 :
            if X['1120'].values <= 0.646156907081604 :
                if X['1150'].values <= 0.6086056232452393 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule605(X):
    if X['1138'].values <= -0.3604079335927963 :
        if X['1274'].values <= 0.5768122673034668 :
            if X['1120'].values > 0.646156907081604 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule606(X):
    if X['1138'].values <= -0.3604079335927963 :
        if X['1274'].values > 0.5768122673034668 :
            return 1
        else:
            return -1
    else:
        return -1
def rule607(X):
    if X['1138'].values > -0.3604079335927963 :
        if X['1595'].values <= 0.8010097444057465 :
            if X['993'].values <= -0.20628273487091064 :
                if X['1367'].values <= -0.08642185851931572 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule608(X):
    if X['969'].values <= 0.2253270447254181 :
        if X['1581'].values > -0.04873348027467728 :
            if X['1464'].values <= -0.901723325252533 :
                if X['1785'].values > -0.7048199474811554 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule609(X):
    if X['1138'].values > -0.3604079335927963 :
        if X['1595'].values <= 0.8010097444057465 :
            if X['993'].values > -0.20628273487091064 :
                if X['1629'].values > 0.9130904078483582 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule610(X):
    if X['1138'].values > -0.3604079335927963 :
        if X['1595'].values > 0.8010097444057465 :
            if X['1344'].values <= 0.06933317147195339 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule611(X):
    if X['1341'].values <= -0.5184979140758514 :
        if X['911'].values > -1.1203668713569641 :
            if X['1613'].values <= 0.6469243764877319 :
                if X['1701'].values <= 0.1431414559483528 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule612(X):
    if X['1086'].values > -0.5627769231796265 :
        if X['1571'].values > -0.14834225922822952 :
            if X['1364'].values > 0.2182706817984581 :
                if X['1415'].values <= -0.008741214871406555 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule613(X):
    if X['1341'].values > -0.5184979140758514 :
        if X['1561'].values <= 0.9261961579322815 :
            if X['948'].values <= -0.6007062494754791 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule614(X):
    if X['1341'].values > -0.5184979140758514 :
        if X['1561'].values > 0.9261961579322815 :
            if X['1637'].values > -0.6859714090824127 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule615(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values <= -0.22018472850322723 :
            if X['1515'].values <= 0.30019931495189667 :
                if X['1741'].values <= -0.38634192943573 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule616(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values <= -0.22018472850322723 :
            if X['1515'].values <= 0.30019931495189667 :
                if X['1741'].values > -0.38634192943573 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule617(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values <= -0.22018472850322723 :
            if X['1515'].values > 0.30019931495189667 :
                if X['1231'].values <= 0.10824361070990562 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule618(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values <= -0.22018472850322723 :
            if X['1515'].values > 0.30019931495189667 :
                if X['1231'].values > 0.10824361070990562 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule619(X):
    if X['1774'].values <= 0.08726129680871964 :
        if X['1603'].values <= 0.11379846185445786 :
            if X['1505'].values > 0.0848839096724987 :
                if X['1382'].values > -0.10965800285339355 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule620(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values > -0.22018472850322723 :
            if X['1610'].values <= 0.03828625567257404 :
                if X['1172'].values > -0.20164380222558975 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule621(X):
    if X['1559'].values > 0.2724491357803345 :
        if X['1328'].values > -0.1790270432829857 :
            if X['1691'].values <= 1.116788238286972 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule622(X):
    if X['1038'].values <= -0.09565142542123795 :
        if X['1806'].values > -0.22018472850322723 :
            if X['1610'].values > 0.03828625567257404 :
                if X['1045'].values > 0.2636784091591835 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule623(X):
    if X['1038'].values > -0.09565142542123795 :
        if X['1533'].values <= -0.36770474910736084 :
            if X['1783'].values <= 0.23676566779613495 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule624(X):
    if X['1038'].values > -0.09565142542123795 :
        if X['1533'].values <= -0.36770474910736084 :
            if X['1783'].values > 0.23676566779613495 :
                if X['1556'].values > -0.02908242493867874 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule625(X):
    if X['1038'].values > -0.09565142542123795 :
        if X['1533'].values > -0.36770474910736084 :
            if X['1384'].values <= -0.25108978897333145 :
                if X['1710'].values <= -0.6283839046955109 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule626(X):
    if X['1348'].values <= 0.18832623213529587 :
        if X['1806'].values <= 0.9110192656517029 :
            if X['1078'].values > -0.020727090537548065 :
                if X['1440'].values > 0.5853632092475891 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule627(X):
    if X['892'].values <= -0.23184429854154587 :
        if X['1714'].values > -0.1425430290400982 :
            if X['1412'].values > -0.44208988547325134 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule628(X):
    if X['1193'].values <= 0.6866239905357361 :
        if X['1104'].values <= 1.1607000827789307 :
            if X['1112'].values <= -0.1907593533396721 :
                if X['1725'].values <= 0.4508434534072876 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule629(X):
    if X['1287'].values <= -0.22430400550365448 :
        if X['1684'].values > -0.8656454980373383 :
            if X['1579'].values > -0.4962355047464371 :
                if X['1741'].values <= 0.10841502249240875 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule630(X):
    if X['1534'].values <= 0.21067752689123154 :
        if X['1537'].values <= 1.5543000102043152 :
            if X['1316'].values > 0.3903924524784088 :
                if X['1141'].values <= 0.285100519657135 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule631(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values <= -0.2368168830871582 :
            if X['1759'].values <= 0.25427746772766113 :
                if X['1674'].values <= 0.08149688318371773 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule632(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values <= -0.2368168830871582 :
            if X['1759'].values <= 0.25427746772766113 :
                if X['1674'].values > 0.08149688318371773 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule633(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values <= -0.2368168830871582 :
            if X['1759'].values > 0.25427746772766113 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule634(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values > -0.2368168830871582 :
            if X['1570'].values <= -0.3376787304878235 :
                if X['1494'].values <= 0.08370174467563629 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule635(X):
    if X['1071'].values > 0.1741170436143875 :
        if X['1755'].values <= 0.053674595430493355 :
            if X['1857'].values > -0.4229840934276581 :
                if X['1217'].values <= 0.47230151295661926 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule636(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values > -0.2368168830871582 :
            if X['1570'].values > -0.3376787304878235 :
                if X['912'].values <= 0.7329432964324951 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule637(X):
    if X['1287'].values > -0.22430400550365448 :
        if X['1038'].values > -0.2368168830871582 :
            if X['1570'].values > -0.3376787304878235 :
                if X['912'].values > 0.7329432964324951 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule638(X):
    if X['1193'].values <= 0.6866239905357361 :
        if X['1104'].values <= 1.1607000827789307 :
            if X['1112'].values > -0.1907593533396721 :
                if X['1605'].values > 0.4073962867259979 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule639(X):
    if X['1742'].values <= 0.25939327478408813 :
        if X['1071'].values <= 0.2775355130434036 :
            if X['1773'].values > 0.5587217211723328 :
                if X['1333'].values <= 0.6469564624130726 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule640(X):
    if X['1742'].values <= 0.25939327478408813 :
        if X['1071'].values > 0.2775355130434036 :
            if X['1011'].values <= 0.4692247211933136 :
                if X['1636'].values <= -0.30092888325452805 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule641(X):
    if X['1742'].values <= 0.25939327478408813 :
        if X['1071'].values > 0.2775355130434036 :
            if X['1011'].values <= 0.4692247211933136 :
                if X['1636'].values > -0.30092888325452805 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule642(X):
    if X['1742'].values <= 0.25939327478408813 :
        if X['1071'].values > 0.2775355130434036 :
            if X['1011'].values > 0.4692247211933136 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule643(X):
    if X['1742'].values > 0.25939327478408813 :
        if X['1287'].values <= -0.45858412981033325 :
            if X['1096'].values <= -0.131795234978199 :
                if X['1407'].values <= 1.572536826133728 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule644(X):
    if X['1742'].values > 0.25939327478408813 :
        if X['1287'].values <= -0.45858412981033325 :
            if X['1096'].values > -0.131795234978199 :
                if X['1787'].values <= -0.15613237023353577 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule645(X):
    if X['1742'].values > 0.25939327478408813 :
        if X['1287'].values > -0.45858412981033325 :
            if X['1740'].values <= -0.7606221437454224 :
                if X['1002'].values <= 0.671540766954422 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule646(X):
    if X['1742'].values > 0.25939327478408813 :
        if X['1287'].values > -0.45858412981033325 :
            if X['1740'].values > -0.7606221437454224 :
                if X['1786'].values <= 0.6554423421621323 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule647(X):
    if X['1755'].values <= -0.1650586873292923 :
        if X['1069'].values <= 0.19832924753427505 :
            if X['1249'].values <= 0.22830865532159805 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule648(X):
    if X['1755'].values <= -0.1650586873292923 :
        if X['1069'].values <= 0.19832924753427505 :
            if X['1249'].values > 0.22830865532159805 :
                if X['1107'].values > -0.11398644000291824 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule649(X):
    if X['1755'].values <= -0.1650586873292923 :
        if X['1069'].values > 0.19832924753427505 :
            if X['1449'].values <= 0.10615042969584465 :
                if X['1664'].values > -0.6892297863960266 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule650(X):
    if X['1755'].values <= -0.1650586873292923 :
        if X['1069'].values > 0.19832924753427505 :
            if X['1449'].values > 0.10615042969584465 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule651(X):
    if X['1755'].values > -0.1650586873292923 :
        if X['1378'].values <= -0.29026345908641815 :
            if X['1600'].values <= 0.15709896385669708 :
                if X['1163'].values <= 0.35216024518013 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule652(X):
    if X['1510'].values > 0.04307365044951439 :
        if X['1672'].values <= 0.3931408226490021 :
            if X['1114'].values > 0.12630541622638702 :
                if X['1706'].values > 0.12027590349316597 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule653(X):
    if X['969'].values <= 0.2253270447254181 :
        if X['1581'].values <= -0.04873348027467728 :
            if X['1027'].values <= -0.2311115562915802 :
                if X['946'].values > 0.18175119161605835 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule654(X):
    if X['1755'].values > -0.1650586873292923 :
        if X['1378'].values <= -0.29026345908641815 :
            if X['1600'].values > 0.15709896385669708 :
                if X['1167'].values > -0.06108180992305279 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule655(X):
    if X['1755'].values > -0.1650586873292923 :
        if X['1378'].values > -0.29026345908641815 :
            if X['1448'].values <= -0.3511849194765091 :
                if X['1467'].values > -0.09939232468605042 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule656(X):
    if X['892'].values > -0.23184429854154587 :
        if X['1642'].values > 0.7493916153907776 :
            if X['1514'].values > -0.9416533708572388 :
                if X['1802'].values <= 0.4408099502325058 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule657(X):
    if X['1755'].values > -0.1650586873292923 :
        if X['1378'].values > -0.29026345908641815 :
            if X['1448'].values > -0.3511849194765091 :
                if X['1785'].values > -0.304720401763916 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule658(X):
    if X['1016'].values <= 0.2948906570672989 :
        if X['1668'].values <= 0.2740703374147415 :
            if X['1188'].values <= 0.3029154986143112 :
                if X['1590'].values <= 0.0649622455239296 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule659(X):
    if X['1413'].values > 0.4179270714521408 :
        if X['1383'].values <= -0.2564472481608391 :
            if X['1208'].values > -0.5841862559318542 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule660(X):
    if X['1516'].values <= -0.1886221095919609 :
        if X['1510'].values > -0.05860229954123497 :
            if X['1845'].values > -0.41631849110126495 :
                if X['1706'].values > -0.44426701962947845 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule661(X):
    if X['1016'].values <= 0.2948906570672989 :
        if X['1668'].values <= 0.2740703374147415 :
            if X['1188'].values > 0.3029154986143112 :
                if X['940'].values > 0.3324812054634094 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule662(X):
    if X['1016'].values <= 0.2948906570672989 :
        if X['1668'].values > 0.2740703374147415 :
            if X['1258'].values <= -0.3987017869949341 :
                if X['1344'].values <= 0.8052089139819145 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule663(X):
    if X['1516'].values > -0.1886221095919609 :
        if X['1087'].values <= -0.40369677543640137 :
            if X['1093'].values > 0.3169180899858475 :
                if X['1678'].values <= 0.4315420389175415 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule664(X):
    if X['969'].values <= 0.2253270447254181 :
        if X['1581'].values <= -0.04873348027467728 :
            if X['1027'].values <= -0.2311115562915802 :
                if X['946'].values <= 0.18175119161605835 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule665(X):
    if X['1016'].values > 0.2948906570672989 :
        if X['990'].values <= -0.1322685331106186 :
            if X['1617'].values <= -0.3229479193687439 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule666(X):
    if X['1016'].values > 0.2948906570672989 :
        if X['990'].values <= -0.1322685331106186 :
            if X['1617'].values > -0.3229479193687439 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule667(X):
    if X['1016'].values > 0.2948906570672989 :
        if X['990'].values > -0.1322685331106186 :
            if X['1097'].values > -1.5757707357406616 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule668(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values <= 0.35106582939624786 :
            if X['1198'].values <= -0.34375937283039093 :
                if X['1298'].values <= 0.08496353775262833 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule669(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values <= 0.35106582939624786 :
            if X['1198'].values <= -0.34375937283039093 :
                if X['1298'].values > 0.08496353775262833 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule670(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values <= 0.35106582939624786 :
            if X['1198'].values > -0.34375937283039093 :
                if X['1193'].values <= -0.2694854289293289 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule671(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values <= 0.35106582939624786 :
            if X['1198'].values > -0.34375937283039093 :
                if X['1193'].values > -0.2694854289293289 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule672(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values > 0.35106582939624786 :
            if X['1855'].values <= -0.18028102070093155 :
                if X['910'].values <= -0.008283132687211037 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule673(X):
    if X['1516'].values > -0.1886221095919609 :
        if X['1087'].values <= -0.40369677543640137 :
            if X['1093'].values <= 0.3169180899858475 :
                if X['1331'].values > -0.4216362237930298 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule674(X):
    if X['1292'].values <= 0.12074096500873566 :
        if X['976'].values > 0.35106582939624786 :
            if X['1855'].values > -0.18028102070093155 :
                if X['1048'].values > -0.21876011043787003 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule675(X):
    if X['1292'].values > 0.12074096500873566 :
        if X['1352'].values <= -0.21137165278196335 :
            if X['1501'].values <= 0.18346093595027924 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule676(X):
    if X['1292'].values > 0.12074096500873566 :
        if X['1352'].values <= -0.21137165278196335 :
            if X['1501'].values > 0.18346093595027924 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule677(X):
    if X['969'].values > 0.2253270447254181 :
        if X['1601'].values <= 0.03931504674255848 :
            if X['1288'].values > 0.039172224467620254 :
                if X['1121'].values <= 0.06773192435503006 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule678(X):
    if X['1292'].values > 0.12074096500873566 :
        if X['1352'].values > -0.21137165278196335 :
            if X['1076'].values <= -0.032805112190544605 :
                if X['1151'].values > 0.013217845931649208 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule679(X):
    if X['1510'].values > 0.04307365044951439 :
        if X['1672'].values > 0.3931408226490021 :
            if X['1584'].values <= 0.01346473372541368 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule680(X):
    if X['1292'].values > 0.12074096500873566 :
        if X['1352'].values > -0.21137165278196335 :
            if X['1076'].values > -0.032805112190544605 :
                if X['1746'].values > -0.0015688869170844555 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule681(X):
    if X['1124'].values <= -0.47279098629951477 :
        if X['1298'].values <= -0.28873322904109955 :
            return 1
        else:
            return -1
    else:
        return -1
def rule682(X):
    if X['1124'].values <= -0.47279098629951477 :
        if X['1298'].values > -0.28873322904109955 :
            if X['1322'].values <= 0.20409603416919708 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule683(X):
    if X['1124'].values > -0.47279098629951477 :
        if X['975'].values <= 0.4906769394874573 :
            if X['1605'].values <= 0.29683560132980347 :
                if X['892'].values <= -0.30359290540218353 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule684(X):
    if X['1124'].values > -0.47279098629951477 :
        if X['975'].values <= 0.4906769394874573 :
            if X['1605'].values > 0.29683560132980347 :
                if X['1141'].values <= -0.01071598008275032 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule685(X):
    if X['1124'].values > -0.47279098629951477 :
        if X['975'].values <= 0.4906769394874573 :
            if X['1605'].values > 0.29683560132980347 :
                if X['1141'].values > -0.01071598008275032 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule686(X):
    if X['1124'].values > -0.47279098629951477 :
        if X['975'].values > 0.4906769394874573 :
            if X['1422'].values > -0.4905744343996048 :
                if X['1196'].values <= 0.9872750043869019 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule687(X):
    if X['1534'].values > 0.21067752689123154 :
        if X['1700'].values <= 0.19715777784585953 :
            if X['1774'].values > 0.40091918408870697 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule688(X):
    if X['1265'].values <= 0.9137217700481415 :
        if X['1665'].values <= 0.49929189682006836 :
            if X['1740'].values > 0.11389986425638199 :
                if X['1161'].values <= -0.07609524950385094 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule689(X):
    if X['1740'].values > 0.07314072176814079 :
        if X['1626'].values > -0.45415909588336945 :
            if X['937'].values <= -0.24592851847410202 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule690(X):
    if X['1265'].values <= 0.9137217700481415 :
        if X['1665'].values > 0.49929189682006836 :
            if X['1456'].values > 0.1311766877770424 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule691(X):
    if X['1265'].values > 0.9137217700481415 :
        return 0
    else:
        return -1
def rule692(X):
    if X['1811'].values <= 0.05955618619918823 :
        if X['1503'].values <= 0.561092346906662 :
            if X['1749'].values <= 0.3278416097164154 :
                if X['1804'].values <= -0.6761706471443176 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule693(X):
    if X['1811'].values <= 0.05955618619918823 :
        if X['1503'].values <= 0.561092346906662 :
            if X['1749'].values <= 0.3278416097164154 :
                if X['1804'].values > -0.6761706471443176 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule694(X):
    if X['1811'].values <= 0.05955618619918823 :
        if X['1503'].values <= 0.561092346906662 :
            if X['1749'].values > 0.3278416097164154 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule695(X):
    if X['1811'].values <= 0.05955618619918823 :
        if X['1503'].values > 0.561092346906662 :
            if X['1227'].values <= 0.23595843836665154 :
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule696(X):
    if X['1811'].values <= 0.05955618619918823 :
        if X['1503'].values > 0.561092346906662 :
            if X['1227'].values > 0.23595843836665154 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule697(X):
    if X['1811'].values > 0.05955618619918823 :
        if X['1478'].values <= -0.509835958480835 :
            if X['1331'].values <= -0.6487257480621338 :
                return 1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule698(X):
    if X['1811'].values > 0.05955618619918823 :
        if X['1478'].values <= -0.509835958480835 :
            if X['1331'].values > -0.6487257480621338 :
                if X['992'].values <= 1.125395119190216 :
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
def rule699(X):
    if X['892'].values > -0.23184429854154587 :
        if X['1642'].values <= 0.7493916153907776 :
            if X['1809'].values <= 0.6284122169017792 :
                if X['981'].values <= -0.003421945031732321 :
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
