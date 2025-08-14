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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c3e3e02-d186-30b0-8f40-d6339127a076 | -23.57513 | -47.24094 | 2025-08-14 04:25:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 20b68c84-8963-320d-9a4e-bb89ba331df3 | -24.45767 | -51.81499 | 2025-08-14 04:25:00 | NOAA-21 | MANOEL RIBAS | PARANÁ | Brasil | 4114500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3cdf64df-6a1e-3aa3-9284-84664173f31f | -23.00357 | -49.18219 | 2025-08-14 04:25:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3ae67c91-09ed-3e36-851b-922faef94e5a | -22.62336 | -47.38584 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ba348ec1-55de-35b8-822e-226f9474a701 | -22.67132 | -47.45701 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f68177da-3387-31f6-8a3a-9844ba7b1756 | -22.6741 | -47.46141 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| c9364ed3-891c-3d3a-bc23-6dd154c7963a | -23.01445 | -45.37368 | 2025-08-14 04:25:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92fa290f-81bb-3da8-99ea-7931553c6d85 | -22.61944 | -47.38909 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1b83a1c4-6dbd-31e4-a4c9-502a26c878f9 | -22.85765 | -49.22142 | 2025-08-14 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb9a5cb6-2472-3322-ae23-f372bf0abf73 | -22.62279 | -47.38969 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cf4605e9-d625-3ca6-af3c-844c6afc9da7 | -29.21309 | -55.64287 | 2025-08-14 04:27:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| bcf5f1cc-7998-3fae-984c-d48f90e64d33 | -31.76764 | -52.32084 | 2025-08-14 04:27:00 | NOAA-21 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| fef025f5-a2eb-3ce5-b156-4bad746827f0 | -6.914 | -59.1455 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e5e2af66-f7f2-33d6-b1ff-ed37843d38f3 | -6.8957 | -59.1269 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6d74b853-8eea-385f-9f30-325fc4c4fdaf | -6.8771 | -59.147 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 136ed3c6-0d96-3520-bf2d-13cbaac45e6a | -6.877 | -59.1663 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1dbdbba2-eda0-3a5d-866c-351645fa9779 | -6.8956 | -59.1462 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 30c15d44-0c29-36a4-b266-9132120027bd | -9.1522 | -59.6578 | 2025-08-14 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 86d7f3d9-7cb5-3c2e-bd43-35c2cbeb73fa | -6.8955 | -59.1655 | 2025-08-14 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 9474dc2b-88d6-358d-9254-05af322a974e | -6.877 | -59.1663 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 9c199256-b8d6-350b-a1bc-13cabc62980b | -6.914 | -59.1455 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| ccaaed1d-13b4-3ead-85a7-8f24ffebd6c4 | -6.8956 | -59.1462 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| cac78dec-93fd-3a14-811e-03b19ba7f39d | -6.8771 | -59.147 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b074b137-8cc5-3c8d-ae38-9cacf882b1bf | -6.8957 | -59.1269 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e83799bb-7826-3a5e-90d0-d60db35df0ae | -2.9106 | -48.2971 | 2025-08-14 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4aa2dcea-79ae-343b-b939-285bcea83ae8 | -6.8955 | -59.1655 | 2025-08-14 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ecb36da9-5f8f-3b17-927c-16249e21482d | -5.98317 | -44.14968 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cfac1f0-7e04-36d1-9e0d-5ab49574de2f | -5.98651 | -44.14838 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d907ff9-a863-31dd-a757-86b550aad527 | -2.90882 | -48.30251 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b05b2afe-37f7-3b1c-b7eb-8f3e04a19ca3 | -2.9077 | -48.24187 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88bcc771-8c67-3fcd-b00a-3c6979145ef3 | -4.61018 | -45.61242 | 2025-08-14 04:46:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 333c4c2e-9af4-3080-ac1a-37a6d9b90b75 | -4.22857 | -47.20974 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d684eebd-3e4b-306d-8f25-cf7808ee49ca | -6.90628 | -45.21103 | 2025-08-14 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42a78b7f-bb59-3c7b-9391-fb8ddc3b8d0b | -4.22428 | -47.2134 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 297b0433-82f1-3f5d-8bcc-1e3936905ff0 | -6.61278 | -43.88454 | 2025-08-14 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 95a103d9-5ad2-3519-ae1a-1666bb5d3bc1 | -6.91054 | -45.21164 | 2025-08-14 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e706ce-6657-39f3-a2cd-3808b0239d9f | -5.89245 | -57.74351 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb929d5c-7dc6-38a2-8651-e74eb27a5db4 | -6.45293 | -44.56441 | 2025-08-14 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7602eea2-11e0-3716-85d2-e91d56a2c6f7 | -2.95519 | -51.66447 | 2025-08-14 04:46:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19d79872-beb3-3dff-8e0c-bee802769817 | -4.24291 | -47.33842 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46512d1b-f4ef-32a2-bce2-45da27f64f5a | -3.81955 | -41.56411 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| edd09671-057f-39a9-9f9b-f4f46e1e907b | -5.89166 | -57.74807 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00560b49-f437-3bea-bd55-db4abb237105 | -7.07774 | -44.94276 | 2025-08-14 04:46:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 653a7383-9537-317b-8942-1b1883014a16 | -2.90313 | -48.24873 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7ef68bf-f2c4-3f81-b782-7ab815017158 | -2.90539 | -48.30198 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fc1bdd43-4d34-381f-a835-5732784842e8 | -3.82294 | -41.57743 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef26cee0-2f83-3e3c-a413-1145241d795a | -2.36803 | -51.90779 | 2025-08-14 04:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 726e3acb-f6b0-334c-bbe8-f5c1c275b8ae | -2.90713 | -48.24557 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3721921c-5b37-377f-9399-8949ec0729c2 | -5.88006 | -43.92472 | 2025-08-14 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ab3515f-050e-3557-89a4-2b5f7942b48a | -6.552 | -44.46505 | 2025-08-14 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82db0d20-a6d6-30c9-87ae-8e5708b8f052 | -6.45357 | -44.5601 | 2025-08-14 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc59d104-773e-313b-bfac-76f07107d458 | -5.98831 | -44.14595 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9efb399-ee48-35cb-a411-9da4c0f96872 | -4.29425 | -48.05895 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 939f9940-1f20-337b-b4db-da8902fcc64d | -5.7582 | -46.66818 | 2025-08-14 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b268c4de-c132-31f6-bbe3-c0558bad0b48 | -6.94509 | -44.55888 | 2025-08-14 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae3c124e-8335-3b74-9501-eea1fb4308df | -2.7291 | -47.43969 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 004e4da1-0299-34fa-82f1-e282baf347c1 | -5.79469 | -43.61076 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de7cb9f8-beea-3aef-b0aa-7fd63c6bb0db | -3.88482 | -54.21392 | 2025-08-14 04:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e85d916-6a2d-38cd-acb6-1595c4a5a9d7 | -4.2597 | -46.66566 | 2025-08-14 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71555e77-2cb0-384e-bea4-c6b4e8524c12 | -5.89343 | -57.7452 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b848117d-6433-343e-926b-05153c265a51 | -5.78135 | -43.60379 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80bf1e83-34ef-3351-b605-2cec226e257b | -6.55281 | -44.01572 | 2025-08-14 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75ce677c-c074-3ffb-9206-bcf5ebd5c4b1 | -3.81817 | -41.57355 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9396195b-d967-305f-85c3-20613c5c643d | -4.6015 | -43.31315 | 2025-08-14 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcabc31a-e7ee-3554-88cb-f58d5cc6d4b7 | -5.98379 | -44.14528 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97ff27a9-5ae8-38c2-96b6-4f1a0ba151a2 | -5.88787 | -57.74262 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 575b1532-0f90-3284-b40a-521189146345 | -2.90597 | -48.29829 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ffe463df-8b0c-356b-9a76-808a1190ba87 | -5.79396 | -43.61578 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5698a981-098f-3e95-9572-1b544379584b | -2.44738 | -47.32689 | 2025-08-14 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f44eda09-316b-3736-9d42-89cdf492a1f6 | -3.91397 | -46.45595 | 2025-08-14 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 322dd2f7-8a03-3bb0-9d7a-9006713fd8cd | -2.48923 | -47.56881 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bc484e5-42f7-317e-b0ec-9e3a951fa063 | -2.36862 | -51.90408 | 2025-08-14 04:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6855927-8ed9-32f5-9d44-a06eb9cf95c1 | -5.97865 | -44.14898 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04631ee0-051e-37b7-9839-4ec4c5c599f5 | -5.88865 | -57.73816 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a070e9a-da74-3567-8c97-c3ea57aeae1e | -3.8214 | -41.55137 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff3776b7-6f19-3e11-bb2a-70a7162076df | -4.22726 | -47.21815 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b264cde-6462-35dc-8627-bf18318c0f87 | -4.59681 | -43.31241 | 2025-08-14 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67206a62-760f-3987-920d-ee0854187030 | -0.74745 | -47.75008 | 2025-08-14 04:46:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e275358-dbd4-3452-a9d9-57ee394cbd8d | -5.86531 | -42.84059 | 2025-08-14 04:46:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 75e9cf37-71b8-3aee-ac7d-880899dc28d2 | -3.81771 | -41.57668 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f098d796-660e-3d97-894f-560bde15121a | -2.38994 | -47.62547 | 2025-08-14 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 469c4e5c-3bc1-30ed-a9ea-a157dabf333c | -2.90939 | -48.29882 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 72b2a4e1-06f6-3e2c-b441-addc91281a97 | -3.81909 | -41.56726 | 2025-08-14 04:46:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b739c9b3-13df-39c5-8ee6-793c0a8b0b8b | -4.14527 | -46.45592 | 2025-08-14 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09613bb1-7445-3e97-a1a1-34e59160b79c | -6.55209 | -44.01264 | 2025-08-14 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b570709f-b506-3f30-a318-7b0471161db5 | -2.91055 | -48.24611 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce8b1cb7-4766-3e5a-882e-bf753ef9ce47 | -5.88325 | -57.74195 | 2025-08-14 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73aef73d-104d-31e9-b446-67f5356a4b7b | -6.61812 | -43.88037 | 2025-08-14 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6488e67-4ed2-3ef3-95aa-061d3d5b321d | -5.98133 | -44.15213 | 2025-08-14 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b74aad9-0ba9-32ab-a6a7-098f21095c53 | -3.99261 | -43.24145 | 2025-08-14 04:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86624160-54b2-3364-aed0-79a3bfeb120c | -5.78603 | -43.60449 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c550133-87f1-3b55-8fce-d30e6630c5f5 | -4.22363 | -47.2176 | 2025-08-14 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3940cb-40c1-3c38-8263-83ab1864c2c7 | -6.61348 | -43.87967 | 2025-08-14 04:46:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b59dc351-8034-354e-9026-e5bf01ef2a38 | -2.36744 | -51.9115 | 2025-08-14 04:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b428f45d-9f4c-3822-b530-dd600069aa27 | -6.18488 | -43.30627 | 2025-08-14 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e9e0ee0-0227-3491-aff7-abae72a9bff8 | -5.15768 | -39.50534 | 2025-08-14 04:46:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 163e5b42-7220-3d9b-811e-621d2812e5f4 | -2.29854 | -48.14289 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd6c7382-a60c-37dc-89f2-b51d5c57ca3d | -5.78062 | -43.60886 | 2025-08-14 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ac51c72-2cd8-3aae-8b98-809a9606195d | -4.4816 | -47.66848 | 2025-08-14 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be97169-a574-3035-9698-0128a7881aa5 | -2.90998 | -48.2498 | 2025-08-14 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README18.md)
