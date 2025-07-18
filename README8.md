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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b0c7101-9a93-3de2-b9e7-72e8f300a421 | -6.26153 | -44.06465 | 2025-07-18 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17fffc5a-4548-399b-bb65-a7b054c67b56 | -8.38333 | -44.0364 | 2025-07-18 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 804b35ad-db5b-3c19-915a-d75c8962a173 | -8.07717 | -43.15633 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| d045ded2-f22a-30e5-bb97-600ed4c4d8a4 | -8.08888 | -43.15162 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f9764b91-d772-302d-9709-936bbedc1b29 | -8.09472 | -43.14932 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 66ba200c-6aeb-31ed-8bb4-efbbcdf8ee9d | -7.06086 | -42.98523 | 2025-07-18 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cbb312b1-80ea-3969-a90f-32e2ac0aaf0d | -5.78094 | -45.07892 | 2025-07-18 03:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 23cface8-04c0-371d-b3eb-27b25e13af6a | -9.59836 | -40.3497 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 13683795-2dae-318e-ac26-9c5f373ae17c | -8.09996 | -43.15031 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f3f63f86-62ae-329c-9980-e42c5a5cac3c | -8.37778 | -44.03539 | 2025-07-18 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd1590b8-0395-3134-829a-a929d4179dcb | -11.16142 | -46.25382 | 2025-07-18 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 406b4e78-6fda-310c-89f2-38ea9bf0d7db | -7.34439 | -44.19314 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9b891658-8860-3856-ab57-daed1e72230d | -7.35011 | -44.19406 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9f02f7bc-f390-355c-ba7c-b46fe3de8e3a | -7.39341 | -43.79652 | 2025-07-18 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e73d74f9-ba6d-3746-a514-22ef76bc7b83 | -8.11104 | -43.14898 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7734ba12-a248-3705-926f-66037b2419ad | -6.68564 | -43.18497 | 2025-07-18 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55d556dc-117d-3c97-9c92-3d06f99cb59f | -7.70287 | -47.29437 | 2025-07-18 03:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 857216b4-8921-3a69-9641-8835488293a4 | -6.03674 | -44.04999 | 2025-07-18 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6733a896-ae69-3942-aa6b-97ffda32858c | -7.28089 | -44.21796 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 951e802f-2780-3989-bca6-0fe57a56e591 | -6.99947 | -43.74947 | 2025-07-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 575d028e-3522-3ae9-a977-98b517cfcac0 | -9.59646 | -40.60537 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 7a0deac1-3f0f-3872-8129-bcf1dd048d82 | -9.59573 | -40.60952 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 190257b5-73b5-3622-a3a7-9da4aacd9327 | -7.47795 | -37.41172 | 2025-07-18 03:36:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e7656bb-9b9d-3e9d-a78d-27da8d718d49 | -7.1916 | -44.07397 | 2025-07-18 03:36:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d62c54e4-22f4-3624-a55b-7dbae686daa1 | -9.4867 | -40.39438 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 633aa54f-faf5-34be-9c48-841b0f90aedb | -5.84976 | -44.97807 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d07afd1-ad5a-3888-bdde-c45c42abd2fe | -9.33093 | -46.88113 | 2025-07-18 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 559eb5fc-8120-37d8-aee0-63b63a9ec036 | -11.78384 | -45.22396 | 2025-07-18 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bf7522b-95ff-3e0d-9630-4facab6948ff | -6.61768 | -47.19548 | 2025-07-18 03:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abd10448-8e44-3b66-83f3-7dbdca77115c | -7.19361 | -44.07642 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eacb808-1d93-3b60-83be-542db7701be9 | -7.70414 | -47.2878 | 2025-07-18 03:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bc59194-f1a0-3dc0-85ca-af9d69051847 | -9.48601 | -40.39846 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33556a16-3c68-38ea-8060-719ecfce782e | -9.51136 | -47.56586 | 2025-07-18 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18ef356d-6126-3c3a-b758-29d606125b46 | -5.85058 | -44.97341 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e879e1d0-8b59-35c0-a546-1095544b8481 | -5.85674 | -44.97439 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d5d1ad7-cee6-3c5c-ae42-e02b89ca7b49 | -8.11687 | -43.14671 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20ecbbc6-ca56-3d07-af9b-30b9b133974b | -5.72695 | -44.50668 | 2025-07-18 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 911f32fc-2ebe-3244-819e-32c7dba18dfa | -7.16337 | -43.59536 | 2025-07-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a52e2032-2c67-33f3-8c3a-78ce197d631c | -9.5979 | -40.34908 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bdf9a36-c15c-3ee5-9e8b-a5b53114ae4e | -6.77462 | -45.51148 | 2025-07-18 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be047049-4968-33ce-827e-e180050e47f3 | -7.61213 | -45.55639 | 2025-07-18 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c39cf11d-8b59-3bb7-9d84-900e950d5398 | -6.7277 | -44.33059 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d92bcce-bc19-3499-b7aa-e616f04b5536 | -7.39408 | -43.79284 | 2025-07-18 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3345a31-2576-3f5b-8898-7ce0b1a7e146 | -6.71611 | -44.32839 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b79c141f-3e73-3ab3-9c6a-2e823d451897 | -7.60677 | -45.55096 | 2025-07-18 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 302d3ab3-6a59-33d6-90a6-73cc28e57aa2 | -9.60004 | -40.61031 | 2025-07-18 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 23633b9c-89ee-3e3f-a451-be40ba68f510 | -8.88549 | -44.79385 | 2025-07-18 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a121b6ea-3884-3409-9852-857d5c54941e | -8.08829 | -43.1549 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 52e4722f-f54d-31ed-bd5c-9c43cb528518 | -6.77368 | -45.51656 | 2025-07-18 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d74ea7be-d9bb-3cfe-bd36-1acdf5a30465 | -11.74475 | -38.51791 | 2025-07-18 03:36:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e6fa012-5c0b-3647-953c-ec8d62bea6d9 | -7.28017 | -44.22183 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fe4edda-6b9a-31ae-a769-ef0e20e3d133 | -5.83581 | -44.10545 | 2025-07-18 03:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b91866b9-2a46-3462-b6c6-7f97f8e1ab6d | -5.91305 | -43.47896 | 2025-07-18 03:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 335d371c-d46f-3975-822b-86780f1f01ad | -6.95851 | -43.75335 | 2025-07-18 03:36:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d49c07be-c10d-3e46-af23-127d4b0c1dc2 | -7.29004 | -44.22512 | 2025-07-18 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47a9879b-d55c-3bd6-900b-619feb07985d | -6.71031 | -44.32731 | 2025-07-18 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94c0396-f28f-37f8-b306-7a1551504466 | -9.33856 | -46.87656 | 2025-07-18 03:36:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3709b853-a3cf-31f3-9914-f2bdc21bc98d | -6.69042 | -43.18944 | 2025-07-18 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5898dc64-58c9-338a-8ac3-dd201e59ba45 | -8.11629 | -43.14996 | 2025-07-18 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 791e4935-4490-35a3-8c2c-bad77186dbf3 | -7.61303 | -45.5516 | 2025-07-18 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca761120-8c82-366c-a5de-0fdcf0ea11b6 | -7.16888 | -43.5963 | 2025-07-18 03:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3bacef-80be-3e04-bf28-f5d305c26a23 | -6.26728 | -44.06567 | 2025-07-18 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ee3783-52fc-3c38-b5da-f2956b4fa846 | -5.85756 | -44.96974 | 2025-07-18 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 394cf605-c55c-3140-bdff-9788f91635fd | -15.15659 | -46.18942 | 2025-07-18 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c3f3a6-1fd4-3e89-9280-b31f4308ab44 | -11.56546 | -47.09154 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2c4b6fdb-bd6c-32ea-8893-99f6d9479521 | -12.70498 | -46.81295 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26e2a76e-58fa-352d-9a99-48b8adc664fc | -12.65895 | -47.09413 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15fc6134-b31d-3129-8493-56dcf54f0d42 | -12.65788 | -47.09922 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7cd543ec-a394-355a-a906-e783f7ea63ea | -11.74367 | -48.19517 | 2025-07-18 03:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6f7a1270-4d0c-35db-9f95-fc9bd65bbb5c | -11.567 | -47.09482 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10ee9992-454a-3a9b-bebf-a2ef9f32f923 | -20.03932 | -41.66097 | 2025-07-18 03:38:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 364454c8-454a-3d00-b832-d7d0c4f55a60 | -11.56173 | -47.08843 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e24cfa6f-bafa-34c8-adce-e3eb86e072c7 | -16.06843 | -43.64714 | 2025-07-18 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97caaddd-e942-3b99-923c-81bd3defe218 | -12.7111 | -46.81418 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11bfd506-a879-3a46-a326-08af4f77a9d7 | -11.55913 | -47.09024 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eef60f17-83eb-3868-a2c2-7ffa6bab15f6 | -14.72312 | -45.06812 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25e15649-37f2-3789-b608-c978867d9448 | -15.18385 | -43.53991 | 2025-07-18 03:38:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 354f043f-68d1-35b9-b401-de7d941e3cd9 | -14.71721 | -45.0701 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d85bbdf1-1106-3406-baaf-0a4ba005493c | -19.26073 | -40.7044 | 2025-07-18 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73b470b5-3874-394d-8d98-fa8917ac44b8 | -14.70512 | -46.18959 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71e74576-b7ea-30a9-9756-27ccf9aec306 | -14.71082 | -46.19066 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c28a3288-c430-3e55-bd74-135098ff10a6 | -12.99919 | -44.85985 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07a591b5-4a14-3bfe-8e37-aa74c6775521 | -18.5652 | -46.48984 | 2025-07-18 03:38:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2b2c5d3-a846-363c-8383-7f774e54c383 | -11.56386 | -47.07813 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dfd17b3a-1ddb-383d-95a3-4dd613999514 | -14.72027 | -45.10963 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 955db819-f3f6-3ea9-95b7-0b45fb4639d3 | -14.74777 | -46.29995 | 2025-07-18 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 907ef9c8-9e05-36af-949a-d2c38b33a88c | -11.45744 | -48.15858 | 2025-07-18 03:38:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63912e76-01ff-3144-ae9f-07abfdce98ef | -11.56224 | -47.07471 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a954e7f2-3088-3b30-be4f-7c7ec336d7bc | -20.03832 | -41.66626 | 2025-07-18 03:38:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 4672bb17-92f1-3a24-b41e-15cefcd4ff12 | -18.61411 | -44.26689 | 2025-07-18 03:38:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ba9b8a7b-bed9-3e96-9a41-3a49fbe9763f | -12.99503 | -44.86201 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1126bc20-e7ec-3f9d-9495-2e1599904817 | -12.70507 | -46.81143 | 2025-07-18 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c65ccd31-1264-3535-bb84-8e2c01b383e8 | -15.64113 | -41.26125 | 2025-07-18 03:38:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 65c2e40e-f849-3fab-b29d-75cebeea8d50 | -12.57637 | -44.74922 | 2025-07-18 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7f2e78f-a716-38c5-84bf-7af7fd105c7c | -14.72621 | -45.10755 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e3da1a1-0412-3ca6-878a-ce434e6bb875 | -14.71961 | -45.11294 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aef59d1a-bca0-3d06-ac83-e3c64922fdbd | -18.87859 | -47.98852 | 2025-07-18 03:38:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 26c5c6b7-05e9-360b-9ef9-681dfdfb483b | -14.71503 | -45.10821 | 2025-07-18 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c07b624-2640-30f2-bcd1-ee9a1d23ce12 | -11.55811 | -47.09532 | 2025-07-18 03:38:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6006086b-2ee5-32a2-85d6-b2ee2e5e2ffc | -11.84834 | -46.75313 | 2025-07-18 03:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
