import sys
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify, solve
from mpl_toolkits.mplot3d import Axes3D

# Ambil argumen dari Laravel
function_str = sys.argv[1]
a, b = float(sys.argv[2]), float(sys.argv[3])
axis = sys.argv[4]
output_path = sys.argv[5]

# Definisikan simbol
x, y = symbols('x y')

try:
    # Ubah string fungsi menjadi fungsi evaluasi
    function = sympify(function_str.split('=')[-1].strip())

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    if axis == "x":
        f = lambdify(x, function, 'numpy')
        x_vals = np.linspace(a, b, 100)
        y_vals = f(x_vals)

        theta = np.linspace(0, 2 * np.pi, 100)
        X, T = np.meshgrid(x_vals, theta)
        Y = f(X)

        Z = Y * np.cos(T)
        W = Y * np.sin(T)

        ax.plot_surface(X, Z, W, color='blue', alpha=0.6)
        ax.set_title("Volume Benda Putar (Sumbu X)")

        # Atur POV untuk sumbu X
        ax.view_init(elev=30, azim=120)

    else:
        x_expr = solve(function - y, x)[0]  # Ambil solusi pertama
        f = lambdify(y, x_expr, 'numpy')

        y_vals = np.linspace(a, b, 100)
        x_vals = f(y_vals)

        theta = np.linspace(0, 2 * np.pi, 100)
        Y, T = np.meshgrid(y_vals, theta)
        X = f(Y)

        Z = X * np.cos(T)
        W = X * np.sin(T)

        ax.plot_surface(Z, Y, W, color='red', alpha=0.6)
        ax.set_title("Volume Benda Putar (Sumbu Y)")

        # Atur POV untuk sumbu Y
        ax.view_init(elev=-80, azim=90)

    # Aktifkan tampilan interaktif (bisa digerakkan dan di-zoom)
    ax.set_box_aspect([1, 1, 1])

    # Atur label sumbu
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Geser garis sumbu Y ke tengah
    ax.set_ylim(-b, b)

    # Simpan hasil gambar
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)

    # Tampilkan gambar secara interaktif
    plt.show()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)