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

## Dados Diários - Página 214

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6f9f66e-e6c0-39fa-bcf3-d03939ab2a11 | -6.31581 | -54.80678 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ba7d42f-a217-3405-aca2-0db75b5bb3d0 | -6.88131 | -45.89547 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c75c259a-d6a8-3482-8f6c-d13d274e0e48 | -11.98755 | -57.61452 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e50e1c92-60f6-32a8-80e5-8e42f736c887 | -6.42295 | -55.19777 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b40d33eb-6708-3533-a6ae-84c5b7e5ebc2 | -5.93537 | -57.708 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a7578f-d536-35a4-a286-dd353cb22b01 | -5.69754 | -53.47875 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d573392a-38f2-3b67-99bd-253e8da2d366 | -6.12691 | -55.68561 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d153de61-1d18-32d1-9a0a-1174d9e56734 | -6.10272 | -53.50625 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a22d2b52-aed7-33a6-b707-075963b43b1a | -5.87589 | -53.52111 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6df16d3f-543b-3d4c-96d2-d06701d8c40f | -6.10148 | -55.72948 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85fb7240-f687-3ede-a794-236fc83d44b8 | -6.22012 | -60.03503 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f94b0fbc-dad8-320f-b44b-fe48d7cfe0b2 | -6.38175 | -56.2291 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d1b5da5-500a-3efe-ad8c-e3594f894b27 | -4.5197 | -61.12884 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74307cd-d0da-3693-8321-a021ce7163d8 | -12.21492 | -57.09014 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5c90725d-612d-39c6-81ca-587bade20b55 | -6.18468 | -52.86728 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94e1765-be91-30ad-91b6-83c4047ce938 | -5.71185 | -53.49717 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 14b65c9e-a323-34f6-a269-3f1d1db8a627 | -4.50561 | -61.11945 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee12b4e-122f-3b24-915c-580ccd6c38b7 | -12.23743 | -57.08909 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b41f7a80-9384-3c58-bb54-1aabd36a0c0e | -7.18483 | -52.62972 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eebe9a32-2d9d-36a5-ba79-fa9e162e7d1b | -6.88219 | -45.89383 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6c6148f5-2d06-3aed-b091-5dd43eaf86fd | -8.27906 | -45.73907 | 2026-10-09 05:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c38198f-10e2-3d84-88df-04ed664a9571 | -10.36855 | -61.22286 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1996fd46-ae0f-3530-84fe-597a5627f19e | -4.121 | -59.88272 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1f31cb0-f42c-3bb1-92f7-433325235a94 | -5.93419 | -51.83482 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d2956fd-dee9-3364-a8ed-7c83189af404 | -4.73705 | -55.65868 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b098e52-220a-3fd5-a9c3-4e8b8b159985 | -12.7789 | -60.60583 | 2026-10-09 05:25:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2372ac57-5aba-3540-89ae-b642325a8bf4 | -12.21315 | -57.07657 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e4dd8fb-0867-3b65-ba5b-1579ced52b91 | -12.22274 | -57.11337 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c0f83aa3-4f3c-3d28-a9e5-4563f8f2148d | -12.12601 | -57.16151 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21aabb0d-3bc8-3a1c-9587-ffaa63f3bbbf | -7.2508 | -48.06758 | 2026-10-09 05:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84bbd574-5c82-3012-a96f-79222b8ad142 | -6.09873 | -55.69881 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801504e7-0b4f-35f8-b453-205a53d6a927 | -12.23856 | -57.10695 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f90e4d04-92e1-3d1c-a6b7-219a1b1f325e | -12.21128 | -57.08958 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 723ca9a7-b23a-38eb-aa2d-20c151f7a569 | -4.93033 | -55.86217 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b845a772-fc6e-3945-a0e1-964bb24edcb5 | -6.41553 | -55.19947 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9189a153-dbb7-3204-b202-04c3f87a7bed | -5.25477 | -60.33733 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdf6cfd1-846c-3645-b957-e5a3267fee05 | -5.24018 | -60.19158 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6e57c9a-e8e3-37f0-bd0c-0bbd36dc2fe7 | -7.08217 | -52.69062 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72df0dff-6ede-3dc7-9508-6a5a6c55687d | -12.23441 | -57.08422 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| dff0b59d-9562-3850-9a88-0e744e4f0b61 | -17.41305 | -52.02164 | 2026-10-09 05:25:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28502a4-3e1c-3977-88e1-b13c362e3f99 | -12.22711 | -57.08313 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d6c19c4a-7d05-3bc9-a93e-a0e14e3196a9 | -6.48902 | -55.29886 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 699a37dc-814c-3839-aa7c-a8fceb4c4cb1 | -6.49513 | -55.30903 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22a362df-ac58-36a0-852c-7eedd2516091 | -12.22097 | -57.09989 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa782d27-e1cf-3026-bc9e-67eb2f7903d8 | -5.96355 | -55.33988 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 631f1122-fc5f-3154-b12e-eb3922d026f4 | -5.89381 | -57.71998 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adac90f6-45c5-360d-a34c-ee01f523f25c | -5.69915 | -53.46762 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bacb6d6-6d4e-3fdd-9018-061c014e6aee | -4.74722 | -55.66446 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e86418-85ae-3aa4-8c81-b76d5eb0121a | -17.41306 | -52.02165 | 2026-10-09 05:25:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0424b61-a40b-3bfe-87db-44a44bf82b3f | -8.21962 | -46.41053 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8409e4d-196f-39ee-a8bf-9fe46c4ec2cc | -4.22505 | -59.54875 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8860a762-3967-3a79-ad45-dad125e2855e | -13.197 | -54.3755 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 843ce595-ed58-36e7-a757-2cfac8c4e054 | -5.96144 | -55.34248 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a120bb70-54fc-3069-903a-6b8c84fc7545 | -11.97691 | -57.61291 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a6ddfe0-f7e4-3272-b24f-07638e75938b | -6.23116 | -52.88969 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a2b0a8-a000-3741-a6a5-5d6ec4694b4e | -5.99992 | -53.49892 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75aba4dc-099f-3402-b3ee-deb52655b013 | -8.22038 | -46.40456 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 986ab705-b5e3-3d22-8c5c-d4056f8327c0 | -6.4048 | -55.27234 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 156af4d0-d268-3098-9ef9-acecf65a04f1 | -13.16051 | -54.34864 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4790c46-dcff-3b20-a2ba-221ee522a480 | -5.97033 | -55.38474 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f3c33b9-0590-35db-a563-d4e254805112 | -6.41236 | -55.19149 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 206a9356-0661-3477-8bd4-0d1b41256bdf | -4.80502 | -56.13835 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afd69571-5d0e-307d-b63f-503f9380434f | -5.8795 | -53.52533 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be638c1a-9511-3bdc-84eb-6a8d5b1a25ce | -6.12578 | -53.05732 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc5bf223-fa82-34b6-b6c8-c02b193407c6 | -6.58073 | -53.01739 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aaf5356-f84f-3b35-b620-68b21d87269b | -5.2096 | -56.07006 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9963d46-3b33-364a-ada4-c445b1f53e63 | -5.22482 | -60.24414 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f1f4c80-9f4e-3df0-b683-3fdcb7ff664e | -12.10787 | -57.15877 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ba93b8a-2e47-3b50-919d-7dc8d7e4ccd9 | -6.12428 | -55.70262 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 037ff7d4-d9b0-3376-baff-d9f1bc875160 | -6.49069 | -55.31298 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03155d9d-332b-3ea8-8442-f8e44fa20848 | -6.11433 | -57.85283 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84d090ee-64cd-3e56-aa9b-c6d1ccc33072 | -5.29979 | -60.0989 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba811d4-5d91-373e-96fe-4c666c723e80 | -5.27075 | -55.95546 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9f62881-613e-36a4-b232-9b6c4a683f6a | -12.17543 | -57.10314 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5513842-9cec-3418-a619-2add4e8277b1 | -12.20872 | -57.13332 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d848f7e3-d13f-36ed-8bf6-40cd76aa0965 | -5.70112 | -53.47233 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14d45457-a951-3051-9f14-953ffca059b5 | -12.23617 | -57.09778 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 38a927bf-b450-3348-a0e2-b06d4eb5b654 | -6.45244 | -55.05392 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba9a2d4-69bf-350c-b276-ea290ccf5692 | -5.85519 | -53.4599 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c801936-a1a9-3959-b678-9e2ba8bdc6aa | -5.27789 | -55.95655 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1612c922-2741-3377-b1af-521324b0bf7a | -6.46278 | -46.0273 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37d16f0f-03e3-342e-b817-efe1ed6ae3d8 | -6.2404 | -52.8564 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7241216b-bcce-31bb-87b6-7f0ebc5184fe | -6.87329 | -45.90718 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8db9aafe-be43-3c67-ada0-b8ba26a9fc0d | -12.21298 | -57.12952 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93f98a82-89b1-301a-b3b5-c29429245010 | -11.75514 | -61.05935 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3df9b893-082a-3df7-b6ed-9485c5d9acbf | -6.50568 | -55.31516 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 266fde6f-fb05-3b21-8d23-c7c07e695c77 | -6.31689 | -59.96412 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce7b29da-489b-3acd-8278-d375313b69bd | -12.20446 | -57.13709 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b76197b-9113-3a67-9824-641915944e9d | -5.26656 | -55.95896 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdee6c8d-3b0b-3282-8f34-33354ccae36f | -12.21671 | -57.10364 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2806a854-6e8f-334a-9fd0-839576f962b5 | -6.52994 | -55.26112 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20e09671-41ec-3c45-8e7c-ed65b2b42be9 | -4.06541 | -59.83038 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fccd5bb0-a381-3973-afd5-81419d53c073 | -12.84707 | -50.57732 | 2026-10-09 05:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed60de99-29d8-36b3-bcd1-365aa0246941 | -5.29923 | -60.10246 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33be28c9-bd3d-3215-8f23-4aea7b39d38e | -6.132 | -53.51023 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea2ff709-ccc8-3da7-9f61-bbe2eea2f754 | -6.87962 | -45.90849 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a4b17cea-d012-3f1f-9bd0-7a1c0ebe6a73 | -4.12322 | -59.89036 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94265a0f-2931-37bd-b687-4cebbf9d7632 | -5.94969 | -55.35589 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 91b204db-8dda-3bb2-a99f-f3f1e79cc770 | -12.23013 | -57.08802 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 8c3b73b6-284d-3951-a235-9f6608a436f3 | -6.51164 | -55.41034 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README215.md)
