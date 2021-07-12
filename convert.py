import coremltools

caffe_model = ('oxford102.caffemodel', 'deploy.prototxt')
model_labels = 'flower_labels.txt'

# look into deploy.prototxt file
# find input: "data"
image_input = 'data'

coreml_model = coremltools.converters.caffe.convert(caffe_model, class_labels=model_labels,
                                                    image_input_names=image_input)
coreml_model.save('Oxford102.mlmodel')
