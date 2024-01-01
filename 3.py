def get_prelast_and_last_part_of_link(link):
    parts = link.rstrip().split("/")
    return "/".join(parts[-2:])


def process_links(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        links = file.readlines()
    processed_links = sorted(
        [get_prelast_and_last_part_of_link(link) for link in links]
    )
    with open(output_file, "w", encoding="utf-8") as file:
        for link in processed_links:
            file.write(link + "\n")


input_file_path = "links_precalculus_clean_3.txt"
output_file_path = "links_precalculus_clean_3_crop.txt"
process_links(input_file_path, output_file_path)
