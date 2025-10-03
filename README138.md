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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef8a4ec-4aaf-38c6-b0d0-37f27190e457 | -15.23271 | -48.72182 | 2025-10-03 05:25:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfc44433-081a-3f88-b161-f9efc8c58d3e | -8.7586 | -49.93161 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0def633-bcf9-347a-8dab-a7e529aa6627 | -8.61311 | -54.97395 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86c37b3f-b881-3606-938a-7609f9206ec5 | -16.68521 | -53.01363 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9c49d19-08b1-30ef-8ffc-cb56dbcce972 | -16.17019 | -57.59474 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 220cd806-b274-3ca9-8576-beeef243c184 | -14.86059 | -49.31142 | 2025-10-03 05:25:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f9cb3269-b2d5-3a2e-a110-d40f5ac70606 | -16.68429 | -53.02195 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0b6a03c-8e3f-332b-a4ba-17feae8cae64 | -16.18184 | -57.60028 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1ee48514-9aee-3e75-91b0-8011792c7d23 | -8.54281 | -50.15313 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28500986-eb42-34f7-b9c7-354db2eabce7 | -18.40279 | -50.77759 | 2025-10-03 05:25:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c5ccda9-8225-31f1-b773-83088e1eeb84 | -8.61744 | -54.97454 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af744ff-d245-32ba-a74e-89180e222538 | -14.5792 | -52.46354 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eb1f7adc-0374-3b27-ad1e-c514fccb2acc | -15.99149 | -50.86761 | 2025-10-03 05:25:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a900f048-e025-35ba-bcf7-d324dbfc9093 | -8.62773 | -54.97821 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d90fc490-e8d1-32e9-9353-def554c057ef | -16.68464 | -53.01962 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1184721d-2ec1-3b78-8be3-751dd32737a4 | -18.18902 | -53.29031 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa6b58aa-304f-39ee-887f-8dfb9cc7b140 | -14.46642 | -48.40527 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffd86d73-3e59-32a1-84e4-72868d984e57 | -8.55846 | -48.64904 | 2025-10-03 05:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e4c0053-1bd9-39dd-989e-154198784518 | -16.17915 | -57.58928 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 51f1f50c-b04f-3ed8-8c49-0a684bad87aa | -13.21952 | -50.89029 | 2025-10-03 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 786d88d8-c598-33aa-8d35-284e9e962be7 | -8.61252 | -54.97811 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc37d729-c875-383a-8e8f-cac1159975d2 | -13.21898 | -50.89494 | 2025-10-03 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9392b73-3a76-3bec-a5e1-5baa4933c711 | -15.01766 | -56.03832 | 2025-10-03 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ab040b5-057e-3485-9112-4c863fdd5f5a | -8.62283 | -54.98182 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4deadd0c-cfbf-312e-b382-2954643f010d | -13.36581 | -58.05511 | 2025-10-03 05:25:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 934d46b9-0276-3629-a757-a45c584f8b96 | -16.18323 | -57.58961 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ac298d8e-18ad-3bc0-b8aa-21b25baee996 | -7.50513 | -48.85438 | 2025-10-03 05:25:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92abcfd8-d507-3ded-afa6-f9f38c12a383 | -14.4863 | -48.46307 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 74a9cb40-729a-3e66-82c7-efe00aa058ad | -8.62116 | -54.97931 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c129873d-9bf5-3e7f-8cf4-197dea2f35c3 | -16.40126 | -52.15922 | 2025-10-03 05:25:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5af0d745-b89d-3b03-abbb-8cd2ff8ce704 | -14.98154 | -49.95541 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 11948c33-c835-3694-9171-20e488273a27 | -8.61863 | -54.96622 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c346cbd8-3029-3ea1-aec4-e1c9bc7b08d4 | -9.16533 | -50.83963 | 2025-10-03 05:25:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa601469-7841-36bd-8215-868fc5764637 | -18.16118 | -53.34418 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a773e945-c968-30cc-9e42-2d67825746c7 | -13.6879 | -48.63963 | 2025-10-03 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96eb1848-6bc3-3922-b161-03b8c23a41fb | -16.06175 | -51.04452 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f90ea7be-4433-357c-b3be-33d179fa06d5 | -8.02281 | -55.42055 | 2025-10-03 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8411d4cb-a955-37e6-b9f5-39b72fa52d5f | -8.71167 | -47.98641 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6886e623-fbf7-3109-b1ca-0a3616870052 | -18.40225 | -50.78331 | 2025-10-03 05:25:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e3ba55-dacc-3b6a-a0a0-fdfd736a0e60 | -14.8572 | -48.35664 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9237ae3d-ed93-37d7-a6d9-be50baee1b08 | -15.23349 | -48.71389 | 2025-10-03 05:25:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b7db4a5-7ccb-3963-955c-a9cdd445862e | -14.86426 | -48.35851 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e2e1537-bc36-3f2e-93be-b6d54b5a91bd | -16.17965 | -57.58542 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| da2f9517-eae0-3cb7-bbbd-707c94ef72a4 | -8.61419 | -54.98059 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5a87fec-2488-360f-8622-d4699836a0f5 | -9.47715 | -47.87219 | 2025-10-03 05:25:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b7fa48d-7ac3-38e6-98e8-fabb71042258 | -15.02707 | -56.03499 | 2025-10-03 05:25:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 073d440a-8607-3a69-9985-9d65a53d59b2 | -8.71243 | -47.98015 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb84b8c7-f43d-3fe3-b3fc-a8e2d075345a | -16.6898 | -53.02269 | 2025-10-03 05:25:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8de067ec-9552-3ad7-b09f-6cffc726dc35 | -16.16659 | -57.59072 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b1f57f73-35e1-3551-8619-a5ff0b37526f | -15.24735 | -49.29619 | 2025-10-03 05:25:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc36d8e8-f553-3013-bfa5-b837129b827c | -14.58054 | -52.45171 | 2025-10-03 05:25:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c335ba18-fceb-3cc5-adec-05a7af23eed6 | -16.07104 | -51.00407 | 2025-10-03 05:25:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac28767f-bc6e-3020-89eb-1dd95365500e | -8.12393 | -50.24089 | 2025-10-03 05:25:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e454fb4e-b39e-3709-988d-f188094eb24a | -15.24052 | -49.29541 | 2025-10-03 05:25:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75cc05ad-0607-3cd0-b3ca-b5323978171e | -14.38299 | -48.47836 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 616b7a4f-dd26-34e0-b309-9a12f93a8da8 | -8.0275 | -55.41739 | 2025-10-03 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4bc31d-d4a4-30b2-831f-c125b0c07e9d | -8.61155 | -54.96751 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88098a0e-7d29-32b7-b9cb-1ed6dad08fed | -13.63522 | -48.67339 | 2025-10-03 05:25:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbc58776-93cf-3369-80b7-e941cd4511aa | -14.9881 | -49.96553 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ecb1f30-9108-35b0-82d7-159eda52fd14 | -8.62603 | -54.99068 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9fa565-cae1-3d78-acf5-fc37d4a15a39 | -7.93613 | -55.02204 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d286fee8-4e89-3857-8234-5c6c75ef6130 | -15.24789 | -50.1268 | 2025-10-03 05:25:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 602c3082-46eb-3103-9243-d5e6c74f6432 | -14.98161 | -49.96429 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 135cc297-89b2-35f1-8019-06c632983d46 | -8.55797 | -48.65292 | 2025-10-03 05:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eab88503-50c4-3c7b-bc67-dab8087129e0 | -8.62177 | -54.97511 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28b1d9a8-4870-3540-a16e-c6e7baa3c43c | -18.40338 | -50.77912 | 2025-10-03 05:25:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b6b22d-8c24-33a7-a1a9-862b2bb42339 | -16.16617 | -57.59396 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9f3b9970-5c63-3284-ae5d-f88aa6192514 | -13.21454 | -50.89261 | 2025-10-03 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cb852dc-75c7-3200-b076-6755e999954e | -8.75975 | -49.92226 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38b79113-3a9c-3edd-9f84-9f8534d6a683 | -8.61908 | -54.97705 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 505adbab-86f4-3ac4-8ff8-3f5ac62c12b9 | -6.33904 | -58.04985 | 2025-10-03 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea8a8569-b961-3b66-bf46-4a4cdae724e0 | -8.54224 | -50.1576 | 2025-10-03 05:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec7323fc-25eb-3fa3-b84e-2027953b991a | -8.62716 | -54.98238 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5edb1301-2d46-3294-8aad-b188fc4d83bb | -18.16076 | -53.34828 | 2025-10-03 05:25:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba8f2b21-4e1c-35c0-8e99-42f1afc8dcb7 | -14.98217 | -49.95887 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 908262b7-f777-3273-9829-a409baf44501 | -13.63587 | -48.67539 | 2025-10-03 05:25:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2deb0b1d-b4f8-3ce4-93d6-153fefb5f41a | -15.23899 | -49.29699 | 2025-10-03 05:25:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c697d3-2715-3899-806a-87fd48f2ac54 | -12.22994 | -60.84668 | 2025-10-03 05:25:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59fbbf78-e5b1-3574-9f9c-631e637662a2 | -15.24849 | -50.12091 | 2025-10-03 05:25:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ada7fd4-e40c-3141-a64e-b108fde5b380 | -16.1778 | -57.59962 | 2025-10-03 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a19cf229-040b-37bf-919a-51ce83000c3b | -14.97354 | -49.96959 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0324222-6a2c-3e95-8b14-59f7ae20f71c | -13.68252 | -48.63409 | 2025-10-03 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff6c0c08-26ed-3a02-b137-e36bd9da621c | -15.9942 | -50.90407 | 2025-10-03 05:25:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b622f2c-a12e-39c4-b185-eb90fb02a495 | -14.98108 | -49.96937 | 2025-10-03 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4704fc81-cc30-3884-adae-2ec03ae14279 | -15.2458 | -49.29798 | 2025-10-03 05:25:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 346a6633-1f18-389f-a3f8-5f603bc07ec0 | -7.5067 | -48.85491 | 2025-10-03 05:25:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf9fbf37-9f58-37f3-b140-ee76955e8299 | -8.55137 | -48.65226 | 2025-10-03 05:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8d12e04a-4dff-3bbb-a2cb-907e7638da90 | -7.24908 | -49.4113 | 2025-10-03 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8331b20b-53f4-3784-bf58-2531c84d8b23 | -15.99476 | -50.8984 | 2025-10-03 05:25:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 599ee9a4-5366-3af1-9170-919fa0c1a2ff | -15.99104 | -50.87215 | 2025-10-03 05:25:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50fe4f9f-7253-3481-826d-3bd4398cd3d0 | -8.61371 | -54.96979 | 2025-10-03 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e55ddd72-ac80-3861-be8d-9db5bbf90a09 | -14.46578 | -48.41184 | 2025-10-03 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be701a16-1571-3bee-9cf5-a8323420fcdc | 4.55063 | -60.70283 | 2025-10-03 05:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 292deeac-0295-382a-82f0-b6d83337dd14 | 4.38724 | -60.11792 | 2025-10-03 05:48:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c3b64b0-10b0-334e-8a7e-be6aad43ee82 | 4.55506 | -60.70655 | 2025-10-03 05:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d85694f-2482-344e-bd30-0a27f86e906c | 4.55133 | -60.70716 | 2025-10-03 05:48:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eed1176-e375-3e33-9796-c2b6404bbc67 | 1.75374 | -55.86587 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60aa916c-248f-38af-83d4-614f4225b8bc | 1.78634 | -55.82861 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a84f0eb-7efd-3e04-a0cd-e439ca64e5c5 | 1.52481 | -55.85034 | 2025-10-03 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da71b63c-12ce-3da8-967d-7eb8500c9dbf | -1.07794 | -53.68549 | 2025-10-03 05:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README139.md)
