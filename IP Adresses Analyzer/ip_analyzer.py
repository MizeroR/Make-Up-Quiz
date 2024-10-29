import heapq
from collections import defaultdict

def process_log_file(log_file_name, n, output_file_nme):
    ip_requests_counts = defaultdict(int)

    # Reads the log file lines to count requests from each IP
    with open(log_file_name, 'r') as log_data:
        for record in log_data:
            # Removes whitespace and skips empty lines
            record = record.strip()
            if not record:
                continue  

            # Split the line and handle potential unpacking issues
            ip_and_count = record.split(',')
            if len(ip_and_count) != 2:
                print(f"Warning: Line skipped due to unexpected format: {record}")
                continue  # Skip lines that don't have exactly 2 parts

            ip_address, request_total = ip_and_count
            try:
                ip_requests_counts[ip_address] += int(request_total)
            except ValueError:
                print(f"Warning: Invalid count value for IP {ip_address}: {request_total}")
                continue  # Skip lines with invalid count values

    # Create a max heap for the top n IP addresses
    max_heap = []
    for ip, request_total in ip_requests_counts.items():
        # Push negative count to create a max heap
        heapq.heappush(max_heap, (-request_total, ip))

    # Extract top n IP addresses
    top_n = []
    for _ in range(n):
        if max_heap:
            request_total, ip = heapq.heappop(max_heap)
            top_n.append((-request_total, ip))

    # Sort the results first by count (descending) then by IP (ascending)
    top_n.sort(key=lambda x: (-x[0], x[1]))

    # Write results to output file with ranking importance
    with open(output_file_nme, 'w') as output_name:
        for rank, (request_total, ip) in enumerate(top_n, start=1):
            output_name.write(f"{rank}, {ip}, {request_total}\n")

# Example usage
if __name__ == "__main__":
    process_log_file('C:/Users/HP/Make-Up Quiz/IP Adresses Analyzer/sample_01_easy.log', 3, 'sample_01_easy_result_n3.txt')

