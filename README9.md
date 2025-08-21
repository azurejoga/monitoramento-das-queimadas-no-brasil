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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5fa3203-6256-3e90-ad21-eea32c951348 | -13.0317 | -45.1724 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 7db0dd54-3768-3c25-9c37-9f6ff4d86b79 | -13.0312 | -45.1957 | 2025-08-21 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 227bc2c3-ec65-358d-b25a-f00cbd18b9a6 | -14.9999 | -54.8343 | 2025-08-21 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f2486a15-9c5e-3cf3-92f0-3dea054a0645 | -7.0354 | -44.6167 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 295.2 |
| d3a19b99-85e8-3de4-8c5d-41c1cf3b5c3e | -8.8737 | -62.3925 | 2025-08-21 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a1eca706-a5b1-3542-8e0f-561eb2dccef3 | -14.8538 | -47.9504 | 2025-08-21 02:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 251e266e-51dc-3506-9eb3-ca5140634d72 | -7.0352 | -44.6396 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 939446a3-ce2a-341b-ba4d-f7a9ddbe9335 | -7.0164 | -44.6413 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 332.9 |
| 7b93d3be-ba94-3f94-b3c2-f4c06eb1d70f | -14.8543 | -47.9279 | 2025-08-21 02:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 32601675-51b6-37f0-b84b-eadea1cbecae | -7.0169 | -44.5954 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| d7ba97e3-fc7e-3c92-811c-8a4b4b9c50f3 | -8.8551 | -62.4123 | 2025-08-21 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6f21d808-023e-326c-bca2-bb7ec6fc8349 | -7.0166 | -44.6184 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 789.0 |
| dcda86d6-b582-3628-855e-5ec947e55c57 | -8.6157 | -62.1374 | 2025-08-21 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2feab393-ca47-3093-ab44-08a0b69b83c8 | -11.5793 | -47.0043 | 2025-08-21 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| be95417b-fe6f-3e1d-891d-8c3deae70155 | -15.0193 | -54.832 | 2025-08-21 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 622be268-7c08-3abb-81f4-724fd4ac53d1 | -8.8735 | -62.4305 | 2025-08-21 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 54448402-df7b-328e-8c60-000e081ee85a | -8.8736 | -62.4115 | 2025-08-21 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e05995de-3658-3c33-a7ef-afd4979b21b8 | -7.0357 | -44.5938 | 2025-08-21 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c27637da-6e85-344e-907c-5eafc29c7b68 | -8.8922 | -62.4107 | 2025-08-21 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 549eadc4-2b10-3c71-b199-9d71c3af0303 | -8.8737 | -62.3925 | 2025-08-21 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| cb053ccf-0dfc-39a9-a046-6c5afb476e86 | -13.0312 | -45.1957 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9b449128-bcd5-39b0-9a1a-a02df459cbd2 | -13.0123 | -45.1756 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| fd93a8bf-aea3-38c5-bffa-e4cb512bedfe | -14.8543 | -47.9279 | 2025-08-21 02:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d18d0012-bd43-37c1-8569-a01f102e2ae2 | -10.4047 | -59.372 | 2025-08-21 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| d0aaeb5b-dd01-37b3-8a2c-bb197813f445 | -13.0128 | -45.1523 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 05ed444b-fc6c-3508-95cf-bb8968ba20b8 | -8.8735 | -62.4305 | 2025-08-21 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f3fa4dfb-92de-3267-9078-ec02bad190a9 | -13.051 | -45.1693 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c8bb6828-f3a3-300d-9509-b929a67a17ca | -13.0317 | -45.1724 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 976cb7fe-fd9c-3ac4-a717-57f9954756f9 | -13.0321 | -45.1492 | 2025-08-21 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| e2d8e0b2-fe99-3b23-a1b4-46e6bc05403c | -14.8538 | -47.9504 | 2025-08-21 02:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 883fba59-b892-31b9-b5e8-6aa7269aaf6c | -8.8736 | -62.4115 | 2025-08-21 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 49e8a0e2-4066-3406-b945-08a78d2fc107 | -8.8922 | -62.4107 | 2025-08-21 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a23601cc-e5e4-3a96-beaa-2c32f6eacce3 | -6.46637 | -35.17514 | 2025-08-21 02:58:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| bfe5924b-db9b-3e90-8404-18cbe977d7e3 | -6.46037 | -35.17407 | 2025-08-21 02:58:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a4e89d13-6e28-3462-b3f1-92048c15179b | -6.46124 | -35.16927 | 2025-08-21 02:58:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 23816699-aae7-3984-bf6b-40696254691a | -6.46723 | -35.17032 | 2025-08-21 02:58:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 3d49beb3-3e4f-3daa-8e75-97e0b94fdc12 | -10.4047 | -59.372 | 2025-08-21 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| fe6b3714-b7d6-3ac9-b046-cc437fd8622e | -8.8735 | -62.4305 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 108c67c4-2c34-36c4-9110-86c1938cfbce | -11.5793 | -47.0043 | 2025-08-21 03:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c3c8e22e-97ef-34ae-9e13-ea047830b86b | -7.0169 | -44.5954 | 2025-08-21 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3f89181c-8699-3cb6-9cbe-2bc9787d4a98 | -7.0164 | -44.6413 | 2025-08-21 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 19c06ccd-567e-32f6-a9db-32ef87ad6ef5 | -15.0193 | -54.832 | 2025-08-21 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 3ab92e4d-c00c-3ee7-adfe-1caa6ad12236 | -8.8737 | -62.3925 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9a0af967-d391-38d7-82bd-dd86a1bb79b0 | -14.8538 | -47.9504 | 2025-08-21 03:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 664997e8-c082-3936-be3d-fa53832dcaea | -7.0352 | -44.6396 | 2025-08-21 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8da2c033-e3cc-3544-969c-3fb240e35826 | -14.8543 | -47.9279 | 2025-08-21 03:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0d382b93-5256-3eca-ab98-e0efc2d38e91 | -7.0354 | -44.6167 | 2025-08-21 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 251.7 |
| ea205d6d-19ad-39c1-9595-c1261f444a91 | -7.0166 | -44.6184 | 2025-08-21 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 489.3 |
| 629919c0-9577-314a-a16b-a12d4ee9b03a | -8.8551 | -62.4123 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 00e8448a-b3e7-373c-90eb-749019978890 | -8.8922 | -62.4107 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8c40e80b-d116-3537-afcf-bb96e6fb8a7a | -8.8736 | -62.4115 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |
| a8c72718-b5b5-30c8-b435-1a1126a2fc76 | -8.8552 | -62.3933 | 2025-08-21 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 497dbc4c-7a37-33c1-8c00-a988ac3d6400 | -7.0164 | -44.6413 | 2025-08-21 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 09594af5-1731-3aad-8b60-db45a18765f1 | -14.8543 | -47.9279 | 2025-08-21 03:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c357bca0-511b-360f-8dc6-63bc2fd687f6 | -8.8551 | -62.4123 | 2025-08-21 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 079faf5b-d5d6-3fec-b257-c07cccd96b9d | -8.8736 | -62.4115 | 2025-08-21 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d35f182a-605b-3642-a880-71f9810a0594 | -7.0354 | -44.6167 | 2025-08-21 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 181.7 |
| ad22e1c3-902f-32d3-8118-9e7dfdaab781 | -7.0352 | -44.6396 | 2025-08-21 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ca65d9c8-64be-3a1c-a810-6c76686649de | -7.0166 | -44.6184 | 2025-08-21 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 414.1 |
| 40c46a09-0722-32a5-a85d-3af6c3e428a6 | -7.0169 | -44.5954 | 2025-08-21 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| afc3c35c-e34b-30d2-86b8-6c617d2d7ee8 | -14.8538 | -47.9504 | 2025-08-21 03:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b7c45653-e813-361a-bd39-ddf63cc3ba5f | -8.8735 | -62.4305 | 2025-08-21 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f45cac0a-a1dc-3714-b5d2-0d043b553d79 | -11.5793 | -47.0043 | 2025-08-21 03:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2525fccc-9b90-357b-8c13-c3bd25b7868e | -8.8922 | -62.4107 | 2025-08-21 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 5d819e64-fe7a-3c62-845c-e9213a5cb911 | -7.0164 | -44.6413 | 2025-08-21 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f99e93fb-b233-3555-9b42-9f38638b5237 | -8.8735 | -62.4305 | 2025-08-21 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 86d39e0e-256f-3861-80ac-744211025be4 | -7.0169 | -44.5954 | 2025-08-21 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e1635e9a-07ba-3ccb-b49b-a78b3d4352c4 | -14.8543 | -47.9279 | 2025-08-21 03:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9d2ee5cc-217b-3762-9dcb-6880db9f7764 | -7.0352 | -44.6396 | 2025-08-21 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7e5ac519-b182-3417-9b5e-cf7e750fe8b2 | -7.0354 | -44.6167 | 2025-08-21 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 12da664a-30c7-329e-bee9-026bffbcc71c | -7.0166 | -44.6184 | 2025-08-21 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 334.7 |
| 5576804d-e7d4-3ffe-a1a9-aa65a36fb5a1 | -8.8736 | -62.4115 | 2025-08-21 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 112f290c-d555-36d3-a7a1-ddf0479c0944 | -14.8538 | -47.9504 | 2025-08-21 03:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 1402959c-a4d0-3345-b2ef-5cfdb8431623 | -7.0169 | -44.5954 | 2025-08-21 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 505305d1-b87a-3ae4-9039-9e0a5a4724ce | -7.0166 | -44.6184 | 2025-08-21 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 309.8 |
| a07c1bb5-c338-332f-b8bf-fe61fd4bb7a1 | -15.7484 | -49.9365 | 2025-08-21 03:30:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| cd87f8f2-29d5-331f-8aa6-21bf3be2c1bb | -15.748 | -49.9586 | 2025-08-21 03:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 59fd3928-063c-3a48-b7d5-80ce54a139a2 | -8.8735 | -62.4305 | 2025-08-21 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d2b5b715-05b1-3bf8-bbd4-8eed7310a866 | -7.0352 | -44.6396 | 2025-08-21 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 9f7869b6-9d48-3ce5-a677-8a04327089c2 | -7.0164 | -44.6413 | 2025-08-21 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| fbce1155-f6b6-30a4-8af0-701a0684c5f7 | -15.7289 | -49.9397 | 2025-08-21 03:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| a35464a7-8281-3562-a16d-21db390e3a27 | -8.8736 | -62.4115 | 2025-08-21 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 32899d86-a923-3ef3-ac20-37e132063ad1 | -15.7284 | -49.9617 | 2025-08-21 03:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 8f92df40-e9d8-3a55-a631-6aedde8ce6e1 | -7.0354 | -44.6167 | 2025-08-21 03:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 8821a4f8-11f2-3bdf-a3b8-e94f67097a3d | -8.8736 | -62.4115 | 2025-08-21 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| bbc3e933-aa25-39e3-9edf-a2eb1e24ae00 | -7.0352 | -44.6396 | 2025-08-21 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c5147a54-dfbf-3220-bc9f-bafde03aeb38 | -7.0169 | -44.5954 | 2025-08-21 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3c41d0a4-340d-34c8-8835-735f599bd6d7 | -7.0354 | -44.6167 | 2025-08-21 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 269.1 |
| f9508820-6a62-3584-ac4d-968a7ca954ef | -7.0166 | -44.6184 | 2025-08-21 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 351.3 |
| dc3301a4-f030-3a77-9350-33b9c0da6d5c | -7.0164 | -44.6413 | 2025-08-21 03:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| da62de37-f7ab-3f83-89e5-3b92b8d2bf3f | -8.8737 | -62.3925 | 2025-08-21 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a2fe9083-0abb-30e9-99c0-5ebc411cb049 | -8.8735 | -62.4305 | 2025-08-21 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 1f3988ae-b3a4-3744-8e1b-4db555a07289 | -6.59347 | -41.3907 | 2025-08-21 03:47:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 228235a8-6d8b-3886-aa0f-03e7578aef3c | -5.84226 | -38.36049 | 2025-08-21 03:47:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b5fd130-1ba9-38e9-b433-3da38572a5d0 | -5.06685 | -42.65821 | 2025-08-21 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c643dfb4-8ffe-34ca-b4e3-28c3bcbf6aa5 | -5.10756 | -43.16459 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 404d32d8-af69-320d-902e-ef3d1e8161d7 | -5.78625 | -45.07184 | 2025-08-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9b41131-0f85-3e3b-af82-fb317df4be60 | -6.19701 | -43.57214 | 2025-08-21 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9feb02e0-d502-3f71-824b-18ff26771654 | -5.04919 | -43.05657 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9786abda-e97c-31a7-b14a-7b3f77d5c26f | -4.64882 | -43.12163 | 2025-08-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README10.md)
