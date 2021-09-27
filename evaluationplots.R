dd = t(read.table('D:\\Projects\\Python\\PycharmProjects\\DLIB_Pytorch_Kropki\\LSTM_test\\lista_procentu_tych_samych.txt', sep=',', header = FALSE))
dd = data.frame(y = as.vector(dd),x = 1:length(dd))
fit3 <- lm( dd$y~poly(dd$x,10) )
plot(dd$x, dd$y, type='l', xlab = "p", ylab = "V(Xi,p)")
#lines(dd$x, dd$y)
#lines(dd$x, predict(fit3, data.frame(x=dd$x)), col='blue')
#predd = predict(fit3, data.frame(x=dd$x))
#which(predd==max(predd))
#max(predict(fit3, data.frame(x=dd$x)))
#points(31, predd[31], col="red")
#http://users.stat.umn.edu/~helwig/notes/smooth-spline-notes.html
library(npreg)
mod.smsp <- smooth.spline(dd$x, dd$y, nknots = 100)
lines(dd$x, mod.smsp$y, lwd = 2, col="green")

x1 = 32
points(x1, mod.smsp$y[x1], col="red")
lines(c(x1, x1), c(0,0.28), col="red")
text(x1+8, mod.smsp$y[x1] + 0.01, "(32, 0.26)", col="red")

x1 = 17
lines(c(x1, x1), c(0,0.28), col="red")
points(x1, mod.smsp$y[x1], col="red")
text(x1+8, mod.smsp$y[x1] + 0.01, "(17, 0.22)", col="red")

x1 = 53
lines(c(x1, x1), c(0,0.28), col="red")
points(x1, mod.smsp$y[x1], col="red")
text(x1+8, mod.smsp$y[x1] + 0.01, "(53, 0.26)", col="red")

x1 = 86
lines(c(x1, x1), c(0,0.28), col="red")
points(x1, mod.smsp$y[x1], col="red")
text(x1+8, mod.smsp$y[x1] + 0.01, "(86, 0.27)", col="red")




#mod.smsp$y[2:100] - mod.smsp$y[1:99]


path_to_results = "d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\"
all = read.table("d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all.txt" , sep=';', header = FALSE)

ViT_B32 = read.table('d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all_ViT_B32.txt', sep=';', header = FALSE)
ViT_B16 = read.table('d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all_ViT_B16.txt', sep=';', header = FALSE)
RN50 = read.table('d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all_RN50.txt', sep=';', header = FALSE)
RN101 = read.table('d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all_RN101.txt', sep=';', header = FALSE)
RN50x4 = read.table('d:\\Publikacje\\Evaluation of methods for image-text matching\\wyniki\\wyniki_statystyki_all_RN50x4.txt', sep=';', header = FALSE)


kolumny = c("ile_bierzemy",
"maen_l_intersect",
"std_l_intersect",
"men_union_len",
"std_union_len",
"mean_max_score",
"std_max_score",
"median_max_score",
"max_max_score",
"min_max_score",
"mean_l_m12",
"std_l_m12",
"mean_l_m13",
"std_l_m13")

#M12 i M13 ustawiæ na NA jeœli wychodzi 1
colnames(all) = kolumny
colnames(ViT_B16) = kolumny
colnames(ViT_B32) = kolumny
colnames(RN50) = kolumny
colnames(RN101) = kolumny
colnames(RN50x4) = kolumny

sink(paste(path_to_results, "M12M13.txt", sep = ""))

pomocdf = ViT_B16[3,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("ViT-B32",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = ViT_B32[3,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("ViT-B32 (BERT)",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = RN50[3,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("RN50",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = RN101[3,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("RN101",s1,s2, sep = " & ")
cat(napis)
cat("\n")


pomocdf = RN50x4[3,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("RN50x4",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = all[17,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("TIPS p=17",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = all[32,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("TIPS p=32",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = all[53,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("TIPS p=53",s1,s2, sep = " & ")
cat(napis)
cat("\n")

pomocdf = all[86,]
s1 = paste(round(pomocdf$mean_l_m12,3),"±", round(pomocdf$std_l_m12,3), sep="")
s2 = paste(round(pomocdf$mean_l_m13,3),"±", round(pomocdf$std_l_m13,3), sep="")
napis = paste("TIPS p=86",s1,s2, sep = " & ")
cat(napis)
cat("\n")

sink()


sink(paste(path_to_results, "TIPS_wyniki.txt", sep = ""))
pomocdf = all[1,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")


pomocdf = all[2,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

pomocdf = all[3,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

pomocdf = all[17,]
napis = paste(pomocdf$ile_bierzemy, 
           paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
           paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
           round(pomocdf$min_max_score,2),
           round(pomocdf$max_max_score,2),
           round(pomocdf$median_max_score,2),
           paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

pomocdf = all[22,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

pomocdf = all[52,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

pomocdf = all[86,]
napis = paste(pomocdf$ile_bierzemy, 
              paste(round(pomocdf$maen_l_intersect,2),"±", round(pomocdf$std_l_intersect,2), sep=""),
              paste(round(pomocdf$men_union_len,2),"±", round(pomocdf$std_union_len,2), sep=""),
              round(pomocdf$min_max_score,2),
              round(pomocdf$max_max_score,2),
              round(pomocdf$median_max_score,2),
              paste(round(pomocdf$mean_max_score,2),"±", round(pomocdf$std_max_score,2), sep=""), sep=" & ")
cat(napis)
cat("\n")

sink()

ces.size = 1.5
plot(all$maen_l_intersect, type="l", xlab = "p", ylab = "In(Xi,p)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$men_union_len, type="l", xlab = "p", ylab = "Un(Xi,p)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$mean_max_score, type="l", xlab = "p", ylab = "sim_mean(X)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$median_max_score, type="l", xlab = "p", ylab = "sim_med(X)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$min_max_score, type="l", xlab = "p", ylab = "sim_min(X)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$max_max_score, type="l", xlab = "p", ylab = "sim_max(X)", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$mean_l_m12, type="l", xlab = "p", ylab = "M1,2", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)
plot(all$mean_l_m13, type="l", xlab = "p", ylab = "M1,3", col = "red", cex.lab=ces.size, cex.axis=ces.size, cex.main=ces.size, cex.sub=ces.size)







all$mean_l_m12
ViT_B32$mean_l_m12


all$mean_l_m13
ViT_B32$mean_l_m13