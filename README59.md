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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6c51ab9-daa6-32a9-9ef4-abbcc7bc0e66 | -13.13537 | -41.9744 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 374c470a-50f6-3e59-bb2a-438a577dec5c | -13.13501 | -41.97226 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 319ec252-b20c-32cc-b137-1006ae4c81b2 | -13.13462 | -41.97538 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f3d8a691-af46-3523-a2f2-a1bb5fccc312 | -6.25968 | -42.50691 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 47ddac6d-f0a6-3e6d-9a03-ead2c80c461f | -6.25582 | -42.50138 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 37e20ac0-5720-35fb-bf5f-e09ba60b5225 | -6.25511 | -42.50626 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8c2e22ce-4d7d-39a7-a915-447930d8858b | -6.25057 | -42.50543 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6a925c5d-777c-319b-9153-a9f76caa93c3 | -6.24984 | -42.51047 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 805b21f7-67ba-3260-a9e0-b2c2da5f1876 | -6.24531 | -42.50956 | 2024-10-13 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9b8062f0-f001-34d1-be96-bb45e30b78bc | -6.08378 | -42.39367 | 2024-10-13 04:40:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15a9705a-3072-3156-a9d7-a0ef0df8b573 | -6.07918 | -42.39304 | 2024-10-13 04:40:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec745025-fb83-324c-9f21-b0ec49efa68e | -5.95691 | -43.19417 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c539c3f8-85c6-302a-b798-d0a32e521d56 | -5.95196 | -43.19772 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 83f9ef9b-920c-3a17-bf01-b867b64514b4 | -5.9479 | -42.66164 | 2024-10-13 04:40:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0873162-b4df-37d1-af20-65b50e1d1bac | -5.94579 | -42.65982 | 2024-10-13 04:40:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3903597-c5a0-3067-865a-84918f7ee76c | -7.93811 | -43.17717 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f211d839-2ffc-34b8-afe7-db0d85978a08 | -7.74142 | -43.3013 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26b4a1f9-026c-34ca-bf99-3a9317188fc1 | -7.74081 | -43.30558 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1105a39d-3dfd-33ec-9e8f-953213e04393 | -7.73701 | -43.30059 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a895f42d-2273-3f3a-95c0-9ed2a7de1d70 | -7.73319 | -43.29562 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63eef3b7-5af4-3659-af96-5ab5d8d75d02 | -7.73259 | -43.29991 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a30e3bb4-ad62-3275-be50-0a6dcfdbb6f9 | -7.72818 | -43.29922 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c462f710-3854-36e0-8ae4-80cac3d5e782 | -7.72376 | -43.29851 | 2024-10-13 04:40:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28ad08cd-9a72-3a1c-b668-9ddf902d3307 | -7.71865 | -43.17207 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7cd93c7e-f34d-3f2b-bce1-f9aafc6c5da6 | -7.71593 | -43.16967 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bccd4647-3806-38c0-9f45-0bf8ebbf9fc1 | -7.71266 | -43.19222 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b824fd13-ae07-35ea-b45a-4bae2c3bbf44 | -7.712 | -43.19675 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a4fe714-bbfe-30a9-9e13-c35ab640f264 | -7.71135 | -43.20123 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e7d68c36-c64d-3009-88f6-4e056df5efe6 | -7.7111 | -43.19399 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36cfe5ef-1228-3121-95e0-6e1fd8377e48 | -7.7107 | -43.20565 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| fee69b2a-ed7f-33db-8649-0ef0b5e9b56c | -7.71048 | -43.19851 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| faf09b0b-65f9-3fa3-9385-15a63cafc52d | -7.70986 | -43.20298 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e64fce67-7572-3d98-9eee-4ca904b89fc5 | -7.70926 | -43.20737 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 22d498ee-57c9-3490-bfba-4c602006b8fe | -7.70886 | -43.18705 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8f6b69e6-9705-3854-82f1-b2d763deeec1 | -7.7085 | -43.17976 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7072ed58-b6d4-3eda-9159-7942404d7226 | -7.70821 | -43.19157 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c94623aa-51bf-3920-85cd-5888e19ba13f | -7.70788 | -43.18428 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb91e86e-3e81-3fc2-9325-8507cc9cfceb | -7.70727 | -43.1888 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ef5b30f-af56-3a9b-849b-1091c520b60d | -7.70691 | -43.20054 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5c99b407-1c60-3206-b464-6be33518ac1e | -7.70665 | -43.19333 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e6fd5e1-cc2a-378d-97eb-96b4f3df2017 | -7.70626 | -43.20496 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 087a03a3-59e3-3949-9d59-d2617aba050e | -7.70603 | -43.19783 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 044999f3-1423-3633-90a9-c8de9ec18257 | -7.70542 | -43.20229 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4ef80dce-3d45-3036-8b2a-e33885c3b925 | -7.70506 | -43.18192 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67279f9a-4e2c-3f91-ad0e-e7cb271a5d32 | -7.70311 | -43.19542 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d6e4ee44-585d-3d1b-8ec9-ffe17cf6a3b5 | -7.70247 | -43.19985 | 2024-10-13 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73c50e4d-5133-3a55-9408-86a85b832d94 | -7.60442 | -43.03569 | 2024-10-13 04:40:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 163a0ab4-6cc6-340e-8bdf-d34945a6955a | -7.2947 | -42.23212 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08274175-2310-3fba-857b-157be9dbbf66 | -7.29325 | -42.23105 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 075115c6-cd8f-396a-9d47-f4c45f0f1310 | -7.218 | -42.28691 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f7631dbc-c98b-3407-9385-b4c948443212 | -7.21661 | -42.29695 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50a4829e-5abf-31ab-93f2-2651123aa050 | -7.21328 | -42.28632 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f5af8f21-6c05-3322-97f7-defba5ff79be | -7.21259 | -42.29131 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ec9e2ee2-41c5-3c88-98d6-92362bd9005f | -7.20858 | -42.28559 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5340f42b-8e17-3a7d-996f-07e8a6d588c9 | -7.20459 | -42.27969 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0ec05abb-1196-3f63-985f-da159dd59894 | -7.20389 | -42.2848 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3eff2bdf-b70a-3eb8-91bf-cce75646d7f7 | -7.16071 | -42.59772 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b652b014-e89a-378b-8319-d520404b62e9 | -7.15612 | -42.59693 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82ed67a7-69d3-356a-8c02-01174563d534 | -7.13907 | -42.65264 | 2024-10-13 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 50f7e524-98be-31f5-beb5-cf5f34fa64cb | -7.07894 | -42.64715 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 60cb2957-ae52-3d6d-b961-7bb368e41503 | -6.81944 | -42.7611 | 2024-10-13 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 434a3462-7394-3733-aede-a1a497cf45de | -6.81879 | -42.76574 | 2024-10-13 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4d6b2313-0326-371a-8a2f-283298c52e14 | -6.63292 | -42.19373 | 2024-10-13 04:40:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f620b8b0-7356-3450-abd4-e9438282e4bd | -6.53375 | -43.38166 | 2024-10-13 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 433313bc-cf7e-3020-b748-2f3a247363fd | -8.13727 | -43.0171 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| eff15423-69fc-320b-964d-57e630223707 | -8.13404 | -43.00724 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e9753bcb-5072-3f4b-a238-da3a697c6cba | -8.13273 | -43.01649 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e1a45d24-6b93-3581-bfd5-ae1f8e2e4b45 | -8.13209 | -43.02098 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c28fdce5-7892-3c40-a5b1-01ceac944b90 | -8.12497 | -43.00591 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| aeb85294-580d-337d-94a9-a7891930a283 | -8.12432 | -43.01052 | 2024-10-13 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 223941b9-32ab-376a-88c3-6f361e055945 | -11.10905 | -43.33543 | 2024-10-13 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fea5634f-e29f-3e52-8a96-f3d901e3b279 | -11.10838 | -43.34037 | 2024-10-13 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f6eb54ed-3fc4-341c-8460-01ad6ab65537 | -12.12489 | -44.74348 | 2024-10-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20064f16-8ac6-38c9-b49f-853f38a4da24 | -12.12417 | -44.74131 | 2024-10-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 886ae221-2023-3cc9-b4ac-36f43e169e41 | -12.12118 | -44.73877 | 2024-10-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f646e4-b47f-33ea-b6d4-d7709a4125b7 | -12.12062 | -44.74289 | 2024-10-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d49f8d1-5afc-3c7d-9c7d-b1ca84983d3c | -11.73954 | -44.48804 | 2024-10-13 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e037b4a1-5032-3c8f-be23-52744e97ff13 | -11.7379 | -44.48477 | 2024-10-13 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a806665f-94ad-3f1a-9b4d-7997d9e5df97 | -11.73522 | -44.4874 | 2024-10-13 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 646f6bc1-646a-32dd-821e-de7c2490ce1a | -11.45894 | -43.93293 | 2024-10-13 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4d6bc110-62f9-3309-9bd8-2ce4aa1f1b29 | -11.44785 | -43.81116 | 2024-10-13 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8ba95eb-8512-36c3-bea0-be6012d6734b | -11.25682 | -44.19895 | 2024-10-13 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c032e91-2343-3b38-bec4-519b64c00519 | -11.25472 | -44.18106 | 2024-10-13 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f4700ab-76f4-3cfb-a0db-7b86459f8b6f | -11.25034 | -44.18043 | 2024-10-13 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34f13593-3cd6-3e29-8381-7510ce8d4256 | -10.78689 | -44.30955 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f8acd3b-488b-37e9-9378-7b7bed793172 | -6.54079 | -44.02392 | 2024-10-13 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9394549-505a-34c2-a7dd-02cafba8bdf0 | -6.45461 | -44.27402 | 2024-10-13 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09545803-d11d-3dcd-bf06-40aacf743f36 | -6.45052 | -44.27362 | 2024-10-13 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec5cd011-dd02-37ac-b75c-e8f03a11775b | -6.40979 | -44.51979 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a557a010-6161-3730-9c93-016c56a7d403 | -6.40927 | -44.5233 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fbd70b3-47d5-3896-99f8-bfbca143c94f | -6.36925 | -44.09138 | 2024-10-13 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d87f70b-1143-336c-9028-f6e97faeab03 | -6.32673 | -44.97006 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b2a7b31-4576-3444-bc34-4b45cc0d211e | -6.25065 | -44.80603 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508cc769-6afb-3373-9cc2-41f501e1aec8 | -6.20751 | -44.50535 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0925294-a9ac-3143-9698-5e19429a3741 | -6.20353 | -44.50474 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8bc853b-b1a9-393e-ad43-608f71ca5a33 | -6.16014 | -44.60532 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cc18fd4-36b4-3e21-a27f-414bf2771eb1 | -6.14915 | -44.11536 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 161f696e-fd3f-386a-a135-fe4dcb6605e7 | -6.14221 | -44.72624 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30b9f69e-b87d-3e68-8930-11c50d910736 | -6.14147 | -44.73127 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74e0385b-09da-37c8-a075-4115f333a508 | -6.13829 | -44.72565 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README60.md)
