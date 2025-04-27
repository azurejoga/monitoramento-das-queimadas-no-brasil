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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cab5c7d-96b4-3a1f-867b-53b07f27b4d5 | -11.3963 | -52.9477 | 2025-04-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 080ba40b-09c4-3351-909a-a33da38d6302 | -11.3963 | -52.9477 | 2025-04-27 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| b49bb825-9862-3b02-a1dc-759f0c03f47b | -6.5631 | -51.1126 | 2025-04-27 00:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1f0f770c-f268-3393-bad7-922716cd111f | -11.3963 | -52.9477 | 2025-04-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 17a8be9d-4d89-363d-89a4-7bc621cf5e57 | -11.4152 | -52.9458 | 2025-04-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 558fde39-2e68-319e-bf21-104766838e5e | -11.3963 | -52.9477 | 2025-04-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 5aeedc65-0db1-3177-abfb-46ac07f73c0b | -11.3963 | -52.9477 | 2025-04-27 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 7278bf28-5645-31ca-8977-0424c5d5dcc7 | -11.4104 | -52.950298 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a218a1ec-b960-34e8-b71e-841194d2f913 | -11.4072 | -52.9361 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2f55224-3616-3169-9c3b-7ee301f17635 | -11.4088 | -52.943199 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f53a3f80-2461-3132-8c80-e6851c4afd4a | -11.3974 | -52.9384 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab314cd5-7736-3d31-a18e-d598e85d1014 | -11.4056 | -52.929001 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee67c36-a1b3-30b8-a59f-5253117f98eb | -11.9681 | -44.148201 | 2025-04-27 00:41:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9aab9a-e3f7-3eb4-ab03-ef499be121be | -11.3958 | -52.931301 | 2025-04-27 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0d3aacb-776a-31d2-87b6-a3ca24ba233f | 2.6709 | -61.074501 | 2025-04-27 00:44:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 537f9ad7-dc55-3f8c-b051-99b6a274926b | 2.6688 | -61.083698 | 2025-04-27 00:44:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bfff4785-257c-3f40-9ef9-cf8fb9b94a70 | -11.3963 | -52.9477 | 2025-04-27 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 112fe2a3-e872-351d-af02-2e45fcc6ea8d | -11.3963 | -52.9477 | 2025-04-27 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| e71a55df-5a87-3bb3-9a75-d90e17b74be7 | -11.40406 | -52.95828 | 2025-04-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 8b1388c2-7771-39cb-9171-260ad40d8e97 | -11.40268 | -52.94875 | 2025-04-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 035475f9-2f95-367c-bfc3-9648e2dd21f0 | -11.97706 | -44.15102 | 2025-04-27 01:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| da609243-cf0c-318d-a93c-936cf28848bc | -11.97382 | -44.15864 | 2025-04-27 01:09:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 9158b799-70af-30fc-bf9c-607152afd368 | -11.39358 | -52.95015 | 2025-04-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 0ef59f5f-1a71-3c3e-ab9e-af677fdb1464 | -11.39219 | -52.94059 | 2025-04-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a1bac01b-763f-39c2-b705-8519b4da4ce3 | -11.4013 | -52.93918 | 2025-04-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1dbef486-d0fa-3550-91a7-9ac7598073b1 | -9.21731 | -60.33273 | 2025-04-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 162507a3-89e9-3479-9b54-27e8367b1325 | -9.22625 | -60.34198 | 2025-04-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9b482a44-23f7-3f54-95ad-81e9326391f1 | -11.3963 | -52.9477 | 2025-04-27 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b024c674-b8dd-3445-9faf-433277086eb0 | 2.68175 | -61.09609 | 2025-04-27 01:13:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| de6527fe-4934-3317-bbbe-b529423ca139 | 2.67148 | -61.09453 | 2025-04-27 01:13:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5e5e49a-f906-3ef7-8cba-21544512fc8d | 4.36959 | -60.80756 | 2025-04-27 01:13:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb1506c2-6685-35fb-b2f3-92b4c536f3d1 | 2.41695 | -61.67302 | 2025-04-27 01:13:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 76efd723-052c-345c-9fb2-ee6231a3ed0b | 4.37118 | -60.79635 | 2025-04-27 01:13:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28ec8b7b-ab43-30ea-ae44-65443ac23c7d | -11.3963 | -52.9477 | 2025-04-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| fb68d606-cfe6-335d-af62-768f583078eb | -11.3963 | -52.9477 | 2025-04-27 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| f75aabfa-4ae6-3b31-964e-fb340e0086ef | -9.2261 | -60.344398 | 2025-04-27 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3880785c-2036-3866-87dc-29dd59fa44c7 | -11.3976 | -52.955299 | 2025-04-27 01:33:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa3105f7-e170-3207-86a1-dda17bdf9585 | -11.4072 | -52.952702 | 2025-04-27 01:33:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9c6d69-b78b-3746-bdc0-2185f49f96c5 | -9.2245 | -60.3372 | 2025-04-27 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 767755c2-69d5-3e1c-b721-8a106311350e | -11.4027 | -52.935398 | 2025-04-27 01:33:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcb0f06a-dee5-3fc6-9232-253db099718f | -11.3931 | -52.938 | 2025-04-27 01:33:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7b1aa5e-a68e-3ba6-93b1-06bb13150a27 | -11.4117 | -52.970001 | 2025-04-27 01:33:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee68e998-24c5-3352-af79-d604327efd1c | -6.5631 | -51.1126 | 2025-04-27 01:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 11697c41-06bc-303f-baa8-a6246d636c05 | -11.3963 | -52.9477 | 2025-04-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b4a2cbdf-934b-37cb-8b93-c1cf68ac92c2 | -11.3963 | -52.9477 | 2025-04-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 0125bf1d-6970-3238-a3c5-6a9e8fcffb48 | -11.3963 | -52.9477 | 2025-04-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 10a66eda-78de-3f5b-9b3b-8e5e95345cb0 | -11.4152 | -52.9458 | 2025-04-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ea21ad4d-2c05-3de4-9597-779fed484bbb | -11.4152 | -52.9458 | 2025-04-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 932e5f31-1cd6-30f3-b6bf-233b073be80e | -11.3963 | -52.9477 | 2025-04-27 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1ae5978d-8489-326a-a402-74b65cff741b | -11.3963 | -52.9477 | 2025-04-27 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 9098bce2-72b5-3e10-a855-f4cc3b5625fe | -11.4152 | -52.9458 | 2025-04-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 6c5389cf-7f6d-3440-a7c9-2326ff84964e | -11.3963 | -52.9477 | 2025-04-27 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 5b855fc3-bfab-3bb7-81be-8583442da2b7 | -11.3963 | -52.9477 | 2025-04-27 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| ab495d12-5488-3660-9f45-778b8eb031c7 | -11.3963 | -52.9477 | 2025-04-27 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bb58504d-cb4b-356c-ad86-b7d85756b196 | -11.4152 | -52.9458 | 2025-04-27 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 070522b3-c717-3004-948d-012b0da6cd54 | -11.3963 | -52.9477 | 2025-04-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 32179d7e-c600-3f76-aaca-df3e6306ca3c | -11.4152 | -52.9458 | 2025-04-27 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cb86f10b-3173-3a9f-ad89-769ff4b7ddb3 | -11.4152 | -52.9458 | 2025-04-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 558f7b93-9eb8-31f7-8966-4d1dac330caf | -11.3963 | -52.9477 | 2025-04-27 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c3012948-0d50-364f-9b54-af633eaec8fa | -11.3963 | -52.9477 | 2025-04-27 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b1bd0605-3f04-3f12-98a6-ab2faa1dd0b8 | -7.32925 | -34.79972 | 2025-04-27 03:21:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8e134c42-cfb1-3046-ac80-ce106a425158 | -5.43954 | -43.34754 | 2025-04-27 03:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ede3605-0307-303a-8da4-fab90fa14812 | -7.33132 | -34.80229 | 2025-04-27 03:21:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0bcf1a47-9369-39bd-b42b-0322b3f2bdaf | -8.07344 | -34.97606 | 2025-04-27 03:21:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 244fce24-aa83-3ab2-b4df-122ffa700efe | -5.31818 | -35.49888 | 2025-04-27 03:21:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3db57950-d0f4-3319-b829-43aabfee0014 | -9.61853 | -37.0265 | 2025-04-27 03:23:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87994232-4e77-3d55-bedc-b32fc074b0c4 | -12.24827 | -41.37925 | 2025-04-27 03:23:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bfef1512-8a4e-319a-95bd-3da95036106e | -9.62138 | -37.03535 | 2025-04-27 03:23:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13f117ba-e5d8-3dab-83c4-c86ae62f0490 | -10.33378 | -37.0167 | 2025-04-27 03:23:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c98b373-e55b-3261-9992-401494b999cf | -12.2472 | -41.37755 | 2025-04-27 03:23:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6352c838-1491-37a7-9351-3177802d19f6 | -10.33349 | -37.01725 | 2025-04-27 03:23:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e7f704a-70fc-31ce-ac04-5d33ad7a84d1 | -13.23101 | -42.00764 | 2025-04-27 03:23:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 28e5061f-efda-38d5-bdf5-af95d3de039f | -12.24654 | -41.38105 | 2025-04-27 03:23:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 73aeefb5-2476-3e9f-b860-1726b3cd0a51 | -22.69868 | -43.34756 | 2025-04-27 03:28:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5107c1aa-d286-3d9f-a572-49282101d564 | -11.3963 | -52.9477 | 2025-04-27 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b56650f7-4459-3c4d-acb6-4f2395e7f68f | -11.3963 | -52.9477 | 2025-04-27 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 6fe9b725-76b5-3895-8fbc-c22e40cb682d | -5.22289 | -36.14423 | 2025-04-27 03:47:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a8a99281-3cb2-32c0-b81b-266308cd3767 | -5.66206 | -35.75505 | 2025-04-27 03:47:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a3c1ffd-496e-33a7-b0b2-aadadbaaccc1 | -5.67272 | -37.21458 | 2025-04-27 03:47:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4cdfa19-8d32-367e-80fe-081ea160b3e4 | -6.84731 | -42.80216 | 2025-04-27 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d18a84a9-3aa7-31ec-96fe-9ac5b6e0979f | -5.43762 | -43.34341 | 2025-04-27 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31cd7a5a-fae5-3aea-9d78-f5adf51084a3 | -10.332 | -37.01579 | 2025-04-27 03:49:00 | NPP-375D | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9aeeeb6d-1f31-3ef3-8533-40281bc097f1 | -8.53043 | -42.22128 | 2025-04-27 03:49:00 | NPP-375D | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1f828b7-6f2b-3173-a20c-8fb69bbd08c2 | -11.97199 | -44.15494 | 2025-04-27 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c56993d3-a8dc-3034-9a09-e55446edd59b | -6.2574 | -43.78865 | 2025-04-27 03:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 296f2d98-dcb2-3162-a65d-113e52913476 | -9.61987 | -37.02607 | 2025-04-27 03:49:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 669903ee-cf10-32a5-98c1-78a84cdb7d15 | -5.43683 | -43.348 | 2025-04-27 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d808865f-caed-34a0-ac0a-a1250eca2481 | -10.33425 | -37.01634 | 2025-04-27 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 16321e81-3039-34ec-8173-f6f43c19f88f | -8.07275 | -34.97604 | 2025-04-27 03:49:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4f8cce8-8e87-3a20-bbbf-11e729aa8ada | -12.24607 | -41.38103 | 2025-04-27 03:49:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9ae6a65-df4b-3324-9550-97cc3df5781a | -9.61932 | -37.02959 | 2025-04-27 03:49:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2014713-c587-32fb-b02b-026e59fd19ba | -9.62211 | -37.03363 | 2025-04-27 03:49:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02b97871-9b69-3e48-ac29-00b0796a270c | -7.00404 | -35.01496 | 2025-04-27 03:49:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 741f14ad-76ba-3364-a8c9-5aa95e9423d3 | -12.24679 | -41.3768 | 2025-04-27 03:49:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e78f225f-a4fe-399b-a448-bfbb66a852f1 | -11.3963 | -52.9477 | 2025-04-27 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| b4e68069-dad2-3bc3-a831-2e1601703511 | -16.3483 | -43.69865 | 2025-04-27 03:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 730bec10-e686-3b55-b72b-e13e6eeb614f | -13.77906 | -41.24965 | 2025-04-27 03:51:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9c18d7ec-1d98-3568-8ed4-d3d019f9b10a | -16.68025 | -43.88207 | 2025-04-27 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84d1a385-dc6e-3a19-8531-d882fccb15b0 | -20.41757 | -43.55439 | 2025-04-27 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 84218235-4bc8-351c-b233-571a6148e0dc | -22.90009 | -43.75217 | 2025-04-27 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
