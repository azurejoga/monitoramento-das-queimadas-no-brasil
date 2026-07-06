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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe974379-0896-3664-b60e-90fedfa29a1d | -13.3163 | -54.3634 | 2026-07-06 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 0051bf2c-9538-3a48-b612-216e680a6bc4 | -13.2972 | -54.3655 | 2026-07-06 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 742aa194-6163-3f49-9e2b-0749632d6552 | -13.2975 | -54.3448 | 2026-07-06 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cb60ebad-193e-3aca-9c00-b0a1062997ce | -12.5138 | -48.2581 | 2026-07-06 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| c04082c7-0141-31a4-b965-6f3f8aa2bc6b | -13.278 | -54.3675 | 2026-07-06 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3448689b-4164-32c1-9bc1-8b7c9bad8cfc | -13.2969 | -54.3861 | 2026-07-06 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 868fae2c-6620-39cb-add3-f60a056db285 | -9.65822 | -67.23046 | 2026-07-06 13:25:00 | TERRA_M-T | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 726e5ecc-f889-389c-b7c5-602829cf2f77 | -10.40198 | -65.13822 | 2026-07-06 13:25:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9d47e73e-3fe9-3a0c-ad45-de484bd8910b | -10.39976 | -65.15642 | 2026-07-06 13:25:00 | TERRA_M-T | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9e100cc2-c053-3970-b5ab-e69b8bfb4890 | -13.278 | -54.3675 | 2026-07-06 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| cab7fff4-aabf-3c8a-91af-9a4cf20fb691 | -12.5138 | -48.2581 | 2026-07-06 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| e731e01b-c061-3db6-ab48-65deb8857914 | -13.3163 | -54.3634 | 2026-07-06 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| f9809bb5-0886-3356-9d5a-965d124e8b3f | -13.2969 | -54.3861 | 2026-07-06 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 13ca1e54-fc92-31c1-961a-7d7abd38ba7d | -13.2972 | -54.3655 | 2026-07-06 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 81fd9514-243d-3b92-97d4-f8b548ccce50 | -13.2972 | -54.3655 | 2026-07-06 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 27cbb09d-5fc2-3457-9600-e55cc8600309 | -13.278 | -54.3675 | 2026-07-06 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 8fea81e3-7ec9-32d0-8541-f5896c911b98 | -12.5138 | -48.2581 | 2026-07-06 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 07d7ca28-fb45-300a-891b-850fbe0ffd59 | -13.2969 | -54.3861 | 2026-07-06 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| a530a1c0-085e-32ff-a07f-bbc08158a7c1 | -13.3163 | -54.3634 | 2026-07-06 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 23e2c88f-0ff0-3075-9d2d-d8816958a54c | -12.5138 | -48.2581 | 2026-07-06 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 463f95bc-d703-3b2b-b5f5-4ae2d980c665 | -13.2969 | -54.3861 | 2026-07-06 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f6fea476-5087-3edd-99ff-fb8de9cc31d3 | -13.2975 | -54.3448 | 2026-07-06 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 848fd208-4847-3ccc-a1d1-a548e37da5af | -13.3163 | -54.3634 | 2026-07-06 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| ac4a1654-f820-3441-83a5-28ceedafece8 | -13.278 | -54.3675 | 2026-07-06 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| da899bd0-6ad6-312f-bdcc-7d86775fce0d | -10.8467 | -46.3582 | 2026-07-06 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 956173bb-bc83-33e6-a9fe-42cf9880f660 | -13.2972 | -54.3655 | 2026-07-06 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 47eecae2-43d7-35a2-a958-060e832bea41 | -13.2969 | -54.3861 | 2026-07-06 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 898e6f43-047d-3bfc-bec6-5166d960e1f4 | -11.9305 | -43.3812 | 2026-07-06 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 485e9adc-2dce-392e-843e-4e8dd112855a | -8.7294 | -54.5645 | 2026-07-06 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 92ff0231-8234-3f05-bb16-00c3a0e24395 | -13.2972 | -54.3655 | 2026-07-06 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 0acae871-7e6b-3917-9c94-a4f9b3af177f | -13.3163 | -54.3634 | 2026-07-06 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fc4fe900-72fe-350f-9d9b-c46b341151c8 | -13.2975 | -54.3448 | 2026-07-06 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5e78ee43-17d8-3d6d-a546-2efe90b65252 | -12.5138 | -48.2581 | 2026-07-06 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 42a463f7-5934-35b9-b07c-21d8e2cb8160 | -13.278 | -54.3675 | 2026-07-06 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 89a67e8a-da0c-3591-9fb0-a980a5c093ef | -11.9305 | -43.3812 | 2026-07-06 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 99b34534-538c-3e6d-8a1a-8ef3689249ee | -8.7294 | -54.5645 | 2026-07-06 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 239eaaa4-fc90-3994-b11b-b98da8b99be3 | -12.5138 | -48.2581 | 2026-07-06 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 265.9 |
| d6b7ab27-7f42-3c52-ac79-dee91e86f73c | -11.9305 | -43.3812 | 2026-07-06 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b0779245-2213-37c9-9dd3-68c7b64df815 | -8.7294 | -54.5645 | 2026-07-06 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| db723889-b8d3-3944-afc2-16b615afbebd | -6.9138 | -43.7049 | 2026-07-06 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1d7e336f-24c1-3540-b4c0-b7dc7a7b6102 | -12.5138 | -48.2581 | 2026-07-06 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 221.5 |
| d2ef3426-6e91-3d13-a2cf-afbfc5811ba3 | -8.7292 | -54.5847 | 2026-07-06 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 57fbac2d-c2d5-37d9-93f6-6705b7b63a7c | -8.7294 | -54.5645 | 2026-07-06 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 1ae0619d-7a40-32a0-ad51-708b33ff9cdc | -6.9138 | -43.7049 | 2026-07-06 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7a37a35c-51a6-3098-86e4-0b72a5757da8 | -12.5138 | -48.2581 | 2026-07-06 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 98cb5063-b092-3260-8d93-4cecc44ec7ff | -8.7294 | -54.5645 | 2026-07-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 5be1c6c9-9f21-37f7-9b26-1c36db7bf674 | -6.9135 | -43.7281 | 2026-07-06 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a2fab098-d423-3724-acfa-c170862ba189 | -11.666 | -46.3846 | 2026-07-06 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5c91e90b-3a12-3da8-887e-916b7483ab55 | -6.895 | -43.7066 | 2026-07-06 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a05968bd-618d-3f5f-a863-8556f9d0cf3f | -12.5138 | -48.2581 | 2026-07-06 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 892dba46-77ed-3929-abdc-1b27e2e2e40f | -6.9138 | -43.7049 | 2026-07-06 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| cbc7c785-a4ab-3df4-acfc-c7d8b89c4cf8 | -7.9281 | -45.4446 | 2026-07-06 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3f4905cb-23b8-3ee0-8ea1-737d28d8a3fb | -12.5138 | -48.2581 | 2026-07-06 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 267df452-6dbc-346a-b8f2-b2b26aec58a6 | -8.7294 | -54.5645 | 2026-07-06 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 278.2 |
| e6745fb6-8a58-3f2d-bd58-b8490eb07e03 | -11.9305 | -43.3812 | 2026-07-06 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c710ab1b-4c56-38ea-ba07-369859486829 | -6.895 | -43.7066 | 2026-07-06 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 31810a82-285e-3693-9007-999fcaeb9bca | -11.666 | -46.3846 | 2026-07-06 14:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 50f83e07-7349-37ae-8997-610ad7069e63 | -8.7108 | -54.5657 | 2026-07-06 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b9e9bc5a-c4d4-3526-bcd7-6c6f10259f39 | -6.9135 | -43.7281 | 2026-07-06 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dc793062-da54-3625-99d2-6b5d39f486c8 | -6.9138 | -43.7049 | 2026-07-06 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 74a8429c-bec3-3d36-a7d2-60fa3ccc77d2 | -12.5138 | -48.2581 | 2026-07-06 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 9552e9b3-0fac-3b38-b7c8-1393f65a5235 | -11.666 | -46.3846 | 2026-07-06 15:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 011a664a-5c91-3c9f-b7f7-93e064bf44c7 | -8.7294 | -54.5645 | 2026-07-06 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 295.5 |
| 7f6de272-bd73-3e86-89a3-2c8662d7585f | -6.895 | -43.7066 | 2026-07-06 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8d3c15e2-9835-327e-bf71-ab208ef0546a | -6.9135 | -43.7281 | 2026-07-06 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 12dc7d2c-aec7-3d6a-8c1b-f57b25805a86 | -6.9138 | -43.7049 | 2026-07-06 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| ae270bd3-baf7-30dc-9506-8b920a1364e1 | -12.5138 | -48.2581 | 2026-07-06 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 8f90231a-818d-3b7c-bc07-0da04d4ff246 | -13.2969 | -54.3861 | 2026-07-06 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 2ad4fc10-df73-36dc-bbb1-bfb20fdfe4d0 | -13.2783 | -54.3469 | 2026-07-06 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 182.4 |
| 65c236ba-7244-3af2-a912-3d64fc0a8496 | -13.278 | -54.3675 | 2026-07-06 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 198.8 |
| 955a852d-4e1b-38e4-9c3e-43de1e438ce7 | -7.9281 | -45.4446 | 2026-07-06 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1d9b4dfd-dc43-34d5-b20f-b9bb5521ddc7 | -6.9135 | -43.7281 | 2026-07-06 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6536654a-ad62-34ed-bfe3-c486b789365e | -13.2972 | -54.3655 | 2026-07-06 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 672c8bf4-54c5-3234-ba4a-d0af101707f4 | -6.9138 | -43.7049 | 2026-07-06 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 17ec11d7-df55-37ec-a5f1-fda6d6b5e4ea | -8.7294 | -54.5645 | 2026-07-06 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 3066f82e-e993-3e3b-bedd-0d1243ad8ec5 | -13.2975 | -54.3448 | 2026-07-06 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 2c6a3504-ff3c-3ecc-b39e-4a3026920b40 | -6.895 | -43.7066 | 2026-07-06 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5f7ced11-870f-3c18-ad29-8c1c28d4a30e | -11.433 | -46.6195 | 2026-07-06 15:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1d7e71d9-4403-3cf6-9b55-ee80e7369eff | -12.5138 | -48.2581 | 2026-07-06 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 76ba27d1-e2fb-35c9-8616-31b3dc12b683 | -8.7294 | -54.5645 | 2026-07-06 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 982e801a-e4f6-3c43-81a5-da067d506661 | -6.9138 | -43.7049 | 2026-07-06 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 200dc5d2-5633-3c80-843d-eaf199d89952 | -8.7294 | -54.5645 | 2026-07-06 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| a240dbc6-9fbd-336b-b95f-7e6a403a9a71 | -6.895 | -43.7066 | 2026-07-06 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 947aaabb-29cc-3da0-9427-e1563b8d820f | -11.9117 | -43.3605 | 2026-07-06 15:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 37948b4d-225d-31b1-9e17-215ebd049c8e | -12.5138 | -48.2581 | 2026-07-06 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 777753d7-7609-3f7e-84b4-2682046c88df | -6.9138 | -43.7049 | 2026-07-06 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c17f0e7b-93e0-3e3f-8951-5d34a515ec80 | -6.9135 | -43.7281 | 2026-07-06 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c76477e5-da55-370f-b24e-86d78361c40c | -9.5327 | -48.1544 | 2026-07-06 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b5b5bf0d-a3ef-3cb1-9292-5ed6e3fde082 | -10.4521 | -50.0073 | 2026-07-06 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8c015071-e94a-3076-b4c2-a4631db14e8e | -10.4521 | -50.0073 | 2026-07-06 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 36f21897-819c-37f8-bdb3-7cd2dcd5f515 | -11.666 | -46.3846 | 2026-07-06 15:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| dc812027-17a9-3b2c-9de7-67c9ccaabc0f | -2.9003 | -42.1659 | 2026-07-06 15:40:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fc8ef4cd-7816-3932-8131-13ee58b58c71 | -6.895 | -43.7066 | 2026-07-06 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 69ac2912-fd78-333b-8912-24049c0a7b1a | -6.127 | -47.6172 | 2026-07-06 15:40:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 22d49aa4-6500-3908-9be3-5f43019b8f75 | -8.7108 | -54.5657 | 2026-07-06 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5e64867d-9f4f-3c19-a748-6e08aeace133 | -8.7294 | -54.5645 | 2026-07-06 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 833d4cb0-0db1-3914-bbd8-b690abee268e | -6.9138 | -43.7049 | 2026-07-06 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b9d9c024-446c-3c97-9015-9bbbc4787046 | -11.6851 | -46.382 | 2026-07-06 15:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 23033014-f254-35d9-859e-f655290841f7 | -6.9135 | -43.7281 | 2026-07-06 15:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| aba7f7e5-0a0a-3e72-b3fe-9ee0e4651895 | -8.7294 | -54.5645 | 2026-07-06 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |


[Clique aqui para ver as próximas entradas](README8.md)
