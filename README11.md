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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e016697-933c-3927-8a61-2328d717401a | -6.21829 | -43.95288 | 2024-12-13 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e240b7a3-9780-33b6-9da9-df389a79b625 | -3.29217 | -45.59134 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18300683-e4b0-31c6-bcac-2edc5e209ac3 | -7.99453 | -39.43064 | 2024-12-13 03:55:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 50732d42-bd9c-3980-bcc7-b46a930147e3 | -8.60608 | -40.57155 | 2024-12-13 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5944e528-ec24-3c2f-b97b-d3f9c2c811dd | -3.28792 | -45.59412 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7675b87a-34c0-38c7-a83a-ca06b6fb1deb | -3.98715 | -44.56698 | 2024-12-13 03:55:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bab2477f-551b-317b-ae89-a8324330eb07 | -5.20721 | -43.29638 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| efdd2553-aeb4-31f7-b5bf-2b6cbf9a0ee9 | -6.92559 | -43.54547 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24d90a86-3075-3ca1-9782-df32ca8a5072 | -6.91424 | -43.54007 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d37704de-4643-39bb-a528-7f23035dcedc | -3.2213 | -42.0766 | 2024-12-13 03:55:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02f070d6-73ca-3842-81d3-58308e30bb99 | -8.27097 | -48.02525 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0739f877-05c1-35a8-889f-6af9ac4d44a8 | -2.73042 | -47.8853 | 2024-12-13 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c96ef13-4903-3ea1-b9ed-dbe7dd1578ae | -6.08599 | -43.53889 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 889f346e-6815-3a6c-95dc-2fa6894a15f1 | -4.51311 | -42.06281 | 2024-12-13 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6cf5fd70-cead-3d4e-9543-81b9cb8903e2 | -3.14463 | -45.5965 | 2024-12-13 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6eb3550-7e77-385e-9950-83b503987fdc | -8.2657 | -48.02443 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 976a0057-362c-3810-8418-64180d95cbac | -6.91821 | -43.54073 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75d6b93a-c484-35a7-8ed2-8a1457db2955 | -8.65551 | -36.9059 | 2024-12-13 03:55:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0aafe5e0-c310-3eb5-9705-86143b02fe29 | -5.8217 | -35.53325 | 2024-12-13 03:55:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42458507-fbb9-3c97-9bd0-2ccac38cb9f2 | -5.21066 | -43.30049 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4c27b083-1c24-3b04-a275-9057f8257b45 | -3.70072 | -50.9451 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 460bf5a3-d23c-3c4f-8681-117c8b58ba07 | -6.11308 | -43.95831 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fc8c18b-890a-3e0a-931e-38e14c74d7f7 | -6.71671 | -39.82819 | 2024-12-13 03:55:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64234229-01f1-39a4-adc4-43fb4f4ebd51 | -6.39924 | -44.04333 | 2024-12-13 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6784e37c-e9c3-3632-a732-2d227e64e318 | -6.92858 | -43.52752 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84be2145-d0c4-3f37-8eae-aae32345a590 | -2.37295 | -48.27959 | 2024-12-13 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e960e438-73eb-3998-8044-7fa4670851a5 | -6.56822 | -39.43588 | 2024-12-13 03:55:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f886402a-a964-33f9-bfb2-acffca3d1ff4 | -6.76409 | -44.82551 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1cfeb709-790b-39be-b66c-82d120a8a90f | -8.26512 | -48.02769 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5e47598-65c6-3872-b698-8b074f6b4823 | -3.28644 | -45.59586 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3233a42-0f36-3ef0-8224-0facf22445df | -4.24738 | -41.92787 | 2024-12-13 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fa1eed3e-334b-322e-b703-6476f885b104 | -5.6325 | -44.8373 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 534c3742-d402-3c7a-9350-4d91233dadeb | -6.91648 | -43.55107 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be192959-a097-3454-9636-73fc68a8ef3c | -3.83374 | -41.56056 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 06dd6322-6a45-3ca4-b3fc-66e8cf2972f1 | -3.14549 | -45.59118 | 2024-12-13 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b43a39-c2b1-36db-bcae-9157a1c34a4f | -7.38747 | -38.17627 | 2024-12-13 03:55:00 | NOAA-21 | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b369d32-8be5-3f65-8398-635d24b5999e | -5.94426 | -43.76711 | 2024-12-13 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 272c70a6-89c2-37cb-902f-760697c8db48 | -4.24811 | -41.92336 | 2024-12-13 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 57509c37-4f16-30fb-b491-cd91deea6062 | -1.89709 | -46.81742 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a024c58b-dd2b-311d-ad7b-01d85a1c18cf | -3.15276 | -49.90857 | 2024-12-13 03:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b940e81a-1ceb-3175-b386-bad33db41e98 | -2.83323 | -40.30016 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02326a19-9633-3266-b599-3e238c401f86 | -4.53529 | -43.2913 | 2024-12-13 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbc9f93e-ebe0-3e12-9fe7-ceeffc1980d7 | -3.6312 | -51.14005 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bf8ed219-9b67-35db-8c23-12091cd2d65b | -5.36053 | -37.91571 | 2024-12-13 03:55:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5fedba5-d0a8-389a-a15a-f23404f00f15 | -8.26506 | -48.02676 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a6840c1-0260-3877-ab55-3aba4cc956ac | -6.09221 | -44.76364 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b53915cf-4217-3536-831f-091ec153a19a | -6.05858 | -44.02964 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59828d16-e8c8-325d-ae10-2d65e4456a23 | -5.44197 | -41.20014 | 2024-12-13 03:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6bfc2264-c330-31ad-b085-decd2f97c0b0 | -4.65468 | -43.82069 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0b32e7e-ef28-304f-abc7-ae1ed5582d75 | -5.48549 | -40.51754 | 2024-12-13 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5133191f-dca0-30a3-b445-1b3a17425a1d | -4.55098 | -43.57906 | 2024-12-13 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 83bb4460-743c-3876-ae35-ba1d0cac5c85 | -3.10519 | -48.28574 | 2024-12-13 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548927be-7f80-3129-9dc0-3be60677e90c | -4.37692 | -47.63051 | 2024-12-13 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2295dee7-05eb-3b33-82c4-ff654bc5caea | -3.10588 | -48.28162 | 2024-12-13 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c6b03b3-f6f8-3c0c-b7dc-19bf4b0d019d | -4.47612 | -48.11701 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c039d6d-9799-336f-b002-2a4b29004f1f | -1.57286 | -46.04304 | 2024-12-13 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 256010e5-d2c9-3cd4-a844-d924c277ee4c | -9.55178 | -35.83859 | 2024-12-13 03:55:00 | NOAA-21 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a43aa4c5-989f-3596-8607-485240fbfb96 | -7.36078 | -46.23705 | 2024-12-13 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 634c2721-7515-3e2e-a864-8b80ecb5ea5e | -5.65016 | -44.96955 | 2024-12-13 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c503b69-7594-3342-9d37-c3c9d92685a0 | -6.90628 | -43.53879 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 451f4b4b-c8ed-3509-853d-ebac546e04f4 | -4.67558 | -42.73584 | 2024-12-13 03:55:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f138ca8-7f0d-3df8-81a2-74631c127c20 | -1.69753 | -45.77411 | 2024-12-13 03:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcde1253-4651-3a8a-adb4-12e9b7f3d90e | -6.76845 | -44.82607 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e3973460-ee97-34ba-8276-7fef8a44de3a | -9.32427 | -35.58255 | 2024-12-13 03:55:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 820a6241-1677-341e-b90b-21a350b1da5c | -3.29276 | -45.59486 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2a7ad269-6317-38ea-8c61-3c4ec05a3ced | -4.51914 | -42.07309 | 2024-12-13 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e4451ac6-411e-34fe-b970-d742f5019b5c | -3.07152 | -40.0461 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a0563b9-f232-37ed-90b2-dbf7c69a12b6 | -6.9229 | -43.53711 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a25529d9-eacb-3378-b3a6-c2be1b4feade | -5.20202 | -43.30281 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eab82af-0213-39a4-a240-1f2ac9650b41 | -2.47518 | -49.03665 | 2024-12-13 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82e06998-5c61-3c1a-a486-58fa8f540551 | -5.95532 | -39.67803 | 2024-12-13 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9583a72a-a45f-3fce-afa2-4588aa8cec7b | -1.46263 | -46.80973 | 2024-12-13 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e235b759-141a-3a0f-b41b-52343ae8fe10 | -5.5801 | -43.61764 | 2024-12-13 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae9dfb82-9419-38c5-afbf-4331628eb6b6 | -4.72564 | -37.36179 | 2024-12-13 03:55:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d3c83077-524a-3e5d-be9b-b746f9b93ff8 | -8.07497 | -34.97549 | 2024-12-13 03:55:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 79cde41a-d86d-385e-b4cd-c5f207712036 | -4.48175 | -48.11795 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9218c869-973e-3029-a3dc-60749f8b2659 | -3.47399 | -45.79686 | 2024-12-13 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70372b31-abbc-3aec-b468-8b9b2704a52f | -6.91706 | -43.54761 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed2a7365-ecb3-37f4-b3b1-bfc3e64094da | -7.43711 | -44.74009 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd82e226-7894-3df4-b14c-469a6d218de5 | -7.43424 | -44.73138 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aca5507-5b51-3d7c-9100-1a1ece71611f | -8.27034 | -48.02755 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8bd27ed-9a03-3c56-b5bc-6d82da232950 | -6.95217 | -35.81303 | 2024-12-13 03:55:00 | NOAA-21 | REMÍGIO | PARAÍBA | Brasil | 2512705 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5167628e-8668-3d3e-ada0-5d8473e41d7f | -6.53571 | -44.52313 | 2024-12-13 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be846f93-4a4e-3be2-a851-1a36fe9e06bd | -4.88301 | -44.40323 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e92d245-924b-3a04-8254-1702323a33f8 | -4.88082 | -44.40753 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36e4f707-1c41-3d4f-87fb-58e191516623 | -5.21928 | -43.29818 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3cb14b5-6eb1-3ccc-b843-ee87e9c27973 | -5.21526 | -43.29757 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 20c460cc-1138-3787-9656-f4973a86050c | -6.56766 | -39.43939 | 2024-12-13 03:55:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8faa176-9f2f-3c49-85bd-36526c82e4e2 | -4.37466 | -48.08101 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 485c8923-6d62-3959-990f-81fa91fe8411 | -1.46419 | -46.81366 | 2024-12-13 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f92598d-7090-38bb-b40e-a27da9cbf86f | -7.8618 | -35.20751 | 2024-12-13 03:55:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53aeadec-628a-329f-bee0-1d6b21fb2f2f | -5.44911 | -44.82733 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99bcced1-d6c8-3f5d-a6fa-c0a984be4e0d | -3.36007 | -42.30757 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6758dfaa-06e9-31a1-985f-6efb30669579 | -8.71735 | -44.00629 | 2024-12-13 03:55:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 155ee766-995c-334f-8bae-909595a38712 | -3.38098 | -42.3333 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e29ba3e-81a8-3f66-8883-7fa960d5bfc4 | -5.20377 | -43.29227 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbdfef6a-6252-3beb-86b3-86e2d587462d | -6.92461 | -43.52683 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1df1e295-73ee-31ee-8010-128958d24911 | -5.08259 | -42.56657 | 2024-12-13 03:55:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11122aa5-6be6-3046-9bac-a90f499e9f8b | -6.06019 | -44.04546 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef437b83-b634-38db-8092-43f12893d3fe | -4.4898 | -48.4647 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README12.md)
