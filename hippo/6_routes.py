import hippo

from sqlite3 import DatabaseError

import mrich as logger

animal = hippo.HIPPO("FFF", "../../BulkDock/TARGETS/A71EV2AZ/A71EV2AZ.sqlite")
animal.db.backup()

bases = animal.compounds(tag="elaborated iter1 scaffold")
elabs = bases.elabs
products = bases + elabs

logger.var("products", products)

for i, c in logger.track(enumerate(products), total=len(products)):

    try:
        reactions = c.reactions
    except DatabaseError:
        logger.error(f"Error getting {c}'s reactions")
        continue

    for reaction in reactions:

        try:
            recipes = reaction.get_recipes(supplier="Enamine")
        except DatabaseError:
            logger.error(f"Error getting {reaction}'s ({c}) recipes")
            continue

        for recipe in recipes:

            route = animal.register_route(recipe=recipe)

            logger.print(f"registered {route=}")

    if i % 100 == 99:
        logger.success("Committing...")
        animal.db.commit()

animal.db.prune_duplicate_routes()

animal.db.close()

# sb.sh --job-name 2AZ_routes -pgpu --exclusive $HOME2/slurm/run_python.sh 6_routes.py