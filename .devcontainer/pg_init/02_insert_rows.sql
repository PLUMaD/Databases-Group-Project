copy pets(petsID, petsType, petsOptionLeft, petsCountLeft, petsSubCategoryLeft, petsOptionRight, petsCountRight, petsSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/pets.csv'
delimiter ','
csv header;

copy puppies(puppyID, puppyType, puppyOptionLeft, puppyCountLeft, puppySubCategoryLeft, puppyOptionRight, puppyCountRight, puppySubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/puppies.csv'
delimiter ','
csv header;

