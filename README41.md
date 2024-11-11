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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e76422ff-a033-3f77-bf09-1e6f55b1fefa | -2.69998 | -46.80681 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 199f3e35-c910-397f-8b30-aa0286b0f60a | -2.87955 | -45.3688 | 2024-11-11 05:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d0016e7-f87e-35a7-8a0e-340af1ecf317 | -2.64992 | -46.79948 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e9199f7e-f47f-3a79-9001-48284523c127 | -2.25212 | -46.51373 | 2024-11-11 05:14:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2b7482f9-a0ba-3a93-b357-43fc5d25129d | -2.69827 | -46.81811 | 2024-11-11 05:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7977d1b-0670-35fe-bd6d-63bdae7723e6 | -19.97825 | -44.1006 | 2024-11-11 05:18:00 | AQUA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 5eabbbc2-f492-35d8-8404-dbc760f9e57e | -17.29092 | -57.49333 | 2024-11-11 05:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 22b4cc05-224d-3d9a-af26-0e8d9d1e8894 | -17.60375 | -57.50497 | 2024-11-11 05:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 4b7b6b71-ba45-3a14-a138-b9f5f36dc488 | -17.29934 | -57.46091 | 2024-11-11 05:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 7e207e37-d492-3ccf-9943-3da0ca19e24d | -17.29904 | -57.45287 | 2024-11-11 05:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 1c7487e6-e6a6-3ca8-9290-9434d2aa949e | -17.63805 | -57.52112 | 2024-11-11 05:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 9cde1fd9-45e7-3afe-9bd3-4d6e673bf859 | -2.7402 | -49.3502 | 2024-11-11 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f412e38f-9a73-3478-b056-77b40ffd5f61 | -2.2297 | -53.6824 | 2024-11-11 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 477dbdee-a8bb-3d9f-8c38-8ea02441ada9 | -2.248 | -53.7426 | 2024-11-11 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d902e5a9-875d-3a61-a026-2a6ba25935e0 | -2.2298 | -53.6623 | 2024-11-11 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 685b3345-636c-3114-add4-2641c0fde424 | -2.2663 | -53.7422 | 2024-11-11 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5833649b-5e18-3a99-9f04-0afe1266645a | -2.2482 | -53.6619 | 2024-11-11 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ab087bcb-d936-3bcf-82a8-99aa007cd364 | -2.7587 | -49.3497 | 2024-11-11 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8a66dbd1-ecb1-3e43-8b39-59fef4095698 | -3.0295 | -50.9815 | 2024-11-11 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6f9a7d2b-461d-35c5-ae8d-a33d4221b864 | -3.1458 | -54.4859 | 2024-11-11 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 115ac202-0e45-3d98-8846-301ed7c4bb62 | -2.2482 | -53.6619 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cb4b1791-c3e2-3f39-b19e-e4772d5d1b0a | -2.248 | -53.7426 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 664937e1-5b9b-3c78-bb76-e5482bda1d4a | -2.7402 | -49.3502 | 2024-11-11 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 04d5c4b9-c5cf-3d52-a78e-47f1d087c155 | -2.2298 | -53.6623 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4e9359f8-0a8e-32b6-939f-af4944299603 | -2.2663 | -53.7422 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dfa73fc2-1334-3594-9e39-fe83a4ed0997 | -2.2297 | -53.6824 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 10b66601-b9f2-3116-97d9-a00bc5015f59 | -2.2114 | -53.6828 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2eff8ef4-e62b-3f2c-abfe-f5bb1eb2c013 | -2.7586 | -49.371 | 2024-11-11 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c045aa12-7818-363c-b153-7b2139b1e75d | -2.7587 | -49.3497 | 2024-11-11 05:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| d2130309-e4f3-3c4e-9523-cc906ef8120a | -3.1458 | -54.4859 | 2024-11-11 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e93ecce3-bc60-3f87-b247-0f7ef5cfb6f2 | -2.2114 | -53.6626 | 2024-11-11 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5fdca89a-cee1-39ef-b5ce-ac0bf6b1e55b | 2.85375 | -60.07806 | 2024-11-11 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86edf918-ebb9-3be3-a174-13919e5749e3 | 2.85432 | -60.0817 | 2024-11-11 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 653e8c43-d60d-330c-ac5f-236e014e04ea | 2.62965 | -61.62519 | 2024-11-11 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6ea7485c-1dba-3848-af36-b00e58bc3751 | 4.6429 | -60.94345 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd0128cd-0d35-3e2f-a120-8bc65971ed66 | 2.67593 | -61.18105 | 2024-11-11 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efb89147-07b5-3857-aafc-de86c9d3dc66 | 4.6495 | -60.94245 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 64c7462b-2916-3cfc-b088-0c96e74347af | 4.64674 | -60.94641 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d2ea852-6e11-393d-9a49-9931f7b011ca | 4.19145 | -60.97126 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55a82167-f6ae-3b5f-ae25-77d6927f27bf | 3.55447 | -60.42456 | 2024-11-11 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967ff3b9-fd95-3b20-a5eb-f571afd962e1 | 2.67539 | -61.17759 | 2024-11-11 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ee00411-1dbb-3014-a997-4322696df0bf | 4.64344 | -60.9469 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 538ca60a-01ed-3df2-becb-ae253e28d022 | 2.67262 | -61.18156 | 2024-11-11 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28d472e3-dc27-3d21-91d3-9fe3f3fd3bbf | 2.85037 | -60.0786 | 2024-11-11 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ec00dfe-5101-31ec-9ad5-beb089085cc9 | 4.6462 | -60.94295 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ec4dbd-9818-326c-b7f6-ae1f5596640c | 4.65279 | -60.94195 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94460870-0f40-3bb5-b4ee-32c32c0e7946 | 2.85714 | -60.07754 | 2024-11-11 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c0a103-3646-35ff-8789-ab877a79eb44 | 4.65619 | -60.93719 | 2024-11-11 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c572b79-2ca4-334c-8f52-de65317ced39 | -3.52478 | -53.49834 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ff0c2b6-17a3-3896-a069-ab6e678b6c01 | -2.22529 | -53.6717 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d19514d9-06df-3403-aaf5-9710160061e7 | -1.44195 | -51.67015 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0a528f-7291-3457-876f-a51c03eb320e | -4.27752 | -50.68015 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b5b1673-881b-3519-bfeb-1ebd09912da3 | -3.14271 | -54.48217 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a6929bc-0d65-3c85-b328-8d84d74c5dc3 | -3.1884 | -54.31849 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7415caa-73db-3455-80da-1ae5f1b722ac | -2.26896 | -53.74825 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a20bc8b-a852-36df-a90b-ca8028cf8234 | -3.62342 | -54.79793 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4411fb65-25f3-3d32-b57a-25a898551d7b | -2.45165 | -57.94341 | 2024-11-11 05:35:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fec107fa-2293-3f2c-bb34-b6a095bced44 | -1.63704 | -55.21449 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98929fca-8cca-32dd-a869-ade6a5a9060a | -1.40401 | -55.45166 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2735de10-f425-31eb-833f-b14f1592008c | -1.39461 | -55.45013 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94231e06-7c72-303a-8cfa-8ab1fb61be3f | -3.11265 | -54.47084 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3ed96b5-2eaf-3d3a-891b-467af3e66652 | -2.25975 | -53.73643 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b299118-d4b0-3d8a-b70f-51fdf97b6cd0 | -1.7228 | -55.03283 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c29bce75-ff01-3f00-bba9-289301f5d2db | -1.51796 | -54.9945 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13b939b0-2ede-3670-a89c-26b0dfd93a75 | -1.81568 | -50.79627 | 2024-11-11 05:35:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfe5cca5-b478-3977-82d4-087e8c289341 | -1.50915 | -52.14371 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4315d398-fdfc-350d-9de5-53c59ad142a2 | -2.23505 | -53.68026 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daf4ed3a-76e9-3913-bb73-f0335ec04c52 | -3.51663 | -54.68487 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9407b1da-646b-3e7e-a8ba-70e95e17ab64 | -1.40324 | -55.45665 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc5a71b0-5098-3f9a-9609-3bb30939db9b | -1.38597 | -52.41204 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fdc7b6b-8e8b-3aea-816e-aa1f61ca7494 | -1.63394 | -52.53918 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a441fe8-29e4-340c-a831-42d668889587 | -1.63987 | -52.54567 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4246b2a7-f98d-3736-9a44-7ebb19efa865 | -4.28066 | -50.6799 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dab10a01-35b1-33a6-bcef-8f2bc24f8af6 | -2.25438 | -53.73561 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e555b03f-ea2d-3514-a707-c22aea99b45b | -3.43137 | -54.53304 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 864e0bfb-1795-375d-bb9b-ad1e5d541450 | -2.07167 | -53.29327 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea0eab1-1cd5-3b19-b08c-b1c8d2608c23 | -3.69912 | -54.65438 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070592c4-496e-3a00-b4f4-312808d7c326 | -2.23422 | -53.66746 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8c2d86bf-c2cd-3ce5-a816-d6d200d07889 | -1.19666 | -53.69793 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ec65a6b-2a79-37e3-b58b-3bd8786759b4 | -1.30467 | -54.66912 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6636632b-fd2b-316f-ab63-833b3929f8b3 | -2.07029 | -53.30055 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef433df8-d0f2-3270-84a2-fcbefca7b23d | -3.4608 | -54.61972 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 137414e4-12ad-3da8-b9a4-4584dfa1a276 | -1.3258 | -54.6022 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f7f55d9-b99a-3ad9-b514-4520d7bfc9b0 | -2.89764 | -54.17961 | 2024-11-11 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92d9afe5-73ee-301d-b260-97f34434060a | -2.81415 | -54.01314 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77b7c427-96cb-3dfa-b271-842493204768 | -0.83766 | -53.04975 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef4d0e4c-faf4-3c60-bf63-f9283b40817a | -1.51712 | -55.00004 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf2b1e21-0746-36d5-9e8c-0e43a4d1d2bc | -3.43092 | -54.53617 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0757c9d-45f1-33d5-9d30-526712dc0719 | -3.69967 | -54.61349 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48ed165a-0171-3f42-8b45-24f81c1eb6f7 | -0.43435 | -51.98538 | 2024-11-11 05:35:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6f0e91-9134-32e8-b615-ffbc500f6dee | -0.42848 | -51.98455 | 2024-11-11 05:35:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f597d86a-9d31-3ebd-8fa9-12bf2a10a818 | -3.18416 | -54.31105 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8253cab7-d239-3a33-8d57-998d9d7440c8 | -3.62385 | -54.795 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406de16b-0c8a-3767-ad0b-cc0fb32316c4 | -1.42503 | -51.10233 | 2024-11-11 05:35:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 683944da-5ad1-3628-9745-e947518fd411 | -3.18368 | -54.3143 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 701e4864-07e5-30be-9a7b-93ece2fb552b | -1.67232 | -55.17265 | 2024-11-11 05:35:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e468a1e-b845-3216-8d88-c8f3c1977a83 | -2.07062 | -53.30044 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e1e6dd8-fd31-370e-a6ee-ac4c8216ad98 | -3.44647 | -56.9332 | 2024-11-11 05:35:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b81441-ef80-3dc2-81f5-2c79e55278be | -0.28574 | -51.72422 | 2024-11-11 05:35:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e54818e7-1335-3fed-81b6-19facb7baa9e | -1.54521 | -55.87372 | 2024-11-11 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README42.md)
