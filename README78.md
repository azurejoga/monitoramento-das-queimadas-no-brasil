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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a31e07e-8939-390e-97d8-f768e4ee59f0 | -2.24581 | -50.41013 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 490ba776-74ba-32ba-802d-671c5ef52400 | -4.09173 | -48.51286 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f894a23-9df4-3313-b44b-e091474d330e | -4.06099 | -49.28671 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12eb53c0-3991-3ce9-a037-f44cf24439b0 | -3.98756 | -48.15936 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe298deb-9c83-312c-b8ff-66078b114e2a | -4.38528 | -47.2209 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1037e516-bb00-3f8e-8534-646a7756139f | -3.07264 | -49.58206 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7368d2bb-a5c2-3805-bd55-afb4c3320765 | -2.5739 | -54.01001 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a71f5ef4-918e-3765-92cd-d7f611944b20 | -3.08455 | -50.42816 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd53c423-6f77-3820-8af8-4b93e643a64a | -2.69478 | -51.69903 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8895589-b6d9-3010-b642-594c482d38f0 | -2.89569 | -51.74989 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4790b4d8-375d-3c2d-aa6e-b0aaf7b9b06f | -3.11741 | -50.15601 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f53f448-730b-3357-816c-8f3a2766a478 | -3.99033 | -46.4237 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a784d7ea-70b8-3cac-8902-3b11a47c0fc2 | -2.26682 | -51.89718 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 131dbb55-cc35-3690-a488-e00919d31b30 | -3.44584 | -50.30691 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2d097f4-c7c1-3bdb-85d7-79043d5a4806 | -7.03796 | -48.27377 | 2024-11-10 04:38:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39c9a7aa-f565-38c8-bc67-867b339899e6 | -2.2313 | -53.77623 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e941b1a-5364-3631-99a6-867f92ed57f2 | -2.46261 | -53.97402 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a4c2f4f-6e38-32dd-85db-4e92bbd64c68 | -2.83898 | -51.80101 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efbb6cc5-3fb9-3141-98bd-a48312e013bf | -3.58635 | -50.41108 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc2fa26b-e6d6-30ca-8a1d-799a243da4f2 | -8.40978 | -44.14171 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f35fe475-7e9b-3df8-814d-1abb6e370a45 | -3.54915 | -51.53851 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d467bb-c86b-3815-8ac2-0d74670b6998 | -2.80202 | -46.60683 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aea9d075-a9f1-3259-8b83-2f099bc1a98e | -3.09791 | -53.31771 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76c83e99-cb09-3331-8a03-a9f20799a13a | -3.59465 | -47.34523 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59307e0c-732f-32b0-9db3-843a89c2191a | -3.79602 | -47.46334 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef7a0e5c-94d3-323c-8cfc-917587dd0b61 | -2.60151 | -49.26818 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6899f42-27a0-3f11-a86e-382473fa1616 | -3.59975 | -50.45835 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d4b52b8-7b7b-30a4-877d-debbfdabfe9b | -3.17178 | -49.10787 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7b8b386-8d50-3e86-ae93-ad2b21d44e59 | -3.85357 | -46.61751 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8c2c0fe-e945-39eb-8424-0d06ac9c3c8b | -2.37729 | -49.82314 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6415e49-0ca2-397e-8ed3-f169a5118a7f | -3.13603 | -45.96046 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 787e6c04-bd7d-3c36-a287-f655160680c7 | -5.08258 | -47.79165 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08aea9da-da0b-3784-9a9c-f4ae839e1dce | -1.48784 | -55.44354 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fe3085ba-4137-3812-8e58-ed4abce72d69 | -3.88901 | -46.43193 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ae3e7f-d88d-3290-b252-332c16a2ca63 | -2.87363 | -49.37193 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ad9a345-d902-3c91-a11e-3d4922f6ade8 | -2.55967 | -50.63459 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99972cf7-d5a3-3fbc-82c0-fc61cc0bef10 | -5.24463 | -46.65816 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92736e81-d1c3-3aaf-a6e6-b5a4bea008c3 | -3.2251 | -50.37801 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41968102-b1fc-39f8-8fd5-8cbb312c95f6 | -3.59082 | -50.27417 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c1da7fe-4a5f-3850-8062-69312023cfa4 | -2.58277 | -50.65772 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f08ce731-0952-3497-87b7-41f3c290c478 | -3.14836 | -52.97526 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ddc25b-41bd-3ecd-9631-e85a83d614b3 | -2.937 | -47.86755 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 719b9a3e-7192-3026-ae9f-2a6ede3eb329 | -3.20645 | -50.62951 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86b7e3f4-ff6e-35fe-bb95-82c05bedc51b | -2.274 | -50.55606 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db0e33f1-5ae4-3252-b0bb-88f9d4595721 | -2.69247 | -51.6901 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8062e43-d75f-3979-9850-d0a68517a515 | -3.20989 | -50.63007 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9f92913-88ea-32a7-a019-d4966dddf741 | -3.05048 | -51.34104 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5568cf4a-5389-396b-89e8-8eccdaa5d128 | -2.94738 | -54.68493 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dd63ebb-680a-34c4-90ce-e5656c3e76cb | -3.18492 | -54.31096 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0a7e520-7ba9-3c06-8bd4-846cf30e0a7e | -2.18414 | -51.74079 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0748fb91-de4a-34d7-aeb9-9b235faa5c36 | -2.73619 | -49.87199 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2678c75-5b81-3c96-8103-30d330601aff | -3.74579 | -50.07278 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed32b33e-9753-34ea-a308-b89edc27a8a2 | -4.28033 | -48.19061 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 125e04dd-488d-3229-98ae-30ed5ea4ea0a | -10.94954 | -40.82226 | 2024-11-10 04:38:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ea9fc9cd-c1c8-3b9e-bb1b-c19e152744eb | -2.57218 | -50.67933 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ea769ac-fcf5-3b50-8c70-97374e510c66 | -2.46248 | -50.4085 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 96067098-8b39-35c8-a876-bc47f5f8f72d | -2.69181 | -51.69426 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88c70bd5-9f90-32ae-97fc-84ad1c04a8ac | -4.38357 | -47.23182 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57a661c4-2589-3c3c-8ec6-ede4cea29f20 | -3.03446 | -48.04682 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e475ae-ccd1-3c5a-bb47-93006cce2777 | -2.99834 | -51.05888 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7b4dd5c-6a29-3cf9-ae7d-6c607c6bdc2e | -2.66288 | -48.49413 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e11fdb4-5a0e-3e2c-ae04-38ad95e06483 | -2.2867 | -50.97198 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b7e1911-e6ab-36c0-8fb1-16050970b0d1 | -2.94741 | -49.35106 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 529912e9-5e1c-3e31-afbf-1eb2c2d48202 | -2.63995 | -49.83814 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3261754d-cb54-351b-af79-f85e05858da0 | -3.23818 | -46.53829 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6012f158-df8e-307f-a708-144f631152da | -3.15679 | -54.4809 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2791d103-191b-3f0c-9826-8890745ef85b | -8.38901 | -44.10665 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86515765-49ca-3b46-99c2-fff90690e1c9 | -3.09424 | -51.2947 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd769cd7-eb49-335a-b278-cbaee24ba7b9 | -3.76331 | -51.7581 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45590fed-a311-3bf7-b776-cc176fc06bb3 | -2.84636 | -48.44507 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd99e42a-557a-3c8f-9b92-8014411c9090 | -4.08509 | -42.93324 | 2024-11-10 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7410ba8-cdb7-3388-963f-194cfb7d2d6c | -9.59746 | -36.02045 | 2024-11-10 04:38:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 466134e1-f94e-3d45-81d5-2182420c2789 | -3.95599 | -49.00803 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4645bd36-a12f-36e0-a439-5e369bffa1e1 | -4.10216 | -49.13348 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b4e43b2-9540-3d30-b214-41f4e28f7188 | -2.2165 | -50.73149 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fac12ca1-6cd5-31ef-a679-4c2d924ac21a | -3.60317 | -50.4589 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34b63a19-b525-31b6-af97-2b8638c78d23 | -2.97078 | -49.35471 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2486674-f2b4-3d00-9d68-5443177c7ade | -2.43153 | -50.40363 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c32c4060-4b90-3bdb-9424-7bb09a21a44f | -7.47279 | -43.59834 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2141d694-b744-3940-8e61-13f2eb356c35 | -2.80941 | -46.64972 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac11788d-2df1-3f95-9c09-13e63518f549 | -3.09628 | -53.32796 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8addf315-0ea8-36b6-a7b4-0a2e0d187aae | -2.21054 | -50.34345 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2858a7eb-cdd2-3af5-af08-667de249880c | -3.84744 | -46.62115 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e24ebf5-67cd-3162-a61b-8b0e29aa42a5 | -3.0777 | -50.42709 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37737ed5-2809-384a-aae6-8ab56592f2bd | -4.27177 | -48.65779 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48b3bdcb-9a67-3ca5-889f-a1ec60cce162 | -2.20205 | -50.22072 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad00753e-b6c5-3ea8-b160-c433a69ae75f | -4.12742 | -46.83922 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03f8fa3a-838b-3ae1-946b-e38603b801c0 | -4.2619 | -45.85888 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cfc5025-a1f5-33f4-8d86-03bf4153ff5a | -3.14061 | -52.97394 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4eddda5-14ed-36fb-9368-230f11c6d8ed | -3.87327 | -51.97916 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c54a522-09ee-3bf6-ad65-c5acd5784ad7 | -3.05473 | -51.06673 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 609bad20-7b98-3831-9c7d-238bbde1b90c | -3.24635 | -50.31004 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 55d2978e-39f2-31f7-8919-97f23eef2daf | -3.24111 | -46.47323 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c23d16f-a373-3669-bf19-d545b1b43327 | -5.5913 | -46.25298 | 2024-11-10 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9d9a131-2ee3-38b6-893b-b621fad1ea1b | -2.81227 | -46.65394 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 041b7466-d580-34b3-8a63-ab8aa7879dbd | -8.41625 | -44.12677 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44f15bda-cf7b-309f-97dd-29ac542ee7c9 | -3.04332 | -50.37991 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a93b609-7377-3b86-9171-b0982b51d4e9 | -4.06154 | -49.28325 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 425bbf1f-adfc-323a-8687-fc969fdb39da | -6.27925 | -44.74091 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 375de28b-dd1a-3dad-ae8a-f0e825eb9c1a | -2.67815 | -49.27277 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README79.md)
