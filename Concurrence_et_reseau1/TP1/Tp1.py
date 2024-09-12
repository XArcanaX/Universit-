import threading
import random
import queue


class Producteur(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        for i in range(5):
            element = f"Element {i}"
            self.q.put(element)
            print(f"Producteur a produit {element}")
            threading.Event().wait(random.uniform(0.1, 1.0))


class Consommateur(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        element = self.q.get()
        print(f"Consommateur a consomme {element}")
        self.q.task_done()

def main():
    q = queue.Queue()

    nb_producteurs = random.randint(1, 16)
    nb_consommateurs = random.randint(1, 16)

    producteurs = []
    consommateurs = []

    for i in range(nb_producteurs):
        producteur = Producteur(f"Producteur {i}", q)
        producteurs.append(producteur)
        producteur.start()

    for i in range(nb_consommateurs):
        consommateur = Consommateur(f"Consommateur {i}", q)
        consommateurs.append(consommateur)
        consommateur.start()

    for producteur in producteurs:
        producteur.join()

    q.join()


if __name__ == "__main__":
    main()