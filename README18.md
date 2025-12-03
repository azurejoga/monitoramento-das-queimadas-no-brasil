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
| 7fb9e593-ccc5-37a6-aa12-f39cc902b24e | -2.63456 | -48.03815 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483e72a8-189f-3ced-a4d1-ef4a83dd7ece | -3.23729 | -45.57123 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c63d5042-379c-3c6d-8ef5-ce2fb7d30c13 | -2.65888 | -54.36081 | 2025-12-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19862144-c01d-30ae-986c-2ab0c410e219 | -2.38684 | -49.38908 | 2025-12-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27b8e61c-749b-36e2-8c8d-4be0f017a2c8 | -2.62407 | -45.14001 | 2025-12-03 05:08:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e7a8f51-cd61-310e-a803-9fb1e10bb7fb | -3.22409 | -46.86209 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f86634ef-b4b9-38c5-9e9e-e75b34bb554b | -2.78599 | -52.95282 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea335564-9600-31eb-8023-0a63788025a7 | -3.22293 | -46.86267 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f222e0f-f4a0-31c5-84b7-ee64ce10db90 | -3.24317 | -45.53154 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 949443d4-5583-3996-b00b-6d334701de0d | -4.67223 | -46.30978 | 2025-12-03 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb2e9b57-8174-3e3f-b45c-f34054a8a8c9 | -2.70182 | -51.89651 | 2025-12-03 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a497d839-dfe8-34b7-90cb-1947cccdf234 | -3.85022 | -47.83152 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91f8e853-6d64-3d68-ac91-f5f12f600107 | -1.19698 | -53.08908 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6be71c9d-8b45-351a-a9d4-52864dd096cd | -3.77954 | -50.00484 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc8518f-8e76-330e-ae71-ae54c620553b | -2.89643 | -53.29516 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 735425ae-44be-3344-a99b-6735ee8a96fc | -2.89587 | -53.29882 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96279535-41c4-365d-91c5-3df779bc10b5 | -3.86017 | -50.50245 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d061e21-044c-35ad-826f-855d80db04bd | -2.39103 | -49.38971 | 2025-12-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e775cb92-c7d0-359b-8fc2-5830e0b3e294 | -1.91242 | -46.28289 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ff5413a-73cb-3c92-81a5-4781d34e05d7 | -3.47363 | -52.98946 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9932d3c8-180e-3d3f-9e68-bf38a9e16f25 | -3.77545 | -50.00418 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a05f6ba-aca0-3844-9b17-297c2e2669ef | -3.23889 | -45.56039 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5df1d7d4-3486-3e22-85f6-6a86a26029ed | -3.05264 | -48.42334 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b8b5a7e-28d4-3e34-ba79-8b54b1f0fb37 | -5.90381 | -43.71444 | 2025-12-03 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c4cf358-298a-3e77-a39d-e19d956bedb1 | -3.22712 | -46.86935 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8078855-bd90-3733-8130-e4957c26a8ca | -3.59493 | -47.27077 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dde22337-dc92-3f57-b2e8-1f66a6feb5ec | -3.24263 | -45.53516 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c4d1362-d3bb-3191-89d7-436eedeafa8e | -3.53261 | -49.99062 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e29c9fd-d8fb-3668-8edd-9c0ce330982e | -2.20188 | -47.99671 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff0a155-3f03-3bed-a976-76a81dc991d9 | -5.38523 | -46.76053 | 2025-12-03 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d21920-2cdb-3ca4-9439-562c5d55446e | -2.93971 | -53.28668 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc08e6f9-d3f1-38bf-8413-e07c0ace59c9 | -2.84254 | -51.05824 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff65388-a944-3379-9133-011a79ac65c5 | -2.45279 | -49.32756 | 2025-12-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edc86d7f-22e8-339b-837c-2835cffa3da6 | -2.57243 | -49.10321 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec265313-aba5-3c82-9c61-2b0e9473bd49 | -2.92249 | -48.23259 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c60cdc53-c11e-39e9-b3b1-18b11ca6ae9a | -3.59582 | -47.26501 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3983c2b2-9131-330a-9dd4-f4a304a70a92 | -5.38616 | -46.75392 | 2025-12-03 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48e1950b-5282-3952-b82f-4102adf00085 | -2.83399 | -50.46274 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8328f25-d937-3420-98cf-a8a4c78e465c | -2.14924 | -53.53665 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0611bfc8-81a8-33a1-a126-c726c99d6ed5 | -2.96347 | -48.58777 | 2025-12-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 769a838e-5bbe-3da4-98de-fe065e883074 | -2.85534 | -46.73441 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6fccf4-e762-3271-a989-14615eec9fdb | -4.07263 | -50.49692 | 2025-12-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ee606b8-baa8-3e88-8410-af959b602534 | -2.24823 | -52.77224 | 2025-12-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e8948b69-60b0-379c-abd8-f51b6e7178b4 | -8.05317 | -43.09777 | 2025-12-03 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92566f2b-bb4e-3a49-abcc-418863f43d8e | -1.8663 | -48.02059 | 2025-12-03 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa52e0cb-ddbc-3eec-a54c-cd6d5bc46f65 | -1.9317 | -52.12135 | 2025-12-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d7f74f1-1d0d-3e88-b7e2-e4f335435b88 | -3.85152 | -47.06036 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc6e53a6-b0ee-3116-9f3a-5e4c07e4b239 | -3.19035 | -41.85971 | 2025-12-03 05:08:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4cc37eab-2cbc-3794-8e93-e2febd4d06f7 | -3.04812 | -48.42262 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddf93b9b-e3cb-3aef-8185-1cbe1d3f50ac | -1.57517 | -53.78874 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0345d440-2b78-30db-b78e-163bae01b54e | -3.85739 | -50.50459 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04c6cedb-dc29-3fa4-b6b2-44d95eeef7b1 | -1.06173 | -53.10164 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57f3f056-1577-3b0d-80e5-0b5b7a1ba24b | -2.63527 | -48.03342 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41e2f56c-8192-3e5d-9e52-7d110ef6709f | -3.30815 | -52.56794 | 2025-12-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cca5344-cd61-3cdc-b98d-7b9fe7a437c9 | -5.9041 | -43.71381 | 2025-12-03 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf13a9ff-63a1-3574-8d74-b61221863d38 | -3.23836 | -45.564 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7faee9da-bc30-3364-8be8-2315dcc7f6f2 | -2.69118 | -51.79691 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c43abe-ed1f-3819-bddf-a4441d131af2 | -2.97974 | -49.51359 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff763a7-25b8-3d5b-903e-bf3e47f86052 | -2.96557 | -48.58572 | 2025-12-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fd32e157-38f6-3b52-af83-ab11544453be | -2.8549 | -46.73734 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b3ea4c8-a715-334e-aedb-90ada8eafbad | -2.98694 | -49.52258 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a196ec97-0eda-3028-834f-51123c9bc316 | -3.28703 | -50.07863 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fa34371-70e4-33ff-b4bd-ee06296501a4 | -2.38427 | -48.95333 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8febde8f-9d52-35c5-b44f-b00f5ae23d4a | -2.24768 | -48.31199 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0efc36e-1996-30a1-b317-da88b86573b8 | -3.24564 | -50.15949 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 365ceba8-9df3-33a7-a126-0d4079a2fca7 | -2.92889 | -53.26637 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a558713-1238-3cc5-8547-4fd3eabcb58b | -2.93174 | -53.27056 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa837b9c-1df0-3251-b0c2-b57da2928a5b | -1.29404 | -53.18129 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b132de8-c538-3da2-a699-1458d4407551 | -2.78907 | -47.4352 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 411f4b13-7e7e-325e-81b8-2c8c6a12797a | -4.07374 | -50.49862 | 2025-12-03 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4351a5a-3c74-37e2-9c75-d67587a4469a | -3.8447 | -47.83592 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5c05578-437a-3fdc-b81c-70b8fd8713e6 | -3.22015 | -48.6143 | 2025-12-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22f5dd37-7e77-3c57-becc-c618be371eb5 | -3.31167 | -52.56847 | 2025-12-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 534439b8-16ed-303b-b156-24210988550d | -2.82963 | -48.44495 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1645adf3-7370-3fc5-b22b-02b3fd081155 | -3.8511 | -47.06327 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c89f9983-2bc8-3d08-8836-af5bd073a7fd | -2.43919 | -47.19353 | 2025-12-03 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d28bb2e-689d-3a18-a75a-ecce67936a6b | -2.78988 | -47.42997 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa651f44-1087-318b-bfc3-597f1e17e9ab | -1.98516 | -46.47995 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88e9a74e-9d0f-3ea0-ac7f-eff167cb1dfd | -2.20576 | -48.00214 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| defb81b8-ab10-35c7-a608-54ab87b4cc6d | -3.19287 | -52.02422 | 2025-12-03 05:08:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 231d396f-06ef-3f3e-8eee-44776c4f3179 | -2.89302 | -53.29463 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ce3ca1b-3c5a-3578-842c-5f41f4312184 | -2.3533 | -50.11075 | 2025-12-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 42928e31-5ace-38de-99c7-87a052ef4f78 | -2.09163 | -53.41441 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4300794e-af6e-3914-b538-57cd6644d075 | -2.17379 | -48.36549 | 2025-12-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acea8b7b-bd2b-35da-ba08-bf89adb31c82 | -2.93686 | -53.28255 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa875065-c71e-3ab5-9449-a0a8fc2c2155 | -3.84946 | -47.83667 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75b13f7e-4415-367e-9519-4a3b09e28637 | -3.75767 | -52.66463 | 2025-12-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a65e68fd-ff2d-3ada-8d20-1c628702ca2a | -1.62263 | -54.32293 | 2025-12-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 246ab93a-8f3e-3bfa-ab7e-044be126398a | -1.94191 | -52.10257 | 2025-12-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7528900-94d6-3b71-a078-fac288c24923 | -3.00119 | -47.89769 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03832104-270a-3c96-9533-b89002cf1f17 | -2.4089 | -48.64766 | 2025-12-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8779235e-7465-3cbe-8a64-226ea0bcfea8 | -2.32077 | -48.57906 | 2025-12-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63731f1e-3e7f-302e-a8ac-03ecdeab924d | -3.19593 | -41.85688 | 2025-12-03 05:08:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ea9fa017-9121-31ba-8746-9df8edf11c26 | -2.96413 | -48.58336 | 2025-12-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eec16d9-35e3-3797-9de4-c6485ab1e8ac | -2.70065 | -49.31271 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed34291-b367-32e9-b541-9443be391691 | -2.82858 | -52.83976 | 2025-12-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffdf2086-61e9-375f-aec3-6e805a69d15f | -2.66107 | -54.08605 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8d2567-9891-3396-8c6b-6f5f9bb7e347 | -14.67801 | -53.41114 | 2025-12-03 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e79a0e66-5d0b-3128-973e-90dcc04edc13 | -10.19905 | -48.09476 | 2025-12-03 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d64fa1-7975-3eaa-9516-4e1ca3542140 | -12.85093 | -52.518 | 2025-12-03 05:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
