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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2951750a-e420-3e25-9a43-88e5ec727cdb | -7.04937 | -41.47063 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 82b8d580-780f-3966-9516-8c805a50ba49 | -7.06577 | -47.36949 | 2025-11-01 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eb6c6998-de6b-3e7d-bf84-eeca4d602544 | -4.17947 | -42.95923 | 2025-11-01 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83d89b33-2115-3b1f-a042-a4510ae49375 | -7.03819 | -41.46703 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b565a8f5-3307-336e-bb3c-cb68980fcf86 | -6.57628 | -48.73989 | 2025-11-01 03:47:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ebb91b0-f06b-3515-a354-271286a625f3 | -7.0376 | -41.46874 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1cfa3ee0-5bb6-3f5e-b29d-2424da3a17d1 | -3.26283 | -45.32944 | 2025-11-01 03:47:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4a41fb0-4b43-36ba-80fd-b7a1bb4594e6 | -7.38262 | -41.93553 | 2025-11-01 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0cb228df-862a-35fa-938f-00d5e2bc2170 | -9.99376 | -37.81804 | 2025-11-01 03:47:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2c08f3a-a2e8-3acb-807f-c837d495a6e0 | -3.26527 | -45.32701 | 2025-11-01 03:47:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da1b93b5-f64e-3aef-92fa-81baa5b08f93 | -13.20627 | -43.13103 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ceb0ed33-9c14-3a94-82ae-ed5bfc1d57fb | -5.20595 | -45.13537 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0b7bfd9-98b2-3e32-a8b8-bc0bcee327f4 | -4.29047 | -46.26222 | 2025-11-01 03:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5fec4a-86a4-37ec-bbf5-eeacf1da3d0d | -15.52044 | -41.67302 | 2025-11-01 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 810de561-b93b-336c-bf22-bd33b2845fb6 | -3.53006 | -47.55629 | 2025-11-01 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ebc0103-82b1-37c9-932c-ba45cbd6d067 | -5.06597 | -43.95897 | 2025-11-01 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab16792-4fb9-3410-9bed-f367510bf112 | -5.4861 | -43.09034 | 2025-11-01 03:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ec24add-03f3-3b84-b93f-e54b8c4f9a6c | -5.11526 | -43.38535 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4acfca28-044b-3004-b14b-1a892d45a02b | -11.84248 | -46.0105 | 2025-11-01 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 03ef77d8-d4f8-3ff0-9ab4-6aa04ba03e40 | -4.64327 | -47.95861 | 2025-11-01 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3684abe3-ce7e-3790-8187-b285c26cda7f | -5.59185 | -49.08 | 2025-11-01 03:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 769fd8c6-e648-3413-b23f-76a4fd58fef7 | -17.90988 | -39.46819 | 2025-11-01 03:49:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f0dd9989-fd3b-3951-bd65-8a907a20bd48 | -7.09906 | -34.96146 | 2025-11-01 03:49:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37bc38a1-7543-3c2a-9f10-1cfb5310c3f9 | -12.62336 | -38.0763 | 2025-11-01 03:49:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 93dcebce-dfa2-3452-91cc-f6c38b1e29df | -15.74886 | -41.33226 | 2025-11-01 03:49:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2510630e-6f93-36a3-8839-e0f0605f7baa | -5.12901 | -38.05648 | 2025-11-01 03:49:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d177dfbd-f687-3b73-b817-cc3571c41c91 | -5.12361 | -43.39181 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c61f036f-fd94-3c4c-8576-e78b027af502 | -4.82314 | -45.79016 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e9dd64b-1b1e-3399-a7c0-bdd7b709abfa | -4.96149 | -40.5516 | 2025-11-01 03:49:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 18.4 |
| a1bb7f94-4b71-3f93-8b04-d9f4fb5ded0c | -5.06418 | -45.11626 | 2025-11-01 03:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 385fccc0-3ea1-362b-beb2-052ea13e9482 | -6.13407 | -45.9431 | 2025-11-01 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 377117c2-d82c-303e-af8d-d98d4f3f533e | -11.44032 | -45.14543 | 2025-11-01 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad42cd8b-fe93-3343-8dc1-85df39b85937 | -15.51972 | -41.67716 | 2025-11-01 03:49:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c587483a-d506-3b03-a6c6-b87125f4f04e | -10.41205 | -44.33487 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7afc8f11-fccc-3fa8-9083-4c3b8deb14f1 | -5.26058 | -45.60914 | 2025-11-01 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fb1f9008-7829-34d2-8054-4199fc48670e | -4.5723 | -49.41761 | 2025-11-01 03:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8b56ecd0-1dba-3fb3-b1c1-1c7a821dfd86 | -4.75373 | -44.46801 | 2025-11-01 03:49:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 799274a7-7787-3a6a-856b-b718cc86e7f1 | -5.18683 | -44.90834 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dbbc709-3efa-33dc-85e4-fef6dfb2bc77 | -5.29958 | -45.34536 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 170a8fac-dcda-37d3-8c08-8380ca80bc46 | -10.79319 | -44.45021 | 2025-11-01 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b272618b-d3bc-3d4c-ad8f-e18bef4c9b57 | -5.10903 | -43.39408 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc78d3d0-55ce-33fd-b9a8-79c24808e6b5 | -10.41121 | -44.33954 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffa2f663-ec67-36fa-8067-626d0865995b | -5.18734 | -44.90539 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9faf7b11-c5ba-3221-8373-46a9f57164df | -4.29609 | -46.26342 | 2025-11-01 03:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7788389-a431-3ce1-a0c8-9dda96e5c8dc | -4.56374 | -45.88045 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2bc1cf8-f01d-3301-b1ec-0c0acda841a4 | -4.83804 | -42.73589 | 2025-11-01 03:49:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca030999-76f5-3249-891e-1ffc4f987330 | -5.5357 | -46.53747 | 2025-11-01 03:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95a31032-da42-30ea-8b3b-60e04e330c4b | -15.3903 | -43.50324 | 2025-11-01 03:49:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26a7aa66-d785-3f1a-9d34-7af9708fb204 | -3.526 | -47.5524 | 2025-11-01 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2edf3df4-992e-382f-8769-52e005ac8e09 | -11.06917 | -45.19855 | 2025-11-01 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f26294e-aa85-34d0-9ba6-173a8bf52971 | -5.20545 | -45.13836 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e616f566-5576-3e56-a623-71673cf3a7ee | -12.88418 | -48.277 | 2025-11-01 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d265de55-6288-3fff-bbb4-eb9d5b52df62 | -4.67739 | -45.80966 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97d86600-00e5-3095-9545-43a80b34d249 | -13.41166 | -42.9966 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9efd7dd7-c342-3d1e-ad5e-b46ac3e4bc58 | -14.02465 | -43.2669 | 2025-11-01 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9e39c35-17a8-39ac-b93e-ffddb2cc47b6 | -14.97632 | -43.56105 | 2025-11-01 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 16dba1eb-4d1b-3c25-a159-10343d33c22f | -4.60604 | -44.42816 | 2025-11-01 03:49:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2adacaa7-f19e-341f-b298-f04a7ee5bfa0 | -13.03123 | -48.25563 | 2025-11-01 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35a90e4c-a504-3674-85a6-614c815f70d3 | -15.36385 | -43.53976 | 2025-11-01 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7662ff2-8baa-3c62-90b1-a78b3d936ce2 | -4.80268 | -45.87526 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3881e382-b6d1-3026-a610-bcce33d6a6d0 | -12.29744 | -48.04731 | 2025-11-01 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5f43aa6-de0d-3e72-b4e3-f1db244e727d | -11.44094 | -48.18282 | 2025-11-01 03:49:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| badeae5b-78b9-38b1-9bc4-a6b77a35c6ea | -6.32202 | -43.62455 | 2025-11-01 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 663133ca-0f29-32dc-b0d1-de1cc123fe25 | -11.43936 | -45.15067 | 2025-11-01 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3486fe2-99ca-3ad1-bf2e-ba870999c7ee | -12.88492 | -48.27329 | 2025-11-01 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fad4e63-1fc0-3293-a7c3-228f1a5a5777 | -5.19088 | -44.91523 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32c0bfad-ae55-331a-a3c0-55510a143d5a | -5.8814 | -44.52684 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7c8649d-9060-388c-ba9f-4569a9f5b078 | -13.74995 | -43.60209 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2885701-0c83-37ef-a260-70f083fe26c6 | -13.4838 | -46.59404 | 2025-11-01 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1357da27-6e0f-329c-8fb7-4eb64e631ced | -4.94944 | -43.45071 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5bf447c-1eae-3ee6-b6b2-fff42a4174f6 | -4.45121 | -44.22102 | 2025-11-01 03:49:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53d8542e-2f95-37ae-9df5-e9b99d5cc89e | -4.58344 | -44.99143 | 2025-11-01 03:49:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b44961a9-897d-388a-a023-f9b822c3716e | -13.35709 | -43.7865 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 362891c3-59fd-3f91-8513-e10cd8f97dda | -4.96532 | -40.55221 | 2025-11-01 03:49:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d147322a-9fd2-364b-a25f-e2f8fdd05ac2 | -15.11084 | -42.25777 | 2025-11-01 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11b7a908-d468-33f0-952c-0262fc86ae35 | -14.97726 | -43.55582 | 2025-11-01 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| acf124cd-8840-341c-99fa-e70e06954bb6 | -4.94349 | -41.76675 | 2025-11-01 03:49:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 825b9103-61c9-3247-97cc-91caad8abcaf | -15.59024 | -43.15618 | 2025-11-01 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69c0d21a-7669-3462-a850-ba96178a41bf | -7.02512 | -38.82841 | 2025-11-01 03:49:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dc682f38-78c6-33ea-a173-51b0318ea413 | -5.58576 | -45.03766 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b79be176-d63c-3710-aaeb-0520c6f500fd | -4.80464 | -45.75998 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c7eb4e2-7743-34c5-8b21-962d11a93425 | -13.41208 | -42.9942 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0a62825e-10d9-3557-b2ce-1efb4167bff9 | -12.40275 | -40.40556 | 2025-11-01 03:49:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 383b3153-1896-3b8c-9f04-a2ccaee3c1fb | -15.11526 | -42.25403 | 2025-11-01 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24d45dde-c6b4-3fb8-8f0e-b0eb7a8fcb1f | -5.2289 | -40.71411 | 2025-11-01 03:49:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6664afc0-e1fc-31d6-8576-ef193fcc2e49 | -13.16146 | -42.28382 | 2025-11-01 03:49:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 82b65adf-140d-3dfb-98d2-31d27b516b76 | -5.12904 | -43.38773 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c690535-7f8b-3d8f-816c-bbd66af5c1d2 | -5.92797 | -43.36642 | 2025-11-01 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ebcc55fa-b0ef-34a0-b77b-99c8614e300a | -4.55872 | -46.6885 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 364a2e05-474a-3aa7-b732-384238f4bf04 | -4.64414 | -47.95374 | 2025-11-01 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91f16417-bc56-3468-838a-9862a11f9481 | -5.83475 | -44.06129 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b9767aa1-10b2-33ca-85d6-b0725d897c13 | -4.64008 | -47.95613 | 2025-11-01 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9419343b-58c9-3cb5-aea5-caa0c3a124d7 | -4.40247 | -48.21869 | 2025-11-01 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 396765e8-ec2b-3078-a6fd-550f45dfa90d | -11.66601 | -41.68749 | 2025-11-01 03:49:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9c73d04-195b-3c47-bf64-6c4a09e74da0 | -5.19141 | -44.91217 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4071a4fa-9a54-39ea-9eb9-85926641ccaa | -13.71949 | -51.46109 | 2025-11-01 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cf112b0-9512-3ef4-9cef-e7f52ad76c34 | -6.79786 | -42.21405 | 2025-11-01 03:49:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f14d9644-1da0-3e3c-bac3-d9fd0ab051b8 | -4.67069 | -45.81609 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37838ca3-3c9f-388b-a425-31e432f8456d | -5.45622 | -45.4069 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e666ccb-9179-3a56-b265-ec0973595d86 | -4.80878 | -45.87259 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
