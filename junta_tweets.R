library(readr)
library(dplyr)

arquivos = grep(".csv", dir(), value = T)

bancos = lapply(arquivos, read_csv)
bancos[[1]]

completo = bancos[[1]]

for (i in 2:length(bancos)) {
  completo = rbind(completo, bancos[[i]])
}

completo = completo %>% select(-X1)
completo
options(scipen = 999)
completo

write_csv(completo, "tweets_debate20180809_completo.csv")
