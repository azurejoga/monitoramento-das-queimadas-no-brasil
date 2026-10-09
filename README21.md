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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 108e0756-ad8d-3416-9aea-7b032e70aaba | -1.146 | -54.2199 | 2026-10-09 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 8c7452fd-08fa-378f-9dee-f51297046f37 | -12.0058 | -43.464 | 2026-10-09 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 27bef38f-0fc3-3f1d-9f4f-2b345e382aed | -3.1787 | -50.5597 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| fa480526-175a-3021-99f8-cd36781c12bd | -3.9912 | -59.356 | 2026-10-09 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1a61afda-7d20-3f9f-82ef-59c3661a81f5 | -3.1101 | -54.1661 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 1777d40b-88ba-359e-8af4-40281d3f8b76 | -3.11 | -54.1862 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| c325c835-82ae-3285-8a24-59b5a5248de1 | -3.5493 | -54.6951 | 2026-10-09 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| b9f6b6e5-ea9a-3b52-a9f6-621c83ad1733 | -3.0007 | -53.9075 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| e78832ed-8eca-33ae-ad3c-534324a8f40d | -9.7054 | -58.0854 | 2026-10-09 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| a396c01f-73f8-35be-8f56-8b31b566190d | -3.5493 | -54.6752 | 2026-10-09 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 4ed156dc-1291-36c4-9e37-2f6a2474da00 | -8.7231 | -45.1583 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 1ed756a5-ab08-33a5-b751-1ec54623a937 | -11.6562 | -43.6846 | 2026-10-09 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bf393d22-65b8-3140-a016-3d759cdd2bde | -8.7228 | -45.1812 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6c94ea4a-585e-3aad-8d92-e8b30590f638 | -3.237 | -54.6635 | 2026-10-09 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e49561aa-647e-39c3-8868-a81bef737562 | -3.1971 | -50.5801 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 29920e6e-09ce-3fd2-8285-717f6553a191 | -9.2973 | -47.4092 | 2026-10-09 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 7b284946-0261-394f-a93d-8f2b99c11bdd | -3.1285 | -54.1657 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 0383c405-e015-39d3-bf03-203cb4daa724 | -9.8629 | -47.4809 | 2026-10-09 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 67143dc3-5fa0-34dd-9628-a61216524506 | -3.011 | -51.0028 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8ebdbac1-16bc-3863-b3d3-1fdaca4c5082 | -3.1972 | -50.5592 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ddbdf20a-c72a-3a77-8f11-9e0929e93632 | -9.2781 | -47.4333 | 2026-10-09 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1688e223-0cd7-3006-acbf-fddfa08865cd | -3.1284 | -54.1857 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 941e7655-1a27-353e-beb0-1f81f3a0155b | -13.2015 | -54.3757 | 2026-10-09 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4c9acda6-a727-32a8-a7bb-03c302c5c659 | -9.297 | -47.4313 | 2026-10-09 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 8bbc41b5-d171-3d7a-8fe0-6c124533e8d6 | -1.1094 | -54.1802 | 2026-10-09 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| bf5d8b18-5916-31da-bacb-3f7fff74811d | -3.364 | -50.4072 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| fccc381d-29b3-3261-bc6f-418a20c44abc | -6.0076 | -53.4919 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 24f7df83-f692-39d3-a56b-9306f8b74c03 | -7.5649 | -61.5523 | 2026-10-09 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f6641eaa-1334-3489-b60f-62d7bd309055 | -3.1879 | -58.6433 | 2026-10-09 00:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9d37b26d-c331-3ddd-ad2e-a67461d1893f | -8.7417 | -45.1791 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 19754826-b20f-343e-801f-50d9ce1d7c2f | -13.1636 | -54.3591 | 2026-10-09 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0c4857ce-3cc0-3cd0-a25e-e1b87802191e | -10.0253 | -48.036 | 2026-10-09 00:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ffa9930b-e85f-3019-8d1c-5ebe270c38ca | -7.4095 | -44.7656 | 2026-10-09 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b21408ac-d84b-3c06-a924-0c1150a55d53 | -3.0924 | -53.9656 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 76f4800b-d214-37e5-bbba-f616574586d2 | -7.5834 | -61.5516 | 2026-10-09 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ce82215e-f9e7-3ab0-a351-edba5ed4b4b7 | -3.1108 | -53.9652 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fc8abdf7-69f0-3811-a8ea-bc59d7b5e81c | -12.2156 | -57.1087 | 2026-10-09 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 065b34e2-c56b-330c-bfc0-dc533367fa11 | -13.1639 | -54.3385 | 2026-10-09 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 64a6bd7f-2972-373e-b786-4fcc6b95aafb | -7.4442 | -63.5589 | 2026-10-09 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| a94b512b-5e0e-317d-ad87-3defc33323ef | -3.5677 | -54.6746 | 2026-10-09 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 7140f593-1552-3b0d-80e8-94121f3b5199 | -3.0925 | -53.9455 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| a4829930-e947-39f7-a34b-3001a2314a6f | -13.4922 | -44.3713 | 2026-10-09 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1136c335-1927-3daa-acba-30b5ce85964b | -12.2346 | -57.1071 | 2026-10-09 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 30b18e3c-2df5-30b0-a7c6-85eefda49d3b | -3.9299 | -56.034 | 2026-10-09 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2a1e57f1-1e25-3164-9f3f-0d61cd8e8d65 | -3.7739 | -58.5921 | 2026-10-09 00:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2dd5626b-5d59-3bf2-88b8-f3958b663713 | -3.1786 | -50.6016 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9326c8d8-591d-3a9b-91f4-b1319754cbcd | -3.0002 | -54.0684 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 173f0445-3b6a-32bc-9efd-cf2f4560a126 | -12.2154 | -57.1287 | 2026-10-09 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 19dc0571-780a-3ab5-b509-13106ed92339 | -8.7423 | -45.1334 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 456.2 |
| cf21102c-5e58-350b-9bf6-a2e9d8b14df9 | -7.2187 | -55.0815 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 29c052e1-293a-39f6-822d-6daecc3d973b | -5.7119 | -53.4658 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| b496cc97-13a1-324a-8c65-07891a2a839e | -8.7426 | -45.1106 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 72549db8-9a91-3d8d-8e95-70b897ff1c65 | -5.7492 | -43.8481 | 2026-10-09 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 170ed488-6890-37bc-bc91-bb5bb521b61e | -6.021 | -40.9577 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 59452ee7-c225-302d-bcfb-814d2e104fec | -11.8499 | -43.5835 | 2026-10-09 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 812d4854-08f1-35d6-bde8-15ce23cef490 | -15.4287 | -43.2373 | 2026-10-09 00:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 195.8 |
| f3fa29d7-b189-3a94-be8d-e60b7012833b | -9.2549 | -60.8863 | 2026-10-09 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| d489f50f-19b7-32de-b5e2-176171a3a3fe | -5.7679 | -43.8467 | 2026-10-09 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3b6b9e81-2d48-3f8e-8ab1-0fef877bd15a | -6.0021 | -40.9594 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 594.8 |
| 18c62be0-d352-3c75-8a4b-13186ce5da54 | -3.1109 | -53.9249 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bd850a29-a78f-3bbb-bfaa-f3acef6ebcd5 | -6.4903 | -62.8554 | 2026-10-09 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| bc2e6e19-9ccf-318b-85e3-70e77afd84e7 | -3.3455 | -50.4078 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e33860ee-ea24-3aa8-9f36-ac15c0801211 | -6.0019 | -40.9837 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 286.6 |
| 0d3dc198-5be1-335e-8a46-c849d4741cf3 | -3.0109 | -51.0236 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3d6fa1f8-820d-3175-b6be-6c7602400d91 | -8.6301 | -66.7886 | 2026-10-09 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8aa8f6bd-bf8d-375d-a717-3834fff243a9 | -2.499 | -56.0675 | 2026-10-09 00:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d4ddae1c-027f-303d-a8df-57290be14d15 | -3.1298 | -53.7834 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e6c9fd2a-3f4b-3eb8-b9a9-13f49fb45cc9 | -3.1114 | -53.7839 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 826b2ab8-6d99-3f14-bcff-0b71142eb740 | -14.8854 | -50.2883 | 2026-10-09 00:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e7742499-17c0-3d3b-a7d9-f1abe2d55b2a | -5.8842 | -43.4199 | 2026-10-09 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 8e607a70-dc80-3aab-9f26-dc402f22d01e | -6.7363 | -55.1675 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 1f2b220a-bdf5-3beb-976d-48f982d887de | -5.9587 | -55.3448 | 2026-10-09 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a58190a1-4979-31e6-a1ac-1410d28de248 | -1.1094 | -54.1601 | 2026-10-09 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| faa0838c-1c87-3592-80f6-4265931bb571 | -5.7116 | -53.5065 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2f5666ff-0d0a-3998-b039-ed64ec2d97db | -3.1787 | -50.5807 | 2026-10-09 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| c3b2a188-ec03-3022-acf9-96ea70583730 | -6.7365 | -55.1474 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 4c34bd0b-d685-3d07-bebd-653f3a6d7cd6 | -5.7117 | -53.4862 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 4e97ff66-9b11-3781-86dc-57a05faa61b9 | -6.8907 | -45.8988 | 2026-10-09 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1f19f5c7-d0eb-32af-90dd-7c3329798ef0 | -13.1827 | -54.3571 | 2026-10-09 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| e6d596aa-ac42-3fb1-a9d7-63bb054860fc | -6.0207 | -40.982 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 9ba30912-07bd-363f-8289-7aa2a219973b | -13.2018 | -54.3551 | 2026-10-09 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| da49d184-7e09-349b-8fee-0cf401b9e444 | -1.1277 | -54.16 | 2026-10-09 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b91e94c9-8854-3282-87a2-96cb335f8414 | -8.9766 | -45.9272 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8b3d44ee-5941-33cc-ae64-0e08492115bb | -11.2142 | -45.2519 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adf52db2-df78-3f5d-83b8-ebc15066d1a0 | -12.0143 | -43.469601 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 542b0cfd-8093-3bb9-9961-7d8ff90feb2c | -13.3705 | -43.894901 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb70a249-b97b-32f5-8f99-1e6b68aea220 | -10.2747 | -47.831299 | 2026-10-09 00:28:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a28d9666-99f3-3ab5-92c2-37dbbdaccff7 | -8.1339 | -49.443001 | 2026-10-09 00:28:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd63feee-658f-32c2-9253-20fcbfe13bdd | -14.0471 | -43.832699 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 275b8a87-d6dd-3526-bbc2-73ba063c718c | -5.1071 | -46.2257 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e51deb9-a12c-356b-a0ca-047ce9d52dcc | -7.3818 | -44.011902 | 2026-10-09 00:28:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b67c6b8e-329f-3b01-ac29-114b7aee4f15 | -1.1372 | -54.222801 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14a92ed-ca16-300e-87a5-a7cb12b1ce49 | -8.331 | -49.125301 | 2026-10-09 00:28:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edd7efa5-c08e-363e-b6cb-ded397852433 | -13.1488 | -54.329102 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ccccbd36-f28b-3024-a658-91c87b9a8f9e | -11.0188 | -45.4361 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee144843-2b47-3919-a21a-16ce16d6f3be | -5.4366 | -45.6842 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c341110-07b3-3224-b8c9-425bf872550c | -6.9807 | -47.671299 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85674ef4-eff1-3a2c-9e87-eb90ee44e2da | -17.7136 | -39.7551 | 2026-10-09 00:28:00 | METOP-C | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b48671b3-1f7b-3007-9c12-2048d08e42f6 | -9.1149 | -48.816601 | 2026-10-09 00:28:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 800fb7b9-9dcb-3148-8412-616e2349ae09 | -8.9026 | -45.238602 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README22.md)
