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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d09b0f4-4021-385f-ad4e-440c71dc9b19 | -18.42733 | -42.26716 | 2024-10-19 03:38:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c2f7c222-e61b-3bc6-9bd3-bfb2674558c1 | -18.41109 | -42.49262 | 2024-10-19 03:38:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ceb91ddf-e779-388b-b78c-718ed82a4f66 | -18.30854 | -42.15833 | 2024-10-19 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1131e5ca-0e08-3d70-a2ae-b2137c0fbbcb | -18.30784 | -42.16205 | 2024-10-19 03:38:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be7725d8-4f14-3440-b608-499a4b72dde1 | -18.29689 | -42.22053 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 44d44887-7e7e-3d6b-8570-40f67e6a34c1 | -18.29278 | -42.2194 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 71feaa8e-076d-36d7-bda9-b298dbca014a | -18.27183 | -42.28477 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| df0fa568-cf5b-3280-a633-d85feb122d1f | -18.26765 | -42.28387 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7997a006-d357-3344-b9e1-b30b47fe1a74 | -18.25374 | -42.24291 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89770a30-5558-3b4c-946f-577e81d33239 | -18.25037 | -42.23784 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24b5bc1c-b53c-3043-88f7-8d556ac7d546 | -18.24962 | -42.24177 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 868c009f-82c4-326f-b8fb-184c6bc502e9 | -18.23289 | -42.44444 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| aca0ca02-ba56-3851-8ab3-2b2b9938c4eb | -18.22932 | -42.60286 | 2024-10-19 03:38:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a88b4330-50b2-3ef6-a1f7-835ddc04716e | -18.22447 | -42.44253 | 2024-10-19 03:38:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75d18baa-f389-34fd-80c7-97fa36766ed8 | -18.22366 | -42.44678 | 2024-10-19 03:38:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a206cc7f-2229-3b1e-a7b7-7091951973af | -18.09434 | -42.71605 | 2024-10-19 03:38:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 022fef1e-4ce6-3938-a64c-faeb984bc615 | -18.08924 | -42.7193 | 2024-10-19 03:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2c93ba7-38c0-3013-9960-32ef7a509490 | -20.25006 | -42.98605 | 2024-10-19 03:38:00 | NOAA-20 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 461bcc8e-8a71-3993-96cd-7296f39f96fe | -20.24514 | -42.98883 | 2024-10-19 03:38:00 | NOAA-20 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 004a2091-1601-3394-a85f-75eefaec97c5 | -16.83222 | -43.32113 | 2024-10-19 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d50a6f59-9734-3fc9-a792-7aceb5745b6e | -18.29613 | -43.17876 | 2024-10-19 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf14a814-15b6-3291-978d-600320322241 | -18.28921 | -43.23787 | 2024-10-19 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e600f72-6501-3baa-9d19-4a5648b97bb3 | -18.28561 | -43.2327 | 2024-10-19 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 32b9313b-1259-3c1a-9710-c27da9d724e2 | -18.28476 | -43.23701 | 2024-10-19 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| decfcf02-22a4-3bbf-9eba-d4910877b2f6 | -18.28115 | -43.23186 | 2024-10-19 03:38:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 3f69e3d9-3450-3d3d-bd20-56b83cb5de24 | -19.67385 | -43.52536 | 2024-10-19 03:38:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 685a4b09-dbdb-3911-b43c-8b3411b9b9bb | -2.7885 | -51.3618 | 2024-10-19 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 9fc845ec-7122-32f3-8476-055127b11b7f | -2.9673 | -52.9169 | 2024-10-19 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 46eba119-2e2f-36ea-a1fb-db2e834087b1 | -2.9489 | -52.9174 | 2024-10-19 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| fd9da171-370e-3492-b43a-2aec443f5d4e | -3.4387 | -50.2158 | 2024-10-19 03:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| ab46c02b-d88e-3637-a887-05b3fb88e9be | -3.4202 | -50.2164 | 2024-10-19 03:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| cb120bb8-1369-3cb7-8815-0d8fbe62e379 | -4.706 | -45.8493 | 2024-10-19 03:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5878fe0a-41c3-3a25-b51f-7960bd6edc81 | -9.053 | -67.4451 | 2024-10-19 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a49f1f7b-3f2b-305a-84f8-20bc7b0a1cda | -9.053 | -67.4636 | 2024-10-19 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a3d25720-c439-394f-b2d6-50222e3ec313 | -9.0345 | -67.4455 | 2024-10-19 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3840761e-3239-3868-8ce5-89e6cb3835eb | -9.0344 | -67.4641 | 2024-10-19 03:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9576726f-2a77-354e-8d0b-94b3cd46f949 | -2.9489 | -52.9174 | 2024-10-19 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f9f9f135-8014-3365-9cc0-ad1df91e0635 | -2.9489 | -52.897 | 2024-10-19 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a1b69714-70bc-3337-bb19-b9f5774a17ba | -2.9673 | -52.9169 | 2024-10-19 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e76a4a51-58bf-3169-ab38-544c1586162b | -2.9673 | -52.8966 | 2024-10-19 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6f537a30-f759-34d7-9bee-ca5dbd9d9ad6 | -3.4202 | -50.2164 | 2024-10-19 03:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| ffa5d6ac-fa59-39e4-aa68-03acc42fd980 | -3.4387 | -50.2158 | 2024-10-19 03:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 5dcf1a4c-b845-3382-a122-f3068e820cae | -4.6873 | -45.8504 | 2024-10-19 03:55:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3a3afd9d-f247-33bf-9937-c029316a6df3 | -4.6875 | -45.828 | 2024-10-19 03:55:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 121ae5a4-8ed7-3a2f-ac11-e5b853712c91 | -4.706 | -45.8493 | 2024-10-19 03:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 4d7ab761-54d1-31a3-9ed5-f63bd7e88f9d | -4.7061 | -45.8269 | 2024-10-19 03:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3a5c9efa-7ab0-399d-a22f-1dd74772403b | -9.0344 | -67.4641 | 2024-10-19 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 56a974bb-8c19-34b4-8651-97f9dc285417 | -9.0345 | -67.4455 | 2024-10-19 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 23884a4c-ed71-36cc-b150-73be92467677 | -9.053 | -67.4636 | 2024-10-19 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 842676f0-6447-300b-b34b-5044b18e808d | -9.053 | -67.4451 | 2024-10-19 03:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 93e15e8c-8713-3f6e-aae4-9ba8f100c3b7 | -2.9489 | -52.9174 | 2024-10-19 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 5905df77-4e45-3712-8ba1-157a6f6d72b5 | -2.9489 | -52.897 | 2024-10-19 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5f376fc8-31ff-3530-9cdf-ee6b9dabc95e | -2.9673 | -52.9169 | 2024-10-19 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3ba083cc-7936-3e29-accd-ea2eea39e34f | -2.9673 | -52.8966 | 2024-10-19 04:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4b739dd6-daf4-30f8-8a96-a09c1ee2e833 | -3.4202 | -50.2164 | 2024-10-19 04:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 7e79ad08-bfc9-3167-81b8-bae713c687e6 | -3.4387 | -50.2158 | 2024-10-19 04:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4c32eca0-91ad-3894-8863-b877bdb13c37 | -4.6873 | -45.8504 | 2024-10-19 04:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ee5cd4f7-a211-3c59-9e63-bbb9cf01f0c8 | -4.6875 | -45.828 | 2024-10-19 04:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8b7d2491-5e1b-3e7b-b736-5c76e43d6a13 | -4.7058 | -45.8717 | 2024-10-19 04:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 87612147-9b85-37f3-8d2c-a947c707d73c | -4.706 | -45.8493 | 2024-10-19 04:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 298.2 |
| e9fcde3c-002e-3cf0-bb56-fc305bb32934 | -4.7061 | -45.8269 | 2024-10-19 04:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 7841f81b-0267-3a7e-b911-daf19aa4f2eb | -4.7248 | -45.8259 | 2024-10-19 04:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b0f25432-ce77-35db-b05b-3aece029852b | -9.0344 | -67.4641 | 2024-10-19 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| eaaa6fd7-edc4-36d4-a90a-4451b6277705 | -9.0345 | -67.4455 | 2024-10-19 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 1ce5dc21-3ce2-338c-9f91-a4dad89a9c44 | -9.053 | -67.4636 | 2024-10-19 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 23e0a8ff-b385-3f05-bfc0-1a5e920b754f | -9.053 | -67.4451 | 2024-10-19 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4d82acb3-c240-387e-800d-a987f189dac7 | -2.9489 | -52.9174 | 2024-10-19 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2073fd81-1bb3-3541-8280-cebd0a1ade9c | -2.9489 | -52.897 | 2024-10-19 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d9baf790-d5c7-354f-a5d1-3d8d57d0b23c | -2.9673 | -52.9169 | 2024-10-19 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e675be25-681e-3969-a59b-97c3e93c2bc7 | -2.9673 | -52.8966 | 2024-10-19 04:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 079862f6-e6c9-3f87-b094-48e9a4da0f01 | -3.4202 | -50.2164 | 2024-10-19 04:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| d1adf7f0-d196-3ec4-a0c7-28368745b67c | -3.4387 | -50.2158 | 2024-10-19 04:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| b5df3565-84f1-3fac-969b-2c490acb739e | -4.706 | -45.8493 | 2024-10-19 04:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 78c623c6-03eb-354f-84be-7f9c3c08999a | -4.7061 | -45.8269 | 2024-10-19 04:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| b06ef376-5c37-39f4-928b-2d4750f26734 | -9.0344 | -67.4641 | 2024-10-19 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f8e34513-9c8b-39b9-973b-3a3c694c71f7 | -9.0345 | -67.4455 | 2024-10-19 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 11fa6565-c003-3a32-b502-7bc0fae04596 | -9.053 | -67.4636 | 2024-10-19 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| eb0415b3-1e8a-3120-9050-919db21b4567 | -9.053 | -67.4451 | 2024-10-19 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 714f1eca-7ac8-3333-b663-d564d58d4305 | -12.5147 | -63.3014 | 2024-10-19 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e146348b-d563-3c40-b060-779c53206f37 | -12.5149 | -63.2822 | 2024-10-19 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5f612bcd-111e-397e-84eb-749da49cd2c1 | -12.5336 | -63.3003 | 2024-10-19 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e19aab41-47dc-3efd-81ac-c99c174364b2 | 3.05311 | -51.46735 | 2024-10-19 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eadc2b8f-3512-3ac8-9d52-c4d8851cedea | 3.05115 | -51.46616 | 2024-10-19 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 095fc903-8b27-3e69-8d4b-348177b3b460 | -2.0922 | -53.4017 | 2024-10-19 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a78ec6c-415d-3636-9ece-d41b2dd5c47e | -6.66559 | -39.59301 | 2024-10-19 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a225c5a6-03f6-3d45-9329-a5fe88ed7799 | -2.94317 | -39.96061 | 2024-10-19 04:25:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e1346d01-2623-316a-82a9-151aa4a4d8c7 | -2.92479 | -41.4642 | 2024-10-19 04:25:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3e125b14-7aa6-3bb0-bebf-761dc7a6cece | -2.88239 | -41.90929 | 2024-10-19 04:25:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0dd9d628-6be7-3166-bb6b-a1a7b8f6aeb8 | -3.56311 | -42.03637 | 2024-10-19 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 44da4502-6001-3c60-a09d-ce92925873f1 | -3.56245 | -42.04071 | 2024-10-19 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fb728ab5-7928-3312-8bea-053ac04de90c | -3.55877 | -42.04017 | 2024-10-19 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ca268bd-82a8-3100-8c4e-bfced3bf4e49 | -3.35233 | -42.77637 | 2024-10-19 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a6c69f5-ce3a-3933-9f15-bfab258059ec | -4.07792 | -42.91267 | 2024-10-19 04:25:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddb05181-04b4-3bdb-97c5-95ef87bbfaa5 | -4.07438 | -42.9121 | 2024-10-19 04:25:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a15ee4ad-624b-3cb0-a69b-080f1ecbfa9b | -4.07377 | -42.91613 | 2024-10-19 04:25:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03936178-1966-31ef-956e-166a4a48227f | -4.07084 | -42.91154 | 2024-10-19 04:25:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63418c69-4be4-3710-a87c-d65cb868701f | -4.07023 | -42.91557 | 2024-10-19 04:25:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd91f1c7-4f38-38c9-b933-67d02f3938a2 | -5.92446 | -42.96117 | 2024-10-19 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 077d91d6-cbde-319a-89ed-ce4a42d0bb51 | -6.54158 | -43.04213 | 2024-10-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 420b4879-4dec-383a-b7e2-61d8a06bc4de | -3.52165 | -43.22798 | 2024-10-19 04:25:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README15.md)
