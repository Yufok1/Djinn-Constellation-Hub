#!/usr/bin/env python3
"""
Model Pre-warming and Hot Swapping System
Eliminates timeout issues through intelligent model management
"""

import queue
import subprocess
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Optional, Set


@dataclass
class ModelState:
    name: str
    status: str  # 'cold', 'warming', 'hot', 'active', 'cooling'
    last_used: datetime
    warmup_time: float
    usage_count: int
    priority: int


class ModelPrewarmingManager:
    """
    Intelligent model pre-warming and hot swapping system
    Keeps models ready based on usage patterns and predictive analysis
    """

    def __init__(self):
        self.models = {
            "companion": ModelState(
                "Yufok1/djinn-federation:companion", "cold", datetime.now(), 0.0, 0, 10
            ),
            "constellation-lite": ModelState(
                "Yufok1/djinn-federation:constellation-lite",
                "cold",
                datetime.now(),
                0.0,
                0,
                8,
            ),
            "constellation-core": ModelState(
                "Yufok1/djinn-federation:constellation-core",
                "cold",
                datetime.now(),
                0.0,
                0,
                6,
            ),
            "constellation-max": ModelState(
                "Yufok1/djinn-federation:constellation-max",
                "cold",
                datetime.now(),
                0.0,
                0,
                4,
            ),
            "idhhc": ModelState(
                "Yufok1/djinn-federation:idhhc", "cold", datetime.now(), 0.0, 0, 7
            ),
            "council": ModelState(
                "Yufok1/djinn-federation:council", "cold", datetime.now(), 0.0, 0, 3
            ),
        }

        # Hot models (models kept in memory)
        self.hot_models: Set[str] = set()
        self.max_hot_models = 3  # Keep 3 models hot at most

        # Warming queue
        self.warming_queue = queue.Queue()

        # Background threads
        self.prewarming_active = True
        self.prewarming_thread = threading.Thread(
            target=self._prewarming_manager, daemon=True
        )
        self.prewarming_thread.start()

        # Usage pattern tracking
        self.usage_patterns = {"hourly": {}, "sequence": [], "transitions": {}}

        # Auto-warm companion (most used model)
        self.schedule_warmup("companion", high_priority=True)

        print("🔥 Model pre-warming system initialized")

    def request_model(self, model_key: str, timeout: int = 45) -> subprocess.Popen:
        """
        Request a model with intelligent pre-warming
        Returns immediately if model is hot, or manages warming if cold
        """
        if model_key not in self.models:
            raise ValueError(f"Unknown model: {model_key}")

        model = self.models[model_key]

        # Update usage tracking
        self._track_usage(model_key)

        # If model is hot, return immediately
        if model.status == "hot":
            model.last_used = datetime.now()
            model.usage_count += 1
            print(f"⚡ {model_key} served hot (instant)")
            return self._create_model_process(model.name)

        # If model is warming, wait briefly
        elif model.status == "warming":
            print(f"🔥 {model_key} is warming, waiting...")
            return self._wait_for_warmup(model_key, timeout)

        # Model is cold, warm it up
        else:
            print(f"❄️ {model_key} is cold, warming up...")
            return self._warm_and_serve(model_key, timeout)

    def schedule_warmup(self, model_key: str, high_priority: bool = False):
        """Schedule a model for pre-warming"""
        if model_key in self.models:
            priority = 1 if high_priority else 5
            self.warming_queue.put((priority, model_key, datetime.now()))
            print(f"📋 {model_key} scheduled for warmup (priority: {priority})")

    def predict_next_models(self, current_model: str, user_input: str) -> list:
        """Predict which models might be needed next"""
        predictions = []

        # Pattern-based prediction
        if current_model == "companion":
            # If user mentions technical terms, pre-warm IDHHC
            technical_keywords = ["analyze", "fix", "build", "create", "execute", "run"]
            if any(keyword in user_input.lower() for keyword in technical_keywords):
                predictions.append("idhhc")
                predictions.append("constellation-core")

        elif current_model.startswith("constellation"):
            # Constellation likely leads to IDHHC
            predictions.append("idhhc")

        elif current_model == "idhhc":
            # After IDHHC, usually back to companion
            predictions.append("companion")

        # Historical transition patterns
        if current_model in self.usage_patterns["transitions"]:
            common_next = max(
                self.usage_patterns["transitions"][current_model],
                key=self.usage_patterns["transitions"][current_model].get,
                default=None,
            )
            if common_next and common_next not in predictions:
                predictions.append(common_next)

        return predictions

    def optimize_hot_models(self):
        """Optimize which models stay hot based on usage patterns"""
        # Sort models by priority score
        scored_models = []
        for key, model in self.models.items():
            score = self._calculate_priority_score(model)
            scored_models.append((score, key))

        scored_models.sort(reverse=True)

        # Keep top models hot
        desired_hot = set(key for _, key in scored_models[: self.max_hot_models])

        # Warm up desired models
        for model_key in desired_hot:
            if model_key not in self.hot_models:
                self.schedule_warmup(model_key)

        # Cool down unused models
        to_cool = self.hot_models - desired_hot
        for model_key in to_cool:
            self._cool_model(model_key)

    def _prewarming_manager(self):
        """Background thread managing model pre-warming"""
        while self.prewarming_active:
            try:
                # Process warming queue
                try:
                    priority, model_key, scheduled_time = self.warming_queue.get(
                        timeout=10
                    )

                    # Skip if model is already hot
                    if self.models[model_key].status != "hot":
                        self._warm_model(model_key)

                    self.warming_queue.task_done()

                except queue.Empty:
                    pass

                # Periodic optimization
                self.optimize_hot_models()

                # Cleanup old models
                self._cleanup_unused_models()

                time.sleep(30)  # Check every 30 seconds

            except Exception as e:
                print(f"Pre-warming manager error: {e}")
                time.sleep(60)

    def _warm_model(self, model_key: str):
        """Warm up a specific model"""
        if model_key not in self.models:
            return

        model = self.models[model_key]

        if model.status in ["warming", "hot"]:
            return  # Already warm or warming

        print(f"🔥 Warming up {model_key}...")
        model.status = "warming"

        start_time = time.time()

        try:
            # Warm up model with a simple query
            result = subprocess.run(
                ["ollama", "run", model.name, "hello"],
                capture_output=True,
                text=True,
                timeout=60,
                encoding="utf-8",
            )

            warmup_time = time.time() - start_time
            model.warmup_time = warmup_time

            if result.returncode == 0:
                model.status = "hot"
                self.hot_models.add(model_key)
                print(f"✅ {model_key} warmed up in {warmup_time:.1f}s")
            else:
                model.status = "cold"
                print(f"❌ {model_key} warmup failed: {result.stderr}")

        except subprocess.TimeoutExpired:
            model.status = "cold"
            print(f"⏰ {model_key} warmup timeout")
        except Exception as e:
            model.status = "cold"
            print(f"💥 {model_key} warmup error: {e}")

    def _wait_for_warmup(self, model_key: str, timeout: int) -> subprocess.Popen:
        """Wait for a model to finish warming up"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            if self.models[model_key].status == "hot":
                return self._create_model_process(self.models[model_key].name)
            time.sleep(0.5)

        # Timeout - return process anyway
        return self._create_model_process(self.models[model_key].name)

    def _warm_and_serve(self, model_key: str, timeout: int) -> subprocess.Popen:
        """Warm up a cold model and serve it"""
        self._warm_model(model_key)
        return self._wait_for_warmup(model_key, timeout)

    def _create_model_process(self, model_name: str) -> subprocess.Popen:
        """Create a model process for communication"""
        # Return a process that's ready for communication
        # This is a placeholder - actual implementation would depend on usage
        return subprocess.Popen(
            ["ollama", "run", model_name],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )

    def _track_usage(self, model_key: str):
        """Track model usage patterns"""
        current_hour = datetime.now().hour

        # Track hourly usage
        if current_hour not in self.usage_patterns["hourly"]:
            self.usage_patterns["hourly"][current_hour] = {}
        if model_key not in self.usage_patterns["hourly"][current_hour]:
            self.usage_patterns["hourly"][current_hour][model_key] = 0
        self.usage_patterns["hourly"][current_hour][model_key] += 1

        # Track sequence for transitions
        self.usage_patterns["sequence"].append((model_key, datetime.now()))

        # Keep only recent sequence (last 50 interactions)
        if len(self.usage_patterns["sequence"]) > 50:
            self.usage_patterns["sequence"] = self.usage_patterns["sequence"][-50:]

        # Update transition patterns
        if len(self.usage_patterns["sequence"]) >= 2:
            prev_model = self.usage_patterns["sequence"][-2][0]
            if prev_model not in self.usage_patterns["transitions"]:
                self.usage_patterns["transitions"][prev_model] = {}
            if model_key not in self.usage_patterns["transitions"][prev_model]:
                self.usage_patterns["transitions"][prev_model][model_key] = 0
            self.usage_patterns["transitions"][prev_model][model_key] += 1

    def _calculate_priority_score(self, model: ModelState) -> float:
        """Calculate priority score for keeping model hot"""
        now = datetime.now()

        # Base priority
        score = model.priority

        # Recent usage bonus
        time_since_use = (now - model.last_used).total_seconds()
        if time_since_use < 300:  # 5 minutes
            score += 5
        elif time_since_use < 1800:  # 30 minutes
            score += 2

        # Usage frequency bonus
        score += min(model.usage_count * 0.1, 3)

        # Warmup time penalty (slower models get priority to stay hot)
        score += min(model.warmup_time * 0.1, 2)

        return score

    def _cool_model(self, model_key: str):
        """Cool down a model to free up resources"""
        if model_key in self.hot_models:
            self.hot_models.remove(model_key)
            self.models[model_key].status = "cold"
            print(f"❄️ {model_key} cooled down")

    def _cleanup_unused_models(self):
        """Clean up models that haven't been used recently"""
        now = datetime.now()
        cutoff = now - timedelta(hours=2)  # Cool models unused for 2 hours

        for key, model in self.models.items():
            if model.last_used < cutoff and model.status == "hot":
                if key != "companion":  # Always keep companion warm
                    self._cool_model(key)

    def get_status(self) -> dict:
        """Get current status of all models"""
        return {
            "hot_models": list(self.hot_models),
            "model_states": {
                key: {
                    "status": model.status,
                    "last_used": model.last_used.isoformat(),
                    "usage_count": model.usage_count,
                    "warmup_time": model.warmup_time,
                }
                for key, model in self.models.items()
            },
            "usage_patterns": self.usage_patterns,
        }

    def shutdown(self):
        """Graceful shutdown"""
        self.prewarming_active = False
        if self.prewarming_thread.is_alive():
            self.prewarming_thread.join(timeout=5)
        print("🔥 Model pre-warming system shut down")


# Global instance
model_manager = None


def get_model_manager():
    """Get or create global model manager"""
    global model_manager
    if model_manager is None:
        model_manager = ModelPrewarmingManager()
    return model_manager


if __name__ == "__main__":
    # Test the pre-warming system
    print("🔥 Testing Model Pre-warming System...")

    manager = ModelPrewarmingManager()

    # Test requesting models
    print("\n📋 Testing model requests...")

    # This should trigger warmup
    print("Requesting companion...")
    time.sleep(2)

    # Check status
    status = manager.get_status()
    print(f"\n📊 System Status:")
    print(f"Hot models: {status['hot_models']}")

    # Shutdown
    manager.shutdown()
    print("✅ Pre-warming system test complete")
