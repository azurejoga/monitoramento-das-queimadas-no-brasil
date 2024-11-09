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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1c3fd5d-0928-3578-a686-4dc90aa08d2e | -2.3604 | -46.8776 | 2024-11-09 13:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| e22b379c-bbc5-38e0-9b1e-8c4afa6c9e72 | -3.2353 | -50.2645 | 2024-11-09 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 09d3018a-a911-3dab-92ee-45d9512c5300 | -2.2803 | -48.744 | 2024-11-09 13:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 41cb4484-c8ab-3658-ab43-f06dda8b8172 | -2.0478 | -46.0903 | 2024-11-09 13:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| d2f82dff-f960-3939-88db-fd63668aee0c | -5.4359 | -43.2673 | 2024-11-09 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 8847de9b-24ab-3f96-824d-3c0c8a614e1e | -3.125 | -50.1419 | 2024-11-09 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c1adeb31-8666-31dc-9fd2-331c3f1a6e60 | -3.6111 | -48.9167 | 2024-11-09 13:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 15ebaef3-0a0d-366d-9d68-c44d896bdec8 | -3.2352 | -50.2855 | 2024-11-09 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 9b7fbc24-b0e7-3e51-96a6-7cd686e8836b | -5.7146 | -43.5261 | 2024-11-09 13:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5831a410-055f-3751-98a7-1b6473a5c001 | -2.379 | -46.8552 | 2024-11-09 13:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 1bd21e40-1ced-3264-b1eb-4ffddf9d05ae | -1.5164 | -52.1491 | 2024-11-09 13:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2fb079b8-ebdd-3560-a4ce-5d565c3c6621 | -17.6079 | -57.4688 | 2024-11-09 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 16262fb9-0643-3003-8bcf-3c4f79a4974d | -3.525 | -44.0286 | 2024-11-09 13:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 684cfd9c-fd87-3f16-a52e-f3d56ebb2168 | -5.4734 | -43.2646 | 2024-11-09 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a234f353-d727-3d7f-9d19-7da4ba509152 | -3.9483 | -48.1724 | 2024-11-09 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 996151b5-fa97-36db-8d42-39bd47ec1da1 | -2.4104 | -48.5265 | 2024-11-09 13:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 0a59664e-6999-3680-b7de-8325d11f30b0 | -5.4544 | -43.2893 | 2024-11-09 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ff17aac9-0735-3e09-a90f-d67a38cd6b63 | -1.5164 | -52.1696 | 2024-11-09 13:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 0e58acdf-5339-3daa-b27d-cd304c6fffc1 | -2.4105 | -48.505 | 2024-11-09 13:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 51d1ff30-6ded-3366-9b49-f87beb3b6f79 | -2.6758 | -46.7806 | 2024-11-09 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4c3f0278-b4f6-366a-ae6c-e7b28e55efcf | -7.4476 | -44.7163 | 2024-11-09 13:30:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b104bb9a-567d-3f35-909a-07bb983ed540 | -5.4548 | -43.2426 | 2024-11-09 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 351f8572-5c5e-3ed3-9b16-306333af2c06 | -7.4474 | -44.7392 | 2024-11-09 13:30:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| bbfd2c59-76bd-3cc5-b94b-89c47b1d69cf | -1.498 | -52.1699 | 2024-11-09 13:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d3547f63-7664-31e4-8507-c44f37014556 | -2.2804 | -48.7226 | 2024-11-09 13:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 073d63ea-e176-3749-87c8-e0d6a7fc3715 | -0.2299 | -51.6455 | 2024-11-09 13:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 93.8 |
| cb34e769-5c33-3796-a488-10b9d5e505aa | -2.3555 | -54.7627 | 2024-11-09 13:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f503ff43-af66-3eb5-abfc-3511af351bda | -17.6083 | -57.4482 | 2024-11-09 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 9b482be2-459f-3a22-bec0-63c0d4c349b8 | -4.8068 | -44.7834 | 2024-11-09 13:30:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 7e58190a-0525-3272-a3b2-39f68e13783d | -6.1836 | -45.4597 | 2024-11-09 13:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 54999ddc-f7bb-365f-a162-83dd4185bbd8 | -1.3838 | -54.6373 | 2024-11-09 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ae3dc77b-cedc-32fe-bfe9-b6cc1f9154dd | -3.0319 | -50.3547 | 2024-11-09 13:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 9510a8f3-db81-365e-b5ed-bfc4f1f95c01 | -3.5339 | -42.4449 | 2024-11-09 13:30:00 | GOES-16 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 8a4af881-77c9-3760-90fd-10a762bc06a0 | -5.4546 | -43.2659 | 2024-11-09 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 0b4fb511-3006-3360-a6b5-355efc141f1c | -3.5462 | -43.5663 | 2024-11-09 13:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a6387640-2845-3b8e-953c-ba92cfa38184 | -2.2295 | -53.7832 | 2024-11-09 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 316.4 |
| 09b80204-6377-3d35-973a-1290c9727b5f | -2.9046 | -45.3044 | 2024-11-09 13:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a858691f-30ec-35e3-8d66-c9bf429fab71 | -2.3605 | -46.8557 | 2024-11-09 13:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 4ece7d29-9ba7-3dcb-8e77-976f9943a733 | -2.2479 | -53.7627 | 2024-11-09 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 139e13d3-0348-3c0a-86ef-949190cd2948 | -3.9669 | -48.1716 | 2024-11-09 13:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 4e2af837-298f-349f-b78c-aaeb46f30f04 | -1.5164 | -52.1491 | 2024-11-09 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6a879468-d381-3b24-9ba7-fb009d18d6a2 | -3.2353 | -50.2645 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 314.3 |
| c8cedbd5-43b8-352f-88fb-cecb1424e460 | -2.9058 | -49.5364 | 2024-11-09 13:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 84b7353c-d51d-345e-b22d-b9ed6b02b2ed | -3.2538 | -50.2639 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| d57e6014-fa82-371c-a195-a30b9a78589d | -2.4365 | -46.3241 | 2024-11-09 13:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d2b624b8-5cb0-36d6-8601-625ebec25333 | -3.2352 | -50.2855 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 244.2 |
| 79ec1a67-2146-3e29-8798-c8749545fd1b | -4.8068 | -44.7834 | 2024-11-09 13:40:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 370.8 |
| a008523b-2787-306d-9b6e-34d6d0380939 | -3.2154 | -50.6213 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7cd0ede2-093c-3160-88ca-877ee290184a | -2.3733 | -48.5703 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 5f21ce9f-37a6-361c-b404-3f5223183d3e | -2.3555 | -54.7627 | 2024-11-09 13:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 74fab157-f5d2-3638-afda-0cc089e6c8ff | -2.2295 | -53.7832 | 2024-11-09 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 4434d3ed-b820-3e11-9017-6534f2502ff4 | -5.4413 | -44.8335 | 2024-11-09 13:40:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3c3b5a58-57dc-3518-853d-86ee3c2d0954 | -3.125 | -50.1419 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| eb39c4e8-33b3-38b1-96a2-d829046d0ef6 | -0.2299 | -51.6455 | 2024-11-09 13:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 151f920e-3715-3617-b801-6416e9327926 | -4.2058 | -48.5491 | 2024-11-09 13:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 24c17924-8829-31b8-ac31-bfedffaeeb1b | -3.0319 | -50.3547 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1e7bf3ef-8f58-37ae-b6d5-775afff66ee0 | -2.0293 | -46.0908 | 2024-11-09 13:40:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| aae591e6-88fe-372e-880e-a2d2644969cc | -4.1246 | -43.5833 | 2024-11-09 13:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 64c3bdc7-12b4-38b2-ab7c-963ccffb1b4e | -2.3556 | -54.7427 | 2024-11-09 13:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4aa1949d-4e21-3aa9-b98a-1b30c9eeb120 | -2.2804 | -48.7226 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bdd114e3-6926-3ff4-afd9-b462e40c34ee | -6.1366 | -42.5544 | 2024-11-09 13:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 656d4d95-9767-3b37-91ed-a1345d46cdb7 | -5.4544 | -43.2893 | 2024-11-09 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6a22bdd9-4fc0-3ad6-8e8d-40ebae0c8381 | -2.3076 | -46.0391 | 2024-11-09 13:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 53653008-0876-36aa-beb8-3ecbc0f4ca9a | -5.7146 | -43.5261 | 2024-11-09 13:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 217c1483-950d-31fe-a029-035992bf843a | -4.807 | -44.7606 | 2024-11-09 13:40:00 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| d99d386b-7381-368a-9f31-606b084f3c45 | -2.2479 | -53.7627 | 2024-11-09 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 1509b4d8-dcdf-3c45-b500-d2586be1c981 | -1.5163 | -52.2106 | 2024-11-09 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9df6402c-0fa3-377b-ae2b-bbe41a3dcd55 | -3.5339 | -42.4449 | 2024-11-09 13:40:00 | GOES-16 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 3e55ae4b-628a-3597-ae08-1334efddb65e | -2.455 | -46.3235 | 2024-11-09 13:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 251.5 |
| a8d614c0-e666-3c27-afdb-eaa9eb68fadc | -1.498 | -52.1699 | 2024-11-09 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 20bbde90-7121-3674-94b9-ed9c63b66f23 | -0.6177 | -49.5351 | 2024-11-09 13:40:00 | GOES-16 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6d352344-deb5-3f2a-8910-0da20be1f0a0 | -2.5781 | -48.1777 | 2024-11-09 13:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4d0fdf95-b286-36e3-a859-9d9ad9565430 | -3.525 | -44.0286 | 2024-11-09 13:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 226.6 |
| cc8bae58-413d-37e3-97d6-bc9ae7c63acc | -3.944 | -48.989 | 2024-11-09 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8dffcd8a-1464-39ac-b8c8-717fc81e49a5 | -2.4105 | -48.505 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 7d0a5e54-6d18-3f68-a569-0fd93b2643be | -17.6079 | -57.4688 | 2024-11-09 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 86e6dfe9-5389-3407-a889-c78d8bb1d1e9 | -2.2322 | -46.4182 | 2024-11-09 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2d3f1dd9-d3f0-37f9-bc14-56885f2e3e7e | -2.2803 | -48.744 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 16b518dc-fb00-37d3-be54-2a90f5e3bc76 | -5.4734 | -43.2646 | 2024-11-09 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d15603e5-1d76-3602-925d-01cf56957aee | -5.4689 | -41.656 | 2024-11-09 13:40:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 2e6ebfed-9c5f-31fa-b863-c163c70d346f | -2.4551 | -46.3014 | 2024-11-09 13:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a18f82fd-2b48-3011-a0fd-74883b708f33 | -2.379 | -46.8552 | 2024-11-09 13:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| bd4e39f3-11f4-3ad9-96ad-7947cb9982f8 | -3.6111 | -48.9167 | 2024-11-09 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 6423de5f-c8b6-38de-a5d2-c81d503c92f8 | -2.6758 | -46.7806 | 2024-11-09 13:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7ebbbfa1-3c9a-3df5-9087-40c903c96f88 | -3.125 | -50.1629 | 2024-11-09 13:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5455d8c2-61f9-3880-9a0f-018fda72bab2 | -2.2321 | -46.4403 | 2024-11-09 13:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 043326d2-2612-3dd6-bcf5-6965b0f693a3 | -3.9669 | -48.1716 | 2024-11-09 13:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 11e6019d-88a8-3fd2-a372-9f0eae174904 | -2.4104 | -48.5265 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 6cd65449-e86c-3c0b-8e43-73025799c918 | -17.6083 | -57.4482 | 2024-11-09 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| cf23283f-2250-3f8e-a3f0-805bbfd8cda6 | -2.2479 | -53.7829 | 2024-11-09 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 244.9 |
| 34d02047-fb27-3467-98eb-6cdad5c500fd | -2.578 | -48.1992 | 2024-11-09 13:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9c7ad863-6f46-3073-8034-b13355ffc32b | -5.4359 | -43.2673 | 2024-11-09 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| abed3579-4f7a-31f2-b53e-34bdb413c03a | -2.6459 | -49.903 | 2024-11-09 13:40:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cd177003-d9a9-3974-8532-90f9a298de71 | -3.7839 | -47.7242 | 2024-11-09 13:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8910fc42-62e1-3a8b-91fd-7ca6c20b5b87 | -5.4546 | -43.2659 | 2024-11-09 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| edab58bf-e5c0-3f3e-8771-b72d3af3df14 | -1.5164 | -52.1696 | 2024-11-09 13:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 510ddfbc-5ca5-3980-9b1e-6fe3ee2273fe | -3.5462 | -43.5663 | 2024-11-09 13:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 2cd253d5-cccf-3b87-98ea-740fa07f9e7d | -2.3918 | -48.5699 | 2024-11-09 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ba959652-e302-38b5-9e07-4b0bf9397faf | -2.2295 | -53.7631 | 2024-11-09 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| afd07181-20ca-3343-b039-330d1098bae6 | -3.9624 | -49.0096 | 2024-11-09 13:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README121.md)
