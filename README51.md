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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efbdbe42-2e30-3342-a131-8a57e58f4843 | -1.54515 | -55.34934 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fea5a49-4238-335f-a51d-127c4587bda8 | -1.54225 | -55.34494 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193978cc-daed-3bce-86dc-eb78e9959efc | -1.54165 | -55.3488 | 2024-10-23 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f9f5ba-94d0-3c76-86f5-a9d984de0bf3 | -2.21209 | -55.05113 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0a7f8d14-5122-3f4e-9036-5dcc9b198a08 | -2.21095 | -55.04974 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fae2dd82-0a41-37ff-9139-5c21a55b1474 | -2.21033 | -55.05377 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a05f7f4e-86ef-30e2-aa92-fb8bce2539b8 | -2.20852 | -55.05058 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e0525a12-a023-3a03-b0dc-ecc3573f3e94 | -2.20738 | -55.04919 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 67d43b1d-d98b-3a4a-abbb-2107ec66d012 | -2.10627 | -56.58736 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2073967-3503-3f53-84fa-283b6db89252 | -2.10572 | -56.59092 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64d50a92-d4f3-3653-8269-b6602401b62a | -2.1029 | -56.58684 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df429ff1-00a9-3626-8ffb-a1865e042c95 | -1.98736 | -56.56878 | 2024-10-23 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4db9aca-28b0-31ea-9ca4-b4f4ee9464c0 | -0.87784 | -57.64833 | 2024-10-23 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 967c221c-6cbe-3b3d-acad-98336c20f495 | -1.11531 | -58.07408 | 2024-10-23 05:14:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e30e34d9-4ee4-34c0-8dbd-d66b9ba3b247 | 1.06245 | -59.63734 | 2024-10-23 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6d15c5d-1960-3820-bbb1-b8bde12ab2ff | 1.06184 | -59.63345 | 2024-10-23 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8851446-7761-34ba-9bec-561dfd6025f7 | 0.75465 | -59.65136 | 2024-10-23 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d71c5a-9850-3255-b9fc-ff93034c89ba | -3.40113 | -44.15284 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca538f46-f5ec-3aa1-aa39-4e201f7ca92e | -3.40004 | -44.16027 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96a6f6f9-1bac-358c-be90-631ba915ce4b | -3.30462 | -44.14883 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a4619df-6087-30a9-80b6-115642a6be56 | -3.30441 | -44.1539 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7f21deaf-a53c-376b-9850-b0a748e47605 | -3.30352 | -44.15624 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e987a2d-f87f-3d55-899d-29ecc0d09df3 | -3.29819 | -44.14542 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 279764ba-fd11-3fec-a8c0-0d2c2e352751 | -3.29734 | -44.14783 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1809089-ed64-33c9-8b57-bf128533b1e8 | -3.29713 | -44.15286 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c1992cc-6d25-3ee3-b97b-0efd60374f7e | -3.29626 | -44.15516 | 2024-10-23 05:14:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c81448c7-73cd-3893-b700-36d03c1e212c | -4.67215 | -44.60067 | 2024-10-23 05:14:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 908c1618-aeed-3d7e-b7c9-48a75563f3a4 | -4.6711 | -44.60816 | 2024-10-23 05:14:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f21a3ea3-8d4d-3c04-a828-1d64668479f3 | -4.13936 | -45.58639 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ed5294a-799c-3c18-a74e-3c1f8742e270 | -4.13762 | -45.59839 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d64d4702-a529-32c8-ac6b-dbc2b062a100 | -4.13485 | -45.57905 | 2024-10-23 05:14:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dd0e276-c631-37ed-a4c6-23bdf969cf0e | -4.13433 | -45.57344 | 2024-10-23 05:14:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f3f7426-8918-3da5-8320-d64864936766 | -4.13403 | -45.58499 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 43db89ec-4d71-386a-8612-1e35d5cacbc4 | -4.13346 | -45.57946 | 2024-10-23 05:14:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f33c09be-215c-3020-841b-23b9d7e8ec42 | -4.13321 | -45.59096 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05d00c26-8106-3b20-91c7-94e749b77bab | -4.13261 | -45.58536 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24410fc3-1d8c-3d42-80cc-6686e51e6aa3 | -4.13238 | -45.59696 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7af860a7-1867-302e-a463-60beff3da814 | -4.13175 | -45.59129 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d0d6360-a651-3b45-9b4d-a9d20ea0282e | -4.13089 | -45.59725 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 82c2b9de-b866-3423-8ec2-858a6bf95294 | -4.1267 | -45.57845 | 2024-10-23 05:14:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8fd0c556-fc08-3fec-9c4b-b2c40e39292b | -4.12584 | -45.5844 | 2024-10-23 05:14:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cefa59fa-10f6-3479-bcde-86d05666ae24 | -4.12499 | -45.59034 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4f10b76-28cd-367d-add7-dee1fa0ce3bc | -4.12413 | -45.5963 | 2024-10-23 05:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56504111-bbdc-3e5e-a432-226bac782acd | -2.03904 | -46.97184 | 2024-10-23 05:14:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d89f110-2bdd-3e17-96aa-64fe19895061 | -2.0384 | -46.97624 | 2024-10-23 05:14:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 81e1adaa-aff5-3866-9dc2-4d5bf4061e76 | -2.03828 | -46.97031 | 2024-10-23 05:14:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e31f4371-9215-32a5-9ef3-6e81f9dfbfd8 | -2.0376 | -46.9747 | 2024-10-23 05:14:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1591a573-72fc-3ca5-a906-f073eb077935 | -3.31164 | -47.19106 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 08cd5d59-6cf5-318a-a922-9c4a2b649c5b | -3.31132 | -47.18955 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e77cb7e-ce8f-3193-a42c-1ea72686b1cb | -3.31062 | -47.19414 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5152a9b0-5ff3-3e59-a598-e80320f354d9 | -3.30558 | -47.19016 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2969a3c3-08a3-300d-90b3-5418eaa046dd | -3.30526 | -47.18866 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daed0587-1a1c-3647-8463-df321070ff8d | -3.30456 | -47.19327 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e661153-810f-3a14-bce3-dd10a2159304 | -2.33041 | -46.24147 | 2024-10-23 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 280fb84c-014b-32ab-948f-0779f08547c3 | -2.32407 | -46.24051 | 2024-10-23 05:14:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 630c295a-9e10-39e8-ad58-122068a6ef05 | -4.25943 | -46.53532 | 2024-10-23 05:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 412f3309-ef5a-30cd-adab-be10cf94c6a6 | -4.25873 | -46.54031 | 2024-10-23 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0485b26-1cf4-3ae0-b450-9a6368a59961 | -4.25784 | -46.53956 | 2024-10-23 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a15cb85c-6b1f-3def-a736-d201b99c1daa | -3.98454 | -46.47009 | 2024-10-23 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a31a64-187b-3efe-8099-ca1f4c1b990f | -3.97801 | -46.47008 | 2024-10-23 05:14:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 386486a3-951f-3fa3-a16a-15152fd05419 | -2.14149 | -47.91761 | 2024-10-23 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffd25748-a6ec-3804-bf4c-75fdba1fc90a | -2.14091 | -47.92148 | 2024-10-23 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8f061cc-6cf2-3587-b040-c8190b9c3ea6 | -2.13583 | -47.91661 | 2024-10-23 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb424380-d638-3f1d-85d8-59e732b60915 | -2.13525 | -47.92052 | 2024-10-23 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d028e18-6aa9-30ea-9f8d-e32c68484a65 | -2.13401 | -47.91791 | 2024-10-23 05:14:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05f30b5f-d5b9-3fb5-a1f5-8eac78ed7455 | -1.97563 | -48.68276 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99287734-391c-3511-ba09-4bcbc078908c | -1.9751 | -48.68618 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f91c61-338f-3c07-82c4-c66164cdcaa5 | -1.97458 | -48.68955 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e51c80-4b8a-35a3-8d56-773cbd29920e | -1.27423 | -48.04833 | 2024-10-23 05:14:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 709145ea-a99b-3086-b067-b6ce8c44a240 | -1.27368 | -48.05198 | 2024-10-23 05:14:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18778bf4-0c10-394a-8898-2d940a244e57 | -3.46081 | -47.66958 | 2024-10-23 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10be2890-f2c5-3af3-af9d-45e28cad3622 | -3.33878 | -49.01269 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72585caf-23af-38a4-9798-96e35ad14b68 | -3.33607 | -49.01256 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 350f8ba4-356d-399f-be27-6b780df72887 | -3.3334 | -49.0119 | 2024-10-23 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aafbe753-6cb0-3ed2-8d04-947845642d5d | -3.14033 | -48.74758 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6f2097-d042-350b-af68-4085fb3c2b16 | -3.1026 | -48.66294 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a68e8526-3116-367e-98ac-5b2ebb65d48a | -3.10207 | -48.6665 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 625b7881-49b8-3359-9ae9-33acd9ea14e7 | -2.96907 | -48.00272 | 2024-10-23 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4192ff-7a98-32d0-95d1-b29873996b11 | -2.96849 | -48.00666 | 2024-10-23 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52e9fcb5-a662-39fb-a3e2-0e9d61577cbc | -2.96761 | -48.00624 | 2024-10-23 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba5aafc8-6fb9-3bc2-9437-68822dc1610b | -2.96278 | -48.00577 | 2024-10-23 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b83fa14-a9c6-37a3-a12b-e3edb0d24c08 | -2.9619 | -48.00537 | 2024-10-23 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db1b100c-8d2e-3904-96f8-216c1ae1e76b | -2.92253 | -48.95695 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14e580d8-d704-35ca-a5a3-e05c4dac2a3a | -2.92201 | -48.9603 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a0da467-8e90-30b1-a2db-6d9ba6fcd1c6 | -2.79116 | -48.56952 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6680bc55-c698-3589-a387-48c5ac4d21ba | -2.79064 | -48.57309 | 2024-10-23 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a89a8de7-fa95-30c7-963b-5b0f1501cceb | -2.65474 | -48.12746 | 2024-10-23 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcda788f-392f-35e6-a480-838eb117e69a | -4.18889 | -47.94762 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27e1bec0-5ffd-3448-a41f-125883b22e67 | -4.18827 | -47.95195 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac0dc1a9-d3eb-33ff-bcc8-8fcbcdeffada | -4.18405 | -47.98111 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc971768-f4ee-31df-b9f5-f3785ccb8509 | -4.18345 | -47.98523 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8c834dee-96f0-3def-937d-017477036868 | -4.18286 | -47.98931 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9a0bdd65-2fed-3984-9078-3fdc4712f958 | -4.18228 | -47.99336 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9ca68abe-64ec-3442-a332-ce44b8d7f40d | -4.17882 | -47.97606 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15243fe8-0e19-3d89-8fa7-e6a00f52835b | -4.17823 | -47.98015 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a3f1f35-a520-3c89-97ed-5732d0d73037 | -4.17765 | -47.98424 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c9f9d66d-daa8-3db4-9953-0e7cf9c3fc4a | -4.17706 | -47.98831 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| eae8a407-a115-3993-924b-86ecd3fdc94c | -4.17647 | -47.99241 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 02f33a5b-7df8-302b-8fcd-a3abed7b2515 | -4.04793 | -48.10267 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcf4998f-9454-3092-9b89-9cf1fbacf3eb | -4.04732 | -48.10687 | 2024-10-23 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README52.md)
