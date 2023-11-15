from typing import Callable, Optional, Sequence, Tuple, List
import torch
from torch import nn


from cs285.agents.dqn_agent import DQNAgent


class AWACAgent(DQNAgent):
    def __init__(
        self,
        observation_shape: Sequence[int],
        num_actions: int,
        make_actor: Callable[[Tuple[int, ...], int], nn.Module],
        make_actor_optimizer: Callable[[torch.nn.ParameterList], torch.optim.Optimizer],
        temperature: float,
        **kwargs,
    ):
        super().__init__(observation_shape=observation_shape, num_actions=num_actions, **kwargs)

        self.actor = make_actor(observation_shape, num_actions)
        self.actor_optimizer = make_actor_optimizer(self.actor.parameters())
        self.temperature = temperature

    def compute_critic_loss(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
        rewards: torch.Tensor,
        next_observations: torch.Tensor,
        dones: torch.Tensor,
    ):
        with torch.no_grad():
            # TODO(student): compute the actor distribution, then use it to compute E[Q(s, a)]
            next_actions = self.actor(next_observations).sample()
            
            next_qa_values = self.critic(
                next_observations).gather(1, next_actions.unsqueeze(1))
            
            # Use the actor to compute a critic backup
            next_qs = next_qa_values.mean(dim=-1, keepdim=True)
 
            # TODO(student): Compute the TD target
            target_values = rewards + self.discount * next_qs * (1 - dones.float())

        # TODO(student): Compute Q(s, a) and loss similar to DQN
        q_values = self.critic(observations).gather(1, actions.unsqueeze(1)).squeeze(1)
        
        assert q_values.shape == target_values.shape
        loss = nn.MSELoss()(q_values, target_values)
        qa_values = q_values
        
        return (
            loss,
            {
                "critic_loss": loss.item(),
                "q_values": q_values.mean().item(),
                "target_values": target_values.mean().item(),
            },
            {
                "qa_values": qa_values,
                "q_values": q_values,
            },
        )

    def compute_advantage(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
        action_dist: Optional[torch.distributions.Categorical] = None,
    ):
        # TODO(student): compute the advantage of the actions compared to E[Q(s, a)]
        qa_values = self.critic(observations).gather(1, actions.unsqueeze(1))
        if action_dist is None:
            action_dist = self.actor(observations)            
        q_values = torch.sum(
            action_dist.probs * self.critic(observations).gather(1, action_dist.sample().unsqueeze(1)), dim=1)
        # values = ...
        advantages = qa_values - q_values
        return advantages

    def update_actor(
        self,
        observations: torch.Tensor,
        actions: torch.Tensor,
    ):
        # TODO(student): update the actor using AWAC
        action_log_probs = self.actor(observations).log_prob(actions)
        advantages = self.compute_advantage(observations, actions)
        weights = torch.exp(advantages / self.temperature)
        loss = -torch.mean(weights * action_log_probs)

        self.actor_optimizer.zero_grad()
        loss.backward()
        self.actor_optimizer.step()

        return loss.item()

    def update(self, observations: torch.Tensor, actions: torch.Tensor, rewards: torch.Tensor, next_observations: torch.Tensor, dones: torch.Tensor, step: int):
        metrics = super().update(observations, actions, rewards, next_observations, dones, step)

        # Update the actor.
        actor_loss = self.update_actor(observations, actions)
        metrics["actor_loss"] = actor_loss

        return metrics
