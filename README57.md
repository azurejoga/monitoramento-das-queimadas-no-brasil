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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ba0ed35-0eef-3723-be94-e874b3209350 | -2.86222 | -54.03904 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| debea761-cf70-30ad-bae1-df2176cc1f0d | -3.03609 | -51.77995 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64b0d2c-8b3a-349f-bf1c-1cd6ebe1d2e3 | -3.3188 | -46.62851 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59b65c53-a322-3937-8941-eeff96bb286d | -1.23504 | -51.8025 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 955883f5-36d2-3edb-b3aa-8ca7f1d3cdf1 | -2.70463 | -46.12061 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e25de98-1eac-3c8a-8344-9f1137624f7f | -2.71992 | -48.59188 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 546ce762-fa00-3f09-8704-c7eeceb5f641 | -2.22944 | -47.76746 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b3208a-a999-3035-a666-b518742d7e56 | -3.14886 | -53.81966 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f9355b-f951-3a41-85de-b319cebb2919 | -2.1175 | -50.62728 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 308e38f6-9cf2-3b67-a55e-1d01f599ac69 | -2.8506 | -54.03358 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 450acccd-e477-3e1a-a0b5-5cf043516c0a | -2.65494 | -46.6124 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1412bbf-ff5d-30aa-95e2-ecd3f8d08569 | -2.15475 | -46.4918 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9305b086-95db-3358-8a38-6d43e68638b5 | -3.6386 | -51.02034 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76353445-4e58-3dd9-8375-60ba84faf9d3 | -1.31018 | -51.75696 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fdeae237-5223-3cce-9668-0ae6dfdc0cd8 | -2.26493 | -53.46573 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aec88f99-d2da-33e9-b581-f76c6f43670e | -2.91469 | -53.06633 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ece8f088-a9d4-38b6-b8cc-4181a84adaa7 | -2.70817 | -46.12116 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c08a552-6124-3219-8a03-2aa1144a5b60 | -3.94732 | -46.6892 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb0dc88e-1008-3aeb-aee7-31655231d74e | -2.62547 | -46.25867 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 817cb43a-57ad-359e-9801-5fc2aae00c8e | -3.35904 | -49.09666 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e29aa562-7cc0-3325-8a96-1130d8c93dd0 | -3.51377 | -42.17969 | 2024-11-30 04:40:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8599531-f68e-3b2b-99ef-f8646f80e8a9 | -3.47273 | -50.53823 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2398013-da5c-35f7-a8bd-f2d76384c3ad | -3.23941 | -50.94728 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 648acd01-9a6a-32b3-b811-294107b20543 | -2.31814 | -50.64354 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ac8f0d0-9ff5-3cb6-a051-d1bbd636ba47 | -3.18882 | -46.60549 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669c2786-40d0-33ec-b633-68b33d06ec24 | -4.02145 | -50.44473 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 821370cd-a511-3cf0-ab82-ba76484d83a5 | -2.60738 | -51.80739 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd04fac9-bb13-35be-b0d8-1d290d462160 | -1.04226 | -52.17073 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae4d6f7-897d-30a0-902e-4516b23ddc5f | -2.57677 | -46.19566 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbb10ac3-8ed1-3aab-bf93-3b688fbb6322 | -1.13556 | -51.67298 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 549585e9-5722-3fad-8921-302e19b0512b | -5.74544 | -46.18218 | 2024-11-30 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87297164-966c-3a43-99c6-fb2526d35669 | -1.28683 | -48.2732 | 2024-11-30 04:40:00 | NOAA-21 | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 826fb530-38f1-3860-9cb5-d44bfa9fdb3b | -3.23425 | -48.73959 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e712fc20-ba23-3a57-96b3-139eb644f097 | -3.97168 | -47.24395 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443fdf28-d6f2-3577-bf8d-c12a8c9b9999 | -3.98785 | -41.50788 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5468cb7f-f7ea-32a0-8c64-5d50c4370d3d | -2.12374 | -48.37891 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc35b6cf-733e-373e-8180-48955ee05366 | -3.02865 | -54.01765 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93423c65-85dc-391b-8317-0959f109e9c8 | -2.57342 | -47.00806 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b575f37-a64d-31cc-9979-41560e7e6b49 | -3.44584 | -42.19764 | 2024-11-30 04:40:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 256d4f89-da1b-3113-9349-1056be3adeb2 | -2.69601 | -46.29636 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dab1c7a-bc65-3451-86e2-461925f40ca7 | -2.87656 | -47.86737 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d8439d-bca0-371f-9912-9aeb8b3e16a1 | -1.60709 | -55.43892 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e89ec03b-df58-3e9d-ab66-0cfea7d0a3cb | -3.97203 | -50.73467 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f113031a-6cd1-3418-9ece-d86891ee5e5a | -4.86266 | -41.3074 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec44b990-1b50-34b3-b828-253c7360e3b4 | -1.12149 | -48.32789 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f215dd57-db20-3357-92ba-3d2512ddb649 | -3.97596 | -41.52197 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e001763e-6a9c-31f4-846f-161f7dbebd58 | -1.83509 | -54.52961 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fc4a8800-9459-3db8-90f2-db8366454f69 | -3.7379 | -53.3702 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 244785a3-dd81-3a04-a9dc-62b7e79e9e28 | -3.452 | -54.62204 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c96cd4fa-7089-3474-9f21-588854ae5c36 | -3.92992 | -51.17602 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ac49e42-850c-3035-b042-918c473ad0b7 | -3.96532 | -48.82908 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4364c5b-4af5-3d58-b13c-e6d76db580a4 | -3.25381 | -53.644 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 45105d86-8528-3d1f-9ad2-b85bfe4fb898 | -3.30364 | -50.27376 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2db66b3-f86c-36e9-b03f-96ccada7d33f | -2.59033 | -48.20079 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 988fe55f-446d-339d-8995-83b44f14a8d3 | -3.9881 | -49.96677 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f395304e-cce2-3028-98a8-d7d6edf1f9da | -1.109 | -48.3646 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9e86d94-9f12-363c-953c-6ae3306c4214 | -2.79957 | -54.04023 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3e660d9-0b2b-3d22-ae2f-71ee830e69f9 | -2.73554 | -47.98911 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184d0ddb-93e8-351f-907c-a63ace001a1f | -2.75189 | -46.09533 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36ff1505-d455-3792-ae64-8cfd96949cc8 | -3.26738 | -48.7658 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a74e51c0-1e43-3ea6-be71-58abc4b81bba | -3.93272 | -46.40274 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c911bf8-c59e-380b-889e-d8ee4a3a9e47 | -3.28267 | -50.60469 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae3a5d46-b1b6-3896-9439-bc606e1d7914 | -1.71832 | -46.22425 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c2d558-c804-37eb-ae60-8e778cb8c201 | -4.02869 | -46.98557 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec5a9db4-92c7-3d94-a187-64726f797337 | -1.58763 | -52.08708 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecdf4a27-d502-3e19-ac37-bac12ea915a1 | -3.11425 | -53.9813 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe876ad8-e68f-3e16-bb30-195bd1e4bbea | -6.79009 | -39.44961 | 2024-11-30 04:40:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 256acce3-3573-3283-b83b-dec4c5bb110c | -3.9098 | -46.5285 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 422058a1-8961-3a2c-a1c8-ee3860d96511 | -3.24308 | -50.20634 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aae86f9e-85f8-36b3-b966-7b1587cfab51 | -3.77354 | -51.6799 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 405cb2fd-de83-32c8-ac5a-8f74b9911235 | -2.78587 | -52.99568 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1ef5eec-cbe2-3b54-ac01-112830c5d9e4 | -2.63233 | -51.76559 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781925a0-d8b2-3c31-80b8-6025fafaa77f | -3.10524 | -53.11148 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ab7ed5d-823b-3dae-a458-cf0bb68b0c97 | -2.03062 | -53.49727 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96a8a76a-c450-375b-b03a-7d35b2c53ce7 | -4.03937 | -48.33024 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3278455-5a64-3ac2-b3ca-cae2366eabc3 | -1.25655 | -54.54847 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02fa0ff1-e184-33a2-b943-57ce4165e543 | -1.39251 | -46.49776 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3401e282-35e2-3cf5-b912-467fda0c9829 | -8.32029 | -44.95021 | 2024-11-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 762c88db-1666-36ad-9828-f8ed1cdbf7a6 | -1.08262 | -52.43191 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51cf00f3-9777-3461-8282-39d34a9de221 | -0.95354 | -51.65939 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6dd8a0ce-3aef-329f-89b9-24039ac3a6a6 | -0.81982 | -51.60609 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55149923-ffe2-38d4-a681-6dbd78a45afb | -1.14639 | -51.67465 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0b32935-dfa5-3486-81c6-8d694a835642 | -0.23608 | -53.76026 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4904b236-ed1e-38a7-833b-53316d60626d | -0.95057 | -51.65469 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c4cd6e4-a2d0-3a67-9b88-3a5a9c0e8216 | -2.0456 | -54.67706 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94d4d677-2aea-325d-80aa-eeb90efbb1d5 | -1.28951 | -51.72397 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5bd97a6-0ea4-3a80-af93-258b216174fa | -1.13095 | -48.35393 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1029f986-c201-33ec-a054-a013ef483156 | -3.96479 | -48.83252 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea9728a-9256-3ef1-845a-eaa901f444f0 | -3.86643 | -50.15582 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d76c46b-2aa4-3b47-885c-34747347c8a1 | -1.54808 | -51.93373 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a9b2ee3-bc6d-3c2e-af6b-8fcaa3c094bd | -2.70079 | -46.12122 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6407998-d107-311e-97c5-a41f6a54b420 | -2.53971 | -47.97983 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05e3dcd5-0acb-3f8a-8aea-77a20ae4cc72 | -2.67438 | -46.10499 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f29d7e2e-2844-3747-aaba-67128b42c838 | -2.26808 | -53.47135 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44f4ef72-3c6c-330f-8325-4e4141c1c051 | -2.32708 | -50.67851 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4832905e-5937-3db1-95b9-a34dd29ed8c5 | -2.91791 | -48.58789 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051e07b1-a629-3eec-abcb-72f21ff6311e | -3.10341 | -50.3597 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b54ce80e-fe0e-3459-ac00-507a2455ffc2 | -1.94682 | -53.34217 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0e2e43f-3c8e-3c6d-ac17-097aa05b8c3f | -3.24526 | -50.14867 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7ef84f9-ab7d-3285-b9f4-cb2560e7dcfe | -3.46055 | -50.22961 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README58.md)
