mod wallet;

use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name="urc-cli", version="0.1")]
struct Args {
    #[command(subcommand)]
    cmd: Cmd,
}

#[derive(Subcommand)]
enum Cmd {
    Keygen,
}

fn main() -> anyhow::Result<()> {
    let args = Args::parse();
    match args.cmd {
        Cmd::Keygen => {
            let (pk, addr) = wallet::keygen();
            println!("PUBLIC_KEY_HEX: {}", pk);
            println!("ADDRESS: {}", addr);
        }
    }
    Ok(())
}
