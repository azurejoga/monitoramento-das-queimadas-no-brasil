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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b8773d2-7eb5-374c-aa24-5f913135675a | -5.80841 | -44.83969 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fed847fd-737f-3279-b611-1a407baedea7 | -9.0636 | -45.77327 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 557e04bb-c47a-36f0-9571-df50dbdcdf70 | -8.06844 | -48.66735 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbd858c-4db1-3cd1-afa2-4ff994cf9cae | -5.48464 | -42.65448 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfbfabd6-5a75-3d04-890c-dd0b4d964964 | -7.24207 | -44.46442 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebc2981d-ff7c-3ff1-a2bd-5892825ae6d1 | -4.95568 | -48.40572 | 2025-09-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd7adb6-0d55-329f-bc2f-101c4b3738bd | -7.61057 | -44.65023 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f45f1ee-f46d-30f4-bf15-97803f722251 | -9.45158 | -46.70678 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4dec714-0090-3eca-adb4-1f6edc0c6a41 | -9.69352 | -46.86935 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546da602-c119-3d3d-9ddb-40f318e86e53 | -6.17835 | -41.05503 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6441e46-5ec2-3a8c-8f77-99123f72dda3 | -6.31076 | -43.57257 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47e134c5-20b8-3d53-bbe6-9605e292d262 | -6.27181 | -43.38976 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6d9ba40-545e-3a35-ace9-80d6d246d4e4 | -6.25089 | -43.41059 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 222e4440-46d5-3a0e-810e-89fbfce4243f | -9.13855 | -45.5687 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5782f1a8-070f-3fc7-90e0-17b2774111d4 | -4.46938 | -48.11261 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d0520db-2ae1-3866-915f-25ded4c1b038 | -8.05067 | -48.67474 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcd492f0-e78f-35af-a300-3749dab1703b | -6.18616 | -41.04773 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40d99b12-83a1-3c37-841e-8f583e4e55ef | -5.70988 | -45.41829 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af080994-69af-3055-96d1-f213973fa39d | -6.17823 | -43.37805 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb2f8b07-5111-3aad-8a29-fa50c04f26ba | -5.21108 | -43.70654 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50537192-5c98-3e90-ae33-6e54dc95d0fa | -6.84957 | -44.8995 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8d2d953-2859-31d8-97e3-2feb560510ef | -5.40641 | -43.43956 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b444164-8bad-3f1d-b4e2-bc6ab8106455 | -5.67703 | -45.46822 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edbee6dc-aa60-3eac-b179-8ecb22649288 | -9.44251 | -46.71773 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82d04c95-e8f6-329a-9b39-e29ccbe2b23f | -5.75003 | -47.47075 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| debc6f72-108e-3b6c-b080-3ff577aa6464 | -5.71755 | -45.40707 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4d7b40a-5d1e-3809-8a32-a7828b3b96f7 | -6.69001 | -46.41037 | 2025-09-10 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c68f5ef7-b8c0-3807-a489-5410b2131834 | -6.15691 | -42.59703 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23e1943c-9652-370f-b7f4-06431a28ddd6 | -6.05433 | -43.32328 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9f80653-d0ca-3ad1-8c0d-a7e833449e21 | -9.06366 | -46.9843 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 78b42006-de4d-3863-8efa-aa1862653c59 | -5.1694 | -42.95395 | 2025-09-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b1d8704-24e8-36b5-afc2-5499efbab8ef | -4.86783 | -42.77245 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d37af1f5-0493-36ad-a8ef-a411404d5012 | -5.64322 | -43.922 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc1b8d55-19a4-389c-9435-11ea8368d974 | -6.48461 | -41.75542 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0370040e-c6c8-346e-b5a5-53037b697ba2 | -7.59374 | -49.28762 | 2025-09-10 04:14:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c071dd2-fbe4-3f02-9bf6-fa6efab00d5b | -8.04165 | -43.82011 | 2025-09-10 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 430709eb-8757-3432-b1ce-3b851a0c2b99 | -5.16703 | -42.75273 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ea8153-6de3-35b3-95a9-bd6a883a390b | -5.67632 | -43.34457 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3ca994-c376-3abd-91f1-5b234c766ece | -5.35263 | -42.62978 | 2025-09-10 04:14:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7538fea1-5caf-36b5-b172-e894e73e834d | -9.81061 | -47.76827 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 476a0b6f-5c88-3363-90fa-fa01ee825110 | -5.6668 | -44.91493 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea1d633-1e69-3d50-b4fc-5e819d6cb18d | -5.72263 | -45.4196 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10f500cf-16b2-36a9-bc8d-314e5355ad60 | -10.44389 | -43.33065 | 2025-09-10 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d83a26fc-b7da-3fe4-8dfc-aa9ae9328e4e | -7.99281 | -46.32494 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a3d26f9-8293-304f-a2b5-88bf6a5f25b9 | -5.55833 | -45.17635 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c776391-f52e-30c8-94a9-2f0304068fcb | -5.88018 | -52.15986 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6532aacf-9872-3c9c-adff-29d83a540f79 | -9.69443 | -46.81945 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 456cc8a6-27f9-3d23-bc31-607ea04233fa | -9.34956 | -46.75215 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2ed36e2a-34b1-393b-b5e0-2650988c8c73 | -6.35485 | -44.07056 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e50e94c-3c71-3375-a230-c3957706dac1 | -4.09868 | -41.57188 | 2025-09-10 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e077376-7492-3ee7-a326-ed58092d22ba | -5.02864 | -43.13625 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9aaf56b-463d-3ded-9dbb-c6c386c4c9e3 | -6.26142 | -43.41286 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f5254e97-7ebc-384b-85bd-b8536d952c95 | -8.495 | -45.6593 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 293db53e-74a0-37b5-a6eb-7634948456fc | -6.1634 | -43.38634 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3c3a7fd-7222-3edc-ab0b-d62737edbd80 | -9.08471 | -45.7079 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1c07532-6a0a-3b15-a09b-8801edac200e | -8.85594 | -47.23549 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a461038c-fac6-3021-a5c4-3645b8e7038a | -8.52303 | -51.38089 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38282708-3f37-3585-827e-d02670e91af7 | -6.62402 | -48.07878 | 2025-09-10 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28528738-3705-39f4-8d6d-5d64f45778ea | -6.65996 | -44.54952 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ff15662-6b12-312d-bb38-2b87e2527eb7 | -6.6492 | -44.08185 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5672178c-299d-3d33-b5cf-79ea3fe363ab | -5.67826 | -45.46052 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e716b78-b0bd-3688-989c-c11a6847a09d | -5.531 | -46.49613 | 2025-09-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 650b1790-b4a3-3362-8cf3-23e39b9baffd | -7.85136 | -46.03333 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83f6a1aa-bc3a-31cb-9d8e-8aff44015260 | -5.42251 | -45.87904 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0549e85d-daa1-31bc-a552-9cdd6dfd2c55 | -6.40786 | -44.44712 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af92d6ec-b506-327f-ae16-2d2ce40643dc | -6.67909 | -44.10799 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b6674e9-af20-3ca6-9f0e-5358c8e14800 | -9.88802 | -46.47638 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba6a57c-37e4-3e44-a7ee-4f2728bd2893 | -9.15096 | -46.0577 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4a1e5e1-2668-3aba-9b55-26ebcba9737a | -6.24159 | -43.4268 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8ca14cc-8331-3c34-8cb7-8ec7ef34b284 | -8.38795 | -47.99116 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 678fafdd-1d93-3bcf-bfca-7dea0947296a | -9.03432 | -49.78471 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80a655ce-68aa-3b5c-bd0e-40f48cc7c2d4 | -7.8901 | -46.26465 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8f3de33-726a-3b96-92e8-5767d4b68959 | -3.37424 | -52.79488 | 2025-09-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77f00990-1271-34a9-ad93-9e494877e659 | -5.80088 | -45.67357 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54211639-7b2b-3f25-bd77-e110471c9e96 | -8.98799 | -46.06285 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d87b02d-334e-3cd7-a5a2-9540553f2333 | -8.98735 | -46.06673 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57e5a306-fa69-37df-ba60-c4525a487561 | -8.67382 | -45.74927 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cd0bf8d-8127-3cde-ba4b-40b0c107eacb | -5.22598 | -43.69816 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c4f184c-cbd9-3f29-94d6-18a5e3af2554 | -9.07272 | -50.4685 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81c3b13f-d243-3913-987e-7d3581e8d6d6 | -6.2277 | -46.24427 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0267e885-f2d7-37a2-94c6-c151c051398f | -5.96728 | -45.80838 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a89b4c4-bdf5-307d-b5ef-07c8a7b8855e | -7.77706 | -46.12954 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 305ffb8e-c06f-3ca1-ad3f-ec9e577b9347 | -5.51509 | -42.68038 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c6165c2-964c-33f9-a312-0dea2a9dd365 | -6.41857 | -44.48207 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bc3f245-77c9-3cd4-bff2-78672a2b91c3 | -5.74976 | -45.25255 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b662ccf8-5a1c-328b-adc8-c7f64b4e4caf | -5.67854 | -43.35198 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9f96db1-48c9-31d3-84ee-a5a67a273183 | -6.3543 | -44.07406 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 150ab866-e590-393b-b74d-99b9b6805230 | -9.05848 | -49.82212 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f511d03c-f231-31f7-bd1a-61be407028c8 | -4.48577 | -48.11521 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5de46795-2885-3fa4-b474-d9d537295963 | -5.41904 | -45.87949 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e83464-dbe0-33cc-8146-6710ef5bb20a | -5.71864 | -45.40788 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b654bc1f-278d-35b5-ac55-1dafb2649466 | -6.18819 | -43.40079 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5516824f-6239-3db4-bd11-1e45ed6d6217 | -6.52542 | -44.8405 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 648f2dae-37b6-39ea-a4bb-c0cdd8b8248c | -5.77992 | -42.44204 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e9b7204-151b-392c-86b1-4d8227548160 | -5.75538 | -40.95444 | 2025-09-10 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0e8fa2bc-2e6a-3abb-83d7-498cbcf4a982 | -9.04814 | -50.47789 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f15e561-02d8-3088-81e6-ce10598491e1 | -6.70027 | -43.54252 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d917b53-77ac-3d1a-9b9d-49bec2f3f900 | -6.29246 | -42.20669 | 2025-09-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a868367-81e9-3430-a5f9-31af5b08256c | -6.26131 | -44.05943 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca47f6af-0dc7-397a-9015-e043bd1e14c2 | -8.49442 | -45.66292 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README28.md)
