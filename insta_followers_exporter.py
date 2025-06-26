# insta_followers_exporter.py

# MIT License
#
# Copyright (c) 2025 damuor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import instaloader

def export_followers(username_to_scrape, output_file):
    loader = instaloader.Instaloader()
    
    try:
        # Step 1: Request credentials
        print("\n=== LOGIN ===")
        username = input("Your Instagram username: ")
        password = input("Your Instagram password: ")
        
        # Attempt login
        loader.login(username, password)
        
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        # Step 2: Handle 2FA if required
        print("\n⚠️ TWO-FACTOR AUTHENTICATION REQUIRED ⚠️")
        code_2fa = input("Enter the 6-digit code from your authentication app: ").strip()
        loader.two_factor_login(code_2fa)
        
    except Exception as e:
        print(f"\n❌ Error during login: {str(e)}")
        return

    # Step 3: Get followers
    try:
        print(f"\n🔍 Fetching followers of @{username_to_scrape}...")
        profile = instaloader.Profile.from_username(loader.context, username_to_scrape)
        followers = [follower.username for follower in profile.get_followers()]
        
        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(followers))
            
        print(f"\n✅ Done! {len(followers)} followers saved to '{output_file}'")
        
    except Exception as e:
        print(f"\n❌ Error fetching followers: {str(e)}")


if __name__ == "__main__":
    print("=== INSTAGRAM FOLLOWERS EXPORTER ===")
    target_user = input("\nTarget username (e.g., damuor_23): ").strip()
    output_filename = input("Output file name (e.g., followers.txt): ").strip()
    
    export_followers(target_user, output_filename)
