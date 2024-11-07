import 'package:hive/hive.dart';

part 'users.g.dart'; 

@HiveType(typeId: 0)
class User {
  @HiveField(0)
  final int id; 

  @HiveField(1)
  final String username; 

  @HiveField(2)
  final String password; 

  @HiveField(3)
  final String email;

  User({
    required this.id,
    required this.username,
    required this.password,
    required this.email,
  });
}
