import numpy as np

from mt3.metrics import transcription_metrics
import note_seq


def main():
    target = note_seq.midi_file_to_note_sequence("maestro.mid")
    prediction = note_seq.midi_file_to_note_sequence("test_colab.mid")
    print(
        transcription_metrics(targets={"0": {"ref_ns": target}}, predictions={"0": {"est_ns": prediction}}, codec=None,
                              spectrogram_config=None, onsets_only=False, use_ties=None))


if __name__ == "__main__":
    main()
