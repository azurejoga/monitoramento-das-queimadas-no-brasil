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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a314992e-eeed-3ae8-8939-6f220c28ed94 | 2.61859 | -50.88009 | 2024-10-23 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ed75bbf-96b4-3a7b-b19b-8d017afc1a40 | 2.61794 | -50.87604 | 2024-10-23 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 39587592-2c02-3763-b15b-f84eb237bdfd | 2.61063 | -50.88553 | 2024-10-23 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b67b0e8-cfca-39ab-9dea-a4e65447c9e5 | 0.98623 | -51.14621 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 918d7d9c-ded0-3f6d-aa31-6ca9f61c63b9 | 0.98557 | -51.14207 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0df4a83-55ee-3552-9505-093a6c599e8a | 0.9819 | -51.1469 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be2cda45-b2dc-3a36-bf97-2889719567a7 | 0.97824 | -51.15175 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42255b2d-05cd-3701-8684-9180e7cdac68 | 0.97457 | -51.15655 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22540579-cbc0-3c2d-950b-489f806fd103 | 0.9739 | -51.15242 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79f6a8bc-126f-3472-ab71-533365c83123 | 0.97024 | -51.15721 | 2024-10-23 05:14:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c9dab83-d207-36d5-b147-193f7755d09d | -2.20537 | -50.87022 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d899d097-ddb7-34d2-baa7-f36733087dfc | -2.20192 | -50.87284 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eeed6fef-e2b4-303e-b85d-a4ed9fe25ba1 | -1.84712 | -50.65293 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 989da484-2469-39e5-b9f3-f2f401101d51 | -3.45808 | -51.20252 | 2024-10-23 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c78c3c99-5951-3956-9b42-88782518df48 | -3.45444 | -51.20369 | 2024-10-23 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03afb66c-a7a2-3862-8ca0-c26717cc69ce | -2.4788 | -50.47486 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7662e99-1055-33ec-9262-636108384718 | -2.47306 | -51.97728 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86a4bb52-46f9-32da-a257-d2f7977ed4b3 | -2.47128 | -51.97132 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0093d6d-1688-37a0-a7e6-bfbab0d2e4b4 | -2.47068 | -51.97538 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e02bdd8-3c37-3bb7-b2b0-77a2bc663083 | -2.47002 | -51.9685 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e6181cf-9d67-3bda-9e60-384b29b48a09 | -2.46938 | -51.97259 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a27cf567-1078-3a00-af69-6fad2d7b7693 | -2.46874 | -51.97665 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 011eb6d0-9be4-3733-b7fc-b54e6da5118a | -2.46696 | -51.97066 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b30dc0b5-bf93-31f6-ab40-feba3d76846d | -2.46569 | -51.96784 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 801664ed-c2fb-3e6b-a88d-d63bafd5dfdb | -2.46505 | -51.97194 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be3ab1a8-e736-3df6-80e8-668df041cbd3 | -2.4141 | -50.48093 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01929a33-77c0-3642-a4f8-53f80ea559da | -2.40931 | -50.48018 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a114748b-ba03-33b2-9f64-20122886107d | -2.28023 | -50.46457 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9487ab-a00a-35ac-a8c9-a44431cf34fb | -2.2798 | -50.46834 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 366315f1-78b0-385d-ba56-b8a41734c3be | -2.23225 | -51.8844 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fee762ff-023b-3675-9738-d272644d1b99 | -2.22791 | -51.88374 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd259ae8-2317-332d-80f9-24cda2425b4e | -3.21006 | -50.79825 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3418287a-e20a-3c24-bf6d-27ce768e1250 | -3.20532 | -50.79751 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22864efb-9ee5-395e-9ac4-f307dd1dbd73 | -2.80097 | -51.59815 | 2024-10-23 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 982d6d51-b1ab-39ab-85fb-de6cfb31bf9d | -2.7993 | -51.36533 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a44303-d743-36dc-9a44-61f27b37d47a | -2.79544 | -51.36008 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf984fa2-c28d-3152-8a65-2f81d69b2f4c | -2.79477 | -51.36463 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46762a8-1a0c-33aa-9c2a-007a8683dee8 | -2.79409 | -51.36916 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26157c55-8ae4-3d8e-99eb-5aa0f14d68cf | -2.79024 | -51.36393 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 578bdcbf-0714-30c8-a62c-93373e67edf1 | -2.78957 | -51.36843 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650426fc-ad86-3bfb-af2b-c372d61339b2 | -2.6082 | -51.77552 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c5993a-fccb-3699-9371-2d65f943ed7f | -2.60792 | -51.77345 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b98ce39e-a6e8-3ced-8154-bed6b55012a7 | -2.60446 | -51.77067 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12180d2d-c385-3fc8-8344-9bfefdbbfecf | -2.60381 | -51.77487 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff675290-1fdb-30e2-af9c-38bf7ee5868e | -2.60352 | -51.7728 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc3825e6-48f7-3210-966c-5502483666fd | -2.60315 | -51.77908 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8249f4f0-ca38-3185-8b61-0adb5cbf4fcc | -2.6029 | -51.777 | 2024-10-23 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44052042-9383-3e40-a098-cc84fa3c494f | -2.58535 | -51.9216 | 2024-10-23 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf332855-409b-3dc4-b981-b0b3c9d6e03a | -2.58101 | -51.92091 | 2024-10-23 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88e11c5d-9bac-3605-9491-4d6b76353cc5 | 3.48437 | -51.26716 | 2024-10-23 05:14:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70cc21a5-3478-3ea0-b880-226abc158b82 | 3.48375 | -51.26345 | 2024-10-23 05:14:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd7fe90-d2ac-36ee-9eb0-2728b9d43cdb | 2.56302 | -50.91813 | 2024-10-23 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a532e44-100e-35f9-97c0-831fb5b7f4e7 | 1.00878 | -52.21821 | 2024-10-23 05:14:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec9bc5ef-a5a1-3c49-b953-96dd5fffb494 | 0.50236 | -51.67759 | 2024-10-23 05:14:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c802027-cc8b-36c1-a741-8ea5b264b4aa | -0.12436 | -51.64219 | 2024-10-23 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d39b209-1259-3176-bcfe-bd8794b8a058 | -0.12372 | -51.64616 | 2024-10-23 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e99ac4db-b245-379c-8af9-11ecb54276c4 | -0.1201 | -51.64147 | 2024-10-23 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03dc21d2-14ab-3938-8ab7-866ea25c4caa | -0.11947 | -51.64544 | 2024-10-23 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64e2b259-71f2-3646-b699-a80055410543 | -2.04339 | -52.6981 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75c6ac27-4131-33eb-819e-01293de5a3ae | -2.00492 | -53.29816 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96dba53f-e498-31dd-9535-8ca25d2194b1 | -1.93143 | -52.7002 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b5652c-f332-38c0-953b-857c0172f781 | -1.46642 | -52.81097 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd793079-1b3c-3ac6-9cb5-2998faee63a0 | -1.55776 | -52.26646 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9dd163c-5bd8-31e0-a5db-9221a49157d0 | -1.55657 | -52.26716 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f2bfade-9de6-32c6-ae03-b67706c633d2 | -1.5536 | -52.20444 | 2024-10-23 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 422917ff-0afc-33a1-828f-161fa24192bc | -1.5524 | -52.26651 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5865497d-1dc1-34ee-b232-bcc46c247287 | -1.5494 | -52.20381 | 2024-10-23 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112d76b6-d118-32b9-a1d1-0bd964ab9c0b | -3.1101 | -54.1661 | 2024-10-23 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 4d4e482b-affe-3316-9002-a287669c281e | -3.1102 | -54.146 | 2024-10-23 05:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ee4e201a-cc96-326e-9672-ea1c77892da4 | -4.1305 | -45.5888 | 2024-10-23 05:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8370aab1-8eeb-3a85-baa3-56b66a911e64 | -4.1719 | -47.9894 | 2024-10-23 05:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 86f8cfe8-97e1-3867-9186-2f579703593c | -4.1905 | -47.9885 | 2024-10-23 05:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| dd2e788b-59b3-33de-9c33-939bdea6516f | -4.00277 | -53.79377 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c730293e-48d3-372b-a7b8-cf65752fc651 | -3.92623 | -53.66725 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 740c1a54-7ca1-3799-ad00-e18168115885 | -3.92489 | -53.66969 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d43b28e-3a70-3017-93c3-90d0e58a6414 | -3.76789 | -53.38479 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b20e15-91c0-39b9-8fb8-9bc605fd107e | -3.65916 | -53.63349 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f366bcff-c986-3484-b595-83a22d5aa891 | -3.56509 | -53.75529 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a8c4400-edd7-3e66-b5cb-008d5a881542 | -3.56118 | -53.75469 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fec6ba91-1666-3744-a1a0-3271d6f6b536 | -3.56043 | -53.75959 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49ba4c45-42d0-363c-af7f-ccee72797fd9 | -3.8784 | -52.32227 | 2024-10-23 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9ce725f0-b064-3fd0-9e0f-d60e6c90495f | -3.79224 | -52.38538 | 2024-10-23 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d2ff5f-cb78-3b9c-a190-0a32053ef222 | -3.79164 | -52.3893 | 2024-10-23 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec1a81d1-2a29-35da-9a00-416738c35008 | -3.78797 | -52.38465 | 2024-10-23 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c30f9a0-fec6-3173-a930-bdef4d33e026 | -3.78736 | -52.38863 | 2024-10-23 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a914c680-a42e-36e5-aa28-ae6caccb671e | -10.76401 | -54.10142 | 2024-10-23 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c55d229b-e7cb-30fa-acc6-b6841965b917 | -10.76382 | -54.22909 | 2024-10-23 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd0ee607-3ce7-3ec6-b62c-7ad11753d59e | -10.8236 | -55.06924 | 2024-10-23 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8211a03-a8ac-38fc-906b-53b924eb1e03 | -3.65565 | -54.21555 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6031042-5ec5-36aa-959f-def0f636e86f | -3.65184 | -54.21502 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae667eb-8aa3-34ac-96eb-eef5cce3ea1f | -3.65114 | -54.21969 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee93b687-eae5-377d-b991-bf4258c27694 | -3.64802 | -54.2146 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cce0591-0cc7-399e-82d2-5e798bc46077 | -3.63569 | -53.97052 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd1acff8-0ba7-31a1-8506-d1817ca6ec1d | -3.63256 | -53.96518 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee8f7ca-f2d6-3d6c-8719-cce36baf7a03 | -3.63185 | -53.96986 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b98c64a8-18fd-3a32-9ddf-c1dae7b41b6b | -3.59254 | -53.78436 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3566800c-d7b4-317d-b58e-6835717b3a89 | -3.59216 | -53.7861 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb73453-2897-3936-8093-4bb577d274ae | -3.58899 | -53.78059 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ef62220-b09f-3244-8f54-0a2517da3ab4 | -3.58866 | -53.78364 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b659adac-2622-3297-af1f-ccc452af16e1 | -3.58827 | -53.78537 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
