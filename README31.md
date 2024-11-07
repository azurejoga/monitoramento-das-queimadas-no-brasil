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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fb6f545-2cfc-3e30-a829-37ae02869eea | -3.24596 | -53.40701 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c7d42e-9e5a-3af2-95f2-a003400206f5 | -3.53639 | -50.29375 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cca569cc-c814-3ae3-8071-f1147d2789ea | -2.94056 | -52.70525 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ea2250e-8647-30cb-ae39-3cfba5d7996a | -5.19432 | -38.02136 | 2024-11-07 04:18:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d4bcbf6d-9de8-3d24-9c5f-a9164133f3cc | -5.03373 | -46.84388 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42070500-2c29-324b-ae5f-11b771fb3719 | -2.90671 | -49.40738 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46417908-e500-3aa1-a3a3-1839579352f1 | -4.22726 | -50.64557 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02bf4693-e8ae-3507-9e35-cf8071652251 | -6.69273 | -43.05942 | 2024-11-07 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9445d1c-4d80-3f8f-82fe-388fee50e11e | -3.6148 | -54.21954 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ebe701-a439-363e-917b-2cb0234d485b | -2.83737 | -49.81585 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fb585c0-2e50-32db-8c17-b1a18773059b | -5.11018 | -43.96067 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 957152fb-fa62-34e6-8905-bfb0c9a2ca89 | -2.60346 | -48.2104 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fb848c0-b8bc-3998-b973-0310763acea1 | -3.2185 | -50.20111 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8710451d-3dd8-373d-aae8-f3236addef2d | -3.01339 | -53.44691 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19374d74-59e9-30bb-bacf-303354a5c67d | -2.40098 | -53.62951 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1b5e533-08a3-3fb3-a786-e545319e6987 | -5.11349 | -43.96118 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a9bde1d-b548-3603-ac1e-066564e25f55 | -7.0105 | -45.01316 | 2024-11-07 04:18:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8cd20ae-7bad-3612-a95c-7069d544f8d3 | -3.36558 | -49.76274 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08865459-a6af-315d-9b26-93bc02ae45bc | -1.14548 | -53.72277 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 951dfd98-e6d0-3ec8-957b-a0f0ac57a1a1 | -2.70569 | -46.67667 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d592659b-4ac9-3044-831e-fc422b7a5c7a | -1.32206 | -54.64325 | 2024-11-07 04:18:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb7fbfa6-271b-3bc5-9b35-a77727ffbdf7 | -2.60482 | -51.75763 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fe3c798-e667-3bc8-bbda-c32627740608 | -1.5183 | -52.54819 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a2f4ce6f-f179-3807-9fdc-1c0d755872e0 | -2.87703 | -51.47183 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20a3eab-028f-30e5-9e39-ccf83daae04a | -4.23727 | -48.54252 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21a08155-6824-38f7-8951-3c52f47453f4 | -4.42193 | -44.03599 | 2024-11-07 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2aae8f8b-3b23-3eaf-b491-14beb2f433ab | -1.38993 | -52.21478 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24615638-dd24-3e3c-8825-df45e4542ad3 | -3.17027 | -50.21679 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05d8d0f2-78a4-3c16-8152-6a44af2e8ae1 | -5.83924 | -46.262 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d97f9dc9-baed-3d6b-bb23-a6db6750935a | -7.24193 | -37.3326 | 2024-11-07 04:18:00 | NOAA-20 | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 005f8929-14d7-3bfa-93a7-5717a0174ac9 | -3.41743 | -50.38917 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ae9abcb-9200-3606-be7b-8ac0e25d62b9 | -7.57168 | -43.43086 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb3a6b4c-6956-3348-a8cc-8cffd5dd1b74 | -4.09288 | -48.32661 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 512f4703-928f-3c31-a183-011fefcb931f | -3.01634 | -53.42873 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d361c413-7ed6-3177-9d77-03b832cd2bcf | -4.71679 | -47.23721 | 2024-11-07 04:18:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34ab3908-33c5-301c-bbc2-f1b2314ba543 | -4.25044 | -49.65203 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0661fb2c-cf8b-3683-9a83-9efd9716f5eb | -2.07556 | -52.04257 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17320dec-86ad-38a5-8f67-07d36879ac60 | -2.83216 | -52.90403 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d61d377b-4d99-34b0-bfe1-7023768c56bc | -7.44593 | -43.24089 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7852d108-b85b-38a5-a649-8e241c8f825d | -3.08757 | -53.71453 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f717605-90c0-36ca-83b5-9aed8dd8e76c | -3.03259 | -53.27309 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1421f65-c884-304e-8973-e81bd33b661e | -2.80693 | -49.35433 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 735ab7eb-20e9-33b3-b2f8-55ae9c474d15 | -3.19716 | -53.39828 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c47f48-14a5-334f-a6e5-42ffbd26ab44 | -5.98724 | -45.35917 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 67b4a9f7-2507-3412-ad41-56fbf8aaf4d2 | -1.4582 | -52.58484 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d5d5939-0ec1-330a-862f-d87343fc0f4b | -7.44614 | -42.89582 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27a32c26-f0d7-3d50-9629-fb5d11fd04a4 | -5.77704 | -46.16624 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f66b06-5056-3fe2-8ef4-17a5cbf534f1 | -3.218 | -50.19871 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c157f67e-ed9c-332a-8873-e7d6acc55752 | -6.96305 | -39.83027 | 2024-11-07 04:18:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06be334f-1cf3-3667-8fad-ecda7a8996c2 | -4.76963 | -48.67931 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd99d462-49df-35dd-b958-60d09625f0af | -5.11295 | -43.96464 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5146aa21-9f71-3439-8621-811c3e0d1b9c | -3.664 | -52.34447 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b46e53-a76f-39bc-84ef-fb3a5a1a00b8 | -8.30896 | -43.62446 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b985c51-93ee-3868-ad0a-51a015f09127 | -2.23088 | -48.02412 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49381bf5-adc9-3a1d-bd59-47ae9535b2fd | -1.18914 | -53.89969 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5f1daeab-45bd-3861-b4e4-d280c59510f8 | -4.9929 | -46.89732 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea58177b-d09b-3b7f-ad19-d3870e7ec86c | -2.6153 | -51.30278 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 051599d8-a771-3e33-ad75-5c040af6173a | -1.14128 | -53.72152 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 567f64e9-73b3-3dcb-8a6a-983984a5a605 | -3.00794 | -53.44588 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b96987d6-7309-3f7c-bf63-e9d5e36c9554 | -1.38832 | -52.19241 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97c771e8-c823-391c-b1bb-dbc7a01a5226 | -3.01416 | -53.44659 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2626bf4-18fc-3d75-be34-14c136aef70a | -2.85068 | -48.44741 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac66a88-ebba-3c2a-8b24-46be473cabb7 | -5.62043 | -43.95519 | 2024-11-07 04:18:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a868f2aa-6152-3dee-b0f5-2cc4557b4fad | -5.4785 | -41.65207 | 2024-11-07 04:18:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77d243a9-b7b3-3563-8f8c-15cab51d82f4 | -3.9656 | -50.99287 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d49bd561-37f0-33ec-9242-192149aafa95 | -5.23228 | -44.9119 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6f6ee008-9704-3529-b6c8-6875268e6a74 | -2.4609 | -45.84735 | 2024-11-07 04:18:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db0f79e-1a0a-37e7-9790-e47fcb5cf718 | -8.30668 | -43.61669 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 77985033-07be-3a8c-887d-48f56f91e8c5 | -2.80972 | -52.94093 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ce5c4c8-434f-3427-923b-64cf3bb9dbee | -4.73362 | -46.65976 | 2024-11-07 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 962acb8e-2856-35ad-b895-7eac4837e91b | -4.7718 | -48.67733 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b803b8c8-b353-3ed2-980c-f705c791b452 | -8.34774 | -43.61935 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c7a287d-2251-3ab9-99c2-fa509bdc853c | -2.61921 | -51.30861 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1388c3b8-8156-3b0b-adc2-14127d57b34c | -6.10894 | -46.32685 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3815fcaa-356a-3758-9191-225a34375a14 | -2.62005 | -51.30358 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14d3ed16-9abe-3420-b08d-94ceb41e946b | -4.37788 | -47.24867 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6eb9515-adc2-3dc4-9bb9-d2e982d703e4 | -5.94621 | -43.69498 | 2024-11-07 04:18:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f0de812-b507-3bc9-94f8-d321544d4398 | -3.03682 | -53.28083 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9262fca-c85c-395b-a079-7e18ac9b2785 | -5.83585 | -46.26148 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c061725-090b-3621-a29b-3f1086d3c46c | -2.81718 | -52.92879 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22682634-ecf5-360a-9864-71fb0827efb8 | -3.19048 | -50.58763 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 498ed7bb-7763-32c7-8cb4-e469778f74da | -4.47888 | -50.48796 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3043cf9-af0b-389a-87b3-41234dccd4d6 | -5.96731 | -45.37747 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e04195-e620-3d8d-922b-7a00fa697f3d | -5.01903 | -44.36618 | 2024-11-07 04:18:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb9112dc-dec6-3573-ae76-250194286eb2 | -2.98505 | -50.30295 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bc957800-3162-3a52-8451-c1363fbb212e | -8.50133 | -42.07903 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 785ae22e-c9e7-362f-b036-6b23264aab4e | -5.81326 | -45.96124 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a87d503-4e1e-3581-8e81-07e9567f227b | -4.07086 | -48.31794 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 575d18ee-f060-37c3-9eef-51e8f972e2b3 | -5.98226 | -45.36909 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9aa03a8a-120c-36fc-aca2-59b3788c31fe | -2.67074 | -49.87825 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 366b8da9-0068-3fa5-b4b6-afd500f5f8c9 | -2.85028 | -51.77483 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb7e2daf-036d-3abb-ab47-e907bc39f38d | -4.24036 | -48.54796 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afb48fe9-1da4-37ab-89a6-0f0e9f07a104 | -3.22389 | -50.38544 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c088444-6f90-306b-b6d1-95df1d49da4f | -2.84991 | -48.67366 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c50d3d73-1cdb-3030-82f9-d9aea5b9fbf8 | -2.60503 | -48.20072 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8559e489-ead4-34f2-8448-5c49852f36ac | -8.5097 | -42.09669 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 36113c8e-bf16-31a9-baf8-55bfa15e6cb7 | -3.03541 | -53.27731 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aba65622-4e86-3cc4-89d1-5964f7dd5bf8 | -3.22713 | -50.44859 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22875675-4158-3bd9-a346-e166030617b0 | -4.25535 | -50.69503 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d7052a5-a122-3675-9dff-265ff01f9255 | -2.72112 | -54.14745 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README32.md)
