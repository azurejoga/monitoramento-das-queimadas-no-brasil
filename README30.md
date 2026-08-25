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
| 09ccb4ba-790a-3520-9442-b433ada0c7b8 | -7.28466 | -45.36282 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e32cbe4-3e06-3e8c-99a1-d1ee0a3fc33b | -6.17669 | -53.47837 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1191afda-d258-324f-92b4-156301f04b4d | -9.06776 | -45.21398 | 2026-08-25 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aadcc9e1-436f-3da9-8669-93094250c348 | -6.33503 | -54.77468 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fb7c6ff-db6b-3ede-9c1d-e52533cf3ee3 | -6.34362 | -54.74866 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d7069f4-78ae-33c6-8413-bc3a450da8d4 | -7.19137 | -42.74467 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42fba930-9b80-31fd-9ef2-1068514f76cc | -7.26058 | -45.85525 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 523ce1d3-313d-3aeb-a362-d1bfeff95a1b | -8.60345 | -54.73771 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7ad8ac0-b679-356c-85d6-9e128a65cd9a | -4.0509 | -48.96709 | 2026-08-25 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d9c69a7-79fc-39f7-ab5a-6d1aac422a30 | -6.0216 | -50.20686 | 2026-08-25 04:25:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c0e7a0d-8cbe-3702-ab6c-f1aaf7876f46 | -7.18502 | -42.73972 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e93f3000-84ca-38cb-9002-fa413f0fb241 | -7.13984 | -42.75636 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3df9ad29-3158-3e71-90a0-9d003a3d5b90 | -5.95445 | -53.60702 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22f068d8-ab85-398d-8a01-33266009e5c1 | -7.13981 | -42.77994 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83d91a92-bd3b-3bf0-8aed-395c9a4e17ee | -6.14941 | -57.70099 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0fb1e9d-50d3-3349-8ed3-f8579c7ebeb3 | -8.1016 | -47.47312 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c60df8fe-db30-377f-98c8-64fe4bea0eaa | -6.33073 | -54.76636 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e02afc1-32cd-334a-a186-efc3b48b8790 | -7.30082 | -43.009 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 57b413b5-f2aa-3ba4-9d28-a4fd10c75eb8 | -6.17188 | -43.76083 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d50806f3-b42e-37de-9267-3d98a812ff97 | -6.16974 | -55.44686 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821fa0eb-5785-3971-9650-95c9e79344f3 | -6.14267 | -57.69994 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 831c5ef3-2e75-38ae-8ba8-16f7372c91d9 | -7.30426 | -42.96801 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0285a3b6-75a0-310c-a7e0-7895085eb147 | -8.16802 | -46.69705 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b3b816c-e8d4-3cfa-8a71-19dcfa623dce | -7.26757 | -45.36365 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 461ff36d-61d4-3dc5-b821-b93cfa043783 | -6.63566 | -58.48362 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45147fc5-ba58-38f1-a249-88802fb998e8 | -7.90037 | -46.37787 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f687029b-fe7b-3e55-b5f2-87c01718dfa2 | -7.28576 | -43.01907 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49e4e8dd-d7b3-3d73-a1e5-6721cd00c473 | -7.27222 | -49.92318 | 2026-08-25 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 968fcff9-17c7-3cab-a774-28f7a2dd0cc5 | -6.70287 | -56.34655 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11075595-43be-33c2-bf00-dffe14f6077e | -6.33536 | -54.76248 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 360325a3-d8c6-3a1e-b578-9f742e811d03 | -5.30019 | -49.14259 | 2026-08-25 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0710980c-565c-3023-bddd-24a5880fc8a2 | -8.57423 | -55.27744 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2f058c5-f651-3bdf-bf92-4ca74dc9b689 | -7.43947 | -43.0876 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 552f2e6c-3e9b-3219-b4ad-b31590e9f814 | -7.41119 | -44.97107 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb0c3cef-59fe-3fd1-8ec6-80274f45a584 | -6.64028 | -45.16375 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d7e23e-e5f6-3866-950c-62423fda4200 | -8.80857 | -46.60165 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3d066da-c834-3108-9a2d-0f1be028f68f | -8.08127 | -47.53273 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9cb06376-89da-348d-abe8-313724dd2c6d | -7.69966 | -46.1461 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81056111-f4cc-3450-9fd2-8bea0338ca3a | -6.34027 | -54.76716 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e16f46c-2548-3bcf-b62a-feda76b7b87a | -7.74638 | -46.15348 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09a7909-8e05-3f0e-98a7-23019ef41709 | -2.8919 | -48.80704 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9183d67b-350f-38b3-9eb0-ef0a715f5f01 | -6.0921 | -44.89209 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fa18ab8-8c8a-3330-b46e-dd5c04493fec | -7.25257 | -49.8549 | 2026-08-25 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d251cb11-3739-31c6-aa8d-8f923e8ac8b9 | -7.30082 | -42.96747 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f10177a-0642-3203-9af4-a616710a6e34 | -6.79405 | -42.69035 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e653b04-33ee-3abb-baaf-cb0fd3d3454d | -5.77604 | -57.55918 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a479c98-2bb8-3a6a-b321-7967121d37af | -6.09595 | -53.41377 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6fcbb90-b2f1-337a-bd89-be1d3c7a774e | -6.2279 | -55.48554 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebb21f9c-6a9c-3a11-bef8-3a52a5bc01c5 | -8.21967 | -54.98145 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c4e83dc-addc-3ba3-b9d3-9a2ecc66cbea | -5.73533 | -43.27723 | 2026-08-25 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 414af1cd-f28b-349d-8c7a-010a935882f2 | -6.83833 | -52.5032 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b6fca29-e734-3e0d-8464-ed9659c2755d | -6.62209 | -58.48643 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9551e40-08f0-3f13-be37-e826eed9f80e | -7.38681 | -44.56525 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87750563-5f04-3ca1-95ab-aa63ca5a8510 | -6.34942 | -54.7803 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb48f81-1d22-3784-ba44-2a0accc21a7c | -6.80881 | -42.67561 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 740858ab-557b-3251-abae-42cefea3090e | -7.8999 | -46.35951 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9fcbe62d-2854-3b5f-89c4-80f06e0858c8 | -6.77064 | -44.8974 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab284705-0520-37bc-8dcc-2e7ed18a1354 | -8.93839 | -50.16233 | 2026-08-25 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae0265bb-107a-326c-9400-d6487166cd90 | -6.82187 | -58.66385 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21c73619-b383-3fc6-b476-bd55a9300098 | -7.6729 | -49.38297 | 2026-08-25 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41f0ecf5-4951-37c6-aa34-0fb5cd6214cd | -9.69224 | -46.05381 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbe56627-24d2-3042-ad7a-fd0b0a8646ef | -6.18075 | -53.48549 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd0ac25-e3f6-38f9-b9f9-f280bac4943c | -6.4153 | -43.07516 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f55d0ec-8290-35a2-9c88-5004304d8529 | -7.27474 | -45.36124 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 308b421b-5c96-37b6-ac8b-cbd6b81e42c8 | -7.66269 | -46.91187 | 2026-08-25 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01ed7f17-fc5f-3ad5-838a-808373e11f27 | -8.30974 | -47.59626 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcfd7923-9cc0-3a32-be26-3f7b706df603 | -6.21049 | -53.49723 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cef0bb2-a3eb-3e65-9271-bbd87a3f83fe | -9.69168 | -46.05731 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3864b76-7b90-3506-99e9-4a2ce7342179 | -6.83271 | -52.50726 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9e1a207c-f00a-3351-ba1f-49e05b7f7e5d | -7.15828 | -42.79844 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df55c308-f1a0-31aa-b0f3-714ab7175cef | -4.95104 | -42.98769 | 2026-08-25 04:25:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65712e81-247c-39f0-aa23-2e51b100b7ce | -9.57111 | -49.22707 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbc9ff33-5a16-30bb-8441-f948b12caa3a | -5.98477 | -43.7429 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4601fe1a-463a-382a-9d26-8c8fa3f5b5db | -7.43373 | -43.12511 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3853cde0-b41e-394f-bfc2-5f31d64ac010 | -6.26549 | -55.41075 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ece9151d-8e7d-38f8-8cbf-b3157d4397dd | -7.90966 | -50.95274 | 2026-08-25 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0804ffb2-2e14-383a-84ef-2af9acb92b2d | -7.2808 | -45.36576 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc03722a-594e-327a-a8ae-6eacc0b171ec | -6.09924 | -44.86844 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 967d1e1d-60a2-3395-acdb-e8c1cbbb4407 | -6.81029 | -42.67723 | 2026-08-25 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 27095126-2a4c-3196-a421-7294ff5e7d75 | -6.44218 | -54.96054 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d338391f-b9d0-368a-ab13-804082706997 | -5.71371 | -46.18309 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c41ff1-8626-3dde-b76f-16d953dfec60 | -7.06356 | -45.00068 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dcc5e6d-1eaf-3e10-b04c-7ae39d997264 | -6.3318 | -54.75037 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb3accba-57fa-398c-848d-d374cf7529a3 | -6.3383 | -54.77806 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bad6e1e4-54e3-3473-af44-159f6f7125b6 | -6.32489 | -54.75676 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdee4f7b-e5df-3c36-a3ea-823cbb5c399a | -7.0608 | -44.99669 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cc9632f-1de3-3b8d-bc5b-8350210d21d1 | -9.21015 | -50.10343 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27414757-cc24-339c-8ac4-f03d4bab7310 | -9.45032 | -51.58435 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b71155a6-9d0d-32b8-b0f6-9d03dc167949 | -5.9526 | -53.58679 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ee31017-762e-3e88-8e70-9139484a3c4e | -3.53434 | -48.17862 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c2907f9b-e9b9-38db-97d6-6b4bef8e924b | -6.14496 | -57.9516 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a95b629c-74cb-3bc1-bc1c-05724e89cf20 | -6.64007 | -58.49832 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 71e5b0fd-dcdc-31dd-8ea6-eb9389353313 | -7.4303 | -43.12458 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eba6e302-4952-389d-9254-46666ed5c637 | -6.22795 | -55.61981 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f5c0abf-4c52-3b47-9c7c-5de91015900c | -9.69391 | -46.0433 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57186b59-a4f1-39d9-b2a9-8c84e9eb42cd | -7.90266 | -46.36367 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0603b177-2af0-3452-91a9-38e93dd401bf | -6.26336 | -55.42259 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f80ab61-055a-34ce-8caf-cf4d78e2ce71 | -7.48921 | -55.35169 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a80853fc-9ba0-3865-a155-a88fc979f471 | -7.89656 | -46.35889 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 54487a64-0abb-3609-95ef-41d65a886571 | -6.35498 | -54.78143 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
