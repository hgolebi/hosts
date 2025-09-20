# nazwa pliku wejściowego
input_file = "my"
# nazwa pliku wyjściowego
output_file = "output.txt"

www_entries = []

with open(input_file, "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        line = line.strip()
        if not line:
            continue  # pomiń puste linie
        # podział na IP i domenę - pierwszy element to IP, reszta to domeny
        parts = line.split()
        if len(parts) < 2:
            continue  # pomiń linie bez domeny
        # sprawdzamy każdą domenę w linii
        domain = parts[1]
        www_entries.append(f"0.0.0.0    {domain}")
        www_entries.append(f"0.0.0.0    www.{domain}")


# zapisanie wyników do nowego pliku
with open(output_file, "w") as f:
    for entry in www_entries:
        f.write(entry + "\n")

print(f"Zapisano {len(www_entries)} wpisów do pliku {output_file}.")
