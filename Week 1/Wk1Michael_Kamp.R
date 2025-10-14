# =========================================
# Michael Kamp
# Data785 Week 1 Assignment
# September 8, 2025
# =========================================

# Load required libraries
library(ISLR)
library(class)
library(ggplot2)
library(gridExtra)
library(grid)
library(caret)
library(e1071)
library(patchwork)
library(lattice)

# =========================================
# Create Output folder if it doesn't exist
# =========================================
dir.create("Output", showWarnings = FALSE)

# Load Auto dataset
data(Auto)
summary(Auto)

# =========================================
# 14(a) Create mpg01
# =========================================
mpg_median <- median(Auto$mpg)
mpg01 <- ifelse(Auto$mpg > mpg_median, 1, 0)
Auto2 <- data.frame(Auto, mpg01)

# =========================================
# 14(b) Boxplots for association with mpg01
# =========================================
vars <- c("cylinders", "displacement", "horsepower", "weight", "acceleration", "year")

plots <- lapply(vars, function(v) {
  ggplot(Auto2, aes(x = factor(mpg01), y = .data[[v]], fill = factor(mpg01))) +
    geom_boxplot(alpha = 0.7, outlier.color = "black") +
    scale_fill_manual(values = c("0" = "lightblue", "1" = "yellow"),
                      name = "mpg01",
                      labels = c("0 (Low MPG)", "1 (High MPG)")) +
    labs(title = paste(v, "vs mpg01"),
         x = "mpg01",
         y = v) +
    theme_minimal(base_size = 12) +
    theme(legend.position = "none")
})

# Combine plots into grid (3 rows x 2 columns)
combined_boxplots <- (plots[[1]] | plots[[2]]) /
  (plots[[3]] | plots[[4]]) /
  (plots[[5]] | plots[[6]])

# Save combined boxplots as PNG (larger size for Word)
ggsave("Output/Boxplots_vs_mpg01.png", combined_boxplots, width = 12, height = 15, dpi = 300)

# =========================================
# Scatterplot matrix
# =========================================
png("Output/Scatterplot_Matrix.png", width=1200, height=1200, res=300)
pairs(Auto2[, c("mpg01", "cylinders", "displacement", "horsepower", "weight")],
      col = Auto2$mpg01 + 1,
      main = "Scatterplot Matrix")
dev.off()

# =========================================
# 14(c) Train/Test Split (70/30)
# =========================================
set.seed(1)
train_index <- sample(1:nrow(Auto2), 0.7 * nrow(Auto2))
train <- Auto2[train_index, ]
test <- Auto2[-train_index, ]

cat("Training set:", nrow(train), "rows\n")
cat("Test set:    ", nrow(test),  "rows\n")

# =========================================
# 14(h) KNN analysis
# =========================================
predictors <- c("cylinders", "displacement", "weight")  # strongest predictors

# Scale predictors
train.X <- scale(train[, predictors])
test.X  <- scale(test[, predictors],
                 center = attr(train.X, "scaled:center"),
                 scale  = attr(train.X, "scaled:scale"))

train.Y <- train$mpg01
test.Y  <- test$mpg01

# Random K values selection
set.seed(42)
K <- sample(seq(1 ,25, by = 2), size=6) # chooses 6 random odd numbers between 1 and 25
Errors <- numeric(length(K))
accuracy_results <- data.frame(K = K, Test_Error = NA, Accuracy = NA)

# Compute test errors and accuracy
for (i in 1:length(K)) {
  set.seed(1) # reproducible
  knn.pred <- knn(train.X, test.X, train.Y, k = K[i])
  Errors[i] <- mean(knn.pred != test.Y)
  accuracy_results$Test_Error[i] <- Errors[i]
  accuracy_results$Accuracy[i] <- mean(knn.pred == test.Y)
}

print(accuracy_results)

# Identify best K by test error
bestK <- K[which.min(Errors)]
bestError <- min(Errors)

# Save KNN test error plot as PNG (larger size)
knn_plot <- ggplot(accuracy_results, aes(x = K, y = Test_Error)) +
  geom_line(color = "blue", size = 1) +
  geom_point(color = "orange", size = 3) +
  geom_text(aes(label = round(Test_Error, 3)), vjust = 1.5, color = "black", size = 4) +
  annotate("point", x = bestK, y = bestError, color = "red", size = 4) +
  annotate("text", x = bestK, y = bestError - 0.015,  
           label = paste("Best K =", bestK),
           color = "purple", size = 5) +
  labs(title = "KNN Test Error vs Random K",
       x = "Number of Neighbors (K)",
       y = "Test Error") +
  theme_minimal(base_size = 14) +
  theme(plot.margin = margin(t = 10, r = 10, b = 50, l = 10))

ggsave("Output/KNN_TestError_vs_K.png", knn_plot, width = 10, height = 8, dpi = 300)

# =========================================
# Cross-Validation to find optimal K
# =========================================
set.seed(1)
ctrl <- trainControl(method = "cv", number = 10)
cv_knn <- train(
  factor(mpg01) ~ cylinders + displacement + weight,
  data = train,
  method = "knn",
  trControl = ctrl,
  tuneGrid = data.frame(k = 1:15)
)

print(cv_knn)

# Save CV plot (larger size)
png("Output/KNN_CV_Plot.png", width=1200, height=800, res=300)
plot(cv_knn)
dev.off()

best_k_cv <- cv_knn$bestTune$k
cat("Optimal K from CV:", best_k_cv, "\n")

# =========================================
# Confusion matrices for all K values
# =========================================
all_k <- unique(c(K, best_k_cv))
conf_matrices <- list()

for (k in all_k) {
  knn.pred <- knn(train.X, test.X, train.Y, k = k)
  cm <- table(Predicted = knn.pred, Actual = test.Y)
  conf_matrices[[paste0("K=", k)]] <- cm
  cat("\nConfusion Matrix for K =", k, "\n")
  print(cm)
  cat("Accuracy:", mean(knn.pred == test.Y), "\n")
}

# =========================================
# Save all confusion matrices as single PNG (larger size)
# =========================================
conf_grobs <- lapply(names(conf_matrices), function(k) {
  cm <- conf_matrices[[k]]
  arrangeGrob(
    textGrob(paste("Confusion Matrix for", k),
             gp = gpar(fontsize = 12, fontface = "bold")),
    tableGrob(cm, rows = NULL,
              theme = ttheme_default(
                core = list(fg_params = list(cex = 0.7, col = "black")),
                colhead = list(fg_params = list(cex = 0.8, fontface = "bold"))
              )),
    ncol = 1,
    heights = c(0.3, 1)
  )
})

combined_conf <- do.call(grid.arrange, c(conf_grobs, ncol = 1))

png("Output/All_Confusion_Matrices.png", width = 1200, height = 1800, res=300)
grid.draw(combined_conf)
dev.off()
