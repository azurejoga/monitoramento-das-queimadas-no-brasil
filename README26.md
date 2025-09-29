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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 679c85bd-a9fd-3f20-8244-f8e6361e14bc | -15.2893 | -49.5035 | 2025-09-29 03:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 5d2025cc-afa5-3467-a042-6041f78e4501 | -11.925 | -48.0273 | 2025-09-29 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 2f994689-73ff-37d4-9e1b-dcdddd00d59a | -20.0698 | -41.3189 | 2025-09-29 03:50:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 8ef19b56-e9e6-3560-aa3e-dd6e77b03247 | -3.1012 | -47.0301 | 2025-09-29 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6e81c253-4d22-3b48-bc93-1bcb0a5b1cac | -0.1012 | -51.2738 | 2025-09-29 03:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e93eaa47-89a6-3eae-bd07-6d99071140b0 | -20.0689 | -41.3449 | 2025-09-29 03:50:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| e2b1c341-4a79-3764-8dca-e4c8a02672dd | -15.2888 | -49.5256 | 2025-09-29 03:50:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| aed55127-9d01-385c-92b1-84313eb6308f | -2.5772 | -48.4146 | 2025-09-29 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6a82b1b2-9433-3341-b8a9-35e0bd7d6ae2 | -7.2402 | -44.7812 | 2025-09-29 03:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0e349cea-fdc1-3333-918b-27781a0e286f | -3.1013 | -47.0082 | 2025-09-29 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 68807baa-f9c9-364c-a86f-8d3ceb3dd58c | -9.4194 | -54.697 | 2025-09-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3782f326-4812-3b0e-af70-b97892ace387 | -8.2851 | -45.4999 | 2025-09-29 03:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 01c35402-3335-34a2-93ad-bc1e944d8c6a | -15.2655 | -48.7544 | 2025-09-29 03:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 55ec37cc-f649-3847-a185-12d46e63469e | -9.4007 | -54.6984 | 2025-09-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5b071c2e-fd80-3197-aa27-a6e773c9489a | -2.5772 | -48.4146 | 2025-09-29 04:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 76a004a2-47ea-3928-bb4f-bed7675f588b | -13.3796 | -48.1577 | 2025-09-29 04:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 80c770a5-ef8d-3c50-8db7-4aae9875172d | -11.8291 | -51.7937 | 2025-09-29 04:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| eeaec36b-73da-3b07-9c2b-44ee3409874e | -13.3989 | -48.1549 | 2025-09-29 04:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d0afcee6-fb41-35a7-84d8-7263e9e96133 | -20.0698 | -41.3189 | 2025-09-29 04:00:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 6fc16a33-13b1-39ea-91bd-676d612ae594 | -7.2402 | -44.7812 | 2025-09-29 04:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| dafa5d16-0398-37a0-a9ae-af3c2b584629 | -9.4194 | -54.697 | 2025-09-29 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2acfbc3a-efdd-3dd5-afd4-0303d1f04756 | -20.0491 | -41.3251 | 2025-09-29 04:00:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 64a9733d-7357-31bc-90ec-92ece074a774 | -11.925 | -48.0273 | 2025-09-29 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5a2b8af2-8d37-3d3a-ae75-da59f831f9f8 | -15.2893 | -49.5035 | 2025-09-29 04:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3f0e069d-e63a-3c0d-b556-c20c70a81b7b | -11.8294 | -51.7725 | 2025-09-29 04:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5505864f-0caf-3135-acd5-81c4f852a085 | -11.8482 | -51.7916 | 2025-09-29 04:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 91e62e0d-a1c7-304f-a650-9273b636b0f5 | -7.2214 | -44.783 | 2025-09-29 04:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 107eefcc-26ca-3542-a0f9-d0963c9e734f | -8.2851 | -45.4999 | 2025-09-29 04:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e48c0234-8057-384c-9573-6ae34b4dc568 | -0.09664 | -51.27623 | 2025-09-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9ff839ff-9e9e-317b-ab34-996cee3952c8 | -2.87839 | -40.02245 | 2025-09-29 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb6b76a3-647d-3faf-ab3d-90aaa2793509 | -2.87507 | -40.02193 | 2025-09-29 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a31d4c25-4bb9-3673-aeed-e1b275d184cd | -0.09513 | -51.28561 | 2025-09-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 07c1eb85-aa5e-342f-a75a-efdd5782eab4 | -2.87453 | -40.02539 | 2025-09-29 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| f1a59ae7-917b-3a0e-83e5-bfa1516f0990 | -2.87785 | -40.02591 | 2025-09-29 04:04:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 493a0b7c-1056-386e-abce-22ab98171e76 | -0.09594 | -51.28254 | 2025-09-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 497d87c4-1cb7-37f0-96d0-408eb95d53ac | -0.09589 | -51.28091 | 2025-09-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 99d08590-c140-3833-a7e9-3754e4bf3ead | -0.09667 | -51.27783 | 2025-09-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 61874a02-19ec-3453-b779-b9583e5f677a | -8.27793 | -45.49919 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0a8be321-49e9-3a0e-bea2-05162d62bb95 | -5.82404 | -42.80791 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d0662d2b-eed5-3753-b964-9b3f3a65ef9c | -7.60164 | -44.42891 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504c435e-8c56-31ae-afb7-5ce77d3719db | -7.38489 | -44.29293 | 2025-09-29 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc9777f3-20bc-3db3-885f-f9029485b7f6 | -5.91068 | -45.85415 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1da2a531-1f29-3a46-b512-92636e2e85ef | -6.57039 | -43.422 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df158772-b78b-3140-b06f-eb5e1231cf12 | -8.30595 | -44.90601 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a20417f-0045-3c10-9e2a-21026cbba0e6 | -5.21981 | -43.76955 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2fa9d68-d3e1-3848-91a0-518d2cfe29bf | -6.38327 | -44.01215 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0c4b3e2-1122-3dc4-b7bd-dd2b3e360965 | -7.76447 | -45.73332 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8342e97c-d891-3a22-bac5-9381acfeb4e7 | -6.22121 | -38.24649 | 2025-09-29 04:06:00 | NOAA-20 | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d98b6f40-82d8-321e-a16e-1a1aa9f3f56c | -6.05276 | -42.45901 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6d1f05f-f947-3940-88e4-4ce2fc92c41f | -7.81125 | -46.90593 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ab6cbe2f-ab96-386c-b674-9510715e690c | -4.1441 | -40.00964 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed2bdf6e-440c-3f4c-b884-0d1f9fefa524 | -5.29719 | -43.1615 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33532c1-a73c-3116-9ffe-761437a6fca6 | -8.28014 | -45.48611 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d72be818-255c-3378-9a51-09dc5b3a473e | -5.76115 | -42.84623 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f656a11-b271-3a5e-b404-a6b2d831c5b7 | -7.03033 | -45.18141 | 2025-09-29 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a152dcff-3663-3565-981e-cda95cfe2f72 | -6.28106 | -42.47711 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eba2139f-d45c-330c-92e9-d4a49d610102 | -5.71522 | -45.5283 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdb90c8b-d753-3972-88ad-2a286a21ec92 | -8.29941 | -45.48446 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4ff7fe9-f2cd-321b-8325-1971ab60a3d3 | -6.46098 | -44.00415 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 511b9bc5-15aa-38ec-8237-540e4cbf2d19 | -8.14439 | -46.39987 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a913da8b-912f-3318-8bda-c1d8d5a5ef1e | -5.36934 | -42.84469 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 236fc600-c471-3e26-8ced-7187301bb939 | -8.30301 | -45.44051 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 15ec6394-bd34-3845-a918-f7617e9f81e2 | -6.13992 | -43.48121 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07fd05db-88b8-39c7-9043-f113d81d1e8d | -6.15366 | -42.78595 | 2025-09-29 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 803aa19b-1918-388e-a555-0818a71e4280 | -8.14831 | -46.40045 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9fa8b008-642a-3550-b497-bc3bc5c70a6b | -5.42257 | -42.26147 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67e483c9-5f01-3426-ba03-240c07c27236 | -5.50938 | -42.73561 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 960adbfd-ce9e-3d8c-a220-107b147a8882 | -6.40609 | -42.82628 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2e554bcb-0b36-324c-8344-a09851f91a30 | -5.15117 | -46.41828 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65225d81-5873-388e-b325-7f08fe822028 | -6.91134 | -43.99826 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 482fd739-0121-3054-911a-9a990279cb48 | -3.09588 | -47.01274 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 05f82512-6813-3341-a049-781ee3418488 | -6.46431 | -43.94023 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd9779d5-7f3e-363e-9ef7-22de90c643b7 | -4.44284 | -40.98182 | 2025-09-29 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 86858adc-3d70-30a2-b1e2-07c54e92a654 | -5.71138 | -45.5277 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc0811a8-f317-3001-9c3f-de5e2ccb5b53 | -7.87244 | -44.5916 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 286c2ede-2d80-3af1-88c5-39aa139154a5 | -5.64602 | -46.25514 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d85ed53-ea51-39c5-8c8a-cfb509c8a302 | -5.15073 | -37.7172 | 2025-09-29 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6eac1798-99d6-32bb-b880-631ec8635303 | -5.28085 | -43.15532 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b1e75b1-8df0-3925-9c5d-d6aac53c7086 | -7.44246 | -46.98915 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e074bf7b-d842-304e-9ee1-2d3f3fc68b64 | -8.29869 | -45.48873 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ec2bd5e2-95a7-3672-a26a-3d6a10276aaa | -5.29597 | -43.16898 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5dc9bce-5434-3a67-9bfa-9de4cda5bf30 | -7.10632 | -45.53796 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd58d8d-a1c3-3603-9873-b97b4affd920 | -4.31633 | -48.08525 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3021064-3eaf-3536-9639-bfd59c828129 | -5.02858 | -42.5382 | 2025-09-29 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6214712f-b755-34b3-95ad-21cea4d72f8e | -5.15011 | -37.71906 | 2025-09-29 04:06:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 884e0d6f-7994-3a60-bb25-5c4ecbf655fe | -8.29932 | -45.43991 | 2025-09-29 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83e604ac-2e55-3edf-a7cd-165a9fe0b446 | -7.58971 | -44.79074 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5abbfc1d-07ae-3775-818c-1da16aa55c87 | -7.81609 | -46.9992 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81327c1c-ff0f-352b-b72a-81ec0ed16be7 | -6.4727 | -44.51397 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24c725f1-e6ac-3772-b4c8-90057ab4dc18 | -5.393 | -42.29659 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64e743d7-b6df-3d60-b89d-d4c237f83915 | -6.10911 | -41.82962 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40c12151-1ff4-3452-a125-e4db0c741781 | -6.7396 | -43.37297 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1d7cc2f2-3f04-3728-ba62-b77a8dde9dfe | -6.47069 | -43.94511 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3945fd8a-50a6-314a-aaa0-65966e3a7e3d | -6.49575 | -44.1227 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c20060c-52b8-3727-9758-eab1f1822763 | -8.29569 | -45.48401 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2256735-c3f9-33bb-9d08-fc369c61a207 | -6.14288 | -42.81001 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 56d27b82-9238-3e03-9117-e0dca1b61d09 | -5.36256 | -42.84361 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c190ee5-2fa5-3196-acb8-75ee95cec071 | -7.38898 | -44.46573 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 758a21f5-92c3-3e5a-8ec0-e2a2cddaf75c | -3.05565 | -49.59906 | 2025-09-29 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68bd3826-a51d-3bd1-badc-04e0211dbcb3 | -6.1132 | -43.44998 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README27.md)
