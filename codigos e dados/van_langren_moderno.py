import pandas as pd
import matplotlib.pyplot as plt

# Dados Langren1644
dados = pd.DataFrame({
    "Name": [
        "G. Ianfonius",
        "G. Mercator",
        "I. Schonerus",
        "P. Lantsbergius",
        "T. Brahe",
        "I. Regiomontanus",
        "Orontius",
        "C. Clavius",
        "C. Ptolomeus",
        "A. Argelius",
        "A. Maginus",
        "D. Organus",
    ],
    "Longitude": [
        17.7, 19.6, 20.8, 21.1, 21.5, 25.4,
        26.0, 26.5, 27.7, 28.0, 29.8, 30.1
    ]
}).sort_values("Longitude")

# Diferença real de longitude entre Toledo e Roma
valor_real = 16.53

fig, ax = plt.subplots(figsize=(9.0, 5.6))

y = range(len(dados))

# Segmentos ligando o valor real às estimativas
for yi, x in zip(y, dados["Longitude"]):
    ax.plot(
        [valor_real, x],
        [yi, yi],
        linewidth=1.2,
        alpha=0.55
    )

# Pontos das estimativas
ax.scatter(
    dados["Longitude"],
    y,
    s=55,
    zorder=3
)

# Linha do valor real
ax.axvline(
    valor_real,
    linestyle="--",
    linewidth=1.6
)

# Rótulo do valor real
ax.text(
    valor_real + 0.18,
    len(dados) - 0.1,
    "Valor real\n16,53°",
    ha="left",
    va="top",
    fontsize=10
)

# Nomes dos astrônomos
ax.set_yticks(list(y))
ax.set_yticklabels(
    dados["Name"],
    fontsize=10
)

# Eixos e título
ax.set_xlabel(
    "Diferença de longitude entre Toledo e Roma (graus)",
    fontsize=11
)

ax.set_ylabel("")

ax.set_title(
    "Estimativas de longitude no gráfico de Van Langren (1644)",
    fontsize=13,
    weight="bold",
    pad=12
)

ax.set_xlim(15.5, 31.0)

# Grade
ax.grid(
    axis="x",
    alpha=0.22
)

ax.grid(
    axis="y",
    visible=False
)

# Remove bordas desnecessárias
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

ax.tick_params(
    axis="y",
    length=0
)

plt.tight_layout()

# Salvar
fig.savefig(
    "van_langren_moderno.png",
    dpi=300,
    bbox_inches="tight"
)

fig.savefig(
    "van_langren_moderno.pdf",
    bbox_inches="tight"
)

plt.show()
