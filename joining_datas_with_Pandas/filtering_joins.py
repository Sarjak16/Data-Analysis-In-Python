# anti join...................................................................................................................................

# Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='empl_cust', 
                            how='left', indicator= True)

# Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the result to srid_list.
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] =='left_only' 'srid']

# Subset the employees table and select those rows where the srid is in the variable srid_list and print the results.

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# semi join........................................................................................................................................................
# Merge non_mus_tcks and top_invoices on tid using an inner join. Save the result as tracks_invoices.
# Use .isin() to subset the rows of non_mus_tck where tid is in the tid column of tracks_invoices. Save the result as top_tracks.
# Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
# Merge cnt_by_gid with the genres table on gid and print the result.

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
