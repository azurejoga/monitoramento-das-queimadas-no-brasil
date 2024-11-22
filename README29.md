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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b58d71f8-968a-3764-a9f0-41bc877cc54e | -10.66082 | -48.11417 | 2024-11-22 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 836d05e3-04c2-356a-a7e3-e0df33340b06 | -7.66832 | -44.50181 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78869fa4-684c-3bfc-ac85-c9681b77a8b2 | -7.28788 | -45.0828 | 2024-11-22 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af4710b7-7bde-3a10-87c7-6786c6b6eab5 | -11.83537 | -44.19497 | 2024-11-22 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cd28cb9-640c-33f9-b581-41761a21af2c | -12.13539 | -40.895 | 2024-11-22 04:14:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29b94ca6-b732-3a09-94cd-0a43faeee832 | -9.35787 | -35.49884 | 2024-11-22 04:14:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9fa75699-8dd5-3a03-b0bc-96daec23ce2d | -10.7076 | -40.5123 | 2024-11-22 04:14:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 288cc44c-857f-38df-821d-ec3bb600a029 | -11.74091 | -47.24208 | 2024-11-22 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cecb106-1e94-3443-a11b-2756f8ba956a | -8.72056 | -44.01711 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edaf194c-f3a8-3326-adb4-9b211fea8cda | -12.18388 | -41.34843 | 2024-11-22 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50628554-d517-370d-a8ae-a4e9d8602186 | -12.44496 | -46.6613 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 875cb623-e2a4-34a9-9933-d3372bb202fd | -8.9271 | -44.25241 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 941e515c-baa1-3929-bcc5-b577f05d54fa | -7.66717 | -44.50896 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f621a52-30e7-344f-931c-b6aca2732bef | -11.87932 | -38.34844 | 2024-11-22 04:14:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85a13c35-df86-3276-832d-a04b3e008ea3 | -12.8327 | -43.89514 | 2024-11-22 04:14:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98c184e0-be92-3fe3-9e9a-61da20839aa6 | -7.65484 | -44.49963 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e223776f-ebd3-3bb7-af7e-12c29055b44a | -8.39353 | -48.05611 | 2024-11-22 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44875ae1-3536-31a1-9e08-35bdba875011 | -12.44525 | -46.66423 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cb37410-d7b2-3b20-a33f-d67f83842056 | -11.88524 | -44.22095 | 2024-11-22 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb0b48b0-ca7b-333c-bab1-d21abc964f26 | -12.83325 | -43.89158 | 2024-11-22 04:14:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 485f2a9f-3be9-32bf-91bf-f57dc2484cea | -12.18745 | -41.34906 | 2024-11-22 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15be2fe9-ba92-3c88-8da3-69e932951fb8 | -7.71249 | -45.66128 | 2024-11-22 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5740a80c-70ae-3fe5-a584-cc0f023c8fc5 | -8.87142 | -40.77951 | 2024-11-22 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 14219b0d-d41d-3d4d-8f97-cc248a10eb54 | -12.85485 | -43.81844 | 2024-11-22 04:14:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac53ea46-03cb-3d24-b62e-f167c3425ec1 | -7.28885 | -45.08371 | 2024-11-22 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e3e3ad2-fc44-3880-81f3-03898b0dd507 | -9.29751 | -43.12423 | 2024-11-22 04:14:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 749ac71e-d2d6-36ff-a3ce-a368d2a9987f | -7.65148 | -44.49908 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6e4a80f-9d6e-393e-88a3-2dfcc78e367b | -10.73272 | -49.53905 | 2024-11-22 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f78dfabb-7bcd-37b8-ae20-6ef4e37ae739 | -7.64754 | -44.50211 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a60cff47-c271-3786-9319-931e5c35cb09 | -7.59792 | -45.26289 | 2024-11-22 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cbb292b-4887-32ec-8ef7-3879454580bc | -8.71224 | -44.00498 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82059139-1b61-3167-a371-6d2a182e5fac | -10.96779 | -37.1815 | 2024-11-22 04:14:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a8e0444-58ec-3118-9b6b-341853679b3c | -11.74162 | -47.23792 | 2024-11-22 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1da5a371-c0a3-3731-a839-1cb54c7f9d91 | -14.44494 | -50.00598 | 2024-11-22 04:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e3c955b-4ffd-3053-aefa-ed7d97a9fc18 | -21.60314 | -43.00058 | 2024-11-22 04:16:00 | NPP-375D | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1aac6ac5-fdc1-370f-bc11-de9fe3e841eb | -16.26781 | -45.06934 | 2024-11-22 04:16:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 961840fc-b4d1-3266-b045-20fdd860be6e | -15.64643 | -46.2299 | 2024-11-22 04:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5519b069-514b-351a-95a3-e11277259493 | -14.44558 | -50.00237 | 2024-11-22 04:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6d03ac1-76c1-30a0-95ee-60c31deb9c3a | -24.58985 | -52.82052 | 2024-11-22 04:18:00 | NPP-375D | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e5aeabef-24d2-33e9-877d-7a30913849ec | -3.2201 | -54.2436 | 2024-11-22 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 3660b777-d75f-3c82-907f-23bc877b2563 | -3.2768 | -53.8199 | 2024-11-22 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 13da0479-cbbb-3b49-9242-2d4b17a0e57d | -4.0131 | -49.9207 | 2024-11-22 04:20:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 82337278-c702-3654-92d7-bf5dae0c0d95 | -3.2384 | -54.2632 | 2024-11-22 04:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 983d76e2-625c-3309-b149-5ccc2f4effbc | -1.1287 | -53.3951 | 2024-11-22 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 211f8ec8-eb65-3b48-a7e1-e7e929269d55 | -3.2385 | -54.2431 | 2024-11-22 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 9462bdd6-cf09-3773-ad29-7d655dc43d5c | -1.2041 | -51.9478 | 2024-11-22 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a0b1d317-28b4-381f-a849-974dfa1a78a7 | -13.2553 | -50.8807 | 2024-11-22 04:20:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 20e1fbf6-8cf5-3a39-9cad-5658955ee04f | -3.22 | -54.2636 | 2024-11-22 04:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6e3493a4-8058-3783-8a86-6a591f5e6ae7 | -2.3549 | -48.5493 | 2024-11-22 04:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| ccaa02fb-7617-35f0-b351-74b3586766de | -3.2386 | -54.223 | 2024-11-22 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f590068c-49b4-3748-ba04-31b3f51439a4 | -3.2569 | -54.2426 | 2024-11-22 04:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a9ad4152-29b7-3e42-8079-babeb5e1b403 | -9.35705 | -35.49584 | 2024-11-22 04:23:00 | AQUA_M-M | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 557be215-0c48-3f29-93cb-eb774dbef614 | -3.2201 | -54.2436 | 2024-11-22 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 086c858e-f21d-33f9-8092-fbb99f99f1cb | -1.2041 | -51.9478 | 2024-11-22 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 304f1410-9777-38dd-ab5c-7d22a0bfb626 | -1.1287 | -53.3951 | 2024-11-22 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a63ea396-54f2-39b1-8ace-cdff124b9901 | -3.8535 | -52.3596 | 2024-11-22 04:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c48817dc-6d58-3669-87a8-118458841ca0 | -3.2569 | -54.2426 | 2024-11-22 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b97deb78-76eb-34cd-8747-62656f62ad72 | -3.516 | -53.793 | 2024-11-22 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 658f557f-27e1-3e91-93d5-24b59c972c3f | -3.2768 | -53.8199 | 2024-11-22 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 40de7b57-1103-3558-a131-c88735ac0310 | -3.8355 | -52.2576 | 2024-11-22 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4bf6afcf-3b21-3eac-a584-222b36368c80 | -13.2553 | -50.8807 | 2024-11-22 04:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d15c18bf-23bd-38be-b324-c61960c86564 | -3.22 | -54.2636 | 2024-11-22 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0e1044b5-6681-3d8a-90e4-d51e11e042e4 | -3.2386 | -54.223 | 2024-11-22 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1767c1cb-168e-3f7f-8952-d7cecd31b90b | -3.2385 | -54.2431 | 2024-11-22 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 195.5 |
| e4792225-e823-36bc-8bf5-783d6aec05f3 | -13.2549 | -50.9022 | 2024-11-22 04:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 302ac302-4bed-3596-96c5-0cb0b20ed603 | -3.2384 | -54.2632 | 2024-11-22 04:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 2031173c-ee3a-3b4f-b5e8-f2200ae8e499 | 1.37705 | -55.95343 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84775812-9d89-3379-8d63-cf1a2a74a486 | 2.38234 | -50.76823 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3fa9c7dc-023b-3769-8323-09dd6cb81f49 | 2.37804 | -50.76454 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4880a63-3a94-33aa-aa16-93613c051451 | 3.68271 | -51.39007 | 2024-11-22 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4aa3f0b-4ba1-3d68-9079-a93d211e30ab | 1.40788 | -55.91861 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d43dbc71-c092-30c2-bf0f-fbb160380a67 | 1.37006 | -55.97568 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5487a449-6488-321e-a70e-c2845aad1fe1 | 1.40615 | -56.04279 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9717d4dd-d076-3bc9-8a75-52a72442504c | 2.38168 | -50.76398 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3e67dc5-186b-3f82-8b01-1251c69cc877 | 1.37244 | -55.95718 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a90b4a71-3f41-3ac9-9362-d171594d11ab | 1.4057 | -56.03982 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a5164ff-2501-38b2-b6b8-bf932de0baac | 3.68002 | -51.38834 | 2024-11-22 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0819586f-f1e1-351b-83b0-1f213cdf993f | 2.18349 | -50.90853 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a78d7c1-ff0e-324e-a438-4f419de66581 | 2.34102 | -51.64871 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a72c2c2d-5ddb-38e8-92d5-e33424358827 | 1.3766 | -55.95049 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31aaec01-06dd-3d92-b13c-44b924ebd01d | 1.40374 | -55.92527 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b585921-4de8-3798-96b2-f3829639cdf0 | 2.3372 | -51.64933 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84b56df9-8bfb-3ad7-85f3-e8f0b58d484b | 0.98501 | -50.06909 | 2024-11-22 04:33:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1abf44d9-b098-3b4f-a0e1-a7cb5733674d | 1.3858 | -55.94304 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb2c2705-9c33-3428-bda8-f41087b58ae7 | 0.57515 | -50.81356 | 2024-11-22 04:33:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4705bc74-a35a-3536-9995-cbcab438b306 | 1.3812 | -55.94674 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be9f1bf1-079b-377d-8814-82dd4419070e | 1.40329 | -55.92233 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51a63f2a-2e0c-3e0d-9fef-92caf40d2690 | 2.37506 | -50.76934 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c55b220-6e42-3b52-8784-9ad5283c5758 | 2.37208 | -50.77414 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57d7007e-4dba-38da-afa7-a79f29e90752 | 1.37422 | -55.96898 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36a335a2-d9a0-3922-9e18-0042a0589b7b | 0.85091 | -51.40768 | 2024-11-22 04:33:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad7c9c3e-5ca6-3822-af7e-d6c4f12002ae | 1.37511 | -55.97488 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15e4b2bf-9c41-38ee-8dbb-08dcb6d32753 | 2.37274 | -50.77838 | 2024-11-22 04:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae15242a-599f-3bba-9b72-84b5ed7140fc | 0.98443 | -50.06527 | 2024-11-22 04:33:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd030ce-c94d-32f3-81bd-062b2bd61438 | 1.37467 | -55.97193 | 2024-11-22 04:33:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 525f5518-e0cf-3c61-b54d-a8f8cac47543 | 0.98653 | -50.06814 | 2024-11-22 04:33:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ddba1b6-23c5-38c6-a3b0-43c6e3496126 | -2.99055 | -53.44447 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c1e548f-1e04-35f9-9f70-3b770540ca2f | -1.2513 | -51.75259 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39851f6f-e00d-3aa7-ad56-97d0a0dcb237 | -3.46414 | -45.90659 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2cd961b6-bc22-34bd-ad6e-5060289b468b | -1.92066 | -52.08735 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
