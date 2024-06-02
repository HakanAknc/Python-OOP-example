def calculate_statistics(numbers):
    """
    Verilen bir sayı listesi için çeşitli istatistiksel hesaplamalar yapar.
    
    Parametreler:
    numbers (list): İstatistik hesaplamalarının yapılacağı sayı listesi.
    
    Returns:
    dict: Hesaplanan istatistiksel değerlerin sözlük halini döndürür.
    """

    if not numbers:
        return None
    
    statistics = {
        'count': len(numbers),               # 'count': Listedeki eleman sayısı.
        'sum': sum(numbers),                 # 'sum': Listedeki elemanların toplamı.
        'mean': sum(numbers) / len(numbers), # 'mean': Elemanların ortalaması.
        'min': min(numbers),                 # 'min': Listenin en küçük elemanı.
        'max': max(numbers)                  # 'max': Listenin en büyük elemanı.
    }

    squared_differences = [(x - statistics['mean']) ** 2 for x in numbers]
    variance = sum(squared_differences) / len(numbers)
    statistics['variance'] = variance
    statistics['std_deviation'] = variance ** 0.5

    return statistics


# Örnek bir sayı listesi
numbers = [23, 45, 12, 67, 89, 34, 56, 78, 98, 41]

# İstatistiksel hesaplamaları yap ve sonuçları görüntüle
result = calculate_statistics(numbers)
print("İstatistiksel Hesaplamalar:")
print(f"Toplam: {result['sum']}")
print(f"Ortalama: {result['mean']}")
print(f"En Küçük Değer: {result['min']}")
print(f"En Büyük Değer: {result['max']}")
print(f"Varyans: {result['variance']}")
print(f"Standart Sapma: {result['std_deviation']}")