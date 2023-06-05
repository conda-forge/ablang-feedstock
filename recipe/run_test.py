# example copied verbatim from the README
# https://github.com/TobiasHeOl/AbLang#antibody-sequence-restoration
# https://github.com/TobiasHeOl/AbLang/blob/f5055a39e53df7692039a544b38fec243764ee8a/README.md#ablang-use-cases


import ablang

heavy_ablang = ablang.pretrained("heavy") # Use "light" if you are working with light chains
heavy_ablang.freeze()


seqs = [
    'EV*LVESGPGLVQPGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNKYYADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTLVTVSS',
    '*************PGKSLRLSCVASGFTFSGYGMHWVRQAPGKGLEWIALIIYDESNK*YADSVKGRFTISRDNSKNTLYLQMSSLRAEDTAVFYCAKVKFYDPTAPNDYWGQGTL*****',
]

heavy_ablang(seqs, mode='restore')
