def zodiac_sign(day, month):
    if month == 12:
        return 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        return 'Capricorn' if (day < 20) else 'Aquarius'
    # ... (other months)
    elif month == 3:
        return 'Pisces' if (day < 21) else 'Aries'
    else:
        return "Invalid date"
