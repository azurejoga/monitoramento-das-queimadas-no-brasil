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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edc7b0e0-ec00-330d-b5d4-df7dd8b43371 | -6.7737 | -56.41973 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e067c29-a360-3730-80b9-20650ea9d390 | -10.88586 | -45.31437 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c959700c-4788-33b4-bfce-5f4e798021de | -7.344 | -55.20606 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f33a848-ffd7-34ec-9b76-9420a0e94b2c | -6.31103 | -56.04243 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 431aa2c5-a01e-37fb-b56f-0e1a322e7e6d | -6.76995 | -59.43789 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c444f0-8657-3a06-bb0b-b7c4745307cd | -12.09007 | -47.06157 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a04f0fbf-9d53-35fb-b8d8-13a68bf4dba9 | -8.34475 | -50.79247 | 2026-09-03 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbf7d9ae-dfa3-36da-91e1-90d9d2302dec | -5.55334 | -60.2297 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc0891f4-b33b-3d9c-8778-2b4fd263b596 | -4.47434 | -55.40351 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9715f6a5-498d-302e-b1e0-1eacd7c73ae7 | -6.7603 | -59.44082 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab9cbabf-3f21-32fb-a858-ce629a0658ae | -6.43468 | -48.5347 | 2026-09-03 04:57:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ff351ee-d3e1-31ef-b95d-b1b98a6f7664 | -11.32369 | -50.52564 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a57f2255-962c-3f66-b234-39eab3d0e34f | -11.00153 | -45.08735 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf2a4324-cad8-3082-8688-371202475155 | -5.75017 | -51.65561 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35ba69a2-1695-3080-933c-dade77bbafbc | -8.25982 | -54.94661 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edd52ca7-62e6-3c54-ac8b-d28770dab114 | -8.46585 | -44.69447 | 2026-09-03 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4d863f4-6ef2-36c5-bd2a-02ba18fffb41 | -7.34056 | -55.20546 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5cce3bd-d45d-3a97-9f37-a1bba2cde598 | -6.80273 | -59.00948 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53bc733-ac6d-3ce2-9da9-69460f1385a7 | -8.43901 | -54.74683 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cefac1a6-b961-3c52-898c-9d8ee215bb3b | -8.42857 | -54.70422 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5df7e76c-a908-3744-ae36-697b335ad12c | -7.29359 | -60.62856 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9539cd0-9af8-3cb9-901d-5afdfefb2511 | -6.3198 | -56.0569 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b520be9f-aae5-33fc-852c-052d0545578c | -11.31814 | -50.53807 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9b85944-2e78-3150-bd7d-1dcf343ac989 | -6.75942 | -44.56697 | 2026-09-03 04:57:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 061fb678-0c57-344f-b00e-8915aab97311 | -8.08782 | -50.96346 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85934d9e-cf7b-3315-9a57-08d7b296c2c6 | -6.14508 | -55.66515 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b4f483-8293-391c-ab9e-bbda8c837902 | -8.078 | -50.95803 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93632ba6-e6f3-3db4-9f43-833cce0d7659 | -9.62009 | -54.30877 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da684b08-e273-3508-9a0e-1016805d2784 | -8.44322 | -54.69918 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b12ea9c-c460-3890-9ba3-c7ebc8bfbe11 | -9.6295 | -54.31393 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c970c737-0a06-3dfe-8f92-ef85f54956ee | -6.64657 | -59.44607 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 78c33698-6742-3602-ac9a-5780aabc13b1 | -5.85224 | -57.55609 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31102bd5-67fe-3136-ab33-e48012d883e3 | -4.94132 | -55.80165 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4d5e6c7-8692-3c72-b54c-ef80bce89c4a | -5.50607 | -60.18933 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2dc364-6e10-31fc-b90f-2d83b21e2cf5 | -7.05587 | -59.22045 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d0fe6f-7848-3e4e-9280-57e99565142e | -7.66826 | -62.54621 | 2026-09-03 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2972288b-245c-3a90-81de-d09afaed6f72 | -7.07893 | -56.51707 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4c96274-9ef2-3414-9abe-cab6dfbd93c8 | -8.44576 | -54.74794 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30639756-28cd-3632-9ceb-6ca91353a545 | -8.45054 | -54.69666 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b1116cd-5363-3551-926d-6c1a6810a37e | -6.63501 | -55.23626 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7478d0f-fbb8-34b9-8bb6-830cc0ea5d4d | -6.88 | -59.40162 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b8de23-6f4a-34ec-9c5e-5d0d53d2941e | -10.88115 | -45.31069 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 910232ac-b383-3f67-8adc-db8e9e73859b | -3.39075 | -59.36113 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988d4bea-b6ce-3381-9d4e-9d4fcc90be31 | -11.31726 | -45.12348 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23a2d58c-3b13-3371-a999-99b97de6bc30 | -7.12509 | -42.22817 | 2026-09-03 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 41bd96f1-b30d-337b-8f29-3ac7ce58e694 | -5.60052 | -60.24049 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d12397b-2462-3154-85a3-ca2df13e73d6 | -8.46644 | -54.66226 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5ebd16-10f3-3e9d-8434-a6747301cf76 | -8.46971 | -54.67395 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d91a19f5-6901-3e63-9eaa-c740f3631595 | -6.81279 | -59.00263 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9d3b17d-baeb-33e7-a416-ec7e8ed9b5bd | -10.47968 | -51.32268 | 2026-09-03 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1acf85f-5328-3bfe-97e8-6758065cafd9 | -12.08547 | -47.0609 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72febc1f-ed07-38e1-9235-342286b0ac5b | -5.37454 | -51.12408 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e799e013-bc45-34db-b9dd-612275517337 | -6.52683 | -55.24227 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25752c87-8808-33aa-8ab4-128e00909647 | -8.4675 | -54.67718 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cd68a4f-9300-325b-a876-1c0fd5051a6e | -6.61798 | -55.25327 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73e0ba3a-58ef-3ed3-b8e0-3ad017fcd08a | -3.11665 | -61.19007 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efaeb572-6453-3fd9-b767-6072f58cc089 | -3.61535 | -60.56434 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6082a8bc-3a52-3d10-88ad-14bd59ecb89d | -5.45896 | -60.06295 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b20a6a30-68fc-3bbf-b0fa-c374aa30f34d | -6.62172 | -55.23007 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dda1e409-e748-3c5f-bfee-2f50ae6e0a0d | -7.29599 | -52.36422 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f69c5d8b-d89e-3c67-af26-b5037390d99d | -3.75079 | -59.31831 | 2026-09-03 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b814de09-31e3-38c3-b2b3-14e810e6ce60 | -6.77311 | -56.4178 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0232cf0b-0ec8-35fc-a5bf-d5d7d56109de | -7.1245 | -42.23251 | 2026-09-03 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6834da15-54a4-3618-80f2-7179ca6a6f11 | -7.61658 | -57.61302 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 719945ca-0659-3c71-991d-2a3ca7bc1e0b | -7.58763 | -57.68966 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc6e5cb-bf50-315d-95eb-aa6cb5a0e647 | -8.43401 | -54.73487 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e3a4f6c-f613-3d0b-b421-c621d2dfd9ed | -7.28976 | -60.62231 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbe54d1-d34d-3bcb-a7b7-527ca0d8cd51 | -7.08028 | -56.51423 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a943f941-b7af-315e-a660-98f42facb00d | -8.44634 | -54.74433 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c1bdbdc-d98b-3bdf-8486-b9ab33d1c2b0 | -10.48261 | -51.3269 | 2026-09-03 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e447eb8e-4697-3c3a-a8a7-2ce164dfb2fe | -8.43343 | -54.73848 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c06b3d-eb1f-3f7e-8eca-bd3d7747bb34 | -6.70268 | -55.4023 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b02fac15-d913-3c12-b9c8-47621fa997b4 | -6.4192 | -56.18031 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4ccda73-4a9e-32b4-9eee-f93f71721bbb | -12.08922 | -47.06355 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52300fc4-fc07-31df-83d6-ee590e8d0911 | -4.9751 | -55.84652 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70d7329b-e4ef-3ced-a234-d0c877137a1d | -11.28645 | -54.06503 | 2026-09-03 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb2e6c2b-7e32-3e07-a059-a061ee86a879 | -8.46692 | -54.68078 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c61749c2-26b6-358d-a9fb-fa3c9c54b7f1 | -5.98355 | -55.70435 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2be2a5c0-57b1-372f-a5e7-36cea55c8ed4 | -8.43648 | -54.69809 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3df81374-2559-3d25-af15-14de3b684617 | -5.76286 | -53.40054 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c0226d-9286-379d-a14e-29a2cc7b38da | -7.04749 | -59.21238 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0721e37-0beb-3012-8241-5f2feaec7528 | -6.04597 | -53.79819 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07f8199a-fb50-310b-97b4-9427945d86a5 | -10.48612 | -51.32731 | 2026-09-03 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e52a9495-2ebc-351d-89a8-c952f5739858 | -7.53782 | -60.72346 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95ea4b13-7737-30f8-830e-665d8ae87493 | -11.33037 | -50.53107 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d8365c61-bd12-3b39-a903-b20a04db5809 | -8.46249 | -54.66531 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1edcdd0-65aa-3a53-b120-3a7fb6b992f0 | -9.60997 | -48.56446 | 2026-09-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efd8fb5d-54a6-3e6c-a42e-c000f7ea60cf | -7.05227 | -59.21542 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5bc89a-b1ef-3d7a-bdff-7c900127d121 | -6.84408 | -59.34589 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5967b0cc-197a-38a3-a5a1-63a3b5ed6d15 | -4.23566 | -62.24178 | 2026-09-03 04:57:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fd0358a-e8c1-378d-bd3c-3a02db98bedf | -7.56613 | -48.36146 | 2026-09-03 04:57:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ee259cd-7260-3e1e-81a0-9950a487d450 | -9.04396 | -65.7382 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a1ac4d4-3e27-311f-8ad8-72b702dad4d9 | -9.70462 | -57.88254 | 2026-09-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e4cdec-9bd4-3936-8738-25fab30b44d6 | -5.56778 | -60.17351 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 274504a8-ea6f-32c7-9333-10e507d726e5 | -6.25493 | -55.41608 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fcffbb9-8911-35c5-8947-51c5011b2595 | -7.72084 | -61.12841 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bac0a7cf-97dd-3ab2-8f8b-b042a3f45cc7 | -4.97441 | -55.85076 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c46da120-fca3-35ce-b1e4-71490fdb84ef | -6.2025 | -53.47773 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544794ba-943d-3aea-995f-23660a570d1b | -8.4698 | -54.66281 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19331328-adab-359d-8d02-0d04f887e587 | -7.0863 | -56.51824 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README40.md)
