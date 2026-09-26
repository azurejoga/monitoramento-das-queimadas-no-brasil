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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e308c8dd-8f59-39aa-a471-8227664a5680 | -3.87195 | -52.28652 | 2026-09-26 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be2e8c28-df16-3a73-bf95-82391a9a43a8 | -5.77745 | -45.10875 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8863ef16-895d-3431-8bea-5004cef33a45 | -5.61731 | -45.23933 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7131ecf2-c3bb-37f2-ad89-d56d9da8ff78 | -5.77964 | -45.07361 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe4a8866-dc4e-3394-9af6-5d45f2678b4b | -4.60624 | -44.65331 | 2026-09-26 04:25:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72b7e8d5-9744-3de6-a56c-cb276fb70063 | -4.29468 | -50.89843 | 2026-09-26 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 603f6f81-aa9b-30ae-9ca9-9d8c8bd7d7f9 | -4.45788 | -47.91967 | 2026-09-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b163ff99-b637-3e82-b189-9086a363e55c | -2.91069 | -54.11831 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c1ce0acb-5ff4-3511-9dea-01db50b171f1 | -7.35604 | -42.08794 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 010bcb3f-9d8f-3671-8572-6921b73de9f0 | -6.59806 | -47.22927 | 2026-09-26 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f89facf6-1e73-344f-a6ce-22a948adc3f0 | -2.91407 | -54.16656 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b2c381e-9a18-3426-98ca-bf1040435932 | -5.12949 | -42.88125 | 2026-09-26 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d8d525e-543a-3b97-a28a-2820509b8249 | -3.41646 | -50.42354 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95192f2a-8a2d-3b8f-be79-5d8af005fca6 | -4.28381 | -48.60921 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c94167e2-9c6a-38c4-af40-666edc43039d | -5.77469 | -45.10476 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a270eca1-efd1-3ff6-9ada-f21a41467fd8 | -3.4129 | -51.66307 | 2026-09-26 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b1fe3ca-04a4-3be5-bb9a-ea26507b03e3 | -7.40842 | -42.63102 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7719936d-386a-38ef-8a7c-9b33e0266e24 | -3.22017 | -48.81868 | 2026-09-26 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65c1d328-b098-370e-bdf6-15059867e81f | -3.96796 | -47.20209 | 2026-09-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1502b960-34c7-354e-a570-5e939b1d95fa | -4.60679 | -44.64986 | 2026-09-26 04:25:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3262bba-eb63-3137-912d-3d6857360c35 | -7.61056 | -46.45734 | 2026-09-26 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f245e528-d603-3bca-84ff-995a1b98bf24 | -1.83523 | -54.72435 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 560db494-de53-3634-93e4-648e69a01ada | -2.16677 | -48.96802 | 2026-09-26 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c10afd5-3813-348d-8ac8-daa7c6c50f2f | -5.68559 | -45.87184 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca5f6b70-73d4-3424-867a-1d481b6532b4 | -5.74432 | -45.06094 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e334b95-e4d1-3274-b4b1-06c1adc03cd2 | -3.80089 | -51.01645 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5159a3fd-365c-3e6d-8fef-0628d25c7b82 | -2.75137 | -48.7597 | 2026-09-26 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dbf3b0e-1086-3b04-a0e1-a77ec5538b6c | -4.86776 | -48.91288 | 2026-09-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f61f1f-429d-352d-9a15-ff1782062c86 | -3.45037 | -43.37032 | 2026-09-26 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b7ad42-0d4f-33c4-8f0e-fa05b2b2d996 | -5.21349 | -46.02741 | 2026-09-26 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99df0e99-a31d-3153-a698-11e4e51c1876 | -7.40143 | -42.62992 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f03e0d1-4c67-3ef2-b734-b87496866e35 | -5.77909 | -45.07706 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7bacee-b994-395a-af91-1e1a2e316b71 | -7.14919 | -42.07122 | 2026-09-26 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64d9e2df-4ab9-3798-8c18-bad6a25a4ff3 | -3.94203 | -42.98803 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d39c708-7e7a-30e6-af41-8a3e3a148b24 | -5.73329 | -45.06627 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24651cf9-f4fe-3d8f-8699-8e0954054ade | -5.74322 | -45.06786 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fb6689cc-2f23-339b-acc1-bf2f0e3d6055 | -1.84195 | -54.721 | 2026-09-26 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 25ff2351-c28e-37c0-b018-f8090920e75a | -3.87064 | -52.28415 | 2026-09-26 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fe2ecb0-7545-374c-bc3e-8fd79a0d2449 | -5.78075 | -45.08796 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 37672661-f992-391a-be92-56dbe2312004 | -8.11614 | -40.74934 | 2026-09-26 04:25:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7b7c9fc-9f0d-35a1-af2d-2e526565708b | -3.4253 | -50.42749 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ed40860-fe43-351c-869d-8c4fd2be2aa7 | -5.77523 | -45.08 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed459da2-86b1-3177-a818-43b56dda7680 | -5.74046 | -45.06387 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 18090a25-8f4c-3847-91df-f3feb09f358e | -2.83545 | -51.35992 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2476b635-f78b-3de2-a797-378593e865aa | -5.77308 | -46.56396 | 2026-09-26 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97f276dc-ce89-3f15-9436-3926aeff4a8d | -3.50346 | -50.7431 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f61a448-a0ac-362f-ae18-7f951c5615dc | -7.35455 | -42.0848 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 082aaf77-1263-3232-ad1d-a332a9866239 | -1.13779 | -54.09304 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2bc1fd1-fd53-3be0-9943-a5d9c63924c9 | -2.45033 | -49.22358 | 2026-09-26 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845bce34-4601-31f2-817b-06d24af937eb | -2.91473 | -54.16268 | 2026-09-26 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3332aadb-7546-34f4-8898-fa0cfd6a91ce | -7.36618 | -42.09369 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 113cad04-6533-3a9f-89db-1aaab30f707a | -4.93086 | -45.81015 | 2026-09-26 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83d0cc6-5e27-33c7-bcba-737bb06722c9 | -3.94539 | -42.98855 | 2026-09-26 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2acffeb-cca3-352a-aca1-8e7249e1d366 | -5.778 | -45.10528 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5943a4d2-0c72-333d-a5e0-7ba9311ccc5c | -4.30167 | -49.13094 | 2026-09-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 086baed6-f5a3-35bf-87e5-2c0c6833bc45 | -7.40551 | -42.62656 | 2026-09-26 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 69d7f25b-3ae1-3ba6-936d-be84efde83b0 | -5.7377 | -45.05988 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14d7a2c2-dba5-3ecc-8445-daf96f889e84 | -5.68224 | -45.8713 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1371a0ad-216d-37be-930a-1180b149a38e | -3.9383 | -40.59261 | 2026-09-26 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 96f058a8-a146-3f9c-80d9-b592512d890f | -6.12918 | -43.73719 | 2026-09-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b87a815-e58d-3fd2-be1f-b2962cdcfa44 | -5.78076 | -45.10927 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ede8861-8cf4-32dc-a747-65d907fb4e96 | -7.35876 | -42.08124 | 2026-09-26 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28d446ce-6200-3b35-bbbd-5a5e16242d85 | -4.40653 | -47.79692 | 2026-09-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84fcebc0-4073-3de1-8332-02f2671fd552 | -3.80016 | -51.02078 | 2026-09-26 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3779de05-8243-3a24-b4eb-4ec207987c15 | -8.12003 | -40.75002 | 2026-09-26 04:25:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 034d853e-4e20-3e76-a06b-b76ae85c8f15 | -6.83722 | -43.50556 | 2026-09-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9a56aa2-adf6-3d1c-8da2-84eda0a9458b | -8.34568 | -44.14989 | 2026-09-26 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 954cde1e-16d7-3041-8d8c-ba2d4d869224 | -2.45292 | -46.05768 | 2026-09-26 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 767a192a-7985-3324-b29a-dc8c99255435 | -2.83856 | -51.3599 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eb8cc08-5f65-3b08-837d-512f660aebcb | -1.20204 | -46.74461 | 2026-09-26 04:25:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67238684-4afc-3827-b6d9-b7af0094c141 | -2.33221 | -46.26773 | 2026-09-26 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3f458e-af7b-35fe-a2fd-d0da0b240c60 | -5.77414 | -45.10823 | 2026-09-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 686dd26a-f881-3f68-ae5a-4cae658d874c | -1.14425 | -54.08997 | 2026-09-26 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11821649-aec3-3ddc-80f3-2283664346fb | -2.83407 | -50.48452 | 2026-09-26 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ea8f80-30cc-3418-8e0e-e1c92ad1677e | -2.44948 | -46.05713 | 2026-09-26 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b15e9f-0c86-32ac-9e0d-3d9e10b07936 | -5.48826 | -45.93865 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 485a3cad-c704-3bde-af54-2dbea289c954 | -5.68836 | -45.87592 | 2026-09-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bd475a7-4399-39fe-adc0-011d0245d476 | -11.16893 | -50.04295 | 2026-09-26 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5a6ce19-babb-3040-bb7b-1422027e731e | -14.82007 | -43.31487 | 2026-09-26 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef1a2e2b-21c2-3194-a40a-197652196117 | -11.73482 | -50.61901 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81da4c7a-46cf-330a-89e7-809cf0a3beb8 | -9.54276 | -56.15648 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ab223f8-4e01-3a08-a942-9d7e7a140476 | -12.00869 | -50.64529 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc4696e-5bc6-3f63-850e-6a0ffdfd2f94 | -11.92888 | -50.5927 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc99bb1a-be40-3279-9b03-c717fd4dfeaa | -11.13751 | -42.8219 | 2026-09-26 04:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3765b87b-3de5-314c-8c92-f5020cb5a79c | -15.57536 | -48.84267 | 2026-09-26 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 900001a5-34e0-387a-8275-7c3c4e8131b0 | -9.63673 | -55.13449 | 2026-09-26 04:27:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49eb86e8-d6f7-3629-a1bb-768de1bfdca5 | -13.71728 | -48.80344 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c0a72b9-02b1-3ba5-b7df-efcb67433349 | -10.41453 | -53.81398 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e41ce5f-f266-3103-869d-713227c78901 | -13.69243 | -48.8032 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88f17d5c-a4cf-3371-9978-5f8c68e29002 | -10.41939 | -53.81504 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8549b3f-cc74-38de-a285-95c9ff1899e7 | -11.28029 | -54.43683 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e06d89f2-f69f-315d-aa4f-3c53973c5a47 | -11.87361 | -50.56751 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 483c0748-349f-3b61-916c-fc19146cb7d1 | -11.9398 | -50.69145 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c9c750e-742a-3fd9-82da-876c10139f2c | -13.84054 | -49.68361 | 2026-09-26 04:27:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80fd09a5-ab1f-3eea-8b79-9e99168d038b | -12.60433 | -51.95338 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae94395e-68e7-34a0-a52a-d0313f1e2603 | -12.20492 | -50.34426 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4ac5df24-9f0a-3c72-9203-ffc66d6c17b2 | -11.01717 | -54.05463 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed9de22-d05f-3f6d-a563-c002826d62f9 | -12.26879 | -50.72187 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e7406170-bc1e-3822-bdc3-873c835a3cee | -10.75442 | -50.83553 | 2026-09-26 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a20f715-0ae3-39d3-8614-13f5e5b4898d | -12.26492 | -50.72115 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |


[Clique aqui para ver as próximas entradas](README16.md)
