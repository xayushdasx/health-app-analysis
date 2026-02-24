import pandas as pd
import numpy as np

np.random.seed(42)
n_users = 5000

users = pd.DataFrame({
    "user_id": range(1, n_users+1),
    "signup_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0,180,n_users), unit='D'),
    "city": np.random.choice(["Bangalore","Delhi","Mumbai","Pune","Chennai"], n_users),
    "acquisition_channel": np.random.choice(["organic","google_ads","meta_ads","referral"], n_users)
})

sessions = []
features = ["consult","pharmacy","diagnostics","browse"]

for user in users.user_id:
    for _ in range(np.random.randint(1,15)):
        sessions.append([
            np.random.randint(1000000),
            user,
            pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0,180), unit='D'),
            np.random.choice(features)
        ])

sessions = pd.DataFrame(sessions, columns=["session_id","user_id","date","feature_used"])

sub_users = np.random.choice(users.user_id, int(n_users*0.25), replace=False)

subscriptions = pd.DataFrame({
    "user_id": sub_users,
    "plan_type": np.random.choice(["199","299"], len(sub_users)),
})
subscriptions["price"] = subscriptions.plan_type.astype(int)
subscriptions["start_date"] = pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0,180,len(sub_users)), unit='D')
subscriptions["renewal_status"] = np.random.choice(["renewed","churned"], len(sub_users))

payments = pd.DataFrame({
    "payment_id": range(1,len(subscriptions)+1),
    "user_id": subscriptions.user_id,
    "amount": subscriptions.price,
    "status": np.random.choice(["success","failed"], len(subscriptions)),
    "date": subscriptions.start_date
})

users.to_csv("data/users.csv", index=False)
sessions.to_csv("data/sessions.csv", index=False)
subscriptions.to_csv("data/subscriptions.csv", index=False)
payments.to_csv("data/payments.csv", index=False)

print("data generated")