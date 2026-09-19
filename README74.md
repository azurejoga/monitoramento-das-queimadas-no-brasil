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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c126af4d-9db1-3359-a6cd-139d24a5c172 | -3.36535 | -50.45638 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f3b23bd-3d7d-352e-95a9-497f0b419b3b | -9.94546 | -46.53133 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb39cdf9-fb74-3b58-9009-7e6b692aaee7 | -9.16047 | -49.99611 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b6bacf9-eac4-36bb-acfe-12de4515ba7e | -9.95946 | -46.56712 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64f6e10d-5867-30b0-ba03-fae702da6a85 | -4.80667 | -56.08471 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be385ffe-2eed-3538-a6f6-5424fd54a01b | -5.87813 | -53.61792 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47b9cf12-4a41-36ba-b5f2-239bc4fa2fd3 | -6.44534 | -58.14643 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70212811-0ca7-37f8-b9e9-4152f5faa78c | -7.60886 | -46.61906 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da419652-f11e-331d-a5b6-a536451fc101 | -5.47007 | -48.9987 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aeca2a6-5987-386d-9646-4efcc5892d7c | -9.89646 | -46.5508 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b581576-a6e1-3b13-b26a-9f27f6c6e895 | -11.48864 | -45.73321 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c1a5e98-46ed-34ae-9342-3791e7da11a6 | -7.64978 | -46.10312 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1491af69-4196-36b7-96da-140640c6c0cd | -6.98458 | -42.18498 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d0632dd-a452-3a3e-a029-bbaa3c6857bc | -11.05401 | -48.30959 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f392f0e9-e8f8-3178-9097-17361732b1dc | -3.69175 | -60.60273 | 2026-09-19 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d6abde1-f01e-34cf-a22f-32e012747b81 | -9.80589 | -48.33036 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 050f3488-8060-3183-b929-681d403b1764 | -3.55084 | -58.55015 | 2026-09-19 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dedf35d8-05c7-3764-b238-ae34829de49b | -8.72998 | -52.36058 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c8ef026-6de0-310b-a50c-d0a019a49fdf | -11.07972 | -48.27843 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 69d27f42-422d-3124-aaa5-ecfbf400ab40 | -10.20821 | -46.59465 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8566212-748e-3608-841f-e4e3a9102817 | -6.31456 | -55.26398 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b29b96ee-29ef-3c10-a975-3afb53dfa380 | -2.89122 | -57.79462 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2640c775-ebdb-304c-8835-e960a8c40374 | -10.98428 | -48.29148 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86504224-f825-30cd-94ee-2c64858812d1 | -3.85232 | -50.00914 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b6ac8e0-8fbb-3b90-9d5a-df9ba074dbfa | -9.99942 | -50.28029 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf1f9237-ebeb-3a3f-9178-bda95f2c6dc5 | -7.68694 | -55.05809 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37e22a4b-d70b-31db-9826-d1e0ae412396 | -2.89481 | -57.79925 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1a891166-b963-38d1-93b3-44500d3630d9 | -9.03435 | -48.72791 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a02ad2b-7dc1-379e-bbdd-83c677f93bb5 | -10.13681 | -49.15571 | 2026-09-19 04:57:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 924b5028-f248-3fb5-92a6-521f38411009 | -7.75574 | -46.72237 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24d35c90-bb59-33e7-b3dc-1d28854f24fc | -4.68581 | -46.39657 | 2026-09-19 04:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a20aa61-4cc0-389c-ba70-f583e343be93 | -7.79252 | -44.84922 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1cad6a1-fd85-3c69-b274-e66b938cc9f6 | -9.763 | -46.07353 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18c755c6-8d37-3ce7-971c-2023effbaea3 | -6.65919 | -50.92336 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5518b72e-5727-31ce-9127-a24eb7d0795f | -5.99796 | -51.79005 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b20682-fe49-31ad-a692-aedc4201f014 | -8.77108 | -48.66798 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f64f3c89-edc7-3027-8914-1653dd6854ee | -5.23162 | -47.56382 | 2026-09-19 04:57:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4415b408-2be3-328d-bb39-0b4bdc24797a | -6.93638 | -55.03552 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e10285d6-4a41-3d9c-aecf-677ae0d13492 | -3.9235 | -55.92572 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e76aeca3-0300-387e-be96-90103d7b33a9 | -10.31464 | -49.95937 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fcf92cd-5659-373a-9bcc-d96121836608 | -11.07408 | -48.31781 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcd67703-a78c-3530-aff9-708a1c90fdfc | -5.89206 | -49.78094 | 2026-09-19 04:57:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4a7e830-923c-3c10-b414-760950e1b23c | -9.91034 | -46.58605 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0126ddb2-d474-3cda-9fd3-9c179d5a2d94 | -2.64381 | -54.68935 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26dd777c-dea9-3002-9d7e-ddf9486e198a | -3.73417 | -54.64608 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f6ca130-c13e-3b95-87ab-3d7119e75655 | -7.05381 | -47.49938 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61917b4b-ed04-38a0-a56b-a913aff0d682 | -5.89617 | -51.65861 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfbe6140-b2c2-3803-9cab-176392fccdb4 | -8.76795 | -44.22963 | 2026-09-19 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62492130-0576-39de-9d7a-9a3b3520ac83 | -6.74263 | -59.42322 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e87c968d-0473-3d28-bac8-56510e7d7069 | -8.85874 | -45.94043 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c67f9bd-f382-315e-9f48-266f425ce3fc | -3.35631 | -50.44752 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a379f51-a902-37a5-9f5f-11520fea1efe | -10.49768 | -46.26676 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d915a49c-b39f-33a5-93d2-8e175ff9ee8d | -11.30664 | -46.78682 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a04a20fd-b31b-3b93-be2e-74635b16d9d9 | -6.67294 | -50.90258 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab5919ea-3060-3c2e-b887-4cb35942c4ac | -3.37104 | -50.44232 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9f2a8d5-b801-3551-895c-39912f7d230f | -11.29572 | -46.77324 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e194b4dd-0b06-3092-ba47-156f5499e7d0 | -7.01885 | -44.65198 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f1a63af-6f44-3f2b-b5cc-d67844ec0d43 | -5.97919 | -53.57994 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 619cd4f9-84a7-33be-8c23-75051e317e83 | -3.72656 | -54.64883 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37557a64-763f-3862-a652-a6fa2a4b7d1b | -9.70963 | -45.99643 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad47e1b-c65b-3312-82dc-777a408ae246 | -10.79805 | -50.88284 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69f1b62c-8451-3ac9-800b-0be01f53ba65 | -7.75905 | -46.76009 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40a1378e-0678-336a-af9c-96a4c2308e15 | -2.64317 | -54.69331 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a611d11-268d-3063-86d1-4ef9a44ed0a2 | -7.19382 | -47.87452 | 2026-09-19 04:57:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90a8a8c3-cf28-347c-8193-8d818898ea3e | -9.96041 | -45.45338 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccde815b-78d2-3b40-a925-129e81915006 | -8.12177 | -44.8267 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0774575-9013-33c4-b2e0-29bf18e1d142 | -2.90817 | -57.7974 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d409244-8556-329f-be91-396e9dd9b0ab | -2.90328 | -57.80063 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba5aa0c3-fd18-31ae-ae80-df66fbc60533 | -6.36795 | -58.28991 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b1d843-8721-3fad-828c-36b8ac9a7a5a | -6.69197 | -59.95905 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dad2a42-4f85-30e3-90de-d827e430251b | -6.93417 | -55.02744 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eb40ab4-2712-309a-9556-b466f30ea16d | -8.81374 | -46.94757 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e08d7426-9baf-3b90-870c-12409731de23 | -11.08098 | -48.27764 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ec7f40b-f31c-3a9f-872b-ac2bed8401e7 | -3.48456 | -49.51269 | 2026-09-19 04:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba0b2cdb-0e94-3428-badb-cc6bb793f881 | -10.93298 | -47.85628 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c6db0b4-60dd-348c-a45f-0bf7e41b4769 | -4.56711 | -54.91638 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47b81099-1b3f-3b47-a3d1-689c51c2d361 | -8.72333 | -44.87435 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17ed1911-1244-3002-840f-9a9cf0038c2b | -3.46326 | -50.61214 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0fc9b66-f744-3278-bb2f-52ae1c2d1666 | -6.63103 | -43.4782 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b900a695-fdd0-3b07-8861-a504a37ef076 | -3.56037 | -53.08866 | 2026-09-19 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42951f18-a493-3594-99c9-11c570e102cc | -8.61353 | -54.60704 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f8e1e51-5136-3823-9a0e-7d9acd65a8b9 | -5.19112 | -49.33333 | 2026-09-19 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72369524-9b32-3852-8627-717fb9a966d2 | -4.55681 | -42.98162 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b732b1c1-8de4-34af-b1e2-2d7ab991b653 | -10.31092 | -49.95881 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097e8100-b3fe-34ad-a705-b42aa1018f72 | -3.38093 | -61.2996 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa3228f7-cb52-3193-9c90-36e8d622850b | -11.12347 | -45.29226 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12929619-f7df-3e28-bdb6-d67d97ec2880 | -6.99108 | -42.18162 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70345123-f000-3eba-8aa0-d5664798dbfc | -10.47708 | -46.30573 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0babdff9-960f-3622-931d-ee58d8ad44d2 | -9.78461 | -45.05891 | 2026-09-19 04:57:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34fee1f5-02f6-3391-bd43-54b73366a63b | -2.90263 | -57.80457 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0615a63b-26b1-3fa9-a959-72680102fcbb | -7.8789 | -46.43037 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1eaf49bb-3c14-32e2-8194-cede448aaef3 | -3.89078 | -49.06193 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bf27321-fb62-3f76-91d8-601870c87669 | -10.20554 | -46.57978 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94104ec0-9fe8-3ff6-b71a-f78891afe696 | -7.40029 | -49.84872 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddf3a077-bd86-3ab8-957f-f461aafd20c3 | -3.18718 | -61.11694 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a01d0b1-304d-39fa-bb05-3cf3bff908e3 | -3.18771 | -61.11369 | 2026-09-19 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b2b5e9b-181e-3caf-9fb1-cc0f4cb6bf2c | -9.70037 | -54.82396 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fed9480-db64-366c-b440-5b7dd6248c19 | -6.76485 | -59.42709 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93248eee-5a1a-328d-afbd-e42fb71fa0ac | -10.13361 | -45.56959 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a84fa69-13e4-351d-bbc5-3e202c56658c | -10.97347 | -49.75462 | 2026-09-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README75.md)
