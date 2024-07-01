//add a new user to the user collection

user = {firstname: 'Sergei', lastName: 'Prokofiev', employeeId: '1013', email: 'sprokofiev@me.com', dateCreated: new Date()};

db.users.insertOne(user);

//Update mozarts email address

db.users.updateOne({employeeId: '1009'}, {$set:{email: 'mozart@me.com'}});

//Display all users. Use projections to only show first name, last name and email

db.users.find({},{firstName: 1, lastName: 1, email: 1});

