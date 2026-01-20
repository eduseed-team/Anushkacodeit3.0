import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import ephem

def calculate_moon_phase(date):
    """Calculate the moon phase for a given date."""
    moon = ephem.Moon(date)
    # Moon phase as a fraction (0-1)
    return moon.phase / 100.0

def get_moon_phase_name(phase):
    """Convert moon phase fraction to name."""
    if phase < 0.05 or phase > 0.95:
        return "New Moon"
    elif 0.05 <= phase < 0.20:
        return "Waxing Crescent"
    elif 0.20 <= phase < 0.30:
        return "First Quarter"
    elif 0.30 <= phase < 0.45:
        return "Waxing Gibbous"
    elif 0.45 <= phase < 0.55:
        return "Full Moon"
    elif 0.55 <= phase < 0.70:
        return "Waning Gibbous"
    elif 0.70 <= phase < 0.80:
        return "Last Quarter"
    else:
        return "Waning Crescent"

def plot_moon_calendar(year, month):
    """Plot a moon phase calendar for a specific month and year."""
    # Create a date object for the first day of the month
    start_date = datetime(year, month, 1)
    
    # Determine the number of days in the month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    
    days_in_month = (next_month - start_date).days
    
    # Calculate moon phases for each day
    dates = [start_date + timedelta(days=i) for i in range(days_in_month)]
    phases = [calculate_moon_phase(date) for date in dates]
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot the moon phase curve
    plt.plot(range(1, days_in_month + 1), phases, 'b-', linewidth=2)
    
    # Add markers for key moon phases
    for i, phase in enumerate(phases):
        if get_moon_phase_name(phase) in ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]:
            plt.plot(i + 1, phase, 'ro', markersize=10)
            plt.text(i + 1, phase + 0.03, f"{dates[i].day}: {get_moon_phase_name(phase)}", 
                     ha='center', va='bottom')
    
    # Set the plot limits and labels
    plt.xlim(1, days_in_month)
    plt.ylim(0, 1)
    plt.xlabel('Day of Month')
    plt.ylabel('Moon Phase')
    plt.title(f'Moon Phases for {start_date.strftime("%B %Y")}')
    plt.grid(True)
    
    # Add a legend explaining the moon phases
    plt.figtext(0.15, 0.02, "0.0 = New Moon, 0.25 = First Quarter, 0.5 = Full Moon, 0.75 = Last Quarter", 
                ha="left", fontsize=10)
    
    plt.tight_layout()
    plt.show()

def print_moon_calendar(year, month):
    """Print a text-based moon phase calendar for a specific month and year."""
    # Create a date object for the first day of the month
    start_date = datetime(year, month, 1)
    
    # Determine the number of days in the month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    
    days_in_month = (next_month - start_date).days
    
    print(f"\nMoon Phase Calendar for {start_date.strftime('%B %Y')}")
    print("-" * 50)
    print(f"{'Day':<5}{'Date':<12}{'Phase %':<10}{'Moon Phase':<20}")
    print("-" * 50)
    
    # Calculate and print moon phases for each day
    for i in range(days_in_month):
        date = start_date + timedelta(days=i)
        phase = calculate_moon_phase(date)
        phase_name = get_moon_phase_name(phase)
        
        print(f"{date.day:<5}{date.strftime('%Y-%m-%d'):<12}{phase*100:<10.1f}{phase_name:<20}")

# Example usage
if __name__ == "__main__":
    # Get current year and month
    now = datetime.now()
    year = now.year
    month = now.month
    
    # Print text calendar
    print_moon_calendar(year, month)
    
    # Plot visual calendar
    plot_moon_calendar(year, month)

