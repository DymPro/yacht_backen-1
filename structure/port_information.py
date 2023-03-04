port_structure = {
      "form" : [
       {
           "title" : "Basic Information",
           "card_id" : 0,
           "fields" : [
               {
                   "field_id" : 0,
                   "label" : "Port Facility Name",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Name of Port Facility",
                   "name" : "title",
                   "value" : ""
               },
               {
                   "field_id" : 1,
                   "label" : "Port Facility Description",
                   "type" : "text",
                   "mandatory" : "true",
                   "placeholder" : "Enter Description of Port Facility",
                   "name" : "description",
                   "value" : ""
               },
               {
                   "field_id" : 2,
                   "label" : "Port Facility Image",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Port Facility Image",
                   "name" : "image",
                   "value" : ""
               },
               {
                   "field_id" : 3,
                   "label" : "Active",
                   "type" : "switch",
                   "mandatory" : "true",
                   "name" : "active",
                   "value" : ""   
               }
           ]
       },
       {
           "title" : "Maximum Ship Dimensions",
           "card_id" : 1,
           "fields" : [
               {
                   "field_id" : 4,
                   "label" : "Card Icon",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Card Icon",
                   "name" : "card_icon_0",
                   "value" : ""
               },
               {
                   "field_id" : 5,
                   "label" : "Length",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Length",
                   "name" : "length",
                   "value" : ""
               },
               {
                   "field_id" : 6,
                   "label" : "Width",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Width",
                   "name" : "width",
                   "value" : ""
               },
               {
                   "field_id" : 7,
                   "label" : "Draught",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Draught",
                   "name" : "draught",
                   "value" : ""
               }
             
           ]
       },
       {
           "title" : "Anchorage",
           "card_id" : 2,
           "fields" : [
               {
                   "field_id" : 8,
                   "label" : "Tugs Availble ?",
                   "type" : "checkbox",
                   "mandatory" : "true",
                   "name" : "tugs_available",
                   "value" : "" 
               },
               {
                   "field_id" : 9,
                   "label" : "Is Anchorage Available ?",
                   "type" : "checkbox",
                   "mandatory" : "true",
                   "name" : "anchor_available",
                   "value" : ""   
               },
               {
                   "field_id" : 10,
                   "label" : "Ship Tender Allowed",
                   "type" : "checkbox",
                   "mandatory" : "true",
                   "name" : "ship_tender",
                   "value" : ""   
               },
               {
                   "field_id" : 11,
                   "label" : "Card Icon",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Card Icon",
                   "name" : "card_icon_1",
                   "value" : ""
               },
               {
                   "field_id" : 12,
                   "label" : "Tidal Movement / Range",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Tidal Movement / Range",
                   "name" : "tidal_movement",
                   "value" : ""
               }
             
           ]
       },
       {
           "title" : "Quays / Berths",
           "card_id" : 3,
           "fields" : [
               {
                   "field_id" : 13,
                   "label" : "Card Icon",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Card Icon",
                   "name" : "card_icon_2",
                   "value" : ""
               },
               {
                   "field_id" : 14,
                   "label" : "Total Berths",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Total Berths",
                   "name" : "total_Berths",
                   "value" : ""
               },
               {
                   "field_id" : 15,
                   "label" : "Total Berthing Length Line",
                   "type" : "text",
                   "mandatory" : "true",
                   "placeholder" : "Enter Total Birthing length line",
                   "name" : "birthing_length_line",
                   "value" : ""
               },
               {
                   "field_id" : 16,
                   "label" : "Quay Depth",
                   "type" : "text",
                   "mandatory" : "true",
                   "placeholder" : "Enter Quay Depth",
                   "name" : "quay_depth",
                   "value" : ""
               }
          
           ]
       },
       {
           "title" : "Distance / Transportation",
           "card_id" : 4,
           "fields" : [
               {
                   "field_id" : 17,
                   "label" : "Card Icon",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Card Icon",
                   "name" : "card_icon_3",
                   "value" : ""
               },
               {
                   "field_id" : 18,
                   "label" : "City Center",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Distance to city center",
                   "name" : "city_center_distance",
                   "value" : ""
               },
               {
                   "field_id" : 19,
                   "label" : "Airport",
                   "type" : "text",
                   "mandatory" : "true",
                   "placeholder" : "Enter Distance to airport",
                   "name" : "airport_distance",
                   "value" : ""
               },
               {
                   "field_id" : 20,
                   "label" : "Shuttle Service Avilability",
                   "type" : "checkbox",
                   "mandatory" : "true",
                   "name" : "shuttle_service",
                   "value" : ""
               }
          
           ]
       },
       {
        "title" : "Security",
        "card_id" : 5,
        "fields" : [
            {
                "field_id" : 21,
                "label" : "Card Icon",
                "type" : "file",
                "mandatory" : "true",
                "placeholder" : "Select Card Icon",
                "name" : "card_icon_3",
                "value" : ""
            },
            {
                "field_id" : 22,
                "label" : "PFSO Name",
                "type" : "text",
                "mandatory" : "false",
                "placeholder" : "Enter PFSO Name",
                "name" : "pfso_name",
                "value" : ""
            },
            {
                "field_id" : 23,
                "label" : "Security Level",
                "type" : "dropdown",
                "options" : ["Level 1", "Level 2", "Level 3"],
                "mandatory" : "true",
                "placeholder" : "Enter Security Level",
                "name" : "security_level",
                "value" : ""
            },
            {
                "field_id" : 24,
                "label" : "PFSO Email",
                "type" : "text",
                "mandatory" : "false",
                "placeholder" : "Enter PFSO Name",
                "name" : "pfso_email",
                "value" : ""
            },
            {
                "field_id" : 25,
                "label" : "PFSO Cell",
                "type" : "text",
                "mandatory" : "false",
                "placeholder" : "Enter PFSO Cell",
                "name" : "pfso_phone",
                "value" : ""
            },
       
        ]
    },
   
       {
           "title" : "Contact Information",
           "card_id" : 6,
           "fields" : [
               {
                   "field_id" : 26,
                   "label" : "Card Icon",
                   "type" : "file",
                   "mandatory" : "true",
                   "placeholder" : "Select Card Icon",
                   "name" : "card_icon_4",
                   "value" : ""
               },
               {
                   "field_id" : 27,
                   "label" : "Company Name",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Company Name",
                   "name" : "company_name",
                   "value" : ""
               },
               {
                   "field_id" : 28,
                   "label" : "Phone",
                   "type" : "text",
                   "mandatory" : "true",
                   "placeholder" : "Enter Company Phone",
                   "name" : "company_phone",
                   "value" : ""
               },
               {
                   "field_id" : 29,
                   "label" : "Fax",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Company Fax",
                   "name" : "company_fax",
                   "value" : ""
               },
               {
                   "field_id" : 30,
                   "label" : "Email Address",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Company Email Address",
                   "name" : "company_email",
                   "value" : ""
               },
               {
                   "field_id" : 31,
                   "label" : "Website",
                   "type" : "text",
                   "mandatory" : "false",
                   "placeholder" : "Enter Company Website",
                   "name" : "company_website",
                   "value" : ""
               }
          
           ]
       },
        {
           "title" : "Port Information ( About Port )",
           "card_id" : 7,
           "fields" : [
               {
                   "field_id" : 32,
                   "label" : "Port Information",
                   "type" : "textarea",
                   "mandatory" : "false",
                   "placeholder" : "Enter port information",
                   "name" : "port_information",
                   "value" : ""
               }
          
           ]
       }
   ]
}
