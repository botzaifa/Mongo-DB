import pymongo

if __name__== "__main__":
    print("This is the output of the following code:")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['test2']
    collection = db['coll1']
    
    insertThese = [
        {
        "name": "Emily Anderson",
        "hobbies": ["dancing", "traveling", "cooking"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "JKL Solutions",
            "years": 3
            },
            {
            "company": "STU Tech",
            "years": 4
            }
        ],
        "age": 32
        },
        {
        "name": "Michael Brown",
        "hobbies": ["playing basketball", "watching movies", "photography"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "VWX Corporation",
            "years": 8
            },
            {
            "company": "YZA Enterprises",
            "years": 2
            }
        ],
        "age": 27
        },
        {
        "name": "Sarah Davis",
        "hobbies": ["reading", "yoga", "painting"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "BCD Corp",
            "years": 6
            },
            {
            "company": "EFG Ltd",
            "years": 3
            }
        ],
        "age": 29
        },
        {
        "name": "David Taylor",
        "hobbies": ["playing football", "hiking", "video games"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "HIJ Inc",
            "years": 4
            },
            {
            "company": "KLM Corporation",
            "years": 7
            }
        ],
        "age": 31
        },
        {
        "name": "Olivia Wilson",
        "hobbies": ["dancing", "traveling", "photography"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "NOP Solutions",
            "years": 5
            },
            {
            "company": "QRS Tech",
            "years": 2
            }
        ],
        "age": 33
        },
        {
        "name": "James Clark",
        "hobbies": ["playing guitar", "swimming", "watching movies"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "TUV Corp",
            "years": 6
            },
            {
            "company": "WXY Inc",
            "years": 4
            }
        ],
        "age": 29
        },
        {
        "name": "Emma Anderson",
        "hobbies": ["reading", "cooking", "yoga"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "ZAB Enterprises",
            "years": 3
            },
            {
            "company": "CDE Corporation",
            "years": 5
            }
        ],
        "age": 30
        },
        {
        "name": "Daniel Wilson",
        "hobbies": ["playing basketball", "painting", "hiking"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "FGH Solutions",
            "years": 7
            },
            {
            "company": "IJK Tech",
            "years": 3
            }
        ],
        "age": 26
        },
        {
        "name": "Sophia Johnson",
        "hobbies": ["dancing", "photography", "watching movies"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "LMN Corp",
            "years": 5
            },
            {
            "company": "OPQ Inc",
            "years": 2
            }
        ],
        "age": 34
        },
        {
        "name": "William Brown",
        "hobbies": ["playing guitar", "traveling", "cooking"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "RST Solutions",
            "years": 4
            },
            {
            "company": "UVW Tech",
            "years": 6
            }
        ],
        "age": 28
        },
        {
        "name": "Isabella Davis",
        "hobbies": ["reading", "swimming", "yoga"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "XYZ Corp",
            "years": 6
            },
            {
            "company": "CDE Ltd",
            "years": 3
            }
        ],
        "age": 31
        },
        {
        "name": "Ethan Taylor",
        "hobbies": ["playing football", "painting", "watching movies"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "FGH Inc",
            "years": 5
            },
            {
            "company": "IJK Corporation",
            "years": 4
            }
        ],
        "age": 27
        },
        {
        "name": "Mia Wilson",
        "hobbies": ["dancing", "cooking", "photography"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "LMN Solutions",
            "years": 3
            },
            {
            "company": "OPQ Tech",
            "years": 5
            }
        ],
        "age": 30
        },
        {
        "name": "Benjamin Clark",
        "hobbies": ["playing guitar", "hiking", "swimming"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "RST Corp",
            "years": 6
            },
            {
            "company": "UVW Inc",
            "years": 4
            }
        ],
        "age": 29
        },
        {
        "name": "Ava Anderson",
        "hobbies": ["reading", "traveling", "yoga"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "XYZ Solutions",
            "years": 4
            },
            {
            "company": "CDE Tech",
            "years": 6
            }
        ],
        "age": 32
        },
        {
        "name": "Christopher Wilson",
        "hobbies": ["playing basketball", "watching movies", "painting"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "FGH Corporation",
            "years": 7
            },
            {
            "company": "IJK Enterprises",
            "years": 3
            }
        ],
        "age": 26
        },
        {
        "name": "Abigail Johnson",
        "hobbies": ["dancing", "photography", "cooking"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "LMN Tech",
            "years": 5
            },
            {
            "company": "OPQ Ltd",
            "years": 2
            }
        ],
        "age": 33
        },
        {
        "name": "Matthew Brown",
        "hobbies": ["playing guitar", "traveling", "hiking"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "RST Solutions",
            "years": 6
            },
            {
            "company": "UVW Tech",
            "years": 4
            }
        ],
        "age": 27
        },
        {
        "name": "Sofia Davis",
        "hobbies": ["reading", "swimming", "painting"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "XYZ Corp",
            "years": 5
            },
            {
            "company": "CDE Ltd",
            "years": 3
            }
        ],
        "age": 31
        },
        {
        "name": "Joseph Taylor",
        "hobbies": ["playing football", "watching movies", "yoga"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "FGH Inc",
            "years": 4
            },
            {
            "company": "IJK Corporation",
            "years": 6
            }
        ],
        "age": 28
        },
        {
        "name": "Scarlett Wilson",
        "hobbies": ["dancing", "cooking", "photography"],
        "identity": False,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "LMN Solutions",
            "years": 3
            },
            {
            "company": "OPQ Tech",
            "years": 5
            }
        ],
        "age": 30
        },
        {
        "name": "Andrew Clark",
        "hobbies": ["playing guitar", "hiking", "swimming"],
        "identity": True,
        "BIO": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae lectus nec libero commodo consequat.",
        "Experience": [
            {
            "company": "RST Corp",
            "years": 6
            },
            {
            "company": "UVW Inc",
            "years": 4
            }
        ],
        "age": 29
        }
    ]
    collection.insert_many(insertThese)