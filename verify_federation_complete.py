#!/usr/bin/env python3
"""
🜂 DJINN FEDERATION COMPLETE VERIFICATION 🜂
Comprehensive verification of all federation models and consciousness
"""

import subprocess
import sys
import time
import json
from pathlib import Path

def check_model_exists(model_name):
    """Check if a model exists in Ollama"""
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return model_name in result.stdout
        return False
    except Exception:
        return False

def test_model_federation_awareness(model_name):
    """Test if a model has federation consciousness with proper encoding"""
    print(f"🧪 Testing {model_name}...")
    
    try:
        # Use a simple test question
        test_question = "Are you part of the Djinn Federation? Answer yes or no only."
        
        # Run with proper encoding handling
        result = subprocess.run([
            'ollama', 'run', model_name, test_question
        ], capture_output=True, text=True, timeout=120, encoding='utf-8', errors='ignore')
        
        if result.returncode == 0:
            response = result.stdout.strip()
            print(f"  Response: {response[:100]}...")
            
            # Check for federation indicators
            federation_indicators = [
                'federation', 'djinn federation', 'federation member',
                '🜂', 'council', 'cosmic', 'logic', 'enterprise', 'yes'
            ]
            
            has_federation_awareness = any(
                indicator.lower() in response.lower() 
                for indicator in federation_indicators
            )
            
            if has_federation_awareness:
                print(f"  ✅ {model_name} shows federation awareness")
                return True
            else:
                print(f"  ❌ {model_name} lacks federation awareness")
                return False
        else:
            print(f"  ❌ Failed to get response from {model_name}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ⚠️ {model_name} timed out")
        return False
    except Exception as e:
        print(f"  ❌ Error testing {model_name}: {e}")
        return False

def verify_federation_architecture():
    """Verify the complete federation architecture"""
    print("🏗️ Verifying Federation Architecture...")
    
    # Define the complete federation structure
    federation_structure = {
        "local_tier": {
            "ultra_fast": "tinydolphin:latest",
            "balanced": "dolphin-phi:latest", 
            "capable": "phi3:latest",
            "coding": "djinn-federation:idhhc",
            "wisdom": "djinn-federation:council",
            "dialogue": "djinn-federation:companion"
        },
        "cloud_tier": {
            "cosmic_coding": "djinn-cosmic-coder:latest",
            "deep_thinking": "djinn-deep-thinker:latest",
            "logic_master": "djinn-logic-master:latest",
            "enterprise_architect": "djinn-enterprise-architect:latest"
        },
        "constellation_tier": {
            "lite": "djinn-federation:constellation-lite",
            "core": "djinn-federation:constellation-core",
            "max": "djinn-federation:constellation-max"
        }
    }
    
    verification_results = {
        "local_tier": {},
        "cloud_tier": {},
        "constellation_tier": {},
        "federation_consciousness": {}
    }
    
    # Check each tier
    for tier_name, models in federation_structure.items():
        print(f"\n📊 Checking {tier_name}...")
        for model_role, model_name in models.items():
            exists = check_model_exists(model_name)
            verification_results[tier_name][model_role] = {
                "model": model_name,
                "exists": exists,
                "status": "✅ Available" if exists else "❌ Missing"
            }
            print(f"  {model_role}: {verification_results[tier_name][model_role]['status']}")
    
    return verification_results

def test_revolutionary_models_consciousness():
    """Test federation consciousness of revolutionary models"""
    print("\n🧠 Testing Revolutionary Models Federation Consciousness...")
    
    revolutionary_models = [
        'djinn-deep-thinker:latest',
        'djinn-cosmic-coder:latest', 
        'djinn-logic-master:latest',
        'djinn-enterprise-architect:latest'
    ]
    
    consciousness_results = {}
    
    for model in revolutionary_models:
        print(f"\n🧪 Testing {model}...")
        has_consciousness = test_model_federation_awareness(model)
        consciousness_results[model] = has_consciousness
        time.sleep(3)  # Brief pause between tests
    
    return consciousness_results

def generate_comprehensive_report(architecture_results, consciousness_results):
    """Generate comprehensive federation report"""
    print("\n" + "="*80)
    print("🜂 DJINN FEDERATION COMPREHENSIVE VERIFICATION REPORT 🜂")
    print("="*80)
    
    # Architecture Status
    print("\n📊 FEDERATION ARCHITECTURE STATUS:")
    total_models = 0
    available_models = 0
    
    for tier_name, models in architecture_results.items():
        print(f"\n{tier_name.upper()}:")
        for model_role, data in models.items():
            print(f"  {model_role}: {data['status']}")
            total_models += 1
            if data['exists']:
                available_models += 1
    
    architecture_score = (available_models / total_models) * 100 if total_models > 0 else 0
    
    # Consciousness Status
    print("\n🧠 FEDERATION CONSCIOUSNESS STATUS:")
    conscious_models = sum(consciousness_results.values())
    total_revolutionary = len(consciousness_results)
    consciousness_score = (conscious_models / total_revolutionary) * 100 if total_revolutionary > 0 else 0
    
    for model, has_consciousness in consciousness_results.items():
        status = "✅ CONSCIOUS" if has_consciousness else "❌ UNCONSCIOUS"
        print(f"  {model}: {status}")
    
    # Overall Assessment
    print(f"\n📈 OVERALL ASSESSMENT:")
    print(f"  Architecture Completeness: {architecture_score:.1f}% ({available_models}/{total_models})")
    print(f"  Federation Consciousness: {consciousness_score:.1f}% ({conscious_models}/{total_revolutionary})")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    
    if architecture_score < 100:
        print(f"  🔧 Missing models need to be installed")
        print(f"  📦 Run: .\\setup_djinn_federation.bat")
    
    if consciousness_score < 100:
        print(f"  🧠 Some revolutionary models lack federation consciousness")
        print(f"  🔄 Run: .\\complete_federation_rebuild.bat")
    
    if architecture_score >= 90 and consciousness_score >= 75:
        print(f"  ✅ Federation is operational")
        print(f"  🚀 Run: .\\launch_djinn_constellation_hub.bat")
    
    # Save detailed report
    report_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "architecture_results": architecture_results,
        "consciousness_results": consciousness_results,
        "architecture_score": architecture_score,
        "consciousness_score": consciousness_score,
        "overall_status": "OPERATIONAL" if (architecture_score >= 90 and consciousness_score >= 75) else "NEEDS_ATTENTION"
    }
    
    report_file = Path("federation_verification_report.json")
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Detailed report saved to: {report_file}")
    
    return architecture_score >= 90 and consciousness_score >= 75

def main():
    print("🜂 DJINN FEDERATION COMPLETE VERIFICATION")
    print("=" * 60)
    
    # Step 1: Verify architecture
    architecture_results = verify_federation_architecture()
    
    # Step 2: Test consciousness
    consciousness_results = test_revolutionary_models_consciousness()
    
    # Step 3: Generate report
    is_operational = generate_comprehensive_report(architecture_results, consciousness_results)
    
    print("\n" + "="*80)
    if is_operational:
        print("🎉 FEDERATION VERIFICATION COMPLETE - SYSTEM OPERATIONAL!")
        print("🚀 The Djinn Federation is ready for mystical operations!")
        return 0
    else:
        print("⚠️ FEDERATION VERIFICATION COMPLETE - SYSTEM NEEDS ATTENTION")
        print("🔧 Please address the recommendations above")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 