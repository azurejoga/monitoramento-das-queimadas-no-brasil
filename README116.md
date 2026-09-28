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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd22906c-07c0-3ec0-8905-e17a9a9afc7d | -7.2567 | -43.36584 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 4b2974f9-954f-3402-bab4-0d4690e52997 | -8.16432 | -47.63537 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 02a0e630-edea-36da-ad04-1fa875b83fb3 | -10.16438 | -46.57451 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c775b5a3-7e5d-35bd-b65a-41e7f54da668 | -9.82961 | -49.14231 | 2026-09-28 16:26:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2fe27c85-41d2-3ed1-9856-53d225f70bb0 | -11.09779 | -51.37608 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 966ce051-9f13-385b-944f-7b272dc7efd8 | -9.29938 | -46.44667 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3944b322-5c63-3f3f-8178-98130dac0847 | -8.96929 | -44.15018 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 47a4ea1e-1946-3b01-94d3-afbbb1022f66 | -10.61606 | -53.99246 | 2026-09-28 16:26:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4620316c-59d3-3c4a-ac3d-ab04bea49325 | -6.39517 | -44.83712 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ce69ae4-b731-3962-87b6-e8b6a5a72e73 | -6.35067 | -45.80589 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35e2e09e-915b-3eb3-91fd-7f1d855d1e95 | -10.96836 | -50.68913 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 74729acb-cf64-3afe-a31c-f53def32b8eb | -8.35862 | -45.46351 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81e44d8e-33f9-39bd-b995-ba0b9125f9e0 | -5.90578 | -42.64975 | 2026-09-28 16:26:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3c24ee41-e8c9-351a-a6d2-9a8373442438 | -7.36429 | -45.40628 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eb06721b-d531-363b-952a-bcb3ecd65410 | -10.72813 | -50.47636 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 994042ab-b25c-36f6-a767-a1195e30ac21 | -9.98091 | -50.13131 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 79fd32d8-0b35-39a3-8bc7-e275c400a56b | -7.41267 | -46.72012 | 2026-09-28 16:26:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| f86a664c-7fcd-3556-a20f-ce07c7fd522d | -7.03545 | -45.81608 | 2026-09-28 16:26:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11cb44a7-fd9e-3e08-9a4a-48b925606573 | -6.2176 | -46.62955 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2164c8f5-cda9-3f1b-8418-e893c7948d00 | -7.04644 | -44.29716 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 460045c4-e10e-3be1-bcc1-854a991866da | -9.32965 | -46.5512 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 35d436e4-5dc4-3780-a777-869465341b2b | -8.10333 | -47.18465 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8f29bab1-bf10-3dba-8289-f5d79186b50d | -10.70621 | -48.74599 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a8776422-1678-3056-ad15-2cb27f759ed8 | -7.38541 | -42.09334 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 3af94f2c-6305-3602-9bf4-09a7c4dc8f1c | -6.89097 | -52.48094 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ebbb0e72-e6a3-36a1-9730-633c2005fadd | -7.4119 | -42.62247 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| cef55cb0-2e3f-34ff-8a73-bc38c4b67155 | -7.46861 | -45.06259 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 971bd90a-c7a1-3c96-95cc-6ada90b3cb7c | -8.16558 | -44.43943 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7b7c5988-38a9-3d96-baee-b37983511206 | -6.35781 | -45.80469 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2503a1b9-65d3-397e-8783-8d8f0649ec64 | -10.76614 | -52.1307 | 2026-09-28 16:26:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b2627aa6-be62-36bc-aff8-765b81c9aed7 | -9.78283 | -45.82038 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e0d2d802-4447-3067-a5dd-fca48314a59f | -11.52952 | -50.6964 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4227c286-b862-3410-abe5-395bcf11c744 | -6.24225 | -41.59293 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b86f3631-a2af-3176-927f-1ce56533f0f9 | -10.98369 | -50.68388 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f5f3f464-728e-386b-bff5-aaf62533ed6e | -11.29163 | -47.67231 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e87d9cb-9cca-36f2-b2df-377afe5a91f1 | -8.35922 | -45.46766 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 499bb06f-9f7d-3c16-b6db-4de2ba9e0f52 | -8.19174 | -54.79224 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1b39f5a2-ce91-3f6c-afe3-f2a4c4a8aa21 | -7.98156 | -45.01221 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 143f61bc-fcb0-3f3e-9f6f-2489a65d262d | -9.99082 | -50.12318 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 30665a7f-72a3-3ec3-b58f-cdd795f9526e | -8.98409 | -44.15567 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 0a20418a-76bf-3867-ab3d-98239d46e037 | -6.69472 | -45.67048 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce683269-f7a8-3e2b-9205-c90ac56a9984 | -9.9717 | -50.13836 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8afffe9b-2338-317a-b35e-551598165856 | -11.14101 | -50.03503 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2d1aa0c4-fa04-3aa4-9fb4-220035686bc1 | -6.40342 | -38.00358 | 2026-09-28 16:26:00 | NOAA-20 | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 58e046d3-6744-3f3a-9ae1-1910c42ccfe0 | -8.32825 | -44.16616 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0d4170f2-5207-31b6-87c9-95b4778c6add | -5.57173 | -45.30103 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d7b6ef81-000c-3c0f-a89f-3fd284f75eac | -10.23535 | -50.00554 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 6b057957-581f-30d9-ba2d-7fcee8baa5ed | -10.94913 | -43.89316 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5148e14e-f179-3e28-8179-c98cef98589f | -4.08945 | -42.95654 | 2026-09-28 16:26:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfd5394f-c686-32bd-9a85-4b30c613594b | -11.20264 | -47.71292 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f878d1f-3c12-30f7-af2e-43b5bb6cb0c4 | -7.69231 | -54.75735 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 80f87c64-ff40-39ca-b5c2-d06d0c3ec2fe | -9.50633 | -46.35314 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3123a2f5-e893-3e1a-8b4d-5f184eceb2b6 | -10.91139 | -44.65293 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b23ee9fe-b9fb-31b1-9e2c-c84bcdf8c643 | -8.65884 | -45.37098 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 38b80d50-71b9-35f1-8e8b-a607059de9c8 | -4.34373 | -48.64527 | 2026-09-28 16:26:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c350b213-2ba1-3b72-a318-71ecd28336ab | -8.1084 | -44.00476 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c14b16c-02c1-3394-9800-27990d1a3959 | -7.71601 | -44.89985 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 97d02823-3120-3853-9cd4-b9a146b9d111 | -7.58433 | -44.7893 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93b1ba2c-6c08-3d49-865a-de94f3152415 | -4.90157 | -46.0003 | 2026-09-28 16:26:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9edbe443-51d7-3f1b-9cde-9d0680a8b8fc | -11.08292 | -46.07192 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 75603ccd-226a-353b-9319-5149d42efe92 | -3.81329 | -44.10592 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b554e154-2e56-3498-acea-6a9c9978ce42 | -7.84572 | -46.92886 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8f21df4b-a29c-35f8-9f5f-ddca08a5c3c7 | -7.03341 | -45.81768 | 2026-09-28 16:26:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc8c076f-6ddb-33c6-915f-bb82a46f04e9 | -11.18183 | -51.37636 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7f2e37e-c64f-3419-abcd-fd11bddcb1e2 | -7.45417 | -44.5951 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a24e7030-9459-3231-b8ce-2d5a9d6e97fb | -10.6038 | -49.98154 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 56a4f1e0-6350-3459-ad10-a7f811f7c732 | -11.2911 | -47.66816 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f89aaa4-4be7-36d8-b74f-c4618aae6317 | -10.11617 | -50.18995 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| acacacf7-8ef9-370c-9ff2-265abd582960 | -7.20404 | -45.07812 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5273b33a-5cae-3445-84ff-1ea7f645d2ca | -6.35661 | -45.79657 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 600a47ef-6bb7-3628-a771-47e4062a81c7 | -6.89198 | -52.47984 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fa7c466d-8332-3de5-9339-bce11fe88998 | -4.28731 | -49.88923 | 2026-09-28 16:26:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a2d0d48a-371b-3f3e-9d5b-d8594e65c020 | -9.93852 | -50.23508 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b38fd34f-1423-3876-a57b-c6de34a2b092 | -8.97668 | -44.15289 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 896d3379-584c-3886-84a1-55eb1976f7e3 | -11.13434 | -50.06279 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f86a11f0-ef48-31b4-8946-d4822666ab61 | -6.15867 | -52.82845 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 5a8ea6c8-a845-39c1-9e04-ca5c898b1a92 | -10.21699 | -49.9918 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 73d02369-08f5-3f33-9e96-fea246b02a65 | -8.68837 | -38.19353 | 2026-09-28 16:26:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3eb4adf1-ed5a-3acf-88fa-f1f1b1fcbdc1 | -8.63648 | -49.47757 | 2026-09-28 16:26:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 861815be-2f14-3cd1-8d31-5f4ca50e9cc8 | -8.52342 | -39.3376 | 2026-09-28 16:26:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1e0d8a1f-36ae-31a2-b891-be6d9f29035f | -7.41904 | -42.62492 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 83b8f732-e3d0-3405-8682-9bb7d2ffbade | -11.14604 | -50.03438 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 66ea604e-2c20-384d-8bdd-bf78e3ad933f | -4.34375 | -42.95415 | 2026-09-28 16:26:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd47de7f-a58c-3b79-a321-49bb24bf335f | -10.90485 | -44.65804 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3f8150cd-8586-3858-932c-6f423890da7b | -6.39173 | -44.83758 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd67c0b9-e413-3520-9898-aba6ed398951 | -6.76121 | -43.72417 | 2026-09-28 16:26:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 017831f0-79e3-311d-9481-12514b3e7381 | -9.06697 | -47.17977 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 042e0b24-8b9f-3f9d-aaf1-1bc89b3ca602 | -11.14594 | -50.07328 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f79c5077-67d6-3fc6-9118-1098b7f34be1 | -6.16487 | -52.83164 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a83979b1-73eb-3f20-85a8-0b367ec6533d | -9.86714 | -43.61978 | 2026-09-28 16:26:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3e5db3c5-0ad0-37e5-b07d-176c6153772e | -10.9611 | -50.67361 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 021f02e4-0875-37a6-aaa6-a26392c9195d | -8.76987 | -45.82543 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6384c1e0-84f7-3a29-b95b-4be3121b8906 | -10.16805 | -46.57174 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b2c030ce-ca9d-3dad-9d46-5d8ba627e318 | -10.95786 | -50.69048 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 3f9d74fd-68ef-37c9-ada8-d909327e52f7 | -9.06748 | -47.18334 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6fb16295-28b0-357c-a5d6-bfd3b46c5f35 | -6.81666 | -45.05425 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4b8d6a06-e624-3c5b-a2df-c4290fd03226 | -9.87053 | -43.61926 | 2026-09-28 16:26:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 313ee78c-71c0-3767-bcfd-9ea9132da007 | -5.558 | -48.44788 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 466e144a-2711-390d-9822-a8544e63f2c1 | -8.03807 | -39.56395 | 2026-09-28 16:26:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d1e7e7f8-23c7-3aaf-9284-c2681bde7c48 | -11.1487 | -50.05495 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README117.md)
