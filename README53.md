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
| 1546c8ee-ad0c-3e6d-a783-72806d35e1ab | -2.88724 | -48.7365 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 406a7bca-c49d-3678-85e2-0321e4b3fe71 | -4.14561 | -48.25246 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19004cc9-0a66-3589-aab4-b3cf17aacbee | -4.12523 | -43.57857 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f0474aec-4562-3dbb-9e66-7a9ef836ee7f | -3.23508 | -53.40028 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 285ea0ec-69ae-3fa4-a608-ff2f21fee538 | -3.53454 | -47.38431 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c874e348-b0bc-38e5-8832-c4ed2bc0accc | -4.12955 | -43.58826 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0d96a74d-bd7b-3fd8-8735-9275873b215f | -2.71887 | -48.72805 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50bed3ac-23d7-3e7b-9ac7-47ace674ff27 | -2.34744 | -48.9511 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b2a45e5-664d-37f9-8179-10296ce0fd09 | -2.19119 | -48.32171 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20e1d07e-ba04-37a3-8433-fed11c64c4e3 | -2.75488 | -53.21253 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 188231cf-7701-363e-b9a4-2d189c8d8d78 | -3.2483 | -50.0208 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b74a3345-502b-3243-a44f-a0acbcb20b8a | -4.26947 | -50.71839 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 060cfe2c-b1e9-35f9-9084-6937571ef9fa | -2.5095 | -46.36587 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d76a57-9768-38ce-8df8-cec6bce2ef9c | -3.69526 | -49.82018 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb772142-a701-3ce3-9fb4-88cb767f3cce | -3.27355 | -50.2959 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b7efbc-f19b-3b2e-9e85-1d88f7643731 | -2.85473 | -49.26734 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42d48c58-b8a4-3ea8-971a-ab9c8196bd12 | -2.64646 | -48.56206 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d604c6d-d715-3271-a51a-0fbd4b332a56 | -3.81632 | -51.87824 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2499913-ba36-3cbf-a556-bdd17ca9411a | -3.17589 | -51.25941 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cd47897-6068-3df8-a87a-005378ff46cc | -2.92169 | -49.12222 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 197a0fc1-4354-38cc-9b4f-d3b12ce1673d | -2.60983 | -49.20449 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5620216-e0a8-3537-ba14-5ecfd611971d | -3.48051 | -51.55098 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4038b523-75f4-3d97-964b-e1f11c346033 | -2.91542 | -48.60028 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5922ac7-701a-3562-9f88-a59281a6922f | -3.29187 | -50.02765 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebefe35-f8ce-37f9-b4a6-63af2d87915e | -2.8621 | -51.66188 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2933e3d-07dc-3d31-8e38-69dfc1dba2b8 | -3.60985 | -51.3767 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe44ffe-bc7a-30dc-939e-a789ef897f25 | -3.24495 | -50.02028 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d31e77e7-e0b8-3310-91c4-acce88c222e6 | -2.77283 | -54.72666 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d78ebe5e-8ec8-3bd1-a3d7-72a5b36084fe | -2.97422 | -50.30138 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f247a6e0-973b-3234-90bd-44763d57a390 | -3.01656 | -53.23379 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdd46e11-2eb6-38c8-b437-7ed05ba97dd6 | -2.89891 | -48.59772 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72d9dd69-08bf-3a93-a8e4-80819553480d | -3.85071 | -47.06826 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8992823-6c9a-342b-8e7b-493d15b1b05c | -2.81075 | -51.34523 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1041cd12-9a42-3909-9ec3-abe9c5d5482b | -2.84402 | -51.77689 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 81681523-0d33-3b13-b253-7ccc8ee43b46 | -2.93631 | -54.11933 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a48a92e-ae0f-3a53-b74f-e444a5242540 | -3.10836 | -50.25869 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 222af29e-0b14-3d7c-8d89-96002659cba7 | -2.28482 | -50.67069 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d7a5eb-b56a-31d2-9fac-732c2147941b | -4.78586 | -48.91533 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b2b4af-59a4-3c34-91a1-d7e3ad720753 | -4.13856 | -46.83853 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81fc53e2-ac50-30f2-a90a-f96779884041 | -2.85373 | -51.77214 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 5616511c-5be1-365f-ae44-9869336895e9 | -3.15753 | -51.05193 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e28f206f-2507-3a9d-87d7-2ee3256d2bc7 | -2.07747 | -53.98957 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d24eeca-b071-3b2d-9148-45dbc03765b5 | -3.14043 | -49.13565 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a523b6b0-019c-3adf-9acd-0f491718f9ab | -1.39194 | -52.19379 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd585dcb-35d5-3ef9-8b6c-844725ac1de5 | -2.44367 | -49.60984 | 2024-11-06 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c5c5030-c246-3e16-a2e6-b5898708f36c | -2.6638 | -46.74386 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 621f4d88-f06a-3d8d-9258-2b5b87dfbd24 | -2.85666 | -51.77681 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 59d12e46-920e-37ac-8146-1797f3aa09ba | -3.06633 | -47.76758 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ceea7ac7-c898-3575-b9e7-a68c03563797 | -2.87005 | -49.49361 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb038da9-db95-387a-8923-958ffefa2735 | -2.63373 | -51.7332 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc5f42b2-56b7-3cd1-bf04-c2633b379fc9 | -2.52192 | -49.13763 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7168d700-f3f8-3bef-b80f-477e58ad266a | -3.67822 | -50.16072 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59dc59bd-42e7-3d85-a2b7-17b0cc1031e8 | -2.94728 | -48.63698 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b88a6364-4f17-3bc4-8275-bf0a1256674d | -4.60338 | -48.69245 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 239974cc-dd7a-3bb5-8a6c-dc6c8cbc50a9 | -3.23589 | -53.39515 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf7dfc4c-5ff8-3536-8feb-8f567140273d | -2.84437 | -51.79814 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc02112f-85c7-3acc-be1a-ab0d7ce21b55 | -3.97627 | -48.14083 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c010e7a8-c95b-344c-b8a4-135855d289eb | -2.28345 | -46.71257 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbfd0115-332b-3afe-b68f-5a9eb51621f2 | -2.83716 | -51.79702 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83a67886-9cab-34f8-a947-8455372e1653 | -3.04155 | -51.26292 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a33e8586-21d3-3879-9a00-532cfe473d3c | -3.48348 | -51.60044 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7566be7b-dd0b-36db-813b-de43b2becbfe | -0.68264 | -51.66831 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd07445-22d9-3f03-895e-62f5de632c86 | -2.64923 | -48.56601 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33110fc2-80a3-325c-b8f5-6a88d35e38f7 | -6.50376 | -44.67701 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 865f288a-5fb1-3122-86d6-c2e06ca14ee8 | -5.84269 | -46.27505 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0271b1b-d750-355c-a97b-21c49dc777a1 | -6.49007 | -39.97281 | 2024-11-06 04:38:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1802ff0-59fe-3a83-bdd4-7212dc49cffc | -5.23287 | -48.14165 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d1522f8-94c8-350e-859d-6a8a5f06395d | -6.49945 | -47.49826 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aedff7c2-4db6-3b28-ac29-4308fc6ac288 | -5.23342 | -48.13813 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 115e5d22-238c-38b4-89fb-d2b7798a2f1b | -6.27345 | -47.21503 | 2024-11-06 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4dba757-e6bf-39b9-a08f-79f1df3c22ba | -6.13185 | -43.97866 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9afda441-42c0-3812-a3da-1ebed805402e | -7.49781 | -43.84333 | 2024-11-06 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bbc058d-209c-3eab-a8ad-8814b024ffff | -12.8687 | -41.76493 | 2024-11-06 04:38:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dca2db7e-9a10-3417-be2a-f9d0fb77e30a | -3.5914 | -58.60007 | 2024-11-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14107c98-363d-3bd4-bd1e-94f176a84887 | -6.66183 | -47.28341 | 2024-11-06 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c36a4a1e-0950-3a26-871b-c59e22dfb929 | -6.93486 | -47.78712 | 2024-11-06 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af90ccbd-fc81-33d9-8598-2510a3dc39a3 | -6.5117 | -44.67822 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 35069647-731a-3802-b598-03f74664ac56 | -4.40971 | -59.53118 | 2024-11-06 04:38:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3c076c-4b91-3e32-a3b0-ee3bd9c9e201 | -6.51293 | -44.13526 | 2024-11-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdbbcefa-a26f-3f84-b701-dd58d5462692 | -6.45739 | -43.57686 | 2024-11-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37954144-7137-37f6-87cd-90e19a5b169b | -5.15812 | -49.6375 | 2024-11-06 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e113e8e-3ba8-318b-8ced-588d42116443 | -6.50059 | -47.49076 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50c4e099-1298-3c53-90a1-bce762d6959b | -6.10566 | -43.96711 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 486a5bf0-4e51-33c5-854f-6249e8466671 | -5.94069 | -43.77689 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb52351f-ca9c-32f5-b04d-050e47df91a3 | -12.8732 | -41.76469 | 2024-11-06 04:38:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 953f5ae3-abac-32ed-b40a-7eae42175d6f | -6.9925 | -48.66272 | 2024-11-06 04:38:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b46235e-1363-370f-b30a-39c0cdcb862b | -6.12498 | -48.06121 | 2024-11-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6cfd0ee-9d29-3aaf-b580-96203fb2f1e8 | -4.40899 | -59.53535 | 2024-11-06 04:38:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d29b766-b4e3-32ca-b64a-ea49f9cb57b9 | -6.51645 | -41.42292 | 2024-11-06 04:38:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01c06c33-365d-3964-862d-f41254169f57 | -6.65921 | -47.87341 | 2024-11-06 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d894728d-f9a3-33b6-b870-981fa8e10cbb | -5.19035 | -48.2394 | 2024-11-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c7dee01-67f6-30ad-9ed4-72e5b07f43d8 | -5.93597 | -43.7801 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 822c8b6e-0721-3025-92fe-c4a056c4f94c | -6.3674 | -47.9215 | 2024-11-06 04:38:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f110247-2a35-30d0-b5b6-82a4f4352e24 | -12.87401 | -41.76558 | 2024-11-06 04:38:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e998cd82-d0e0-31b4-8cb5-47bcfadb2b70 | -6.49487 | -47.48226 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 20c97b2f-0319-30bf-a906-fbf4177a20fe | -7.15005 | -48.32411 | 2024-11-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d8c009d-9b89-357d-b06e-fbd368af6459 | -5.93453 | -43.7802 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9468df05-1d0b-3e80-8832-00bef874d302 | -6.48638 | -44.68494 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0c215020-7cc6-3df8-9394-8e3d8deb6176 | -7.37474 | -43.50792 | 2024-11-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c22c30-18bd-3a1c-944d-fe98c4e87215 | -6.10925 | -43.97142 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |


[Clique aqui para ver as próximas entradas](README54.md)
