import androidhelper

droid = androidhelper.Android()
message = droid.dialogGetInput('by jacob990', 'cosa vuoi che dico?').result
droid.ttsSpeak(message)
