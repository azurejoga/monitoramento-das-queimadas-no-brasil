# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032d27f3-c72c-3dc5-8651-57e2dd363b41 | -25.6472 | -50.409599 | 2026-04-21 00:32:00 | METOP-B | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d08b89d-89c4-3b98-8d85-c9fd2b539113 | -27.952299 | -50.2145 | 2026-04-21 00:32:00 | METOP-B | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b66fc56f-2648-3bc7-8b49-76b8b12976c5 | -19.099001 | -56.059101 | 2026-04-21 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86fc08a5-f1b6-370b-ad14-7e597dbf4ce3 | -19.1008 | -56.0681 | 2026-04-21 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6484cfa9-6a2c-3e73-a357-95392cc5d74f | -21.9475 | -47.976601 | 2026-04-21 00:32:00 | METOP-B | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bbd50f06-967b-36cb-a7ec-c0733ea27955 | -21.039801 | -48.554298 | 2026-04-21 00:32:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b23fcdd6-fbe5-3515-8e47-4e1dc987dcd4 | -21.037701 | -48.545399 | 2026-04-21 00:32:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba247287-4992-32e4-8436-e207482fcaaa | -21.9431 | -47.958099 | 2026-04-21 00:32:00 | METOP-B | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d6e98d3-e64e-3cc7-9822-38ca3375afb1 | -21.945299 | -47.9674 | 2026-04-21 00:32:00 | METOP-B | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 06e74a13-e8b7-390b-a84d-ba3247cfe12d | -27.95115 | -50.22294 | 2026-04-21 00:33:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| d589e854-75ce-35f8-9e16-266cc3aa4557 | -25.11052 | -49.42744 | 2026-04-21 00:33:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 933017a2-fd3f-3545-88bf-8394b24974fb | -25.64032 | -50.41783 | 2026-04-21 00:33:00 | TERRA_M-M | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 0bb5cf92-9165-33de-b8b8-4f64a8113b64 | -27.95115 | -50.22293 | 2026-04-21 00:33:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 75a97c93-a73e-3857-911f-e601af581254 | -25.64032 | -50.41782 | 2026-04-21 00:33:00 | TERRA_M-M | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 5e0ebf0b-003a-3c83-b8af-c99a48df19b5 | -25.11052 | -49.42746 | 2026-04-21 00:33:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bc6c96ce-d6f7-3443-b96a-c0c450fbbf96 | -21.04345 | -48.55695 | 2026-04-21 00:35:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 27ea4b51-62ee-3e6c-a02a-eec94d49e1d8 | -21.94643 | -47.97468 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 50.9 |
| ec6d1c8f-0663-3752-8f93-d75d7b2ecb6a | -19.095 | -56.07104 | 2026-04-21 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| edf8dbc6-15af-3770-ad04-a8afbd56cc7e | -21.94845 | -47.98715 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 713d2a38-b284-341e-9b89-69e47de3d6f8 | -19.095 | -56.07103 | 2026-04-21 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 6c4b2984-215c-3c4b-834e-5ada05362d9b | -21.9376 | -47.98267 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6969e030-cad5-3aba-aa3f-05fc8c4c2ee5 | -21.04345 | -48.55696 | 2026-04-21 00:35:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 4170c165-6190-3a51-9d06-e80e648b077c | -21.94642 | -47.97469 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 1f8ea288-444c-3649-b9ad-8099a1f3807f | -21.9376 | -47.98269 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c024c4e0-f3a2-33bc-9b41-0373e08eb78f | -21.94846 | -47.98714 | 2026-04-21 00:35:00 | TERRA_M-M | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 4ab5bf34-dd1a-3bb2-aa0e-ebdc654b4bac | 2.91122 | -60.29574 | 2026-04-21 00:39:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cc26bfbf-cfd6-37fa-97eb-d8fafc83053a | 2.91122 | -60.29575 | 2026-04-21 00:39:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ce6c7526-29c1-304b-a00c-f86d0181205e | -21.955 | -47.9797 | 2026-04-21 00:40:00 | GOES-19 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a1d71870-8a3a-3552-96af-f57c0a64b2cc | -21.9557 | -47.9561 | 2026-04-21 00:40:00 | GOES-19 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4e438ff6-e088-35d7-b5ad-58bb210aabcb | -21.9341 | -47.9849 | 2026-04-21 00:40:00 | GOES-19 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bb773f33-ab9f-3659-a784-67bc35ded67e | -21.955 | -47.9797 | 2026-04-21 00:50:00 | GOES-19 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d065dc57-3018-3932-abfd-7f224911d8f8 | -21.955 | -47.9797 | 2026-04-21 01:00:00 | GOES-19 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 920be72a-2f0f-3196-86e9-ad769417a840 | -21.380199 | -48.714001 | 2026-04-21 01:04:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 42ca4c0e-a07e-3eec-b44e-bc9e932ddbe4 | -19.0947 | -56.072601 | 2026-04-21 01:04:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff34d8a5-ef11-347f-9dc4-fdb49fa0a64e | -21.040899 | -48.553299 | 2026-04-21 01:04:00 | METOP-C | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae82bef9-eff1-38de-a058-fd0745e64457 | -21.372499 | -48.7253 | 2026-04-21 01:04:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb1f100-60f3-3779-b3f6-8c1fc220ce5c | -21.948601 | -47.975399 | 2026-04-21 01:04:00 | METOP-C | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a9fe8381-1af4-31d2-b607-5243308fca6a | -21.370501 | -48.716599 | 2026-04-21 01:04:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04bc6c3e-c835-3a99-b079-ff41b79974a6 | -21.382299 | -48.722698 | 2026-04-21 01:04:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0fd0181-cd40-3fd9-982e-bbd64b681bc0 | -9.80153 | -37.4738 | 2026-04-21 03:25:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c84c0ec2-31fd-3877-861c-e5d319a586a6 | -9.94249 | -38.44027 | 2026-04-21 03:25:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 20f8983d-486e-35fb-b3ec-4c816034300b | -12.27854 | -44.61895 | 2026-04-21 03:25:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55c514b0-6965-3671-ba9b-e7f244568e25 | -9.80635 | -37.47473 | 2026-04-21 03:25:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 686789ae-9867-362c-9a91-ab9a9b3fb5aa | -9.80417 | -37.47559 | 2026-04-21 03:25:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 44b02137-2fb9-307a-987e-26729b92b1a9 | -12.23743 | -44.20034 | 2026-04-21 03:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c40cb55-fe55-3e39-be75-b4456b484318 | -9.94191 | -38.44331 | 2026-04-21 03:25:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6594e117-b6d9-319d-aaa0-c3bf552cd796 | -9.79934 | -37.47469 | 2026-04-21 03:25:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2d789e93-38d7-35e6-aed9-4462a711ae3a | -12.24331 | -44.19463 | 2026-04-21 03:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eedbe06-02ae-3430-b9ad-3336480b2e51 | -12.24188 | -44.20125 | 2026-04-21 03:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a42619e9-4c16-3afc-a1af-82f18e316365 | -12.23886 | -44.19357 | 2026-04-21 03:25:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c291c05-acc4-34a3-8ea4-4e5a1e96a943 | -9.80058 | -37.47913 | 2026-04-21 03:25:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e6be4129-9b3c-3ec4-881b-924fbe044f01 | -15.95718 | -39.10425 | 2026-04-21 03:28:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ef8ea296-3730-3d0d-a1ad-5b6ad8783e9c | -22.49731 | -43.07619 | 2026-04-21 03:30:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d80118d-6f73-3b2e-8b1f-d0d2972b1816 | -21.95366 | -48.03651 | 2026-04-21 03:30:00 | NPP-375D | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adb2ab0f-7714-3e8a-81fe-56eed0adbe87 | -22.49812 | -43.07258 | 2026-04-21 03:30:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa095032-fb65-32e5-8ed8-3558d3df6cc9 | -8.23857 | -35.7222 | 2026-04-21 03:45:00 | NOAA-20 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9d9ba800-5384-357d-a57f-3948a6af0551 | -22.33535 | -41.77323 | 2026-04-21 03:47:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b1de771-2bdc-3a65-ab49-7569b107fa96 | -9.80452 | -37.47729 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b159450-2e57-3e59-b5ca-aed5baa6df54 | -11.95333 | -43.37683 | 2026-04-21 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff910fa-3592-3ce3-a62e-38e7265f6971 | -13.95336 | -45.34046 | 2026-04-21 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 317865a1-98b0-3789-9304-a9d6c26d4238 | -9.80234 | -37.46946 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 283702f1-a5d8-3163-baea-75f0f4a8354f | -21.0405 | -48.55523 | 2026-04-21 03:47:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67e91db8-5176-3552-a5c4-906dc3dd722e | -9.94511 | -38.43927 | 2026-04-21 03:47:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 34806ecb-8654-3e54-8c4e-ec69062bde32 | -15.12977 | -41.83744 | 2026-04-21 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6c81510c-1a46-3543-a205-d1b6fccd7400 | -11.72269 | -44.73878 | 2026-04-21 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72bb2c0c-c933-351f-bd4a-7ac11bee9696 | -12.27823 | -44.61615 | 2026-04-21 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 639ba89c-1d1e-300f-9d88-2f4e35675070 | -20.32096 | -46.17074 | 2026-04-21 03:47:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b87995b-c959-37c8-8e9e-37826535f94d | -11.99503 | -47.77557 | 2026-04-21 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f4bdedc-c949-3200-8acc-c7d6225e18ab | -13.95235 | -45.34532 | 2026-04-21 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8591b951-170f-3f9a-806a-613ec67efad1 | -18.85103 | -48.27872 | 2026-04-21 03:47:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66bf99a8-e1f1-3815-b217-77efd5a2991d | -9.94098 | -38.44257 | 2026-04-21 03:47:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bd78731b-a88d-30df-b201-06ab95df1709 | -9.80114 | -37.47673 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 243af240-9787-329e-aaf9-c4ed34f2c0d0 | -14.55012 | -42.27575 | 2026-04-21 03:47:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c06acc14-86d7-39c2-927e-3458e91e2937 | -15.12889 | -41.8424 | 2026-04-21 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8bb719e0-d280-3d74-95a7-4ab0eea602d0 | -12.2398 | -44.19289 | 2026-04-21 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f079c26d-807e-30af-b51d-80de146a311e | -9.80174 | -37.47309 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3ec04d43-07e8-3bda-9f43-339b9a13d6b0 | -9.94162 | -38.43867 | 2026-04-21 03:47:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36e6a50a-a8df-3c97-b1c2-ad2f94d5b757 | -12.28205 | -44.62271 | 2026-04-21 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0733aa50-5d32-3715-97d7-b035967b1997 | -9.80512 | -37.47365 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1966e370-6399-3f99-aeb2-d0ce2634874b | -11.95695 | -43.38251 | 2026-04-21 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf358d6f-b277-301a-9729-701f965cbe91 | -18.85185 | -48.2749 | 2026-04-21 03:47:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ee46174-2eb0-3270-8a44-1437e248610e | -15.95622 | -39.10143 | 2026-04-21 03:47:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5461468f-75cc-308d-8cfd-e7720f16918b | -9.79836 | -37.47253 | 2026-04-21 03:47:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8b5d1934-f243-33df-a862-1a251405ab8b | -13.95347 | -45.33944 | 2026-04-21 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f3a83c4-2257-3842-ba5c-4e0365866a3a | -15.95961 | -39.10203 | 2026-04-21 03:47:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64e72047-d4eb-3743-933e-a2769ad053ba | -12.23882 | -44.19808 | 2026-04-21 03:47:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85c0963e-d2f4-3d99-a554-5759b3c1efe4 | -21.03971 | -48.55885 | 2026-04-21 03:47:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3839a557-bfac-3981-adc1-23c55ebca305 | -20.32383 | -46.16756 | 2026-04-21 03:47:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16487006-bd8d-3369-bf3f-e0a2e9c4c1eb | -15.42165 | -43.05255 | 2026-04-21 03:47:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edcc5cb7-3f3c-38f9-8a93-18fdab8b74a6 | -21.95211 | -48.03111 | 2026-04-21 03:49:00 | NOAA-20 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6da3faca-eccc-3f92-887f-08aa97388c8f | -25.10561 | -49.43063 | 2026-04-21 03:49:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 227746ee-1a52-3d38-b753-291d58e34b59 | -23.98069 | -48.14013 | 2026-04-21 03:49:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 21b42c56-da3d-39e4-aa45-dfaddee2c6f3 | -25.10973 | -49.38891 | 2026-04-21 03:49:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b565d50-fbdd-382a-8f90-b88777adde59 | -23.03506 | -48.43333 | 2026-04-21 03:49:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56c56d3e-a569-39c4-929f-3bb688f3812b | -17.91178 | -44.41048 | 2026-04-21 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff1a0c46-736e-35b8-a3b0-8697b605f527 | -23.64659 | -48.00089 | 2026-04-21 03:49:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 865dec19-882e-37ed-ab26-3bdeab2c5e8b | -21.37048 | -48.72121 | 2026-04-21 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53c2376a-15ef-36a1-99e2-35dd4ddec9d0 | -25.10888 | -49.39262 | 2026-04-21 03:49:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62b4b582-3245-3558-a0f2-4ded7b0a6328 | -21.36971 | -48.72472 | 2026-04-21 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927bb4f6-e1ba-371e-a9fc-31031ec22582 | -17.16304 | -46.83469 | 2026-04-21 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README2.md)
