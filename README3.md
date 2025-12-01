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
| 8f1d43c3-404e-3346-b138-6c1261b4606b | -2.27583 | -47.40939 | 2025-12-01 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c381b1ea-bd3c-3510-be42-0f22c033014a | -2.84929 | -45.62291 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 6f0b062e-d251-3879-a72a-197a6d4a6a72 | -4.27061 | -46.70642 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 88ef9119-96df-379d-958c-d768be8df7e7 | -2.27708 | -47.41846 | 2025-12-01 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f59bd263-e606-3902-afde-2ba565ac85cc | -4.6978 | -44.41291 | 2025-12-01 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a5148404-40bd-3ac7-9809-9c94f063ee78 | -2.93337 | -53.26816 | 2025-12-01 00:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2146f0ae-4bf8-39a0-a0c0-0aeb76068437 | -2.33988 | -45.74036 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cefa7fbd-df6b-3540-bd0a-c7de7dd9f373 | -2.92182 | -48.23192 | 2025-12-01 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f749069a-a794-36e8-b173-6598e2a77dec | -3.67765 | -47.29003 | 2025-12-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9f4807f7-8d44-3b6e-b2dd-05b5fb4d7db3 | -3.13287 | -50.25122 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 86099d34-1d5f-3993-a1a9-acff875f5228 | -4.38893 | -43.33712 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 63072392-155f-3012-899f-fb9a68ff1821 | -3.55852 | -42.53637 | 2025-12-01 00:13:00 | TERRA_M-M | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| bf539e9f-0977-3231-b953-41733392ecbf | -3.20842 | -44.43174 | 2025-12-01 00:13:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5af1cda7-40ce-32aa-8ddd-864cfccf443d | -3.70884 | -45.906 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 740a6777-b580-33ad-bf9f-bab5fc6dfb48 | -4.37292 | -43.15562 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 3259d5b2-148f-3af4-896f-35ac5c622880 | -4.70685 | -44.41156 | 2025-12-01 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4aed9d5c-cd0a-312f-93ae-a69597240813 | -3.57991 | -45.70555 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f21adbf3-b4e2-3ae0-bf77-9595f65b981b | -2.13449 | -45.32514 | 2025-12-01 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5a22fd5-99a6-3c03-847d-10ca77aaebfa | -3.21871 | -50.12774 | 2025-12-01 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 8d1d9476-fd20-394f-bf54-166f50ab0cfe | -2.85053 | -45.63179 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce39ead2-ccd1-3952-950b-b23a1993b16c | -4.37783 | -43.32795 | 2025-12-01 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| caeead6b-1b98-3a40-bc3d-160c972e1df8 | -2.04426 | -46.67358 | 2025-12-01 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f101ff5f-8e01-388e-8e52-8b87ce121bba | -2.74148 | -49.32552 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eea08429-5ba4-358c-b63b-1ef1b7d62157 | -4.12965 | -43.72792 | 2025-12-01 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2ff42311-cefc-373f-8c6a-04ed1f2f9134 | -2.60189 | -49.27097 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af0b9b8f-9649-3235-bb3d-1222c7cae9d3 | -3.15113 | -45.48061 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 8871f46f-4c88-3591-b3e0-ebdc9d16ae38 | -3.68924 | -50.62693 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d3f66215-98cf-31de-a00c-9fd0c26f6fca | -5.49959 | -42.16628 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 76175e7e-115a-31b8-9450-ced5c799cca8 | -4.37139 | -43.14488 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| b0509f00-bfee-3ce7-9ec9-fee411bda12d | -2.34874 | -45.73911 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9aa46c61-2359-3242-92b6-6aa1259a9023 | -3.19736 | -45.54037 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfb8a413-b380-3ba5-9103-fc2ce5c3e1a3 | -3.1499 | -45.47171 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b85264cc-8b21-3a00-b378-aba213a588ad | -2.25178 | -45.70475 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5d1d2709-b4a6-313b-bdb7-9ca014fb32c4 | -3.71514 | -50.65234 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 80c15e64-a404-3d14-9146-a64fbff6886e | -3.10038 | -44.98239 | 2025-12-01 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eed34a01-1458-31b0-b15f-0ee8ec0f3300 | -2.61023 | -49.25846 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| afa04b79-50da-304c-b162-ac17cab24799 | -3.57868 | -45.69673 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2d0e4c38-c9a7-3adf-af0c-01236e849a1f | -1.6015 | -45.99216 | 2025-12-01 00:13:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 86c8fd1b-90e5-3409-a116-656674483cc7 | -3.38093 | -47.2751 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fa7b8b8a-aacc-3533-a84d-3234670c1443 | -1.92502 | -47.06517 | 2025-12-01 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 308f8489-fb52-349d-8c61-4d76a9449122 | -4.03382 | -46.73053 | 2025-12-01 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 78b9bf7e-a4d6-3618-8ccb-8ebdbdbbb15e | -3.45058 | -50.16329 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3992cbc1-4c06-3b92-89c7-0e2427afa161 | -2.44927 | -46.33542 | 2025-12-01 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d805a9a1-ddc9-318d-85ea-67732590280e | -2.27076 | -45.71114 | 2025-12-01 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d26ee6f-17ad-3c73-8b59-3a9b61590596 | -2.24957 | -45.62344 | 2025-12-01 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ca8dbca5-ce93-3451-9eb5-487bfc71b41b | -3.2623 | -48.56591 | 2025-12-01 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5fa54fe4-0bba-3e22-9e33-50f238615c56 | -1.66941 | -46.5471 | 2025-12-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb68151f-31c4-34f0-8135-449d11c273ae | -2.39548 | -47.60983 | 2025-12-01 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c83d9e4f-f206-334d-91d8-febfb04b1962 | -3.2637 | -48.57619 | 2025-12-01 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c0ad8bca-3151-3ef7-9f1c-33d15d7aa23b | -3.59976 | -47.26043 | 2025-12-01 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6a358251-18a6-3998-bcd0-da4109f7bc1e | -4.69648 | -44.4036 | 2025-12-01 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22d47238-a936-3379-b40f-05b842e72fc8 | -3.35643 | -46.08749 | 2025-12-01 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 63018845-47bb-3496-9440-ec4ca49f5901 | -4.59701 | -45.94128 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1529dd39-4544-30a0-b63e-692c58cdb268 | -3.74111 | -46.00904 | 2025-12-01 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d061bea8-86a2-3dc7-9fc0-09536f009065 | -2.35999 | -49.30029 | 2025-12-01 00:13:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8734016f-c50c-30a2-baf3-e34644c1ace8 | -2.59396 | -45.83977 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c6a27747-591c-35b8-8a73-807ed9b89634 | -4.36323 | -43.15702 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 11039211-492e-3194-9eee-2ae33b7dc109 | -2.83878 | -48.83527 | 2025-12-01 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2c17594-102f-3824-9e97-41943e763d7e | -3.00038 | -45.12323 | 2025-12-01 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4aa73019-b373-370a-9b22-cecb9662c04e | -2.92196 | -45.28798 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ae6a068f-fa1e-381d-a401-ebbf4d618618 | -3.04797 | -49.47369 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0159c4b9-d4c7-3dee-b7ef-e47491823296 | -2.97321 | -45.32028 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a045a6cc-1209-313a-8032-c1945f45b232 | -3.93969 | -45.85234 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1dd2e6cb-5dda-3973-ab49-bd26f2033fd5 | -3.50496 | -43.32019 | 2025-12-01 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| e87f391b-a556-3b78-a988-2617d4fc5066 | -4.3617 | -43.14629 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 85380fd4-3868-33ed-8395-c9a4eccaa05d | -2.86873 | -45.5023 | 2025-12-01 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| deb2bf96-5424-345a-bd4b-01869c274c33 | -3.57046 | -47.18093 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 32e2ef38-9e00-3d0d-a6fe-fac00bab3219 | -3.39116 | -47.28292 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6cf8ee14-f72c-39e2-8020-283ca1a7a266 | -3.2131 | -41.56012 | 2025-12-01 00:13:00 | TERRA_M-M | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| c77ee6d4-7b04-3bec-9251-bb2220a8e5d1 | -4.13905 | -43.72659 | 2025-12-01 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d44fef77-63de-3b6b-b701-e799afa3450e | -2.63975 | -49.10929 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 44cc5f1c-a80a-3895-8143-9479ec2e98f5 | -3.62011 | -50.62768 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7930e9e5-8e55-3127-9524-aa2fec75f3b7 | -3.47732 | -51.35772 | 2025-12-01 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b91f9835-c433-3a7a-8620-6cd81bd3d685 | -2.45098 | -47.07942 | 2025-12-01 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c64df3e5-f771-30cb-a93c-b4a825df79c2 | -3.10832 | -54.16452 | 2025-12-01 00:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 9ec699bd-3d55-3910-94d0-9ad80749292e | -3.58511 | -50.28117 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e54dcb5d-7775-329e-8cee-d34f4477ebbb | -3.56921 | -47.17184 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5145655-4129-36c9-8ed1-a78d3fea0b47 | -3.27332 | -44.18418 | 2025-12-01 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b637f668-c0eb-3843-8959-b3d02cf6568c | -8.0507 | -43.1472 | 2025-12-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 995a1327-29aa-3be2-a67a-9eada7f67eb1 | -3.6008 | -47.2739 | 2025-12-01 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a861188a-f737-3748-95db-be735944e744 | -8.0321 | -43.1257 | 2025-12-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 1b3e5c61-49e3-3378-9fc3-868c9be9f1e4 | -4.4064 | -43.3351 | 2025-12-01 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7409573e-6042-3022-bc4f-81d31e93edd9 | -20.0142 | -57.4484 | 2025-12-01 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 2a14b91b-d378-3f86-a1e4-944dadf15a42 | -4.3889 | -43.173 | 2025-12-01 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| fcf0fc1a-f9a9-3d7d-a481-7e234989f979 | -3.282 | -44.177 | 2025-12-01 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| bdfdb74b-29b2-3ef6-8abf-d878bb767f29 | -4.3877 | -43.3362 | 2025-12-01 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 7312d878-e8bf-335e-ade2-677ca466f009 | -3.7009 | -45.9 | 2025-12-01 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fa428a7d-1cb8-36d2-96d6-64a6fe4fb383 | -2.2534 | -45.6167 | 2025-12-01 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 6a496556-d45d-3027-a4c3-3a0bab90b176 | -8.0513 | -43.1001 | 2025-12-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 390c702a-376e-3d57-ab6e-1838a2ce5a43 | -4.3516 | -43.1519 | 2025-12-01 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 378bcf23-b6ed-3f07-81f1-934fc83ba8a7 | -8.051 | -43.1237 | 2025-12-01 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 234.5 |
| fffe7df0-26cc-3c8a-abda-76beee71090f | -3.1989 | -50.1396 | 2025-12-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8950f2a1-5f70-3d17-8d8d-1c23a0ee4f1d | -4.389 | -43.1497 | 2025-12-01 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 77b91805-eb56-3772-9683-a2b310232445 | -4.3702 | -43.1741 | 2025-12-01 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 8f84d3eb-a227-390b-a188-281b42896d01 | -3.2174 | -50.139 | 2025-12-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 03247013-c706-3779-a183-04ba7a2db700 | -4.3703 | -43.1508 | 2025-12-01 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 341.2 |
| 00886d5a-4d2c-37b5-b7e4-c4f129469e0d | -23.1251 | -45.2832 | 2025-12-01 00:20:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 5b50f74d-63f1-3618-8975-479ac533b647 | -2.2534 | -45.6167 | 2025-12-01 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9480a36e-ab4f-3833-a068-a13c95cc8e4c | -3.3014 | -44.0385 | 2025-12-01 00:30:00 | GOES-19 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4f5bfcf6-80ff-3ccf-a345-51745a6c9fdb | -4.3702 | -43.1741 | 2025-12-01 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 220.5 |


[Clique aqui para ver as próximas entradas](README4.md)
