library(data.table)
library(tidyverse)

df1= fread("mnt/git_repos/player_name_data_scraping/src/player_names.csv", header = TRUE)
df2=fread("mnt/git_repos/player_name_data_scraping/src/player_names_2.csv", header = TRUE)
df3=fread("mnt/git_repos/player_name_data_scraping/src/player_names_3.csv", header = TRUE)
df_All =rbind(df1,df2,df3)
df_All_trimmed <- df_All[,2:4]
df_wide = reshape(df_All, idvar = "name", timevar = "value", direction = "wide")
df_wide_jamaica <- dplyr::filter(df_wide, grepl('Jamaica', value.Nationality))
df_wide_jamaica%>% write_csv("Downloads/jamaican_player.csv")