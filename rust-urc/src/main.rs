mod core;
mod wallet;

use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name="urc-cli", version="1.0")]
struct Args {
    #[command(subcommand)]
    cmd: Cmd,
}

#[derive(Subcommand)]
enum Cmd {
    /// Generate a new Ed25519 keypair
    Keygen,

    /// Sign a message with secret key hex
    Sign {
        seckey: String,
        msg: String,
    },

    /// Verify a signature
    Verify {
        pubkey: String,
        msg: String,
        sig: String,
    },
}

fn main() -> anyhow::Result<()> {
    let args = Args::parse();

    match args.cmd {
        Cmd::Keygen => {
            let (pk, addr) = wallet::keygen();
            println!("PUBLIC_KEY_HEX: {}", pk);
            println!("ADDRESS: {}", addr);
        }

        Cmd::Sign { seckey, msg } => {
            let sig = core::sign_msg(&seckey, msg.as_bytes());
            println!("SIG_HEX: {}", sig);
        }

        Cmd::Verify { pubkey, msg, sig } => {
            let ok = core::verify_sig(&pubkey, msg.as_bytes(), &sig);
            println!("VALID: {}", ok);
        }
    }

    Ok(())
}

