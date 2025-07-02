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
| 4880defd-f80b-37f5-8897-da75051479cc | -6.29672 | -43.67665 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dacc1d9-adfa-332c-9e25-2b92d7a411fe | -7.78407 | -44.01792 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9f7bf00-0b56-36f3-833c-6c57efc23a66 | -7.18879 | -43.17251 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e0cb73c-d981-3fe0-a095-a52aa0a5adca | -6.29319 | -43.67611 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 17cb2463-5104-3ee0-9ae3-0ddea24020d9 | -5.62938 | -43.6601 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 828c5136-33ca-356c-abe7-146dbd8484ff | -7.30106 | -44.5664 | 2025-07-02 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4260d5a3-6c86-3157-9a69-dd48545a21da | -7.61658 | -45.75829 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a04ae81-cda5-3c78-8b96-8d369bdea4cf | -7.61325 | -45.75777 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ec3ef043-b3b3-3ec7-a48e-cab5d4a2e629 | -6.27439 | -43.68131 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 562818de-902f-3a33-aa39-4b9996404bcd | -7.20808 | -43.09171 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a620177a-2408-3a0b-bc18-73fcb4ab948d | -6.02579 | -49.23218 | 2025-07-02 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfe6a1e-824d-359f-9de6-33d55d6d7899 | -6.28143 | -43.68242 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6d3571d2-b41a-3f39-8bee-216414820a8a | -7.6693 | -44.65904 | 2025-07-02 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a88dda2-6ac1-3a32-9f48-3420701f9517 | -5.61887 | -43.65854 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5c8de34-c2d6-33a6-a6c8-da9a13ed81ec | -7.80862 | -44.0253 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bed7a195-2f0c-393b-b11f-9e4615eb879e | -5.07184 | -43.72974 | 2025-07-02 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 857f8c66-907c-391d-a9d9-71970e4e05b6 | -7.61156 | -45.7467 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64d437ca-a36e-3ca4-abae-849fe86b457b | -6.90083 | -44.77598 | 2025-07-02 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27642be7-f8fc-307e-8743-6c2c2fabcd00 | -4.31948 | -48.07991 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e5fe6e7-214f-3c41-b7f7-48a2364949bf | -6.28495 | -43.68296 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 76986a26-2f1a-3310-9a16-681b848bb65c | -5.62646 | -43.6557 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c33d7870-87ab-3c6b-86c9-7c0e5a43f833 | -6.7116 | -51.41007 | 2025-07-02 04:25:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e21aeec-3910-3fb2-95b5-35e8dee95a57 | -7.73792 | -44.76129 | 2025-07-02 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b98a2702-22f2-334f-ba8b-88f339dd540b | -7.80979 | -44.01733 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| aa3e78c6-b1c5-3dd6-88cf-ac04186371a3 | -4.55998 | -48.0024 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dfbe472-bbac-31f4-97d7-498bab61c6d7 | -7.2592 | -46.39719 | 2025-07-02 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1349f47-b20a-3f9b-bb5f-40169d82541c | -6.53926 | -55.02715 | 2025-07-02 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 546698c3-4fcf-319b-af76-fa0abf0be57b | -5.07173 | -37.71702 | 2025-07-02 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 033cdcaa-4634-320f-8d0a-123a9cc78d26 | -4.1908 | -48.13768 | 2025-07-02 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97986bd2-ddde-32e3-b45d-77c0a93bce26 | -7.81104 | -44.03019 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7004ecbe-22f1-3bae-afc5-3ec52fed7782 | -6.90367 | -44.78016 | 2025-07-02 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83252209-0017-3722-8014-379421fef2d0 | -5.62588 | -43.65958 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e3c614-ef30-3008-8057-b10677700ada | -4.32232 | -48.08422 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a9b126b-76b2-37ae-9331-ab8006e51d00 | -6.23091 | -46.24874 | 2025-07-02 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f37c2af-a4e6-31c2-afa0-ade208b302cd | -6.70703 | -51.41288 | 2025-07-02 04:25:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4767ec9a-69a5-3bdb-9958-2a508aef6745 | -6.95619 | -42.89908 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 891347b1-0673-3711-9bc9-504d3320eebd | -5.91014 | -42.99026 | 2025-07-02 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ce18018-e0e9-3585-b98d-a249bd343c07 | -7.21972 | -43.08906 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e2c8a07b-24e6-33e1-95fc-cb0fefd9412d | -5.62827 | -44.26754 | 2025-07-02 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a368c1b-aa41-3c11-afea-ef9e2cd12873 | -6.96561 | -43.08683 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cd8428b-2851-3ffb-be30-9e588d633671 | -7.08477 | -49.59477 | 2025-07-02 04:25:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 824a6b99-4818-37c5-b335-5f7946bd9e45 | -7.20821 | -40.24161 | 2025-07-02 04:25:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34e22e62-e63a-3be8-8e30-d1c4390ab8c9 | -7.81919 | -44.02692 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| b6d8bd7c-46e1-352a-aef2-e26b55637fc4 | -5.62296 | -43.65519 | 2025-07-02 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83044b38-e36b-37f0-89e8-dfba1ec68542 | -7.80872 | -44.0217 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 616b1b6f-fd48-3e51-83e2-38fe0836a511 | -7.8046 | -44.02514 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93a0ce14-9082-3fb9-8236-07eefe441fae | -7.21302 | -43.08357 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7a7d082b-df0b-3da8-afe0-8fb079dcae49 | -6.2738 | -43.68526 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e5e2c8ff-1763-37bf-902e-303178895bc7 | -7.21435 | -43.17635 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91fa831e-ee2c-39c0-add8-7254942192d9 | -7.79343 | -44.02748 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 630134e7-b7a7-37fe-a2c0-555ddc6917f5 | -7.61712 | -45.75477 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58a16463-7ae0-3055-903c-a7705f0a07e5 | -4.28199 | -48.18242 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be46db6b-8b70-30a2-a4c9-70cdbbaf787f | -7.20631 | -43.07811 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d1670f14-ed4a-3ab0-8344-a0393244a19d | -7.61047 | -45.75373 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b44b728-956a-3364-b5d3-efe1304c86cc | -7.51219 | -47.36384 | 2025-07-02 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 156e2ae0-507b-3b57-9197-fd09165446f7 | -7.79171 | -44.01503 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ece07c9-9579-3d31-b60f-5275358fa1f4 | -7.21238 | -43.08792 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ee1ef2fb-6b90-3614-958d-fe4531e2851c | -2.5846 | -51.92519 | 2025-07-02 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23ab5755-2ea3-38b9-8dc0-4b167b534adc | -6.71045 | -51.41701 | 2025-07-02 04:25:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 47bd9dde-e5b0-3084-b2b3-2d699861fdf5 | -4.3753 | -48.08062 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f9e383-7ac0-3970-8d88-93f3855d98e0 | -4.37367 | -48.0688 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb61cc0-b570-3601-b5be-03931a328e25 | -7.1961 | -43.17357 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdb0ec9e-e0fe-3699-a9cf-b6e193e8af56 | -7.80933 | -44.01773 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0925f43c-e40a-3bca-aa30-a17c08d97a9f | -5.62485 | -44.26702 | 2025-07-02 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a7a1cca-27bb-3ab4-abac-97ff985ee70d | -4.31663 | -48.07563 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d2141e-c73c-36ce-a837-bb5b6da554a2 | -4.28424 | -48.19055 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3fa98d30-809a-358c-8210-f26cbcc6e190 | -7.09102 | -44.38139 | 2025-07-02 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d475ed74-1bf9-3e8c-9350-8e65555df379 | -7.80399 | -44.0291 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bf083a24-7e7d-3b6e-8e2e-742db56ae8b3 | -7.60714 | -45.75321 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b36daf6-b8ce-3932-bd41-f8f89317f602 | -5.07126 | -43.73359 | 2025-07-02 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| edf46bb1-7034-391f-b554-daac3dd393a0 | -7.8058 | -44.01719 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| c9ab1a4c-7a21-3304-9a4a-c32a002d53d5 | -7.78055 | -44.01738 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5efb5e4-bb9e-34d5-9f35-295c91dccf1b | -7.80752 | -44.02965 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3a42fcd6-33f6-37d3-9362-0372f7602751 | -4.41082 | -42.14969 | 2025-07-02 04:25:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c9e7669-1b4e-33d7-b9c9-23794599929b | -7.78467 | -44.01395 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb24e3bf-89bb-358f-b529-645990f17632 | -7.16354 | -49.5154 | 2025-07-02 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3d8fe22-82f7-3245-a8c2-072b32816b6b | -7.81164 | -44.02622 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 96099cd8-c71f-35f3-a48e-83763bef6395 | -7.21908 | -43.0934 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9ab2d600-6e2a-31d4-b5b9-473cebe0e1a3 | -7.20871 | -43.08738 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e1081b54-5641-32d0-bb4b-6aba7395c9ba | -7.30229 | -45.3689 | 2025-07-02 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6253eda1-a1ac-3c5d-9e8c-d98c422054f2 | -4.12537 | -43.06887 | 2025-07-02 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 135a79b9-26fb-3bc8-9dd8-6398be69348c | -7.21541 | -43.09283 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 615524ee-08f8-3370-b6bb-71b1e4f9ecc7 | -4.31829 | -48.08742 | 2025-07-02 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0b9e4ea-1f8f-3c7d-ae35-9fee5a12d71f | -5.88043 | -44.79952 | 2025-07-02 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ae2bee3-439f-3e1d-990b-7719bfaf650f | -5.91747 | -43.45514 | 2025-07-02 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d66d73f8-7dc4-3b87-85a3-e517e93a3738 | -6.6628 | -43.84461 | 2025-07-02 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d87cd5b-e830-3beb-abf6-ee536e385705 | -5.77968 | -43.62191 | 2025-07-02 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a990cdd0-c552-31fc-91f3-815730a203bc | -7.212 | -40.2466 | 2025-07-02 04:25:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5297fed6-fe81-348e-a778-6f8fa3c64f43 | -4.17184 | -42.0325 | 2025-07-02 04:25:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3259d543-2b78-3fd5-b52c-98e3f403250f | -6.27605 | -44.20321 | 2025-07-02 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06271e57-1fb0-3b7f-b910-917d7c1eebc1 | -6.29612 | -43.68059 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a10aee93-8669-3698-b3e4-ad0212a687ff | -6.89878 | -52.19373 | 2025-07-02 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b94e64b5-a26c-3411-b508-91691d879d34 | -5.91393 | -43.45457 | 2025-07-02 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9e0f543a-e937-3daf-b120-1014ca08a643 | -7.80168 | -44.02062 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 8baf751a-810e-3587-8e17-029a38161775 | -6.9575 | -42.8903 | 2025-07-02 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2b66c3b9-e8be-31e0-b31a-b56d82b8a81d | -7.61434 | -45.75074 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd39be75-6df4-3e7f-9d5e-a08fe1471760 | -7.79111 | -44.019 | 2025-07-02 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f853e42-3afb-3f4a-9106-01ae62863ac9 | -6.21055 | -44.19772 | 2025-07-02 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76cabd55-9138-3e42-8ba1-9147a08193de | -7.60993 | -45.75725 | 2025-07-02 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f64a0746-5c3a-3953-a488-e30db986de92 | -6.27087 | -43.68076 | 2025-07-02 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
