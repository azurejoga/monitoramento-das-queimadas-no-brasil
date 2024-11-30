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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7966033c-e4a3-32bc-8e4d-51ec13a85ef4 | -2.68039 | -46.275 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7047af0-5a24-3ea4-859d-dd3a7bdb99b4 | -1.28256 | -51.74419 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 890d5368-7222-32b5-883f-852829dd37f3 | -2.571 | -51.83624 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fddeb9ab-2124-3c37-878f-e30f85f96f06 | -5.27749 | -50.05254 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a31097-5040-3bc0-9ff6-faecf3563e04 | -1.71455 | -52.63112 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3043837-0186-31fb-80d3-62ca0dad2e7b | -5.76245 | -46.60949 | 2024-11-30 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47b8a245-61f0-32b2-acba-0faae9ac3f5c | -4.2045 | -50.6854 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ccf72b3-6ec0-3b59-a5d0-56a98ba3a689 | -3.76193 | -50.17192 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b6d4564-a756-32d0-8775-4d40d4074919 | -4.09559 | -44.85694 | 2024-11-30 04:40:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea57c337-4395-3d17-a021-c7677dbf0092 | -1.24417 | -53.35707 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e98749c4-714e-340e-9ffe-f4e41bf661c3 | -3.73068 | -49.87265 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f1d543a-0a94-32da-9845-241d5528888c | -3.12053 | -53.27643 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 053a6393-c1f8-38dc-b83b-bdea80a08ffb | -2.9499 | -48.33868 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac47e36-7d36-36e3-95dc-9fea0716165a | -1.4724 | -55.12862 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaeefd1f-3805-3c38-a0a6-b65376dc3359 | -2.14833 | -50.60938 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa9e4c1-ec5e-336f-bc08-912f9c7fd430 | -3.09218 | -53.29398 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0a334d23-7ee7-3bbf-bdb6-48da3e59daa2 | -3.29585 | -51.07862 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a34caf0-0e43-37a9-b0bb-248db0dfbe5a | -3.25692 | -53.64963 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd27a2f2-cc6a-39c3-b143-c948b280fd6e | -2.98548 | -49.59221 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a31c66a-5326-3bda-97fa-31a3b3837a7e | -4.0488 | -48.33529 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c327a3-9a32-3a7b-b420-f1720f85405b | -2.27283 | -53.46695 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ce0d117-adc0-38da-8ca5-12bb60479a99 | -1.44694 | -55.20253 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efbc9603-49ac-3881-b346-79a1ef8d4c03 | -1.87459 | -48.80083 | 2024-11-30 04:40:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90a6c104-a8af-3d2a-9298-435a61164f20 | -2.27789 | -46.4209 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c239a4-92bc-3753-be64-1890c84e817e | -2.44647 | -46.50767 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c379ec87-631e-354a-b19c-46e2536efc28 | -3.35007 | -50.51577 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07e88a88-5e47-3d84-95e9-08f8817c5d83 | -1.29607 | -51.72923 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d925f62d-ee69-36a3-97a5-3d6a75f0b47f | -6.90258 | -43.54203 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e5ab155-60fe-3fa6-94ab-8ac141913f0c | -2.69435 | -46.11617 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e03b301-0821-39b0-ae4a-9a36d7a336b7 | -2.67146 | -46.10048 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85327b3e-9d6f-39e8-a9e3-2c6b47ea8f43 | -2.7699 | -55.3387 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 517af400-73e0-3129-b7b5-97c7f0ab0986 | -2.69391 | -48.27753 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d7177d-09bd-3d2a-a392-a3a6489c067f | -1.61741 | -52.35582 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08382d82-c6e5-3a95-a6cd-fce10cb25de1 | -3.31315 | -50.49852 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 089e151e-c822-3d60-8a31-684fa78d42b5 | -3.70567 | -47.14774 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e13b594-241c-3654-9be7-0ac75a5998b5 | -1.70174 | -52.63854 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9a6de5e-d782-33c4-9010-f0dd58e22cd1 | -3.06581 | -53.91507 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 619cae48-cd84-357f-bf67-a0af34ed9d22 | -4.02391 | -46.20657 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69209d9-724c-3020-8a46-f28a155b0205 | -5.03932 | -49.98637 | 2024-11-30 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37ea7b9b-d054-3c4e-9de1-1a8a0b95cf23 | -3.26679 | -50.20266 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4aed03b-3a4a-323f-bd9a-3965f1d43445 | -2.29441 | -51.33352 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3945006-0a28-39f2-bb85-a868945ad7dc | -3.5334 | -50.21904 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ea6cc6b-0e43-37b7-8578-84ac927f4e21 | -2.19222 | -50.57473 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b24eafdb-c7b4-3f72-b06f-2cca577563bf | -2.61389 | -51.81256 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a441a247-641e-3b79-95f3-6b24d39d65b2 | -2.69902 | -48.59571 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9ad98a2-7a45-3ae1-9a0f-68ce6aa77e5a | -3.96178 | -46.73479 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 470f8ec6-ca10-3950-8bc4-fc0708249e2f | -3.84701 | -46.65832 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac6bc98-53f0-3da1-abc9-1f8840e4d63e | -3.54509 | -50.18831 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b9d3ea7-1acb-3006-bf38-be47b827e0ac | -2.37506 | -47.87974 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6be958-3f69-3bce-891a-f7dae3638cab | -3.36073 | -46.40096 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1566214-2449-3db3-bf32-bd70f7de448d | -3.13991 | -50.44607 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b3bf674-2868-3625-9f3e-abd0026ef1f3 | -3.2657 | -50.62433 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4dd3282-f3c6-3fa6-a64e-db3206e5e55b | -2.69848 | -48.59914 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e213d0b-4190-37d4-b16b-b41165276fee | -3.03054 | -54.18749 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d14ee6f1-a686-3dc7-91da-5fb83bd9616a | -2.66655 | -46.13224 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6ec3b44-8c3b-3468-9592-ceadea4ad4fb | -3.02257 | -47.80386 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70962e1a-628c-31f7-9b79-dd63451697b8 | -6.90754 | -43.53847 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8fbbe704-bb23-36da-9b4b-d28d600280bc | -4.04648 | -48.30632 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11311605-6589-377c-b5a2-084fb58f4688 | -3.37432 | -50.82486 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b773f8fe-a4e5-34de-bd4d-8a0c6edf16e5 | -3.89057 | -46.67693 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf14ef5c-996e-35b8-bf2c-0338e6b31bab | -3.05771 | -49.54382 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0253196-e95b-3e7b-bbc8-a0cccedc208b | -3.14828 | -53.82322 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70a10e8a-c416-3eea-a311-b331f5c3508f | -2.74644 | -48.61708 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f20e729d-717d-3f6a-a979-44a1af21301f | -2.78885 | -51.6703 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 322f333b-5db3-35b0-a073-85190d8e9c7f | -3.03412 | -50.98095 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d71efbe-6a6e-31b2-aca3-c206ff8a09df | -2.47915 | -50.40635 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d06cdc58-1813-39e5-a5b4-97badc8718bc | -2.639 | -46.24074 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 458355d3-d861-33e8-aa2b-6fdc2d226300 | -1.22315 | -51.73636 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af476139-7fcd-3938-a024-8e1939f99696 | -3.09388 | -54.02448 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97aed4b9-23bb-3dd7-a50e-69d3e794194b | -2.22201 | -51.42686 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc7e4410-8c58-314e-bcda-87eeec8c8f9a | -2.14437 | -46.49023 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 766ff561-d6bb-306f-bf94-afbf7c6106f3 | -3.24636 | -51.34655 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94707b79-e377-3435-adbb-191ea841725a | -3.77415 | -51.67598 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 447f3039-5cdf-37de-8c36-8b327539c3c0 | -3.37392 | -50.17576 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e492829c-0950-3b64-8956-8a83a052fd98 | -2.76921 | -48.56086 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fae10f6-988b-3109-af24-2e6f46793552 | -3.27737 | -45.57139 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d12447b2-c6af-345b-a29c-dbd99bcb744d | -4.96292 | -47.59261 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24613b3b-c7bf-3dbe-a091-28ac1b5c6735 | -3.26962 | -48.77319 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6181b1b-f8f2-3cc5-bc2e-5c8789b526d4 | -4.6265 | -48.02808 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 969485c6-c87e-3150-8a68-cf15550d70f4 | -1.23782 | -51.61984 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 385b12ed-3f0c-34ec-a51b-8caef8403adf | -2.96112 | -53.89151 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d2387df-528f-3b32-9a80-dda76e2ce1ea | -2.70204 | -49.81571 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 361e3ee8-f9bd-3ae0-af1d-d8bfc20e3ece | -2.12102 | -50.60517 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87157079-1dca-3221-ae73-06741cce6bed | -2.78492 | -49.82858 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c45947e-2859-30d1-9237-7b33eda08e7d | -2.38117 | -47.88426 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c1cb2e-dd0d-37f2-8951-bec23d3fb15a | -2.37236 | -50.59132 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44fe9f68-8559-3ab5-914c-76b207aad302 | -2.80705 | -49.77474 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d69d212-7586-38ae-902e-78c97c717b9f | -3.33089 | -50.05719 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb629930-9365-31be-9012-b97bf84c1a4e | -1.14393 | -53.66602 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bafba543-09f0-3b2c-9a52-2093043f3696 | -3.28773 | -50.61661 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd72fc2e-af9e-37e5-bb23-5110a08e2b1b | -3.11744 | -53.10848 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5073b741-0160-35af-8929-cfbd261e888b | -2.69599 | -48.65855 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e8dfe2-0426-3634-823d-e17106485a47 | -1.09954 | -53.38962 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d57ea7ce-48bb-3c65-b40e-883083d6a9bc | -5.30925 | -44.71711 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b556f9cf-0443-34c3-ba89-de8545dda157 | -7.97135 | -50.68098 | 2024-11-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5c61de-0d44-3730-b673-66ece75833ef | -2.70051 | -46.12402 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85eb2ee6-cc0c-312d-99cd-984a43f8fded | -1.27378 | -51.62539 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83344d67-7adb-33f0-9530-f7895aa1f1c3 | -2.86842 | -53.99973 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5812fadf-8129-3210-8505-5d94cb456f02 | -2.146 | -50.62412 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d8327c-74a2-32cd-860d-5480d9fb1105 | -1.06934 | -53.63623 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
