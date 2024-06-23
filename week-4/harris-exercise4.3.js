//Display all users in the collection

db.users.find();

//Display the user with the email address "jbach@me.com"

db.users.findOne({email: 'jbach@me.com'});

//Display the user with the last name Mozart

db.users.findOne({lastName: 'Mozart'});

//Display the user with the first name Richard

db.users.findOne({firstName: 'Richard'});

//Display the user with employeeID 1010

db.users.findOne({employeeId: '1010'});