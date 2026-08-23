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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47f117d9-0785-3aa6-955e-b0c463a3ad1c | -13.67125 | -51.85072 | 2026-08-23 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3053b45-6470-3e36-a263-02083770900f | -15.22349 | -48.23987 | 2026-08-23 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0e197e4-d809-3161-a88d-21b178033128 | -17.16035 | -46.40735 | 2026-08-23 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 875bdb4e-0f83-3396-bbe2-9391a4c3ba51 | -14.37353 | -51.77967 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8e4eeb3-cf82-3039-906b-80d03cee0e00 | -14.37846 | -51.78064 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ede85cc-2870-318f-a91b-88cb285a3152 | -12.56006 | -47.93835 | 2026-08-23 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fa4563d-21dc-3c36-a1e5-814f81524963 | -14.39324 | -51.78359 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35fc798e-24bb-3bf2-b124-142ad6ef6c36 | -8.53591 | -54.83104 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af225db5-93c6-31a4-818a-490e4dbc1fa0 | -11.14646 | -46.18069 | 2026-08-23 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e3312ed-4843-3180-a077-fab721707180 | -11.43182 | -44.53329 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 601a81b3-8e35-32b1-bf91-3c76e35ec694 | -13.93727 | -45.35023 | 2026-08-23 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10fc04a8-9901-31d2-bdf9-9603ad6d1cba | -8.53043 | -54.82413 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 599b006a-1698-3407-887b-39105de03b64 | -15.0425 | -48.68577 | 2026-08-23 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6455078e-6902-35ff-865f-dfd786419908 | -10.83822 | -50.97374 | 2026-08-23 04:10:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 060a0ba3-06dd-3e0a-961d-66f44e071c2f | -13.19459 | -51.44502 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee0b799-f7ab-389b-bff6-19b0b60b520f | -12.7527 | -48.41276 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 244067bf-44a0-3c91-8ade-2e8cdd186514 | -12.74865 | -48.41188 | 2026-08-23 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b9dd38d-3f78-3804-838f-98998ebf0b9c | -18.0329 | -43.03657 | 2026-08-23 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7a932460-1157-31ad-9a86-b5241bcb1e98 | -12.40903 | -42.89864 | 2026-08-23 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 30ac5d09-3892-3859-ba4d-8263a9dffbf5 | -11.44602 | -44.53182 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 236f5545-2bdb-311c-828d-2d4fc602c1fb | -9.42644 | -51.66936 | 2026-08-23 04:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 496493cf-deaa-33b2-853d-700cd59370f3 | -13.25937 | -51.59737 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c9ee7d-67f7-3cbe-8300-034ba05fc2a2 | -18.47648 | -43.94564 | 2026-08-23 04:12:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ada6b4b7-85c1-3de1-936a-e087ed9c3dcc | -20.96601 | -48.92489 | 2026-08-23 04:12:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88b1e6a7-8ada-392b-8994-c24978ce339d | -19.46305 | -46.81372 | 2026-08-23 04:12:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 279d664f-78de-3e2f-9101-bdde687ddeb5 | -19.89155 | -44.74936 | 2026-08-23 04:12:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0caba51-05d3-347a-94f1-c8065800d7ce | -20.27069 | -48.65825 | 2026-08-23 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db368c76-2faf-36d7-9697-cf661ba439ac | -20.66464 | -46.56613 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a17b18a-3f08-303e-bf1c-8cdbbd62a123 | -21.24546 | -47.83825 | 2026-08-23 04:12:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65011a1a-eed5-3ded-9483-304c7aeb9ebf | -18.64275 | -43.9241 | 2026-08-23 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabe5227-e6a7-307a-8dd4-f58ee3a66de0 | -20.65448 | -46.56438 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bceacee-f99d-3ab2-8302-86e27e24b389 | -20.27437 | -48.65897 | 2026-08-23 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da9f557a-4380-3ff8-8eed-4b4c53f97f70 | -18.99306 | -46.32022 | 2026-08-23 04:12:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15457f6c-5eee-3844-8ad6-d39529569f23 | -21.45156 | -46.14558 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 1aaee940-dbba-379c-ad46-0ea4a57b0157 | -19.81952 | -46.92968 | 2026-08-23 04:12:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b273f0b9-a47b-3309-9057-90bc9eeeafb4 | -19.83153 | -43.88055 | 2026-08-23 04:12:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34eb4a5f-444e-3b3f-b3b6-9527c57b6af9 | -19.87784 | -45.69539 | 2026-08-23 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 555fbadd-6d4a-32b6-8c17-558f1210b8ee | -19.62961 | -45.73528 | 2026-08-23 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cef06901-7fbd-3de9-beff-cf3ff552b9a3 | -20.66063 | -46.5693 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 389c629e-f7c8-3a16-8041-49c3f6edbb12 | -21.45551 | -46.14244 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 752ef462-0feb-310c-b40d-de8e7b2c0710 | -17.75622 | -47.02616 | 2026-08-23 04:12:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83145cc3-4843-364f-8c3f-2e04c49fd0f7 | -19.80719 | -45.64457 | 2026-08-23 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 519c3047-e2c6-358a-b154-25cb86e6fd6d | -19.95979 | -46.0668 | 2026-08-23 04:12:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4794b268-4136-3f9a-ab94-0049bb768306 | -20.49027 | -47.12582 | 2026-08-23 04:12:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eeb1286-ea84-3786-859e-7531696d4cd1 | -20.27353 | -48.66362 | 2026-08-23 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e9cf201-2e04-3023-a080-ee66eeb58425 | -17.75484 | -47.03428 | 2026-08-23 04:12:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dcbf8c8-5383-3428-8b92-aa705d6d7b7f | -23.12586 | -48.67833 | 2026-08-23 04:12:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84c2e8cf-a604-342a-9140-80ba96f81995 | -22.00886 | -45.31886 | 2026-08-23 04:12:00 | NOAA-21 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef3c4f3c-b1d2-3238-87c2-6a811f8d99aa | -21.4549 | -46.14619 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 574ab570-1574-3a3a-b33b-77c12cafa711 | -21.45823 | -46.14681 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c98d0a9-1872-3339-988e-2835b004d26c | -18.54023 | -47.15947 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a005f80-c96c-37f4-9b87-8dc0d8f9969d | -20.10839 | -43.68223 | 2026-08-23 04:12:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6868a86-b8b1-3361-b02a-9447328d05be | -17.75063 | -47.03769 | 2026-08-23 04:12:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6c053e17-f686-38c2-afad-ecf1b5abe438 | -20.61636 | -46.04907 | 2026-08-23 04:12:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94a14ccf-1b19-3a10-90f8-82460c48ee46 | -20.96148 | -48.92884 | 2026-08-23 04:12:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5000933-d16a-302d-bb27-52df22df79f7 | -20.65596 | -46.57646 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df4bead8-8db2-3805-9a89-872f30304354 | -21.45884 | -46.14306 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 195eaa1a-26e4-3df2-a5a6-d40a890186f4 | -20.65258 | -46.57587 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fd0cbcc-6672-3ff2-951a-83c6b39b5e28 | -18.04328 | -47.2821 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14a124ff-5e3f-3b15-aff6-bd0043d6b43f | -20.6585 | -46.56116 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 98d5200f-11a1-31bb-b08b-1152ae2cc355 | -20.87549 | -45.73063 | 2026-08-23 04:12:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 487c8f8f-d102-3877-b4c1-8c0904f889e0 | -21.44823 | -46.14497 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c259034c-ea75-30c3-9bfe-0fbce126b153 | -20.4896 | -47.12981 | 2026-08-23 04:12:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3367ee67-08ab-3880-acbe-c1f4c8cca788 | -19.78661 | -43.70187 | 2026-08-23 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8b24ad7-1f05-3333-9692-f7ebb7bcd8a2 | -18.51438 | -46.59982 | 2026-08-23 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2aa18258-af5c-38ca-8a0e-a16995f1f02a | -19.81112 | -45.64145 | 2026-08-23 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1263d13b-ff7c-3ad2-bbfa-feee6fafd4a2 | -21.45218 | -46.14182 | 2026-08-23 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| e2383101-2961-3153-b4f1-815b10588c4f | -20.25304 | -44.05247 | 2026-08-23 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebbffcfa-0574-3a6e-899a-edd05de98925 | -18.52901 | -47.16166 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4dd6ae42-f7a8-3920-b614-e095df9c75b0 | -18.59702 | -47.12703 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 690127c0-37ad-3393-867a-327193e57966 | -20.65787 | -46.56496 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6ea2783-6c24-3298-ba07-3084fa6321e9 | -20.65678 | -46.59253 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5247fc-80e7-38c6-ad0a-d6cba5793645 | -18.5255 | -47.16102 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94b1f4ff-ac4c-3b2c-8290-fceda47f4f64 | -20.67626 | -45.27397 | 2026-08-23 04:12:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aec28e13-d3c5-3728-9d69-3d7f935800cf | -18.53252 | -47.16231 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd2de7ad-c9a1-3b61-8519-cd74239c1178 | -20.65322 | -46.57203 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5aa1ed-7dc7-3617-8089-7d11c6ee1492 | -18.08354 | -46.94023 | 2026-08-23 04:12:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abfc7243-b319-3d3c-b610-7e20054a8bfc | -19.82227 | -46.93438 | 2026-08-23 04:12:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c05cd602-eb8a-3a14-95e5-9a146a916281 | -20.65999 | -46.57315 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f4a5ae-cb12-3332-8c3e-12ba120ba50c | -17.75132 | -47.03362 | 2026-08-23 04:12:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9c992c15-c663-386d-a24b-905d28acd67d | -18.53673 | -47.15879 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1526340-1be6-3525-b993-5f18005e8c30 | -19.78716 | -43.69817 | 2026-08-23 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 728178aa-b2a1-3767-ad9f-97bcb4f925e5 | -20.65724 | -46.56876 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6498968-e829-3388-b508-41df835d7625 | -19.64962 | -46.04964 | 2026-08-23 04:12:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8db0309e-96a7-368b-8147-92bc0e63a1e6 | -19.45962 | -46.8131 | 2026-08-23 04:12:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b246c8b-eeab-3d32-b055-7703f5d19625 | -17.88537 | -51.67049 | 2026-08-23 04:12:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92eb5b5a-5553-3721-9c9a-5f9d848664ad | -19.64536 | -45.72278 | 2026-08-23 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 330327d9-a5af-3363-a6d9-9c55394d7908 | -18.27906 | -43.30167 | 2026-08-23 04:12:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8333bc44-44d2-3623-a929-a0425000bb8d | -20.64855 | -46.57914 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85ddefb3-5f54-3e92-b2dc-088e10d01d5c | -20.66125 | -46.56553 | 2026-08-23 04:12:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02683606-3f2e-33ec-a8bb-32d00be625e3 | -23.54898 | -47.4504 | 2026-08-23 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 453c5ba1-46c4-3f47-83b7-5f711cdc2e52 | -19.93184 | -40.78835 | 2026-08-23 04:12:00 | NOAA-21 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 95974623-1b2c-3fee-ab04-25675aa9911f | -18.47317 | -43.94511 | 2026-08-23 04:12:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eb481ef-438a-304f-9c40-1bbd5aa3e4a1 | -18.2785 | -43.30536 | 2026-08-23 04:12:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6af977cc-0227-33ae-98c9-a8d8b2e85811 | -20.96518 | -48.92955 | 2026-08-23 04:12:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a38e369-938d-3c59-9e77-16d54ff3234b | -19.93561 | -40.78873 | 2026-08-23 04:12:00 | NOAA-21 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 174406f4-5bd5-3a86-b8cb-2c0410d1c8fe | -19.64202 | -45.72219 | 2026-08-23 04:12:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 484179c6-d154-3676-befe-922d7bb6ae76 | -18.9949 | -49.46341 | 2026-08-23 04:12:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3216d32-7f57-306d-b1d9-62c0805d1dac | -18.04683 | -47.28275 | 2026-08-23 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d0ccf51-83a0-3a56-a5cc-3593a63c5613 | -19.8282 | -43.87998 | 2026-08-23 04:12:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
