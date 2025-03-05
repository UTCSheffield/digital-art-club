union() {
	difference() {
		union() {
			difference() {
				union() {
					cube(size = [0, 0, 0]);
					translate(v = [-6.0, -6.0, -1]) {
						cube(size = [12, 12, 6.0]);
					}
				}
				translate(v = [-5.0, -5.0, 0]) {
					cube(size = [10, 10, 5.0]);
				}
			}
			translate(v = [-4.0, -4.0, 1]) {
				cube(size = [8, 8, 4.0]);
			}
		}
		translate(v = [-3.0, -3.0, 2]) {
			cube(size = [6, 6, 3.0]);
		}
	}
	translate(v = [-2.0, -2.0, 3]) {
		cube(size = [4, 4, 2.0]);
	}
}
