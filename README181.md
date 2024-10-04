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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98ac6256-1a59-3c8f-b35c-37ea92389555 | -15.36023 | -58.14537 | 2024-10-04 06:10:00 | AQUA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a72b27fa-7bf3-33f5-b7e5-63aca11c0d9f | -15.3588 | -58.15571 | 2024-10-04 06:10:00 | AQUA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f7b9e3e7-4fa1-378d-975a-e3e3e2c4e09f | -11.77075 | -58.887 | 2024-10-04 06:10:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f007c775-ec45-3236-babd-e1becee08fcc | -14.17795 | -60.25124 | 2024-10-04 06:10:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4543014-411e-36f5-9d6d-a5b5103fa306 | -8.87734 | -61.82857 | 2024-10-04 06:10:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b7d10082-f2dc-36b1-bf34-65f6caeb300b | -8.87644 | -61.82283 | 2024-10-04 06:10:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aa3caca6-4fd7-3ae2-a3fb-3d09bb3965a6 | -8.87469 | -61.83416 | 2024-10-04 06:10:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1c807c5b-1b08-3919-a35f-7d3b343e124d | -13.61679 | -51.20421 | 2024-10-04 06:10:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 76c6be05-133f-3989-be52-355200ef8477 | -13.08052 | -51.13426 | 2024-10-04 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 47c51e40-f506-3fc0-913c-f330f8978ed0 | -13.0688 | -51.10348 | 2024-10-04 06:10:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 41de1035-b099-3b9b-8999-aac0f3da321f | -9.33409 | -50.79058 | 2024-10-04 06:10:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| bbdab14b-229e-30a4-b26e-8c482f045b23 | -9.32134 | -50.79469 | 2024-10-04 06:10:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2d9c88ef-c2b6-39aa-8fe7-12772cb3395f | -9.31942 | -50.78932 | 2024-10-04 06:10:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| d5aff6d7-91a0-3499-8540-b2228c914895 | -9.1073 | -51.51346 | 2024-10-04 06:10:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f8f99fa1-ff03-3d7c-8a14-fbb2aab11095 | -10.44997 | -50.72398 | 2024-10-04 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| a180016e-af66-3856-8147-a9dd0c40c3ca | -10.44992 | -50.72886 | 2024-10-04 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c8da198d-77a7-35d4-8ae9-e51da4b9c7d3 | -10.42443 | -50.80639 | 2024-10-04 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a4c65838-3e43-3d4b-a724-a7c340fbf29b | -12.66988 | -54.04373 | 2024-10-04 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1b0083b7-4f9d-3a90-b9a9-18051453859b | -12.66363 | -54.0499 | 2024-10-04 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 60b4ffb4-7b5a-3a16-8f09-cefb7013dbda | -12.65802 | -54.04218 | 2024-10-04 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d80d147a-7ff2-3ff2-a70e-107d6d6f2ca4 | -12.65583 | -54.05898 | 2024-10-04 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 37cf4c3b-da11-3676-add1-317e6623ab84 | -12.595 | -53.11229 | 2024-10-04 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9fa6db3b-f681-3472-ad52-84e6a185a28f | -12.59412 | -53.119 | 2024-10-04 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 67f63839-b415-3214-b35b-d238895867d0 | -12.59249 | -53.13199 | 2024-10-04 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 7f6de427-3d99-3f27-98ac-0ac0e05be8d0 | -12.58223 | -53.11066 | 2024-10-04 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 39f208ea-edd7-30a0-93bd-187064e644af | -17.04425 | -56.69727 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| a1509ebc-63f9-337f-a6ab-c27f2115f847 | -16.92625 | -55.83176 | 2024-10-04 06:10:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 535469c4-2541-3267-9777-e64026a780e7 | -16.92474 | -55.82602 | 2024-10-04 06:10:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| b1a5c8e1-7d4e-3782-872f-bccfefddcdae | -16.68087 | -55.50089 | 2024-10-04 06:10:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 2cd757bd-421c-328c-a8b0-fec8ecfe5be5 | -11.8239 | -56.58385 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1cffdf0b-14c4-309d-bb97-0ef3ff1e59b6 | -11.82238 | -56.59477 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 6705dffb-5775-3ba2-ade9-38f7763edc7c | -11.82087 | -56.60566 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7c2b5ea8-149f-3655-bc3b-b6a1772dac60 | -11.81117 | -56.60428 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fe2ec3fd-120c-39e5-8400-0a3968e48afb | -14.94889 | -56.42287 | 2024-10-04 06:10:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 707b7687-f121-3ba3-b72e-469aefb045bf | -16.61425 | -57.17728 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 240d304a-7f85-3830-8f8b-0513523c08b3 | -16.61268 | -57.18908 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 728b1292-de25-3f29-b1fb-e1f5763dafec | -16.61111 | -57.20087 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 285659e0-0c82-3c6b-8e68-fbd46b736dd8 | 2.68961 | -61.31988 | 2024-10-04 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d30643f-edc0-3a04-a5b3-520fea824861 | 2.68899 | -61.31617 | 2024-10-04 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c646b78-ea69-3967-b0e3-33750d516ef1 | 2.68343 | -61.31725 | 2024-10-04 06:10:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1edf3575-dd56-330e-9380-076b07919ff9 | -10.69262 | -69.03425 | 2024-10-04 06:14:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c16e3c39-a6a0-30bd-9b9a-41580a294829 | -10.68907 | -69.03002 | 2024-10-04 06:14:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 437da307-c531-3c34-9823-19b39a4421fd | -10.68857 | -69.03361 | 2024-10-04 06:14:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cfec7f5-6fb1-3195-890c-e98977c40eef | -9.59802 | -65.67142 | 2024-10-04 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2de9460-ab68-3cc8-9203-c1a95ddc1f01 | -7.8289 | -73.07368 | 2024-10-04 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfe774b1-8002-3aae-a9e8-7c8b395ecace | -7.79629 | -73.06861 | 2024-10-04 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0912333b-fad4-344b-911d-3df00af82b63 | -7.75036 | -73.10072 | 2024-10-04 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1191b763-6e06-3425-827c-44bfa5c71003 | -7.68367 | -73.0548 | 2024-10-04 06:14:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47ff7004-baef-351a-91ab-b37f4a47e62a | -7.63774 | -73.08688 | 2024-10-04 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90a7a56b-0bd6-3f25-8e54-e5fd7a94cec6 | -7.6372 | -73.09037 | 2024-10-04 06:14:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49f8eacc-8795-3255-81e6-6199ce1421ca | -7.38766 | -72.93658 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0acf5bd8-ad75-3e69-be7e-3949c8cc297d | -7.38488 | -72.93256 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fafeec00-58fc-362c-aa71-df26c61c3697 | -7.38433 | -72.93605 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d940fba-3938-3680-98a1-913e91bcada4 | -7.38155 | -72.93204 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ea83f8-c625-345e-9a94-c8b0873da06c | -7.381 | -72.93553 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bb40c5c-0b76-33d3-b5a7-e98991bd930e | -7.37484 | -72.90955 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dddead2e-aded-3a7e-b6cc-a77cd6f4880c | -7.45782 | -72.70027 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1497cc3-d2ae-3e57-97fe-9d40045c7c51 | -7.43535 | -72.80087 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e7fe86a-f5fc-36fb-a80a-60027b25fc94 | -7.43202 | -72.80035 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6145b53-3860-31c6-9435-6f122140029c | -7.43106 | -72.72486 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 506bfe3e-7545-3598-b892-446ee6a9280f | -7.43051 | -72.72836 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a23f8f6a-acf6-3d5a-b21e-2fe88db2d61d | -7.42717 | -72.72784 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 188f135f-fa62-3f82-b86b-54606c751299 | -7.42662 | -72.73135 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a100a13f-3453-31df-8f30-fdf89d2291c6 | -7.42607 | -72.73486 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74c8375-5164-3994-9d67-7e4ad5c673f5 | -7.42383 | -72.72732 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 859d3061-70be-348c-9d98-4bdaa0d926b5 | -7.42328 | -72.73083 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23985ac1-4b20-39a4-9d35-0a3cb0a07848 | -7.42274 | -72.73434 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd096236-55fe-313b-96b3-76f2d54cc887 | -7.41995 | -72.73031 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 512979ac-ba1c-32f0-8864-48299a94ac26 | -7.41959 | -72.81991 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6effc283-141a-3a1b-a9b0-5688687405e6 | -7.4194 | -72.73381 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b27cfba2-a18f-38fd-8707-04947a97f0c3 | -7.41904 | -72.82341 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f84b849-bd97-3fd4-96db-8a1dc377f990 | -7.41625 | -72.81939 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 807f223d-27dd-3f45-8ed9-b484d311ac29 | -7.41571 | -72.82288 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 081a6526-f423-3c2a-ac76-3d6b63b24a0c | -7.41292 | -72.81886 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f59eaa4-da2f-3126-b3c3-9b321b988481 | -7.41237 | -72.82236 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2a7ae4a-e780-3054-9fe1-331796295616 | -7.38288 | -72.79266 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4604ea9c-8913-33da-b098-8e40c9b37e34 | -7.35746 | -72.64866 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb156057-3be1-326d-8ca7-303766737675 | -7.31127 | -72.75654 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 136be1a5-735b-3e2f-af2e-d9a5cb20a914 | -7.31073 | -72.76005 | 2024-10-04 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae1b382-71f3-346d-b6a9-256eb14330af | -7.05521 | -71.75823 | 2024-10-04 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef819989-9c3f-3c53-b7af-974bdddadc94 | -7.05466 | -71.76187 | 2024-10-04 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36e63464-595b-395f-b602-8cf8f0d8a40b | -7.00372 | -71.66153 | 2024-10-04 06:14:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eea956a-1600-33d1-8b3f-936edb8e2cc1 | -16.6868 | -57.4741 | 2024-10-04 06:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 7c6dacea-1f3b-3880-a460-a3b59aae2bc2 | -16.6871 | -57.4536 | 2024-10-04 06:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| c8e3650a-7ff8-3b32-b736-92bf7b436457 | -17.1085 | -56.7892 | 2024-10-04 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 2a788219-6c2f-378f-b65e-2540e687fd3e | -17.1378 | -57.4016 | 2024-10-04 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 1d1df61b-71de-3902-9af7-1f1d3d255b66 | -17.1574 | -57.3993 | 2024-10-04 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 96b90113-b5ea-3493-b0fe-1e975645edf1 | -17.1577 | -57.3787 | 2024-10-04 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 8aa70032-89b4-354c-9be7-bdcce199dfdd | -17.1771 | -57.3969 | 2024-10-04 06:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 738fa651-e50e-3b76-a745-ef694dac167d | -16.6871 | -57.4536 | 2024-10-04 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| ebf2e61a-2a64-32cb-8589-f85da75a5e0a | -16.6133 | -57.176 | 2024-10-04 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| d939bd29-689a-3fc4-b316-ce66ad96e9ee | -16.613 | -57.1965 | 2024-10-04 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| c1d49f99-a536-3164-8ffd-9a78af7a4075 | -16.5938 | -57.1783 | 2024-10-04 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| b04bb9a3-041a-34d2-9a69-f585615a208b | -16.5935 | -57.1988 | 2024-10-04 06:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| aaf0e681-6a6a-3273-9496-b4bdd20d71c5 | -16.9283 | -55.8405 | 2024-10-04 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 20033926-1cf5-3ab5-9421-cbf1c0714a18 | -17.1085 | -56.7892 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| 9bb60008-3239-32c2-9cdd-a8a863f90e0b | -17.0113 | -56.7392 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| a434405b-2327-30d6-962d-a1a87908eb39 | -17.011 | -56.7598 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 6e6349ed-200c-39ce-88c3-f464a9d82761 | -17.0106 | -56.7804 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 0b0efc58-ee5e-3a8b-a590-54e058f555ad | -16.9913 | -56.7622 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |


[Clique aqui para ver as próximas entradas](README182.md)
