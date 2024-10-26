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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96aab74c-7225-30cc-bafe-791fc089bd45 | -18.61599 | -46.92983 | 2024-10-26 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 070d80d8-eb35-3fdc-b757-998d63153c8c | -18.61523 | -46.93385 | 2024-10-26 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fe4d504-aca4-33be-80dd-a939f0da6e23 | -13.09413 | -47.14376 | 2024-10-26 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 713d3109-32bd-3468-b8ba-a946a9960820 | -11.9601 | -48.73475 | 2024-10-26 03:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c7a1ba-b2a5-3883-855f-b5887281b9d7 | -11.60588 | -48.60075 | 2024-10-26 03:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c172c5c3-48f9-3691-a21a-63ae6e9354bc | -11.60527 | -48.60405 | 2024-10-26 03:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e213658-aa11-3fae-b2fa-b69834de4487 | -13.29242 | -49.57968 | 2024-10-26 03:57:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48cfd2b3-00e1-3c17-857b-dab983605d9b | -12.72236 | -48.53128 | 2024-10-26 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 080ae052-bad7-36ce-9635-718169f5fc40 | -12.7193 | -48.53149 | 2024-10-26 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4b63aa9-e08c-3826-a1d0-8894f2806a95 | -12.59928 | -48.76974 | 2024-10-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d325250a-b798-3630-a1c9-900a58422e70 | -12.59865 | -48.77297 | 2024-10-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 295db112-c074-3bea-ad4b-0b6916ce592d | -12.59803 | -48.7762 | 2024-10-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 999627e9-31a2-3655-b8e6-bddcc51a6780 | -12.5941 | -48.76867 | 2024-10-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b3750620-4b01-37c8-b774-3f3953bb40c4 | -12.59348 | -48.77188 | 2024-10-26 03:57:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8e3add52-d0b2-36e3-b6a6-429196c1c3bb | -15.76738 | -49.24977 | 2024-10-26 03:57:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9369874f-6881-3b44-8931-f4618014a416 | -17.0555 | -53.45337 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbfd376a-fb7d-3a0f-862c-71e98f4abc91 | -17.05423 | -53.45901 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf4318a8-21f1-31ad-910b-f3acdf9797a1 | -17.05295 | -53.46467 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87808f91-fe23-3a55-a84c-e86795ae788f | -17.05037 | -53.44648 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7465e38-da56-334f-a571-f3b01f39d9f5 | -17.04915 | -53.4519 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13956223-abe4-3101-9eae-96a7286d361e | -17.0479 | -53.45743 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 399e5812-28d1-3692-b60b-78a296d9d2c6 | -17.04664 | -53.46303 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7fe2216e-8fba-374c-8e35-cbe94e77c61e | -17.04535 | -53.46875 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 90c907fb-fcd5-3bc7-b404-8d70b23a9940 | -17.04516 | -53.43996 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4187fb6-eebb-37de-bbcc-63a686912bb6 | -17.04395 | -53.4453 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56a49181-1cde-369b-a9ed-fafa6a9539cb | -17.04023 | -53.46178 | 2024-10-26 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 74f48ab4-b725-3b85-80a0-7a8db4e909c2 | -20.72835 | -40.60139 | 2024-10-26 04:00:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 73873f19-846a-34d4-ad14-4ede9c167bc7 | -22.78868 | -41.98926 | 2024-10-26 04:00:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3cf20f0c-2033-3a8c-8605-552d271a3bbf | -20.85396 | -42.89029 | 2024-10-26 04:00:00 | NOAA-21 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b9d901d4-9893-3552-b699-fc4ea05be9dd | -20.41672 | -43.55087 | 2024-10-26 04:00:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 941cd7dd-2259-3764-8185-eb5fa4664132 | -20.41606 | -43.5548 | 2024-10-26 04:00:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b311653d-ab22-3e4a-95e7-d0a57fed9503 | -21.62713 | -43.46753 | 2024-10-26 04:00:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 516a1827-b70c-36ab-ae70-4ced3e2a1a76 | -21.15649 | -42.97688 | 2024-10-26 04:00:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| abc12edc-87dc-304e-8a01-9653ec2ad4af | -22.9183 | -42.71884 | 2024-10-26 04:00:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44c4e360-a4e7-3ea0-bdfb-058e78012113 | -22.91512 | -42.71881 | 2024-10-26 04:00:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0488ef6-421f-3e3f-8d36-6dc8191adba5 | -22.92117 | -45.41461 | 2024-10-26 04:00:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6ef4bdde-6c80-3363-b140-cc7ec1068a08 | -19.76605 | -45.65426 | 2024-10-26 04:00:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7866eec-77ba-3af1-985e-742660665766 | -23.33996 | -46.7735 | 2024-10-26 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 488d57e6-dfeb-326d-a55a-35432825269d | -20.76422 | -46.76822 | 2024-10-26 04:00:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eb36c0e1-108d-3648-ab07-28fb7744d516 | -22.54097 | -48.81441 | 2024-10-26 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3f336c4-2429-30b8-a52d-f583d56138d7 | -24.88964 | -49.55135 | 2024-10-26 04:00:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f3f42f43-23e4-323e-b5af-f76f87759e3c | -29.81536 | -51.17589 | 2024-10-26 04:02:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| ae62270c-1abf-33cb-b576-43fbce960662 | -29.19313 | -51.96372 | 2024-10-26 04:02:00 | NOAA-21 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 038738ea-536a-350f-85c4-cc92b9e11294 | -2.9501 | -52.5708 | 2024-10-26 04:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e0b04ac9-9b7a-36a8-9400-0aa0f1b7934b | -2.9944 | -50.5025 | 2024-10-26 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ceae5f9d-fbf6-3ecd-a376-10ee61230640 | -2.9945 | -50.4816 | 2024-10-26 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d96a7fa5-0c46-3051-bf59-75c2dd5348ed | -3.013 | -50.481 | 2024-10-26 04:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 552764fd-a8b1-3cfc-9ac7-d8080d03d752 | -3.4729 | -43.3377 | 2024-10-26 04:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 997a2c2b-c2de-3e44-8d2c-f3d540ca1889 | -3.473 | -43.3144 | 2024-10-26 04:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 49f578e0-6d4e-3a5d-8c98-61179140e1ea | -3.4915 | -43.3368 | 2024-10-26 04:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f3a82538-a2f3-3456-8650-d5cf8a94734c | -3.4917 | -43.3136 | 2024-10-26 04:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4a0e9449-e534-3f32-b5e3-5d2027c12806 | -3.582 | -51.2137 | 2024-10-26 04:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e56d4bf1-0d6c-3d0d-a2eb-39eeb5e4e43c | -3.6084 | -45.8147 | 2024-10-26 04:05:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6615a477-609e-373a-bda3-216832f6b13c | -4.5613 | -48.0358 | 2024-10-26 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| aaf5ab78-5930-394d-b853-51f5fa1cd28d | -4.5614 | -48.0141 | 2024-10-26 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 81f8b7f1-9f43-3f86-98cf-cff41449331c | -4.5799 | -48.0349 | 2024-10-26 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| c5f7cdfd-09d7-3198-80bd-07e1584d5486 | -4.58 | -48.0132 | 2024-10-26 04:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 81d4ee30-338c-34cf-a412-d7f1d81a5209 | -6.8534 | -45.8794 | 2024-10-26 04:05:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 3e762b2c-afbd-3046-88f8-036e9fb81764 | -7.6474 | -63.4584 | 2024-10-26 04:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 48948487-ba5a-3cd0-a4fd-0792c5418466 | -8.5095 | -45.6354 | 2024-10-26 04:05:53 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7aef5f3a-9d19-33db-87ab-c7ade9b95c0b | -8.5283 | -45.6334 | 2024-10-26 04:05:53 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4d528825-d6f8-3cf3-a7ec-5031b0080862 | -17.254 | -57.4903 | 2024-10-26 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 2c323758-08e3-3a7c-809d-838326cb875d | -17.6667 | -57.4822 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 9506bea9-11b9-36ff-ac07-963612e0e641 | -17.6865 | -57.4798 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 987009f3-1211-3dcf-920a-5a8ffe439322 | -17.7443 | -57.555 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| fab37b3a-b909-3ebe-98de-0295d52b28bf | -17.7446 | -57.5344 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| a7f63066-4984-38c1-82ea-2fbc2d804206 | -17.745 | -57.5138 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 091fb680-9acf-375c-a71b-3acb95ca8a08 | -17.7644 | -57.532 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 2080a83d-7abc-344e-bcba-b68654fff3fb | -17.7647 | -57.5115 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 8ee9d292-8fbe-3cdf-bedb-f236d6deafc0 | -17.7674 | -57.3467 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| b3004014-5f27-372c-966d-dab2ae4f910f | -17.7868 | -57.3649 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 79785239-92d3-37e1-a262-ce8e0a2cc696 | -17.7872 | -57.3443 | 2024-10-26 04:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 963d3180-af19-3102-b8b7-45a8b9571be9 | -17.843 | -57.5431 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| baa0186f-3df9-3a5c-87d2-8ba029986681 | -17.8628 | -57.5407 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 2b3ec170-cc2a-3b05-bd3a-bc24804d314d | -17.8631 | -57.5201 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.8 |
| fcba38f5-7a95-32b5-be56-234790fdb5f5 | -17.8828 | -57.5177 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.3 |
| 7056656b-3fd4-3041-9dbd-3e7654b0f1a5 | -17.9415 | -57.5516 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| c33de254-be90-3f54-8171-778a96e30ce3 | -17.9418 | -57.531 | 2024-10-26 04:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 9bec0b43-0870-3d88-8463-9e02f9c71068 | -18.0629 | -57.3721 | 2024-10-26 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 8871d1db-bfed-3871-be51-a0974bf4b961 | -18.0827 | -57.3696 | 2024-10-26 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 7a1a7009-d3fa-3445-ae38-9c65952e6fc1 | -18.2649 | -55.9975 | 2024-10-26 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| ea982f68-bb5b-379e-a522-13b974730449 | -2.3709 | -66.4527 | 2024-10-26 04:15:19 | GOES-16 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| eac67802-b928-3c7f-a4b2-e840e5af8bd0 | -2.9317 | -52.5713 | 2024-10-26 04:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f0afb970-9adf-3b18-8b8a-826d9876ec37 | -2.9501 | -52.5708 | 2024-10-26 04:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| a13d8f51-7ee4-3abc-bb5d-f168da5ccff5 | -2.9945 | -50.4816 | 2024-10-26 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 19d1da82-8d43-3f77-8482-fc5cab70a74e | -3.0129 | -50.502 | 2024-10-26 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b89660dd-5a23-3ed1-84fa-d8c9267bd15b | -3.013 | -50.481 | 2024-10-26 04:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 13b86b43-225c-3e0a-8956-47ed898ee3ec | -3.4729 | -43.3377 | 2024-10-26 04:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| c5ff9fe7-01a9-3f29-9d78-d8437380bd08 | -3.473 | -43.3144 | 2024-10-26 04:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 3cc7c54e-bdc3-399d-87e0-66cca926f479 | -3.6084 | -45.8147 | 2024-10-26 04:15:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ee26f32e-efa2-30b5-8620-3955994b41ff | -4.5613 | -48.0358 | 2024-10-26 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a1d9475e-549b-3b7f-872a-a7495b53f122 | -4.5614 | -48.0141 | 2024-10-26 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| dba4e2d3-7b0c-341f-b82c-5a320afee9d8 | -4.5799 | -48.0349 | 2024-10-26 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 157959aa-4c27-370e-92fb-e46c1625c05c | -4.58 | -48.0132 | 2024-10-26 04:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| a9631500-d91f-3d89-8d17-7122f1d6e710 | -6.8534 | -45.8794 | 2024-10-26 04:15:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 025eac89-6d7a-3d8d-96bc-03c4ae0d3102 | -7.6474 | -63.4584 | 2024-10-26 04:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0574c49c-ca89-3751-9d9b-56884347074d | -17.0499 | -53.452 | 2024-10-26 04:16:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| efebd0e1-456f-34be-bdef-740dd3554cdb | -17.254 | -57.4903 | 2024-10-26 04:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| f84a35ef-9443-37c4-bf7e-4e92559c002e | -17.6667 | -57.4822 | 2024-10-26 04:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 020fa43f-14a4-3d03-bfab-2a2535b155eb | -17.6865 | -57.4798 | 2024-10-26 04:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |


[Clique aqui para ver as próximas entradas](README37.md)
