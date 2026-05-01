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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c976c6f-3334-355d-a9ee-9e0f89ac3bab | -17.24811 | -47.08146 | 2026-05-01 04:00:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df23d26a-18a2-33c7-b32a-56e1ff8ff179 | -19.09126 | -40.08134 | 2026-05-01 04:00:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 719af315-2af2-3020-9be5-265b7fd0be2d | -18.89425 | -39.92697 | 2026-05-01 04:00:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 42510daf-6395-3e2a-b405-0d955db34949 | -19.0965 | -40.66685 | 2026-05-01 04:00:00 | NOAA-20 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc136c33-df64-32f5-b1fb-b3063e27ffbe | -14.23266 | -43.65128 | 2026-05-01 04:00:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 977cf6fd-85d5-31e7-8f50-2904463f1acf | -19.43486 | -46.89008 | 2026-05-01 04:00:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8d4555b-af3a-32de-ad4d-61778b94997a | -16.76703 | -45.81253 | 2026-05-01 04:00:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bf1b276-3949-3fd0-9d9d-4cde08d2b620 | -21.95105 | -48.03777 | 2026-05-01 04:02:00 | NOAA-20 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97510980-05c7-34d0-830c-0c617d37bb69 | -20.0531 | -50.4532 | 2026-05-01 04:02:00 | NOAA-20 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 777ea513-2957-3018-8ca3-0870893578b6 | -20.81238 | -45.18218 | 2026-05-01 04:02:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd481792-892e-3cfb-a2c7-b4706bd182c8 | -20.61357 | -48.93036 | 2026-05-01 04:02:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 595b567b-df80-3fdf-998a-2a1dc0f078c8 | -20.21172 | -46.45991 | 2026-05-01 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ee5a25f-e28e-3d08-8cc4-475e0b1763e1 | -21.13748 | -48.55904 | 2026-05-01 04:02:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0ffcc93b-f01a-3a13-9175-ac87a9f14627 | -21.67191 | -43.61338 | 2026-05-01 04:02:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1eb37143-3e57-37c5-86b2-9f2589a534fa | -20.813 | -45.17947 | 2026-05-01 04:02:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1b8fe98-51ac-314d-a63e-fc94cd654332 | -20.2078 | -46.45918 | 2026-05-01 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f97ce466-be42-3b78-8ec0-e4ade89f3344 | -20.2127 | -46.45462 | 2026-05-01 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708fe9d0-b412-3d91-8fcf-9aed089ff1e4 | -21.01907 | -44.07953 | 2026-05-01 04:02:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a1eebae6-17d0-3618-9dc2-7ef376d13a7e | -21.6753 | -43.61404 | 2026-05-01 04:02:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5e3ebe8-4708-3b83-a4d3-e0d4fb1c1854 | -20.05244 | -50.45632 | 2026-05-01 04:02:00 | NOAA-20 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 55d30e5f-7494-38ff-9b18-8f6f57c1dd76 | -21.70097 | -48.42315 | 2026-05-01 04:02:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09a8e2c2-761f-3527-88e5-8cf0ea8a094a | -20.8122 | -45.18387 | 2026-05-01 04:02:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50eae22c-fac7-3938-a3bf-6cf6891f0c64 | -28.20321 | -48.70301 | 2026-05-01 04:04:00 | NOAA-20 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 871d1cb4-dc47-3e28-ae4c-9a7c374544e3 | -10.9624 | -45.09 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 48b4f1f8-1767-3738-903f-673536fa5e6e | -10.962 | -45.113 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 570864c2-73a9-3476-aa47-c9beae2acc07 | -10.9811 | -45.1104 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e54a99c7-a7a7-3f8a-a98f-ca27349d5609 | -10.9815 | -45.0874 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 317.4 |
| 4194a7e5-eecf-36e6-8fb0-ad785d6cf796 | -11.0006 | -45.0847 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 10711744-b913-3037-9554-e84ce7d746b8 | -10.9819 | -45.0643 | 2026-05-01 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 23d0c9cb-8436-3fd3-bdee-e989e9f3d22c | -10.9815 | -45.0874 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 316.1 |
| 73c0c7e4-90db-3ace-9e8c-43c6c1948584 | -10.9624 | -45.09 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 43b5693f-ff32-3b2d-b18b-f8f732af513f | -10.9811 | -45.1104 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b72cefa9-b418-3c43-9034-9a18593072c4 | -11.0006 | -45.0847 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 31745ae5-ec4d-36fb-b90e-a64c16deec38 | -10.962 | -45.113 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e0725b4b-52a0-3824-bdf5-296224439433 | -10.9819 | -45.0643 | 2026-05-01 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 4ecffe49-e766-3d6e-ab39-4361f0adf723 | -10.9815 | -45.0874 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 306.4 |
| 3c347493-a4ab-36d1-a325-fb9bbb9e7142 | -10.9624 | -45.09 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 78f57f7c-2018-31af-a69d-e55adefecbf6 | -10.9811 | -45.1104 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f3695b43-8130-3390-b26f-ae023be71ccc | -11.001 | -45.0617 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ffbcfee2-aacd-37f9-b118-124179e18ddb | -11.0006 | -45.0847 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bdb81456-9f3b-34eb-984f-8c516ba78994 | -10.9819 | -45.0643 | 2026-05-01 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| ea029470-60c4-3a37-ac84-f87a1cf14b90 | -10.9819 | -45.0643 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 62b85ab3-38f2-32b1-a0fc-cca3fc2440c5 | -10.9811 | -45.1104 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ee93b4b4-cbbf-3a6e-9244-acb74ef2cb63 | -11.0006 | -45.0847 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 98b27aff-65bc-32a2-87fb-183badda51ae | -10.962 | -45.113 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 0cbc764f-2b1b-346a-833a-29bf32fc6782 | -10.9624 | -45.09 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| a5e8418a-9b9a-3dd9-8868-5d21f25930b7 | -10.9815 | -45.0874 | 2026-05-01 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.7 |
| b10ea51d-63b7-392c-bd5e-ad864822a58f | -9.64254 | -42.94974 | 2026-05-01 04:46:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5d1058f-9055-37ca-a7cd-265aa881d68e | -7.3156 | -46.20234 | 2026-05-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40dbf98e-d02a-3ece-b7fe-0ca323d6a6e4 | -9.56492 | -44.57449 | 2026-05-01 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f5fd4dc-ef7c-35a8-93f4-744178212f04 | -10.55645 | -44.3359 | 2026-05-01 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b7c62636-b4e1-31b5-afc8-099796dfe266 | -8.33265 | -45.35998 | 2026-05-01 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59835f26-67ad-318f-9f6e-cb4df5cf5fb5 | -8.33692 | -45.36078 | 2026-05-01 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97a63aa1-ae0b-311c-827a-fdade6cc57d5 | -9.56547 | -44.57347 | 2026-05-01 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9e389c0-c943-3ee8-848e-383d82fb4fa5 | -10.97454 | -45.08501 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f69325bb-49a5-392b-bf24-980b7660a4b8 | -10.00736 | -48.67661 | 2026-05-01 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ceaf350-ba46-3742-81da-8063a3465499 | -8.22911 | -43.88069 | 2026-05-01 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6e3be35-81ce-35d7-bf60-5978d62224a1 | -10.96876 | -45.09362 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 668aaf0b-6292-33fa-851d-62340b25b1d2 | -10.96939 | -45.08894 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 454e6d36-144b-3815-b949-7c38eb505cd6 | -10.97329 | -45.09437 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 727d1276-50a4-3b9b-bc69-45507da07d97 | -10.96753 | -45.10285 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d393a24-1072-31d1-b54a-bd4efe4298df | -10.55169 | -44.33527 | 2026-05-01 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07463e68-5403-37b1-a8ac-5e3ae7fd3396 | -10.97517 | -45.08033 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f4749ca4-05c2-3e36-bdbd-a9b1f64a0a61 | -4.80388 | -49.97182 | 2026-05-01 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54974466-7ffb-3eb9-9de8-6ae4ca3a14d1 | -10.97205 | -45.10357 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 2c0dc43b-0e4b-377f-a07f-190171cf834e | -10.55711 | -44.33699 | 2026-05-01 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| de6b9a49-05d3-3b0d-b1b3-fb2ae0923f3a | -9.56554 | -44.56972 | 2026-05-01 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1526a3f-4054-3c3d-8f27-db13f61efe8e | -10.97392 | -45.08968 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| dd7dd0d4-2293-3bbf-94ef-260b01c50dd2 | -7.05365 | -45.05946 | 2026-05-01 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2878e9d6-1e82-3593-a07a-2c0403feb58d | -6.44185 | -44.58419 | 2026-05-01 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e4434a1-2eb1-3231-b5d3-7d7580c59dc2 | -8.23315 | -43.88644 | 2026-05-01 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ec6767e-b4e0-31c4-aa07-76f727138ede | -10.96814 | -45.09826 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c9d6987b-a7b2-3c23-b770-287852e883b7 | -10.97267 | -45.099 | 2026-05-01 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 0e2acf88-46b2-3f1c-a835-afe7bde012f1 | -12.37704 | -50.03235 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e49dea5a-f8d2-3608-a914-171bb7dbb815 | -10.97844 | -45.09044 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| dc95007b-01b7-3f20-9df4-5ab4761e9fb6 | -10.9772 | -45.09971 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 4b0c0c3e-c375-3fe8-836b-88087d68db3e | -14.69479 | -52.94609 | 2026-05-01 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3c7e680-d9a6-31bf-ab7d-b37365366f4b | -10.99331 | -45.08318 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6651f339-00ec-3891-8aa1-c7fb0efd59a1 | -10.98878 | -45.08246 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| dda1a934-679c-3df3-8fa4-12726b57c701 | -11.57097 | -54.56157 | 2026-05-01 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e24a4a-6cf3-30dc-a4d0-0fbf812a5319 | -15.42808 | -46.67213 | 2026-05-01 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e958493a-88bc-3ec5-92d1-eca1b20368af | -12.37745 | -54.75087 | 2026-05-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3513f123-dd16-314a-8ee5-0686e1f7b824 | -11.37762 | -55.17498 | 2026-05-01 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ce4901f-587f-320d-93ca-8b35c9596e5e | -11.43449 | -55.09889 | 2026-05-01 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 665d8a40-7a82-348c-857c-35340d49894f | -12.37358 | -50.03181 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4e1b2f2-e502-3433-a955-7586e4b6c067 | -12.3805 | -50.03289 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bef5b0b-d790-36ad-bf50-4bf88017e2aa | -14.9015 | -45.18221 | 2026-05-01 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe6334c9-218d-3d33-9d0b-9158dfa2497e | -12.37047 | -54.74971 | 2026-05-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c44f2172-9ad5-34c1-9544-63397b4e523f | -12.98879 | -54.68293 | 2026-05-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43b882df-3674-3566-a867-1bc29349f766 | -11.4338 | -55.10304 | 2026-05-01 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dea54d45-9151-3e55-abe8-891ff97c9404 | -13.36807 | -39.91045 | 2026-05-01 04:49:00 | NOAA-21 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3da9fc7d-985e-3e01-8769-21cc1de36483 | -13.78869 | -44.09724 | 2026-05-01 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2609e1e3-0eee-339b-816f-b85a12a1830f | -10.72116 | -56.23016 | 2026-05-01 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5724e35f-f90a-3f46-b849-e8ecf50f0e4e | -13.37319 | -54.26981 | 2026-05-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 256a8a1f-bf22-31fe-bab2-bfed0519227b | -12.285 | -44.62883 | 2026-05-01 04:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebb8700b-1c4a-384f-ba7b-cca992e59d4f | -10.99267 | -45.08788 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75423569-cd7f-37b8-8d8f-53562c091d1d | -12.37396 | -54.75029 | 2026-05-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae8fbc00-2516-3428-993d-3519a6877185 | -12.37129 | -50.03175 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a9cb163-b619-32df-8156-574cb43d92a5 | -14.68486 | -52.94445 | 2026-05-01 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b991a70-8b45-3895-9e74-2f2da0ad72ed | -14.20585 | -57.43056 | 2026-05-01 04:49:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README5.md)
