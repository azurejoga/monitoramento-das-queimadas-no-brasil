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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f7440ad-463c-3a72-a244-46784813c2bc | -8.35003 | -46.16711 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ec18262-3530-399c-bfa0-e5a7857d5eb7 | -10.9296 | -50.41168 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bd68552-b6c7-305f-a1c7-43aac1f3ce3a | -13.21559 | -47.73287 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0823cdf4-ea0e-34d6-8c13-22b616c495fd | -6.83141 | -44.78021 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d83340cb-33f3-3294-8afe-1f714a31d8c4 | -12.23002 | -47.48935 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc4d8a40-6414-3816-858f-492b709a4c99 | -1.59315 | -48.02999 | 2025-10-25 04:19:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49dd7de3-1c58-3323-a0eb-81094e338ead | -1.32749 | -49.11542 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bddc8ce7-ceec-3f1b-b3d9-553effdf1031 | -7.48342 | -46.87984 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8514010-d59f-33f3-91d1-081581bb5c26 | -7.55746 | -47.11378 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c609cea4-1732-38e9-9561-29c234a594a4 | -5.81367 | -52.10012 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 060700fe-6335-375e-985c-241b5ed75d30 | -8.14196 | -46.86545 | 2025-10-25 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b01191d-7365-35ed-ae1b-3ff0c0d04752 | -12.00451 | -44.0232 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d7d11d3-4bec-3632-b138-024d51b1d76f | -8.07317 | -48.16938 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d3dec51-271a-3b5b-9b18-babe28d66567 | -12.22528 | -46.50381 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 4956e26b-d1fe-3ca7-9091-817885d9b524 | -6.94765 | -45.03297 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a95d3a6-7ca4-38d2-9f90-6490da12549f | 1.63836 | -55.74886 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43074164-df31-33bc-85ec-327706870435 | 0.36465 | -50.92519 | 2025-10-25 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc33092a-ab6e-3cc6-bf3b-1f426fba04a5 | -8.11699 | -47.06175 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5378e428-e641-3d9a-bed5-58bf588f7ca9 | -9.59153 | -46.8827 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b95a026-e051-373b-8fdf-7ea9d1d0bf25 | -7.12801 | -45.50039 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d97208b7-717b-36c8-b4ff-41ec8123d056 | -10.56378 | -44.93583 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 281c2966-21f8-3f70-b28a-f69682e9d4ba | -12.36704 | -48.12724 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d9700bb-0de1-3bca-860c-35c2da638d98 | -6.01956 | -48.12482 | 2025-10-25 04:19:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac99775f-e810-314f-9e29-9a6c098614f3 | -7.54682 | -42.51717 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45c091a9-0742-3e1e-9571-7eaa19f80363 | -9.71282 | -45.42296 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20cdcc3e-2f0f-3204-82d1-6b2793ca50cf | -10.2689 | -43.96982 | 2025-10-25 04:19:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f74bf36-9acf-3c13-98f1-ef72d96dfacd | -13.2891 | -47.49542 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a441ac3-eb37-3847-a5e4-c1ee9f5061de | -12.25193 | -47.4468 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07493aa7-85c7-321e-b001-266b2d231ba4 | -12.21088 | -46.50871 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecc9a89f-5c92-3617-9a6a-439a9ee5f816 | -7.84875 | -46.42611 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6faed0f-a50b-36fa-ad18-0a145cba8d7e | -5.70926 | -49.30907 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a546a97-df32-3f42-b3ab-4d73b91e1a4a | -9.25242 | -45.58394 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63731aab-3ae8-3825-b456-785f7467045a | -12.07214 | -46.39911 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34db49b8-9fb3-34e9-b290-8630be8dbbf0 | -10.64298 | -48.06438 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 805d6da0-45e5-3af6-9015-7d5b55b79b0d | -7.54276 | -42.52049 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8d6501b-5f45-3166-a849-de00a910fefb | -6.11593 | -48.10644 | 2025-10-25 04:19:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0272d556-3c4b-37bf-9a0d-47bec79042d1 | -11.57429 | -51.4722 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87718525-d77b-3bab-81fa-1172133b39d7 | -8.59729 | -44.82718 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a6e79f-8141-3e04-8598-da812fd82d09 | -12.05719 | -46.40752 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d107613-5875-333a-a5fb-86f76d29e0a0 | -10.89739 | -48.03762 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1284a78d-bf74-3860-a31a-5773770149fb | -12.82719 | -47.25775 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 068a6240-67a3-3c89-b64f-87c9bd2afcaf | -10.65979 | -48.07138 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9443ff4a-e03b-398b-b0cc-6307fe93d829 | -9.32621 | -45.18201 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96185a27-3eb9-3713-98e0-4d5adc508f83 | -12.07764 | -46.40727 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a896eb48-4297-36c5-b5ae-6becb0ce9778 | -6.25898 | -47.02909 | 2025-10-25 04:19:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d23f1902-9e3e-3fc5-9bf2-ed835a596807 | -13.42044 | -47.95877 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f49c64f1-534c-3db1-b929-27bc5f95758a | -8.33372 | -46.18299 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 816fd18b-7187-3205-844f-ae488fefad32 | -9.28774 | -57.54705 | 2025-10-25 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5707f0cb-d4ef-3388-a2ee-6ce632406d5e | -6.85587 | -46.29004 | 2025-10-25 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad67143c-b1d3-39be-b644-2fbaf33f32d5 | -11.32462 | -53.93763 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20892a75-4a5b-3fd7-9729-28489d6b12ea | -1.30424 | -49.33816 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56f80080-4d0e-366d-9aa9-edfcce5adbdc | -6.64054 | -46.12555 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd05310a-b503-3620-9406-8d52fbfcbe08 | -7.15235 | -44.12154 | 2025-10-25 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3d4bd74-1cd8-37fa-9eee-3796508519ec | -6.90911 | -45.16899 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70e5d2a5-5c19-39ba-8ca6-5d356cfe7311 | -10.89382 | -43.8246 | 2025-10-25 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73b7c040-e16c-3a66-9296-ef75511ba701 | -13.04023 | -47.208 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc4c64c8-cbf2-38f3-aa91-518451304acc | -6.9196 | -45.16711 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90ae2e3-2ba3-3556-93d9-d9c68df8ad7e | -11.36409 | -54.32611 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08444ac-2f1b-3244-87e2-fa0093120f28 | -9.11297 | -50.40096 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e22325-0af8-3bc5-8cc0-990e879211e7 | -13.06379 | -47.56411 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdf8c929-4956-34d4-9be9-cf9608936851 | -10.84774 | -47.91777 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a13390f1-451a-33b8-a44a-58f7a275732c | -7.48693 | -47.0322 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fa6e520-b67e-31cc-b082-f9f1f3aadf1c | -12.31085 | -43.8493 | 2025-10-25 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94abc262-1f89-32fa-b692-8c79762bdc5c | -12.70391 | -46.3367 | 2025-10-25 04:19:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 082a7562-edba-3922-b6d1-0b4619e923ec | -12.71692 | -46.9138 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70812fc2-77e4-3941-8612-6e24875bae53 | -12.79338 | -48.67447 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04005de9-04b5-3da6-935f-cdf3e5e70f51 | -10.87104 | -48.04522 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef54154e-a789-39bb-a7fb-2d165aa35e06 | -6.91794 | -45.15612 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e03f7f2e-1582-3d98-9991-c2cff0e7f98e | -8.61059 | -54.66072 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c323b0f-98f3-3231-a0d9-fe0f9469f5dd | -10.4144 | -44.50013 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f96e7e8-df9d-3ce0-9122-843f888d0038 | -11.06203 | -49.62097 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84dc03f3-cee7-3d0b-9624-d6ead14779d1 | -12.87135 | -48.60047 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fd37d8e-3a7e-3fec-96d5-6af7223ae2d6 | -9.98764 | -44.16251 | 2025-10-25 04:19:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b128664f-02a6-3276-a2d3-7f2bbc20a172 | -1.33171 | -49.11609 | 2025-10-25 04:19:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07419f68-cc4b-3cec-88ae-f339fbbccf57 | -10.66811 | -48.06456 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dd1c809c-0acd-39a2-bc23-b13bebd090b1 | -10.56439 | -47.99128 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3128313-52a6-3e20-9bd0-6d34924cff6f | -5.69897 | -49.32166 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68885b92-05e3-3b80-838b-2475ddfa788e | -7.06037 | -44.49085 | 2025-10-25 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58ab1ddb-a925-369b-97b3-d3192c9b1281 | 0.27869 | -51.3967 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b2b2d72-f03a-360a-9d33-ffd46c3d13e7 | -10.1104 | -47.77063 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd72dbf9-a69f-303a-831a-270e5b170896 | -9.23919 | -45.58184 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6991fdaa-b115-3560-95f6-7324702145f2 | -10.51526 | -47.67353 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db0b0f6-7f80-3f93-afb1-24bd9bb095ee | -11.75182 | -44.65066 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acc169ad-9e0a-3be1-b21b-12ba5ba42e68 | -12.17936 | -43.60947 | 2025-10-25 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa5fd16-294b-3fd9-ad90-b92d4b70cea6 | -8.33984 | -46.18767 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0ac78b2-48cd-3990-81f0-36066698312c | -6.24665 | -46.39375 | 2025-10-25 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c379c78-1bad-329e-bd5e-66ac12aa153a | -12.10425 | -52.49422 | 2025-10-25 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52d51fd3-5c02-3b96-ad75-d62f60c5b4b1 | -13.35827 | -47.42083 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fa729a5-b120-36c5-9eb4-029397087aa0 | -7.54335 | -42.51664 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c25ff55-15b4-3097-835e-735c4435bd47 | -10.64585 | -45.23658 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c9e699d-ab5f-372e-9c65-00c1544170ed | -9.28183 | -46.99907 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 413a82be-13a5-3eb5-be2e-c4ba6443a242 | -6.80893 | -42.39731 | 2025-10-25 04:19:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f188d14e-b0b3-3e56-bd1f-4bd1e4bedce4 | -9.31961 | -45.20235 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5340fd-b803-3811-b073-39c54f08c1ff | -6.96296 | -42.53204 | 2025-10-25 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1f503e3-e75b-3b16-a4d6-466faed26a26 | -7.73323 | -45.32916 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14a39691-eaeb-33b6-924c-70ac812c62e5 | -6.23862 | -46.40004 | 2025-10-25 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3786aa6-1fd8-39ab-81fe-0585efc9351f | -12.05819 | -46.44391 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb6b4621-09ed-323e-87d5-dcbd21b40e63 | -8.12973 | -45.48552 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3943536f-0210-32fb-9322-7a65f2fa87ff | -7.39324 | -43.90453 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c19a88aa-2ad4-338a-aa75-390ee5294403 | -10.74135 | -51.68522 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
