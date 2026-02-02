import tensorflow as tf
import os
import functools

model_path = os.path.join("models", "oral_lesion_model.h5")

# Monkey patch to handle mismatched Keras versions (quantization_config issue)
original_from_config = tf.keras.layers.Dense.from_config

# original_from_config is a bound method, so we don't pass cls to it again
def patched_from_config(cls, config):
    if 'quantization_config' in config:
        config.pop('quantization_config')
    return original_from_config(config)

# Apply patch specifically to Dense
tf.keras.layers.Dense.from_config = classmethod(patched_from_config)

# Also patch other common layers just in case
layers_to_patch = [tf.keras.layers.Conv2D, tf.keras.layers.DepthwiseConv2D, tf.keras.layers.SeparableConv2D]
for layer_cls in layers_to_patch:
    original_fc = layer_cls.from_config
    
    def create_patched(orig):
        def patched(cls, config):
            if 'quantization_config' in config:
                config.pop('quantization_config')
            return orig(config)
        return patched
    
    layer_cls.from_config = classmethod(create_patched(original_fc))


try:
    print(f"Loading model from {model_path}...")
    model = tf.keras.models.load_model(model_path, compile=False)
    
    print("\n" + "="*30)
    print("MODEL INSPECTION REPORT")
    print("="*30)
    
    output_shape = model.output_shape
    print(f"Output Shape: {output_shape}")
    
    # Check last layer
    last_layer = model.layers[-1]
    # print(f"Last Layer Units: {last_layer.output_shape[-1]}") <--- This was crashing
    
    print("\n" + "="*30)
    print("MODEL ARCHITECTURE SUMMARY (Manual)")
    print("="*30)
    
    # Check FIRST layer
    first_layer = model.layers[0]
    print(f"First Layer Name: {first_layer.name}")
    try:
        print(f"First Layer Config: {first_layer.get_config()}")
    except:
        print("Could not get first layer config")

    # Check input shape
    print(f"Model Input Shape: {model.input_shape}")
    
    print("\nCONCLUSION:")
    if output_shape[-1] == 1:
        print("-> This is a BINARY classification model.")
    else:
        print(f"-> This is a MULTI-CLASS classification model ({output_shape[-1]} classes).")
    print("="*30 + "\n")

except Exception as e:
    print(f"Error loading model: {e}")
