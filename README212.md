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

## Dados Diários - Página 212

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c849cea6-b49d-3082-b9a3-c303fc11012e | -7.2185 | -55.1016 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8fb74f29-d5dd-37c1-b18d-c59df6126132 | -9.8442 | -47.4608 | 2026-10-08 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 59c98712-ac7f-3e46-a293-ce2eb1a2db2d | -8.1876 | -54.7219 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f1fc6df6-1bdb-357e-aeee-e11c3bf0401b | -8.1875 | -45.781 | 2026-10-08 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 61b49260-ff3a-3069-88bc-511f306c756c | -12.1545 | -44.7547 | 2026-10-08 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 236.4 |
| aef57dad-6484-3dcc-9b0f-105784eef729 | -10.4337 | -47.2824 | 2026-10-08 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 221.9 |
| bf1d0026-dad9-30c2-8cfd-532d323a19ed | -8.2826 | -45.7038 | 2026-10-08 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a26bc405-3256-3cdc-8cb6-10b303395bb8 | -9.8439 | -47.483 | 2026-10-08 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4e259c1b-c948-30ce-9555-a28c5de559a6 | -8.1878 | -45.7584 | 2026-10-08 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9e4b1600-d782-3784-832a-f10cd3c6c425 | -12.1738 | -44.7517 | 2026-10-08 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 99621933-db2b-3c45-8486-f2e5a41e51eb | -8.0709 | -55.3121 | 2026-10-08 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bc053029-63f5-3137-bd64-07aee48876f0 | -8.0895 | -55.311 | 2026-10-08 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9a5ca296-de84-3bdb-9a3a-98ff4268b8bc | -9.475 | -64.3525 | 2026-10-08 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 848a2411-eb1a-395c-a9c0-79e85a31df54 | -9.738 | -46.9398 | 2026-10-08 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5d2ea8e1-e751-349b-b856-05a6cb5e61eb | -7.8876 | -55.0023 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| bb1c1e58-cf81-3821-8b26-bbebee8bdd51 | -7.2371 | -55.1005 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5463135f-5814-3831-9e2d-3a7d7427bbbe | -10.6722 | -47.83 | 2026-10-08 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 795af3f6-d588-340d-8d44-d088ceddf556 | -13.1641 | -54.3178 | 2026-10-08 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 1f7fca87-fb02-383e-b116-187bb045c09e | -7.0065 | -59.1223 | 2026-10-08 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| b1055960-bddb-3518-80b1-3075f36ae4ce | -6.7366 | -55.1274 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e588bd4a-bd0b-337e-8c57-fffebd9d1420 | -10.4527 | -47.2801 | 2026-10-08 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 234.9 |
| c06aae70-2faa-3e52-b081-462170c5303f | -11.3103 | -44.8337 | 2026-10-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 952de53d-77e6-3282-acf9-1b2ac5263af7 | -9.9398 | -43.5542 | 2026-10-08 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| e69d67b4-2827-3311-8970-abdfc664004e | -11.7932 | -46.7733 | 2026-10-08 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6f1a5de9-837e-340b-9a11-70d00be1c063 | -12.1733 | -44.775 | 2026-10-08 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 741884ab-4e2b-3a10-b4bb-6b6d5c107902 | -10.4334 | -47.3046 | 2026-10-08 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| af807fb3-988e-32da-93dd-698096d20203 | -9.0592 | -65.9209 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| bdedf13c-c7c9-3a8d-ab6d-b11e697c170e | -13.3671 | -43.8742 | 2026-10-08 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ea0cb92d-4647-3293-8aa4-3411162419fe | -9.8253 | -47.4629 | 2026-10-08 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 2fe7f1d9-28a0-3486-8f89-0f5356cfd3f7 | -9.9014 | -44.8147 | 2026-10-08 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| ad29f7e1-3cdb-3e8b-a040-621dd3b4d5c6 | -8.0711 | -55.2921 | 2026-10-08 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2e0b72f2-adae-3409-9b89-fbb1d968311e | -7.869 | -55.0035 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6b3d9106-02f2-355c-b06a-c01d75ea4bf3 | -7.8874 | -55.0224 | 2026-10-08 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 4a3da6ce-f6fe-3361-b7df-df4457844fd9 | -13.1833 | -54.3158 | 2026-10-08 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 243.0 |
| fc065d71-0c58-3ac0-ab2f-3cd522e9707a | -7.4697 | -42.8315 | 2026-10-08 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 85749810-58aa-3d89-ac04-38e73380759f | -7.5284 | -45.8885 | 2026-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| dbb5c7d1-e30e-3fe1-914d-fbfab4e3f9c1 | 1.6937 | -55.6263 | 2026-10-08 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 647daf7a-dbbe-3cd0-a0e8-7b3ca08081eb | -8.6107 | -67.0116 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 035cd5a8-910c-30c8-ac1c-7b5a3ffc354f | -11.9832 | -57.5867 | 2026-10-08 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fc794308-5e40-3807-8a33-4dfca9d8dd6c | -8.6107 | -67.0301 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 293.1 |
| 1594ca54-4460-3315-a7e4-172f3396db51 | -9.9018 | -44.7917 | 2026-10-08 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 116a1a4e-9064-3e93-bd19-606de37dc40f | -9.1543 | -49.8142 | 2026-10-08 13:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b6ee32f4-d518-3408-a612-a80d8816d9fe | 3.0733 | -60.557 | 2026-10-08 13:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7df680d6-f6bf-3384-a32a-c2cc22726bd6 | 1.6937 | -55.6461 | 2026-10-08 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 3c0c8794-95e5-3d8a-9ee6-0d6a06f96a94 | -10.6912 | -47.8278 | 2026-10-08 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a0cb260b-a01f-368f-8bbb-429e74579ea9 | -8.6106 | -67.0486 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.8 |
| bb037112-330f-39f7-b654-5a255ce334d2 | -8.6291 | -67.0482 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d7949cec-1d59-3ed1-8a63-1458ec10030a | -11.335 | -51.8673 | 2026-10-08 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8ca3e7d1-d096-3dba-8f98-6deb07ab12fb | -13.1639 | -54.3385 | 2026-10-08 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 6d780481-a9ea-3f8e-9509-4a39e0e8a755 | -9.825 | -47.4851 | 2026-10-08 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 39800c7a-c1f0-3f02-9f82-4b5d511240b9 | -7.0066 | -59.1029 | 2026-10-08 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fd2eed4b-f288-37ee-a636-a432c0cc2a81 | -7.4694 | -42.8551 | 2026-10-08 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| eab1f9a4-bb2d-38e1-8cb4-8fd2ca308357 | -8.1996 | -46.3415 | 2026-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ca936800-3fe3-3027-bb2f-4248bfee6a8b | -7.5286 | -45.8659 | 2026-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 22a9c0d9-e0c7-3c96-8e8e-116d04147914 | -13.3865 | -43.8708 | 2026-10-08 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 9f71d00d-bbfc-31e7-bf66-b45a441820d6 | -8.9501 | -45.1334 | 2026-10-08 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 0c8fee5f-8366-3008-b26d-71a4d3d6102c | -11.3539 | -51.8654 | 2026-10-08 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f433a747-ed47-3ea6-8db3-431661dd5b1b | -8.5313 | -46.911 | 2026-10-08 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9f74b553-3765-3d07-aeb1-be3c42ec6339 | -8.6292 | -67.0111 | 2026-10-08 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 587a21ad-2c39-37ce-80a0-29284a220927 | -11.335 | -51.8673 | 2026-10-08 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 87df21e9-f641-3177-aefb-b6d37fb7264c | -11.3103 | -44.8337 | 2026-10-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 04cefcca-9862-3906-854a-ee4460afe5ce | -7.2369 | -55.1206 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ba1c733e-ea7f-3f0a-8827-20a7e9e271e6 | -10.4334 | -47.3046 | 2026-10-08 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9501754f-8d40-3367-b61a-a2626f02c20a | -12.1733 | -44.775 | 2026-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0df155b1-3977-33ee-a94a-627827b3afa2 | -7.0065 | -59.1223 | 2026-10-08 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 269.4 |
| 6e0ebb97-8ab2-3d4c-bdff-a969a92f70eb | -9.1543 | -49.8142 | 2026-10-08 14:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a51386c1-e72b-38d5-8abb-a09217093531 | -11.6173 | -43.7142 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6087c2b8-014b-3ecf-8a11-9a71ea53f623 | -8.1996 | -46.3415 | 2026-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 44352317-5db3-374d-b8b3-1c8a44d20ca4 | -15.5546 | -44.5275 | 2026-10-08 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 2e905bf4-b80c-3afb-b07c-d0eb1de31928 | -7.0066 | -59.1029 | 2026-10-08 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 9dffc15b-3e7b-33df-a2b8-2c2371bb0ae8 | -8.6107 | -67.0301 | 2026-10-08 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 321.5 |
| 2aa0dc7a-f952-3880-a51c-4f360fc86153 | -8.969 | -45.1313 | 2026-10-08 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 16d82a22-f737-3327-9d7a-78a7b5e45599 | -8.1878 | -45.7584 | 2026-10-08 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7748886c-ef0c-38b5-a921-2feb884151a1 | -11.394 | -46.6697 | 2026-10-08 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 702ce944-fb3a-3938-a72d-3d4f3cc75014 | -6.988 | -59.123 | 2026-10-08 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 38d430f9-841c-3737-8f0e-06bbb16e159c | -11.8408 | -47.3496 | 2026-10-08 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4a0eca64-290c-3124-9cc6-9b1c59c4a07b | -12.1922 | -44.7953 | 2026-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 74165e1e-d2ea-34cb-9548-8918920d0b3c | -7.2185 | -55.1016 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 78966c65-5ed4-35a0-8615-6307a3f208a6 | -6.8292 | -39.5472 | 2026-10-08 14:00:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 4c3342a6-4f42-3daf-86c5-802b9737a0e3 | -9.0592 | -65.9209 | 2026-10-08 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| cb73a542-1457-35cd-96e5-fc30219e89ad | -7.2184 | -55.1216 | 2026-10-08 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 72c68456-618b-30d5-8ad7-4fc6dde7f9b6 | -11.2657 | -45.209 | 2026-10-08 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| ed10ade1-c5a4-3cb0-b8f6-63ce0b0196fd | -11.6562 | -43.6846 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| da78f543-b3fc-313d-bc30-e55bd396c08d | -8.6292 | -67.0111 | 2026-10-08 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 1cdbaf82-0dad-3c13-9111-51659e8986cb | -9.9014 | -44.8147 | 2026-10-08 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c7764794-36b2-394f-93f5-748c59f3e361 | -11.619 | -43.6196 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c417c8ce-8a70-3f64-a80c-f0436700e565 | -8.6106 | -67.0486 | 2026-10-08 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 13abb8a1-107b-332d-bd2c-e9949b8ca82d | -7.1889 | -44.3272 | 2026-10-08 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 83c83e3b-d6fd-3f1d-8d59-dc871fb1dc02 | -9.9398 | -43.5542 | 2026-10-08 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| f4e31567-403c-3e8c-a863-c22b1351217e | -10.6722 | -47.83 | 2026-10-08 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 673d4795-dff3-3d77-8418-1391f6d246c8 | -8.0769 | -45.5886 | 2026-10-08 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 2a49a68c-3ca4-3667-a65d-c43840a41b42 | -10.4527 | -47.2801 | 2026-10-08 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 67db6684-1a8b-3e38-beb6-4df4b3f6aed6 | -10.6912 | -47.8278 | 2026-10-08 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c1f6b20e-2ab0-3245-a81b-684cdf7c6c51 | -7.5286 | -45.8659 | 2026-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| e06f4397-f179-30e3-95ce-bfb491f1c0cd | -10.4724 | -47.2333 | 2026-10-08 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| eb0ae220-446d-333f-9649-16cf0050aad8 | -7.4694 | -42.8551 | 2026-10-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| ba89b67c-1b11-3269-9e3e-20e911ed55d0 | 2.7641 | -60.0106 | 2026-10-08 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| da4ac978-5627-3903-93d6-022bc6194601 | -11.6186 | -43.6433 | 2026-10-08 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.1 |
| 5921f76c-d82c-351d-be7e-537971a1df61 | 1.7121 | -55.6063 | 2026-10-08 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 57fdc9e5-8979-31e5-9379-ba8fedde142a | -13.1641 | -54.3178 | 2026-10-08 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |


[Clique aqui para ver as próximas entradas](README213.md)
