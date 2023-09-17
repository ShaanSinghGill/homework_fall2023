Command to achieve atleast 30% on imitation learning: 
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Ant.pkl \
--env_name Ant-v4 --exp_name bc_ant --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Ant-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000

Command to achieve less than 30% on imitation learning: 
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000

Command for achieve hyperparameter tuning: 
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 1
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 10
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 100
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 1000
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 10000
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name bc_Hopper --n_iter 1 \
--expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000 --train_batch_size 100000

Command to run dagger for Ant task(first task): 
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Ant.pkl \
--env_name Ant-v4 --exp_name dagger_ant --n_iter 10 \
--do_dagger --expert_data cs285/expert_data/expert_data_Ant-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000

Command to run dagger for Hopper task(Second task): 
python cs285/scripts/run_hw1.py \
--expert_policy_file cs285/policies/experts/Hopper.pkl \
--env_name Hopper --exp_name dagger_Hopper --n_iter 10 \
--do_dagger --expert_data cs285/expert_data/expert_data_Hopper-v4.pkl \
--video_log_freq -1 --batch_size 10000 --eval_batch_size 10000