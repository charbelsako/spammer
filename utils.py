# never tested. Useless file
def get_parent(elt, n_iter):
    current = elt
    for i in range(n_iter):
        parent = current.find_element_by_xpath("..")
        current = parent