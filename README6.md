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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a4d25c9-9509-3962-bb52-ffda6ce12085 | -6.914 | -43.6816 | 2026-10-05 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0bb30c0a-15fe-304f-8068-293a4cafd215 | -3.0364 | -54.2282 | 2026-10-05 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c6b4963e-5e1c-3e57-a48f-702a9bf5a976 | -3.2755 | -54.1819 | 2026-10-05 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| dfb00e49-811b-3b5a-b9e8-b7f03aa779c0 | -6.2529 | -52.847 | 2026-10-05 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 99da173b-b0fe-3748-80f2-2ec965b4aefa | -7.4441 | -63.5777 | 2026-10-05 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 79915f43-356e-37be-93b7-1dac3bdef6e8 | -6.0075 | -53.5122 | 2026-10-05 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 33e0fa2a-9608-368c-af1e-a51bdd4ee4a5 | 3.1098 | -60.5943 | 2026-10-05 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 52bd8dd7-c15a-3b11-8327-b7c1bc1cae54 | -5.5893 | -49.7388 | 2026-10-05 01:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e3f13712-c81b-386e-a36a-78a374cfe0ae | -6.8955 | -43.6601 | 2026-10-05 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ec9be1a8-23b6-36c3-ba0b-b59341c02e17 | -6.8952 | -43.6833 | 2026-10-05 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c9e24b95-4e0c-34b2-bfb7-1366f5763359 | -2.9082 | -54.0907 | 2026-10-05 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 085c7193-7f17-3114-a5f0-a85c39aa8dcb | -6.2159 | -52.8285 | 2026-10-05 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 09e81ed5-27a3-3f94-b304-5aaa952456d6 | -8.6736 | -54.5481 | 2026-10-05 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b32d146d-9971-3312-bb41-0b9d8750e896 | 1.8583 | -55.7821 | 2026-10-05 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6ff123ac-2047-3903-8e42-9063149511ef | -2.6859 | -49.0325 | 2026-10-05 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6fec3e42-11c5-3a32-8f40-a823730b7324 | -3.5128 | -54.6162 | 2026-10-05 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a7293b66-2d82-3dac-b4b6-5197bc110986 | -7.4441 | -63.5777 | 2026-10-05 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c0aaab5f-a251-3123-8c75-e094fe894b09 | 3.1098 | -60.5943 | 2026-10-05 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 393de1f8-8634-3a7c-9313-4981fa8903d8 | -9.1613 | -68.2568 | 2026-10-05 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5a5210a6-3147-33bd-8fc1-fa8c9ed7670d | -3.2755 | -54.1819 | 2026-10-05 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d6f29245-f0c3-35d0-935a-2d0f7bdca33b | -6.914 | -43.6816 | 2026-10-05 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 529603d1-c90e-3bc9-80cf-2defe276bb4e | -7.4626 | -63.5583 | 2026-10-05 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1dfb2b6d-bbbf-33de-a923-67d5a3856dbe | -5.9882 | -53.635 | 2026-10-05 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 37dbe75d-7fa5-3230-ba9c-c78e777c72bb | -9.8532 | -36.3006 | 2026-10-05 01:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 7f7dad7d-339e-3772-9d4c-027e510da696 | -7.4442 | -63.5589 | 2026-10-05 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 20257f85-5a19-3fe6-bdf2-209196442070 | 1.8766 | -55.7819 | 2026-10-05 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ddf4300d-dd27-3407-944d-ea32087e033d | -3.8448 | -50.3063 | 2026-10-05 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 71b4b146-d8bc-3240-8c38-5a9305455c8c | 1.8583 | -55.8018 | 2026-10-05 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4365380a-40da-3cbb-a29a-c1f2b5d20f27 | -3.0548 | -54.2277 | 2026-10-05 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 55cb6eea-4a26-3f56-b89c-4783b8383a08 | -6.8952 | -43.6833 | 2026-10-05 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 7b9b7649-703a-37ae-888b-3c9ae52b5df1 | -2.9082 | -54.0907 | 2026-10-05 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| da108ea6-8b14-34b0-98b3-af0e57c9c14b | -6.2161 | -52.808 | 2026-10-05 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| af7d5869-1ef8-394f-83c4-92ebb9eef4c8 | -3.9859 | -55.8152 | 2026-10-05 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1f9fc863-201a-3f1f-a63a-3ed302b77290 | 1.8767 | -55.7621 | 2026-10-05 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| d18d3be3-0b79-317f-a532-c1903d14c584 | 3.1097 | -60.6133 | 2026-10-05 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0badb8c9-9e19-3cdd-896d-aed5c0c59807 | -3.8447 | -50.3273 | 2026-10-05 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c9ed1866-80c7-349d-ac2a-9533f6a0633a | -2.7044 | -49.032 | 2026-10-05 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 77178632-f2db-367b-be4d-ffb4dbd09b40 | -6.2529 | -52.847 | 2026-10-05 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| bba24bf9-3aa4-313f-b092-35856a04e2cc | -6.0075 | -53.5122 | 2026-10-05 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1d92d50e-47cc-31e2-8dc9-83f6b9ecc77d | 1.8766 | -55.8016 | 2026-10-05 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 4d642a1f-72ba-3c00-aca1-77dcc46e58d4 | -6.2159 | -52.8285 | 2026-10-05 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| aa93b1d3-1f4a-3f76-8a3f-aa17935ab523 | -12.87903 | -61.72588 | 2026-10-05 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c319bcb4-5400-3de2-ab46-318d4a031980 | -11.97704 | -63.61034 | 2026-10-05 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 95176547-b828-392e-ba4b-36e531e4def4 | -12.87622 | -61.70855 | 2026-10-05 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6e922ffc-b817-3e78-93e2-168475726434 | -3.11 | -53.69 | 2026-10-05 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a363103-48a2-3475-829a-a903169579a5 | -3.08 | -53.75 | 2026-10-05 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3930de-8a93-3d7a-b6d9-78429e7b2bfd | -3.05 | -54.17 | 2026-10-05 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1c3db3-5396-3368-857f-74d9a2da05dd | -3.08 | -54.18 | 2026-10-05 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ada106a-7abe-3bbe-a294-5be4f26630b2 | -3.11 | -53.75 | 2026-10-05 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9f213e-a1eb-3b9d-a90f-da807a92ea2b | -9.48267 | -67.1647 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 272bf6c0-e379-3cd2-870f-4e871dad707b | -8.59635 | -66.69358 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 313d4edb-40db-3a4f-b640-e32e8fd89724 | -9.14288 | -68.23198 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e5842cdd-728a-3d3b-82f7-8b259c2d5827 | -9.13153 | -65.91656 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0de00718-288f-36cf-8f80-422855d8c753 | -8.54148 | -67.02486 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04682b87-0651-3904-932e-d66ae1767a3b | -10.21589 | -61.44823 | 2026-10-05 01:15:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| c39b23c1-ff90-3a41-8ff8-d9a77648066d | -9.21752 | -68.16976 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 20176e8e-9827-3986-8d0c-87e058ba117e | -9.13803 | -65.89462 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 445c1f7d-c775-34ed-ad40-fc870395d325 | -9.13179 | -67.82556 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c435008c-cd85-3d99-8711-c105f248a602 | -9.15292 | -68.23959 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 164cf964-8b21-3e3a-b054-9c81b1fec1b5 | -9.14396 | -65.89828 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e65ca69-c3ed-3f97-848f-a1e135fdc0c7 | -9.40394 | -65.88883 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7ed11f58-abe1-3614-8510-54ce0f5da47f | -9.03125 | -67.55697 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 316ea97d-acac-31c2-a5f0-f70a54d4ad1f | -9.12158 | -68.20786 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f87cb9da-67a0-3d4e-9b9a-91e93b3cbbb1 | -9.13007 | -65.90636 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 07c565e6-3427-3459-9f16-d00dcbe56115 | -10.6193 | -67.92268 | 2026-10-05 01:15:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 917e29c7-2799-3ee5-8f26-528513b42080 | -8.624 | -69.49802 | 2026-10-05 01:15:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7fa5baee-a1b2-3817-a6dc-d2308a88dc37 | -9.15658 | -68.26623 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ccd1cde2-fb77-38da-ad50-04ae55ddf39b | -8.62525 | -69.5072 | 2026-10-05 01:15:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 22cab478-1eeb-3d3f-b8de-6542b728f410 | -9.1228 | -68.21674 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3196c526-67a3-3696-a7c0-9a77e1f95166 | -9.10086 | -64.37904 | 2026-10-05 01:15:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c16fb087-4cc4-342e-b3fd-dae253184c5e | -8.58588 | -66.68537 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7afc1bc4-d4a4-382f-9347-0d90f742fff2 | -9.11975 | -64.36315 | 2026-10-05 01:15:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 504ea63a-e1ee-3802-a0f6-f1eb32eabdac | -9.50074 | -68.49785 | 2026-10-05 01:15:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99970479-46c6-337a-8e5a-0bb8d401eb08 | -8.59501 | -66.68403 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e019d163-f7f8-34ff-b99f-281885bd5acc | -8.58723 | -66.69493 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 982c966f-5cf5-3cbe-b2ee-d2aae71465cc | -9.13949 | -65.90488 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| bb995111-ad49-3455-bc2c-481b450e0006 | -10.21714 | -61.45459 | 2026-10-05 01:15:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c9820d5c-b747-3f98-a624-cc4ceb0d4ae5 | -8.67035 | -70.04639 | 2026-10-05 01:15:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6c3d6724-117f-3513-9cdf-aa2bb9ca53e8 | -9.25562 | -67.6496 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c155259-ce34-358d-89be-89e1a792acdf | -10.0752 | -67.3839 | 2026-10-05 01:15:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54959721-38b3-392f-a731-c620c155aed7 | -10.48414 | -68.61143 | 2026-10-05 01:15:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 858c9c78-bbfb-3cbc-9dae-704ed181614a | -8.74711 | -64.19414 | 2026-10-05 01:15:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c00cebc1-a34d-3149-9ddf-5b8f1d4f90ec | -9.67492 | -66.82684 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fc944e80-d7cc-36e2-9ed5-7b67d4a7dca0 | -8.52082 | -67.00887 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| db01f644-f6d7-337c-a16c-6c5e69e790f9 | -9.1654 | -68.26497 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2a69a8ae-6267-3c71-9ce4-56022f76eba4 | -9.39599 | -65.90044 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8fce13fd-fa2b-3fd2-9021-f117016e4027 | -9.16418 | -68.25609 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 798f09d1-94ec-3606-bf9d-cb855b5ea62d | -9.33718 | -64.71987 | 2026-10-05 01:15:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e32198a-0617-36fe-9ca6-cc99c1cdf227 | -9.15536 | -68.25735 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f872b048-ec48-3b85-bd49-97df88f020bc | -9.10468 | -65.36352 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45f394a5-4d33-3853-8556-33c8419cb8b6 | -9.38556 | -68.33006 | 2026-10-05 01:15:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa2f2728-e75b-3bee-bb1c-cc5a46546894 | -9.09499 | -64.3858 | 2026-10-05 01:15:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d72bbe87-ff6e-3d63-ba4f-5c2960c0b190 | -10.8631 | -68.69041 | 2026-10-05 01:15:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6d7e22f7-5144-3f3e-88e0-43b309c9a70f | -9.91338 | -65.0146 | 2026-10-05 01:15:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c5b6dbf-2740-30f6-b992-1cf6d737fb55 | -9.4054 | -65.89905 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d517bd8e-70db-3efa-a130-5a2b5b8d0345 | -9.48139 | -67.15558 | 2026-10-05 01:15:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c3d8aec1-31eb-3701-b35e-16afe6a07a3f | -9.16662 | -68.27385 | 2026-10-05 01:15:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 79f928fc-1d38-3527-92db-d3ae3940d899 | -7.36547 | -72.60853 | 2026-10-05 01:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 86e904b2-31f8-32f9-8078-b68be61fd492 | -7.45022 | -64.4385 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e44a76aa-28ce-3a8f-b569-53ee29b9e24a | -7.45496 | -64.42995 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README7.md)
