#!/usr/bin/env python3
"""
Enhanced Predictive Analytics Framework
IDHHC's Advanced Pattern Recognition System

Leverages comprehensive cross-model view to predict user needs,
optimize model selection, and enhance decision-making quality.
"""

import json
import statistics
import threading
import time
from collections import defaultdict, deque
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


@dataclass
class PredictionInsight:
    """Represents a predictive insight"""

    prediction_id: str
    prediction_type: str  # 'user_intent', 'model_selection', 'complexity_level', 'collaboration_need'
    predicted_value: Any
    confidence: float  # 0.0-1.0
    reasoning: List[str]
    supporting_data: Dict[str, Any]
    timestamp: str
    validation_status: Optional[str] = None  # 'correct', 'incorrect', 'partial'


@dataclass
class UserPattern:
    """Represents a learned user pattern"""

    pattern_id: str
    pattern_type: str
    frequency: int
    last_occurrence: str
    success_rate: float
    context_factors: Dict[str, Any]


class EnhancedPredictiveAnalytics:
    """
    Enhanced Predictive Analytics leveraging Cross-Model Intelligence
    Predicts user needs, optimizes workflows, and enhances decision quality
    """

    def __init__(self, memory_dir="memory_bank", cross_model_comm=None):
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(exist_ok=True)

        # Cross-model communication reference
        self.cross_model_comm = cross_model_comm

        # Prediction models and patterns
        self.user_patterns = {}
        self.interaction_history = deque(maxlen=1000)
        self.model_performance_history = defaultdict(list)
        self.complexity_patterns = defaultdict(list)
        self.collaboration_patterns = []

        # Real-time analytics
        self.prediction_cache = {}
        self.pattern_weights = {
            "recent_interactions": 0.4,
            "historical_patterns": 0.3,
            "cross_model_insights": 0.2,
            "contextual_factors": 0.1,
        }

        # Prediction engines
        self.intent_predictor = IntentPredictionEngine()
        self.model_selector = ModelSelectionEngine()
        self.complexity_analyzer = ComplexityAnalyzer()
        self.collaboration_predictor = CollaborationPredictor()

        # Thread safety
        self.analytics_lock = threading.Lock()

        # Background analytics processor
        self.processor_active = True
        self.analytics_thread = threading.Thread(
            target=self._analytics_processor, daemon=True
        )
        self.analytics_thread.start()

        # Load existing patterns
        self.load_patterns()

        print("📊 Enhanced Predictive Analytics Framework initialized")
        print("🧠 Cross-model intelligence integration active")

    def predict_user_intent(
        self, user_input: str, context: Dict[str, Any] = None
    ) -> PredictionInsight:
        """Predict user intent based on input and comprehensive cross-model context"""
        with self.analytics_lock:
            # Get cross-model context if available
            if self.cross_model_comm:
                cross_context = self.cross_model_comm.shared_context
            else:
                cross_context = {}

            # Combine all available context
            full_context = {
                "user_input": user_input,
                "recent_interactions": list(self.interaction_history)[-5:],
                "user_patterns": self.user_patterns,
                "cross_model_context": cross_context,
                "additional_context": context or {},
            }

            # Use intent prediction engine
            predicted_intent = self.intent_predictor.predict(full_context)

            prediction = PredictionInsight(
                prediction_id=f"intent_{int(time.time())}",
                prediction_type="user_intent",
                predicted_value=predicted_intent["intent"],
                confidence=predicted_intent["confidence"],
                reasoning=predicted_intent["reasoning"],
                supporting_data=predicted_intent["supporting_data"],
                timestamp=datetime.now().isoformat(),
            )

            self.prediction_cache[prediction.prediction_id] = prediction
            return prediction

    def predict_optimal_model(
        self, user_input: str, predicted_intent: str = None
    ) -> PredictionInsight:
        """Predict optimal model selection based on comprehensive analysis"""
        with self.analytics_lock:
            # Analyze input complexity
            complexity_analysis = self.complexity_analyzer.analyze(user_input)

            # Get model performance history
            performance_context = {
                "complexity_level": complexity_analysis["complexity"],
                "domain": complexity_analysis["domain"],
                "performance_history": dict(self.model_performance_history),
                "recent_successes": self._get_recent_model_successes(),
            }

            # Use model selection engine
            optimal_model = self.model_selector.select(
                user_input, predicted_intent, performance_context
            )

            prediction = PredictionInsight(
                prediction_id=f"model_{int(time.time())}",
                prediction_type="model_selection",
                predicted_value=optimal_model["model"],
                confidence=optimal_model["confidence"],
                reasoning=optimal_model["reasoning"],
                supporting_data={
                    "complexity_analysis": complexity_analysis,
                    "performance_context": performance_context,
                    "alternative_models": optimal_model.get("alternatives", []),
                },
                timestamp=datetime.now().isoformat(),
            )

            self.prediction_cache[prediction.prediction_id] = prediction
            return prediction

    def predict_collaboration_need(
        self, task_description: str, predicted_complexity: int = None
    ) -> PredictionInsight:
        """Predict if collaboration between models would be beneficial"""
        with self.analytics_lock:
            # Analyze collaboration patterns
            collaboration_analysis = self.collaboration_predictor.analyze(
                task_description, predicted_complexity, self.collaboration_patterns
            )

            prediction = PredictionInsight(
                prediction_id=f"collab_{int(time.time())}",
                prediction_type="collaboration_need",
                predicted_value=collaboration_analysis["needed"],
                confidence=collaboration_analysis["confidence"],
                reasoning=collaboration_analysis["reasoning"],
                supporting_data={
                    "recommended_models": collaboration_analysis.get(
                        "recommended_models", []
                    ),
                    "collaboration_type": collaboration_analysis.get("type", "general"),
                    "expected_benefits": collaboration_analysis.get("benefits", []),
                },
                timestamp=datetime.now().isoformat(),
            )

            self.prediction_cache[prediction.prediction_id] = prediction
            return prediction

    def learn_from_interaction(
        self,
        user_input: str,
        model_used: str,
        outcome_quality: float,
        actual_complexity: int = None,
        collaboration_used: bool = False,
    ):
        """Learn from interaction outcomes to improve future predictions"""
        with self.analytics_lock:
            # Record interaction
            interaction_record = {
                "user_input": user_input,
                "model_used": model_used,
                "outcome_quality": outcome_quality,
                "actual_complexity": actual_complexity,
                "collaboration_used": collaboration_used,
                "timestamp": datetime.now().isoformat(),
            }

            self.interaction_history.append(interaction_record)

            # Update model performance
            self.model_performance_history[model_used].append(outcome_quality)

            # Update complexity patterns
            if actual_complexity:
                self.complexity_patterns[model_used].append(
                    {
                        "input_length": len(user_input),
                        "actual_complexity": actual_complexity,
                        "quality": outcome_quality,
                    }
                )

            # Update collaboration patterns
            if collaboration_used:
                self.collaboration_patterns.append(
                    {
                        "task_complexity": actual_complexity,
                        "models_involved": [model_used],  # Simplified for now
                        "success_rate": outcome_quality,
                        "timestamp": datetime.now().isoformat(),
                    }
                )

            # Update user patterns
            self._update_user_patterns(user_input, model_used, outcome_quality)

            # Validate previous predictions
            self._validate_predictions(interaction_record)

    def get_predictive_insights(
        self, user_input: str, full_context: bool = True
    ) -> Dict[str, PredictionInsight]:
        """Get comprehensive predictive insights for an input"""
        insights = {}

        # Predict intent
        intent_prediction = self.predict_user_intent(user_input)
        insights["intent"] = intent_prediction

        # Predict optimal model
        model_prediction = self.predict_optimal_model(
            user_input, intent_prediction.predicted_value
        )
        insights["model_selection"] = model_prediction

        # Predict complexity
        complexity = self.complexity_analyzer.analyze(user_input)["complexity"]

        # Predict collaboration need
        if complexity > 6 or full_context:
            collab_prediction = self.predict_collaboration_need(user_input, complexity)
            insights["collaboration"] = collab_prediction

        return insights

    def get_analytics_summary(self) -> Dict[str, Any]:
        """Get comprehensive analytics summary"""
        with self.analytics_lock:
            # Calculate model success rates
            model_success_rates = {}
            for model, performances in self.model_performance_history.items():
                if performances:
                    model_success_rates[model] = {
                        "average_quality": statistics.mean(performances),
                        "total_interactions": len(performances),
                        "recent_trend": statistics.mean(performances[-10:])
                        if len(performances) >= 10
                        else None,
                    }

            # Calculate pattern insights
            pattern_insights = {
                "total_patterns": len(self.user_patterns),
                "most_common_intents": self._get_most_common_intents(),
                "complexity_distribution": self._get_complexity_distribution(),
                "collaboration_success_rate": self._get_collaboration_success_rate(),
            }

            # Prediction accuracy
            prediction_accuracy = self._calculate_prediction_accuracy()

            return {
                "model_performance": model_success_rates,
                "pattern_insights": pattern_insights,
                "prediction_accuracy": prediction_accuracy,
                "total_interactions": len(self.interaction_history),
                "active_predictions": len(self.prediction_cache),
            }

    def _update_user_patterns(
        self, user_input: str, model_used: str, outcome_quality: float
    ):
        """Update learned user patterns"""
        # Extract pattern from input
        pattern_key = self._extract_pattern_key(user_input)

        if pattern_key not in self.user_patterns:
            self.user_patterns[pattern_key] = UserPattern(
                pattern_id=pattern_key,
                pattern_type="interaction",
                frequency=0,
                last_occurrence=datetime.now().isoformat(),
                success_rate=0.0,
                context_factors={"preferred_model": model_used},
            )

        pattern = self.user_patterns[pattern_key]
        pattern.frequency += 1
        pattern.last_occurrence = datetime.now().isoformat()

        # Update success rate (running average)
        current_total = pattern.success_rate * (pattern.frequency - 1)
        pattern.success_rate = (current_total + outcome_quality) / pattern.frequency

        # Update preferred model if this one performed better
        if outcome_quality > 0.8:
            pattern.context_factors["preferred_model"] = model_used

    def _extract_pattern_key(self, user_input: str) -> str:
        """Extract pattern key from user input"""
        # Simplified pattern extraction
        words = user_input.lower().split()

        # Look for key patterns
        if any(word in words for word in ["error", "bug", "fix", "problem"]):
            return "debugging"
        elif any(word in words for word in ["create", "build", "make", "develop"]):
            return "creation"
        elif any(word in words for word in ["explain", "how", "what", "why"]):
            return "explanation"
        elif any(word in words for word in ["optimize", "improve", "enhance"]):
            return "optimization"
        else:
            return "general"

    def _get_recent_model_successes(self) -> Dict[str, float]:
        """Get recent success rates for each model"""
        recent_successes = {}

        for interaction in list(self.interaction_history)[-20:]:
            model = interaction["model_used"]
            quality = interaction["outcome_quality"]

            if model not in recent_successes:
                recent_successes[model] = []
            recent_successes[model].append(quality)

        # Calculate averages
        for model in recent_successes:
            recent_successes[model] = statistics.mean(recent_successes[model])

        return recent_successes

    def _validate_predictions(self, interaction_record: Dict[str, Any]):
        """Validate previous predictions against actual outcomes"""
        # Find relevant predictions to validate
        for pred_id, prediction in list(self.prediction_cache.items()):
            if prediction.validation_status is not None:
                continue  # Already validated

            # Check if this interaction validates the prediction
            if prediction.prediction_type == "model_selection":
                if prediction.predicted_value == interaction_record["model_used"]:
                    if interaction_record["outcome_quality"] > 0.7:
                        prediction.validation_status = "correct"
                    else:
                        prediction.validation_status = "partial"
                else:
                    prediction.validation_status = "incorrect"

    def _analytics_processor(self):
        """Background processor for analytics and pattern learning"""
        while self.processor_active:
            try:
                with self.analytics_lock:
                    # Clean up old predictions
                    self._cleanup_old_predictions()

                    # Update pattern weights based on recent performance
                    self._update_pattern_weights()

                    # Save patterns
                    self.save_patterns()

                time.sleep(60)  # Process every minute

            except Exception as e:
                print(f"Analytics processor error: {e}")
                time.sleep(120)

    def _cleanup_old_predictions(self):
        """Clean up old predictions to maintain performance"""
        cutoff_time = datetime.now() - timedelta(hours=24)

        to_remove = []
        for pred_id, prediction in self.prediction_cache.items():
            pred_time = datetime.fromisoformat(prediction.timestamp)
            if pred_time < cutoff_time:
                to_remove.append(pred_id)

        for pred_id in to_remove:
            del self.prediction_cache[pred_id]

    def _update_pattern_weights(self):
        """Update pattern weights based on prediction accuracy"""
        # Simplified weight adjustment based on recent accuracy
        accuracy = self._calculate_prediction_accuracy()

        if accuracy["overall"] > 0.8:
            # Increase weight on historical patterns
            self.pattern_weights["historical_patterns"] = min(
                0.4, self.pattern_weights["historical_patterns"] + 0.05
            )
        elif accuracy["overall"] < 0.6:
            # Increase weight on recent interactions
            self.pattern_weights["recent_interactions"] = min(
                0.5, self.pattern_weights["recent_interactions"] + 0.05
            )

    def _calculate_prediction_accuracy(self) -> Dict[str, float]:
        """Calculate prediction accuracy metrics"""
        total_predictions = 0
        correct_predictions = 0
        by_type = defaultdict(lambda: {"total": 0, "correct": 0})

        for prediction in self.prediction_cache.values():
            if prediction.validation_status is not None:
                total_predictions += 1
                by_type[prediction.prediction_type]["total"] += 1

                if prediction.validation_status == "correct":
                    correct_predictions += 1
                    by_type[prediction.prediction_type]["correct"] += 1

        accuracy = {
            "overall": correct_predictions / total_predictions
            if total_predictions > 0
            else 0.0
        }

        for pred_type, counts in by_type.items():
            accuracy[pred_type] = (
                counts["correct"] / counts["total"] if counts["total"] > 0 else 0.0
            )

        return accuracy

    def save_patterns(self):
        """Save learned patterns to disk"""
        patterns_file = self.memory_dir / "predictive_patterns.json"
        try:
            patterns_data = {
                "user_patterns": {k: asdict(v) for k, v in self.user_patterns.items()},
                "interaction_history": list(self.interaction_history),
                "model_performance_history": dict(self.model_performance_history),
                "collaboration_patterns": self.collaboration_patterns,
                "pattern_weights": self.pattern_weights,
            }

            with open(patterns_file, "w", encoding="utf-8") as f:
                json.dump(patterns_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Patterns save error: {e}")

    def load_patterns(self):
        """Load learned patterns from disk"""
        patterns_file = self.memory_dir / "predictive_patterns.json"
        if patterns_file.exists():
            try:
                with open(patterns_file, "r", encoding="utf-8") as f:
                    patterns_data = json.load(f)

                # Reconstruct user patterns
                for pattern_id, pattern_dict in patterns_data.get(
                    "user_patterns", {}
                ).items():
                    self.user_patterns[pattern_id] = UserPattern(**pattern_dict)

                # Load other data
                if "interaction_history" in patterns_data:
                    self.interaction_history.extend(
                        patterns_data["interaction_history"]
                    )

                if "model_performance_history" in patterns_data:
                    for model, performances in patterns_data[
                        "model_performance_history"
                    ].items():
                        self.model_performance_history[model].extend(performances)

                if "collaboration_patterns" in patterns_data:
                    self.collaboration_patterns.extend(
                        patterns_data["collaboration_patterns"]
                    )

                if "pattern_weights" in patterns_data:
                    self.pattern_weights.update(patterns_data["pattern_weights"])

                print("📊 Predictive patterns loaded successfully")
            except Exception as e:
                print(f"Patterns load error: {e}")

    def shutdown(self):
        """Graceful shutdown"""
        self.processor_active = False
        if self.analytics_thread.is_alive():
            self.analytics_thread.join(timeout=5)
        self.save_patterns()
        print("📊 Enhanced Predictive Analytics shut down gracefully")


# Prediction Engine Classes
class IntentPredictionEngine:
    """Predicts user intent from input and context"""

    def predict(self, context: Dict[str, Any]) -> Dict[str, Any]:
        user_input = context["user_input"].lower()

        # Intent classification based on patterns
        intent_patterns = {
            "question": ["?", "how", "what", "why", "when", "where", "explain"],
            "command": ["run", "execute", "start", "launch", "create", "build"],
            "problem": ["error", "bug", "issue", "problem", "broken", "not working"],
            "optimization": ["optimize", "improve", "enhance", "better", "faster"],
            "exploration": [
                "explore",
                "investigate",
                "analyze",
                "research",
                "understand",
            ],
        }

        intent_scores = {}
        for intent, patterns in intent_patterns.items():
            score = sum(1 for pattern in patterns if pattern in user_input)
            intent_scores[intent] = score

        # Get highest scoring intent
        predicted_intent = max(intent_scores, key=intent_scores.get)
        confidence = min(0.95, intent_scores[predicted_intent] * 0.2 + 0.5)

        reasoning = [
            f"Detected {intent_scores[predicted_intent]} pattern matches for '{predicted_intent}'"
        ]

        # Add context-based reasoning
        if context.get("recent_interactions"):
            recent_intents = [
                i.get("predicted_intent") for i in context["recent_interactions"][-3:]
            ]
            if predicted_intent in recent_intents:
                confidence += 0.1
                reasoning.append("Consistent with recent interaction pattern")

        return {
            "intent": predicted_intent,
            "confidence": min(0.95, confidence),
            "reasoning": reasoning,
            "supporting_data": {"all_scores": intent_scores},
        }


class ModelSelectionEngine:
    """Selects optimal model based on various factors"""

    def select(
        self,
        user_input: str,
        predicted_intent: str,
        performance_context: Dict[str, Any],
    ) -> Dict[str, Any]:
        complexity = performance_context["complexity_level"]
        domain = performance_context["domain"]

        # Model selection logic
        model_scores = {
            "companion": 0.5,
            "constellation-lite": 0.5,
            "constellation-core": 0.5,
            "constellation-max": 0.5,
            "idhhc": 0.5,
            "council": 0.5,
        }

        # Adjust based on complexity
        if complexity <= 3:
            model_scores["companion"] += 0.3
            model_scores["constellation-lite"] += 0.3
        elif complexity <= 6:
            model_scores["constellation-core"] += 0.3
            model_scores["idhhc"] += 0.2
        else:
            model_scores["constellation-max"] += 0.3
            model_scores["idhhc"] += 0.3
            model_scores["council"] += 0.1

        # Adjust based on intent
        if predicted_intent == "command":
            model_scores["idhhc"] += 0.4
            model_scores["constellation-core"] += 0.2
        elif predicted_intent == "question":
            model_scores["companion"] += 0.3
            model_scores["council"] += 0.2
        elif predicted_intent == "problem":
            model_scores["idhhc"] += 0.3
            model_scores["constellation-max"] += 0.2

        # Adjust based on recent performance
        recent_successes = performance_context.get("recent_successes", {})
        for model, success_rate in recent_successes.items():
            model_scores[model] += (success_rate - 0.5) * 0.2

        # Select best model
        optimal_model = max(model_scores, key=model_scores.get)
        confidence = min(0.95, model_scores[optimal_model])

        reasoning = [
            f"Complexity level {complexity} favors {optimal_model}",
            f"Intent '{predicted_intent}' aligns with {optimal_model}'s capabilities",
        ]

        if optimal_model in recent_successes:
            reasoning.append(
                f"Recent success rate of {recent_successes[optimal_model]:.2f}"
            )

        # Get alternatives
        sorted_models = sorted(model_scores.items(), key=lambda x: x[1], reverse=True)
        alternatives = [model for model, score in sorted_models[1:3]]

        return {
            "model": optimal_model,
            "confidence": confidence,
            "reasoning": reasoning,
            "alternatives": alternatives,
        }


class ComplexityAnalyzer:
    """Analyzes complexity of user input"""

    def analyze(self, user_input: str) -> Dict[str, Any]:
        # Basic complexity indicators
        length_factor = min(10, len(user_input) / 20)

        complexity_indicators = {
            "technical_terms": len(
                [
                    w
                    for w in user_input.lower().split()
                    if w
                    in [
                        "function",
                        "class",
                        "method",
                        "algorithm",
                        "database",
                        "server",
                    ]
                ]
            ),
            "question_complexity": user_input.count("?"),
            "multi_part": len([c for c in user_input if c in ".,;"]) + 1,
            "code_elements": len([c for c in user_input if c in "{}[]()"]),
        }

        base_complexity = length_factor + sum(complexity_indicators.values())
        complexity = min(10, max(1, base_complexity))

        # Domain analysis
        domain = "general"
        if any(
            term in user_input.lower() for term in ["code", "programming", "function"]
        ):
            domain = "programming"
        elif any(term in user_input.lower() for term in ["data", "analysis", "report"]):
            domain = "data"
        elif any(term in user_input.lower() for term in ["system", "server", "deploy"]):
            domain = "system"

        return {
            "complexity": int(complexity),
            "domain": domain,
            "indicators": complexity_indicators,
        }


class CollaborationPredictor:
    """Predicts when collaboration between models would be beneficial"""

    def analyze(
        self,
        task_description: str,
        predicted_complexity: int,
        collaboration_patterns: List[Dict],
    ) -> Dict[str, Any]:
        complexity = predicted_complexity or 5

        # Base collaboration need
        collaboration_needed = complexity > 6
        confidence = 0.6

        reasoning = []

        # High complexity tasks benefit from collaboration
        if complexity > 7:
            collaboration_needed = True
            confidence += 0.2
            reasoning.append(
                f"High complexity ({complexity}) indicates multi-model approach needed"
            )

        # Multi-domain tasks
        domains = []
        domain_keywords = {
            "technical": ["code", "programming", "system", "technical"],
            "analytical": ["analysis", "data", "research", "study"],
            "creative": ["design", "create", "innovative", "artistic"],
            "ethical": ["ethical", "moral", "right", "wrong", "should"],
        }

        task_lower = task_description.lower()
        for domain, keywords in domain_keywords.items():
            if any(keyword in task_lower for keyword in keywords):
                domains.append(domain)

        if len(domains) > 1:
            collaboration_needed = True
            confidence += 0.15
            reasoning.append(
                f"Multi-domain task ({domains}) requires diverse expertise"
            )

        # Historical collaboration success
        if collaboration_patterns:
            recent_successes = [p["success_rate"] for p in collaboration_patterns[-5:]]
            if recent_successes and statistics.mean(recent_successes) > 0.8:
                confidence += 0.1
                reasoning.append(
                    "Historical collaboration success supports this approach"
                )

        # Recommended models for collaboration
        recommended_models = []
        if "technical" in domains:
            recommended_models.append("idhhc")
        if "analytical" in domains:
            recommended_models.extend(["constellation-core", "constellation-max"])
        if "creative" in domains:
            recommended_models.append("companion")
        if "ethical" in domains:
            recommended_models.append("council")

        # Remove duplicates while preserving order
        recommended_models = list(dict.fromkeys(recommended_models))

        return {
            "needed": collaboration_needed,
            "confidence": min(0.95, confidence),
            "reasoning": reasoning,
            "recommended_models": recommended_models,
            "type": "multi_domain" if len(domains) > 1 else "high_complexity",
            "benefits": [
                "Enhanced accuracy",
                "Diverse perspectives",
                "Comprehensive analysis",
            ],
        }


# Global analytics instance
enhanced_analytics = None


def get_enhanced_analytics():
    """Get or create global enhanced analytics instance"""
    global enhanced_analytics
    if enhanced_analytics is None:
        enhanced_analytics = EnhancedPredictiveAnalytics()
    return enhanced_analytics


if __name__ == "__main__":
    # Test the enhanced predictive analytics system
    print("📊 Testing Enhanced Predictive Analytics Framework...")

    analytics = EnhancedPredictiveAnalytics()

    # Test intent prediction
    intent_pred = analytics.predict_user_intent(
        "How do I fix this complex algorithm bug?"
    )
    print(
        f"🎯 Intent Prediction: {intent_pred.predicted_value} (confidence: {intent_pred.confidence:.2f})"
    )

    # Test model selection
    model_pred = analytics.predict_optimal_model(
        "Create a sophisticated AI system", "command"
    )
    print(
        f"🤖 Optimal Model: {model_pred.predicted_value} (confidence: {model_pred.confidence:.2f})"
    )

    # Test collaboration prediction
    collab_pred = analytics.predict_collaboration_need(
        "Build ethical AI system with complex algorithms", 8
    )
    print(
        f"🤝 Collaboration Needed: {collab_pred.predicted_value} (confidence: {collab_pred.confidence:.2f})"
    )

    # Test comprehensive insights
    insights = analytics.get_predictive_insights(
        "Optimize this machine learning model for production"
    )
    print(f"💡 Comprehensive Insights: {len(insights)} predictions generated")

    # Test learning
    analytics.learn_from_interaction(
        "Fix algorithm bug", "idhhc", 0.9, actual_complexity=7, collaboration_used=False
    )

    # Get analytics summary
    summary = analytics.get_analytics_summary()
    print(f"📈 Analytics Summary: {summary['total_interactions']} interactions analyzed")

    analytics.shutdown()
    print("✅ Enhanced Predictive Analytics test complete")
