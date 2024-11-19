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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3fdc09f-7677-3b13-9599-35d1a02974af | -8.00297 | -44.39651 | 2024-11-19 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c034db14-e925-3638-b1e9-d737d78ea047 | -7.896 | -44.22695 | 2024-11-19 00:43:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d29af4c7-27d8-339c-87dd-535c56cf3a61 | -8.68099 | -47.97736 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0f6ffa48-85fd-36a3-9cd0-4b6747c9bf3c | -9.72158 | -48.12614 | 2024-11-19 00:43:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f2e4152-f787-3f42-9dd0-f31393c0fc21 | -5.95244 | -39.68393 | 2024-11-19 00:43:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 443733d0-f566-3fb5-8089-8115dcbae060 | -6.25508 | -43.56824 | 2024-11-19 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 7fd8e7da-b007-3768-b842-dd601be4e569 | -7.5728 | -46.45813 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| cd0a9378-a005-39c5-bc9a-6f7fadc51b84 | -8.00033 | -44.37794 | 2024-11-19 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 41dc7373-6097-3bfa-aa27-dc5c6a38a26e | -5.39305 | -40.65523 | 2024-11-19 00:43:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| b4355cc4-b9a1-3149-81d0-d43604a21c4d | -10.90068 | -44.56182 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 34244778-3266-39d7-beff-036acb292cf7 | -6.40122 | -44.73102 | 2024-11-19 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d3a3aa15-f39e-3835-8a1e-9e4835b89590 | -9.48877 | -46.12559 | 2024-11-19 00:43:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2c5ab734-b8c3-3b4f-bc17-4d30d99b7792 | -9.54404 | -40.33651 | 2024-11-19 00:43:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 2d7379df-6f76-32f1-a0d7-7b07ce4e4a56 | -8.67285 | -47.98916 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e4e3d45d-39a2-334e-b73a-3dcd75a06178 | -9.24939 | -44.9968 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b77f26cc-c961-311f-81b0-285ebe99aae0 | -5.94843 | -39.6591 | 2024-11-19 00:43:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 0094fea2-db08-3b42-bf60-fda40bd993d5 | -7.39993 | -42.77182 | 2024-11-19 00:43:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 7abe3e88-41fd-361f-86f4-2bf283feda3f | -7.90764 | -45.94218 | 2024-11-19 00:43:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1da3f977-9a4d-3dca-990e-18b08400dcf0 | -10.52625 | -49.36922 | 2024-11-19 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2941d7e8-547a-38e9-b118-1faf7036bd4e | -7.99901 | -44.36864 | 2024-11-19 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5b879cc6-13e7-384e-94df-f7f4346d2d3e | -11.89053 | -43.80938 | 2024-11-19 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 360cf402-c086-370f-bf92-e9b3ecc2528d | -9.25952 | -45.00446 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 96039743-6881-3f9f-b0b9-8031909ec205 | -10.84827 | -44.25483 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6a5dfdf3-81c9-3576-a93f-5325a62fd15c | -5.9683 | -46.30739 | 2024-11-19 00:43:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3c859cc-86c6-3a4c-b1ab-a5dcf827c3f5 | -7.39827 | -42.76052 | 2024-11-19 00:43:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| af19f32b-c74e-3c6d-b7fc-042a320d61ec | -9.26203 | -45.02236 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fd34c95-0f3f-3f9b-9412-debb855c51c5 | -11.02493 | -41.74103 | 2024-11-19 00:43:00 | TERRA_M-M | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e6e1d19d-5187-36b2-83cc-4fc29125656c | -6.04572 | -46.60419 | 2024-11-19 00:43:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 00ad40ac-be2b-379c-b67a-dc4c4d0ec04d | -9.25826 | -44.99551 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 811ec5c7-10dc-3709-be6b-78cfa5fbde5b | -5.38782 | -40.66181 | 2024-11-19 00:43:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| f03ebe80-09c4-3541-a860-53bf633390f2 | -6.05667 | -44.04949 | 2024-11-19 00:43:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1dd96047-1ecc-3a1c-967a-27053ac253fe | -7.57156 | -46.44914 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c864524e-f9ec-3048-ac51-f3b12dce0ceb | -5.98509 | -45.36922 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bde10e4a-0ced-3552-97fd-4586e69ecd7f | -3.02666 | -48.00998 | 2024-11-19 00:45:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a90a2cee-e95a-39cb-a58e-c117e6cf7a08 | -4.44969 | -46.11609 | 2024-11-19 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8b194b54-3a39-3be7-b581-09e653c0e452 | -5.30614 | -44.28765 | 2024-11-19 00:45:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| abadaf4e-205e-387c-a566-edf65c3a686d | -2.65049 | -46.55602 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0694f198-712a-3b99-86c1-eb47de89dad0 | -3.70607 | -43.47749 | 2024-11-19 00:45:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dabffd44-9751-3918-85f6-240d9d38c7a8 | -3.3162 | -51.537 | 2024-11-19 00:45:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f1b98204-bceb-38d7-9f8b-da8d868a6585 | -5.58223 | -46.44067 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e170e1aa-ee11-3278-9d47-eb4ea499bc4b | -3.37163 | -54.11799 | 2024-11-19 00:45:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 90f8dca5-488a-3d98-b66c-dd2886f61e27 | -2.65914 | -48.48374 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| dcf6b0cd-1248-3907-93a8-20d1112c53cf | -2.69072 | -46.05627 | 2024-11-19 00:45:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 066cea78-01b3-3c10-bfa6-702d9b55a6ff | -2.94986 | -48.31826 | 2024-11-19 00:45:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d1689e1-10bf-3ff2-bd5a-93e0451c1802 | -2.33437 | -45.68273 | 2024-11-19 00:45:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ca1d96ff-9e93-3e93-bd79-ff457264bd25 | -1.94394 | -46.51575 | 2024-11-19 00:45:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0b3cdcfb-67bd-30a4-a06b-266d22f893d1 | -4.22937 | -47.18238 | 2024-11-19 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 046b73ec-50cf-3aad-8e11-e1c2449072e6 | -3.75118 | -44.56682 | 2024-11-19 00:45:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 30225d22-41fb-3c64-b371-5c1d4eed141d | -3.56627 | -50.25995 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a44855b4-be47-33c2-94a8-95805d787d94 | -4.95411 | -49.50267 | 2024-11-19 00:45:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b6d12a0-ed6f-3a69-bc99-85831673c4ce | -3.32449 | -52.71323 | 2024-11-19 00:45:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c22b714b-055f-3673-8a65-eb1735f5bb6e | -3.30808 | -45.33636 | 2024-11-19 00:45:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bafa268f-ed63-331c-b716-12ec8d124e24 | -3.39598 | -50.35808 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35333faa-099e-3555-8a19-38095d319fab | -4.82805 | -47.31855 | 2024-11-19 00:45:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 46b8e1dc-9402-3da2-beb8-bf719d96aa86 | -2.57002 | -45.5902 | 2024-11-19 00:45:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b4f23636-73d0-38ac-9e7b-11122ae718ba | -4.45092 | -46.12494 | 2024-11-19 00:45:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65f4c399-75ca-31ea-bc6d-bbbbcae75ec6 | -3.34287 | -50.48613 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44b82478-25d0-3027-9eb6-45bba01113f5 | -2.61178 | -46.81025 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7b162e3-95a9-3226-b5f3-47ee9cbad6ba | -1.99904 | -44.79918 | 2024-11-19 00:45:00 | TERRA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fb044928-55c6-3b8b-b9b3-03adb137e44f | -3.88092 | -46.66238 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6824d905-3766-373a-bca9-aad714f3517b | -2.79619 | -48.60508 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7c5276c6-8020-3a3f-854e-86226763864f | -2.63176 | -46.565 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e78becd-196b-3892-81be-3646cb581900 | -4.2306 | -47.19127 | 2024-11-19 00:45:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9aaf8453-53b5-3d64-896b-25bfd24fddcb | -2.51813 | -45.28516 | 2024-11-19 00:45:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 73bc470a-ef8c-3c16-848d-ab467454b14c | -2.95117 | -48.32771 | 2024-11-19 00:45:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d3547270-d79a-3841-b306-d63247ea00da | -3.36842 | -54.09439 | 2024-11-19 00:45:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d29f59e6-50ee-3d24-bb7c-2bad19e2567e | -4.09671 | -44.8528 | 2024-11-19 00:45:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60cecc0a-c094-37cd-adc3-4e8c3f49147b | -2.69827 | -51.88203 | 2024-11-19 00:45:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 14ce21c6-5354-3b8b-a4ba-7ca9e4679cc5 | -3.04856 | -40.07348 | 2024-11-19 00:45:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 14ce5579-550b-3380-8d80-4e36bac47556 | -2.7228 | -45.96041 | 2024-11-19 00:45:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 654efb24-8c07-3357-b203-9c6b7051cfb0 | -2.84156 | -46.66957 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5505c58a-55da-3584-8d47-3aa50fd791b3 | -2.91031 | -46.83937 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d90a8cab-8960-312a-aac8-85d7b3b84cda | -2.68029 | -46.17594 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a42b0fc-0824-33e9-99ee-1745cef4f214 | -3.2865 | -50.62366 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e858e7d3-b16e-333d-88fd-11fe45523b96 | -2.78294 | -48.57741 | 2024-11-19 00:45:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c0a710d-ad7f-30ed-a075-14e1f31e9b38 | -2.99611 | -45.15154 | 2024-11-19 00:45:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 067470f4-6b84-3e41-b6d8-6aa679f8329d | -4.99793 | -44.33114 | 2024-11-19 00:45:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e574fa4c-eedb-358b-bc0e-200077f809a0 | -3.94739 | -46.41297 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a4208add-b2dc-3a77-b385-6c02b6f35611 | -5.59109 | -46.43942 | 2024-11-19 00:45:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72d18d25-a41c-3dce-aae4-d5732e98bc06 | -3.15764 | -45.44524 | 2024-11-19 00:45:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6bb02fdf-d10a-34bd-b6dd-d686859e4f50 | -3.03716 | -49.46613 | 2024-11-19 00:45:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 775e0060-1a64-35b2-8e8a-f6ce0da9a9e0 | -4.73069 | -49.5107 | 2024-11-19 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 27f05ac8-4d99-32ab-b8e4-6f3fa619922a | -3.52004 | -50.22895 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d7b0cbd7-82b5-3cdf-86bf-8c9e6544d28c | -3.50812 | -50.2182 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 754f33cf-e63b-3387-952b-6bcde3c2288b | -5.38824 | -46.11086 | 2024-11-19 00:45:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c344146-8df9-3a49-9d95-974125ea335f | -3.56459 | -50.24766 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e7f5dce-6c37-32eb-8e44-239623768a65 | -2.72418 | -51.81514 | 2024-11-19 00:45:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5b2a46f9-0a3f-3da9-801d-a3d3d10c25f9 | -2.23386 | -46.48367 | 2024-11-19 00:45:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e73ad7a6-1181-39e8-a9f7-fc815b529f6f | -4.22207 | -50.67596 | 2024-11-19 00:45:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f756338-68d2-3b3a-bcf8-faf48a014c4c | -2.68777 | -46.22924 | 2024-11-19 00:45:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 5e1e380e-db31-3fca-b4b7-73b28711bdae | -2.66349 | -51.71445 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8eca0841-4389-3467-a3c8-a679276eef7b | -4.30654 | -46.74881 | 2024-11-19 00:45:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0cedc22e-6794-366d-897e-c3160be78f53 | -3.42375 | -50.25422 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c441f16a-fd76-3945-ad1f-f9be7e0791a8 | -3.19662 | -52.44205 | 2024-11-19 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b23b7adc-1446-3ce0-b3b7-ef761ae00c5d | -3.51313 | -50.23627 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 90ea69c4-f356-33f5-8715-4d4a8ac4cb11 | -3.33413 | -50.50017 | 2024-11-19 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 30cfa75a-eaa4-3d51-8f20-187563b760a1 | -3.38745 | -52.8001 | 2024-11-19 00:45:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 0af8d342-7377-3f6f-96bb-7b206721c874 | -3.53727 | -50.40879 | 2024-11-19 00:45:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 49000e92-17f5-35a2-a462-4db5fe6eb601 | -3.61549 | -54.2174 | 2024-11-19 00:45:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| d1096c94-9f98-3a3d-a228-e8c214289a65 | -2.63437 | -46.84295 | 2024-11-19 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README8.md)
