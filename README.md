Calculation of word co-occurrence in text data - suitable as a preprocessing step before visualizing a text-based network (analogous to the "coocurence" function from the "udpipe" package implemented in R)

The inputs are:
  1) sentences - a list of texts,
  2) window-size - the number of words within which to consider co-occurrence (for example, if the parameter is equal to 3, then it is considered that word X meets word Y if it is within +/- 3 words from it),
  3) min_edges - the minimum number of links required for further analysis (for example, if the parameter is equal to 3, then the final dataframe will not include links of words that occur less than 3 times).

The function outputs a dataframe without duplicates with 3 columns: word X; word Y; the number of times they occur together. 

The output can be used for visualization of a network in Gephi or NetworkX.
