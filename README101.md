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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19f85a2a-6d64-300f-9404-b53aeb596266 | -7.75104 | -42.57268 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a581cb6b-8457-336b-9673-bb36cb2781bb | -7.77104 | -42.52117 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a61f7419-f6ce-3cb7-89b1-636f529e3bca | -11.49162 | -44.99952 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df8459b3-e09a-3e68-82e1-6acf72f5d914 | -9.92465 | -43.71751 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d3d5369-7592-342b-a600-8801c6328bef | -4.65002 | -47.95636 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10b7dc39-0eea-3d26-b34d-148a10fc0123 | -10.00178 | -50.24519 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2e421038-79f0-3b67-9bf8-4a09c86a12eb | -11.32337 | -49.01799 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c878b30f-aa16-36cd-9570-d694753dcd1d | -10.28789 | -50.29988 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b429f3c-0604-36fa-a87a-0f683359f500 | -6.69111 | -42.84017 | 2025-10-03 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9a240ae-c3b6-3d00-ab3f-957a26ba928b | -10.22623 | -48.24299 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d02b0ee-fdca-3109-94f6-885bcf90fb95 | -7.78209 | -42.50325 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc9b0b30-407f-34e4-ab4f-d2b11b0eec61 | -12.2211 | -43.76587 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d2f3966-a7d4-3d8d-8b71-e209e39ea55a | -6.22926 | -45.35141 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 827ad2c9-511a-3806-9232-366ec0121828 | -6.93093 | -44.4105 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc2f9145-212c-34cd-bcef-2398225d7a8f | -6.26659 | -53.11818 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19e0950b-fafd-3b06-a0bd-9b0b3eb1ee13 | -9.71358 | -48.95119 | 2025-10-03 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2907762c-8e46-3144-825b-edc094f144c5 | -11.46693 | -45.03759 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e50d260d-0a28-35ab-a051-7afd460aa925 | -7.52998 | -47.29 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23d081a0-df45-3416-b55f-3c49e2812a8a | -4.66261 | -45.80573 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde2f4a0-982b-3dc4-ae64-1432eae1c5ab | -11.15389 | -47.18321 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad567f56-9ddf-3f1f-9c46-44845e63f8d0 | -11.60414 | -47.65222 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0eb8755e-13d7-3311-805c-1743d3972b5c | -7.80029 | -49.86855 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38af1595-e28c-3388-bc7d-90765ba73c71 | -6.37839 | -43.87707 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32430de8-7742-3acc-aeaa-f8dac06fb41c | -11.91475 | -46.26224 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 066fcad1-8aa7-3bd2-a284-3186a0147c50 | -6.41383 | -43.8451 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd4d57cf-cbe0-3f17-ac27-663361178216 | -11.13696 | -47.20317 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d418cc7-c273-35d6-8c0c-73eb92bbd34b | -11.64258 | -46.86988 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b0b1d48-ff69-3dae-ba7b-f6b60975495b | -6.0473 | -44.22382 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 603f0266-f8b2-3181-aaac-dbaf2f309a6f | -11.06578 | -47.80022 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89bf4a8b-d729-3e7a-958e-0fcb4af0c469 | -6.04622 | -44.63031 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e7d26e70-08d6-3820-8332-0850140a5008 | -11.9082 | -46.28216 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea31bbb-077f-3bab-ab0b-144c7c2dce5a | -10.90121 | -46.70585 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3374eea-d2a2-3f0e-894c-bca5060c8bee | -9.06464 | -46.65186 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1316caa0-8535-3046-b683-1839527bf1f0 | -8.53911 | -50.15788 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ba4b138c-d75c-389f-9552-d3206919ec18 | -9.95224 | -48.77494 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91166543-4401-3873-b70e-82664a663ec1 | -10.00277 | -50.26051 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ee5fcf6-defc-3339-95e3-3edd035da6b0 | -5.38002 | -48.95711 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12711b69-cebf-3643-b214-23dce2999291 | -9.91877 | -43.75831 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 128831a5-5b2b-3b1a-bbb8-8169bde1303e | -7.76444 | -42.5976 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a9eee295-8240-3319-8c17-d8a87ea75068 | -10.9092 | -46.72266 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db324cc4-6e75-3db1-b18f-b856be72d686 | -5.90505 | -43.9076 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28cee4ca-378f-34a3-8b8a-fb0c33d305f9 | -11.25606 | -47.79715 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8b6a020-4b7c-32ba-a666-6b72caca252c | -5.71881 | -43.65741 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 897c0909-5bb8-3e9a-9da5-651ce5dd7d4e | -11.45579 | -44.95566 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34995537-7c6a-306b-9de1-68d93b518045 | -10.90577 | -46.72211 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 393b1fee-e621-3908-934b-f292d1c4a33f | -5.62867 | -43.90049 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 869e277f-387d-3232-8f91-d3d12d77b62a | -6.05819 | -44.62391 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c300be52-d9be-36a0-af27-9b7ba1859dbb | -6.40972 | -44.54683 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9b8bd9-0b33-3031-a81e-b5be54aae88d | -6.20459 | -45.91985 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14e6c563-cc46-3e4c-a6a5-94c4ae88909c | -6.04385 | -44.62161 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31b98a13-2106-34da-8839-63907458d156 | -10.87483 | -47.82496 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 061b28c3-6ce6-3521-bab3-57e8b5714270 | -6.23741 | -45.34473 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 626e7eeb-97c0-3174-b737-6dee372dadf5 | -8.24844 | -47.03752 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2b60db9-89da-321a-b7e8-f89e69b8242b | -7.7631 | -46.25971 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 6b2cf4b2-5ab1-37c3-810b-08da2d4740ce | -11.32448 | -49.01097 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5605dc73-c43d-3682-98ee-4d183920503b | -10.94817 | -46.71645 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41509ce9-f867-30ec-a5ba-fe5ea79d8313 | -5.90201 | -43.90257 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7c5684a-2e47-3931-849d-06c7f9dcb715 | -11.86935 | -44.97968 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4f29a0f-a504-3593-b6ba-0ac19d1c237d | -6.70601 | -42.79504 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb821491-67d3-3452-9458-76b7cad65fcd | -5.84771 | -43.36535 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b80c0bb-6c68-354d-87ff-f7f185d1e02f | -7.45823 | -47.00873 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecd51972-de24-306e-9d94-2b04eee23259 | -10.88288 | -46.71076 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f3e575-124a-3932-a37a-b1bb96ecc6af | -10.88974 | -46.7351 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37a8755b-3a48-370b-a9a2-172d64a90d85 | -11.67294 | -44.27485 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 677382ef-1529-30a0-b161-a25efb6d939e | -10.83294 | -41.27754 | 2025-10-03 04:32:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7f5c35bf-e140-3087-bb66-d603182891c9 | -11.6226 | -45.03305 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d89cf06-3bc9-322e-87a2-7147a2247208 | -11.83516 | -45.03101 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b87f572-9668-3ce7-aaff-9887da269ed7 | -10.89146 | -46.72374 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| d79d752a-4b92-3d04-8d2b-78081742dc6f | -5.89489 | -43.72185 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89f66c22-eecc-315c-a520-c788f182a911 | -10.58431 | -48.70876 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6f1dba05-90ff-3542-a9c6-cb1f5b042066 | -10.10694 | -50.35381 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca84a60f-fb10-3aa1-b708-ee557a069cac | -10.88917 | -46.71563 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a352b067-357f-3f93-a9a2-1bb6665f56c1 | -9.98425 | -48.78722 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df8f90d8-0899-363b-b539-ce3f871c9c85 | -6.40613 | -44.54613 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46735c56-877b-30ca-b9c1-52ffd6f22386 | -9.44059 | -47.37846 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91ff4b60-3849-3521-849b-85ee6decce9e | -5.80128 | -45.85468 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 547fd8da-57ae-3fbf-b265-4fda505c5463 | -10.88402 | -46.72644 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fae8a45-57b4-3c73-b4f9-491441043251 | -5.61389 | -51.93755 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5cdb8459-2fb7-3d09-96f4-63191e777ebf | -7.73259 | -46.25165 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03cd4dc7-0383-3f17-a3be-35697a247d64 | -11.30372 | -47.83764 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 518095f9-1da8-39b6-bab0-1bc7300aed8b | -11.90228 | -46.29778 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89ff3d6d-4745-3a24-b1e0-a10cdcb8977d | -11.14034 | -47.20372 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a7c1698-2e19-3c5c-ad05-fdc0cadce9f5 | -11.86558 | -44.9791 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ac32f6e-2aed-3b65-bc02-454679537efe | -11.85556 | -44.96817 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 94ddd310-93ef-3871-b6e3-184d4904b1f4 | -5.64218 | -43.91166 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 22a48d1f-2d75-3416-a306-4c0411024269 | -11.47777 | -45.01567 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07204bf-e26e-3f1d-8e62-fddc8990b321 | -5.99929 | -44.2695 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc515ad2-0906-3c7b-b770-e5dbcb0b10ee | -10.33803 | -43.73363 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3675c032-f161-3768-b1a7-49a5a083f283 | -11.12475 | -43.391 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de2c64a2-27a5-3903-b762-8797d22983d9 | -11.61102 | -45.02842 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9699b873-9fc2-3c8a-af5f-78af5abf66a0 | -5.34887 | -43.75108 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 13c8c701-94db-3a66-b3ee-09942338f26a | -7.35143 | -46.27205 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83849088-752b-3631-a31c-6dbc64faeccf | -10.66757 | -48.58948 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7995b15-5c4f-3792-82ed-1b9cae3a8a4f | -11.063 | -47.79611 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa81b2f4-ae63-3026-ba2f-dc2524468c2c | -11.59122 | -47.62423 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5df0498f-3f95-3762-8d9d-a1e3e7a99f24 | -11.1896 | -47.74675 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07b2025d-7bca-3dde-9f8b-1c19a7f862a7 | -5.63913 | -43.90666 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d80ac901-bf96-3f2a-84d7-e0f8a2f43de9 | -7.76603 | -42.58641 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60808915-d6f0-31b5-b8be-b48c35d0c073 | -7.77487 | -42.58385 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 65ce495c-0c86-375f-ae2f-a595a5c92392 | -7.21695 | -46.87711 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README102.md)
