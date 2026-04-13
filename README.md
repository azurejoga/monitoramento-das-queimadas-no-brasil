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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df906f71-e4a6-3113-bcb9-b4ef757587f5 | 3.3274 | -61.2344 | 2026-04-13 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 462c0ff1-9345-3329-9246-0e3fac03e444 | -11.8105 | -43.637 | 2026-04-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1f5c2767-0314-3f3f-9865-334c3196592c | 3.3092 | -61.2347 | 2026-04-13 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6f249522-7a1f-35ac-a5fa-9af0e5b8e5eb | -11.7913 | -43.64 | 2026-04-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b904aab8-b8ad-39da-a770-012b0f3b6ff1 | -11.811 | -43.6133 | 2026-04-13 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 48ec2ac9-4d5b-31b8-b054-a48b5dc320ce | -11.8105 | -43.637 | 2026-04-13 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| ca3e3a4d-cd22-3cba-9fdb-76595d556daf | -11.811 | -43.6133 | 2026-04-13 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 62c10ac9-9558-3480-b110-bac222234a68 | 3.3092 | -61.2347 | 2026-04-13 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 70c041d8-c00b-3b31-81d7-d78314323e24 | 3.3274 | -61.2344 | 2026-04-13 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3f0555b4-ebe3-3084-8112-454d16b90897 | -11.7913 | -43.64 | 2026-04-13 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 824a6f70-2164-31ec-84e3-ae7ddca34cfb | -21.25341 | -48.57492 | 2026-04-13 00:16:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b6ca21c1-fc7b-3e89-a25b-2c634f5dda65 | -22.28425 | -48.09046 | 2026-04-13 00:16:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9a4a2c56-2a10-3607-9051-95bcae4f212e | -21.2547 | -48.58506 | 2026-04-13 00:16:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 97ab2236-fb99-370c-9eac-288c21dbde02 | -15.31646 | -46.82918 | 2026-04-13 00:18:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2543cae7-51fb-396d-b88e-b24fc4c4411c | -11.79109 | -43.62392 | 2026-04-13 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c9aeead5-fb55-37eb-973a-4c748f235d84 | -11.79372 | -43.64034 | 2026-04-13 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e33dc32e-5a65-3589-8d57-8d5b717a296d | -11.80534 | -43.63844 | 2026-04-13 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 5c3b9a6b-73db-327b-9232-5994f1d2bea6 | -11.80273 | -43.622 | 2026-04-13 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 24eeab05-e20f-3035-b115-af044718ef85 | 3.3092 | -61.2347 | 2026-04-13 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b6192a0f-fa73-35e4-a8f9-4517d5554613 | -11.811 | -43.6133 | 2026-04-13 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 864991b0-0e0a-3549-861b-e61b1dbcf341 | -11.7913 | -43.64 | 2026-04-13 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8146b8e1-fd2d-3638-890f-ead2bce86479 | -11.8105 | -43.637 | 2026-04-13 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ef70c475-0a72-3f8d-ad90-1b83340c35a3 | 3.3274 | -61.2344 | 2026-04-13 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4de96390-a965-37e1-b705-15cb708cecfe | 3.30408 | -61.24333 | 2026-04-13 00:22:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 792973ee-ac62-3155-a897-63574b87336c | 3.32665 | -61.24036 | 2026-04-13 00:22:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| bc730815-62f0-3762-b0ca-4a991db7df1c | 3.31993 | -61.24569 | 2026-04-13 00:22:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 61c9d0aa-57af-3152-bad9-65fcf3685734 | 3.31082 | -61.23783 | 2026-04-13 00:22:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c6e4e714-4f8f-3b63-b3cc-5f128ef7da69 | -11.7913 | -43.64 | 2026-04-13 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9d8a8d1c-160d-3458-a360-6dc76a3bb9bd | -11.811 | -43.6133 | 2026-04-13 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 9318da76-7e9e-331c-905b-9ceec76eff7b | -11.8105 | -43.637 | 2026-04-13 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bc7a5190-da71-3069-b147-2450c407cafa | 3.3092 | -61.2347 | 2026-04-13 00:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| cf58aa02-fea7-3d79-9c3d-25f9adeaad61 | 3.3274 | -61.2344 | 2026-04-13 00:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4ea06bc3-1c63-34dd-af21-6ff2e55fedbd | -11.8057 | -43.629799 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd4dc75e-3811-3b58-af9e-c9041f49b58e | -11.8039 | -43.622398 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5062e44a-4b58-3c4c-8d22-9ec2ec6568a1 | -11.7976 | -43.639599 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba8242c0-a022-34de-a70d-49000aa39eb4 | -11.7959 | -43.632198 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4dcfc318-5519-306d-9432-a00ff576dd2a | -11.7941 | -43.624802 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d2f34a8-2555-3b2f-8257-2273303f0162 | -11.8074 | -43.637299 | 2026-04-13 00:30:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b748d5c-00ee-3186-a982-98ea973681b4 | -11.7913 | -43.64 | 2026-04-13 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 238df333-a966-3716-b512-2d3a0c8d79f8 | 3.3092 | -61.2347 | 2026-04-13 00:40:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 185fa2be-c74c-3419-a42f-dc61745fb6fd | 3.3274 | -61.2344 | 2026-04-13 00:40:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 27bcc26b-5a1f-338c-afff-1a8417f945cd | -11.811 | -43.6133 | 2026-04-13 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| be614094-ceef-3ed6-afe7-db2f726faceb | -11.8105 | -43.637 | 2026-04-13 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ede7d959-b696-31da-b27d-01bfec97de88 | -11.811 | -43.6133 | 2026-04-13 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e4f35bb9-e682-3413-a3bb-3bfd3530641d | 3.3274 | -61.2344 | 2026-04-13 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| acba4e3f-8696-30b0-9b6a-62e71279ad57 | 3.3092 | -61.2347 | 2026-04-13 00:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e605f8a5-7985-3c40-8725-00a207e1f16c | -11.8105 | -43.637 | 2026-04-13 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 25985e0b-d549-3344-8cf8-82120750bfdc | -11.7913 | -43.64 | 2026-04-13 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0e8806e1-e1a3-3eee-98df-46d5da06c036 | -11.8105 | -43.637 | 2026-04-13 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| debfa81d-6e3a-33a2-9fd6-3c98dc40c57b | 3.3092 | -61.2347 | 2026-04-13 01:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c4c4212c-1060-38cd-aa36-2f3ec602fe18 | -11.7913 | -43.64 | 2026-04-13 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8b67632b-a53a-3880-882e-4778cb68f341 | -11.811 | -43.6133 | 2026-04-13 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 67dd50e3-1897-3b16-b4f8-72bb3a0f7f48 | 3.3274 | -61.2344 | 2026-04-13 01:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1b2d8fc2-0f31-3833-97d2-c18a091470c3 | -11.7913 | -43.64 | 2026-04-13 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ee5ee6d0-a935-37bb-8366-ed7dd29581b3 | -11.811 | -43.6133 | 2026-04-13 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4d4f0871-dfd8-354e-9d12-cac9e75e779b | 3.3274 | -61.2344 | 2026-04-13 01:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3c2d95a3-b4bc-3e1b-a196-97d3c8331ade | -11.8105 | -43.637 | 2026-04-13 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| b68bd00c-a930-3d1a-98e0-31deea1caffa | 3.3092 | -61.2347 | 2026-04-13 01:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 12cb6764-7541-3b53-b260-875f8bc3ee14 | -11.7913 | -43.64 | 2026-04-13 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 63168169-eb7a-3ed6-8f7a-b9e9affe7942 | -11.8105 | -43.637 | 2026-04-13 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 7fa1b342-8206-3d54-b39d-d304f78a4db1 | -11.811 | -43.6133 | 2026-04-13 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b11e3633-b5f3-3684-8f2d-200da0d70d43 | 3.3092 | -61.2347 | 2026-04-13 01:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| c84ccb6e-e28e-3cca-b5f2-219e476c9a06 | 3.3274 | -61.2344 | 2026-04-13 01:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 21baf4f1-f2e3-3f6c-bc8c-51f1d45b0fdf | 3.3092 | -61.2347 | 2026-04-13 01:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c699a3fe-38e0-3472-a6b9-921e89f44582 | -11.811 | -43.6133 | 2026-04-13 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| bf0f900e-fa9f-349d-a4ba-4355c417d66d | -11.8105 | -43.637 | 2026-04-13 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| f106824f-21c2-35ad-9610-ee336089db25 | 3.3274 | -61.2344 | 2026-04-13 01:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 640a56e8-79aa-3ea6-8a23-c450a0100e2e | -11.811 | -43.6133 | 2026-04-13 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c73bcdd8-cfa8-38bf-9b67-b02901a8ebab | -11.8105 | -43.637 | 2026-04-13 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 533c9873-cffe-34ab-b31a-aeba7338e978 | -11.811 | -43.6133 | 2026-04-13 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2e96ad2a-b2b7-3152-966c-80d88bffc1d2 | -11.8105 | -43.637 | 2026-04-13 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 65aaa283-1f70-359d-ab19-27be7b9217ee | -11.7913 | -43.64 | 2026-04-13 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5ef9f5aa-2651-3b9e-a884-fba10efa6828 | -11.811 | -43.6133 | 2026-04-13 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8ff1735e-f24f-3539-b827-9ed7a3ebf7fe | 3.3092 | -61.2347 | 2026-04-13 02:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 48d92222-6ebd-37cf-87c8-75fdd77a75a3 | 3.3274 | -61.2344 | 2026-04-13 02:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 52cd3f8c-9577-37b2-a90e-24a43970c9e4 | -11.8105 | -43.637 | 2026-04-13 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| a50c1c06-37d9-3779-8388-d9a86e3da55f | 3.3092 | -61.2347 | 2026-04-13 02:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 34.4 |
| e8c44d37-824d-3421-9276-3d92da93bcd6 | -11.8105 | -43.637 | 2026-04-13 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c33f1c60-55a9-3a67-a3d8-49c0ec864575 | 3.3274 | -61.2344 | 2026-04-13 02:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a40b13e5-366f-3f0d-8ab4-eb127a9e16b7 | -11.811 | -43.6133 | 2026-04-13 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2b1e487a-fd22-324a-ada2-1b46283c799e | -11.811 | -43.6133 | 2026-04-13 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e2212361-8496-372a-94ab-fdb056e81db8 | -11.8105 | -43.637 | 2026-04-13 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ea549c6c-162b-33b0-a5e3-c4114e2dc4f1 | -11.8105 | -43.637 | 2026-04-13 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b1a37c72-d82c-307e-86e3-ac68b10dd3b1 | 3.3092 | -61.2347 | 2026-04-13 02:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 32.1 |
| cbb20cf6-ce20-3811-9676-8e2f7fa23f9e | -11.8105 | -43.637 | 2026-04-13 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| db091c81-dcb6-3e3a-aa28-73c34c8810f3 | 3.3092 | -61.2347 | 2026-04-13 02:40:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 321bcccf-278e-3f32-a0f2-22fbc0949024 | 1.1028 | -60.5225 | 2026-04-13 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 204.8 |
| ee1adb8b-0359-371d-a2b3-3aa05c2ab164 | 1.1028 | -60.5414 | 2026-04-13 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 204.3 |
| 7f3a1264-e409-3e90-9f01-7706b0cc9147 | 1.121 | -60.5413 | 2026-04-13 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 470b1307-161d-37d4-a5e0-b8a430f5ff49 | -11.8105 | -43.637 | 2026-04-13 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5d7489c0-1ed2-359d-804c-3eb66e17ae70 | 1.121 | -60.5224 | 2026-04-13 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1718bef6-30c5-3308-baf4-2731e4318102 | 3.3092 | -61.2347 | 2026-04-13 02:50:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 32.3 |
| dc182b17-4df5-384c-ae48-b98aa6b7f624 | -9.79887 | -37.4766 | 2026-04-13 02:56:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 626311f3-f522-3a84-b726-3c48f1969425 | 1.121 | -60.5413 | 2026-04-13 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 753dc0c3-8d6b-3164-9e1e-2ebe422635b4 | 1.121 | -60.5224 | 2026-04-13 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e6263e45-372f-3bd2-a8e3-21d08a57b5dd | 1.1028 | -60.5225 | 2026-04-13 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 356ef7e9-ccd2-37bd-a3bc-fa7dfa20e7e5 | 1.1028 | -60.5414 | 2026-04-13 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 0a57307e-83b1-3a2b-8d83-5c2ce0ab4f23 | 1.1028 | -60.5035 | 2026-04-13 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 2c670b36-2245-3a26-a839-ea69da8baf11 | -11.8105 | -43.637 | 2026-04-13 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4a03218d-036f-3622-80e6-1b5eac51368c | 1.121 | -60.5224 | 2026-04-13 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |


[Clique aqui para ver as próximas entradas](README2.md)
