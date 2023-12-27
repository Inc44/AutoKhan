def get_prelast_and_last_part_of_link(link):
    parts = link.rstrip().split("/")
    return "/".join(parts[-2:])
def reconstruct_full_links(processed_links, original_links):
    reconstructed_links = []
    for processed_link in processed_links:
        parts = processed_link.strip().split('/')
        for original_link in original_links:
            if all(part in original_link for part in parts):
                reconstructed_links.append(original_link.strip())
                break
    return reconstructed_links
file_links_d_c_path = 'links_precalculus_clean_3_crop.txt'
file_links_p_path = 'links_precalculus_clean_3.txt'
output_file_path = 'links.txt'
with open(file_links_d_c_path, 'r', encoding='utf-8') as file:
    links_d_c = file.readlines()
with open(file_links_p_path, 'r', encoding='utf-8') as file:
    links_p = file.readlines()
links_d = reconstruct_full_links(links_d_c, links_p)
with open(output_file_path, 'w', encoding='utf-8') as file:
    for link in sorted(links_d):
        file.write(link + '\n')