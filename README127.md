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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe3fc16-2ac1-3035-9c1d-52c59705dc81 | -5.66792 | -40.71637 | 2026-08-31 16:33:00 | NPP-375 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0b5a5154-2738-3792-93c5-05bdcfc378f0 | -7.51936 | -44.4526 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45615896-2c16-362e-996e-65fb5f4f08de | -7.6108 | -55.28751 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cbabf052-ca0c-3224-b0d2-4746a635dac2 | -8.13882 | -45.52313 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff0ccc79-4427-3c37-9f7f-03f44e5d3499 | -7.92745 | -45.00716 | 2026-08-31 16:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 457ecade-2c3b-3833-8e68-6cad1c52edea | -5.62655 | -45.5684 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 915ebb38-ac18-3cd9-b427-19973d84ef54 | -4.08705 | -45.94063 | 2026-08-31 16:33:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a116c55d-b2d2-3a44-8e4f-fe5da910477b | -6.87271 | -41.70457 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 744fc964-676c-3769-8bbc-a864bd938424 | -5.68526 | -42.73463 | 2026-08-31 16:33:00 | NPP-375 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a2c6f51a-f53b-37ca-a94e-bd961d07173c | -6.8386 | -41.72792 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| a84cac8c-ad1b-3c2c-a2bb-125f1b8ab62d | -3.29041 | -39.24895 | 2026-08-31 16:33:00 | NPP-375 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a94683d1-d4de-3c93-be77-57ac02dcab75 | -8.943 | -50.76171 | 2026-08-31 16:33:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fdc39d71-e203-36f8-88a0-4380df8848ae | -6.85839 | -41.65624 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 72bcae22-13be-3d5d-8b9d-06e4185233be | -7.98623 | -44.33262 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6e8c2f9c-cebd-3961-bff7-f99b23b7b133 | -5.87039 | -52.09307 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 990d14b7-953d-3382-8ff4-1d9b8b231158 | -3.82482 | -44.92862 | 2026-08-31 16:33:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55e98134-e3a6-3c5e-8a1a-cbe5e3f278bb | -5.80642 | -43.64272 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5d18151f-1e62-3cf7-aae7-531c3434b954 | -6.15268 | -52.63689 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 23ebd041-836e-33ff-9836-cf8222242def | -6.06666 | -53.83425 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15fb1dc3-73bb-3918-b957-6478825bb052 | -1.77809 | -53.5014 | 2026-08-31 16:33:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d61d34a9-5c48-3365-af9c-9277cc92f2c0 | -4.9568 | -43.09828 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0b57603-fd72-33b4-b64e-b4447cf2cf04 | -6.2068 | -53.58372 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d72338ad-2771-35af-9548-96d6098313e7 | -7.0063 | -45.45889 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12269e2a-9c0d-3198-86c8-c271ddd5d976 | -7.91408 | -44.24039 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f2cbc80d-aa62-3837-83ae-fb72b4b535f6 | -5.54354 | -46.60278 | 2026-08-31 16:33:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 67116aa7-2a46-3c92-97fb-dcbcbe1b668a | -6.44234 | -41.53355 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6e1e9f67-134c-3696-914b-eb45c2385fb8 | -7.63481 | -46.73466 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e02433c6-d851-3030-b406-2e48e60b4208 | -3.65131 | -54.85259 | 2026-08-31 16:33:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 30aa8bdc-0014-3404-840c-26baa955bdcd | -1.62463 | -48.21159 | 2026-08-31 16:33:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7034290a-565f-3b82-8cb2-3fd01841caad | -7.10578 | -42.76503 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f15699a8-9812-39ee-88eb-68fd1dd9d69e | -7.98934 | -44.28231 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 989efcce-ce11-3d5e-bcdf-4c6eb4fb6290 | -3.58318 | -44.96885 | 2026-08-31 16:33:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 884508e5-a827-3ba7-be50-9827b3307266 | -6.25893 | -53.64941 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c3d8eb93-6952-35c3-8882-5541917ba01b | -7.62834 | -44.92842 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1fe6bde1-0900-3585-9ae5-33891822e35c | -7.09986 | -45.79023 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 2c6ee628-bac3-3456-8f93-c3ca220ff1f2 | -8.32919 | -45.7288 | 2026-08-31 16:33:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65523bd5-dbd0-38bb-b035-6db4990bd259 | -1.87096 | -50.65131 | 2026-08-31 16:33:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 98c2144a-04c5-3e1f-b916-0036d6e7ea70 | -7.10418 | -42.75458 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7b5d8625-e3e2-3be6-8f45-e930f187222e | -4.30868 | -49.09737 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| faef3b2f-10a9-3d33-a312-f8ab2dbc110e | -8.04976 | -47.27874 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6a724dbb-b9be-3b3b-8f80-b7c298f86a97 | -4.91102 | -43.46104 | 2026-08-31 16:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0c64797-99c4-3644-8df8-4226e9f5c643 | -5.83717 | -43.86928 | 2026-08-31 16:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23360351-b2c4-362b-ab8b-9f16fcb830a7 | -4.09627 | -38.28665 | 2026-08-31 16:33:00 | NPP-375 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 08f7b683-d8f4-3d7f-98b3-16292ca4829e | -7.02535 | -56.54233 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 45f0ca95-b49d-333d-a860-fb8542d827bd | -3.83428 | -55.56445 | 2026-08-31 16:33:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8db229f9-8245-3aa3-9245-64a4e60507ad | -6.68274 | -38.49868 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 67bbb826-51e1-3509-bfd1-1a6e05c3270b | -4.25066 | -40.75763 | 2026-08-31 16:33:00 | NPP-375 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 313ef132-2aa5-310e-9e0f-7b8113986952 | -8.53937 | -51.57888 | 2026-08-31 16:33:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9fea011d-3d00-31ce-8e98-ba63980bf54d | -6.34746 | -35.24918 | 2026-08-31 16:33:00 | NPP-375 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 37.9 |
| e6f7e1b0-3b4c-3c40-b30b-a477f77c19bc | -6.69848 | -44.03303 | 2026-08-31 16:33:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0e4bc9bf-9493-38fe-8e04-ca0759164774 | -6.80141 | -43.56385 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cde01a2c-968b-33e2-b00f-0e9a26d159a5 | -6.91854 | -55.73234 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f7800d3f-ca77-3ee7-bfea-a7cc23ed2abc | -4.63979 | -43.49997 | 2026-08-31 16:33:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01179599-08b9-38c9-a36f-34c8e25f15ae | -7.11031 | -42.75008 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d215c185-e0e2-36ff-a1ca-d4a6078837db | -3.60048 | -48.99429 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6be16b5a-df80-3a7a-af6f-7b2743093fbd | -7.91464 | -44.24412 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| acc54ca4-0557-3e48-97ae-8b595175449c | -6.93978 | -55.63165 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 47b9529c-e408-313d-af41-17a395ca1c3e | -7.02541 | -55.64164 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 480cf068-d732-3d82-9015-2e8a98b28001 | -3.41768 | -43.37673 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3669edb4-a351-3db2-95b5-f0c02f29e154 | -7.60848 | -55.28331 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6428fec4-6ce3-33f2-8e2d-a17e86f8bbc6 | -5.98127 | -51.92472 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c630ded9-e604-3071-82c4-f04a318ac3b9 | -2.56286 | -47.1981 | 2026-08-31 16:33:00 | NPP-375 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ca135b7b-7dbb-3802-ace6-fb40b045a1ec | -7.60921 | -44.84702 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38fdc05b-a057-33e7-87c0-20153daa9b55 | -4.73702 | -56.27201 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c9fc3d6a-f7c3-36ee-b12c-a0bb9c1cdf45 | -6.4081 | -49.93331 | 2026-08-31 16:33:00 | NPP-375 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c350e0a-c99c-3058-9ea6-8f69962c1451 | -7.94081 | -44.2398 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f70e18a0-f297-32ca-8069-4ab9e0b18b73 | -3.1886 | -42.54454 | 2026-08-31 16:33:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40c69d23-1371-34b9-a6b1-7d4753f7ad69 | -5.87964 | -52.15956 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 001255bc-a201-342f-8c3d-f719ec6f5735 | -6.78569 | -45.21523 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3c4ffa48-3a26-3c68-b351-0deba76b7f13 | -8.13584 | -45.58013 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 06046631-311e-3db3-9855-18ee82aa27db | -4.84917 | -55.82877 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 099cd200-1205-39ff-8802-f1bbf9ba3381 | -5.86351 | -52.08334 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9932f67e-5600-30ca-a2bd-bc144d931b03 | -2.55032 | -54.66475 | 2026-08-31 16:33:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e16e55c-09eb-3308-adb9-5ce29f28455b | -7.26627 | -45.35192 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| a8290a4e-fb60-34a2-8e24-ac48d4a4b70a | -5.62715 | -45.57239 | 2026-08-31 16:33:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18050fbe-2582-322c-aace-f6e409cb0bdc | -6.85893 | -41.65975 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 80c42010-b2e0-3d42-b645-fda8c95fc75e | -3.28657 | -39.24952 | 2026-08-31 16:33:00 | NPP-375 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7dd0a476-8ef5-3448-a4d2-a5cf37177c8a | -5.89669 | -52.242 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 26519241-98fa-3242-8d8e-47d38dde9648 | -6.26602 | -53.65019 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| de3274ec-a25b-3531-904d-fd8e69d55b95 | -5.58613 | -42.3335 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 38fcbb21-97f7-30c4-bb4a-79075b41c9e2 | -6.91524 | -55.70734 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0ee7fe35-d598-3461-a9c0-da4d3a59d85d | -6.30115 | -44.61861 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 21e9ffc8-849b-36fc-92c4-e3742ab148a3 | -6.87413 | -43.71604 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0bd7be37-b985-35c4-a08e-9f4e8fbec905 | -2.84711 | -43.46646 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d33747-6976-3745-9538-4852ba087e31 | -7.94591 | -44.25057 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| acbd8969-ec37-3887-b525-d569ecf8e808 | -5.4505 | -42.6579 | 2026-08-31 16:33:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d8541333-924b-302d-9620-3cf14c64b84c | -6.98582 | -45.39514 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 95a9f71d-09c9-378b-90e0-5dbb76f9ae0b | -1.94174 | -50.65044 | 2026-08-31 16:33:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 70544f67-9b8f-3639-8d81-7ed8e0f13769 | -7.98635 | -46.51918 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dfc3b785-1081-3536-846c-e552660280f5 | -6.91711 | -55.73013 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6634cc6d-9d08-394d-9980-879d55c45e7e | -5.38965 | -47.71392 | 2026-08-31 16:33:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1f700449-8266-3626-9dd2-5ab42f6d2dc9 | -7.16825 | -44.68719 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40cc5cb8-f23a-353e-8d99-0c061d15c5ea | -2.80044 | -49.58193 | 2026-08-31 16:33:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ba4b4bfd-d7ff-3259-9b78-f004bd7808c3 | -7.99678 | -44.285 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.0 |
| c6e431a0-7be9-3161-826a-62d7fa97172c | -7.09864 | -45.78185 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7074f10a-b934-39c6-842c-fbbf17450fbb | -7.98319 | -46.52449 | 2026-08-31 16:33:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b4761eee-4456-36f0-a127-aa39e8e17141 | -7.37214 | -45.06607 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8907ef60-8658-3dce-a7a9-61d00e3a5dd8 | -6.25604 | -53.67276 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c2152225-5ad8-346f-a197-42d5826f074c | -1.72516 | -48.29237 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| ef419729-816e-3347-9b00-9617084c53e4 | -6.49913 | -41.85445 | 2026-08-31 16:33:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README128.md)
