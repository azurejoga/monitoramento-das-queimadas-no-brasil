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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acfaca4e-d551-306a-af33-aec8ce7245ee | 2.9435 | -60.17877 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5722b374-4073-345c-8ed2-bf1986ed257d | 2.00784 | -61.08188 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e93ca4b4-987b-32ea-8c79-afaea2f45116 | 2.7179 | -61.34673 | 2026-04-14 01:02:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f7b1684-09d1-3e01-8962-bbf684fe8e1a | 1.90445 | -61.09721 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e2456d9f-a445-302d-bad4-d237911aacce | 2.58121 | -60.33438 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 47de2498-6e75-3d45-bfea-3a4fb3abb671 | 3.68087 | -61.86771 | 2026-04-14 01:02:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 77067ef4-cfac-3be8-9339-56547765a5c2 | 2.93306 | -60.18701 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 54b63f7c-9b84-34c7-a775-d9e224e16238 | 2.01545 | -61.09196 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 30970a9d-717c-3996-9b6a-b3853d8d0435 | 2.9422 | -60.18826 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e67afb9-d6ad-3a30-86ed-57e111dc5b6f | 2.00661 | -61.09073 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7faf5c7b-b0c5-3b12-bea9-f1461dfdf0e3 | 4.32209 | -59.74049 | 2026-04-14 01:02:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 70260f4d-dabb-3814-916b-035a13752720 | 4.3207 | -59.7506 | 2026-04-14 01:02:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 148a751c-f0bb-398b-b9b5-cc228333bd79 | 2.0138 | -61.1015 | 2026-04-14 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ffda7a10-6eb6-34c8-8638-0818dbaffdef | 2.0138 | -61.0826 | 2026-04-14 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3a66d29b-884a-3ff3-939a-e4945081dc69 | 1.1028 | -60.5225 | 2026-04-14 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ab2f3414-17c7-38f9-a581-3b6fde7abe50 | 2.9464 | -60.16 | 2026-04-14 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0018db5b-e753-3172-819e-a81941bcaf74 | 2.9281 | -60.1793 | 2026-04-14 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 93b7ab96-dcf5-3cda-8860-6fb6b5b9795a | 2.9463 | -60.179 | 2026-04-14 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.7 |
| b5b25dcb-9bbe-33ae-8818-49c477d831a2 | 2.0158 | -61.082699 | 2026-04-14 01:19:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e847ac9f-bdc0-3586-acc6-6d44575f001b | 2.0192 | -61.067402 | 2026-04-14 01:19:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 419a368e-6af1-3b0f-bb21-43db20aeb812 | 2.0138 | -61.1015 | 2026-04-14 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9ed35d5e-a23f-3e23-aab6-19a45517dd43 | 2.0138 | -61.0826 | 2026-04-14 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 64203542-2778-3337-ae52-95f2a537c5f5 | 4.3195 | -59.7501 | 2026-04-14 01:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 85bf971c-9cc0-3256-a07e-bec1df275779 | 2.0138 | -61.0826 | 2026-04-14 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e1bd85a9-92fb-338b-9585-377e4819403e | 2.0138 | -61.1015 | 2026-04-14 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a86aa48b-38b8-3755-9b4a-e00c139ba14e | 2.0138 | -61.0826 | 2026-04-14 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8ed9882a-692e-3aa4-8113-95b01c82ed13 | 2.0138 | -61.0826 | 2026-04-14 01:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 92c05131-631a-3b6e-b426-3bb9b39df8c9 | 2.0103 | -61.084599 | 2026-04-14 01:52:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e7c874b4-8162-3be4-91d2-b3d032fd6399 | 3.2433 | -61.188499 | 2026-04-14 01:52:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bae78685-8f45-3a0d-b96a-92851b3194c1 | 2.0139 | -61.068901 | 2026-04-14 01:52:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9dcfed2f-ee9a-3ac8-a21c-68db6d1c0d41 | 2.0138 | -61.0826 | 2026-04-14 02:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8e41c4c3-211a-394e-83dc-0bc1fa97fc89 | 2.9463 | -60.179 | 2026-04-14 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 286d4ce6-33d3-3921-8154-ab4cd362abff | 2.9281 | -60.1793 | 2026-04-14 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cdb84991-48b6-32d4-8df1-29c63139317c | 2.0138 | -61.0826 | 2026-04-14 02:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4c7d4d20-367c-328a-bf67-9c8331e26158 | 2.9463 | -60.179 | 2026-04-14 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1c7b3e44-a37b-32f3-b85b-6bb5d0c38b42 | 2.9281 | -60.1603 | 2026-04-14 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5a43edd8-7b07-3d4f-9c77-80d96885475b | 2.9464 | -60.16 | 2026-04-14 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| f4fbc82a-8e2f-3e8f-8c16-4ed396d196b6 | 2.9281 | -60.1793 | 2026-04-14 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 47db6303-404e-3d7f-a912-32dfc45d888e | 2.9463 | -60.179 | 2026-04-14 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f15c2539-1e6a-36cf-a3b2-8b5f901dbf73 | 2.928 | -60.1983 | 2026-04-14 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b06c3d82-79a1-3390-8893-541cc1502dcb | 2.9281 | -60.1793 | 2026-04-14 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.6 |
| d04315b7-6783-3bfb-a321-56aa40bff08c | 2.9281 | -60.1603 | 2026-04-14 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 636e89eb-93a8-38a6-b13c-5af49ba246ac | 2.9464 | -60.16 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 38348775-701a-3c10-a33a-4a5efefbc0a2 | 2.9463 | -60.198 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| a88b54b3-a2aa-3714-9d48-3680aaedd78a | 2.9281 | -60.1793 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 9b2cdefe-46cf-3871-8e86-e59c38025c95 | 2.9463 | -60.179 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| c219dbcb-b552-3c87-adbd-a65fd4ea2826 | 2.9281 | -60.1603 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 634d0cfb-87d4-3949-a7e4-d4795c496d26 | 2.928 | -60.1983 | 2026-04-14 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 973d7b80-f1b5-3a1d-ac7d-a260da3ca8f8 | 2.9463 | -60.179 | 2026-04-14 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| cbb6a0ac-e335-397a-8e4b-c6a99f1d0d95 | 2.9281 | -60.1793 | 2026-04-14 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 65d0ecba-fb1c-3570-ad8d-44f948833fcd | -9.53715 | -37.02831 | 2026-04-14 03:25:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db2df580-296f-3b92-8658-6e3d69a30c9a | -9.53646 | -37.03239 | 2026-04-14 03:25:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 984a8504-da0f-3cbe-9c17-d3f554796e05 | -9.28562 | -40.45921 | 2026-04-14 03:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65740063-07c8-37d3-838a-a5f25b174279 | -9.54665 | -37.01653 | 2026-04-14 03:25:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52c9fbdb-a321-302e-bcf1-645d62cd7ab1 | -9.53523 | -37.03119 | 2026-04-14 03:25:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e39c2f94-70f5-33bf-b439-dc9933160611 | -14.4017 | -44.59116 | 2026-04-14 03:25:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f37f9df2-5cba-3a10-b2c5-d5f88f57214d | -14.40286 | -44.58578 | 2026-04-14 03:25:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00b643c1-c63d-3c87-90c3-0a807dc78572 | -14.89319 | -42.41609 | 2026-04-14 03:25:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6995748-f831-3d58-857e-22a9e0a681f8 | -21.34345 | -47.05328 | 2026-04-14 03:28:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e69454c-7186-321b-897e-546651143391 | -21.33286 | -47.0689 | 2026-04-14 03:28:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b85c9b5-4ec5-377f-80ee-d19f951a1287 | -19.60801 | -40.07268 | 2026-04-14 03:28:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| deb50773-a821-3f1e-8747-5bffe9a5f380 | -21.33714 | -47.0513 | 2026-04-14 03:28:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f88bb7eb-0ccc-346f-8d45-bf09cf98e835 | -21.19032 | -48.61136 | 2026-04-14 03:28:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aa705164-431c-35de-b87f-535d2ad61703 | -21.15478 | -42.97549 | 2026-04-14 03:28:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ddbe45ab-7960-3377-bba8-5754e55017ba | -21.19733 | -48.613 | 2026-04-14 03:28:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c84b1354-5d06-36d6-a836-cf7691d06f90 | 2.9463 | -60.179 | 2026-04-14 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3d7459cb-1ae1-3f45-9d95-94f47b45d0b4 | 2.9281 | -60.1793 | 2026-04-14 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 04873108-211c-33f0-ad61-d4329f8271aa | 2.9281 | -60.1793 | 2026-04-14 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 7b460979-ff88-3053-96eb-6c0c3e65ad41 | -9.53574 | -37.03099 | 2026-04-14 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea470f5a-1a6d-3cd4-bfb1-7dbc5fea2b23 | -9.80024 | -37.47205 | 2026-04-14 03:55:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e9c7c36b-feee-32b4-8986-32f07e62fe89 | -9.28369 | -40.45859 | 2026-04-14 03:55:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2fd47f23-443f-3cf4-8cbc-874113c10944 | -9.53629 | -37.02748 | 2026-04-14 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5692796a-6775-32ad-9bf5-ea005560be44 | -9.80356 | -37.47258 | 2026-04-14 03:55:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87051846-77d6-33f3-b3a4-18d20c5d3609 | -9.803 | -37.47608 | 2026-04-14 03:55:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7012786d-35eb-3e5f-a1b7-51a66669d8ef | -9.68335 | -37.35957 | 2026-04-14 03:55:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2b45a71-1d30-33d8-bb13-e6b2a7bfb227 | -9.00976 | -38.39482 | 2026-04-14 03:55:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c6b646d-1e82-3582-8af0-b5138497108b | -7.83521 | -42.05219 | 2026-04-14 03:55:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2db6278-6455-34b3-89b3-52fb79de974a | -9.54732 | -37.01825 | 2026-04-14 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5ef282b-e303-3432-9688-1f8051d6610c | -15.42501 | -43.01895 | 2026-04-14 03:57:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0785077-290a-3043-baee-cc10db0cbc52 | -15.45005 | -41.69151 | 2026-04-14 03:57:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae23b888-52fd-378c-965f-5964dcdbc9fd | -11.44994 | -38.82244 | 2026-04-14 03:57:00 | NPP-375D | BIRITINGA | BAHIA | Brasil | 2903607 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a256d675-2d0d-3a27-b544-ee8c61ca09d7 | -9.45564 | -47.82468 | 2026-04-14 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 521ff58d-4993-36c6-9188-6df20b853477 | -14.40319 | -44.58969 | 2026-04-14 03:57:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8786cb6-3f8a-3afa-85c2-eb7a76edeab8 | -9.45074 | -47.8194 | 2026-04-14 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13a36da5-7f05-3c45-b1c7-687df1361eab | -12.24626 | -44.17083 | 2026-04-14 03:57:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45eff07d-1b3e-3fc9-b711-7574268d84f0 | -14.39896 | -44.5889 | 2026-04-14 03:57:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93a11ce8-5b43-38ff-9c21-972dcae78387 | -14.40246 | -44.59372 | 2026-04-14 03:57:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de379e47-8ca0-3f60-9cd5-5e494b7bac3d | -11.0178 | -39.005 | 2026-04-14 03:57:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13e89ff2-8dbb-3d08-bcfb-d6c137672d1a | -12.24381 | -44.16776 | 2026-04-14 03:57:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a2e02c1-23cf-35df-a201-35e9138b1ea7 | -12.24309 | -44.17179 | 2026-04-14 03:57:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8867c89d-8948-3bb3-9a03-ab55d3a49bb1 | -15.3858 | -40.8508 | 2026-04-14 03:57:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 931e7485-93c2-3470-a90f-3531bc9a08b4 | -20.12012 | -46.75355 | 2026-04-14 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c249c963-72e1-3fe6-ad6e-6fa0d6cc144b | -23.02504 | -48.44633 | 2026-04-14 04:00:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21b8695b-eac2-3b9f-9c16-4b20c5c2d0ee | -20.11604 | -46.75566 | 2026-04-14 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75970aae-77cd-3142-aa49-1ac78c0e1410 | -20.38279 | -41.57499 | 2026-04-14 04:00:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 334dfab7-4d62-39ac-bc6f-53e8a7800481 | -17.53096 | -44.75428 | 2026-04-14 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e0a945-6f6c-3bb7-bb1f-01ea77376d3a | -21.1974 | -48.61204 | 2026-04-14 04:00:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5a48965c-09d2-3b7f-8d80-19a5de3154a1 | -23.02398 | -48.45134 | 2026-04-14 04:00:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa0d90fe-71e0-3289-b55f-9492661b2f06 | -19.60751 | -40.07048 | 2026-04-14 04:00:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec534663-516a-3c9e-9d20-7c7ec03ca2bc | -19.6036 | -40.07355 | 2026-04-14 04:00:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
