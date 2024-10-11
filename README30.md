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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3c7e57-eb8f-3fb0-b66f-9918ff81ed82 | -3.36718 | -44.37179 | 2024-10-11 03:36:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 58a14252-a0df-3f2d-ac2c-134e0a47ff02 | -3.36252 | -46.49801 | 2024-10-11 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad1f014f-9e84-31bf-88ea-cc3dd9e7a2a6 | -3.30577 | -46.07926 | 2024-10-11 03:36:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05582084-9771-3377-8d37-3462e8a903e7 | -3.29959 | -46.07861 | 2024-10-11 03:36:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 25dc7ee0-c269-3eda-86d6-b16eee13b4aa | -3.2989 | -46.07817 | 2024-10-11 03:36:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31a4a059-51ee-3a6d-a61a-54d4f123e6bd | -7.88783 | -40.83379 | 2024-10-11 03:36:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c930054d-d4e2-382d-bc3a-40a791639679 | -7.88733 | -40.83103 | 2024-10-11 03:36:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 6c336780-9174-345c-83d9-f10ebff3c787 | -7.84845 | -37.90535 | 2024-10-11 03:36:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 442c5178-ceec-3e2c-9c80-81f8d6bf9eca | -7.72586 | -34.91278 | 2024-10-11 03:36:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5970b0a0-e94d-352e-8e4b-7a854063def3 | -7.72252 | -34.91225 | 2024-10-11 03:36:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d82b087a-ef2f-3753-8b48-e55e474bd2a2 | -7.67872 | -42.49049 | 2024-10-11 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d7564eec-6db8-36f7-aa3c-7a415cd9ff60 | -7.67817 | -42.49359 | 2024-10-11 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0093b516-36c0-364a-893a-d3e5d4808983 | -7.67416 | -42.48651 | 2024-10-11 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3e8734a-efe6-3826-86e8-68da80b67fe0 | -7.64166 | -42.4036 | 2024-10-11 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 48bc3d6e-b40b-33cd-9e73-1635be124d70 | -7.63656 | -42.40284 | 2024-10-11 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 536d5b1c-1902-3ef0-bf1a-8c9bed2cddb9 | -7.632 | -42.39907 | 2024-10-11 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1563a9fe-26f9-35ef-9665-6b5b9995f7b0 | -7.49459 | -34.86828 | 2024-10-11 03:36:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3205cd02-acef-3fae-be37-1a05218e8a01 | -7.49126 | -34.86775 | 2024-10-11 03:36:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 081bf523-7f3f-3216-b75c-7c7e1d1a7806 | -7.46311 | -34.97935 | 2024-10-11 03:36:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b3040a2-2cfd-318d-bd91-3b0891e7927d | -7.24719 | -35.1381 | 2024-10-11 03:36:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dddb77e0-73c2-31bb-a4f7-5c9640defb42 | -7.12863 | -35.13403 | 2024-10-11 03:36:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d09e08a0-8a5f-372c-8594-475b5196e5b5 | -7.12671 | -35.18894 | 2024-10-11 03:36:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ee39d896-5b68-3cc4-8194-bc30029dff82 | -7.10327 | -34.97641 | 2024-10-11 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14fc1712-4fab-3fb0-a4e4-4c229e6fdca5 | -7.09992 | -34.97588 | 2024-10-11 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2c50ce68-1c86-3476-b61f-3442961d29f6 | -6.88904 | -41.66215 | 2024-10-11 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6646aa08-5f9e-35c1-baef-0dc2103ae1d4 | -6.88808 | -41.66777 | 2024-10-11 03:36:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cc85ef7d-fe34-3c1d-940e-eb238ffe6962 | -6.83999 | -38.57661 | 2024-10-11 03:36:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01ad9e81-964c-3cf3-8731-3a7e7d0566fe | -6.81848 | -39.98488 | 2024-10-11 03:36:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4dd0b30a-fe63-357d-83d3-15e97de72a82 | -6.81588 | -40.08096 | 2024-10-11 03:36:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a1685bdc-2baf-3253-87f1-01131763d5d7 | -6.81584 | -40.08125 | 2024-10-11 03:36:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0f32583b-7067-3775-b9a2-3a56fb260f05 | -6.67645 | -42.09353 | 2024-10-11 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 99f5c25b-2134-37b0-b991-fa0b9c67501f | -6.48535 | -43.87771 | 2024-10-11 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d07ca125-cbf4-3c2a-8052-38f6d2964258 | -6.48464 | -43.88174 | 2024-10-11 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f1eea6-c9c7-3796-bb5b-6267c8654f75 | -6.48142 | -43.87766 | 2024-10-11 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e8e7732-eddc-3f4b-bfe8-a06f20ca4961 | -6.45212 | -38.82409 | 2024-10-11 03:36:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f39ca74-de96-3c39-b72f-0c621bb3e141 | -6.44805 | -38.82348 | 2024-10-11 03:36:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 625fe6a9-1b00-3ac2-9c0a-71867182f51c | -6.44745 | -38.82703 | 2024-10-11 03:36:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17532b37-0b2b-3bb2-ae02-8810cd2e417c | -6.44397 | -38.82284 | 2024-10-11 03:36:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e503d1e-426b-39dd-87a8-b5cabd22ccfd | -6.42542 | -43.65648 | 2024-10-11 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1bbd2a2-04a1-3507-8100-8fd0b1eb6eb0 | -6.37286 | -40.47628 | 2024-10-11 03:36:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99fe5d47-c06e-3894-a03b-9e1720b72ec6 | -6.1934 | -43.43499 | 2024-10-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8aa8e51-50d0-3bc6-a74b-af18199d653a | -6.18789 | -43.43369 | 2024-10-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c6b6c71-407e-3ab8-8657-22f48c401532 | -6.18723 | -43.43743 | 2024-10-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11e2c7eb-d3d0-31e4-a5d5-133f71cf6234 | -6.17418 | -43.70889 | 2024-10-11 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9235cab1-944d-367c-a9d5-058ba1d5489a | -6.16281 | -43.70702 | 2024-10-11 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7714a1bc-ceda-391e-a602-50cbe83fe0cc | -6.16211 | -43.71101 | 2024-10-11 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59361c40-e201-306a-b617-a761cd88f5d6 | -6.02855 | -43.62536 | 2024-10-11 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ecf1b6-e67d-3e4c-98cc-2c06ce7a8772 | -5.82135 | -43.22701 | 2024-10-11 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f8a1321-64d9-3bc1-b0cc-269ae7e5544d | -5.82074 | -43.23053 | 2024-10-11 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9d6e69c-acef-3236-8390-db9777940284 | -5.75598 | -43.17906 | 2024-10-11 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ab03f208-9ba1-31ad-94cb-193bd04b3116 | -5.70785 | -36.23869 | 2024-10-11 03:36:00 | NOAA-21 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64f62a9d-308e-3554-bd17-52a931cb11df | -5.69731 | -43.63652 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a40fba53-7536-3a0c-bca3-258a8a976787 | -5.69661 | -43.64043 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5688522-0748-31dd-ab54-2cdeb853ff7a | -5.69592 | -43.64429 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9efec85-acef-37c4-b756-271034422525 | -5.6916 | -43.63564 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6cdac3c-3e74-3f5f-a933-e2755c6bafde | -5.6909 | -43.63954 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25ef0f4e-d4ce-3ffd-941d-016c854c94ac | -5.6902 | -43.64343 | 2024-10-11 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fff7b7d6-864a-3ba7-9048-2fc7bbc00663 | -5.68984 | -40.98205 | 2024-10-11 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25bccada-a2ac-3511-8cb7-d5e9cf8bfedd | -5.68978 | -40.98569 | 2024-10-11 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a301b046-ded7-3a61-a143-42aba56623f3 | -5.45915 | -36.71579 | 2024-10-11 03:36:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4ca31dfa-9cfd-35b8-8bcf-012132bf473b | -5.45781 | -42.39529 | 2024-10-11 03:36:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9a83bde-d69b-3cf4-9241-7f0e7fa1c358 | -5.45725 | -42.39857 | 2024-10-11 03:36:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c907410f-8842-3c99-ad80-9014da393e32 | -5.45701 | -42.39769 | 2024-10-11 03:36:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f268332e-d766-38ff-8123-0396d8dfbc8d | -5.39459 | -41.24419 | 2024-10-11 03:36:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4cb1a657-d8f0-3110-a116-35261ba80a51 | -5.35332 | -42.94655 | 2024-10-11 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94074128-b837-3d76-a095-1084c737f94f | -5.34899 | -42.94404 | 2024-10-11 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cfeab5af-302e-3cf8-9522-2a6bf787fc92 | -5.34789 | -42.94536 | 2024-10-11 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33869e17-a24d-36f2-a44c-5dd3acc93e5d | -5.25543 | -37.62826 | 2024-10-11 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10469e1e-7fa4-36a5-b9d2-6d5d28a0305f | -5.20247 | -41.2933 | 2024-10-11 03:36:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d7905863-5e5d-3f6a-83d6-c22ed08042ae | -5.20051 | -41.29116 | 2024-10-11 03:36:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b290b99-fc8e-3fd2-8a29-6a62d41a79c2 | -5.19956 | -41.29684 | 2024-10-11 03:36:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95fb0e02-fa63-355f-aa07-26b629dfe232 | -5.11803 | -37.41972 | 2024-10-11 03:36:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dfb587e1-9f38-3a8f-aff9-3b994f47d6fe | -5.07496 | -43.14767 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca17d87-e215-3b88-9cf9-0af8b6c67d45 | -5.07431 | -43.15147 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7edf6651-3f4f-3611-a462-04b41dc03d44 | -4.93979 | -43.00969 | 2024-10-11 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6f0b563-e9aa-302c-98e1-278bd7bae3e1 | -4.93915 | -43.01337 | 2024-10-11 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8aa0cf57-99e2-3aa7-918e-ea665f2d2c42 | -4.74394 | -42.92829 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 65bc4376-6130-3582-a70e-9198072a1c33 | -4.74333 | -42.9318 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| afb8ef75-bd78-3dc3-a1b5-31b2163faa10 | -4.47327 | -42.88568 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bb06912-8ae8-3421-9c8b-1a92a09eafeb | -4.47266 | -42.88929 | 2024-10-11 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fdc1c6d-003c-38a6-bea0-817758f56cf0 | -3.70524 | -40.69801 | 2024-10-11 03:36:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 844b1003-9ec5-38eb-8cf1-f4404329df76 | -3.70434 | -40.70337 | 2024-10-11 03:36:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7bca9d3b-e9e8-3246-b3da-304cd425f66e | -6.96297 | -44.83862 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47457ec3-aa89-3c0f-bf3e-96527ea8d6b9 | -6.96172 | -44.83388 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8139f180-a2b4-3081-a7d7-69b176db2482 | -6.96153 | -45.29179 | 2024-10-11 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cacffec9-50f7-313e-acfc-cbf172ac7b35 | -6.96093 | -44.83832 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 784375fb-9e5f-3ea4-9bb0-38192028e62b | -6.95984 | -45.29404 | 2024-10-11 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1e0dd50-3a24-3951-b087-0d2bcda067d4 | -6.95778 | -44.83313 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b772398-6a71-3138-9e9e-ff9f49b3fbc3 | -6.95694 | -44.8376 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b753ceb-aea6-39de-a17e-06333b7871d4 | -6.95561 | -45.28921 | 2024-10-11 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51fe10d7-5fbc-3012-9009-e1915fb41d0e | -6.9549 | -44.83729 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95b80902-faaa-3c4c-8889-c06c7736174e | -6.95467 | -45.29436 | 2024-10-11 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 71937172-cd9c-30e9-b6f8-88749869ecb4 | -6.95093 | -44.8365 | 2024-10-11 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76a1d646-9dcf-3572-b8c6-e58416eb2028 | -6.94857 | -45.22303 | 2024-10-11 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb9a5386-ac92-3a86-a431-0999c75673f0 | -6.93509 | -44.60608 | 2024-10-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c9265dd-85eb-3f08-96e8-60cf0a8acf44 | -6.84554 | -46.93397 | 2024-10-11 03:36:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c53a3cba-628a-3cd2-9b57-1abc59207494 | -6.51114 | -44.00708 | 2024-10-11 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ee7de0b-1cfb-347b-a352-fd80060b3c39 | -6.49879 | -46.16885 | 2024-10-11 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd3b508c-9ad0-38df-8d2a-35bde5cc940b | -6.36041 | -46.16197 | 2024-10-11 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 523e6556-ed17-336b-b175-9cec0cdbdfdd | -6.33144 | -46.34142 | 2024-10-11 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
