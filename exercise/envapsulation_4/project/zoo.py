class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return 'Not enough space for animal'

        if self.__budget < price:
            return 'Not enough budget'

        self.__budget -= price
        self.animals.append(animal)
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        worker_list = list(filter(lambda w: w.name == worker_name, self.workers))
        # worker_list = [worker for worker in self.workers if worker.name == worker_name]

        if not worker_list:
            return f'There is no {worker_name} in the zoo'

        worker = worker_list[0]
        self.workers.remove(worker)
        return f'{worker_name} fired successfully'

    ########
    def pay_workers(self):
        amount_to_pay = sum([worker.salary for worker in self.workers])
        if amount_to_pay > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= amount_to_pay
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):

        tend_amount = sum(list(map(lambda x: x.get_needs(), self.animals)))
        # tend_amount = sum([animal.get_needs() for animal in self.animals])
        if tend_amount > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend_amount
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    @staticmethod
    def get_detailed_result(zoo_type, zoo_types):
        zoo_types_all = [zt for zt in zoo_types if zt.__class__.__name__ == zoo_type]
        result = f'\n----- {len(zoo_types_all)} {zoo_type}s:\n'
        result += "\n".join([f'{zt}' for zt in zoo_types_all])
        return result

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        for animal_type in ['Lion', 'Tiger', 'Cheetah']:
            result += self.get_detailed_result(animal_type, self.animals)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        for worker_type in ['Keeper', 'Caretaker', 'Vet']:
            result += self.get_detailed_result(worker_type, self.workers)
        return result
