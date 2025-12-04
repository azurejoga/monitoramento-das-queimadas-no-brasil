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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b119876c-4add-36ec-bcad-a694baf70944 | -1.99982 | -45.33083 | 2025-12-04 00:34:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e5bcf655-7454-37bd-bff4-80b251ac3bd4 | -4.05476 | -50.52606 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 163b0ba8-51d1-381a-9d7d-48ed9a2b226b | -4.40198 | -45.40032 | 2025-12-04 00:34:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59614d78-f313-34c8-9bb3-991edee87787 | -2.21283 | -46.22069 | 2025-12-04 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ef1acef6-9c14-36a4-a16a-eb5753a970e0 | -1.28803 | -53.17681 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d07015b3-6391-3671-9878-39dfdec19678 | -2.36664 | -47.69406 | 2025-12-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0d68daa7-4149-33b6-827a-f03f55dae400 | -3.07356 | -50.43321 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b5673a88-6a7e-3b06-949d-f8aab32bc6db | -4.52594 | -46.47897 | 2025-12-04 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 58abaa55-303a-31bf-86bb-a3ab2b735be5 | -4.09597 | -45.73539 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7d4b3746-c955-3ae0-8803-fd9290b12952 | -4.41013 | -43.13652 | 2025-12-04 00:34:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 88c324e6-e2ed-3750-888f-28eed509709b | -2.77726 | -52.95049 | 2025-12-04 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c4542ce3-0074-3305-8c70-a0c93efb55a9 | -2.04482 | -50.7811 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d257b4f1-7b40-334f-9f63-2bc03992d023 | -2.57438 | -49.09628 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5d80cf6c-eac2-3349-8114-e1e0c7366b8e | -2.42129 | -48.59048 | 2025-12-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 315d934b-2559-3c80-ab7b-8c3d5aac8644 | -3.93276 | -47.20733 | 2025-12-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fd556056-23bc-39b2-97c7-9d170b298992 | -4.5032 | -45.76315 | 2025-12-04 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1ca25adb-b901-3103-a7c4-82d749eae47b | -3.68747 | -50.66524 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 58f9c664-f242-3024-aff2-20dcebcc9b7e | -3.51361 | -47.19702 | 2025-12-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| feb3e887-ce1b-3d72-bb72-79023d27f015 | 2.52535 | -50.85135 | 2025-12-04 00:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d6d3b99a-8f3b-3e9d-94bf-c4fbf55bafeb | -3.57146 | -47.18234 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9ad4d2ae-d6b6-3fa2-b018-6bccf92565f2 | -3.638 | -54.81115 | 2025-12-04 00:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fb921a04-c011-3820-ba86-d3684f35b2b2 | -4.48792 | -45.27786 | 2025-12-04 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c81d947b-b673-3dd1-b774-7a3fb07d2e4b | -3.93458 | -43.14264 | 2025-12-04 00:34:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 92d93776-4501-377c-8713-cde6bbd68735 | -4.0259 | -47.34384 | 2025-12-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2ff23bf1-7dfd-3655-923e-7b3425ac1ec6 | -4.20588 | -44.26639 | 2025-12-04 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff46023b-ad02-3e17-8254-8e28ed035aa8 | -3.00435 | -45.43941 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7880d349-2b2a-3380-8b9c-14d197f44615 | -2.86827 | -45.25396 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d0d0507b-2fcc-3a0b-80ba-8b7bd8b026de | -2.53271 | -49.45628 | 2025-12-04 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2ea50adf-3f0b-3b7d-9f47-3392e4699b22 | -2.53405 | -49.46587 | 2025-12-04 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5ee30618-22de-3e61-8d4c-099500e357cf | -4.2029 | -44.24598 | 2025-12-04 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| adb75304-1f5f-3a87-a7a4-6a7da633854f | -2.48417 | -45.22322 | 2025-12-04 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f22da343-5d05-3347-b11b-9e6850e9ac08 | -3.65757 | -43.60576 | 2025-12-04 00:34:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| cc980011-7e14-3f4b-9420-11c90663a31c | -1.42167 | -53.0116 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 49103f14-9146-36a4-85c6-15a3da463721 | -3.22767 | -46.86593 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e0f619f9-06b4-39a6-b47b-791f1b272633 | -4.86133 | -44.87109 | 2025-12-04 00:34:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4a10ee0c-4521-3ccb-b51d-ba9db842d126 | -3.36276 | -43.57119 | 2025-12-04 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 649e5370-9a61-355a-ad90-c001be30ca51 | -3.85959 | -49.26356 | 2025-12-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f48dcd1e-9b0f-398f-99ac-43134d0f5780 | -2.88336 | -46.80185 | 2025-12-04 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 48719212-1c9c-36a4-83a5-cb1fc5868bba | -4.4733 | -50.092 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd7a5141-4de7-37df-b8a3-12178be44db1 | -3.51543 | -47.20983 | 2025-12-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 31479bb1-e495-3c34-8a97-5e3de05c2255 | -3.79868 | -50.60731 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed9b606a-56c6-3f6e-92d9-cf644802c45b | -0.18628 | -49.07108 | 2025-12-04 00:34:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa65e79f-3f82-3d3f-a390-21d7eefdcc38 | 2.91867 | -51.00605 | 2025-12-04 00:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d3efb954-22f1-3b47-abab-4d87111cb410 | -2.78903 | -47.42748 | 2025-12-04 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a5e40a3-b67f-366e-b29e-564ab49f7c18 | 0.32272 | -49.73129 | 2025-12-04 00:34:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b1442dfe-4c85-345d-a3ad-a74bd7b7eb1d | -3.91354 | -50.10767 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7354119b-c8d1-321e-916f-89ef101801de | -3.35823 | -43.57746 | 2025-12-04 00:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 68fe97c3-8b97-3538-8b23-083fc359dead | -2.85595 | -45.25584 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ff95d8ce-2e06-3d6d-b22b-af10d8a0cd65 | -2.00166 | -45.32493 | 2025-12-04 00:34:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| fa6b7881-0a38-3bc9-beae-fb5076172dbd | -4.13673 | -50.51725 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b2689ea-2794-3e8d-8ba0-499f138d8e5f | -2.89937 | -45.35368 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 65e7f4ca-7083-32df-b47c-7bad96f65359 | -3.47818 | -52.3583 | 2025-12-04 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6cd2e49-9ddc-3ce9-949d-f91b34afbff7 | -3.18082 | -48.6148 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a847aa9-bad5-3cd5-8cfd-9142d65acb05 | -2.07435 | -48.37194 | 2025-12-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2c816cab-4d81-3b1d-a934-f123246e2d30 | -1.8765 | -50.96112 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cf71d44-1f51-3346-aea0-3759786373aa | -3.21445 | -48.61472 | 2025-12-04 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 830d6392-5a01-3d54-a628-051523b01d1a | -2.97133 | -49.09601 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8dee8c42-3ab1-3eec-9766-d7f851bc0034 | -4.12216 | -50.68739 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 51a23f51-2cfc-39f9-a691-965ec53b789a | -2.42277 | -48.60108 | 2025-12-04 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2ce41017-183c-30f6-8fc7-a25abe34cb01 | -1.35928 | -53.22855 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 415a784a-1428-3aa4-ad2a-b5e6f09a66b7 | 3.46483 | -51.25604 | 2025-12-04 00:34:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16d091f2-216d-363c-bf58-6be0ba9772ae | -3.38148 | -49.00667 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 13967c18-669e-34bc-acca-0af116855a4a | -4.03508 | -50.38445 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b9a8c79c-90ca-35ee-86b9-76334c32f822 | -4.12375 | -49.4351 | 2025-12-04 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04e8ae46-5be5-3427-9443-41f736b830c8 | -4.12789 | -50.5185 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e649dd1-9974-3c63-b78a-75a25616843d | -3.54825 | -50.53502 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89e71b57-fdd5-3ce7-8f6c-ff44ff195634 | -2.61637 | -49.26108 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4869b504-a72c-398b-9762-f70f211a61ab | -3.66927 | -50.80843 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0b97e9c-25fa-3cf5-806b-9ee213774e0c | -4.18609 | -46.113 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3ccc4c20-8527-325d-84d0-fb670408966b | -4.34342 | -49.9521 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d010ae2a-480d-3174-ade3-7c3b730d98e8 | -3.63858 | -52.65366 | 2025-12-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc2f344e-24ff-3691-a276-8e5c0c26da14 | -2.64948 | -51.62515 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76e7ac4d-c249-3881-acbc-b45e74fd4639 | -4.3849 | -46.67179 | 2025-12-04 00:34:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6674a662-ca3e-3cd2-a948-4cd8f52c0fc6 | 0.83241 | -50.23053 | 2025-12-04 00:34:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a99c62b1-1d56-376b-93c1-e417eef84ebd | -4.12305 | -50.09313 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| c096583e-d192-3ed4-afa9-f99fcdbd55d5 | -2.54325 | -45.7183 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a9783e7f-ffbb-3fa3-86f3-63b99ad2e482 | -1.17043 | -48.86457 | 2025-12-04 00:34:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c2996fc4-e3b5-3a56-8e04-576e8f2e6536 | -3.85823 | -49.25401 | 2025-12-04 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abdc4e84-a717-3e76-a49b-63dea139b6c3 | 2.92689 | -51.01316 | 2025-12-04 00:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 76607193-aaa1-3517-83c1-083b11b28a79 | -2.59782 | -49.2637 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e0b9d9b-974d-34f6-895f-1b89829c98cf | -4.12429 | -50.1021 | 2025-12-04 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 7c1c53dc-864d-30be-b72a-7ca096067ba2 | -3.01203 | -45.44482 | 2025-12-04 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 49dddf80-ae20-3c18-8457-81b73206bc31 | -2.63082 | -47.30864 | 2025-12-04 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| c0c5ca85-bbfd-3f50-88d5-8b93933c4dc1 | -3.91603 | -50.12562 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 291e59d7-223e-3f28-9298-4e2c8b2dd8c5 | -3.84982 | -47.83541 | 2025-12-04 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b8882909-4cf5-3cf3-88f5-dee23182d3cd | -3.15614 | -50.56061 | 2025-12-04 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e8e68fdf-b75d-3bf4-8c19-7d7c7a45c901 | -2.54191 | -49.45498 | 2025-12-04 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8c66c75e-22cb-3096-aaf8-8779f25e9ef3 | -3.37892 | -49.25529 | 2025-12-04 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 97830688-dd63-330f-a525-52f06244f4be | -3.63212 | -52.53949 | 2025-12-04 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0d402ec8-c75d-398a-9749-1a2dfd4c54e9 | -2.42897 | -50.29604 | 2025-12-04 00:34:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9a978408-91ee-3ff4-bb14-c1e9c22de4c0 | -4.21638 | -44.259 | 2025-12-04 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f32c417e-c5d1-3d6d-86f2-1e3a2a0457cc | 3.67225 | -51.28777 | 2025-12-04 00:34:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29f0f111-38b2-361d-9748-79056283bbc1 | -3.93116 | -50.16911 | 2025-12-04 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33510ff7-df0a-35d1-9dfb-bf9377406845 | -4.50543 | -45.77853 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 3318e016-2a83-30f4-b5f1-8c331e1409bf | -3.88444 | -45.76839 | 2025-12-04 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d75f5363-1b3e-30fa-8b98-753008da7636 | -2.02535 | -47.00134 | 2025-12-04 00:34:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4eb56da2-2477-385d-85a4-c3967cb77584 | -4.43567 | -43.86519 | 2025-12-04 00:34:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9a115064-1f54-39fb-9154-5e113bbde5cd | -1.43205 | -53.01971 | 2025-12-04 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1aa753db-2372-3ce8-8897-a20cedcbfedf | -4.25316 | -44.14738 | 2025-12-04 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 866088ed-5af3-3036-b249-0788923057f8 | -2.3463 | -45.5917 | 2025-12-04 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |


[Clique aqui para ver as próximas entradas](README4.md)
