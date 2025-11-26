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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c35f52-6b11-374f-b246-eb0b4b8bb597 | -3.51425 | -43.68925 | 2025-11-26 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 43b2dc53-aac7-3770-a889-4fbab0813f29 | -3.51 | -43.69621 | 2025-11-26 00:13:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0b3d26a-731a-3a28-8fee-8ab7e1cccd81 | -1.51121 | -46.75782 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d4a46502-427c-3c67-9ba0-b856112178f9 | -1.67141 | -46.24249 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e1c6d1cd-3836-3924-88d6-6923bf748c43 | -1.51243 | -46.76661 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1cbb1eaa-f981-38c2-abbc-ab6490336144 | -1.21691 | -46.88874 | 2025-11-26 00:15:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2b65d44-a66f-38ef-a163-3509d2e46a47 | -2.78422 | -52.94841 | 2025-11-26 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ee732ccd-152c-3519-a7e0-e05873bfb8fd | -1.28141 | -46.3636 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e3022e4-532d-3675-a4d8-bb7aedd1305d | -2.41205 | -49.35138 | 2025-11-26 00:15:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7c26b0a8-8411-3d3e-93b6-af7f3704c654 | -1.45854 | -46.70244 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4df5a8b7-3d5c-30e1-9874-4fcd72855648 | -2.78709 | -52.96996 | 2025-11-26 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| eb9b651e-a649-3dee-b00f-600826b45efe | -1.45733 | -46.69365 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f563888-0ca6-34a9-bd25-53012b281b4f | -1.67019 | -46.23371 | 2025-11-26 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 61958948-85db-3c36-b533-7d6666ce62f8 | 1.32413 | -50.85526 | 2025-11-26 00:17:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53915b89-47ce-36bf-9463-6064035e2e0e | -3.47071 | -43.42828 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc29c5bd-1841-37c0-9165-940ebdd0d183 | -4.17472 | -43.7244 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cbf299d3-9ddc-3c60-822e-aa0150d525e6 | -4.56899 | -43.80013 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e516c135-b7e5-3074-83cd-691f9f32929d | -5.24824 | -37.40954 | 2025-11-26 03:27:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1699a27-b06f-38bd-a6e3-62a873099580 | -4.25354 | -45.13467 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37d288df-1cce-3b52-aaa1-4a6a68f1fa78 | -4.61885 | -41.06251 | 2025-11-26 03:27:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e11df7e3-cb09-3ff7-9dd5-cec13a76e870 | -4.70767 | -43.9974 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86bd01ae-58c9-37ce-b986-ea5230605787 | -4.1698 | -43.71381 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 025478f7-52e3-3908-8099-2e6935a1745c | -3.47626 | -43.43466 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdb9aa2d-7464-37bf-8c91-3c5a809ed239 | -5.96541 | -35.19021 | 2025-11-26 03:27:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 506e9b2b-2ad8-3d51-a619-c6c96f43dfe6 | -4.23659 | -40.39004 | 2025-11-26 03:27:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 184fd0ed-20af-3499-8910-0df6eceb935c | -5.60751 | -35.63381 | 2025-11-26 03:27:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ed472954-31db-32e7-ba8c-53a64a0e387d | -4.17373 | -43.72989 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ee2362f5-2a9d-3d7e-8206-d2c95184724a | -4.18022 | -43.73101 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 976ac255-b8c3-383e-935a-6c3c9505edc8 | -3.67278 | -43.57432 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68653ead-7194-3975-82d3-59e65811c8dd | -4.16886 | -43.71919 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 645c3eae-6638-3245-b268-12c18da50c64 | -4.17631 | -43.71479 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 13c72ba2-b16d-39f3-a82e-95ca355bcd3a | -4.16522 | -43.73999 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9839a3c8-509a-395b-b047-ca4d345b89e8 | -4.60252 | -44.41293 | 2025-11-26 03:27:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 250aadd1-e492-3a19-9c03-6af2c365939a | -4.26889 | -45.13003 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d53aaf90-104f-3f92-8486-4775fcad36ca | -4.27013 | -45.12322 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 084e6a6f-6dde-37b3-a210-1f35560fbd10 | -3.47716 | -43.42936 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d39189c6-cd01-35c6-85c9-2c28ed5ae25c | -4.17015 | -43.71263 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7ddb9398-008a-32fe-a294-15958f356cf9 | -4.55579 | -43.30186 | 2025-11-26 03:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8feb39d-4822-3fb1-ac3f-3a9f420e2a19 | -5.17596 | -35.70664 | 2025-11-26 03:27:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 361de3fa-0171-3152-8d81-ae42d6b3fc52 | -4.66511 | -43.97694 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d83ea1a4-9f39-3984-8c35-1b80da2cc39f | -4.16721 | -43.72894 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 142dc171-d73e-37b7-ba94-f6a2ef9177e3 | -4.18092 | -43.7268 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d48b64f-01b7-3eaa-8d89-29c24ec3389f | -4.25784 | -45.12427 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0c530502-78f6-3dd4-a984-10efdae10fb2 | -4.14782 | -43.64857 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b90a08b9-f5ac-3465-868a-1196b58fd14e | -4.17537 | -43.72018 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d0d0e90b-cf94-368e-bc89-c8e313655b90 | -3.67446 | -43.56545 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3bdfc6f-ffac-3d60-a105-460f90275b44 | -5.9648 | -35.19069 | 2025-11-26 03:27:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0679a95b-7340-3749-a5b6-38c8cd101cca | -4.17667 | -43.71357 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7858d737-09e1-30df-96e9-d6f26f5e609c | -4.1711 | -43.70735 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ab88c4-a0f1-3cb7-a568-1577d9083328 | -4.17443 | -43.72565 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f593e0bd-3364-3c53-9b85-2265eb9fc112 | -4.4533 | -44.30084 | 2025-11-26 03:27:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e97c9577-c4f8-3342-869c-340a3ff73e6c | -4.5638 | -43.29306 | 2025-11-26 03:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 380fa8f0-f638-3925-9c2b-ebbfb576d349 | -4.61398 | -41.05818 | 2025-11-26 03:27:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3935e200-150c-3805-9a61-b8b620e26e80 | -4.56295 | -43.29798 | 2025-11-26 03:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5a17c51d-bd21-366e-8d9a-7f86ea9ced2b | -3.47154 | -43.4277 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51f2b550-70ad-3b9b-afda-658b15aeea3d | -4.26489 | -45.12541 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f9ec841-42f1-3dcb-be7f-abecf2ea9e47 | -4.45223 | -44.30682 | 2025-11-26 03:27:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2add318-3b0b-3c86-b08f-084f6e069cf7 | -3.67372 | -43.56879 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db0f145a-7fbf-3d67-8891-5788b607c308 | -4.59478 | -44.41759 | 2025-11-26 03:27:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7559ab40-a4be-3ebe-81ad-f3e56318abfc | -4.16233 | -43.71834 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1a037a4-cfb2-362e-915e-5bbb7fa02434 | -5.55194 | -38.14489 | 2025-11-26 03:27:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 968f95b0-d0e9-3d42-a23d-2f47c49f161c | -4.70864 | -43.99197 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b12989a-743a-3d1a-9d26-f26d6b48373d | -3.67462 | -43.56351 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52254e07-b98a-3c57-bb56-ea35272f445a | -4.1682 | -43.72344 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 04d4bbf5-3f53-387a-8fb7-a978a65a2369 | -4.17157 | -43.74218 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 998c7786-8a3e-35a4-84fc-d0933617476d | -4.17997 | -43.7323 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d53e663-7249-380e-abb1-6fb9ff12c12b | -4.65628 | -43.9831 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6fa567d1-0a6e-321e-b74d-9318cc879f91 | -5.60303 | -35.6377 | 2025-11-26 03:27:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 04493a35-9934-38a7-a70f-bbca31381430 | -4.17174 | -43.74092 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 54fe8e89-9d9b-3787-820e-1a8a3242d439 | -4.65761 | -43.9813 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97ac9793-7d2b-3b47-adf7-50567d531e10 | -4.59833 | -44.41359 | 2025-11-26 03:27:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 771d6790-73e6-396a-a00b-274ecdfcdaaf | -3.67351 | -43.57081 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d07e272d-dc24-34b3-a70a-cb57c3dbd164 | -4.16791 | -43.72467 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a1e10df1-6e37-32d2-8342-b840b61800ae | -4.1812 | -43.72552 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6cb6ae6-fd62-3656-9760-dfdf8623d3b7 | -4.65857 | -43.9758 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d35eefe-fa66-3696-bd82-c261e78cd96c | -4.26058 | -45.13585 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8013e16f-a03c-3807-bb9f-e67704b8e221 | -3.66797 | -43.56441 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d2a1226-e5cc-36df-a565-47662101c320 | -3.47705 | -43.43405 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b60af23-1f3e-3c8c-a4b6-630fdf26282e | -4.56805 | -43.80546 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2825f7b7-d24f-3d73-a0d7-80a641cbed94 | -5.20163 | -38.46497 | 2025-11-26 03:27:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 53dd6b31-2b3e-3fec-8791-72237f421f49 | -5.80576 | -35.58842 | 2025-11-26 03:27:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7277fa0c-51ee-311c-b465-27643f33acc4 | -4.1757 | -43.71896 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 80b7340c-c7e4-300b-a159-99ca1eca5adb | -4.16044 | -43.72921 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40635dfb-62bc-3fb0-b274-ad267ccd680d | -4.16505 | -43.74123 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7e1b0d34-dad8-3e38-ac0f-d3ab4e066870 | -4.652 | -43.97483 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29ed3b36-f796-366b-b864-4996bbab01cc | -4.99506 | -40.78489 | 2025-11-26 03:27:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8249d32d-7887-3c3b-946c-da05eba7d08f | -4.17273 | -43.73543 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7517ac15-e882-3f10-b09d-13ce759237f8 | -4.17724 | -43.70942 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35e9dfd4-6d93-330f-b915-885ad6c044e4 | -4.25479 | -45.1278 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f0aad3a-42dd-3f7b-89a6-52949d698387 | -4.59584 | -44.41158 | 2025-11-26 03:27:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 517579bc-1543-3423-8fe5-33d92a29a072 | -4.25543 | -45.13802 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 85f06fe0-9479-30a9-b0a5-6e6af6ddda12 | -3.67059 | -38.80843 | 2025-11-26 03:27:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 73194517-5204-388c-90c9-390dff9cfc7f | -3.68022 | -43.56979 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18b0bf66-2e10-362a-bec8-97b4454731e9 | -3.14467 | -40.17951 | 2025-11-26 03:27:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1834dd8-c42a-3575-8bda-f40382b18854 | -3.66722 | -43.56782 | 2025-11-26 03:27:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b4c3057-29c3-38cc-8257-052368e9c5d0 | -4.56629 | -43.29847 | 2025-11-26 03:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5aa618e3-50c8-3473-a732-33ddab0719cd | -4.26185 | -45.12887 | 2025-11-26 03:27:00 | NOAA-21 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c872289-d259-34f1-a975-07109f0f93f7 | -4.16621 | -43.73447 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9c1ed5df-8220-3886-b517-f1e70595e1b8 | -4.16918 | -43.71798 | 2025-11-26 03:27:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 84db9e86-8128-357f-8f40-c198f128c0f0 | -4.66384 | -43.97862 | 2025-11-26 03:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README6.md)
