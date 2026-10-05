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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bed0255-55d6-3fbd-ba4c-734b21074497 | -6.2161 | -52.808 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ecf0ebdb-04aa-308d-b85c-c8c8b84b9ed7 | -7.4626 | -63.5583 | 2026-10-05 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2718a0c4-3608-3427-8809-c32dc6311b71 | -5.5891 | -49.76 | 2026-10-05 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 77ee9245-58ea-3e1f-8da5-1333128c427a | -3.2755 | -54.1619 | 2026-10-05 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2f3b309d-0adf-35cc-ba2f-2f58db2c6f50 | 1.7303 | -55.6456 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| acf6a7a6-ddd8-313b-862f-14f5aed5ddeb | -6.1974 | -52.8295 | 2026-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a077016d-1ae4-36e4-9432-782f4d98a98c | 1.8583 | -55.7821 | 2026-10-05 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| abfaaf4e-e8ec-384d-9f5b-220f3be7b231 | -6.253 | -52.8265 | 2026-10-05 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fb0f8834-5e5b-3ae0-9f64-6dfa338f2a96 | -8.655 | -54.5494 | 2026-10-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| f0ec6981-b690-31b9-bfaa-4fcc68973aea | 1.8766 | -55.8016 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| bf1d7d11-6964-30c5-bdec-1acb453b3260 | -0.3952 | -52.0357 | 2026-10-05 00:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 02314c23-e03f-397c-9de5-b2a472c984cd | 1.7303 | -55.6456 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| dc26fd52-96ae-3f23-a5ef-663380f1d845 | -3.5128 | -54.6162 | 2026-10-05 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 76c90e3b-312a-371b-8c9a-901e75162a9a | -2.6859 | -49.0325 | 2026-10-05 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5871c64a-f2b8-3d0c-ad39-a6b0cff4189e | -2.9082 | -54.0907 | 2026-10-05 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| e3d3b3ca-42c3-393a-8fdd-08d7b1324b38 | -6.1974 | -52.8295 | 2026-10-05 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 7e2535c2-3dce-3069-a6a3-b8c709d3a095 | -5.5893 | -49.7388 | 2026-10-05 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8a07d14-f64f-3f76-a5d2-18e84f4390c6 | -6.2343 | -52.848 | 2026-10-05 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4d794d15-b454-3bb3-9857-2a63f2179c0c | 3.1098 | -60.5943 | 2026-10-05 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9a23f7bd-9ff2-3e48-84a2-fc9b4ca0fa87 | -6.2159 | -52.8285 | 2026-10-05 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 0cc74479-4e44-3596-9f3e-a5c46b4f2a9b | -8.6548 | -54.5696 | 2026-10-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cabfb9cd-d15c-3a4f-8da2-c2dfa1f880e9 | -3.9032 | -49.7137 | 2026-10-05 00:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 62226d95-20e2-3293-87b3-45edc89aef73 | -3.0364 | -54.2282 | 2026-10-05 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0d533a9f-872f-3cdd-a167-c52a2f0db4df | -8.6736 | -54.5481 | 2026-10-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| dc6f1492-5625-38dc-b57d-30ade5a86d8e | -6.0075 | -53.5122 | 2026-10-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e66c02d5-9d9a-3bfd-8f9c-2efc8480ad1f | -3.0548 | -54.2277 | 2026-10-05 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a36681b7-8766-3a8c-a26d-49c8837ce70f | -2.9488 | -59.1667 | 2026-10-05 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 169df47a-d798-3cbb-bc97-47a5d4d92027 | -7.4257 | -63.5595 | 2026-10-05 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 19ca3a65-62b7-30b9-82dd-d9298c6711b2 | -3.2755 | -54.1619 | 2026-10-05 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 5f85ac37-495a-3bf0-8024-861f4f751764 | 3.0915 | -60.5946 | 2026-10-05 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dee9d366-cbcf-327b-8141-ad300efb2f2a | -7.4442 | -63.5589 | 2026-10-05 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 164.2 |
| c608ee3d-b376-31ad-b4e3-9f1f2eb83924 | -7.4626 | -63.5583 | 2026-10-05 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 80dd2143-5be9-3041-b7e2-7f7bb3770c54 | -3.9217 | -49.713 | 2026-10-05 00:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ba1e8c9b-4893-3b90-a329-e6398d3dc4cc | -3.8448 | -50.3063 | 2026-10-05 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 77feb47e-118f-3eef-804c-79c8e3478d74 | -0.3768 | -52.0358 | 2026-10-05 00:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 39.2 |
| c4f3ad58-c3d1-3ba5-ae4c-f2e599187e48 | -6.914 | -43.6816 | 2026-10-05 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1a97e65b-7e71-3358-bb8b-0e6698a9afd2 | -6.2529 | -52.847 | 2026-10-05 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| c3be38ce-da00-3672-96bf-4afc6dd79ea9 | -6.8955 | -43.6601 | 2026-10-05 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 80d03f90-b546-37ac-8aef-d6d41b05e84a | -3.2755 | -54.1819 | 2026-10-05 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| e34bcb5e-a6d4-34bc-a304-7f2c69fd19d5 | -7.4441 | -63.5777 | 2026-10-05 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4cc6dfb3-5490-3bab-a91e-2fc571d0504c | -3.5127 | -54.6362 | 2026-10-05 00:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 19cd556e-0cd5-3592-a05b-bc5e08a1f069 | -1.4756 | -54.5365 | 2026-10-05 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8b84b191-8896-332b-be33-73d1f7bd77b3 | -2.7796 | -54.0937 | 2026-10-05 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 114c9653-eb14-3086-acba-1ddf492d8f98 | 3.1097 | -60.6133 | 2026-10-05 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0f52193a-a356-3fe9-a8f1-8c03501e06e4 | 1.8766 | -55.7819 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fa837850-0da0-3c3b-905f-73be65503929 | -3.8447 | -50.3273 | 2026-10-05 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 9ffaa977-a25f-3fb6-a98f-b1b5f1dc57ea | -8.6734 | -54.5683 | 2026-10-05 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8d979715-dd30-3e6a-8001-aa8ed69f65a3 | -6.8952 | -43.6833 | 2026-10-05 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 389b997d-37af-38fb-8933-5d49a426cbf7 | 1.8583 | -55.7821 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4b594077-995f-3008-a5cb-b0cd43f64b49 | -3.9033 | -49.6925 | 2026-10-05 00:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1ce763bc-689a-309b-9eca-8d19c9bb64d2 | 1.8767 | -55.7621 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0fff9ec5-3488-323c-97e9-51cf749630db | 1.895 | -55.7619 | 2026-10-05 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f85e0469-8067-3d9a-93d6-f8ec641b6bd2 | -3.5128 | -54.6162 | 2026-10-05 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fc6f478c-5d64-3329-8707-fdaa2cb756cb | -3.8447 | -50.3273 | 2026-10-05 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 14ac0c5c-6c05-36b4-b127-2cd05cd269ae | -3.2938 | -54.1814 | 2026-10-05 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7bb72f57-3750-354f-8624-1f5a7a730295 | -3.9217 | -49.713 | 2026-10-05 00:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1301fb83-d2c9-37a1-8379-10094bda5d22 | -7.4441 | -63.5777 | 2026-10-05 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1d49f816-8d48-303d-8915-2e71884831af | -6.2529 | -52.847 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 6e42b51f-343a-3ac1-a1e3-4aee0ac51baf | -6.914 | -43.6816 | 2026-10-05 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 991a39f8-9a1c-39db-a10f-f032480da57e | -2.9082 | -54.0907 | 2026-10-05 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 032a651a-a8f4-3d53-8310-e076165a80f7 | -1.4757 | -54.5165 | 2026-10-05 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1a8f8ec2-6559-39e5-b056-d085e146873c | -2.6859 | -49.0325 | 2026-10-05 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9201c208-4b33-3300-95cf-102900fad6dd | -1.4756 | -54.5365 | 2026-10-05 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| fdfd7c62-9871-35c2-9d4d-967e7aa3c56b | -6.253 | -52.8265 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 924a2656-8a68-378e-9337-45f68ceaba01 | 1.7303 | -55.6456 | 2026-10-05 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 8f0d25ca-1099-3363-accd-ed36756f5de0 | -8.6736 | -54.5481 | 2026-10-05 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 02ee47d8-877f-3198-b508-84c0e3d5d80e | -6.2159 | -52.8285 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 29b9ffa2-13ea-39f6-984c-516119e6aa0f | -8.6734 | -54.5683 | 2026-10-05 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8d1f988a-1ed4-3492-bfaf-209d91d4294f | 3.1098 | -60.5943 | 2026-10-05 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 23862490-6318-3512-958e-7826201b6af9 | -3.9032 | -49.7137 | 2026-10-05 00:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c4a14a13-ee6d-30d9-bb56-b370fbecde02 | -6.2161 | -52.808 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 13251e29-1ae5-36ef-9884-0b851845ba59 | -7.4442 | -63.5589 | 2026-10-05 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| ec83d266-3dc1-32d9-b003-6795059a9949 | -10.086 | -36.2053 | 2026-10-05 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| 70ecc7fc-5c0a-3926-8c0f-d10c741c991e | -2.7796 | -54.0937 | 2026-10-05 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8c4163a0-12a8-38e0-b7a9-53d7e1413abc | -8.655 | -54.5494 | 2026-10-05 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0068dfc4-5a7d-3446-91a5-de6e3edc6b38 | -3.4211 | -54.5587 | 2026-10-05 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 339f94e0-b4bd-39cc-92c8-8a72aaa01442 | -7.4626 | -63.5583 | 2026-10-05 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a991a233-98a8-30bf-9a0b-c347f87df72b | -3.2755 | -54.1819 | 2026-10-05 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 55609cef-9caf-3d4f-bbd4-df92a08a66d2 | -6.0075 | -53.5122 | 2026-10-05 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 7ac1ab1e-bb2a-3e18-9d38-bdd44f7dbecf | -6.2343 | -52.848 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 495e6335-679c-3ba5-bf93-d6aaaca1c461 | -6.8952 | -43.6833 | 2026-10-05 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| be98b127-b953-3297-90b2-cc695098cf78 | -6.1974 | -52.8295 | 2026-10-05 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 6b73e15a-07eb-3f8c-9560-1de0054d1174 | -3.8448 | -50.3063 | 2026-10-05 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| efe3ba8f-9a5f-3cf4-b9b2-e6646e59655c | -3.8447 | -50.3273 | 2026-10-05 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e61eb977-f76b-30b8-90e4-edf22e1943be | -6.1974 | -52.8295 | 2026-10-05 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8dad0c1e-7037-3ab5-bf9c-c4fa256c7108 | -6.253 | -52.8265 | 2026-10-05 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| adc85ce0-db90-3535-a78e-13393e4931bc | 3.1097 | -60.6133 | 2026-10-05 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f234b09f-9ed1-3b9e-b61d-6524516185f3 | -3.5128 | -54.6162 | 2026-10-05 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 18e106a1-9b7e-3664-a14a-ce3279aed224 | -8.655 | -54.5494 | 2026-10-05 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4e84325c-c314-39c4-8361-0b3d8569c05d | -3.0548 | -54.2277 | 2026-10-05 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 0737c0cc-c920-34eb-a3bc-0080b568a35e | -2.7044 | -49.032 | 2026-10-05 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b6401a66-a84f-3496-99bf-cf70deb0667e | 1.7304 | -55.6259 | 2026-10-05 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9f152e7e-530d-3516-8222-ac7be8c325cc | -3.8448 | -50.3063 | 2026-10-05 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 94b46126-2a58-39ee-b0ab-2c85ee0f22a4 | -7.4442 | -63.5589 | 2026-10-05 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 3c179ce0-a7c6-3934-bfc9-cafc632deb5b | 1.7303 | -55.6456 | 2026-10-05 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 2ac287db-af82-3e5d-bc24-a0a69d0ac900 | -2.6859 | -49.0325 | 2026-10-05 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 41f81f1b-b7b9-39de-b1de-2c12ce45c33b | -7.4257 | -63.5595 | 2026-10-05 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ee7b23e8-2c67-33ce-8267-5c3a49940c54 | -1.4756 | -54.5365 | 2026-10-05 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f1b7e79f-b87b-3000-b001-5cbd6ea91c9a | -3.8756 | -55.8184 | 2026-10-05 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1ae1a9d4-f996-38c7-b4d5-6b75985caad6 | -7.4626 | -63.5583 | 2026-10-05 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |


[Clique aqui para ver as próximas entradas](README6.md)
