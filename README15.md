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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84fce359-a75c-31c0-bbed-7bc9139106a9 | -3.75049 | -44.56843 | 2024-11-22 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b3294b7-83d0-31f7-b599-ba754dbf731f | -3.441 | -42.5459 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c2c91a7-8cca-361a-b4b3-04cede8c2641 | -3.62103 | -41.07743 | 2024-11-22 03:49:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 96aa970a-ff1c-31b6-8510-9bd27f94e07e | -8.93095 | -44.24894 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac64cc88-06c8-3fa6-9bf4-45723b201b93 | -4.40244 | -44.12398 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b5b9326-249f-3ca3-923c-6891e8596ef5 | -9.17597 | -35.67758 | 2024-11-22 03:49:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47c6562b-c8eb-370e-a712-a909a9e694f9 | -4.57441 | -48.0191 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 557b787b-670b-3e26-b785-01e7e99d2b0f | -5.32827 | -45.25336 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd3fe03d-0bed-31f6-a590-e41576e579be | -1.96256 | -48.39017 | 2024-11-22 03:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd98eafe-e891-38d1-8714-ddc7327c3904 | -7.65541 | -44.50261 | 2024-11-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d59c2e5a-e7fa-38b3-9b8d-84592c9c6f24 | -3.75632 | -46.12592 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 466fae38-db4d-3ef8-affa-cf804be56052 | -1.96153 | -48.38872 | 2024-11-22 03:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f69499e-fd68-3d08-bc6d-d60690562208 | -3.7625 | -46.12304 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ef6cc895-9a0e-3805-b6d4-104d0c15f78d | -6.12148 | -42.51807 | 2024-11-22 03:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e7fd560e-043a-3e71-8c5e-f68973190802 | -3.34749 | -42.79044 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b541f623-15c6-3fbb-b7eb-4f22aefa7ac7 | -6.36327 | -44.00648 | 2024-11-22 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c870ae6f-4ad8-349b-b7f4-ab76e09fd116 | -5.01077 | -41.95726 | 2024-11-22 03:49:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2ebd5c11-ede3-31b4-91ba-f1a1f8db25bf | -9.29971 | -43.12699 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f6ed60af-fefa-3cd4-ae23-625d0207a365 | -6.50591 | -42.18818 | 2024-11-22 03:49:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29ccffb0-be22-3bfd-b20c-b7bca49c70d9 | -3.90635 | -40.97816 | 2024-11-22 03:49:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08fa787b-a0a0-3d19-b091-b2a5cd88404c | -6.1852 | -45.45159 | 2024-11-22 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce696481-a6db-3588-b833-71866afb7502 | -2.93461 | -40.86924 | 2024-11-22 03:49:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ab70a67-21c7-3a01-84e6-cd76d0297cbc | -3.68759 | -40.86261 | 2024-11-22 03:49:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95fb9d0d-7e09-37d3-9036-b69eef3ea17a | -3.83904 | -41.56317 | 2024-11-22 03:49:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62930e85-0b7a-301b-9c7a-8a5f09b80f0a | -8.93462 | -44.25425 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2be94bf-5f8d-3576-9984-17a34cf7c202 | -7.21698 | -45.08083 | 2024-11-22 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74079082-3430-3050-99b8-131ccb5223aa | -4.13495 | -46.7067 | 2024-11-22 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b580cfa1-5771-3a29-bdd5-1451446f28b5 | -7.46402 | -39.22937 | 2024-11-22 03:49:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 726e5e8a-79dc-34e5-8186-c1b43b6e5398 | -3.75694 | -46.12221 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2c4f30c-b597-38e8-8acf-246bae2891b6 | -6.26994 | -44.54586 | 2024-11-22 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| db71a0b4-99c9-3870-a8f1-9870711cdedd | -5.58657 | -45.21372 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 37123caa-8340-3b8f-b314-9ab48f8e869b | -3.79096 | -44.01593 | 2024-11-22 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24255d2c-56a2-3348-af8c-8ab5a565d16c | -7.41759 | -34.8088 | 2024-11-22 03:49:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d9f0b641-ff41-3189-9db6-6cd6d57f6efe | -3.45968 | -45.90152 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 92f79b24-8e37-3698-b21f-80d0733c273e | -10.10225 | -37.32995 | 2024-11-22 03:49:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f9d8d8f-efa2-3203-9079-1978a662179c | -4.43116 | -46.58712 | 2024-11-22 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b25519b7-159f-3ca2-8cb1-19cf59298028 | -8.0715 | -47.08606 | 2024-11-22 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df3da16d-3dbe-3440-beff-0af142cf751a | -7.28956 | -45.0837 | 2024-11-22 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f63e166-830c-3d58-a038-d773ffd3d710 | -3.47189 | -50.01128 | 2024-11-22 03:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0715e0b-51d9-38f7-a5cb-b3d2dcaf4a2d | -4.06433 | -46.41713 | 2024-11-22 03:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 087579c3-e4ef-348b-9965-c6048f95bb00 | -4.23896 | -41.92709 | 2024-11-22 03:49:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72cfaa6b-0c8c-371f-99d2-0a36131b5554 | -8.93014 | -44.2535 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf3c5f88-d022-3e1c-a168-b3541c91cbdd | -7.37768 | -34.88575 | 2024-11-22 03:49:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce3a9e8b-504b-3906-bb2f-82be79709eb1 | -3.03422 | -45.66141 | 2024-11-22 03:49:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0037da-0372-33e6-b590-af3045c86b73 | -5.11025 | -43.16523 | 2024-11-22 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f55e36dd-70f2-34f2-b0d9-9fd590012328 | -3.41031 | -45.23417 | 2024-11-22 03:49:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afd727b7-91e4-3373-b630-02b2c46cc9ef | -10.48654 | -36.9306 | 2024-11-22 03:49:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| c820c2ad-fcfb-3a89-b51b-2f0531abe0f3 | -6.02945 | -46.10654 | 2024-11-22 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12fb389c-3e72-3f21-9655-759da68b33a0 | -5.47628 | -42.07155 | 2024-11-22 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22b1ad53-cbbf-3a4a-a058-755cbb3552fc | -5.83347 | -44.01788 | 2024-11-22 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18eddd2e-1c19-38d5-8169-73c92d828b88 | -4.58096 | -48.02266 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b14463c-0c73-37aa-be90-67933bd8084a | -4.00653 | -49.9263 | 2024-11-22 03:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8fd158d-dc60-384e-8560-d0479cff14a3 | -2.98178 | -45.12026 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| e3c70ce8-fb16-313d-a8a4-c5acb6cf84df | -3.75139 | -46.1214 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6590e056-a0ea-3eeb-9f0b-bc166f2604f5 | -5.23792 | -42.63758 | 2024-11-22 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e45bb3a6-2305-3ef9-b0da-6aacf9240912 | -6.62793 | -42.38234 | 2024-11-22 03:49:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5c0ba1d-1108-3df7-b16e-5f2027995939 | -6.4309 | -39.27779 | 2024-11-22 03:49:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac1d3da6-15e0-31b8-97bb-ee9c33cff0d5 | -8.92037 | -41.18897 | 2024-11-22 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b8618b36-ddd8-3581-a019-a5b0e49a6442 | -2.98073 | -45.12669 | 2024-11-22 03:49:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| bf3a6429-8674-332d-930c-f925196324a1 | -2.6996 | -46.21968 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 327303b2-2eba-3891-9da9-04eeab89dca7 | -4.23835 | -41.93082 | 2024-11-22 03:49:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d108d9c-f2c3-38f4-a90f-eb48e232330e | -7.64575 | -35.06633 | 2024-11-22 03:49:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4e766d87-c982-3ccb-8ebc-99fc5271771d | -1.74424 | -46.30223 | 2024-11-22 03:49:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3f5aceb-c8c5-3237-bf63-3fc82eca217b | -8.92565 | -44.25282 | 2024-11-22 03:49:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be100bd5-d69a-3512-af90-13dbcdbb3a98 | -4.4081 | -44.11953 | 2024-11-22 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b5e587f-62c7-356f-b670-5da714f83721 | -5.75497 | -46.188 | 2024-11-22 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ab9c0dc-f765-3045-94db-41e45fca3b42 | -8.71117 | -44.00807 | 2024-11-22 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7534135-c525-3b24-8509-f30e1541761b | -5.63194 | -44.53363 | 2024-11-22 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 797daff7-705f-3d9e-a8af-cc93c86cdc4d | -4.43702 | -42.59523 | 2024-11-22 03:49:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79a57bc7-4af4-3ab1-87c0-3de28562b1a8 | -7.71902 | -45.66227 | 2024-11-22 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 385e36c3-b7bd-3ee6-b45d-efe525dcca9f | -5.58828 | -45.20972 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 644852ea-436b-30da-a75d-72cc2bfe1e8c | -1.78517 | -47.10798 | 2024-11-22 03:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f32cd593-fbd3-3cd3-b71f-68e2efdb1a8b | -5.07491 | -39.72935 | 2024-11-22 03:49:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cb511c5-3b35-3f52-a3fd-52043baa5196 | -7.45002 | -39.77702 | 2024-11-22 03:49:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 755cac6a-34fc-3b80-b0a4-1fc32b054b42 | -3.34821 | -42.78605 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a0323614-7c0b-3e46-b19f-bb781f92726d | -4.14783 | -43.88068 | 2024-11-22 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240fcfc7-7ae6-3143-9bc0-423c0a252335 | -1.52093 | -47.06553 | 2024-11-22 03:49:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba4541fc-c1ef-32fa-9899-81afac58cc1c | -5.26885 | -44.29604 | 2024-11-22 03:49:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 423ea03a-6441-3d2d-a89c-05b32b181d9a | -6.82062 | -46.77687 | 2024-11-22 03:49:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dbc3ac8-c182-3a84-a17d-b94072ac59fa | -4.68865 | -40.69269 | 2024-11-22 03:49:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 99ef9d9f-2803-3afa-8837-d7a1b4ba3757 | -9.16783 | -43.1631 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f90b4e1b-8af9-3ba9-860a-9c2e78b89f2f | -3.49657 | -49.96633 | 2024-11-22 03:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc808f0c-447a-3dd2-8dd2-b9f9cd651986 | -6.00746 | -41.9672 | 2024-11-22 03:49:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 420e51e6-ae38-3ac8-8c7a-54aa3db46af9 | -3.47005 | -45.90688 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e21793ad-6577-345b-a6dd-5e113a9ba60d | -2.28031 | -46.55761 | 2024-11-22 03:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ba30252-7bc0-3b68-b9ec-ec57ad9549b7 | -2.0864 | -46.28929 | 2024-11-22 03:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 167f9573-1bd5-3965-83a1-8682e86174c8 | -9.36061 | -35.49614 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 4d3256dc-cc8b-3d95-9c2b-7bb03227c32e | -4.22888 | -40.38542 | 2024-11-22 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ea04910b-4cbc-36be-b8da-554ec1fd159f | -1.80066 | -48.46906 | 2024-11-22 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26f8372d-b600-3687-9aef-8b37dea72bcb | -4.70371 | -48.29411 | 2024-11-22 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd09c0e0-f305-3a29-a3df-df857ee2b480 | -2.69786 | -46.0896 | 2024-11-22 03:49:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aac553c-6166-35ea-b5b4-7e931956ee99 | -5.5097 | -45.48821 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21475f4d-f7bf-3e57-9959-67d35bc52313 | -3.75084 | -44.56988 | 2024-11-22 03:49:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e81fdd96-5b47-35b8-8ed2-2ed40ba10f82 | -3.75756 | -46.11857 | 2024-11-22 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66ee54c3-9e85-39c5-8102-91f864e365de | -3.46825 | -45.91758 | 2024-11-22 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d887a8ba-ff76-348b-8670-4aad0d672181 | -5.58709 | -45.21075 | 2024-11-22 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36df3d35-3841-39fa-9b3e-4becd75021ed | -5.12654 | -42.81725 | 2024-11-22 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c22c7e25-60ac-31be-950b-2408a885138f | -3.00644 | -45.13417 | 2024-11-22 03:49:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 955044ed-083d-3ed2-bd1f-6bebe7e98064 | -9.17197 | -43.16381 | 2024-11-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d771edd1-645f-3fb5-b415-d5ce94feeb57 | -3.67371 | -39.58039 | 2024-11-22 03:49:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README16.md)
