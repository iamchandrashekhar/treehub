from django.shortcuts import render

def home(request):
    """Home page with introduction to TreeHub"""
    context = {
        'title': 'Welcome to TreeHub',
        'featured_trees': [
            {'name': 'Oak', 'description': 'Strong and long-living deciduous trees'},
            {'name': 'Pine', 'description': 'Evergreen conifers with needle-like leaves'},
            {'name': 'Maple', 'description': 'Beautiful autumn colors and syrup production'},
        ]
    }
    return render(request, 'trees/home.html', context)

def about(request):
    """About page explaining TreeHub mission"""
    context = {
        'title': 'About TreeHub',
    }
    return render(request, 'trees/about.html', context)

def tree_types(request):
    """Page displaying different types of trees"""
    tree_types_data = [
        {
            'category': 'Deciduous Trees',
            'description': 'Trees that shed their leaves annually',
            'examples': ['Oak', 'Maple', 'Birch', 'Cherry', 'Elm']
        },
        {
            'category': 'Evergreen Trees',
            'description': 'Trees that retain their leaves year-round',
            'examples': ['Pine', 'Spruce', 'Fir', 'Cedar', 'Cypress']
        },
        {
            'category': 'Fruit Trees',
            'description': 'Trees that produce edible fruits',
            'examples': ['Apple', 'Orange', 'Pear', 'Peach', 'Plum']
        },
        {
            'category': 'Flowering Trees',
            'description': 'Trees known for their beautiful blooms',
            'examples': ['Magnolia', 'Dogwood', 'Redbud', 'Jacaranda', 'Sakura']
        }
    ]
    context = {
        'title': 'Tree Types',
        'tree_types': tree_types_data
    }
    return render(request, 'trees/tree_types.html', context)

def forest_facts(request):
    """Page with interesting forest and tree facts"""
    facts = [
        "Forests cover about 31% of the world's land area",
        "A single tree can absorb 22 kilograms of CO2 per year",
        "The oldest known tree is over 4,800 years old",
        "Trees can communicate with each other through underground networks",
        "Amazon rainforest produces 20% of the world's oxygen",
        "One tree can provide oxygen for two people for a day"
    ]
    context = {
        'title': 'Forest Facts',
        'facts': facts
    }
    return render(request, 'trees/forest_facts.html', context)

def tree_care(request):
    """Page with tree care tips and guidelines"""
    care_tips = [
        {
            'title': 'Watering',
            'tip': 'Water deeply but less frequently to encourage deep root growth'
        },
        {
            'title': 'Mulching',
            'tip': 'Apply 2-4 inches of mulch around the base, but keep it away from the trunk'
        },
        {
            'title': 'Pruning',
            'tip': 'Prune during dormant season to remove dead or diseased branches'
        },
        {
            'title': 'Fertilizing',
            'tip': 'Most trees don\'t need frequent fertilizing; test soil first'
        },
        {
            'title': 'Protection',
            'tip': 'Protect young trees from lawn mowers and weather damage'
        }
    ]
    context = {
        'title': 'Tree Care Guide',
        'care_tips': care_tips
    }
    return render(request, 'trees/tree_care.html', context)
