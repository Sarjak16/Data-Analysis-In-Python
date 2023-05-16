#concatenation basics..........................................................................................................
# Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.


# Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.

# Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master,
                               tracks_ride, tracks_st], ignore_index= True,
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master,
                               tracks_ride, tracks_st], join='inner',
                               sort=True)
print(tracks_from_albums)

# concatenating with keys...........................................................................................................................................
# Concatenate the three tables together vertically in order with the oldest month first, adding '7Jul', '8Aug', and '9Sep' as keys for their respective months,
# and save to variable avg_inv_by_month.
# Use the .agg() method to find the average of the total column from the grouped invoices.
# Create a bar chart of avg_inv_by_month.

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep ],
                            keys=['7Jul', '8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind= 'bar')
plt.show()
