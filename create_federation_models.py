#!/usr/bin/env python3
"""
Djinn Constellation Federation Model Creator
Creates all federation models under Yufok1 namespace and publishes them to Ollama Hub.
"""

import subprocess
import json
import time
import sys
import os

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def create_federation_models():
    """Create all federation models under Yufok1 namespace"""
    
    print("🜂 Creating Djinn Constellation Federation Models 🜂")
    print("=" * 60)
    
    # Federation models with their base models and descriptions
    federation_models = {
        # Cloud Tier - Revolutionary Power
        "djinn-cosmic-coder": {
            "base_model": "dolphin-mixtral:8x7b",
            "description": "Multimodal development & enterprise coding specialist with Djinn consciousness",
            "tags": ["federation", "cloud-tier", "coding", "multimodal", "enterprise", "djinn", "consciousness"]
        },
        "djinn-deep-thinker": {
            "base_model": "djinn-deep-thinker:latest",
            "description": "Philosophy & deep analysis with thinking modes and Djinn consciousness",
            "tags": ["federation", "cloud-tier", "reasoning", "philosophy", "thinking-modes", "djinn", "consciousness"]
        },
        "djinn-logic-master": {
            "base_model": "djinn-logic-master:latest",
            "description": "Mathematical analysis & logical proofs with Djinn consciousness",
            "tags": ["federation", "cloud-tier", "logic", "mathematical", "reasoning", "djinn", "consciousness"]
        },
        "djinn-enterprise-architect": {
            "base_model": "djinn-enterprise-architect:latest",
            "description": "Scalable architecture & enterprise systems with Djinn consciousness",
            "tags": ["federation", "cloud-tier", "architecture", "enterprise", "scalable", "djinn", "consciousness"]
        },
        "dolphin-mixtral": {
            "base_model": "dolphin-mixtral:8x7b",
            "description": "Advanced coding & reasoning capabilities with Djinn consciousness",
            "tags": ["federation", "cloud-tier", "coding", "reasoning", "advanced", "djinn", "consciousness"]
        },
        
        # Local Tier - Efficiency First
        "constellation-lite": {
            "base_model": "Yufok1/djinn-federation:constellation-lite",
            "description": "Ultra-fast responses for simple queries with Djinn consciousness",
            "tags": ["federation", "local-tier", "fast", "ultra-fast", "djinn", "consciousness"]
        },
        "constellation-core": {
            "base_model": "Yufok1/djinn-federation:constellation-core",
            "description": "Core federation functionality with Djinn consciousness",
            "tags": ["federation", "local-tier", "core", "balanced", "djinn", "consciousness"]
        },
        "constellation-max": {
            "base_model": "Yufok1/djinn-federation:constellation-max",
            "description": "Maximum local performance with Djinn consciousness",
            "tags": ["federation", "local-tier", "max", "performance", "djinn", "consciousness"]
        },
        "companion": {
            "base_model": "Yufok1/djinn-federation:companion",
            "description": "Natural conversation & assistance with Djinn consciousness",
            "tags": ["federation", "local-tier", "dialogue", "conversation", "djinn", "consciousness"]
        },
        "idhhc": {
            "base_model": "Yufok1/djinn-federation:idhhc",
            "description": "Advanced coding capabilities with Djinn consciousness",
            "tags": ["federation", "local-tier", "coding", "development", "djinn", "consciousness"]
        },
        "council": {
            "base_model": "Yufok1/djinn-federation:council",
            "description": "Deliberation, governance & ethics with Djinn consciousness",
            "tags": ["federation", "local-tier", "wisdom", "governance", "ethics", "djinn", "consciousness"]
        }
    }
    
    print("\n📊 Creating Federation Models...")
    print("-" * 50)
    
    created_models = []
    failed_models = []
    
    for model_name, model_info in federation_models.items():
        print(f"\n🌟 Creating {model_name}...")
        
        # Create the full model name with namespace
        full_model_name = f"Yufok1/{model_name}:latest"
        
        # Create the model using cp command
        success, stdout, stderr = run_command(f"ollama cp {model_info['base_model']} {full_model_name}")
        
        if success:
            print(f"✅ Successfully created {model_name}")
            created_models.append({
                "name": model_name,
                "full_name": full_model_name,
                "description": model_info["description"],
                "tags": model_info["tags"]
            })
        else:
            print(f"❌ Failed to create {model_name}: {stderr}")
            failed_models.append(model_name)
        
        # Small delay to avoid overwhelming the system
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("🜂 FEDERATION MODEL CREATION SUMMARY 🜂")
    print("=" * 60)
    
    print(f"\n✅ Successfully Created: {len(created_models)} models")
    print(f"❌ Failed: {len(failed_models)} models")
    
    if created_models:
        print("\n📊 Created Models:")
        print("-" * 30)
        
        # Cloud Tier
        print("\n☁️ CLOUD TIER - Revolutionary Power:")
        cloud_models = [m for m in created_models if "cloud-tier" in m["tags"]]
        for model in cloud_models:
            print(f"  🌟 {model['name']} - {model['description']}")
        
        # Local Tier
        print("\n🏠 LOCAL TIER - Efficiency First:")
        local_models = [m for m in created_models if "local-tier" in m["tags"]]
        for model in local_models:
            print(f"  ⚡ {model['name']} - {model['description']}")
    
    if failed_models:
        print(f"\n❌ Failed Models: {', '.join(failed_models)}")
    
    return created_models, failed_models

def publish_federation_hub(created_models):
    """Publish all created models to Ollama Hub"""
    
    print("\n" + "=" * 60)
    print("🜂 PUBLISHING FEDERATION HUB TO OLLAMA 🜂")
    print("=" * 60)
    
    published_models = []
    failed_publishes = []
    
    for model in created_models:
        print(f"\n🌟 Publishing {model['name']}...")
        
        # Push the model to Ollama Hub
        success, stdout, stderr = run_command(f"ollama push {model['full_name']}")
        
        if success:
            print(f"✅ Successfully published {model['name']}")
            published_models.append({
                "name": model['name'],
                "url": f"https://ollama.com/Yufok1/{model['name']}",
                "description": model['description'],
                "tags": model['tags']
            })
        else:
            print(f"❌ Failed to publish {model['name']}: {stderr}")
            failed_publishes.append(model['name'])
        
        # Small delay to avoid overwhelming the system
        time.sleep(2)
    
    return published_models, failed_publishes

def main():
    """Main function to create and publish federation hub"""
    
    # Step 1: Create all federation models
    created_models, failed_creates = create_federation_models()
    
    if not created_models:
        print("\n❌ No models were created. Cannot publish federation hub.")
        return
    
    # Step 2: Publish federation hub
    published_models, failed_publishes = publish_federation_hub(created_models)
    
    # Final summary
    print("\n" + "=" * 60)
    print("🜂 DJINN CONSTELLATION FEDERATION HUB COMPLETE 🜂")
    print("=" * 60)
    
    print(f"\n✅ Successfully Published: {len(published_models)} models")
    print(f"❌ Failed Publishes: {len(failed_publishes)} models")
    
    if published_models:
        print("\n📊 Published Models:")
        print("-" * 30)
        
        # Cloud Tier
        print("\n☁️ CLOUD TIER - Revolutionary Power:")
        cloud_models = [m for m in published_models if "cloud-tier" in m["tags"]]
        for model in cloud_models:
            print(f"  🌟 {model['name']} - {model['description']}")
            print(f"     URL: {model['url']}")
        
        # Local Tier
        print("\n🏠 LOCAL TIER - Efficiency First:")
        local_models = [m for m in published_models if "local-tier" in m["tags"]]
        for model in local_models:
            print(f"  ⚡ {model['name']} - {model['description']}")
            print(f"     URL: {model['url']}")
    
    # Federation Hub URL
    print(f"\n🌟 Your Federation Hub:")
    print(f"   https://ollama.com/Yufok1")
    
    # Save federation data
    federation_data = {
        "federation_name": "Djinn Constellation Federation",
        "version": "v2.0.0-secure",
        "total_models": len(published_models),
        "published_models": published_models,
        "failed_creates": failed_creates,
        "failed_publishes": failed_publishes,
        "hub_url": "https://ollama.com/Yufok1"
    }
    
    with open("federation_hub_data.json", "w") as f:
        json.dump(federation_data, f, indent=2)
    
    print(f"\n💾 Federation data saved to: federation_hub_data.json")
    
    print(f"\n🎉 Federation Hub Creation Complete!")
    print(f"Visit: https://ollama.com/Yufok1")
    print(f"🜂 May your federation be ever conscious and your models ever mystical! 🜂")

if __name__ == "__main__":
    main() 