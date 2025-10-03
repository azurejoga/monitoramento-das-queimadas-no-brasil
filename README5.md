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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9032a65-a057-32ce-9450-d418212f75a2 | -14.91151 | -48.30059 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9ade355d-1c6c-341f-a692-60544aed8876 | -17.59283 | -46.66063 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ce64c579-9890-3566-83b5-897df2982afe | -15.99481 | -50.87436 | 2025-10-03 00:50:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b0b24aec-b244-3f3b-8c4a-47299d3215e5 | -18.40535 | -50.77503 | 2025-10-03 00:50:00 | TERRA_M-M | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| efd81213-cc16-3575-9de1-757447a0a9ba | -14.91458 | -48.34863 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6f87d3f8-2adb-3573-8694-9779948bf4a6 | -15.80578 | -46.26462 | 2025-10-03 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0a7502dc-42bb-3c81-8b7a-0619ed823105 | -14.7382 | -48.12958 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a9be9c4a-ebd1-383d-9ef6-ddb9ac00a042 | -14.69773 | -43.88793 | 2025-10-03 00:50:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 4687823a-ddb6-32b4-a321-370c63f30a5d | -14.89673 | -46.97272 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1e1bbbf4-58f2-361f-b0a0-f1de234efcd5 | -14.90824 | -46.9702 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 212eb49d-4384-39ca-9fbf-efaac319a694 | -14.60092 | -46.71229 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c36e9de2-4444-3372-981e-869493c0f385 | -15.90398 | -56.18916 | 2025-10-03 00:50:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| e70303bb-2232-37b4-9ab2-3780c70b41e5 | -14.93508 | -46.91534 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e396cc22-bcef-367d-8e06-533904fa32d4 | -16.33873 | -49.9449 | 2025-10-03 00:50:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aa97acd4-0110-32be-84e2-5b9671eca10b | -15.09993 | -43.47579 | 2025-10-03 00:50:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 21e32aa1-fa59-377a-bd10-656b2aae3eb8 | -15.93945 | -46.2153 | 2025-10-03 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7c81f419-3f18-3bbf-a852-60519c745996 | -14.90724 | -48.34268 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9b2664d9-0ecd-35b8-b9bf-732a3f630c82 | -17.8171 | -52.03373 | 2025-10-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8ee5c8d5-0ae5-305d-a8c3-7938cb97194a | -16.04346 | -51.02153 | 2025-10-03 00:50:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de2203ee-fe6f-35d5-9ae6-8c8a51eb5f59 | -15.09711 | -43.46959 | 2025-10-03 00:50:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 81f8a24c-a1a1-3dd5-b367-dc3ca8e7ab49 | -15.91919 | -43.34547 | 2025-10-03 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c0abf6f8-ca96-3c70-a43c-ae3f7f6c4a8e | -15.29002 | -49.30131 | 2025-10-03 00:50:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9275edca-e966-3b62-9128-0be31d3e0169 | -14.97675 | -49.96148 | 2025-10-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 984a71f2-10bc-3bc0-82e3-e3ab4a160dd3 | -15.35218 | -47.06663 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a7740b4b-298b-3d2c-9675-a6440e95c914 | -15.73359 | -51.29896 | 2025-10-03 00:50:00 | TERRA_M-M | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01b4d0f8-d8b4-3e59-843a-d1d54f7fc199 | -17.03397 | -52.23636 | 2025-10-03 00:50:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ddce8148-23a0-34ad-8423-8ffdef1491a5 | -14.91854 | -48.30645 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a4616992-6868-3b24-ac11-0840830268a2 | -16.03896 | -50.92609 | 2025-10-03 00:50:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e7b3a30-5bed-3884-8f9e-4d741d9571ef | -15.55803 | -48.19455 | 2025-10-03 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 420fb367-aed6-3b51-8edc-5236e9bc298e | -17.58572 | -46.6837 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| e1715d56-974e-3c7f-ab46-a8a7dbfe9d90 | -15.23901 | -50.12352 | 2025-10-03 00:50:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e617738d-159b-3609-8068-5d94649cc3cd | -14.90067 | -46.85186 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| dfa4567a-78d6-3790-a36b-f7aefdfeacdf | -16.33721 | -49.93462 | 2025-10-03 00:50:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65d104d6-3d3e-33a5-8fdf-a205b95c2384 | -14.95124 | -47.51641 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ad2679e6-df59-391e-9e96-cf894069f619 | -15.90952 | -56.18216 | 2025-10-03 00:50:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| ee1f465d-3f0c-3bf7-b0e3-e8bb285697e0 | -15.99894 | -50.90295 | 2025-10-03 00:50:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fddd38e9-8ac1-3639-a37c-faf165079038 | -16.07012 | -51.0113 | 2025-10-03 00:50:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0812abb-abe8-3d77-bec4-bf74e91be193 | -14.7022 | -43.91092 | 2025-10-03 00:50:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 38.3 |
| b73b1317-2728-3882-97cf-6b6861e8a7e6 | -14.9011 | -48.30291 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 11bc02e8-1dae-3eb5-9cf2-05a4dc3324a4 | -14.93231 | -46.89831 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| adefed03-04c4-311e-ab00-77e01649c0f2 | -14.91248 | -48.33561 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| acef28a9-6e1a-3849-bbbd-8d9e17f5becb | -16.18428 | -57.58519 | 2025-10-03 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| ed57534f-104c-322a-85e1-972450c36e20 | -16.17707 | -57.59164 | 2025-10-03 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 3f9cc892-a028-3624-b787-05c3d9ffae1b | -18.33957 | -52.0119 | 2025-10-03 00:50:00 | TERRA_M-M | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 485b05f2-2f8a-37ed-9f6b-9ac4fb2ab79f | -15.24682 | -50.11181 | 2025-10-03 00:50:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef08160b-998e-3bfb-aaac-9c32f3e95659 | -15.09331 | -49.56847 | 2025-10-03 00:50:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d86540d1-ac04-36cc-ab86-521c4ec0fd52 | -17.59445 | -46.66612 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 10d798d5-65f1-3d4a-be97-3599ba899e5c | -15.21566 | -47.65094 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 34928daf-198b-3684-a47f-caa1552ccfcd | -14.4407 | -46.38019 | 2025-10-03 00:50:00 | TERRA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9c3d3bbb-bb33-3159-a215-0f3d294f33a5 | -15.17472 | -43.63837 | 2025-10-03 00:50:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 75d2394c-112a-3d79-b72e-a29e8d01b502 | -18.39781 | -50.78589 | 2025-10-03 00:50:00 | TERRA_M-M | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d538b336-90b2-316b-9c42-fafb91d8a062 | -14.95371 | -47.53197 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 66ac2aa6-1311-3ab2-ada6-0da72fe3a735 | -15.57893 | -48.19112 | 2025-10-03 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0924d63b-12fd-307a-98a0-699806fd73f3 | -15.29173 | -49.31249 | 2025-10-03 00:50:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| c4b527c0-0435-3e23-aae2-26f0efe2b11b | -16.68907 | -53.01907 | 2025-10-03 00:50:00 | TERRA_M-M | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eb579d44-38d2-3444-ac68-0745bf586b67 | -15.73493 | -51.30828 | 2025-10-03 00:50:00 | TERRA_M-M | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15ffd899-e1f5-32a9-aef4-bd1fe813fe81 | -15.95133 | -46.21206 | 2025-10-03 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ba1eeb89-a1fc-3fe7-9531-9de6c6ca6e63 | -15.22242 | -47.96688 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 52227f5a-e3dc-37cf-a698-229f3fe42914 | -14.89792 | -46.83518 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0ab20231-502d-3e1f-a6fe-86e75a273d77 | -14.88622 | -48.34541 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b19f297d-5908-3788-a489-cd2324af8325 | -16.76749 | -43.967 | 2025-10-03 00:50:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 58b2c479-89d9-37ee-95dd-9dee2bfea65b | -15.5854 | -46.94228 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 09fa3b0d-4914-3d89-9daa-1807d4ebedad | -14.89677 | -48.34425 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4f7acdd6-e94d-3f21-99e9-8ea9277ff7ad | -15.35242 | -47.07684 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 19bbd4fe-5a3a-3f30-bcb0-260afed8526c | -14.6727 | -48.09052 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 798be000-c99a-3799-8652-4f430027bfbd | -15.1181 | -46.68233 | 2025-10-03 00:50:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b22573f4-6651-3339-998a-2bdc1ea247a8 | -15.36023 | -46.28535 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4521ac04-da35-30e9-8cf4-a47c76951975 | -14.94433 | -46.89857 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a1a690e5-a16a-3524-83c6-ab60b234ca7f | -15.46596 | -51.56343 | 2025-10-03 00:50:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d928877-e445-3a02-86a7-b1e929c8e618 | -17.81583 | -52.02451 | 2025-10-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a22798ff-9763-3b23-bb57-931fc6e6ff80 | -15.57413 | -46.94548 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1ab155f5-202b-3b0f-8e53-b6001863d0a3 | -14.97828 | -49.97191 | 2025-10-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9a249aca-6e3e-3a76-8494-3fc3dd236a57 | -14.74889 | -48.12805 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a847e999-b185-38d4-b967-edbcbc73d66f | -14.74686 | -48.11521 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 580086fe-bd1b-3200-955e-2642a789c5be | -14.90612 | -48.2961 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 940628dd-0c6b-352b-beed-83971166b06a | -15.21337 | -47.6367 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 449d3ce1-1c42-30ab-8c57-cf9e2b2a459d | -14.88896 | -46.85384 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 152.7 |
| b7f99aab-41e4-3891-9676-0ba699dcb085 | -17.59699 | -46.68174 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 770ae875-5687-3883-97e4-ca3413eb12bf | -16.34838 | -47.09336 | 2025-10-03 00:50:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aedeaad2-ba7b-3fc2-8269-9b197d710620 | -15.24946 | -49.2975 | 2025-10-03 00:50:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8e1739a1-68b6-3902-b38a-c4d27cfea998 | -14.89804 | -47.83438 | 2025-10-03 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 94612e76-7a1f-3eeb-a79f-217af89f56aa | -17.58318 | -46.66815 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 7e5acea5-1220-305e-95d9-ac4973f6de9c | -14.91761 | -48.3403 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 83b2b6e4-c86e-34f4-aca6-514c8bbb97fb | -15.9436 | -46.2072 | 2025-10-03 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 97163b67-10f6-397f-8d3e-d8a1f8b0d62e | -16.06875 | -51.00182 | 2025-10-03 00:50:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 98fcd48f-ce3d-36b5-88a3-90eb136a77e6 | -17.59549 | -46.67622 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 309.7 |
| cdc1a25e-c05c-36a3-9d28-10cbf31c49c8 | -14.73407 | -48.10355 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cde8adf4-b9b8-33e9-93e2-8d210051bd37 | -14.8991 | -48.28992 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7302cbbd-bc61-3ce5-9046-b1561123210e | -14.68357 | -48.08994 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8b3c42d1-c824-3448-911e-e546814e87f2 | -15.57651 | -46.95998 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0917885b-30e9-30dd-ae63-a2cf5ad905d7 | -15.32272 | -46.39026 | 2025-10-03 00:50:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 06f6e191-7d78-3e25-9e33-de784ea929ad | -17.59812 | -46.69168 | 2025-10-03 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 28.7 |
| a8bd916d-b489-3edd-9a26-74fd18ba2858 | -15.24832 | -50.1219 | 2025-10-03 00:50:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 6856cd7d-f566-3732-bc18-ee002c487f0c | -14.98115 | -49.95513 | 2025-10-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5c01da93-8601-3c57-9113-b7700a0448fa | -14.88618 | -46.83711 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 55548aa5-b044-3e93-b329-e9bc2bb270de | -15.11509 | -46.69355 | 2025-10-03 00:50:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 965b920e-badf-30b4-9083-219d32a98ab3 | -14.91554 | -48.32679 | 2025-10-03 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c0408089-d5fb-3da3-b65a-9d9c02f4f2ee | -15.22957 | -47.9714 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 90cb8944-55e8-348d-85b4-c77d6a451ba8 | -15.34958 | -47.05994 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e6b05633-b0c2-3180-9b17-836263ba61f3 | -15.25865 | -47.91891 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |


[Clique aqui para ver as próximas entradas](README6.md)
