import csv
from math import sqrt

def sample_mean(samples):
    n = len(samples)

    return sum(samples) / n


def sample_variance_and_std_deviation(samples, sample_mean):
    n = len(samples)

    # Performing list comphrehension in order for the algorithm
    # being faster
    variance = sum(
        [(x - sample_mean)**2 for x in samples]
    ) / n
    return variance, sqrt(variance)


def sample_covariance(sample1, sample1_mean, sample2, sample2_mean):
    n = len(sample1)

    return sum(
        [
            (sample1[idx] - sample1_mean) * (sample2[idx] - sample2_mean)
            for idx in range(n)
        ]
    ) / n


def sample_correlation_coefficient(
    sample1_std_deviation,
    sample2_std_deviation,
    samples_covariance
    ):
    return samples_covariance / (sample1_std_deviation * sample2_std_deviation)


def read_csv_file(filename):
    x2 = []
    x3 = []
    with open(filename, newline="") as csvfile:
        csv_reader = csv.DictReader(
            csvfile,
            delimiter=";"
        )
        for row in csv_reader:
            x2.append(float(row["X2"]))
            x3.append(float(row["X4"]))
    
    return x2, x3
            

def main():
    x2, x4 = read_csv_file("./ENB2012_data.csv")

    # Computing means
    x2_mean = sample_mean(x2)
    x4_mean = sample_mean(x4)

    print("Attributes means")
    print(f"X2: m = {x2_mean}")
    print(f"X4: m = {x4_mean}")

    # Computing variances and std_deviations
    x2_variance, x2_std_deviation = sample_variance_and_std_deviation(x2, x2_mean)
    x4_variance, x4_std_deviation = sample_variance_and_std_deviation(x4, x4_mean)

    print("Attributes variance and std deviations")
    print(f"X2: sˆ2 = {x2_variance}; s = {x2_std_deviation}")
    print(f"X4: sˆ2 = {x4_variance}; s = {x4_std_deviation}")

    # Computing the covariance and sample correlation coeff
    x2_x4_covariance = sample_covariance(x2, x2_mean, x4, x4_mean)
    corr_coeff = sample_correlation_coefficient(
        x2_std_deviation, x4_std_deviation, x2_x4_covariance
    )
    print("Attibutes covariance and correlation coefficient")
    print(f"s_x2_x4 = {x2_x4_covariance}; r_x2_x4 = {corr_coeff}")
    

if __name__ == "__main__":
    main()