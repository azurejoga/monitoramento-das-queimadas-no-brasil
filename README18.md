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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 397f2855-540c-326f-b8e3-d9c4799c9dd5 | -10.45079 | -45.06123 | 2024-12-13 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aeacfd1-a1a5-36b9-b4e1-83384698cd2b | -5.95219 | -39.67865 | 2024-12-13 04:21:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3fa0648-6e84-3540-bfab-2bb386aac144 | -4.73377 | -46.80376 | 2024-12-13 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b782591-cbe3-3da1-8f10-c66eccda3474 | -5.44903 | -44.8246 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ec3430e-8928-3ed2-96ba-7b8075df5717 | -2.5003 | -51.79499 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e72fc48d-068c-36b4-b100-c12fab22ba81 | -2.18865 | -53.65495 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2907e218-e4df-3c39-a690-8f74178fd2c3 | -6.09791 | -44.76351 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5f9c710-5551-3b23-9458-bcd585b995b6 | -3.272 | -45.49306 | 2024-12-13 04:21:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0717e7-52a4-3715-b2b0-bf5f92478722 | -5.94669 | -43.76598 | 2024-12-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9092908e-b06b-31ac-9682-65aad00d93cf | -5.6259 | -44.8381 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32bf5b13-3233-39f5-bf62-7c2ca1aa61de | -4.769 | -44.41553 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 659323c1-4635-36ec-9c36-678c96b9781a | -6.76095 | -44.8294 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf127d42-5dc5-3341-a555-3c01e228a89d | -4.16416 | -42.4397 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 328d20af-6553-31eb-9258-46d851efb588 | -5.21201 | -43.29084 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64b9604a-7a82-3520-8352-21a7ae32bc9d | -8.165 | -43.82357 | 2024-12-13 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70e768dd-916c-3d42-9d47-d5f5cbc67d70 | -10.02489 | -36.28708 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 8c5b2273-606b-34a9-aaf2-e5a999a4f441 | -5.45114 | -36.87097 | 2024-12-13 04:21:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e9fdb489-53b2-3462-9d00-a5be4dc277bd | -4.72234 | -37.3593 | 2024-12-13 04:21:00 | NPP-375D | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf4c3fdc-82be-36b1-926a-c54a2c268fa6 | -7.97114 | -48.16198 | 2024-12-13 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0e1628c-1e7d-3c48-983e-603a5d9fdcd5 | -8.16556 | -43.81994 | 2024-12-13 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 543c592e-d718-3a37-87a2-90ada429ee9e | -9.16911 | -49.47981 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7509a2a4-b614-31db-b789-56224c9048fb | -2.91733 | -48.02718 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 781d2b7b-b462-32f2-bcdc-5e7035ef96f6 | -2.50524 | -51.79583 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ad38d72-1fa2-35c9-b7fc-cdca548d89d7 | -7.99471 | -39.43461 | 2024-12-13 04:21:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ee42e28c-e657-3aa4-845a-92a5fb215c70 | -3.80127 | -51.09446 | 2024-12-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2d8439-dbe1-34b2-8bef-8443d57931a5 | -8.95388 | -51.3715 | 2024-12-13 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6083724-ead2-3c19-8b2b-f8e5a657d911 | -4.65369 | -43.81585 | 2024-12-13 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 261d08c7-7efa-30b4-b60f-d0513504f907 | -9.14006 | -49.4893 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27905121-69d4-3a8d-bc5a-545358f670a1 | -9.46918 | -37.06589 | 2024-12-13 04:21:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 99e0f225-ced5-3261-bf19-f3ef6b12a095 | -4.54932 | -43.57496 | 2024-12-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43cf5a84-f937-34fe-96cd-ca58fee988f6 | -2.52096 | -51.79267 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d530507-d86f-383d-bbb6-9d61d4643b5c | -3.66992 | -45.22905 | 2024-12-13 04:21:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adacbe60-5eb0-3a4f-be5c-0cf7e666dc07 | -5.21818 | -43.29548 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d5657240-0038-3ffa-8ba2-4de106e92a30 | -2.23237 | -53.72364 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39800b38-7cf0-3adf-894b-465e2dc8382e | -5.96429 | -43.36575 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1fcdbf29-7924-3065-a18a-18a7d547e2b0 | -5.36159 | -46.23249 | 2024-12-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c24187b1-ee1e-3699-9bd5-2a0f2f20fe5a | -4.78564 | -48.50586 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad8cb079-fdf8-3eee-9010-fc554a92f88b | -9.19566 | -49.47703 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dbaf740-7e67-3d50-a925-e4ae94f4f6da | -6.5914 | -44.16112 | 2024-12-13 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 207801fa-9eee-3dc8-bb07-d43151c98a59 | -3.18674 | -45.61316 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70ec01c3-7c7b-3a62-a32f-efc3e012d1f9 | -10.8665 | -44.93832 | 2024-12-13 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5584b9d3-647a-354b-a5f5-260f80b405a1 | -9.1653 | -49.4791 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e1de254-6f67-3f62-acfe-d03da4bf966d | -10.20879 | -47.58366 | 2024-12-13 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98bae5b2-90d7-3c55-bbdb-931670c19b63 | -2.50518 | -51.80282 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f592516a-dbf1-3bac-b0f5-3cbc324127de | -3.2677 | -46.92547 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a389960b-8729-35eb-bbda-a53a0918f741 | -4.55066 | -48.00965 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04eba6ea-2f5d-3ecb-889e-132f7f748396 | -6.08387 | -43.53796 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36196bb4-ac27-3d64-a1d3-db9833f11cf3 | -3.15058 | -49.908 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d391ed3-e740-3472-a87e-d41067af8f0b | -4.26887 | -43.83048 | 2024-12-13 04:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2c91149-92c8-328e-95ea-d74616fae7f9 | -4.24353 | -41.92535 | 2024-12-13 04:21:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1e535fa0-8c1d-3e22-848c-71f4c7831008 | -3.18334 | -45.61263 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a59ed1-ef14-3863-96e8-7f3d743b0b76 | -5.44881 | -45.40017 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22ff3b67-d2df-33d3-a872-153e7621b280 | -8.3673 | -44.58951 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43a2bb20-4570-3fc4-a74d-5250ccc7cfbb | -4.73441 | -46.79982 | 2024-12-13 04:21:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a16596b1-c261-3771-b082-7be02955635b | -4.47778 | -47.98233 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f981f259-8894-3c31-b7ae-5beea01d0858 | -7.42864 | -44.73528 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 514fb7a4-d4f8-35a2-963d-e314fe10bf0e | -5.27896 | -48.79001 | 2024-12-13 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aa29d2c-9eab-38b8-a6ed-1d862db6b435 | -6.56669 | -39.43626 | 2024-12-13 04:21:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89d5d2fc-587f-354a-9e7b-3603b27b5aae | -7.57705 | -47.11672 | 2024-12-13 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26e756dd-325b-38c7-a83c-3a82062f5788 | -8.71579 | -44.00389 | 2024-12-13 04:21:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1752747-2319-379a-ac93-bc72ce8b9d33 | -3.83188 | -41.556 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9618a4b2-20d3-3778-852d-4689a17c87ac | -4.97707 | -44.49105 | 2024-12-13 04:21:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f29a0298-c87f-35d1-846c-fdc47fd769bb | -5.6476 | -43.36155 | 2024-12-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d97e98f-efa9-39b7-b23a-c44c9f57ea3c | -4.7838 | -48.50316 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b1b3581-4249-35a4-b2a7-3292a311ebb6 | -9.07766 | -36.12789 | 2024-12-13 04:21:00 | NPP-375D | SANTANA DO MUNDAÚ | ALAGOAS | Brasil | 2708105 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e94de735-c9dd-328e-a1cf-ed33100ae6a4 | -3.01423 | -48.03315 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e034b551-13a5-3c3e-b455-e9840adc29d0 | -5.23701 | -45.13339 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39323bc2-4666-3019-a98d-0b8b97b17537 | -2.49852 | -51.80608 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e782d79f-5cb7-354f-8fd0-1ee0dc4eef65 | -2.49446 | -51.7997 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d5de223a-19bb-34cd-917c-8a49c43bbb1c | -4.77921 | -48.50734 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e32042cd-3e64-355d-bcd5-863d9093f8a5 | -8.27022 | -48.02617 | 2024-12-13 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dd05b8b-b65d-3a84-86ac-7d642cd7a80a | -7.58112 | -47.11347 | 2024-12-13 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 908de162-2e32-3f18-929d-ee0581caa6c4 | -3.28767 | -45.59191 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 406b0777-4723-317a-b27f-36c9da4d90a2 | -6.76482 | -44.82646 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a2fa35a-33a6-3426-8acd-2272f897804c | -6.7615 | -44.82594 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6433c32-989f-348e-9f9d-4a7f5bbb31a1 | -4.41774 | -42.89861 | 2024-12-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9c34083-85d5-321a-ae75-6890724cd2a7 | -9.19185 | -49.47641 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c239cac7-b89a-3a4a-b528-40d3ef78e8c6 | -2.51513 | -51.79742 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1b3755db-a0b0-3913-b8fc-0fadf3263014 | -10.02076 | -36.27669 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d6022ad5-d96b-3b6e-a84e-0b61613bd118 | -3.00734 | -48.02728 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618d021e-c7a9-3f0a-91f7-a87344139a63 | -3.27539 | -45.4936 | 2024-12-13 04:21:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b5c8d72-57df-33b1-9219-57764888b64c | -9.82639 | -44.17847 | 2024-12-13 04:21:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50530be3-967d-304d-a4b6-9e9ca7441b97 | -5.59313 | -46.53128 | 2024-12-13 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2da62f08-81f0-3798-81bb-2839696ab645 | -6.48385 | -44.35139 | 2024-12-13 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f297abe6-561f-37b9-8bd0-f4a3790accc2 | -3.83009 | -41.56779 | 2024-12-13 04:21:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 62626e96-7749-36df-bbb8-cd9ecee8a0e1 | -5.02228 | -44.37409 | 2024-12-13 04:21:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b499cc03-d771-3b1d-a861-7bcd25abe8c5 | -9.16439 | -49.47636 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f07d4e0-fac8-3895-96e5-a6f46f309804 | -4.64029 | -42.88121 | 2024-12-13 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89bee379-4886-3e17-bc55-0b20926aa2ba | -2.65149 | -51.87349 | 2024-12-13 04:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 26e6a680-97ee-32a0-b853-c765722fc16e | -5.45176 | -44.80727 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd464281-11a6-3b65-a356-3d6ef76d7954 | -5.08306 | -42.56581 | 2024-12-13 04:21:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 69e18068-9480-3e00-8f51-385e8811c8eb | -4.54877 | -43.57845 | 2024-12-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 510ef329-1ac0-36fd-a786-b75629461c83 | -4.44977 | -44.65638 | 2024-12-13 04:21:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02d1eec4-f3f6-370e-abc8-051dfa156fcd | -5.20864 | -43.29032 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18bfd864-cb5c-3e96-9b61-fb7a58a68e9f | -4.78259 | -48.50056 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 944aea9f-50d2-37de-ad5b-01ddab6d2371 | -8.60584 | -40.57127 | 2024-12-13 04:21:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7dc8bf0d-f829-3bb4-a7d3-515e61471506 | -6.56257 | -39.43558 | 2024-12-13 04:21:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33aa5665-83c8-3c12-8260-5ab6e14a7ce2 | -4.24702 | -41.92588 | 2024-12-13 04:21:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3dfdd6bf-abb1-39dd-a55a-f75ae6570742 | -7.14714 | -41.46774 | 2024-12-13 04:21:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7aedb6ea-f06c-3b70-be39-237a9afffc2f | -5.94559 | -43.77301 | 2024-12-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
