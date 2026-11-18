
class TextEditor:
    """
    Kelas TextEditor untuk mengelola isi teks
    serta fitur Undo dan Redo.
    """

    def __init__(self, history_manager):
        self.content = ""
        self.history_manager = history_manager

        # Menyimpan kondisi awal teks
        self.history_manager.save_state(self.content)

    def write(self, new_text):
        """Menambahkan teks baru."""
        self.content += new_text
        self.history_manager.save_state(self.content)

    def set_text(self, new_text):
        """Mengganti seluruh isi teks."""
        self.content = new_text
        self.history_manager.save_state(self.content)

    def delete(self):
        """Menghapus seluruh isi teks."""
        self.content = ""
        self.history_manager.save_state(self.content)

    def undo(self):
        """Membatalkan perubahan terakhir."""
        previous_state = self.history_manager.undo()

        if previous_state is not None:
            self.content = previous_state
            return True

        return False

    def redo(self):
        """Mengembalikan perubahan yang dibatalkan."""
        next_state = self.history_manager.redo()

        if next_state is not None:
            self.content = next_state
            return True

        return False

    def get_text(self):
        """Mengambil isi teks saat ini."""
        return self.content
