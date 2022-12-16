copy animals(animalsID, animalsType, animalsOptionLeft, animalsCountLeft, animalsSubCategoryLeft, animalsOptionRight, animalsCountRight, animalsSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/pets.csv'
delimiter ','
csv header;

copy exotic(exoticID, exoticType, exoticOptionLeft, exoticCountLeft, exoticSubCategoryLeft, exoticOptionRight, exoticCountRight, exoticSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/puppies.csv'
delimiter ','
csv header;

copy food(foodID, foodType, foodOptionLeft, foodCountLeft, foodSubCategoryLeft, foodOptionRight, foodCountRight, foodSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/pets.csv'
delimiter ','
csv header;

copy kittens(kittiesID, kittiesType, kittiesOptionLeft, kittiesCountLeft, kittiesSubCategoryLeft, kittiesOptionRight, kittiesCountRight, kittiesSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/puppies.csv'
delimiter ','
csv header;

copy land(landID, landType, landOptionLeft, landCountLeft, landSubCategoryLeft, landOptionRight, landCountRight, landSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/pets.csv'
delimiter ','
csv header;

copy pets(petsID, petsType, petsOptionLeft, petsCountLeft, petsSubCategoryLeft, petsOptionRight, petsCountRight, petsSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/pets.csv'
delimiter ','
csv header;

copy puppies(puppyID, puppyType, puppyOptionLeft, puppyCountLeft, puppySubCategoryLeft, puppyOptionRight, puppyCountRight, puppySubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/puppies.csv'
delimiter ','
csv header;

copy sea(seaID, seaType, seaOptionLeft, seaCountLeft, seaSubCategoryLeft, seaOptionRight, seaCountRight, seaSubCategoryRight)
from '/docker-entrypoint-initdb.d/seed_data/sea.csv'
delimiter ','
csv header;