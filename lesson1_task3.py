enter_symbol = '\n#'  # enter\n",
tabulation_symbol = '\t'  # tab\n",
ln = '#' * 9  # line\n",
o_letter = ln + (enter_symbol + tabulation_symbol*2+'#')*3+'\n' + ln
h_letter = (enter_symbol+tabulation_symbol*2+'#')*2 + '\n' + ln + (enter_symbol+tabulation_symbol*2+'#')*2
print(o_letter)
print(h_letter)
