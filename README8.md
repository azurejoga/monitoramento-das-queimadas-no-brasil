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
| 51c3c605-c40a-37f3-8e44-6d343491a971 | -4.40902 | -43.12244 | 2025-11-12 03:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd255116-7044-3fb6-8137-2c0092684b52 | -7.12763 | -41.86777 | 2025-11-12 03:42:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 96c7517a-a8d2-3dab-be53-ec0bc52f9deb | -3.93299 | -43.47843 | 2025-11-12 03:42:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe355a84-e779-3123-92c9-2af4135d7a4b | -6.47143 | -43.5377 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2775c4c-6a15-3b2c-9d21-d952cec4f001 | -4.91123 | -44.32061 | 2025-11-12 03:42:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2541fb-41e9-33a3-afea-3c68e3e7e4e1 | -4.5197 | -40.36292 | 2025-11-12 03:42:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc491746-4d69-398d-b246-1ddd6939e3b6 | -3.98358 | -47.30353 | 2025-11-12 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d98026d8-d504-3516-b357-9d0654cc5f9d | -7.27641 | -41.58057 | 2025-11-12 03:42:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbb68559-ac8f-3754-935b-4dcd372df87e | -6.47594 | -43.54153 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76b2dca6-d9e4-3399-86c6-d5085b1eddf5 | -3.97699 | -47.30196 | 2025-11-12 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1077a6cf-507b-342d-86bf-adeea2943e5d | -6.31246 | -43.8121 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ab64135-f85e-35ab-8a36-54b0657f5f5c | -4.72685 | -42.82367 | 2025-11-12 03:42:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f82364fe-5ae7-3df0-8f86-db89aecfb402 | -5.01329 | -44.09427 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc755d12-1196-34c8-8f99-61f9e1d0f52d | -6.98451 | -41.28323 | 2025-11-12 03:42:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59825959-ab7f-36f2-b7fd-866f73d36504 | -5.651 | -39.88572 | 2025-11-12 03:42:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 447c5c2f-327e-3ae3-921b-49bf402fe7d2 | -4.64058 | -47.95788 | 2025-11-12 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a265819-8d16-3a28-8989-52d8f0bfe249 | -7.50032 | -41.23947 | 2025-11-12 03:42:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6acaee0b-109b-3a65-a03c-85e4331c60ed | -6.51272 | -35.21056 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca3f8eb6-e4c3-3165-9d03-87aff5a1de26 | -7.45227 | -44.75214 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 279d196d-2f88-3f30-b580-6307ef85fddb | -6.50942 | -35.21004 | 2025-11-12 03:42:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bda4978a-9dad-3f9d-9bcb-e7165645dc5b | -6.48046 | -43.54533 | 2025-11-12 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1f04df8-5229-3ba8-9d1d-db4cecff2477 | -6.61234 | -42.07133 | 2025-11-12 03:42:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b524a90e-3cda-3580-b618-441875cfef4c | -4.98401 | -37.99863 | 2025-11-12 03:42:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c000f5cc-2f51-30c0-bb03-544b0acd0e65 | -3.87916 | -42.2254 | 2025-11-12 03:42:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85323941-f396-30b1-9258-5836d2ef79fd | -5.21833 | -38.58966 | 2025-11-12 03:42:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aa85b506-2a35-38c3-89cc-d8180d5457fb | -7.10864 | -40.21052 | 2025-11-12 03:42:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45cf5575-f2ad-384d-b98f-9cf2eaac8874 | -9.84159 | -36.03374 | 2025-11-12 03:42:00 | NOAA-20 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cdc675ac-a24b-36be-b0c1-7bdaa4f81303 | -9.05188 | -38.93517 | 2025-11-12 03:42:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9f2b229-8030-39b0-8813-1e9b3768d083 | -9.96035 | -36.29269 | 2025-11-12 03:42:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 345f8acf-d123-30e3-89f1-f1f1b341a57c | -9.66467 | -43.89765 | 2025-11-12 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83230f2e-ae15-3ec2-a048-16d3ba30ba0c | -5.75071 | -35.32254 | 2025-11-12 03:42:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97d9282f-d022-3c83-b288-2c68e8079a39 | -7.08215 | -41.5791 | 2025-11-12 03:42:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 91c5fd6c-277d-308f-b52c-6b728c277c58 | -4.93361 | -44.29623 | 2025-11-12 03:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac836801-c66e-387b-8d77-ea9f6333bc41 | -7.11206 | -40.2146 | 2025-11-12 03:42:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5569fd1d-167a-3669-a68e-59d1cbc283eb | -7.69203 | -36.38568 | 2025-11-12 03:42:00 | NOAA-20 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92d9432f-35bf-36a7-a3c6-29283b066d9e | -6.67838 | -42.01328 | 2025-11-12 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2e3e4568-6231-3231-aa2b-02708898d217 | -7.09415 | -40.44675 | 2025-11-12 03:42:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b7087ac8-310e-31fc-b027-a55fe09bd3f7 | -4.64839 | -47.95376 | 2025-11-12 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1972380-41b3-34c8-8885-87038cf22c3c | -4.09643 | -48.02339 | 2025-11-12 03:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 28817ceb-e9f1-34ec-be16-f5adf34a0864 | -5.22575 | -38.59088 | 2025-11-12 03:42:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7727a7ed-c6db-39b1-8719-8e001d52f1d6 | -7.834 | -41.75293 | 2025-11-12 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4822fb53-871b-3ff3-b66c-4f8b6a4516aa | -5.64289 | -45.98746 | 2025-11-12 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b51b8994-5497-3c20-9184-428ffe251620 | -3.96215 | -43.78094 | 2025-11-12 03:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbfab9e3-fcc1-32a3-a6dd-6bb69c1ad9a6 | -7.83328 | -41.75719 | 2025-11-12 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5148d5dd-2624-3564-951a-f4e6d213b815 | -4.31215 | -43.05812 | 2025-11-12 03:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63748212-3637-324d-9171-6a7fb9b89881 | -6.99766 | -42.78788 | 2025-11-12 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cd8ea686-ded1-36b8-9596-738d7dfd0ccb | -7.45766 | -44.75293 | 2025-11-12 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe54f936-b1f1-3933-bd8f-5b3998d6732b | -8.9215 | -35.4048 | 2025-11-12 03:42:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f206f2b7-dd6c-3a60-b4e4-4c801d78f408 | -8.51178 | -36.19103 | 2025-11-12 03:42:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3cf53df4-d786-30fa-9317-41884b4dc85f | -5.6489 | -45.98838 | 2025-11-12 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0541ee4d-7363-3d3f-a074-4e50983daffc | -7.47417 | -42.56268 | 2025-11-12 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6535841c-13e8-3028-8b3d-b3a3396f3b28 | -17.13103 | -44.65327 | 2025-11-12 03:44:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b5f96f1-7195-3024-8792-cf475fc4d7f3 | -10.45124 | -44.96798 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5e09956-68c9-38c5-8de7-2885ddfd5520 | -14.23145 | -43.53794 | 2025-11-12 03:44:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb144460-e2e4-3a58-a5d7-b674bb8d6bba | -12.94016 | -43.79891 | 2025-11-12 03:44:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08af8cff-50f4-353f-80f0-c57c1ddd9869 | -10.59885 | -44.89986 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8fa6884a-b287-31c6-80a6-437d97713d3b | -10.55246 | -44.8363 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 38354edb-b0b6-300e-a6e8-efb9ea7596e7 | -16.2908 | -43.83107 | 2025-11-12 03:44:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c12aa26b-51c6-3074-8d18-8f48ca694d28 | -10.49444 | -44.93698 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d44610c3-771d-3f73-a6ee-7ae265695213 | -16.83439 | -46.08946 | 2025-11-12 03:44:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cc8868a-6d41-3d42-8085-c493920271b5 | -10.49901 | -44.94108 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d4e02d3-862c-3587-82d0-ad95ca993349 | -13.16355 | -42.958 | 2025-11-12 03:44:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1eeb12c5-e029-3d31-92ab-fbb48aadfb44 | -10.50417 | -44.94204 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 00a17fa7-acea-3eca-8e49-1010c99484ad | -10.32701 | -44.27613 | 2025-11-12 03:44:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64c75259-e1f7-3508-9329-23ae9c0c17a3 | -10.49784 | -44.94743 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3993b9b1-c3c2-3e15-afba-e7e946031767 | -13.33216 | -43.1785 | 2025-11-12 03:44:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5d4dd55-2b4f-310a-842c-43d28efc774f | -11.00251 | -38.32237 | 2025-11-12 03:44:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| caeb9d68-6f29-3c49-bfed-5721048c28e5 | -13.45462 | -44.41863 | 2025-11-12 03:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5be0d06e-0bb9-3635-959e-ca3934fbf6dd | -14.01178 | -44.08393 | 2025-11-12 03:44:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b94c8ef-0094-348a-9deb-eab0bb40c15d | -10.49267 | -44.94649 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d725f5da-850f-3740-abf5-599b63e9dae4 | -11.00595 | -38.32295 | 2025-11-12 03:44:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69ff1204-93a8-3e4d-86b5-242f9097dd33 | -15.29608 | -42.93262 | 2025-11-12 03:44:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 415224d6-21eb-31b0-bdb8-131cd5a04258 | -9.8543 | -47.8754 | 2025-11-12 03:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccc6fb04-6df5-3435-97ce-ac7fdf6c9333 | -10.45064 | -44.97115 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a133720f-5234-3461-87b5-cf35474132e9 | -13.15317 | -44.96276 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bcc3a6a-dec1-3116-bbcb-b6f9ae71963f | -16.45122 | -45.0079 | 2025-11-12 03:44:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5417c6a6-6818-3b3d-9cb1-05569bb5ab72 | -10.19213 | -44.90232 | 2025-11-12 03:44:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17fcf016-d2f5-31e4-8343-ee53a80355c9 | -10.49842 | -44.94426 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4eef74f9-2141-39e3-b0ab-1099e3c41dfa | -11.61896 | -38.05003 | 2025-11-12 03:44:00 | NOAA-20 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9f8f7964-641f-3454-9b72-460e1b720727 | -15.45131 | -43.08437 | 2025-11-12 03:44:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 585cc7d1-8b4a-3016-b5c0-6382b87a50cc | -16.44756 | -45.00183 | 2025-11-12 03:44:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30c4064c-98fe-3ea8-ba07-186cf572ee18 | -10.59946 | -44.89658 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9952d740-fcd6-30b0-ad59-86fca039bb17 | -10.49326 | -44.94332 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 807b84bf-0225-3ecd-b711-624329a0f82b | -13.45608 | -44.41537 | 2025-11-12 03:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 889d800d-4028-344a-bd2f-77f293d99581 | -15.52077 | -43.01217 | 2025-11-12 03:44:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37efb25d-3599-3e85-9c1e-225207868ff6 | -13.872 | -43.49474 | 2025-11-12 03:44:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66786639-05fc-3dba-a6e8-4435cea3779d | -16.44656 | -45.00698 | 2025-11-12 03:44:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da9b493d-15db-317d-b05d-4df514da5659 | -17.70517 | -39.1909 | 2025-11-12 03:44:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13dac68b-d311-3bf2-9f26-98cc727351a1 | -15.51662 | -43.01134 | 2025-11-12 03:44:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6efe9d8b-c1a1-312f-a1d6-548a25e40f2a | -10.50476 | -44.93884 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a96866d3-4370-332a-adff-b1df823459be | -13.15699 | -44.96944 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f530fee-ac6a-3c1f-ae54-e7f6bd3003d2 | -13.45512 | -44.42037 | 2025-11-12 03:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f61a4a-1158-3182-9b69-3121d8241415 | -14.40533 | -44.37989 | 2025-11-12 03:44:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bfd90357-3d1b-3f44-b928-bcb789d3de06 | -10.55094 | -44.83205 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 345a1cf6-9821-3c32-9445-a3c63cc7fea4 | -17.12565 | -44.65697 | 2025-11-12 03:44:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4792ed5f-4859-3e94-a755-08e432d484b6 | -17.12656 | -44.65229 | 2025-11-12 03:44:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3653bd1-6eca-3a59-bcbf-7f1d30d6e044 | -15.51247 | -43.01053 | 2025-11-12 03:44:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e2a81316-88b2-365e-9276-8ec6038ae33a | -17.13012 | -44.65794 | 2025-11-12 03:44:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25820a84-9357-3117-85a2-9931c267ec42 | -10.55604 | -44.8331 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01934431-0cfa-383c-973f-377412102ad4 | -16.83586 | -46.08463 | 2025-11-12 03:44:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README9.md)
