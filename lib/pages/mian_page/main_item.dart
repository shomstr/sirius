import 'package:flutter/material.dart';
import 'package:sirius/design/colors.dart';

class MainItem extends StatelessWidget {
  final String title;

  const MainItem({Key? key, required this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      color: ButtonsColor,
      margin: EdgeInsets.zero,
      elevation: 0.06,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(25)),
      child: InkWell(
        borderRadius: BorderRadius.circular(25),
        onTap: () {
          // ignore: avoid_print
          print('Press $title');
        },
        child: SizedBox(
          height: 128,
          width: 380,
          child: Padding(
            padding: const EdgeInsets.only(left: 8, right: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                _title(),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _title() {
    return Text(
      title,
      textAlign: TextAlign.center,
      style: const TextStyle(
        fontSize: 40,
        fontWeight: FontWeight.bold,
        height: 1.2,
        letterSpacing: 0.0,
      ),
    );
  }
}
