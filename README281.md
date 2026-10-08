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

## Dados Diários - Página 281

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d126214c-a543-3540-873b-23068f76a549 | -6.15559 | -39.43716 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 2a029123-95ca-3436-b9ba-1120be536270 | -5.43561 | -46.64856 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 23b1cbf0-cb87-37d4-ad99-8024c8a8267e | -7.48711 | -42.79945 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 06874fa2-bd3a-3cbf-86c8-4e7f89d424f7 | -8.18859 | -46.36275 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 13c2bbb4-1506-3349-ad01-115df76683d2 | -6.12558 | -44.13251 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d83662a-5804-3a12-b99f-4f94b1bff794 | -7.78822 | -44.57673 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40faaae6-ab52-3cd2-be47-a9cf0e2ce8da | -6.13245 | -47.939 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ea9a94e0-7069-334e-8106-2200377fafd0 | -6.15935 | -52.64774 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a58a235d-786d-38f1-950a-6cac4f628579 | -7.26232 | -43.50642 | 2026-10-08 16:20:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 80b9804e-d5be-3c65-b125-1ee4170de160 | -5.29099 | -48.10433 | 2026-10-08 16:20:00 | NPP-375 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a465a740-2e02-3826-b236-a4f8cb72a22c | -7.20444 | -45.09105 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 87ca5aa8-a54b-3d85-b946-bc2572d51122 | -5.89246 | -44.17752 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0689c8d8-ae8d-3911-a057-1e730dc71611 | -2.77712 | -54.07552 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| df3d898b-52cf-3145-b936-54a59d2ff65a | -5.3713 | -44.19545 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ff6069e0-090d-342f-8b73-b00857af8f06 | -5.92858 | -51.83381 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 709ca061-93ce-35e0-a24e-be8435935398 | -5.75582 | -42.07762 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 7b893931-c590-35fa-9290-dfdfc0876185 | -3.08187 | -53.94263 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| cbc68c5c-1553-378e-a52e-3dee1d9d7798 | -4.91852 | -46.0284 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3aac8487-6414-3c5d-ac04-5c2753bb9898 | -6.19647 | -51.43819 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2004b302-050c-351a-af3e-d43e3101d624 | -2.99461 | -43.28748 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d84a2a46-baad-30f2-8791-782f8d6257eb | -4.95167 | -42.73601 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 419e6b04-752d-3ca7-83c1-21c8312f42c7 | -7.31998 | -43.99479 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8df406bd-1c21-373b-87bc-e80aac501b61 | -4.08876 | -44.1237 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| dbb58f40-6c39-3f49-8e35-d40f95be3108 | -6.3349 | -44.86993 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ebd73730-c3a1-3555-94ad-bf2b6eb38f73 | -6.9545 | -45.27863 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3fd540b6-63b7-31fb-9689-9984831f2327 | -5.92467 | -51.82565 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b9192358-b50b-384b-aecc-07b48deeb8c9 | -5.70441 | -41.73159 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a09861da-67f6-3838-8145-d71f3f495083 | -3.76722 | -44.35468 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 96596d18-9785-3168-befd-1cadef199764 | -6.00063 | -53.49831 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c3df70b6-572d-3193-9e67-669032acb04f | -5.02491 | -42.44318 | 2026-10-08 16:20:00 | NPP-375 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b3230813-d1e7-31e2-8299-4a9ba3e51d43 | -2.74851 | -54.13165 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d5d59528-e026-3736-9cb7-5f64a643a79a | -6.54783 | -35.65842 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | PARAÍBA | Brasil | 2512747 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ce38acad-07b4-3c03-aa8e-ea45e9b3e456 | -5.95735 | -46.37984 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6f601d26-a6a3-3211-8b03-f79174ce0fcd | -5.38821 | -42.96421 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 713d195c-6162-354a-b3be-09e0a0cb0610 | -5.75779 | -35.28843 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c0f373b0-ddce-3bc6-8b54-b7696fdcead3 | -4.63125 | -43.49498 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d3b39ef1-ec7b-319f-a1cb-98e9ad1ef5a9 | -5.75407 | -42.0658 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0ed1eb6c-5ef6-349b-95c4-6ccf6b7587e1 | -7.4866 | -42.82229 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| dd1af189-c751-3887-b715-9a0f28f9b424 | -4.09263 | -44.12318 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f1132a59-1bd6-338a-932d-91955aeb71ce | -6.06871 | -44.10415 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b2f430d7-90c2-3915-915b-adf3401be08e | -6.66992 | -45.35334 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8bb4f975-f3c5-3725-a678-1b33e275e4f4 | -4.30306 | -38.10305 | 2026-10-08 16:20:00 | NPP-375 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 56961d67-4520-3d05-ad25-df65064261c4 | -7.06816 | -40.94477 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 46c4998c-6710-31e1-b40a-0b815f09465a | -6.06976 | -44.65246 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe18e361-c837-317f-bae2-a7d0c87a7af3 | -6.05494 | -42.59124 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 40f48e78-8bac-335e-80b2-6204b79aa791 | -4.16484 | -43.34251 | 2026-10-08 16:20:00 | NPP-375 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56f0360c-bc68-34a7-ad08-4f16ae73932b | -5.50889 | -42.82656 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 2f3ddbdd-3f47-3541-a887-c17b10a660d8 | -6.11061 | -38.16442 | 2026-10-08 16:20:00 | NPP-375 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c7268f3c-bbf5-3e0d-b111-bbcb69f868ea | -2.37707 | -45.70842 | 2026-10-08 16:20:00 | NPP-375 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b93cb81-254e-3a3b-98f1-814b92795f73 | -6.43334 | -44.81273 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e699838-8ddc-3516-be25-7ea646373279 | -6.93092 | -43.67185 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9ad319bf-9f4f-336e-9805-f0906fd0e4ba | -5.69901 | -53.47315 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 6d11e8ae-d4ae-35cb-9229-301768818b1d | -4.52358 | -44.015 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 98389aa1-dbbc-31aa-a7f1-3588e6ead50f | -5.46372 | -45.58964 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fc59dab-8121-31b3-8bb1-98ce3d15167f | -6.44795 | -52.70433 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| b764349b-11d3-3290-9ce5-c7ad28166b8b | -3.09014 | -53.94888 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| cf19e1d3-b794-33bc-bbd5-ac23ed5302c3 | -7.3472 | -50.02581 | 2026-10-08 16:20:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| ed9b07df-c705-3dce-94c9-4ac687e731a4 | -5.86039 | -53.46322 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3fb9152e-cddd-3bcb-b6b5-16560c24b8b4 | -6.22611 | -44.862 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b024485d-e262-3987-a531-37cfe28ffad4 | -6.57674 | -53.02451 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8f209cee-07df-345e-9540-20ea26bfbbcd | -5.97395 | -41.36727 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fe02e983-fa99-3af0-adbb-808ebe116580 | -7.16418 | -46.51741 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b5fa89f-9f46-3473-8d7e-99571d8a4fbd | -6.09656 | -47.65419 | 2026-10-08 16:20:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe446a59-760e-3af2-bb72-2238599bb59d | -7.59885 | -42.39282 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| de6b85fc-24c2-3ee0-b447-6f6c8eba7205 | -4.04931 | -38.93816 | 2026-10-08 16:20:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 9c4225f7-57d8-3620-bc7a-a4c6c2aca30f | -3.38528 | -50.21538 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1588fc06-759d-3801-89d8-a797e0a9f1e4 | -5.74728 | -41.73303 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 24659dff-8e29-3bc5-8fed-2d86319d84df | -4.15342 | -43.19584 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| adb1967a-e7bf-308b-a32d-0b0e3bf1d5a0 | -6.04231 | -46.64061 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ed0ad6c-1ffe-3d5f-b4fc-5e7b8074e91a | -6.45304 | -52.70847 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 107d7c0f-42fb-3bfc-a86e-94560e54bb72 | -5.38567 | -44.18317 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b29db0a-5279-3ed3-b976-8aa75a4faf81 | -3.15064 | -43.04123 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b625bff0-c8e1-395d-ba32-744344a6d3c9 | -5.87696 | -45.94336 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e456971b-6cfb-3749-8bce-753b6dc7f16c | -6.85102 | -41.76963 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 698e8c7c-1911-34b7-9f8b-f623c5558127 | -7.39687 | -45.65185 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3731dadd-e82c-3c40-a8bb-972d34062af6 | -6.0568 | -42.60383 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94f50629-0ddd-3a1f-93db-517ef406bf17 | -6.99598 | -44.13222 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 696a35a5-48d3-3485-a468-02a02f5acfde | -3.94469 | -41.54971 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e24d03c5-063e-3307-80c9-a04c719d1e0f | -3.91517 | -44.38328 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 12b3bb7e-96b1-3893-9949-c9e4ce9ecbba | -6.84397 | -41.74663 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 4892a6db-a560-388c-b090-2546c6f132b9 | -5.12841 | -46.02698 | 2026-10-08 16:20:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5fc5bda5-3820-3e9d-adba-f3a05b9464cd | -3.30366 | -53.71887 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9c064192-b2d7-3891-be4e-0ebc977b7f93 | -5.7476 | -42.07079 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1d033149-3a41-3122-8cdb-efa459cee0d5 | -3.26563 | -42.9547 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ae3cf8e-58d8-3649-9f5d-63387f834de5 | -5.74093 | -41.71445 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b292b553-e853-3efd-a112-d298ae13fa77 | -7.63546 | -44.37839 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a13f35b7-63a2-3df4-8ed7-239563cc7233 | -7.26809 | -45.34566 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a16d0d96-e002-3a14-ac0c-99456eb256c3 | -3.17083 | -50.6034 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6ff7a8b5-39b5-3917-b8af-8346067131bb | -4.35774 | -43.80679 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ba027c1b-7890-3f5c-a32e-e8511cff1a5e | -3.08385 | -53.96585 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5e842bb7-16bb-3259-a914-2b99248a200b | -3.01032 | -54.08069 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9492d2b3-267b-3b5b-a23b-cca6702d155a | -8.1076 | -50.93042 | 2026-10-08 16:20:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9c0a494a-2914-36fd-a368-f8bd5cdac271 | -5.7156 | -41.64033 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5f983ee4-de8e-33e2-838d-462c05d53ef1 | -3.77761 | -52.62902 | 2026-10-08 16:20:00 | NPP-375 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9a4a4485-c6fb-396d-a392-75fbedb0f964 | -7.53922 | -42.08724 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 030983b1-3944-31c6-8866-937ee4577b53 | -5.37615 | -45.94139 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4e99c5b3-e1cf-32f8-886f-4c35c42aec90 | -3.93994 | -42.47713 | 2026-10-08 16:20:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d00d04b-1c69-37ab-b740-b6003fc08478 | -6.43752 | -44.81218 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59c3f920-cef8-335d-93ff-306797488096 | -5.77442 | -45.39263 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f63ddb51-daa7-3c33-b2d6-ebcfb42c8fd6 | -6.67542 | -45.36087 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README282.md)
