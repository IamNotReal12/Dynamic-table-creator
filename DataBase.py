import csv
import sqlite3
from tkinter import filedialog
import customtkinter as kc
from CTkTable import CTkTable


class AppData(kc.CTk):

    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)
        kc.set_appearance_mode("dark")
        self.after(0, lambda: self.state("zoomed"))

        self.tabla_visual = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.contenedorpadre = kc.CTkFrame(
            self,
            width=1200,
            height=1000,
            corner_radius=20,
            border_width=5,
            border_color="#000000",
            fg_color="#1B1A1A",
        )
        self.contenedorpadre.grid(row=0, column=0)
        self.contenedorpadre.grid_propagate(False)
        self.contenedorpadre.grid_columnconfigure((0, 1), weight=1)
        self.contenedorpadre.grid_rowconfigure((0, 1), weight=1)

        self.contenedorencabezado = kc.CTkFrame(
            self.contenedorpadre,
            height=55,
            width=1000,
            corner_radius=20,
            border_width=5,
            border_color="#A6FF00",
            fg_color="#000000",
        )
        self.contenedorencabezado.grid(
            row=0, column=0, sticky="n", pady=(20, 0), columnspan=2
        )
        self.contenedorencabezado.grid_propagate(False)
        self.contenedorencabezado.grid_rowconfigure(0, weight=1)
        self.contenedorencabezado.grid_columnconfigure(0, weight=1)

        self.tituloencabezado = kc.CTkLabel(
            self.contenedorencabezado,
            text="GESTOR DE TABLAS DINAMICAS-ACADEMIC SQL🗄️",
            text_color="#A6FF00",
            font=("Segoe UI", 25, "bold"),
        )
        self.tituloencabezado.grid(row=0, column=0)

        self.contenedoropciones = kc.CTkFrame(
            self.contenedorpadre, width=500, height=700, fg_color="#171717"
        )
        self.contenedoropciones.grid(row=1, column=0, sticky="w")
        self.contenedoropciones.grid_propagate(False)

        self.contender_inputs = kc.CTkFrame(
            self.contenedoropciones,
            width=400,
            height=300,
            border_width=3,
            border_color="#88058F",
            corner_radius=15,
        )
        self.contender_inputs.grid(row=0, column=0, pady=20, padx=20)
        self.contender_inputs.grid_propagate(False)
        self.contender_inputs.grid_columnconfigure(0, weight=1)

        self.contenederencabezadoopciones = kc.CTkFrame(
            self.contender_inputs,
            height=45,
            fg_color="#88058F",
            corner_radius=12,
        )
        self.contenederencabezadoopciones.grid(
            row=0, column=0, sticky="ew", padx=2, pady=(2, 0)
        )
        self.contenederencabezadoopciones.grid_propagate(False)

        self.label_titulo_acciones = kc.CTkLabel(
            self.contenederencabezadoopciones,
            text="SECCIÓN DE ACCIONES",
            font=("Segoe UI", 14, "bold"),
            text_color="#FFFFFF",
        )
        self.label_titulo_acciones.place(relx=0.5, rely=0.5, anchor="center")

        self.btn_crear_tabla = kc.CTkButton(
            self.contender_inputs,
            text="CREAR NUEVA TABLA",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#FF007F",
            border_width=2,
            border_color="#FF007F",
            hover_color="#33001A",
            corner_radius=20,
            height=35,
            width=320,
            command=self.CrearTabla,
        )
        self.btn_crear_tabla.grid(row=1, column=0, pady=(15, 8))

        self.btn_insertar_datos = kc.CTkButton(
            self.contender_inputs,
            text="INSERTAR DATOS",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#00E5FF",
            border_width=2,
            border_color="#00E5FF",
            hover_color="#002B33",
            corner_radius=20,
            height=35,
            width=320,
            command=self.InsertarDatos,
        )
        self.btn_insertar_datos.grid(row=2, column=0, pady=8)

        self.btn_borrar_tabla = kc.CTkButton(
            self.contender_inputs,
            text="BORRAR TABLA",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#FF6600",
            border_width=2,
            border_color="#FF6600",
            hover_color="#331400",
            corner_radius=20,
            height=35,
            width=320,
            command=self.LimpiarTabla,
        )
        self.btn_borrar_tabla.grid(row=3, column=0, pady=8)

        self.btn_buscar = kc.CTkButton(
            self.contender_inputs,
            text="VER / ACTUALIZAR TABLA",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#00E5FF",
            border_width=2,
            border_color="#00E5FF",
            hover_color="#002B33",
            corner_radius=20,
            height=35,
            width=320,
            command=self.ActualizarDato,
        )
        self.btn_buscar.grid(row=4, column=0, pady=8)

        self.btn_guardar_csv = kc.CTkButton(
            self.contender_inputs,
            text="GUARDAR TABLA (CSV)",
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            text_color="#A6FF00",
            border_width=2,
            border_color="#A6FF00",
            hover_color="#223300",
            corner_radius=20,
            height=35,
            width=320,
            command=self.GuardarTablaCSV,
        )
        self.btn_guardar_csv.grid(row=5, column=0, pady=8)

        self.contender_opciones = kc.CTkFrame(
            self.contenedoropciones,
            width=400,
            height=300,
            border_width=3,
            border_color="#88058F",
            corner_radius=15,
        )
        self.contender_opciones.grid(row=1, column=0, pady=30, padx=20)
        self.contender_opciones.grid_propagate(False)
        self.contender_opciones.grid_columnconfigure(0, weight=1)

        self.encabezado_filtros = kc.CTkFrame(
            self.contender_opciones,
            height=45,
            fg_color="#88058F",
            corner_radius=12,
        )
        self.encabezado_filtros.grid(
            row=0, column=0, sticky="ew", padx=2, pady=(2, 0)
        )
        self.encabezado_filtros.grid_propagate(False)

        self.label_titulo_filtros = kc.CTkLabel(
            self.encabezado_filtros,
            text="FILTROS & CONFIGURACIÓN",
            font=("Segoe UI", 14, "bold"),
            text_color="#FFFFFF",
        )
        self.label_titulo_filtros.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_nombre_tabla = kc.CTkLabel(
            self.contender_opciones,
            text="Nombre Tabla:",
            font=("Segoe UI", 12, "bold"),
            text_color="#FF007F",
        )
        self.lbl_nombre_tabla.grid(
            row=1, column=0, sticky="w", padx=25, pady=(8, 0)
        )

        self.entry_nombre_tabla = kc.CTkEntry(
            self.contender_opciones,
            width=340,
            height=30,
            fg_color="#171717",
            border_color="#00E5FF",
            border_width=2,
            corner_radius=10,
            text_color="#FFFFFF",
        )
        self.entry_nombre_tabla.grid(row=2, column=0, pady=(0, 5))

        self.lbl_campo_filtro = kc.CTkLabel(
            self.contender_opciones,
            text="Campo Filtro:",
            font=("Segoe UI", 12, "bold"),
            text_color="#FF007F",
        )
        self.lbl_campo_filtro.grid(
            row=3, column=0, sticky="w", padx=25, pady=(2, 0)
        )

        self.entry_campo_filtro = kc.CTkEntry(
            self.contender_opciones,
            width=340,
            height=30,
            fg_color="#171717",
            border_color="#00E5FF",
            border_width=2,
            corner_radius=10,
            text_color="#FFFFFF",
        )
        self.entry_campo_filtro.grid(row=4, column=0, pady=(0, 5))

        self.lbl_valor = kc.CTkLabel(
            self.contender_opciones,
            text="Valor:",
            font=("Segoe UI", 12, "bold"),
            text_color="#FF007F",
        )
        self.lbl_valor.grid(row=5, column=0, sticky="w", padx=25, pady=(2, 0))

        self.entry_valor = kc.CTkEntry(
            self.contender_opciones,
            width=340,
            height=30,
            fg_color="#171717",
            border_color="#00E5FF",
            border_width=2,
            corner_radius=10,
            text_color="#FFFFFF",
        )
        self.entry_valor.grid(row=6, column=0, pady=(0, 10))

        self.frametabla = kc.CTkFrame(
            self.contenedorpadre,
            width=700,
            height=630,
            corner_radius=15,
            border_width=3,
            border_color="#00E5FF",
            fg_color="#171717",
        )
        self.frametabla.grid(
            row=1, column=1, sticky="nsew", padx=(0, 20), pady=20
        )
        self.frametabla.grid_propagate(False)

        self.contenedorencabezadotable = kc.CTkFrame(
            self.frametabla,
            height=45,
            width=680,
            fg_color="#88058F",
            corner_radius=12,
        )
        self.contenedorencabezadotable.grid(
            row=0, column=0, sticky="ew", padx=10, pady=(10, 5)
        )
        self.contenedorencabezadotable.grid_propagate(False)

        self.textotable = kc.CTkLabel(
            self.contenedorencabezadotable,
            text="Visualiza tu tabla aqui...📋",
            font=("Segoe UI", 18, "bold"),
            text_color="#FFFFFF",
        )
        self.textotable.place(relx=0.5, rely=0.5, anchor="center")

        self.frametablacreada = kc.CTkScrollableFrame(
            self.frametabla, height=520, width=650, fg_color="#1B1A1A"
        )
        self.frametablacreada.grid(row=1, column=0, padx=10, pady=10)

    def CrearTabla(self):
        NombreTabla = str(self.entry_nombre_tabla.get().strip())

        if self.tabla_visual is not None:
            self.tabla_visual.destroy()

        if not NombreTabla:
            print("⚠️ Escribe un nombre para la tabla.")
            return

        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()

        sql_crear_tabla = f"""
        CREATE TABLE IF NOT EXISTS {NombreTabla} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            socio TEXT NOT NULL,
            plan TEXT NOT NULL,
            peso_kg REAL NOT NULL,
            proteina_g INTEGER NOT NULL,
            asistencias INTEGER DEFAULT 0
        );
        """
        cursor.execute(sql_crear_tabla)
        conexion.commit()
        conexion.close()

        self.CargarYMostrarTabla()

    def InsertarDatos(self):
        nombre_tabla = self.entry_nombre_tabla.get().strip()

        if not nombre_tabla:
            print("⚠️ Escribe el nombre de la tabla primero.")
            return

        ventana_modal = kc.CTkToplevel(self)
        ventana_modal.title("Nuevo Registro")
        ventana_modal.geometry("350x400")
        ventana_modal.grab_set()

        entry_socio = kc.CTkEntry(
            ventana_modal, placeholder_text="Nombre del Socio"
        )
        entry_socio.pack(pady=10)

        entry_plan = kc.CTkEntry(
            ventana_modal, placeholder_text="Plan (ej. Premium)"
        )
        entry_plan.pack(pady=10)

        entry_peso = kc.CTkEntry(ventana_modal, placeholder_text="Peso (kg)")
        entry_peso.pack(pady=10)

        entry_proteina = kc.CTkEntry(
            ventana_modal, placeholder_text="Proteína (g)"
        )
        entry_proteina.pack(pady=10)

        entry_asistencias = kc.CTkEntry(
            ventana_modal, placeholder_text="Asistencias"
        )
        entry_asistencias.pack(pady=10)

        def guardar():
            try:
                conexion = sqlite3.connect("BaseDatos.db")
                cursor = conexion.cursor()

                sql = f"""
                INSERT INTO {nombre_tabla} (socio, plan, peso_kg, proteina_g, asistencias)
                VALUES (?, ?, ?, ?, ?)
                """
                cursor.execute(
                    sql,
                    (
                        entry_socio.get(),
                        entry_plan.get(),
                        float(entry_peso.get()),
                        int(entry_proteina.get()),
                        int(entry_asistencias.get()),
                    ),
                )
                conexion.commit()
                conexion.close()
                ventana_modal.destroy()

                self.CargarYMostrarTabla()
            except Exception as e:
                print(f"⚠️ Error al insertar: {e}")

        btn_guardar = kc.CTkButton(
            ventana_modal, text="Guardar", command=guardar
        )
        btn_guardar.pack(pady=15)

    def CargarYMostrarTabla(self):
        nombre_tabla = self.entry_nombre_tabla.get().strip()

        if not nombre_tabla:
            print("⚠️ Ingresa el nombre de la tabla para visualizarla.")
            return

        encabezados = [
            "ID",
            "Socio",
            "Plan",
            "Peso (kg)",
            "Proteína (g)",
            "Asistencias",
        ]

        try:
            conexion = sqlite3.connect("BaseDatos.db")
            cursor = conexion.cursor()
            sql_mostrar = f"""
            SELECT * FROM {nombre_tabla};
            """
            cursor.execute(sql_mostrar)
            registros = cursor.fetchall()
            conexion.close()

            datos_tabla = [encabezados] + registros

            if self.tabla_visual is not None:
                self.tabla_visual.destroy()

            self.tabla_visual = CTkTable(
                master=self.frametablacreada,
                values=datos_tabla,
                colors=["#171717", "#222222"],
                header_color="#88058F",
                hover_color="#002B33",
                text_color="#FFFFFF",
                corner_radius=8,
            )
            self.tabla_visual.pack(expand=True, fill="both", padx=5, pady=5)
            self.textotable.configure(
                text=f"Tabla Actual: {nombre_tabla.upper()}"
            )

        except sqlite3.OperationalError:
            print(f"⚠️ La tabla '{nombre_tabla}' no existe en la base de datos.")

    def ActualizarDato(self):
        NombreTabla = self.entry_nombre_tabla.get()
        ValorAModificar = self.entry_campo_filtro.get().strip()

        ValorNuevo = self.entry_valor.get()

        if not NombreTabla or not ValorAModificar or not ValorNuevo:
            return

        dialogo_id = kc.CTkInputDialog(
            text="Ingresa el ID del registro que deseas actualizar:",
            title="Actualizar Registro",
        )
        id_registro = dialogo_id.get_input()

        if not id_registro:
            print("⚠️ Operación cancelada: No se ingresó ningún ID.")
            return

        conexion = sqlite3.connect("BaseDatos.db")
        cursor = conexion.cursor()

        sql_update = f"""
        UPDATE {NombreTabla}
        SET {ValorAModificar} = ?
        WHERE id = ? 
        """

        cursor.execute(sql_update, (ValorNuevo, id_registro))
        conexion.commit()
        cursor.close()
        self.CargarYMostrarTabla()

    def LimpiarTabla(self):
        nombre_tabla = self.entry_nombre_tabla.get().strip()

        if not nombre_tabla:
            return

        try:
            conexion = sqlite3.connect("BaseDatos.db")
            cursor = conexion.cursor()

            cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla};")

            cursor.execute(
                f"DELETE FROM sqlite_sequence WHERE name = ?;", (nombre_tabla,)
            )

            conexion.commit()
            conexion.close()

            if self.tabla_visual is not None:
                self.tabla_visual.destroy()
                self.tabla_visual = None
            self.textotable.configure(text="Visualiza tu tabla aqui...📋")

        except sqlite3.OperationalError as e:
            print(f"⚠️ Error al limpiar la tabla: {e}")

    def GuardarTablaCSV(self):
        NombreTabla = self.entry_nombre_tabla.get().strip()

        if not NombreTabla:
            return

        RutaArchivoGuardar = filedialog.asksaveasfilename(
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
            title="Guardar Archivo CSV",defaultextension=".csv"
        )

        if RutaArchivoGuardar:
            try:
                datos_tabla = self.tabla_visual.get()
                with open(
                    RutaArchivoGuardar,
                    "w",
                    newline="",
                    encoding="utf-8-sig",
                ) as archivo:
                    writer = csv.writer(archivo)
                    writer.writerows(datos_tabla)
            except Exception as es:
                print(f"{es}")


if __name__ == "__main__":
    App = AppData()
    App.mainloop()
