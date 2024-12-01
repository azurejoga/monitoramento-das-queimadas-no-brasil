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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4315e02-0bf0-388b-822b-66043ce937bc | -5.6103 | -45.053299 | 2024-12-01 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4c2dc20-4944-39b5-af3d-8c493d4018f9 | -1.9759 | -46.462002 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa14ce9-55ac-30d1-aab9-7f422dccd3c5 | -3.2184 | -53.127899 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0ce2cb3-f86a-33e1-bbf0-8bb017cc4f46 | -2.8126 | -53.058998 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d89803d8-9695-383f-ba85-7f6511f43f81 | -2.1261 | -46.576599 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6b8557-2362-3416-89ee-9238f9766edb | -3.0229 | -51.533001 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6058fec7-adab-3fb0-87c0-ced63a3f58fb | -5.1858 | -43.9496 | 2024-12-01 00:34:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c19655e-7f8e-310f-9396-1e9828c4cb00 | -2.8303 | -52.591702 | 2024-12-01 00:34:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9206ba3e-deac-32fe-8a27-ee54a0ca1d51 | -3.5249 | -50.4772 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c9b5eb-cb3d-3ab7-a35e-30cf5d7105b5 | -3.302 | -50.040199 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9a6d03-07d1-33d5-94a1-777d05028605 | -2.6302 | -46.883499 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da28108b-a680-37e6-994f-ad3e82c97679 | -3.2684 | -53.624401 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cedbf86-f052-3ee7-a506-96520f3cf658 | -3.509 | -53.828701 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b204880-a6d7-3bd4-8295-875b38ec5822 | -2.6263 | -54.189899 | 2024-12-01 00:34:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d6c79d-b5ff-3d38-88b7-64de5ccdad35 | -4.8839 | -41.301102 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca331b8b-f7a8-3d04-8101-16a8e439c944 | -3.3328 | -53.362999 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 049e2a5e-64c8-32a2-af9b-8c2484079cf3 | -2.6296 | -51.75 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11e1ef43-7204-34e4-b778-9dd45750d161 | -3.2045 | -54.161999 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd7ad62e-299c-3a3d-94d9-88e4ba30fa56 | -3.1165 | -53.2682 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d6c589-dbc8-34fe-9324-0e92de6022ce | -6.922 | -43.5243 | 2024-12-01 00:34:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06509e55-6bea-3f3f-bea4-fdfe62c35cbd | -3.0634 | -53.807899 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 567c57c9-e59c-38ba-a133-7d05188d481c | -2.6285 | -46.876301 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 020de73b-252b-3566-b919-9da8a569ea9c | -3.4895 | -53.833 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38613818-259d-3c35-bbe3-e90067b8435b | -1.257 | -47.505001 | 2024-12-01 00:34:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a345fa17-0197-3566-8f06-51f03b2a24c6 | -2.678 | -46.5989 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15a2da4a-2267-3ace-b000-7e55b038f372 | -4.174 | -48.619301 | 2024-12-01 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901cccec-7ef1-3ec2-baaa-192c1c1f57a1 | -3.2681 | -50.207802 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40fb9adc-a73d-36cd-bce2-504c93e41aeb | -3.3136 | -50.136501 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88cbd78-41eb-34ae-a15c-b8e951b9a0a9 | -2.7262 | -49.368099 | 2024-12-01 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 088c82b0-d818-3cd3-a837-6033d6b6557b | -3.1394 | -53.8265 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c8aeb4-56ca-3886-bf77-75868cc2f1d5 | -2.6115 | -51.806599 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84294937-bae7-3a7f-8cf3-c08cce28901a | -3.2086 | -53.130001 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b2fb00-3398-350e-b0d0-b23490762cd5 | -1.6991 | -46.1572 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19fa8731-e462-33e5-8187-be5f692eb0b9 | -10.6612 | -44.485802 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21d39dc4-20c5-3cc8-a976-4990a773c7ea | -3.2586 | -53.626598 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1628a1-2c32-3147-8f19-514512478908 | -4.8904 | -41.3279 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8e9b385-a826-3d31-bada-7b7998da35e4 | -2.6235 | -51.768799 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2b28d3-a16c-3a48-bc4f-b1a032b6c490 | -4.1725 | -48.6124 | 2024-12-01 00:34:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2a9e531-b483-360a-863e-07d98ebb96b6 | -3.0391 | -50.243198 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974a5f06-7e6a-3db4-973f-bde34c1733bf | -1.6974 | -46.149502 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc9440b1-b224-3c0e-abb9-69dddfff79e5 | -4.8872 | -41.314499 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e2efb27-c7bf-396a-95e3-a74dc5927a4c | -11.3152 | -54.325699 | 2024-12-01 00:34:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 751c1b0d-69a0-3791-a719-bf88f58d18c8 | -3.3204 | -50.211601 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d7ae70-6495-30c7-9333-a69f1f43ae57 | -2.1163 | -46.5788 | 2024-12-01 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ff73cb-10ba-3e23-841a-8793767395d3 | -2.1232 | -50.3395 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b1ae4b6-3c2f-377b-bc4c-22600887275e | -3.5379 | -50.1712 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9048f02d-39d3-3164-993f-4d901961b7b9 | -4.8937 | -41.298801 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3059374f-ea0b-3de5-9708-5feb85783a66 | -8.943 | -44.251701 | 2024-12-01 00:34:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f42900ea-e644-3917-817d-04071a255d47 | -2.3326 | -50.670399 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d02889e7-6214-39b6-bd17-5e71352d0e5c | -1.7072 | -46.147301 | 2024-12-01 00:34:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c15e6a07-2e9d-3eb2-83c2-7b9e7b04f6f0 | -2.372 | -50.390999 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1140d9-57cd-3357-861b-0a9f40addf21 | -3.2936 | -53.828201 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 073ad330-8cc0-33f9-9e0a-5df452f1b6f0 | -2.7983 | -53.041302 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99231eb7-6640-31d4-8842-05aba9ef7fbb | -2.6612 | -46.125301 | 2024-12-01 00:34:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09d50c49-dd8a-3c45-aff4-82c9debc78db | -7.3802 | -45.826698 | 2024-12-01 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf18ad24-420c-3f53-98e1-b1af4ffd1a5f | -2.1123 | -46.249199 | 2024-12-01 00:34:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d217c071-d79b-3dc7-aeb6-9bfd84b51062 | -3.0585 | -51.054001 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bf34c7-24a4-356a-9c68-40bf5c3c56e2 | -2.1216 | -50.332298 | 2024-12-01 00:34:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dbac503-7d23-3bfe-9f4a-b6b2bb159d64 | -3.0073 | -45.127899 | 2024-12-01 00:34:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6152c06-ff28-3c3a-84a4-a990a27fbf0a | -2.7533 | -45.9436 | 2024-12-01 00:34:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 425f5eb3-abc3-3407-8db3-743e84445043 | -2.6581 | -51.875999 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a485132-14c4-3977-9a1c-3ee0a1338b82 | -2.64 | -46.881302 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06259b21-ccc2-359c-941e-1db2871ef17b | -2.8412 | -49.871799 | 2024-12-01 00:34:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441a0fcb-8f9a-3055-a3c3-7744c0056d62 | -2.5135 | -51.828201 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 547339b0-4329-3868-9160-dc0e84dda886 | -3.2513 | -53.639599 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e9b7ae9-b09e-383a-8563-63da0f0256a8 | -2.8973 | -51.569199 | 2024-12-01 00:34:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6b2a6c-8cda-3c4f-a31c-4f22bdce1f33 | -4.543 | -45.698101 | 2024-12-01 00:34:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e2208ca-006e-3740-8cfa-b640a9a03b84 | -2.5911 | -46.9375 | 2024-12-01 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f89e9d8-b149-385d-82e2-fc1df05cc21b | -3.7716 | -51.6134 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d70fbcf5-46d1-3735-b8a7-8a2e7df7e605 | -2.6827 | -51.712002 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc4ea36-6168-356b-8308-31ef10c58585 | -10.6532 | -44.495701 | 2024-12-01 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae3904ad-22d2-3d01-a11f-71d56e74f333 | -3.089 | -54.286999 | 2024-12-01 00:34:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06f7fa0-181c-3282-98a0-88dd56879cd5 | -6.5937 | -44.186401 | 2024-12-01 00:34:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f516fb6b-b935-3b19-afda-c3d8dd3a6a7a | -2.6562 | -51.8675 | 2024-12-01 00:34:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 312f9bb6-e95f-317c-9f3b-ca3af574c5d7 | -2.8081 | -53.0392 | 2024-12-01 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08dbfa21-9752-3b6c-a499-b9b63b5ad20b | -10.5197 | -42.415001 | 2024-12-01 00:34:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 04b44dd0-6c17-3b06-bd10-c836f03317cb | -3.3269 | -50.194801 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baf94ffe-42a5-39e6-af8b-5429c96d7599 | -3.2635 | -53.648399 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37203526-693d-3f44-984b-3473ebeda22b | -2.5154 | -51.836601 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9cb27d-8477-341e-af46-50ceed8a9065 | -3.3252 | -50.1875 | 2024-12-01 00:34:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c59cf6e-4923-3a99-ac86-9ab155633c20 | -2.6865 | -51.7286 | 2024-12-01 00:34:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee4c0f7-6fce-332d-8356-16d81c47e556 | -3.0609 | -53.796799 | 2024-12-01 00:34:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed7b2be-3b84-3e10-9b66-54bad86132d2 | -4.897 | -41.312199 | 2024-12-01 00:34:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72d1f1c3-2153-31ae-b880-8be60900b362 | -3.168 | -53.634899 | 2024-12-01 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 481aa3a0-6b0a-3664-af49-d45e55cb63f7 | -1.3647 | -51.847698 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7706bf6-147d-3096-8add-4541d000acae | 1.6672 | -50.764599 | 2024-12-01 00:38:00 | METOP-C | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d752fb59-a5fa-30d5-92a5-a2fd3cae1db1 | -3.6788 | -50.248001 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f54145-a9ce-3b9c-a862-fd23d8eec22e | -4.2536 | -50.831902 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae1da48-225f-349a-99fe-17518d8ec1e9 | -1.0786 | -53.389301 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f43bbc-bfb1-3bc3-9986-1e5271a52b6d | -4.137 | -49.361801 | 2024-12-01 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3bebca3-9470-34c2-82f7-7202dd9dd8a7 | -2.04 | -54.6819 | 2024-12-01 00:38:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06bf7476-3e07-3d31-bb2e-5d2bb0cbed83 | 0.9408 | -50.199402 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 31304b97-d036-3533-9f8c-ce761c656d8c | -1.6694 | -53.772099 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e777125e-0120-3b13-8c36-a62f9b8323d6 | -1.3192 | -51.738602 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad13e6c-c5b4-37db-bc5f-28179e967c37 | 1.1615 | -55.974098 | 2024-12-01 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5deb19fb-c780-3607-a73b-f99bb194760a | -1.7148 | -52.616001 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c07d1c-ae44-3592-9135-d93554341d4b | -1.2795 | -51.6548 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad083a16-0bb6-3c0a-902e-45b16dc5a50d | -1.6524 | -53.742599 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ccc3ba-45c9-3524-a92b-04e8092b7a6e | -3.5394 | -51.497299 | 2024-12-01 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdfc1d31-06a8-366b-85b1-7d87057b2308 | -1.196 | -51.740601 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
