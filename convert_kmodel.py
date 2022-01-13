#%%
import nncase
import tensorflow as tf
#%%
def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

#%%
workpath=''
model=workpath+'testmodel.tflite'
target = 'k210'

# compile_options
compile_options = nncase.CompileOptions()
compile_options.target = target
compile_options.dump_ir = True
compile_options.dump_asm = True
compile_options.dump_dir = 'nncase/tmp'

# compiler
compiler = nncase.Compiler(compile_options)

# import_options
import_options = nncase.ImportOptions()

# import
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)

# compile
compiler.compile()

# kmodel
kmodel = compiler.gencode_tobytes()
with open(workpath+'testmodel.kmodel', 'wb') as f:
    f.write(kmodel)

#%%
def main():
    return
#%%
if __name__ == '__main__':
    main()