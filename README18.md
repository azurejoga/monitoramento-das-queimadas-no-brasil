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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bf1a43f-91c5-36d9-9bfc-f99441e43b9f | -16.07987 | -58.50909 | 2026-06-30 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1a371882-6602-3e52-be2d-9b5d481897e8 | -21.31966 | -48.54199 | 2026-06-30 05:18:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16b1355b-a951-3ebe-882c-8008facdd3ff | -17.44079 | -47.16631 | 2026-06-30 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d949a427-c299-3f73-960e-391009987092 | -16.19611 | -59.32001 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 844b5973-e377-35f1-994e-69c776d5d39c | -15.40368 | -59.4999 | 2026-06-30 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e150d86-34eb-395b-8217-9e6c65f09335 | -18.38064 | -55.72139 | 2026-06-30 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 549b7e7a-4f36-36ac-8f05-645f1428f8fc | -18.24497 | -53.84899 | 2026-06-30 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d5f2ef1-8e53-3470-b818-780cd8423912 | -15.37277 | -59.28703 | 2026-06-30 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 479f62de-e7f6-37ce-8cb0-23759b5b3273 | -17.70906 | -46.78159 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9bf52f3e-32aa-377b-b95b-0a3349617466 | -17.71124 | -46.7837 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82cb13c0-7a1d-382b-a0ae-21d42519f34b | -16.19666 | -59.31642 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55f99728-bd75-31dc-9db8-eb24c7f5ed0e | -18.24114 | -53.84417 | 2026-06-30 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d157fdcc-4828-39ef-98c0-cbb28c8d63c4 | -16.19111 | -59.33023 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1e625bd-c833-3990-8ada-6dd46812bdb9 | -21.31332 | -48.5414 | 2026-06-30 05:18:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd70cc22-0b47-350f-826a-5aedaa36ecc0 | -16.17286 | -59.33823 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec8c95ad-569c-3fdf-b1fb-d8e18bb7df12 | -17.70848 | -46.78775 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fec95ea2-dfb0-32be-9e91-c38f26c5c891 | -17.91052 | -52.72076 | 2026-06-30 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13581a6e-9fc3-30fd-a474-de287ef3fd66 | -16.07707 | -58.50487 | 2026-06-30 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d7f2517b-5c05-348e-8c11-489ffba0c828 | -17.44287 | -47.16164 | 2026-06-30 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1df4696c-44ea-31a9-a351-d0ee01377f72 | -17.70791 | -46.79378 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 98d40be7-b4cc-3df8-be3c-0943026f761b | -18.246 | -53.84059 | 2026-06-30 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 720385a7-2a88-30d5-be47-9b82521737fb | -18.78085 | -57.34832 | 2026-06-30 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 29d4fedb-e07d-36b4-880d-226a6d2b0ad0 | -18.24549 | -53.84478 | 2026-06-30 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fedcb6f6-29cf-3931-8a9e-5ae80c83f8f8 | -17.44233 | -47.16731 | 2026-06-30 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6cbb8dab-89d1-311f-a269-9e4b08a45526 | -17.70966 | -46.77526 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6a0a925-ecf3-3aa8-8e4b-890da4288e0f | -17.70451 | -46.78248 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ed3371-a5eb-31ab-9739-91a9e8a5d75f | -15.37608 | -59.28758 | 2026-06-30 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b21f2f-751c-327d-82e0-33bb55b4eb23 | -17.70233 | -46.78043 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9241bf57-3f7f-3e8e-b4cd-22519c6bdb49 | -18.79566 | -57.37233 | 2026-06-30 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 765884ca-8de4-3b1c-b7f5-6b10a485598b | -16.07372 | -58.50433 | 2026-06-30 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 49b1bd82-6255-369d-ade8-cbe943773dea | -17.71071 | -46.7898 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 81a859c4-5fc0-3367-8e00-2516b51d21b4 | -18.77729 | -57.34777 | 2026-06-30 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0b3b1ee0-931a-3c7b-8d1b-233d69039339 | -17.44129 | -47.16062 | 2026-06-30 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bd9744c-352d-3181-8493-ed922ecf05d9 | -18.24446 | -53.8532 | 2026-06-30 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e30fd720-ae14-3815-b3b6-33e5b2de9146 | -17.70506 | -46.77624 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29f9e30e-3f67-3a06-9bbb-b7944e8410ec | -21.31595 | -48.54395 | 2026-06-30 05:18:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2976572-b322-3d38-be4b-7e86ae1e3b6c | -10.9397 | -43.0593 | 2026-06-30 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b910842e-d422-31db-9689-5c86da5b1f01 | -10.9209 | -43.0384 | 2026-06-30 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8261763f-e01b-3158-bcdb-a1534d0fc96b | -10.9593 | -43.0326 | 2026-06-30 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bf335596-0cfe-3051-ab9c-ba96ea0bb902 | -10.9401 | -43.0355 | 2026-06-30 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 9b58764c-82b9-35df-b7c3-449d52762e29 | -22.78975 | -49.34695 | 2026-06-30 05:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7e9d39f-c530-3d9d-8453-893a01bd2f41 | -10.9401 | -43.0355 | 2026-06-30 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| c38859ec-8e94-3146-b8e5-b9a9afa82eae | -10.9397 | -43.0593 | 2026-06-30 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 13a73979-afa4-3092-82b7-8eaf88c34686 | -10.9593 | -43.0326 | 2026-06-30 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b86740ff-a2ad-3dc1-8ae7-a6406ba316e7 | -10.9209 | -43.0384 | 2026-06-30 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5b4af32f-9908-3974-815e-2f03c610dd0d | -10.9401 | -43.0355 | 2026-06-30 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 8511ed03-441e-3614-bf81-719b69221c9f | -10.9593 | -43.0326 | 2026-06-30 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 59ad6ff3-393d-3b63-be80-dc1b732a35b4 | -10.9397 | -43.0593 | 2026-06-30 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 650a9219-998e-39b1-bd86-f879a175fb8d | -10.9209 | -43.0384 | 2026-06-30 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b2e1ede0-5f0c-3164-a33c-251538f22f2a | -10.9405 | -43.0117 | 2026-06-30 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 740278d0-24fc-35ce-94cf-365ce7dcca82 | -10.9397 | -43.0593 | 2026-06-30 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| d9b1173e-cf04-3fc5-9e51-4856de6be0f6 | -10.9401 | -43.0355 | 2026-06-30 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.8 |
| 90be76e2-55f5-3e29-a620-a18d30a1f855 | -10.9209 | -43.0384 | 2026-06-30 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 5d565c5a-23c7-30e5-9283-bb18e30bd48c | -10.9397 | -43.0593 | 2026-06-30 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0d4235fd-0731-3815-8a0d-9b55909104c9 | -10.9593 | -43.0326 | 2026-06-30 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3d17d4de-0ef2-3112-b09e-3ae73d15a7a5 | -10.9401 | -43.0355 | 2026-06-30 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 272.3 |
| b733a3d4-5c1e-3c25-8b78-a4843b475f78 | -9.61105 | -56.93184 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a70344b5-fc69-31ee-afa3-13961ac9b98f | -12.44775 | -58.48797 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e7b6f79c-a010-34ca-b4b6-3d11a42ec737 | -9.607 | -56.92958 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 13d2b6c2-4cf0-33b1-8420-64cfac8fd3f5 | -9.20289 | -63.52634 | 2026-06-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3eeafc0-5ad6-3cc6-85ce-9e5cf5c32cb4 | -9.60073 | -56.92186 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36f71af2-67a1-33af-a591-0c4568032059 | -12.44652 | -58.49933 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c18d3584-2ae8-30f1-94b3-6be81b31148e | -9.15744 | -58.29382 | 2026-06-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6654b876-1313-3e24-840d-c170163e5744 | -9.6062 | -56.9363 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1966c535-cead-32cf-9520-998f064468e1 | -9.32275 | -58.01948 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc26c81e-4af6-36e5-8b82-7f6d12f1db30 | -11.9353 | -57.71164 | 2026-06-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a4ce75e-4c57-3b7d-b196-d7371fdf646b | -9.60783 | -56.92265 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d2ae6f70-254c-334d-b3d0-502f8d603009 | -9.60474 | -56.92407 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1f6fc9a2-b609-3e87-b6d5-f684f099b273 | -11.93599 | -57.70493 | 2026-06-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33d89a2f-636c-32a6-b6a7-b4aef6029c62 | -11.93617 | -57.70768 | 2026-06-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de287e78-fd7c-3d59-8b9c-76145c9ee6a9 | -9.08602 | -59.39526 | 2026-06-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bfa5fc6c-c060-3ef4-adf8-ed13bdc3ea36 | -9.32137 | -58.03099 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ded9d5d1-deee-3c4a-8f50-34bc5b46f0b6 | -9.60397 | -56.93092 | 2026-06-30 06:01:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e9794fbc-6c9a-3fa1-b99b-0817598debb4 | -9.09208 | -59.39606 | 2026-06-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc6533f-757a-37fd-a8aa-fbd8f3361786 | -12.45319 | -58.5002 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b7393115-76d2-308d-bf3a-ab3c0f55567d | -11.9004 | -57.37928 | 2026-06-30 06:01:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a7c69e3-beec-3914-987d-d5372143780a | -9.32867 | -58.02619 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1b76d23-09af-39ba-b28d-ea413932e647 | -10.29742 | -57.13414 | 2026-06-30 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f0ac735-c236-32db-a438-3e109821aa4d | -11.9603 | -58.61577 | 2026-06-30 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d515d76c-6587-3a38-b451-4373f2ae610c | -8.87636 | -63.93233 | 2026-06-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58a91ea4-f3e0-3602-8418-b8a2eff45217 | -9.15749 | -58.29555 | 2026-06-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 31b87bad-ef0f-3a6e-bdd3-41438968ac02 | -11.90746 | -57.38027 | 2026-06-30 06:01:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c436b1ea-afb7-3749-bbfc-ee9344d4933d | -12.45443 | -58.48884 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3dc3308f-631c-351d-870e-700952c0856b | -10.29822 | -57.12713 | 2026-06-30 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2060493-ab25-38e2-a1a8-46a99989914b | -9.32798 | -58.03194 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74bf4c86-0fec-3e06-9576-375052ae5bdf | -9.15026 | -58.2984 | 2026-06-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1185345-3bcf-3dd7-baf6-f5536a2713bc | -12.45381 | -58.49454 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 937d24c9-d888-329f-bf7a-fb354d248623 | -10.06551 | -60.49662 | 2026-06-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9249d242-00a0-3986-b898-385bd9aa4f55 | -9.15676 | -58.29928 | 2026-06-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9222348e-92ea-3abe-af30-9ebff9d35625 | -9.33007 | -58.01452 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cdbff33-7e91-3ee9-9a2e-ad1139c016c7 | -9.32937 | -58.02033 | 2026-06-30 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec465923-7b11-3544-b3ef-728c16221a3b | -12.44713 | -58.49365 | 2026-06-30 06:01:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 40ceddf6-163f-39fd-b5ce-45a1963b3dab | -10.07124 | -60.49739 | 2026-06-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96b9eb8-5ae1-3a7f-bab6-5d32e17442c3 | -11.90643 | -57.41381 | 2026-06-30 06:01:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ada07dc-c58b-347d-b992-b2a2ce85f9b4 | -11.93544 | -57.71431 | 2026-06-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fed7a030-2d40-31af-87b9-831a7063b2c7 | -10.9397 | -43.0593 | 2026-06-30 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d7767952-f064-33ea-ad12-a83d8d41c6a6 | -10.9401 | -43.0355 | 2026-06-30 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 280.2 |
| cd34da30-797e-3c0e-960c-cbf506b123f5 | -10.9209 | -43.0384 | 2026-06-30 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| c80a7638-109e-3696-9a6a-beaaed3faa9d | -10.9593 | -43.0326 | 2026-06-30 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bb7a262c-39d3-354c-8b0f-b1095f591849 | -10.9401 | -43.0355 | 2026-06-30 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 288.9 |


[Clique aqui para ver as próximas entradas](README19.md)
