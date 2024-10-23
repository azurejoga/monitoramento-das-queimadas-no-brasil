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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8854627d-c6ee-3c71-8aa5-aaa6ae80d1d5 | -17.21082 | -57.51409 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5c8fa698-ba0b-33b7-8825-b2f4f5e765e7 | -17.20802 | -57.50948 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4ef4275d-6db9-399c-b2ee-d876d1d3df85 | -17.20736 | -57.51346 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8dcc31b1-f7e8-3aa1-89b2-66e58ffedc70 | -17.20389 | -57.51283 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d7bd878f-2f94-3a5c-9e26-ace3b7babcb7 | -17.19138 | -57.29077 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 56e33369-2b01-3da2-bed1-06be6eb3f290 | -17.18252 | -57.30129 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 736d0dfe-6bdc-3d6c-9c16-719c0566f52e | -17.17974 | -57.29675 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 44c83314-0186-3c72-b69c-d4458909f32d | -17.06883 | -57.47677 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d667b2b4-e363-31dc-b300-efaeae2407ba | -17.06536 | -57.47614 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b79bc2d8-0cc6-3886-98b7-82b4be13b7e5 | -17.06469 | -57.48013 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 820d1b47-3b06-3280-821a-5f1f410b68b7 | -17.0619 | -57.47552 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1074f601-0b6d-3b03-90c4-9bd4e33e58d3 | -17.06123 | -57.47949 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a537694d-df08-397a-993a-55aea1d69ec7 | -3.0917 | -54.1666 | 2024-10-23 04:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 677ca7a6-f013-3b9a-82b7-7adb5995eb38 | -3.1101 | -54.1661 | 2024-10-23 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| e1a20dd8-0f3f-3c62-af77-6486f7bb499b | -3.1102 | -54.146 | 2024-10-23 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f2a47302-a9da-3323-8a5f-ec608a1b3d71 | -4.1719 | -47.9894 | 2024-10-23 04:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 9284b00f-42c2-38e5-b94e-724069a295aa | -4.172 | -47.9677 | 2024-10-23 04:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6f269830-dd9d-3eb0-bf5c-2f309fc67e06 | -4.1304 | -45.6112 | 2024-10-23 04:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d0af8fd2-374a-3c06-87a6-572d2b6e91d0 | -4.1305 | -45.5888 | 2024-10-23 04:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 460627af-a0ee-3757-beb3-198e759c7645 | -4.1905 | -47.9885 | 2024-10-23 04:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| c2577774-e5f5-3876-a97b-2ffec586f7a6 | -4.1906 | -47.9669 | 2024-10-23 04:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 15055335-fd42-3460-9be3-2d8c67a46ce6 | -5.5858 | -43.2562 | 2024-10-23 04:55:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9c8bfeb8-4e0e-309e-a377-9e48060f05e2 | -27.08987 | -48.63976 | 2024-10-23 04:57:00 | NOAA-21 | ITAPEMA | SANTA CATARINA | Brasil | 4208302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 058aaa23-f66f-3d6a-b737-641e37cdbf7b | -30.1119 | -51.60949 | 2024-10-23 04:57:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 460a9eba-01b2-328f-9a2a-dd1f31273e37 | -29.81332 | -51.17609 | 2024-10-23 04:57:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| fd766ea7-f1b1-3903-bd72-6034fac83592 | -3.1102 | -54.146 | 2024-10-23 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 879bf0df-a392-3f80-b054-59bc33535c80 | -3.1101 | -54.1661 | 2024-10-23 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| be708a94-fd6e-3245-8ed7-8affc0149c23 | -3.0917 | -54.1666 | 2024-10-23 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fba9f308-e2f5-3e4f-95a9-318021ef959d | -4.1906 | -47.9669 | 2024-10-23 05:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7ed3dff3-4436-383c-b1d1-ce928bc734ac | -4.1905 | -47.9885 | 2024-10-23 05:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 8d3cacdc-6969-3b92-ab1d-5d697040018f | -4.172 | -47.9677 | 2024-10-23 05:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b5fa450b-df7b-3cbe-a14f-326eae941f9a | -4.1719 | -47.9894 | 2024-10-23 05:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 069dd045-a690-3f70-842e-c011d05aa6b4 | -4.1305 | -45.5888 | 2024-10-23 05:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 619b63fd-3321-3d46-9e41-af328b841491 | -1.53848 | -51.93872 | 2024-10-23 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9655acd1-fb32-34d3-aec7-1c86a5f6fbe3 | -1.39943 | -52.00361 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c62ded0-baea-3d04-9d99-e57fc66f14f8 | -1.39578 | -51.99903 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5169023-1345-3cfe-8617-1920bc33f320 | -1.39519 | -52.00293 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63d0a8dd-cff2-3200-9112-e1475ce0fedf | -1.39275 | -51.99475 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0f94985b-9b8c-37f1-919a-b46abb32d326 | -1.39213 | -51.99865 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d1675abe-17af-39ac-89ad-7667bfd7d010 | -1.39212 | -51.99445 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df64e9d1-f7e5-31d0-9585-8019d96b8c96 | -1.39153 | -51.99835 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cbc423fa-85b5-37b4-9220-7ae470a0645c | -1.38851 | -51.99406 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a192bbc9-af6b-3cce-a549-8eddf1311333 | -1.3879 | -51.99796 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 47ce2ab1-0973-3379-9230-54e40e534997 | -1.38788 | -51.99375 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a905ca89-8b97-3ef2-810d-f2e8f8d9b726 | -1.38729 | -51.99766 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2f53821f-1364-3feb-ae43-9e9dbc8ad711 | -1.38489 | -51.98949 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb6363ae-1ded-309a-ba72-32349af44d6e | -1.38427 | -51.9934 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd8b5c5f-87a8-316b-bdda-88e88f16908b | -1.38423 | -51.98917 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 93aa9427-01ab-32a5-b1c7-9aa3cf14f33d | -1.38364 | -51.99308 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe5c484a-f6c4-3083-b6b8-684d559ea757 | -0.95195 | -52.085 | 2024-10-23 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e36a3571-d424-3040-b1f3-8e8e599d38f6 | -0.8556 | -52.3394 | 2024-10-23 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80634df0-5c90-32f4-b0b2-fc797d97f718 | -1.94563 | -52.00534 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd6dade3-27e9-36a4-a2be-7537c4c052ca | -1.93488 | -52.10506 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f18a6ac-52ae-30a9-82fb-4a0b4a2aa256 | -1.93427 | -52.10902 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a14c6e-7a5c-334a-bb94-17f6e30a6aa5 | -1.93062 | -52.10445 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dfde8ac-f62b-37ca-a708-1e984a36cd47 | -1.76861 | -52.23547 | 2024-10-23 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d26040d8-24a4-375b-aaeb-77d1a77a8b49 | -2.84999 | -53.33588 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 896b0747-cd9f-3874-8978-81b660561033 | -2.84602 | -53.33527 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc956e43-b2ac-3d76-896e-758776db2d9f | -2.84205 | -53.33466 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da9ec23e-5665-34c6-981a-cc55bb31db28 | -2.78923 | -52.92068 | 2024-10-23 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8be668f-252c-3beb-8747-7a8ebda7bfa6 | -2.78868 | -52.92429 | 2024-10-23 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97c6227a-f56d-31c5-a86e-f022dc8a5046 | -2.78813 | -52.92791 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3866f162-a465-304a-86a7-357cb5b70751 | -2.78462 | -52.9236 | 2024-10-23 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cdda656-3794-3971-882b-97ebf26f1830 | -2.78407 | -52.92719 | 2024-10-23 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98560e1b-130f-3b0c-8a32-192e0c907f1a | -2.17375 | -53.2621 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0eab8826-6756-309f-8b06-1adf2126c38c | -2.1481 | -53.35762 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c273867-2cd7-342b-9222-7a023ec29b76 | -3.07494 | -53.24815 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 124e82ad-eb49-3149-83ea-99ba32386fd9 | -3.0744 | -53.25164 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 451ab590-fc6c-3982-a7aa-31f114bdb07f | -3.07094 | -53.24749 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb538960-538f-3156-be7d-ff527cc2147e | -3.0704 | -53.251 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ad91486-23ec-3b77-9414-83f0c2cda17d | -3.06987 | -53.2545 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff6c70e7-a7df-321e-b67c-40b93cca5133 | -3.06747 | -53.24334 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2a7e193-e75e-3b0e-9beb-1d74d8a71530 | -3.0664 | -53.25038 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9b837bc-10d3-3b6e-91f9-dcd62ee5e910 | -3.064 | -53.23917 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21dd72f3-6759-3274-a241-bc61f2b61eb9 | -3.06346 | -53.24271 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaafbdde-1729-3cdd-9229-5ff2c82b1293 | -3.5235 | -52.82367 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab2790c-5314-3a5a-b844-5a7ca0934b0b | -3.52204 | -52.8244 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bba7698e-cf3d-37c0-a3be-dd5ec6938979 | -3.52147 | -52.82808 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c816e99b-2864-311e-a941-98e8919a7a9f | -3.51935 | -52.82301 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c5f1a3a-67d3-3ece-91e9-857ff0943f7b | -3.51881 | -52.82669 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b3f6fe8-2cdf-32cb-a5dc-8e51b384662a | -3.51791 | -52.82371 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31874ac2-2b02-362e-bba2-a10cb5a7d3ba | -3.46972 | -52.86175 | 2024-10-23 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9600f328-266a-3147-a318-3042c87f00aa | -1.95015 | -54.75454 | 2024-10-23 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49bbddcf-bd0f-3775-90b4-cb019ca5ce7e | -1.8842 | -54.579 | 2024-10-23 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fa0d401-dd75-32d0-ad25-33a671d49867 | -1.80423 | -53.69508 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5896cae5-6b06-3168-9801-c252ed9eeb80 | -1.75114 | -53.7183 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b46a7168-9179-341e-a64a-11ea9c5a74a2 | -1.2575 | -53.37572 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 596d7f89-5918-38b9-b56b-0ecc84e782c1 | -1.22869 | -54.14661 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 679c30ec-7203-3289-a48c-3e1bae83a84e | -1.21421 | -53.37371 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbaecc45-71c7-3a82-a4ab-c8738650d674 | -1.21034 | -53.37307 | 2024-10-23 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccfe36dd-c446-3ef2-9400-fd34d4d83560 | -1.19986 | -53.64252 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcabc0f2-5a54-330e-afa4-159bed827605 | -1.19911 | -53.64734 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7cb60f2-b550-35a0-b800-fcec6aef998a | -1.16195 | -53.66094 | 2024-10-23 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 802f19b6-43fa-3328-af89-1982ce1f8efa | -1.10742 | -54.20823 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af36f0f3-0824-387b-80ed-184ac0836790 | -1.08699 | -54.16988 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f05ce38-d407-3fca-bbc2-42f9ece35e80 | -1.08394 | -54.1163 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2f20c88-5453-3432-975a-cf13d4af6a4f | -2.16418 | -54.40931 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90057bcd-55c6-3116-a80d-9d30ef98d6a8 | -2.16351 | -54.41364 | 2024-10-23 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46d23573-1472-3e47-8b0c-f6086c4371c7 | -3.2684 | -53.70837 | 2024-10-23 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e3a18d-35a6-3c33-aa5e-9c78d348eeb4 | -3.10652 | -54.15548 | 2024-10-23 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README50.md)
