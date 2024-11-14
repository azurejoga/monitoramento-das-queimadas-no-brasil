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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a0d085-3cea-3cfc-bea2-1128f4c62670 | -3.7139 | -50.6255 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0a7847e5-4555-3067-9de3-1c7f723f7c03 | -17.5869 | -57.5533 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 194.2 |
| 5201afde-bf45-3e07-91a0-9f5f4a75b113 | -3.0523 | -45.5237 | 2024-11-14 00:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 569bd526-3e29-3700-be55-046e8f286beb | -17.6263 | -57.5486 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 38989fe0-eea4-3b49-9ce4-6e49dd501973 | -3.714 | -50.6046 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5b3659e1-3955-32ed-83f4-efcc05fb1fc1 | -17.5879 | -57.4917 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 4c2b0b14-3a1e-3294-8651-452d5dddf88b | -4.2135 | -50.5016 | 2024-11-14 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| edf9d8d2-66e4-3115-b9eb-4f0073aa73c0 | -2.6564 | -47.0008 | 2024-11-14 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4a34fd2c-0d91-39fa-abec-1ee6378a8d6b | -17.5672 | -57.5557 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| ea4bdeb6-392d-30a5-8f9e-3926f698e921 | -17.2543 | -57.4698 | 2024-11-14 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 8343d7b3-e816-3735-8205-bd2081fbdd41 | -5.2023 | -44.3473 | 2024-11-14 00:30:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| aa112cf4-bd58-32f1-b820-00726c3d7600 | 1.048 | -60.5986 | 2024-11-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3040d4c7-0dd3-32b6-80b9-8283c636d6c0 | -3.2916 | -50.0524 | 2024-11-14 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 85c24518-32d1-3a2c-8621-13ad91118f2e | -4.0682 | -50.0029 | 2024-11-14 00:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8a6fcbf4-3c94-37fd-b337-015aee2d649b | -4.0005 | -45.5503 | 2024-11-14 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 9e661a9a-323d-3e8a-b92b-d45add7477cf | -2.6751 | -46.9783 | 2024-11-14 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 0d8f1ced-c6c1-34c3-8d1e-448483c785b0 | -17.6066 | -57.551 | 2024-11-14 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 7328f78d-f1ea-3cbd-bf61-2efcdbe6774f | -1.4078 | -51.1195 | 2024-11-14 00:30:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f85127b7-8c90-3687-87aa-7b29f6982425 | -0.9102 | -51.7243 | 2024-11-14 00:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 3790711a-eb2c-31e9-8162-dc1a524e43ad | -2.641 | -46.1849 | 2024-11-14 00:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 51bfef42-6db4-3923-b608-f7f8f207ce5a | -0.8918 | -51.7245 | 2024-11-14 00:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 3990aee7-c177-35ab-94f0-6748d05044bc | -2.0268 | -46.9299 | 2024-11-14 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 8ce245c1-9c74-3f16-a934-caa6fa3f0d34 | -3.0358 | -45.0741 | 2024-11-14 00:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 32e2c730-2eba-3eb9-a8ff-c9ff01329f30 | -2.6565 | -46.9789 | 2024-11-14 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7d3def19-551d-33fc-b848-ec8f6dfc1efa | 1.3034 | -60.4263 | 2024-11-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 05264e4f-a533-385e-ab28-abff15e8068e | -1.369 | -52.3558 | 2024-11-14 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| dc57379a-81d0-3c8d-bbb4-44abf33fab8a | -3.1463 | -45.2954 | 2024-11-14 00:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2511d809-4399-3a65-be33-d3f62be4c461 | -3.4014 | -50.3011 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c39d22cf-e5b0-317a-aca4-2cbe2b1af1ff | -3.6402 | -50.5863 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f87971b7-e35e-3762-a445-77d90cabdff7 | -4.0189 | -45.5719 | 2024-11-14 00:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| a0841259-cf2a-3547-99fe-9e8bc46fb05a | -3.4755 | -50.2566 | 2024-11-14 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b9a0e2c4-d4e4-372c-abc5-1c73c277fc52 | -2.675 | -47.0003 | 2024-11-14 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| eb2b513b-502f-3480-b92a-0105f672e0b7 | -3.1464 | -45.2729 | 2024-11-14 00:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 03e8f5a6-d727-3024-8093-5f560b54b5a2 | -5.5676 | -45.3687 | 2024-11-14 00:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8697fc8a-e1a0-379f-bcb7-69d29de778c5 | -2.8791 | -51.7932 | 2024-11-14 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| a44926da-b7fc-32f3-95d5-fa38148d6845 | -2.9708 | -45.857498 | 2024-11-14 00:32:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31e9df69-9ea3-3c4f-ba0f-551ad9cba23a | -2.3546 | -46.981899 | 2024-11-14 00:32:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 502c94dc-ca44-3f01-a9f6-506570d99718 | -4.278 | -46.880501 | 2024-11-14 00:32:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d73d5bec-3517-37a1-988f-4bbf92a95f90 | -1.3436 | -51.424801 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11e2302d-41f9-3413-b318-ff910b614ae7 | -3.5458 | -49.903999 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f47c4170-7c75-3261-88a5-7e5693d5dbef | -4.3219 | -45.4263 | 2024-11-14 00:32:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0074a079-e1af-3a45-8de0-2c3192780762 | -3.1633 | -45.444599 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2871fc76-3c37-33c7-b04d-3564614639f2 | -2.0241 | -46.9319 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ffec21-82dd-3ae3-998b-1df924d294e3 | -1.8451 | -46.285 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa78a1c-792b-37a0-9e0e-0bd38fa00972 | -2.0164 | -46.943298 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03220007-a98b-31b3-8ca6-5cce310a22bf | -1.3825 | -51.0947 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9993fb6-6666-3f67-8020-f1db6d83a392 | -2.2416 | -47.477901 | 2024-11-14 00:32:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d01f713-9af3-38b6-8321-54eedf2ad88e | -2.8791 | -46.8442 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 539e069e-645b-3366-9ad7-86ed89b397de | -2.9721 | -51.243599 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 798b26b8-d4fc-3bfd-9ca7-32c0beb9eaa0 | -1.6037 | -52.396702 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acda078c-ddc7-3d8a-905c-f9bba69d8d23 | -2.3575 | -46.500702 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2988a14-4e92-3a42-8a95-5a66899c76fa | -9.1556 | -50.529999 | 2024-11-14 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41641908-0498-3619-8a9a-a3d524b26a41 | -1.3672 | -52.352901 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12b999e1-04cc-3ce0-8d47-3207cffbe116 | -0.2172 | -51.502602 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c7902b67-48d9-3ff6-a407-a98e033a8580 | -0.8907 | -51.747002 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a0d8da65-8b64-388f-a4e4-bc5e3f222996 | -2.6491 | -46.829201 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c650418a-d8f1-3ff6-be60-446bb721f76c | -4.0044 | -45.5658 | 2024-11-14 00:32:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae9c0d5-cd8a-3418-8c89-2976d3d42010 | -2.6563 | -51.717602 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc64fdf-943a-3b6d-9c81-395dd16a17f0 | -1.3527 | -52.334 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b465bd74-624a-3a1f-8572-a55f0b92ab43 | -4.2729 | -48.205101 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f86b9eb5-9ad0-35ec-ae70-543148854f76 | -1.3704 | -52.367001 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62651849-f00b-3033-8484-2244464c847e | -1.6066 | -52.226501 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2079bc8c-9960-3fae-9588-283085ce0346 | -4.065 | -50.012001 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c853ae6e-dc18-341a-b770-185af08ea4e6 | -4.0374 | -47.222801 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 076766ed-179d-3355-8912-26d064be0c24 | -3.2998 | -49.864498 | 2024-11-14 00:32:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28eea14b-e01a-3694-aa7c-1b35d76d9a78 | -3.2651 | -50.577301 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1798e662-e9a3-3176-b1cd-073c6058c4d8 | -3.8688 | -52.257099 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e232d29-83e0-354b-9aa3-7c77f45c6338 | -2.0169 | -46.496201 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8b5ae0-88bd-36a2-8c8a-7292681b0ce0 | -3.3276 | -52.783298 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d6603c-c012-3348-a4f6-0a2fc9acf177 | -3.2717 | -50.058899 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba32c9fb-fef7-3332-9b3a-7db76659b00c | -3.9403 | -46.399502 | 2024-11-14 00:32:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b29f6b6b-8f43-3028-8b79-58637856cb99 | -2.1488 | -50.5172 | 2024-11-14 00:32:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9877fc-5773-38da-be05-9a96c3990f1b | -3.8134 | -51.917099 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3193c55b-f1f4-31a0-901c-e3c0d7332c3a | -3.0351 | -50.334702 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d7aac4-b12e-37c2-898b-c6b881800e21 | -3.032 | -50.320999 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4127f0a1-df01-3b44-a7df-940afca73981 | -2.3601 | -45.974701 | 2024-11-14 00:32:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 777fd471-62c1-3b9b-98aa-66c0f3df3273 | -1.6615 | -52.562401 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40336716-955f-36cd-b7a7-34eef1121f5e | -3.5197 | -52.9062 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924b88fa-fd06-3e89-bd54-e675e5d187a6 | -6.0325 | -44.033298 | 2024-11-14 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3de01df7-9e2a-3f1c-ba75-7903408f46e1 | -3.4008 | -50.310799 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ff1ee7-40f6-3f36-a7c0-3b46fe6fcedd | -2.6945 | -45.551899 | 2024-11-14 00:32:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b844718-2ad0-3bb0-bf21-d1ecb58dc260 | -3.4596 | -50.297699 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70f574c-0e1e-305c-87d7-e6f74660da24 | -1.3688 | -52.359901 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d7ab53-f1ff-3832-9139-fdcf3cfb7c1f | -0.2141 | -51.488998 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e16d286d-1afa-3f09-82fc-2e70d542233c | -3.627 | -50.582802 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4122a978-89e8-30e2-a198-1aed4bf2468a | -1.0453 | -47.333099 | 2024-11-14 00:32:00 | METOP-B | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9740cf-5ab5-32e1-bb3d-72e887839228 | -6.937 | -39.818298 | 2024-11-14 00:32:00 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 23e2e859-e159-3377-9333-4adb60a326b7 | -2.0143 | -46.934101 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c085d81b-6ec6-3b2d-a6a4-c9e32c190bed | -2.8811 | -46.853298 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e872d42-9a37-3d80-a9c3-fb2d75fb8ce5 | -4.3492 | -49.673801 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf9b6c62-0103-3ef5-93b0-f7138ae7d515 | -0.8845 | -51.7197 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9e08d952-de09-3382-a707-5bac183f7d5e | -4.6064 | -46.295601 | 2024-11-14 00:32:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b689e314-2e87-37b8-87d5-0a9187a8996c | -5.1838 | -44.361599 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53d7a749-1ea0-3e85-9793-f84ed263ed04 | -1.4449 | -52.240299 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c4eeee2-1178-3a99-86bb-3c41edf17f58 | -4.0471 | -47.220501 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| defc258d-970f-37d9-b8dc-6d9f3db4b9d9 | -2.1826 | -46.366001 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff9a239-7030-3f76-bf7b-44ad15a46899 | -3.8773 | -46.083 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07652da5-9334-3084-a00b-dc7afba11f07 | -6.0166 | -48.030499 | 2024-11-14 00:32:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a662765-dc16-3af8-9379-40f4dd345026 | -3.2702 | -50.052101 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1268456b-4b18-3ea3-b737-f3d2e8734549 | -1.9387 | -52.145901 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
