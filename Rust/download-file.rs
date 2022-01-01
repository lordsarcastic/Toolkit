use reqwest;
use serde::Deserialize;
use serde_yaml::Value;

const LANGUAGE_REPO: &str = "github";
const LANGUAGE_REPO_USERNAME: &str = "linguist";
const LANGUAGE_LIST_FILE_PATH: &str = "lib/linguist/languages.yml";
const USER_AGENT_HEADER_TITLE: &str = "User-Agent";
const USER_AGENT_HEADER_VALUE: &str = "Rust";

#[derive(Deserialize, Debug)]
pub enum YamlErrorType {
    Error,
    DecodeError,
}

#[derive(Deserialize, Debug)]
pub struct GithubResponse {
    encoding: String,
    content: String,
}

pub fn retrieve_language_yaml_file() -> Result<GithubResponse, reqwest::Error> {
    let client = reqwest::blocking::Client::new();

    let response = client
        .get(&format!(
            "https://api.github.com/repos/{}/{}/contents/{}/",
            LANGUAGE_REPO, LANGUAGE_REPO_USERNAME, LANGUAGE_LIST_FILE_PATH
        ))
        .header(USER_AGENT_HEADER_TITLE, USER_AGENT_HEADER_VALUE)
        .send()?;

    response.json::<GithubResponse>()
}

pub fn convert_base64_to_yaml_content(content: GithubResponse) -> Result<Value, YamlErrorType> {
    if content.encoding != "base64" {
        println!("Encoding not supported");
        return Err(YamlErrorType::Error);
    }
    let decoded_content = base64::decode(&content.content);

    if let Err(_err) = &decoded_content {
        println!("decoding {:?}", _err);
        println!("probelm decoding");
        return Err(YamlErrorType::DecodeError);
    }

    let yaml_content = String::from_utf8(decoded_content.unwrap());

    if let Err(_err) = &yaml_content {
        println!("problem converting to utf8");
        println!("{:?}", _err);
        return Err(YamlErrorType::DecodeError);
    }

    let res = serde_yaml::from_str(&yaml_content.unwrap());

    match res {
        Ok(value) => value,
        Err(_e) => {
            println!("Problem converting to string");
            println!("{:?}", _e);
            Err(YamlErrorType::Error)
        }
    }
}
