def optimal_page_replacement(reference_string, frame_count):
    frames, page_faults = [], 0
    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Menentukan halaman yang waktu penggunaannya terjauh di masa depan
                future_usage = {frame: (reference_string[i + 1:].index(frame) if frame in reference_string[i + 1:] else float('inf'))
                                 for frame in frames}
                farthest_page = max(future_usage, key=future_usage.get)
                frames[frames.index(farthest_page)] = page
            page_faults += 1
    return page_faults

def lru_page_replacement(reference_string, frame_count):
    frames, page_faults = [], 0
    recent_usage = {}

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Menemukan halaman yang paling lama tidak digunakan
                lru_page = min(recent_usage, key=recent_usage.get)
                frames[frames.index(lru_page)] = page  # Ganti halaman LRU
            page_faults += 1
        # Memperbarui penggunaan terbaru
        recent_usage[page] = i

    return page_faults

def fifo_page_replacement(reference_string, frame_count):
    frames, page_faults = [], 0
    queue = []

    for page in reference_string:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
                queue.append(page)
            else:
                # Mengganti halaman yang pertama kali masuk (FIFO)
                first_in = queue.pop(0)
                frames[frames.index(first_in)] = page
                queue.append(page)  # Menambahkan halaman baru ke queue
            page_faults += 1
        else:
            # Jika halaman sudah ada, tidak perlu menambah page fault
            # Memperbarui posisi halaman yang sudah ada di FIFO queue
            queue.remove(page)
            queue.append(page)

    return page_faults

# Contoh referensi string dan jumlah frame
reference_string = [5, 1, 4, 6, 1, 7, 1, 8, 6, 7, 1, 7, 6]
frame_count = 3

# Menjalankan simulasi untuk ketiga algoritma
optimal_faults = optimal_page_replacement(reference_string, frame_count)
lru_faults = lru_page_replacement(reference_string, frame_count)
fifo_faults = fifo_page_replacement(reference_string, frame_count)

print("Jumlah Page Faults dengan Algoritma Optimal:", optimal_faults)
print("Jumlah Page Faults dengan Algoritma LRU:", lru_faults)
print("Jumlah Page Faults dengan Algoritma FIFO:", fifo_faults)
