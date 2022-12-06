dict_rev = {'review_0': {'input.txt': 'User needed help creating an account'},
  'review_1': {'input.txt': 'User calling needing assistance with their RSR report, user stated they need assistance with errors they see.'}}


# for key in dict_rev:
#     print(key)
#     print(dict_rev[key])
#     print(dict_rev[key]['input.txt'])


# dict_rev['review_0']['input.txt']


import pandas as pd
df = pd.read_csv("batch_records_latest1.csv")

#duplicate = df[df.duplicated('Description')].sum()
ab = df.duplicated('Description').sum()
df.drop_duplicates(subset ="Description",inplace=True)
print(df)

test = "test"

json_list = [
  {
    "User needed help creating an account": {
      "classPredictions": [
        {
          "class": "CreateAccount",
          "score": 0.7366121411323547
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.056484878063201904
        },
        {
          "class": "AccessAccount",
          "score": 0.021102936938405037
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.016780104488134384
        },
        {
          "class": "FileComplaint",
          "score": 0.013472743332386017
        }
      ]
    }
  },
  {
    "User calling needing assistance with their RSR report, user stated they need assistance with errors they see.": {
      "classPredictions": [
        {
          "class": "RemoveUser",
          "score": 0.2666485905647278
        },
        {
          "class": "RegisterAsPD",
          "score": 0.1589585840702057
        },
        {
          "class": "GetUpdate",
          "score": 0.09012075513601303
        },
        {
          "class": "CallForInformation",
          "score": 0.04947218671441078
        },
        {
          "class": "FileComplaint",
          "score": 0.03477659448981285
        }
      ]
    }
  },
  {
    "Amy called in needed assistance with registering for a grant as pd": {
      "classPredictions": [
        {
          "class": "ApplyForGrant",
          "score": 0.46003058552742004
        },
        {
          "class": "RegisterGrant",
          "score": 0.2344183325767517
        },
        {
          "class": "AddGrant",
          "score": 0.050375036895275116
        },
        {
          "class": "RegisterAsPD",
          "score": 0.03516969084739685
        },
        {
          "class": "RemoveUser",
          "score": 0.02000224031507969
        }
      ]
    }
  },
  {
    "User needed their session terminated": {
      "classPredictions": [
        {
          "class": "ResetPassword",
          "score": 0.19325388967990875
        },
        {
          "class": "RemoveUser",
          "score": 0.11178931593894958
        },
        {
          "class": "LogIntoEHB",
          "score": 0.08327501267194748
        },
        {
          "class": "RegisterAsPD",
          "score": 0.06617264449596405
        },
        {
          "class": "ChangePassword",
          "score": 0.06161164492368698
        }
      ]
    }
  },
  {
    "User calling trying to access the RSR report but not able to see it.": {
      "classPredictions": [
        {
          "class": "AccessGrant",
          "score": 0.1842082291841507
        },
        {
          "class": "AccessAccount",
          "score": 0.1052069440484047
        },
        {
          "class": "GetAccess",
          "score": 0.09963741898536682
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.06523825228214264
        },
        {
          "class": "RemoveUser",
          "score": 0.06504981219768524
        }
      ]
    }
  },
  {
    "Grantee is unable to log into account using email so he made a backup with another email. \nGrantee was having trouble finding how to find the organization associated with the grant number provided.": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.18175940215587616
        },
        {
          "class": "AccessAccount",
          "score": 0.06901267915964127
        },
        {
          "class": "FindHealthCenter",
          "score": 0.06168815493583679
        },
        {
          "class": "AskAboutStatus",
          "score": 0.05753147974610329
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.055877432227134705
        }
      ]
    }
  },
  {
    "the user was working on a grant app in grants.gov and requested assistance after submitting a ticket request as well": {
      "classPredictions": [
        {
          "class": "ApplyForGrant",
          "score": 0.08258451521396637
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.07154928892850876
        },
        {
          "class": "CallForInformation",
          "score": 0.07150397449731827
        },
        {
          "class": "CallForAssistance",
          "score": 0.055686578154563904
        },
        {
          "class": "AccessAccount",
          "score": 0.054780520498752594
        }
      ]
    }
  },
  {
    "caller called in needed to speak to some one regarding the cares act provider relief": {
      "classPredictions": [
        {
          "class": "SpeakWithSomeone",
          "score": 0.4352594316005707
        },
        {
          "class": "RemoveUser",
          "score": 0.07907567918300629
        },
        {
          "class": "RegisterAsPD",
          "score": 0.05582012981176376
        },
        {
          "class": "CallForInformation",
          "score": 0.03227802738547325
        },
        {
          "class": "ApplyForProgram",
          "score": 0.029750864952802658
        }
      ]
    }
  },
  {
    "The caller called because his organization runs a program for covid testing but for the uninsured. The caller stated that they haven't been paid and they need to speak with someone from HRSA for further assistance.": {
      "classPredictions": [
        {
          "class": "SpeakWithSomeone",
          "score": 0.24541957676410675
        },
        {
          "class": "RemoveUser",
          "score": 0.10150400549173355
        },
        {
          "class": "RegisterAsPD",
          "score": 0.09629326313734055
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.060452550649642944
        },
        {
          "class": "ApplyForProgram",
          "score": 0.04720568656921387
        }
      ]
    }
  },
  {
    "Caller stated that she was still having issues with the budget period showing up in her PA.  She stated that she had her GMS on the line to talk with us but then she stated he was not available to speak to tier 2.": {
      "classPredictions": [
        {
          "class": "CreateEHBAccount",
          "score": 0.09388464689254761
        },
        {
          "class": "FileComplaint",
          "score": 0.08281797170639038
        },
        {
          "class": "AccessAccount",
          "score": 0.0805273950099945
        },
        {
          "class": "MakeChanges",
          "score": 0.06485673785209656
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.056745585054159164
        }
      ]
    }
  },
  {
    "The called to speak with Turk Hassan from the OIT helpdesk regarding  issues with the computer": {
      "classPredictions": [
        {
          "class": "SpeakWithSomeone",
          "score": 0.44728517532348633
        },
        {
          "class": "GiveAccess",
          "score": 0.07122334837913513
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.044659361243247986
        },
        {
          "class": "RegisterAsPD",
          "score": 0.0367346927523613
        },
        {
          "class": "RemoveUser",
          "score": 0.03350740298628807
        }
      ]
    }
  },
  {
    "Please call me . I have a couple questions regarding reporting that requires speaking to someone. thank you!": {
      "classPredictions": [
        {
          "class": "AccessAccount",
          "score": 0.12207840383052826
        },
        {
          "class": "SpeakWithSomeone",
          "score": 0.10655219852924347
        },
        {
          "class": "GetAccess",
          "score": 0.07410236448049545
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.05183050036430359
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.04347224533557892
        }
      ]
    }
  },
  {
    "User was able to try it again through the phone and was able to get access": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.1699240356683731
        },
        {
          "class": "GetAccess",
          "score": 0.16914679110050201
        },
        {
          "class": "ChangePassword",
          "score": 0.08689792454242706
        },
        {
          "class": "RemoveUser",
          "score": 0.047212257981300354
        },
        {
          "class": "AccessGrant",
          "score": 0.04546189308166504
        }
      ]
    }
  },
  {
    "User needed to know how to get access to this grant": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.6587185859680176
        },
        {
          "class": "AccessGrant",
          "score": 0.12072990089654922
        },
        {
          "class": "ApplyForGrant",
          "score": 0.03712139651179314
        },
        {
          "class": "GiveAccess",
          "score": 0.022442156448960304
        },
        {
          "class": "AddUser",
          "score": 0.014383647590875626
        }
      ]
    }
  },
  {
    "the caller needs to get access to a grant application and they received notification to access the application but it did not work": {
      "classPredictions": [
        {
          "class": "AccessGrant",
          "score": 0.26781150698661804
        },
        {
          "class": "GetAccess",
          "score": 0.1531323939561844
        },
        {
          "class": "AccessAccount",
          "score": 0.08098045736551285
        },
        {
          "class": "ApplyForGrant",
          "score": 0.08073320984840393
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.05802593380212784
        }
      ]
    }
  },
  {
    "User calling for assistance with how to get access to their NCC Report for grant H8HCS44984": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.4042462706565857
        },
        {
          "class": "AccessAccount",
          "score": 0.15604476630687714
        },
        {
          "class": "AccessGrant",
          "score": 0.09237416088581085
        },
        {
          "class": "CallForAssistance",
          "score": 0.04575935751199722
        },
        {
          "class": "CallForInformation",
          "score": 0.032356295734643936
        }
      ]
    }
  },
  {
    "User called for assistance with how to get access to this grant to submit their Progress report.": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.256605327129364
        },
        {
          "class": "AccessGrant",
          "score": 0.18269188702106476
        },
        {
          "class": "AccessAccount",
          "score": 0.10347697883844376
        },
        {
          "class": "CallForAssistance",
          "score": 0.07534432411193848
        },
        {
          "class": "AskAboutStatus",
          "score": 0.0445466972887516
        }
      ]
    }
  },
  {
    "User called wanting to know how a user can get access to their grants and register as BO": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.26048794388771057
        },
        {
          "class": "RegisterAsPD",
          "score": 0.0948043093085289
        },
        {
          "class": "AccessGrant",
          "score": 0.07676941156387329
        },
        {
          "class": "GiveAccess",
          "score": 0.07338634878396988
        },
        {
          "class": "AddUser",
          "score": 0.05133672058582306
        }
      ]
    }
  },
  {
    "The user is trying to get access to the land grant in the EHB.": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.4074760377407074
        },
        {
          "class": "AccessGrant",
          "score": 0.1981448531150818
        },
        {
          "class": "GiveAccess",
          "score": 0.044202808290719986
        },
        {
          "class": "AddGrant",
          "score": 0.03836698457598686
        },
        {
          "class": "LogIntoEHB",
          "score": 0.022382881492376328
        }
      ]
    }
  },
  {
    "User needed help locating an inactive grant": {
      "classPredictions": [
        {
          "class": "ApplyForGrant",
          "score": 0.5609986186027527
        },
        {
          "class": "RegisterGrant",
          "score": 0.08514675498008728
        },
        {
          "class": "AddGrant",
          "score": 0.05924741551280022
        },
        {
          "class": "GiveAccess",
          "score": 0.05221549794077873
        },
        {
          "class": "AccessGrant",
          "score": 0.017971906810998917
        }
      ]
    }
  },
  {
    "User is looking to find a grant (H80CS29018) in the EHB but is unable to find it and also a report with tracking #00309849. Additionally, the grantee will like to speak to the Payment Management System for assistance with some questions about the portal.": {
      "classPredictions": [
        {
          "class": "AskAboutStatus",
          "score": 0.1875002682209015
        },
        {
          "class": "ApplyForGrant",
          "score": 0.06106358766555786
        },
        {
          "class": "GetAccess",
          "score": 0.05893787369132042
        },
        {
          "class": "FindHealthCenter",
          "score": 0.055086638778448105
        },
        {
          "class": "RegisterAsPD",
          "score": 0.054653532803058624
        }
      ]
    }
  },
  {
    "Received call from Lin who needed assistance with accessing her EHB account.": {
      "classPredictions": [
        {
          "class": "AccessAccount",
          "score": 0.17004767060279846
        },
        {
          "class": "AccessGrant",
          "score": 0.09420482069253922
        },
        {
          "class": "UnlockAccount",
          "score": 0.08458791673183441
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.07547003775835037
        },
        {
          "class": "GetAccess",
          "score": 0.06544849276542664
        }
      ]
    }
  },
  {
    "User called to have their current EHB login terminated.": {
      "classPredictions": [
        {
          "class": "RemoveUser",
          "score": 0.1689842790365219
        },
        {
          "class": "LogIntoEHB",
          "score": 0.15436658263206482
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.13201995193958282
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.066211998462677
        },
        {
          "class": "ChangePassword",
          "score": 0.047815222293138504
        }
      ]
    }
  },
  {
    "Grantee states is calling regarding COVID-19 insurance.  She went to St. Joseph hospital and she set up a payment plan for Payment Services.  Her account was pulled up for review.  She has been calling since September last year, she still haven't received an answer.": {
      "classPredictions": [
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.08123278617858887
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.0740683525800705
        },
        {
          "class": "FileComplaint",
          "score": 0.07276859879493713
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.058745093643665314
        },
        {
          "class": "MakeChanges",
          "score": 0.05160098150372505
        }
      ]
    }
  },
  {
    "Caller stating that she is getting some error and she is not sure how to correct the contents that she already out n the report.": {
      "classPredictions": [
        {
          "class": "GetLoan",
          "score": 0.14145077764987946
        },
        {
          "class": "CheckStatus",
          "score": 0.11929143220186234
        },
        {
          "class": "FileComplaint",
          "score": 0.0814434215426445
        },
        {
          "class": "GetUpdate",
          "score": 0.07301202416419983
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.06725732982158661
        }
      ]
    }
  },
  {
    "Caller needed assistance with information for upcoming funds": {
      "classPredictions": [
        {
          "class": "CallForAssistance",
          "score": 0.49317529797554016
        },
        {
          "class": "CallForInformation",
          "score": 0.0852779969573021
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.07851356267929077
        },
        {
          "class": "GetUpdate",
          "score": 0.038383737206459045
        },
        {
          "class": "GetAccess",
          "score": 0.03293389081954956
        }
      ]
    }
  },
  {
    "Grantee needed assistance with enabling account and reset password": {
      "classPredictions": [
        {
          "class": "UnlockAccount",
          "score": 0.226618692278862
        },
        {
          "class": "ResetPassword",
          "score": 0.1461479812860489
        },
        {
          "class": "AccessAccount",
          "score": 0.07852150499820709
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.06420774757862091
        },
        {
          "class": "AccessGrant",
          "score": 0.05485560745000839
        }
      ]
    }
  },
  {
    "User calling calling regarding the Provider Relief Fund/ uninsured Claims": {
      "classPredictions": [
        {
          "class": "CallForInformation",
          "score": 0.6163965463638306
        },
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.05569671839475632
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.04953796789050102
        },
        {
          "class": "CallForAssistance",
          "score": 0.048906609416007996
        },
        {
          "class": "ApplyForProgram",
          "score": 0.02947373501956463
        }
      ]
    }
  },
  {
    "The user would like to have HRSA HR contact information. He stated he has an officer letter and he has questions regarding the onboarding process and his background investigation": {
      "classPredictions": [
        {
          "class": "MakeChanges",
          "score": 0.1090608462691307
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.08505535125732422
        },
        {
          "class": "GetLoan",
          "score": 0.08079187572002411
        },
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.05387595668435097
        },
        {
          "class": "SpeakWithSomeone",
          "score": 0.049656059592962265
        }
      ]
    }
  },
  {
    "the user wanted to speak with someone regarding loan repayment": {
      "classPredictions": [
        {
          "class": "SpeakWithSomeone",
          "score": 0.7633965611457825
        },
        {
          "class": "RemoveUser",
          "score": 0.03133691847324371
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.021140748634934425
        },
        {
          "class": "RegisterAsPD",
          "score": 0.01796068251132965
        },
        {
          "class": "GiveAccess",
          "score": 0.01784067042171955
        }
      ]
    }
  },
  {
    "error message when saving data that was inputed. Jira Reference Id :EHBSOPS-51305": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.2501964867115021
        },
        {
          "class": "ResetPassword",
          "score": 0.0838894173502922
        },
        {
          "class": "GetLoan",
          "score": 0.07245342433452606
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.05976910516619682
        },
        {
          "class": "GetUpdate",
          "score": 0.04600434750318527
        }
      ]
    }
  },
  {
    "the caller applied for the nurse corp scholarship and was checking on an update": {
      "classPredictions": [
        {
          "class": "AskAboutStatus",
          "score": 0.09328939765691757
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.07580814510583878
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.06556566804647446
        },
        {
          "class": "ApplyForProgram",
          "score": 0.05508363991975784
        },
        {
          "class": "RegisterGrant",
          "score": 0.05297994613647461
        }
      ]
    }
  },
  {
    "the user requested their session be terminated": {
      "classPredictions": [
        {
          "class": "RemoveUser",
          "score": 0.11191293597221375
        },
        {
          "class": "ResetPassword",
          "score": 0.09455004334449768
        },
        {
          "class": "AccessAccount",
          "score": 0.09316885471343994
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.08482253551483154
        },
        {
          "class": "RegisterAsPD",
          "score": 0.06146521866321564
        }
      ]
    }
  },
  {
    "the user required assistance with the provider relief fund application": {
      "classPredictions": [
        {
          "class": "CallForInformation",
          "score": 0.5715389251708984
        },
        {
          "class": "CallForAssistance",
          "score": 0.14196522533893585
        },
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.042943838983774185
        },
        {
          "class": "GetUpdate",
          "score": 0.03483475372195244
        },
        {
          "class": "ApplyForProgram",
          "score": 0.022876037284731865
        }
      ]
    }
  },
  {
    "User calling regarding the Loan Repayment Program": {
      "classPredictions": [
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.3132224380970001
        },
        {
          "class": "CallForInformation",
          "score": 0.1958441287279129
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.10723032802343369
        },
        {
          "class": "CallForAssistance",
          "score": 0.08687292784452438
        },
        {
          "class": "GetUpdate",
          "score": 0.0607621856033802
        }
      ]
    }
  },
  {
    "Received call from Leon who needed assistance with accessing his EHB account.": {
      "classPredictions": [
        {
          "class": "AccessAccount",
          "score": 0.19100742042064667
        },
        {
          "class": "AccessGrant",
          "score": 0.0879112035036087
        },
        {
          "class": "GetAccess",
          "score": 0.0816117599606514
        },
        {
          "class": "UnlockAccount",
          "score": 0.08024456351995468
        },
        {
          "class": "RegisterAsPD",
          "score": 0.07126541435718536
        }
      ]
    }
  },
  {
    "The user is calling about a LAL. He was unable to get to the LAL survey (By weekly covid response survey last night.": {
      "classPredictions": [
        {
          "class": "GetUpdate",
          "score": 0.12633642554283142
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.062349528074264526
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.05983968824148178
        },
        {
          "class": "RegisterAsPD",
          "score": 0.0567026361823082
        },
        {
          "class": "CallForInformation",
          "score": 0.0558546781539917
        }
      ]
    }
  },
  {
    "Grantee needs assistance with their VPOP. In their HRSA Force account, all their sites populate. When they go to their VPOP account certain sites do not populate.": {
      "classPredictions": [
        {
          "class": "ReportUnableToLogin",
          "score": 0.1399105191230774
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.07759618014097214
        },
        {
          "class": "AskAboutStatus",
          "score": 0.06922924518585205
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.06052288040518761
        },
        {
          "class": "AccessAccount",
          "score": 0.057814083993434906
        }
      ]
    }
  },
  {
    "For grant H8FCS41401, please administratively close submission tracking number 00295992": {
      "classPredictions": [
        {
          "class": "ExtendDueDate",
          "score": 0.4498751163482666
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.12876692414283752
        },
        {
          "class": "GetUpdate",
          "score": 0.09902237355709076
        },
        {
          "class": "GetAccess",
          "score": 0.04751838743686676
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.02750849723815918
        }
      ]
    }
  },
  {
    "The user stated she is having issues login into her EHB account. She is getting an error message that states, Error : Error occurred during login. \n\nThe user  usually login using her PIV Card.\n\nHHS ID: 2002860684": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.27948418259620667
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.11928106844425201
        },
        {
          "class": "GetUpdate",
          "score": 0.11472636461257935
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.06623279303312302
        },
        {
          "class": "RemoveUser",
          "score": 0.04230892285704613
        }
      ]
    }
  },
  {
    "I haven't been on the EHB for awhile and can't remember my info.  Need to get in to take care of some business. thanks.": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.1168827936053276
        },
        {
          "class": "RemoveUser",
          "score": 0.07406024634838104
        },
        {
          "class": "GetAccess",
          "score": 0.07233893871307373
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.0655464380979538
        },
        {
          "class": "RegisterAsPD",
          "score": 0.06265681982040405
        }
      ]
    }
  },
  {
    "Caller called in needed assistance with applying for grant for Nurse corps": {
      "classPredictions": [
        {
          "class": "ApplyForGrant",
          "score": 0.3414773941040039
        },
        {
          "class": "CallForAssistance",
          "score": 0.11217590421438217
        },
        {
          "class": "RegisterGrant",
          "score": 0.07468477636575699
        },
        {
          "class": "CallForInformation",
          "score": 0.05302388593554497
        },
        {
          "class": "AccessAccount",
          "score": 0.041786037385463715
        }
      ]
    }
  },
  {
    "The caller is new to the EHB and she wanted to make sure that she didn't have any task that was due that she wasn't aware of.": {
      "classPredictions": [
        {
          "class": "MakeChanges",
          "score": 0.1007782593369484
        },
        {
          "class": "ApplyForProgram",
          "score": 0.07680650055408478
        },
        {
          "class": "CheckStatus",
          "score": 0.07063454389572144
        },
        {
          "class": "AskAboutStatus",
          "score": 0.06629054993391037
        },
        {
          "class": "GetLoan",
          "score": 0.055886100977659225
        }
      ]
    }
  },
  {
    "Caller needed assistance with locating onsite visit": {
      "classPredictions": [
        {
          "class": "FindHealthCenter",
          "score": 0.09829779714345932
        },
        {
          "class": "CallForAssistance",
          "score": 0.07344131916761398
        },
        {
          "class": "AccessAccount",
          "score": 0.07322192192077637
        },
        {
          "class": "CallForInformation",
          "score": 0.06806688010692596
        },
        {
          "class": "ApplyForGrant",
          "score": 0.0649620071053505
        }
      ]
    }
  },
  {
    "I changed my password 2 weeks ago but the system will not accept my newest password therefore, I cannot access my acct.  Please assist.  Thank you": {
      "classPredictions": [
        {
          "class": "ResetPassword",
          "score": 0.1382158100605011
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.11429595947265625
        },
        {
          "class": "ChangePassword",
          "score": 0.11085434257984161
        },
        {
          "class": "AccessAccount",
          "score": 0.10636206716299057
        },
        {
          "class": "RemoveUser",
          "score": 0.049828872084617615
        }
      ]
    }
  },
  {
    "RE: EHB tracking # 191137 for Mountain Valleys Health Centers, I cannot get access to the app.  The PD is not able to add me, the Edit menu does not give the opportunity to add users.  Please advise how I get access to the app.  Thanks.": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.1384730339050293
        },
        {
          "class": "GiveAccess",
          "score": 0.0937960147857666
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.064667709171772
        },
        {
          "class": "GetUpdate",
          "score": 0.06392572075128555
        },
        {
          "class": "AccessGrant",
          "score": 0.06290263682603836
        }
      ]
    }
  },
  {
    "A staff person has requested access to the grant folder, but I can't find the request in the EHB for approval.": {
      "classPredictions": [
        {
          "class": "AccessGrant",
          "score": 0.16443276405334473
        },
        {
          "class": "AskAboutStatus",
          "score": 0.1324319839477539
        },
        {
          "class": "AccessAccount",
          "score": 0.11047268658876419
        },
        {
          "class": "GetAccess",
          "score": 0.09361062198877335
        },
        {
          "class": "CallForAssistance",
          "score": 0.06369280815124512
        }
      ]
    }
  },
  {
    "Breyanna called to get assistance with resetting their EHB password.": {
      "classPredictions": [
        {
          "class": "RemoveUser",
          "score": 0.09062914550304413
        },
        {
          "class": "RegisterAsPD",
          "score": 0.08934184908866882
        },
        {
          "class": "UnlockAccount",
          "score": 0.0890764370560646
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.0859512984752655
        },
        {
          "class": "ResetPassword",
          "score": 0.08486979454755783
        }
      ]
    }
  },
  {
    "User calling for assistance with how to create their EHB account. They are getting a error that the email already exists": {
      "classPredictions": [
        {
          "class": "CreateEHBAccount",
          "score": 0.33684492111206055
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.08866691589355469
        },
        {
          "class": "LogIntoEHB",
          "score": 0.06116696819663048
        },
        {
          "class": "CreateAccount",
          "score": 0.04946005716919899
        },
        {
          "class": "GetUpdate",
          "score": 0.04034505784511566
        }
      ]
    }
  },
  {
    "User needed assistance resetting their password because they were unable to log in": {
      "classPredictions": [
        {
          "class": "ResetPassword",
          "score": 0.2513563930988312
        },
        {
          "class": "LogIntoEHB",
          "score": 0.1634267121553421
        },
        {
          "class": "ChangePassword",
          "score": 0.14400693774223328
        },
        {
          "class": "UnlockAccount",
          "score": 0.09817168116569519
        },
        {
          "class": "RemoveUser",
          "score": 0.06417254358530045
        }
      ]
    }
  },
  {
    "User calling for information on how to access their expenditures report that has been change requested": {
      "classPredictions": [
        {
          "class": "AccessAccount",
          "score": 0.18485839664936066
        },
        {
          "class": "GetAccess",
          "score": 0.1130763590335846
        },
        {
          "class": "CallForInformation",
          "score": 0.07366537302732468
        },
        {
          "class": "AccessGrant",
          "score": 0.07304167747497559
        },
        {
          "class": "GetUpdate",
          "score": 0.0662311464548111
        }
      ]
    }
  },
  {
    "The caller needed access to grant H80CS00594 and to register as PD for this grant.": {
      "classPredictions": [
        {
          "class": "GetAccess",
          "score": 0.2641046345233917
        },
        {
          "class": "AccessGrant",
          "score": 0.18488819897174835
        },
        {
          "class": "AccessAccount",
          "score": 0.11484132707118988
        },
        {
          "class": "RegisterAsPD",
          "score": 0.062295667827129364
        },
        {
          "class": "ApplyForGrant",
          "score": 0.04400850087404251
        }
      ]
    }
  },
  {
    "User called regarding claims from the Provider Relief Fund": {
      "classPredictions": [
        {
          "class": "CallForInformation",
          "score": 0.47124210000038147
        },
        {
          "class": "AskAboutLoanRepaymentProgram",
          "score": 0.06882056593894958
        },
        {
          "class": "ApplyForProgram",
          "score": 0.06274039298295975
        },
        {
          "class": "FileComplaint",
          "score": 0.061408914625644684
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.04370222985744476
        }
      ]
    }
  },
  {
    "User called wanting information on FQHC's and trying to find information on them in their state, but stated to find each one you needed a zip code on the website, so user wanted to know if there was a list\nEmail is ccervantes@dentistry.ucla.edu": {
      "classPredictions": [
        {
          "class": "GiveAccess",
          "score": 0.17275464534759521
        },
        {
          "class": "RemoveUser",
          "score": 0.12113446742296219
        },
        {
          "class": "CreateEHBAccount",
          "score": 0.0494803786277771
        },
        {
          "class": "FileComplaint",
          "score": 0.048144835978746414
        },
        {
          "class": "AddUser",
          "score": 0.0426812544465065
        }
      ]
    }
  },
  {
    "There was an unexpected error while processing your request. Please try again by refreshing the page or if the problem persists, please contact Call Center. \n\nReference Id: c27caa5f-aa53-48cc-afaa-bae06af81ab5. Jira Reference Id :EHBSOPS-46940": {
      "classPredictions": [
        {
          "class": "ExtendDeadline\t",
          "score": 0.12656696140766144
        },
        {
          "class": "LogIntoEHB",
          "score": 0.1110592931509018
        },
        {
          "class": "RemoveUser",
          "score": 0.10294171422719955
        },
        {
          "class": "RegisterAsPD",
          "score": 0.07989172637462616
        },
        {
          "class": "GetUpdate",
          "score": 0.07240801304578781
        }
      ]
    }
  },
  {
    "User called in stating they were trying to log in to EHB but get the error that the username is not recognized": {
      "classPredictions": [
        {
          "class": "LogIntoEHB",
          "score": 0.4967406988143921
        },
        {
          "class": "RemoveUser",
          "score": 0.07607833296060562
        },
        {
          "class": "ChangePassword",
          "score": 0.07272645086050034
        },
        {
          "class": "ExtendDeadline\t",
          "score": 0.03618251904845238
        },
        {
          "class": "RegisterAsPD",
          "score": 0.025319209322333336
        }
      ]
    }
  },
  {
    "Caller wanted to know if this was the number to it hardware support": {
      "classPredictions": [
        {
          "class": "AskAboutStatus",
          "score": 0.18841010332107544
        },
        {
          "class": "GetLoan",
          "score": 0.1449470967054367
        },
        {
          "class": "CheckStatus",
          "score": 0.0829819068312645
        },
        {
          "class": "ApplyForProgram",
          "score": 0.059138644486665726
        },
        {
          "class": "RegisterAsPD",
          "score": 0.036483101546764374
        }
      ]
    }
  },
  {
    "Nick called in needed assistance with accessing a previous submitted  Performance Report.": {
      "classPredictions": [
        {
          "class": "AccessAccount",
          "score": 0.13188064098358154
        },
        {
          "class": "CallForAssistance",
          "score": 0.1203964576125145
        },
        {
          "class": "SubmitPriorApprovalRequest",
          "score": 0.11105695366859436
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.0912664532661438
        },
        {
          "class": "AccessGrant",
          "score": 0.07591762393712997
        }
      ]
    }
  },
  {
    "Can you please reset my password? For some reason it never recognizes my password and I have wait 30 minutes and then create a new password to access my account": {
      "classPredictions": [
        {
          "class": "ResetPassword",
          "score": 0.326000452041626
        },
        {
          "class": "AccessAccount",
          "score": 0.10433131456375122
        },
        {
          "class": "ChangePassword",
          "score": 0.10241591185331345
        },
        {
          "class": "LogIntoEHB",
          "score": 0.06914660334587097
        },
        {
          "class": "ReportUnableToLogin",
          "score": 0.04969894886016846
        }
      ]
    }
  },
  {
    "User calling to get information on hrsa-21-093 application they applied but got errors, User wanted assistance on what those errors were.": {
      "classPredictions": [
        {
          "class": "GiveAccess",
          "score": 0.11310163140296936
        },
        {
          "class": "RegisterAsPD",
          "score": 0.0973128080368042
        },
        {
          "class": "GetUpdate",
          "score": 0.0929718017578125
        },
        {
          "class": "GetLoan",
          "score": 0.08780723065137863
        },
        {
          "class": "RemoveUser",
          "score": 0.06019927188754082
        }
      ]
    }
  }
]
import json
response_dict = {}
unidentified_intent_dict = {}
for ele in json_list:
    for key,value in ele.items():
        if (value['classPredictions'] [0]['score']) >= 0.4:
            response_dict[key] = value['classPredictions']

        else:
            response_dict[key] = 'Unidentified Intent'
            unidentified_intent_dict[key] = value['classPredictions']

with open('response_dict.json', 'w') as fp:
    fp.write(json.dumps(response_dict, indent=4))

with open('unidentified_intent_dict.json', 'w') as f:
    f.write(json.dumps(unidentified_intent_dict, indent=4)
    )


test = "test"

    

