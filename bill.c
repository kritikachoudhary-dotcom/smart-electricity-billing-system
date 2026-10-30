
#include <stdio.h>
#include <stdarg.h>

/* Variadic function to add multiple unit values */
double sum_units(int count, ...)
{
    va_list args;
    double total = 0.0;

    va_start(args, count);

    for (int i = 0; i < count; i++)
    {
        total += va_arg(args, double);
    }

    va_end(args);

    return total;
}

/* Calculate total units based on number of inputs */
double calculate_units(int count, double units[])
{
    switch (count)
    {
        case 1:
            return sum_units(1, units[0]);

        case 2:
            return sum_units(2, units[0], units[1]);

        case 3:
            return sum_units(3, units[0], units[1], units[2]);

        case 4:
            return sum_units(4, units[0], units[1],
                             units[2], units[3]);

        case 5:
            return sum_units(5, units[0], units[1],
                             units[2], units[3], units[4]);

        default:
            return -1;
    }
}

/* Progressive electricity tariff */
double calculate_energy_charge(double units)
{
    if (units <= 100)
        return units * 2.0;

    else if (units <= 200)
        return 200 + (units - 100) * 3.5;

    else if (units <= 500)
        return 550 + (units - 200) * 5.0;

    else
        return 2050 + (units - 500) * 7.0;
}

int main()
{
    int count;
    double units[5];

    if (scanf("%d", &count) != 1 ||
        count < 1 || count > 5)
    {
        return 1;
    }

    for (int i = 0; i < count; i++)
    {
        if (scanf("%lf", &units[i]) != 1 ||
            units[i] < 0 || units[i] > 1000000)
        {
            return 1;
        }
    }

    double total_units = calculate_units(count, units);

    if (total_units < 0)
        return 1;

    double energy_charge =
        calculate_energy_charge(total_units);

    double fixed_charge = 50.0;
    double subtotal = energy_charge + fixed_charge;
    double tax = subtotal * 0.05;
    double final_bill = subtotal + tax;

    /* Output results for Python */
    printf("%.2f\n", total_units);
    printf("%.2f\n", energy_charge);
    printf("%.2f\n", fixed_charge);
    printf("%.2f\n", tax);
    printf("%.2f\n", final_bill);

    return 0;
}
