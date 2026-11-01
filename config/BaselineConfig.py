
out_dir = 'out'
eval_interval = 10 # keep frequent because we'll overfit
eval_iters = 100
log_interval = 10 # don't print too too often

always_save_checkpoint = True
init_from='scratch'

wandb_log = True # override via command line if you like
wandb_project = 'Final'
wandb_run_name = 'BaselineModel'

dataset = 'CodeSnippets'
gradient_accumulation_steps = 4
batch_size = 12
block_size = 512 # context of up to 512 previous characters
layerNorm=True

n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.0

learning_rate = 6e-4 
max_iters = 800
lr_decay_iters = 600 # make equal to max_iters usually
min_lr = 6e-5 # learning_rate / 10
beta2 = 0.95

warmup_iters = 50

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model
