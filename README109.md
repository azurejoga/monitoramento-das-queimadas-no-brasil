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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20a4ff16-b59e-349a-b699-376a2ea1052e | -12.8888 | -44.5909 | 2024-10-29 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| a7c1108f-64f5-38f7-b531-f1030d7a80cc | -12.8879 | -44.6378 | 2024-10-29 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 25ac5161-0730-3933-a77a-936eb5b66fe9 | -12.6953 | -48.8503 | 2024-10-29 13:36:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1a1e9166-992d-39d9-8731-bea9ca16e9c9 | -12.7145 | -48.8477 | 2024-10-29 13:36:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| a4bc33a2-bab5-3b35-bda8-301d28d84604 | -1.458 | -54.0763 | 2024-10-29 13:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 59d9e176-9706-3e06-a146-e06160c726cf | -1.3932 | -49.0387 | 2024-10-29 13:45:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 636c50e1-7325-3535-9a00-3bc952fc0a2f | -1.3747 | -49.039 | 2024-10-29 13:45:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a48f2511-a6de-31ae-b99c-c3e2bc84a177 | -1.3932 | -49.0174 | 2024-10-29 13:45:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 53dfce75-4777-309b-9cdf-997063655529 | -3.1038 | -42.5589 | 2024-10-29 13:45:23 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2271ffbd-827e-36f0-8151-3324a79f8625 | -3.1097 | -54.2865 | 2024-10-29 13:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 45d2ee60-12ad-3fbc-a5df-7d5b7298e6bc | -3.0734 | -54.167 | 2024-10-29 13:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 80b726ae-9e5a-3ab0-9a90-4732b10b90a9 | -3.6648 | -42.4384 | 2024-10-29 13:45:27 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 66785041-88b5-3f45-806a-8b26978f901a | -3.8556 | -41.8112 | 2024-10-29 13:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 72884dba-90f8-398f-943b-c59b184313de | -3.8225 | -44.1522 | 2024-10-29 13:45:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9944c464-e93d-3ff3-88f3-6e0243e087b1 | -4.3473 | -43.779 | 2024-10-29 13:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 557.7 |
| d339a9d3-a5cb-31e7-8dcb-4ed6899864c4 | -4.8606 | -42.6275 | 2024-10-29 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 90013ae8-7f16-3f22-a4e8-ca85f8045247 | -4.8619 | -42.4622 | 2024-10-29 13:45:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 39406aff-ee8a-3568-af0a-ace133c5f09a | -4.8617 | -42.4858 | 2024-10-29 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| c6b87be5-dfbc-3dce-bb1c-72c8f0b83cfd | -5.75 | -41.7294 | 2024-10-29 13:45:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 676133f1-3e15-305d-a0f7-233a5a7fffed | -6.3534 | -41.581 | 2024-10-29 13:45:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| e0448764-f733-3317-ac69-25b068a9501f | -6.6781 | -44.6935 | 2024-10-29 13:45:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 8c475725-7127-389d-924e-434718bc3361 | -6.9968 | -41.35 | 2024-10-29 13:45:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| bd36f794-a84a-3c19-8bde-ff84b97bd739 | -6.9971 | -41.3258 | 2024-10-29 13:45:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 0aa007e6-0dec-3c31-b5e9-bb00c505eb33 | -7.016 | -41.3239 | 2024-10-29 13:45:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| e3b385d8-3d4d-3446-984c-d982b16f176e | -7.0157 | -41.3481 | 2024-10-29 13:45:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| ddd34adb-2062-352e-a4d5-01a9e4b4d78f | -12.8888 | -44.5909 | 2024-10-29 13:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 57cb7c66-6eab-31ce-bb90-ff5017a33dd6 | -12.7145 | -48.8477 | 2024-10-29 13:46:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 3582980c-117f-3679-acec-c44a1149ea06 | -12.6953 | -48.8503 | 2024-10-29 13:46:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 77661f22-a7d2-303e-a600-cc553254ec89 | -12.8879 | -44.6378 | 2024-10-29 13:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9c429dd6-53d9-3ea2-abca-273ffdb9792f | -12.8883 | -44.6143 | 2024-10-29 13:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 309.4 |
| c62762cb-8f2a-3ace-ba0b-78d83c52d794 | -19.5862 | -56.7136 | 2024-10-29 13:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 6e049fb0-0286-3928-8db8-8c6fc587c308 | -19.6067 | -56.6898 | 2024-10-29 13:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.1 |
| f227e46a-e6a8-3feb-85f1-b878b8d256bf | 1.5838 | -55.6277 | 2024-10-29 13:54:57 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a00e0b89-0219-3d5b-9ab4-9b4a0a7ab37b | -1.4116 | -49.0384 | 2024-10-29 13:55:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 51f75f35-22ee-30e1-97c0-743ab1641993 | -1.3932 | -49.0387 | 2024-10-29 13:55:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7832222a-c5ab-3cc9-abba-18041fa36e63 | -3.1038 | -42.5589 | 2024-10-29 13:55:23 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1e8812ca-d41f-3dbb-a889-dfab372b1e06 | -3.1281 | -54.266 | 2024-10-29 13:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 78e6c7e5-7886-3e1b-9f58-69d891ab7ef8 | -3.8042 | -44.1072 | 2024-10-29 13:55:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b906e5e5-1608-3052-b2f5-538353b05410 | -4.3473 | -43.779 | 2024-10-29 13:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 524.0 |
| 23e428bf-7b20-3185-88d3-a565d68e7749 | -4.8606 | -42.6275 | 2024-10-29 13:55:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 248.6 |
| d6807fb2-6659-3529-b36f-31b2c72a1159 | -5.2848 | -43.4179 | 2024-10-29 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 5db969fa-3a74-3084-95a4-064f2bc7bb8d | -5.285 | -43.3947 | 2024-10-29 13:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 92eb39a7-ee4a-3b02-8d26-ccf126f25d30 | -6.3534 | -41.581 | 2024-10-29 13:55:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| e3a29c14-90ef-3b4b-8c51-c81e00689ccc | -6.9968 | -41.35 | 2024-10-29 13:55:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 828dd946-aaea-31f8-a64b-4075bc015632 | -6.9971 | -41.3258 | 2024-10-29 13:55:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 821cc950-fc53-3b5a-b65c-5b73fe29b89a | -7.0157 | -41.3481 | 2024-10-29 13:55:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 151.2 |
| 0654414e-2c31-367b-b7ff-17ea2d069a57 | -7.3964 | -44.2617 | 2024-10-29 13:55:48 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ed145c4f-03d9-3d87-a103-557d68e431c5 | -7.8833 | -42.9534 | 2024-10-29 13:55:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 721.1 |
| b93eaa4c-95d3-355c-8500-758137970dbe | -12.7145 | -48.8477 | 2024-10-29 13:56:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 1472b547-82d5-3426-bad0-b4113f7a908b | -12.6953 | -48.8503 | 2024-10-29 13:56:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| d572799a-9ff8-3765-a7a9-1eab2eac75e9 | -12.6956 | -48.8283 | 2024-10-29 13:56:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 399a9056-cdd6-36cc-b8a7-185aa07eb751 | -19.6067 | -56.6898 | 2024-10-29 13:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 3328a2a5-7884-317d-b498-c130261c5fe0 | -19.6268 | -56.6869 | 2024-10-29 13:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 0bee81af-6ab0-3eab-a5f8-51c4013d31ab | -23.9917 | -54.1329 | 2024-10-29 13:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| e3c746a5-6c42-3ace-a810-eb1ce7d057f8 | -2.4588 | -57.5347 | 2024-10-29 14:05:20 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 112d4e3f-54e8-33f1-ac5e-8dbf58781401 | -3.8558 | -41.7873 | 2024-10-29 14:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 82655b20-98d8-3d18-b731-99b7112d839e | -3.8556 | -41.8112 | 2024-10-29 14:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 4abff16b-029c-3674-b05b-1830c9b288f7 | -3.8745 | -41.7862 | 2024-10-29 14:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 346e8e61-f305-3f7f-a232-b9138137238e | -4.8617 | -42.4858 | 2024-10-29 14:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| ba3cc094-d36c-30a8-bf4a-3965f528237a | -4.8619 | -42.4622 | 2024-10-29 14:05:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| bfa3cb1a-d6f2-31b3-9f2c-b685b42a1172 | -4.8606 | -42.6275 | 2024-10-29 14:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 52a9ec9a-fca1-3b28-b7dc-e6c6cdf4ef0e | -5.8535 | -42.6958 | 2024-10-29 14:05:39 | GOES-16 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 710f72ad-9e94-34f6-8a91-e7ad6ed1d0f6 | -6.3723 | -41.5793 | 2024-10-29 14:05:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 114033e4-ac8f-3a9c-8033-070fb33c3f86 | -6.3534 | -41.581 | 2024-10-29 14:05:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 342.1 |
| 4816863f-5aa5-39cf-9784-3df22f6f8219 | -6.3532 | -41.6051 | 2024-10-29 14:05:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 46fae956-d9df-3b06-99e7-856400a75d1c | -6.5907 | -42.277 | 2024-10-29 14:05:43 | GOES-16 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 4395630f-4be2-3988-82bb-606b44defd51 | -6.6781 | -44.6935 | 2024-10-29 14:05:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1dcb230f-9428-3afa-8526-9e09866ca6c1 | -7.0157 | -41.3481 | 2024-10-29 14:05:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 58dd4207-b8a7-3a91-bef4-5c57c64cbda8 | -6.8482 | -42.8215 | 2024-10-29 14:05:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 9508246e-b825-32ed-94d3-af73c4e957cf | -6.8485 | -42.7979 | 2024-10-29 14:05:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 6f1eb41e-fbdf-35b4-bdd0-bddf86ed8e7d | -6.9971 | -41.3258 | 2024-10-29 14:05:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| bba222e5-ccae-39db-be9c-fab2bcece551 | -6.9968 | -41.35 | 2024-10-29 14:05:45 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| d7aa3c51-0ade-32dc-88cc-333dea239c52 | -7.3964 | -44.2617 | 2024-10-29 14:05:48 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| eafc1f7c-5a56-3021-86b4-24c4a1aa0aac | -7.8833 | -42.9534 | 2024-10-29 14:05:50 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 378.4 |
| 35407484-80e4-3b76-91c9-ae048ade4e6e | -7.9628 | -45.6901 | 2024-10-29 14:05:51 | GOES-16 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 415ebc71-75d0-39ed-bfd1-82ab1a384ccf | -12.6956 | -48.8283 | 2024-10-29 14:06:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 8dbcfa9b-e17c-30d4-8794-68fd1c0e0f55 | -12.6953 | -48.8503 | 2024-10-29 14:06:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 8c8d92da-9e3b-3ca6-848d-5c3bff1ca3b2 | -12.7145 | -48.8477 | 2024-10-29 14:06:18 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| a65dcc8f-c544-3f48-b072-e4023e2ed0d5 | -13.4774 | -43.2352 | 2024-10-29 14:06:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 71187eec-e0ff-3510-8eee-69d41c2930f9 | -13.4247 | -42.981 | 2024-10-29 14:06:21 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 387c6fe3-25dc-35ae-99f0-d56c83db50ab | -13.4242 | -43.0051 | 2024-10-29 14:06:21 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 97874ef9-419a-3c15-9a08-8e31ec9c1729 | -13.4769 | -43.2593 | 2024-10-29 14:06:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 4fca84c0-8261-3164-bb05-e1320495de82 | -13.4964 | -43.2557 | 2024-10-29 14:06:21 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 2d0adf4a-f362-3d69-8f36-bcce3c338b42 | -14.0175 | -46.1388 | 2024-10-29 14:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 981cbe38-dec2-3a2d-be6c-f554facf7868 | -19.5067 | -56.6829 | 2024-10-29 14:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 3454a4ec-fcbe-3615-96ad-94c85b2f8c03 | -19.6067 | -56.6898 | 2024-10-29 14:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| fb5b69dc-e94a-33d8-86cc-28b7a3c50de0 | -23.9917 | -54.1329 | 2024-10-29 14:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| 0af82850-4626-3eeb-b13d-2ae543df58b1 | -23.9923 | -54.1106 | 2024-10-29 14:07:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| b4c6b6b9-4779-3928-9965-6523da41beef | -1.0243 | -48.83 | 2024-10-29 14:15:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 5ffe4aac-d411-355c-8236-0da19eab515f | -1.4117 | -49.0171 | 2024-10-29 14:15:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 78a427a5-05f3-382d-99d2-3535692ca20b | -1.3932 | -49.0174 | 2024-10-29 14:15:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 39cafc66-0482-3b94-a853-c0a02ea0978a | -1.4116 | -49.0384 | 2024-10-29 14:15:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 75047aca-26b2-3429-a88f-313243c90058 | -2.3316 | -57.1281 | 2024-10-29 14:15:19 | GOES-16 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 45b876a2-2c8e-318c-b772-f7478a6b8475 | -2.3499 | -57.1473 | 2024-10-29 14:15:19 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3056c47d-03d3-3aed-b9e7-6b5cd55fb428 | -2.3316 | -57.1476 | 2024-10-29 14:15:19 | GOES-16 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 266.2 |
| 866037f7-a71d-3380-a383-721ecb0cc8f3 | -3.8558 | -41.7873 | 2024-10-29 14:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| c3b43bec-ca0d-3c0d-8bdb-8816970cdf0f | -3.8556 | -41.8112 | 2024-10-29 14:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| 2ef3a1e8-bad5-3945-a567-d9c6476109ec | -3.8745 | -41.7862 | 2024-10-29 14:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 33f5ab15-47a7-3ebd-836b-f79bb3fd232c | -4.8619 | -42.4622 | 2024-10-29 14:15:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 69068c83-5600-3b6b-81d2-8dd55892160b | -5.2848 | -43.4179 | 2024-10-29 14:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |


[Clique aqui para ver as próximas entradas](README110.md)
