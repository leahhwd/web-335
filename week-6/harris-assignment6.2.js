//Leah Harris
//Assignmment 6.2 

//Display all students
db.students.find();

//add a new student
student = {firstName: 'Zarya', lastName: 'Wilson', studentId: 's1019', houseId: 'h1010'};

db.students.insertOne(student);

//Update property of new student
db.students.updateOne({studentId: 's1019'}, {$set: {lastName: 'Wilson-Diaz'}});

//Delete student
db.students.deleteOne({studentId: 's1019'});

//display all students by house
db.houses.aggregate([{$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_info'}}]);

//display all students in house gryffindor
db.houses.aggregate([{$match: {'houseId': 'h1007'}}, {$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_info'}}]);

//display all student in the house with an eagle mascot
db.houses.aggregate([{$match: {'mascot': 'Eagle'}}, {$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_info'}}]);