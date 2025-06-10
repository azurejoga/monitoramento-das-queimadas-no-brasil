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
| f1549897-a438-3a8b-9b90-fe326eac5dfa | -11.57307 | -48.14092 | 2025-06-10 00:39:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9d9a4627-2a60-3308-9582-784277fcea81 | -8.60686 | -46.57134 | 2025-06-10 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 87757f5f-0237-30ff-a57c-d03238eef538 | -7.02124 | -44.5808 | 2025-06-10 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 18811df0-8b2c-339a-af16-adfcad15c6ff | -11.76674 | -54.38672 | 2025-06-10 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| fd69af1a-233f-3cbe-8f67-7739cacb9da7 | -11.63211 | -47.68919 | 2025-06-10 00:39:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 510b1527-0fd5-3b0f-a3e2-827fdd1f6b50 | -12.48982 | -46.84221 | 2025-06-10 00:39:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0c156657-aad1-3a86-a15d-05c98de405a0 | -10.2753 | -47.61375 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| df287565-4f05-3e1b-9946-ced30a4f8e6a | -12.09743 | -44.74836 | 2025-06-10 00:39:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a929535-4656-3c43-8554-7f895734bbaa | -10.83558 | -53.77776 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d40b44fd-cf66-3eab-be44-d517fb41549e | -8.60823 | -46.58083 | 2025-06-10 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3821b189-291f-30fb-a0e0-0052ae844c18 | -5.81784 | -46.48717 | 2025-06-10 00:39:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 465d7a8c-bd1a-3e9c-818a-99a4a02b1926 | -8.6096 | -46.59032 | 2025-06-10 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3331d737-459c-3457-9a54-346f41171e0e | -7.01657 | -44.62052 | 2025-06-10 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d9ad0d17-7258-3661-a4c7-cdbd698f37a5 | -10.2156 | -46.53494 | 2025-06-10 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f8cb4360-ec9b-3fde-bcbe-def3602b3185 | -10.06053 | -48.66323 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cc94581c-0419-32ad-aaa2-64d95496cd6c | -6.1853 | -43.3257 | 2025-06-10 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 52a10e4d-0342-3130-a603-fc0f4b284c8b | -10.0545 | -48.667 | 2025-06-10 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| afe0d2c9-42a6-37c8-ae56-076a9d7f51b2 | -6.204 | -43.3241 | 2025-06-10 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 8cdb5404-935f-3987-8dcb-d5d91510122f | -12.7169 | -58.0242 | 2025-06-10 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| d87f1379-cdc9-34ea-95fc-fe904aeec7cf | -5.2108 | -43.3067 | 2025-06-10 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 3e95ab10-ac76-3268-943e-c0fd7446dc93 | -5.639 | -43.6015 | 2025-06-10 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9d9a2fc4-0324-39c7-98dc-62dba6b0d650 | -10.0548 | -48.6452 | 2025-06-10 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 2a631914-af84-3dac-93c0-d2cfd2b2a58c | -5.2106 | -43.33 | 2025-06-10 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a4993ceb-31bc-3b0a-a4c0-043797de04d1 | -2.92174 | -48.23407 | 2025-06-10 00:41:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e50b44f-f5d3-3e51-adf6-6f416318eb30 | -3.58801 | -49.43894 | 2025-06-10 00:41:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a028abf5-26df-3942-99db-79fe670103a2 | -2.92299 | -48.24313 | 2025-06-10 00:41:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 470b5227-8ba5-3349-9bb5-29bed41f494c | -3.40246 | -47.58466 | 2025-06-10 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0e7633e7-5068-33e1-b41c-fee5196dd03f | -3.04342 | -49.43593 | 2025-06-10 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 24936477-8477-39c9-93ea-fd0bea5b0a51 | -17.5445 | -46.3266 | 2025-06-10 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3da30080-318b-3496-8604-055d4f932142 | -6.204 | -43.3241 | 2025-06-10 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a8c0128d-7407-3baa-83a6-1f698a043a20 | -5.2106 | -43.33 | 2025-06-10 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 308c7a5e-c20b-3a8e-8640-f670398c251c | -17.5245 | -46.3308 | 2025-06-10 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 8760920a-21ec-3cf4-a14e-476052b7ed22 | -10.0545 | -48.667 | 2025-06-10 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 63ef8e95-4601-3983-a281-5589281c2dea | -17.5251 | -46.3074 | 2025-06-10 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0aa7f546-a59c-3366-bada-3089712b674b | -10.0548 | -48.6452 | 2025-06-10 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 65f0cc29-8ff0-3a91-9c45-23d604f141bc | -5.2108 | -43.3067 | 2025-06-10 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 30bf8d2d-edce-3428-a279-c658830bf971 | -9.5152 | -40.331 | 2025-06-10 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 673c7a48-59af-37a3-8826-5865715c78ab | -6.204 | -43.3241 | 2025-06-10 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d51ed180-06f4-3a26-9ab2-fcbde61eb766 | -9.496 | -40.3337 | 2025-06-10 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 8c51a36f-9b7d-3a6a-8980-1801a99df0be | -10.0545 | -48.667 | 2025-06-10 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| c5f4a93e-0b5e-3258-84f7-9757a2a6ac88 | -10.0548 | -48.6452 | 2025-06-10 01:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c8bda6f2-3811-3c3c-b17a-ab3fcad0afa6 | -9.5156 | -40.3061 | 2025-06-10 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 760f1481-3485-3e8f-927b-0da107d46e30 | -9.4964 | -40.3088 | 2025-06-10 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.8 |
| eb339ac6-10e9-3f24-93ae-f1902d501e71 | -6.204 | -43.3241 | 2025-06-10 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8a61aa07-90f0-3f65-beaa-68fa7fb194ff | -10.0545 | -48.667 | 2025-06-10 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b648cf4c-fd56-3c4b-9c59-b195abbdb030 | -6.204 | -43.3241 | 2025-06-10 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 54edb855-91a1-36cb-bfaf-5f6b9deb4273 | -5.2106 | -43.33 | 2025-06-10 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f299efd0-db6a-3daf-97ca-916edc0c4f28 | -6.1853 | -43.3257 | 2025-06-10 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| bfabf934-23e1-38f3-a727-8745f16d1048 | -10.0545 | -48.667 | 2025-06-10 01:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 8811fbb5-439a-3d0f-8c5c-9338cb49454c | -5.2108 | -43.3067 | 2025-06-10 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 9e091e21-9f22-38c7-8417-da7b425bbe57 | -5.1921 | -43.308 | 2025-06-10 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 018cff54-44c8-39ba-a1fd-3afc3455962b | -10.0545 | -48.667 | 2025-06-10 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a1e62320-73b5-366d-9c9f-b7ae898874f1 | -5.2106 | -43.33 | 2025-06-10 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f7f840fc-6842-3e7d-964b-79a5a487ede7 | -6.204 | -43.3241 | 2025-06-10 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f4893883-6d03-33ba-b91d-5de479204159 | -5.2108 | -43.3067 | 2025-06-10 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 13bf2d4d-4a90-3824-b0a5-336082d34753 | -5.2106 | -43.33 | 2025-06-10 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 10437d37-e02a-363c-b824-014bf417c2b4 | -6.204 | -43.3241 | 2025-06-10 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 91ae8464-e248-37a9-a200-55bb847146ad | -10.0545 | -48.667 | 2025-06-10 01:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| b6c351d6-982d-367b-a45f-87810457d8d0 | -5.2108 | -43.3067 | 2025-06-10 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 9e882cd4-684d-3b3b-afe0-3cd66441abf7 | -5.2106 | -43.33 | 2025-06-10 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2b366e37-1b32-3034-9b94-8c60801ba4d2 | -6.204 | -43.3241 | 2025-06-10 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1ec5fbf4-79cb-385a-aae4-659f3191e00c | -10.0545 | -48.667 | 2025-06-10 01:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8ae92667-21dd-3cad-9089-9132ff306397 | -5.2108 | -43.3067 | 2025-06-10 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 8dd16757-088c-3db5-8f43-5a566263c872 | -5.2108 | -43.3067 | 2025-06-10 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0ace9ad8-3ed9-3c14-9834-119d4521340f | -10.0545 | -48.667 | 2025-06-10 02:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 04aea01d-319a-3a6d-b9e4-a64bb59140b5 | -6.204 | -43.3241 | 2025-06-10 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ee2da77d-8fa0-3c8f-8c5b-3c07d31de384 | -10.0545 | -48.667 | 2025-06-10 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f073e18f-44ab-3d74-bb81-b87028be314d | -6.204 | -43.3241 | 2025-06-10 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0f3608c2-0337-372b-9410-831d60fe04ac | -5.2108 | -43.3067 | 2025-06-10 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| d0515336-8bb3-3ab3-ae4e-07e1e203bfab | -10.0545 | -48.667 | 2025-06-10 02:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 67ccc6e2-84c2-32ab-8d06-5c6a035dcf30 | -10.0545 | -48.667 | 2025-06-10 02:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c38dd275-1fe6-311f-930c-c9204b4a636d | -5.1921 | -43.308 | 2025-06-10 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 847c5d67-dae0-3152-976c-24b28ec3f16d | -5.2106 | -43.33 | 2025-06-10 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8132b78e-9b99-3e4d-b67b-37235e798956 | -5.2108 | -43.3067 | 2025-06-10 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 2cdbc0be-1ccc-31c8-8b50-f26e3ef85a36 | -5.2106 | -43.33 | 2025-06-10 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d7a0f8cd-d743-3852-8847-623d79bac735 | -10.0545 | -48.667 | 2025-06-10 02:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 78df4b73-bdad-3fbc-9bfe-0f76188880fa | -5.2108 | -43.3067 | 2025-06-10 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| a8237d5f-afe7-3c92-9436-555867eb25aa | -10.0545 | -48.667 | 2025-06-10 02:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 1dc5400b-fca4-3bad-874b-546aa11fa417 | -5.2106 | -43.33 | 2025-06-10 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 68538f17-7522-35eb-8d45-2702ae803f20 | -10.0545 | -48.667 | 2025-06-10 03:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 4b034afc-21ea-3a84-b72c-3898ab125456 | -5.2108 | -43.3067 | 2025-06-10 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 6e6ac866-248b-3ac0-80d2-0214ca259d5c | -5.2106 | -43.33 | 2025-06-10 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d0941bf8-d764-3ba5-a39d-3f7767a20631 | -5.2108 | -43.3067 | 2025-06-10 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 0f9c5ee7-1b09-3e35-9ec5-c6cd00f7eaa1 | -6.19722 | -43.33495 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| cd30cbb0-5564-3771-bc35-746b7eabc4a1 | -5.21001 | -43.30837 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| ef36f715-c35a-37d4-90d8-896b9d5fa3cc | -6.19157 | -43.32779 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 699375ef-c6a0-3b68-ad98-1e0b939c6f1a | -5.20778 | -43.32092 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f734f21f-22fc-3671-992c-9284613b8832 | -5.64634 | -43.59606 | 2025-06-10 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42649a81-6157-3c9a-b601-66d9bb776d5a | -5.20921 | -43.31509 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| bc3284f7-2fc0-304c-b471-3fc049d0e617 | -5.78194 | -43.62477 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f23c665-c211-3dd8-8cb9-e8b5a92c4fe1 | -5.21579 | -43.31564 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| adf1b24b-001f-3e7f-a5c3-0778a01c8299 | -4.31506 | -37.97061 | 2025-06-10 03:23:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7750e751-0d01-395c-8dee-bc1b891733b9 | -5.21612 | -43.31603 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 63fa0f94-4cb7-3142-95e9-21ca2d19d43e | -6.21196 | -43.33083 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dd8a6ae-3dbc-334f-8ec5-6d57d518198e | -5.64516 | -43.60252 | 2025-06-10 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27775262-fdc1-370f-93f4-ae518cdfcd35 | -6.21866 | -43.33234 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be5f5ebf-0297-3e04-8a1d-7400739de92c | -5.20889 | -43.31467 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f6f63d47-32fb-3bcd-83b3-8bed58e64d5d | -5.20806 | -43.32133 | 2025-06-10 03:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 62dd351c-e334-3e62-901e-c2f0d2091761 | -6.19836 | -43.32883 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ecf95904-8dbf-3d0e-bdc5-b656ffddbdd7 | -6.19047 | -43.33372 | 2025-06-10 03:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README4.md)
