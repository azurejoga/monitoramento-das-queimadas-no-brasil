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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f34a7587-9c0f-306d-990c-451076a60785 | -3.05421 | -51.04998 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b7b4b07-1edc-3b99-af9f-0e61493f04aa | -3.05359 | -51.0538 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| effcb8ee-684e-30ea-847d-4e19b7433dd8 | -3.0524 | -51.05041 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed9db149-8ae7-31e0-92f5-a7c50bb8ac9b | -3.04272 | -51.02143 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d58549-94c9-37f0-b7f7-d0d61a424542 | -3.03865 | -51.02472 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9ea4c0e-50d1-3b28-9307-f53785445a50 | -3.62875 | -50.79477 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34070bb8-dc4f-32e6-bd51-c2b98c101a2c | -3.50782 | -51.35669 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41da0166-f177-3194-93ac-158d1657803f | -3.50556 | -51.34836 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac98ff5b-ab85-3af0-bb87-680a02bb63a4 | -3.50324 | -52.0907 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22aac58d-e740-33eb-8203-cddd76adab19 | -3.48359 | -51.60015 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 134f108a-01f2-3702-a03a-e7860dca023c | -3.48005 | -51.59957 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7245197-c5af-3d76-b9cf-80fb590ee2da | -3.43009 | -51.57117 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5372dbdc-e2b9-3d54-82e1-838bddccbf5e | -3.39916 | -51.24474 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5ee119e-5e76-3742-8eee-52494f446e22 | -3.38375 | -51.38618 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 622d6df8-7d4e-397f-93e8-ed74ec144b69 | -3.24498 | -51.73485 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91ccdd1a-4da5-387a-a194-501645de5c45 | -3.23339 | -51.14506 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6f8a783-0485-3238-8bfd-58240bef4a50 | -3.23052 | -51.14061 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6e17c4-54f5-3605-86db-5ca48174ad5a | -3.22991 | -51.14449 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a8a250a-ea95-33af-abe5-4071602220e4 | -3.22906 | -51.71968 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50450dd6-fc78-371a-bcc0-d70d8cc66c4f | -3.22765 | -51.1362 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef0fe91c-735e-3e4c-b297-e1e6344b2ee4 | -3.22548 | -51.71911 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da67221c-9b81-3edc-8c80-b77e79755f27 | -3.22385 | -51.25076 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbe4cb08-00f2-3922-a657-598547fd3c4b | -3.22324 | -51.25462 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfdf6044-ae1a-3a47-97c2-47ff45dc2aa4 | -3.21913 | -51.25794 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a928b1c3-b330-3c95-9f99-8ce5b15e274b | -3.21899 | -51.35007 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6643697a-b23c-3afe-bf65-49a54f31611e | -3.21548 | -51.34951 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071810ee-9c77-3216-8238-303e18cdf08b | -3.21149 | -51.19305 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efabd8bf-0f7c-30a4-817c-cbfdb80b6b29 | -3.20286 | -51.58691 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47c2e248-4a75-3f87-bb5b-d92988dbe6fb | -3.20221 | -51.59094 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 63a3dfa5-b812-313c-ae53-3d47db166008 | -3.20155 | -51.59499 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91b06c21-3b72-338a-a783-897e873af064 | -3.19931 | -51.58635 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cecf585-a3c2-3cf7-b2f2-0adc4b59ed39 | -3.18425 | -51.36465 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8299be0c-6718-3c24-bcf1-969e5b22a2fe | -3.16663 | -51.24959 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af872228-8be9-361e-9f01-de5ac3f3ea93 | -3.16313 | -51.24907 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 701348f8-62f6-3139-8074-c8ce7e7df18f | -3.15241 | -51.15991 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39e59f35-7568-3cf1-89dc-f2ef9a41d335 | -3.10046 | -51.2754 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a42076f-7cd8-3dd3-9d4d-e91a9c79511e | -3.09695 | -51.27483 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e2fa6c-51e7-30cc-81a6-84ad8fd1888c | -3.0887 | -51.28154 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7a57c57d-e8c9-370a-870b-91a9bd95da6a | -3.08581 | -51.27708 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 838ee2e5-12d8-3a36-9eee-2bf6f09e9cfb | -3.08522 | -51.2131 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 916f7a0e-50c1-309a-aedc-64ea88e8b5c6 | -3.08519 | -51.28099 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ddf763f-f02c-3bce-923a-65c064f00f90 | -3.08398 | -51.22083 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c209536f-32a9-36c8-8dad-53493f3dd420 | -3.08168 | -51.28045 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 138b6143-d60a-37a6-b33d-1531a480d8ae | -3.0811 | -51.2164 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 584e824f-822a-33ab-8c4c-92d8b0a81bdd | -3.08033 | -51.10929 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 619f0d9c-10c6-3846-af45-b7f21aca3457 | -3.07747 | -51.10488 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6adb1d98-5195-3eb4-accd-c3a094954872 | -3.07685 | -51.10875 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e993bdf3-ce36-3182-8adf-8c055c2f9462 | -3.07591 | -51.27151 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c237d256-4662-3e2f-9647-faa480ee820e | -3.0724 | -51.27097 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c284673e-0a7a-3446-a07b-39888354676f | -3.58384 | -51.29252 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d398ec4-23e2-3072-943e-3faafb43e8a2 | -3.55934 | -51.48924 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78cb1f23-6a54-3b49-8a0e-dfe54d5826b0 | -3.54711 | -51.38647 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6492535c-9075-3b82-bdfb-0e2b7821ff5f | -3.54679 | -51.38303 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| efa5a1df-df08-3e8c-a65d-a768a08716d6 | -3.54618 | -51.38691 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 870fd12a-2f15-332d-a32b-7b86aa5614ac | -3.54422 | -51.38208 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4033008d-f4fc-3248-acf0-f48320ea2b5f | -3.5436 | -51.38595 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9a590da6-87a1-3a12-a8f9-f4550ac260dc | -3.54328 | -51.38251 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7d3cbc6a-299f-3815-a584-ca7575ef8f4e | -3.96914 | -52.13199 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edf85a46-065e-3a6f-9a12-73565af3e17d | -3.89333 | -51.90887 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7945e6b-e177-340e-99d7-d297b15bd32e | -3.86466 | -51.82167 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78cafe25-894a-3961-8e1c-dd27201bc830 | -3.86109 | -51.82109 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee97c2b0-0fec-3162-a754-665fc6091cfe | -3.84021 | -51.90558 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3033684b-f411-3ab1-808b-8b7a38e60b0a | -3.83955 | -51.90967 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c725e5bd-769a-3db9-8892-49f6993297f8 | -3.83597 | -51.90906 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cc17d60-8dec-3368-8b0e-28ca42e39ee4 | -3.79483 | -51.80832 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba3d3a0-ddf0-350e-95fb-3ae5d4dc176b | -3.79354 | -51.81644 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7bb4054-315d-30cf-ada5-37be5832bfc2 | -3.78833 | -52.06689 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaa93656-aff4-376c-a489-6cb38dd33578 | -3.78514 | -51.97272 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d20ff425-b74b-34de-8963-b45dc7f71036 | -3.77185 | -51.977 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a50a1047-fd0d-3242-a895-0567b02959ab | -3.76824 | -51.92991 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f7ef6b-5946-3c0c-9d09-0ee55b393a2d | -3.76597 | -51.82866 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df88f096-7385-3df3-ac7d-1aab5653e670 | -3.75784 | -51.81074 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e655421b-5eb4-3944-8215-406f41f2c175 | -3.72051 | -51.63536 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46df3210-e01c-3274-824c-864a68c1b10f | -3.69315 | -52.00696 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 179cbb21-e5af-3e39-a72a-cc62d654a730 | -3.69248 | -52.0111 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce12661-bd0a-3dad-8f3f-90f8dd9f0d56 | -3.68888 | -52.01049 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f98bc2f6-8c00-33b6-af84-e42f93b59dfe | -3.67736 | -51.84065 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 443808a5-7421-383f-a37a-e2c2018b6eab | -3.67671 | -51.84473 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8f02115-fae0-3292-8b90-1e5ca629cb7b | -3.63869 | -51.78429 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3067d58-91f9-362b-9531-a1943da7f22b | -3.95084 | -51.23757 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e246968-ad96-302e-99ec-d7d7afbced9d | -3.89104 | -51.90937 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d1d5cef-498b-3e3b-9318-422e1e34609a | -3.87386 | -51.1954 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 634cdb5c-0c4a-3fc8-9df4-d6c54c429ac1 | -3.86868 | -51.41468 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1222dccd-ddc7-313c-b591-e311b1dd8c0e | -3.86453 | -52.19855 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc430eef-da40-3f83-a0d4-67eeb292c604 | -3.83651 | -51.29571 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0ea64f6-45a1-35f8-815f-41251ca00c1b | -3.80903 | -51.13424 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0eb7c55-2d80-3f99-a8fc-a051022b2e2b | -3.79194 | -52.06749 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfc892b4-b8fa-3f64-a977-c89fc0cfe6b7 | -3.79126 | -51.80775 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37f39eaa-85fb-3fb6-980c-75c52c681019 | -3.78997 | -51.81586 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e96bf2a-7358-382d-b4b3-7560ac6f6c46 | -3.77545 | -51.97758 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0dbd0281-7fc7-3372-85b5-1d7b1b3759d9 | -3.72519 | -51.33412 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d395217f-e6ef-3355-bfef-7eb3c099c143 | -3.71472 | -51.78306 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bff33cb-945e-3d5f-9ce2-521e3c383841 | -3.68128 | -51.0839 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d18b45ab-a503-38f6-bb45-565f4f943bf2 | -3.6803 | -51.84528 | 2024-10-21 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cba0f619-86b1-3127-a9e9-4f0bb68998a2 | -4.43529 | -50.92707 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 234326ba-6781-39a1-8adc-81caad7c6ace | -4.43187 | -50.92651 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c91fdbd-5885-39ca-a59f-896e13a84d97 | -4.42326 | -50.93657 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14cc5328-f42e-36bd-8e1f-693a259cf8bc | -4.41984 | -50.93601 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4e93c32-fb35-3f6d-ad9a-a37e1425e1ad | -4.28887 | -51.05334 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da8f9fde-9948-38d6-bf08-3ac617b38e39 | -4.28543 | -51.05278 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README43.md)
