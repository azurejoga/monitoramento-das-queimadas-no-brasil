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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c100df43-190a-303c-8e25-a133fbbb8678 | -14.92568 | -47.13578 | 2025-10-06 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd013e8a-e774-328f-a887-de432b1df093 | -19.93922 | -44.64653 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 11024cbe-1cdf-3576-9988-0afeeef2dfd3 | -14.67786 | -48.38953 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fdb1da89-231e-3429-8b26-be8176e74012 | -15.34969 | -47.99863 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eb7c982-3cfc-3dcd-ac41-78bc9cc2f2ce | -15.92124 | -48.61968 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10c3d1bd-16a8-3ab4-98de-d125322034ba | -19.89091 | -44.78712 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05dd239d-be34-38f7-967c-af006734568e | -21.17065 | -43.57032 | 2025-10-06 03:38:00 | NOAA-20 | DESTERRO DO MELO | MINAS GERAIS | Brasil | 3121506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 16b9c6b5-03b8-308c-9f44-4c883bf2570a | -19.50315 | -44.17323 | 2025-10-06 03:38:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccbc32d5-52c7-3ddd-a7b7-399e0aee78f4 | -14.69561 | -48.29993 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce5b936d-7679-309d-b78a-8d7c45461dc3 | -15.87876 | -46.26332 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4d59a67-90aa-38f1-b9c1-2c0197385b64 | -13.62954 | -48.7258 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4998977-c6b2-3807-babb-b24738b1aaac | -13.36323 | -47.57186 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee1440b9-7f0c-30df-a4d6-a7a0d41ddcc3 | -14.90986 | -46.85429 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05cf9531-92c3-35b0-a284-ffff24b89cb0 | -18.0071 | -44.99695 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17b8b239-1db2-30c8-899a-20bad4fb7b71 | -21.30272 | -43.84111 | 2025-10-06 03:38:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7a1cc1ef-ec70-3fe8-9779-3dac90746312 | -15.50997 | -46.84336 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d9a6e33-8063-3af7-ae89-2974aa7918ae | -15.28815 | -46.32414 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b36dfd1b-1803-3e47-b2c5-512e947374af | -21.40314 | -45.05455 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2dec9ea5-f5da-37f4-aba9-9f7ed2af0a3f | -14.56036 | -46.66641 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f6fe899-88f7-3746-850a-015b9cba24b4 | -18.27069 | -45.41744 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2442c93b-ae0e-3655-b5ee-536a69dd3057 | -15.73547 | -46.25906 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2f5c309-6be9-3958-8818-a54a4cc2b676 | -21.40204 | -45.06002 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0f470bb2-1380-3462-9d99-26202643d262 | -14.90881 | -46.85919 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a0f1458-8d15-35e1-8028-f56deffe2d01 | -14.26855 | -45.86738 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e040d9bb-770c-3c08-b2d5-09eedca5806e | -18.02018 | -45.00274 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37d9d7bb-4cde-3bda-b4a3-d69cfaeb832a | -14.36157 | -47.72648 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90b94437-0a95-3f8a-901e-1aa4e495a82f | -18.39635 | -45.22341 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 17427495-0f6a-3be8-922b-d40d5e5470c8 | -14.90981 | -46.84643 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d03b24b0-e4a3-3ba1-9ded-b0a564441d12 | -17.5875 | -44.4535 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9a15735-d142-335c-9e63-9de309d7a4b8 | -14.26777 | -45.87127 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 620dc35d-dbf0-37b6-bb68-d98e28dea749 | -14.92273 | -46.82343 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4af7052b-0498-3732-9e95-a218fd18ab21 | -13.37498 | -47.57694 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4d9c243-734c-3559-b27e-33ce349d9cd2 | -14.3075 | -45.85674 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cdc1dc1-9b63-3346-95a6-cbb3a400f549 | -17.96886 | -45.0038 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d4cdab-ab53-31c6-af32-cda44faf5bfe | -21.38319 | -45.05527 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ba517268-37f5-34be-b064-8351b5c2acd2 | -21.39128 | -45.04097 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b12b3277-28e5-330d-895a-af6b9b42252e | -18.38633 | -45.22058 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d566749b-2701-3dca-83f7-131aeec3ea32 | -21.39373 | -45.07642 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0a877e74-2a5b-30d0-ab6e-4f0f3b905beb | -14.55326 | -46.64108 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d4a6bad-a021-3799-8b0a-e59a700e2a06 | -18.39264 | -45.21559 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0da75e9a-cd0e-3ae4-a270-54aee4093dd4 | -17.65935 | -44.4334 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 316486fb-cb6b-3bcc-b1ee-7288bcd92fe1 | -17.24785 | -46.91606 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 754282f1-a738-3df0-ab82-de14a3b18bd0 | -18.0127 | -44.99524 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f57fc65-722a-3dd1-b580-9c102695f32c | -14.35481 | -47.72698 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627b7bb5-853d-3a08-a858-64cdeb785e6b | -14.32936 | -47.65973 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3de10a7-08e5-34ee-8418-e957bdbde26e | -19.01611 | -45.03181 | 2025-10-06 03:38:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.3 |
| dc02bbc6-ae8f-367d-8e16-dfc6fb91a352 | -18.01594 | -44.99788 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 515cb4a1-8bba-3d14-8cf2-cae1807f7cb3 | -15.55721 | -46.83939 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d27629d0-ab59-3b22-a023-c01d758ba060 | -17.60236 | -44.45583 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 686d0796-1aad-3090-a630-de26b4c82f89 | -17.24702 | -46.91993 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db8d51b1-d29a-3bd2-83ff-aa6603372eff | -15.1588 | -45.74575 | 2025-10-06 03:38:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6ddc24e-b6c3-3d50-8d9a-b560e5607366 | -15.75198 | -46.26535 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af7e7de-8839-397b-8ec0-7d2ece24a554 | -17.24599 | -46.92473 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fcba0e8-96fa-3d28-9c76-b5b80fc09b0f | -14.34332 | -47.71844 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c2602d-8a77-3691-a579-a7e657c2691a | -20.11787 | -44.40607 | 2025-10-06 03:38:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 10672b87-88be-3391-862c-0efb29473334 | -15.37986 | -47.98232 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57ece52d-302d-3f75-9869-ff1df63356ca | -14.69466 | -48.3754 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cfca6b63-5dc6-3f7e-8b73-b9eabf7f17b9 | -14.90483 | -46.84858 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa8da980-0f49-3ff7-a7ca-c3d636591611 | -16.32496 | -41.94809 | 2025-10-06 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 226563b0-1f41-398d-8ce3-96916277dd80 | -14.5486 | -46.6522 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c731d04-7e7b-390d-b714-3491c7a33ee2 | -15.26041 | -47.14762 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abdda67f-731a-36b7-8265-3ff49975b06c | -15.86966 | -46.25001 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 886d3fb2-a62d-3781-86c8-4291d43ca5b4 | -16.34347 | -47.05824 | 2025-10-06 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d688461-0f54-3ed7-a2e6-e7ee95b7418a | -14.34969 | -47.71976 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84c1798-792b-38be-988e-36568b82404f | -14.92179 | -46.82782 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84d00615-f1cb-3e0c-8f2c-b59c9bca1b83 | -14.54768 | -46.65674 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bd850df-c555-3a14-ab35-47e922c9b660 | -14.71067 | -48.36484 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 175e2edf-dd8e-3d69-af1b-b7c91a7bfffc | -13.35687 | -48.03772 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 576f26d8-3fda-3da5-a5a8-3d6fad2766f6 | -20.91612 | -45.25487 | 2025-10-06 03:38:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b08a6835-3474-32c8-820a-1d317c3b3ecd | -14.90589 | -46.84365 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdf8f25f-cd48-3f00-b616-67f776f61061 | -17.95982 | -48.5551 | 2025-10-06 03:38:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47806cde-4697-339a-a2e7-b3e468f58f3c | -13.2563 | -48.46603 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0651046-b2e1-361f-9a9f-96eea0329bce | -18.38828 | -45.21103 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65375973-32af-34d8-8333-f24b4b972d4d | -15.87318 | -46.26162 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c3e1c84-fb25-36f3-96cb-2f89dafa95cf | -20.66548 | -42.28765 | 2025-10-06 03:38:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cccd41d9-e9c0-3710-8fe6-87f84915841b | -16.23679 | -49.65998 | 2025-10-06 03:38:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2446d460-dd69-38b3-a5b7-98def6e79dbb | -19.93452 | -44.64526 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 61592a4a-a2ff-3e42-8072-0d37fc4ab374 | -14.91219 | -46.84343 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2c347aa-380a-3e39-9cab-23dde0bdda94 | -15.16881 | -45.77124 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c5854f5-857d-3488-8b00-5a0e6b82563c | -13.36958 | -47.57358 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9bd2a76-2217-3e94-b9ad-1ee79dbd1725 | -15.29276 | -46.33084 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeb8f92a-cff9-36c1-a8f8-ee2ebae3841a | -15.31304 | -47.31882 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bb544f7-d39e-331e-af38-457038e09bed | -14.67516 | -48.33837 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d7a853d-6c8a-33b8-b728-f21f88a3defd | -14.68812 | -48.37387 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c04b9135-a9b5-3f2c-8c03-775d682285bd | -15.93156 | -48.6091 | 2025-10-06 03:38:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd99e820-83de-39db-aba2-5e00cd84063e | -15.75861 | -46.2621 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c980f203-739f-34b7-8309-1e0c11135f5f | -15.33332 | -47.31363 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49ad23eb-a1e1-36cd-96ae-d048164f194b | -14.55941 | -46.67097 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab545971-e404-3ac0-98a8-3da43b943294 | -13.728 | -48.07248 | 2025-10-06 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6fc14bf-b18e-3959-b79f-5bfe9f6a3642 | -21.30177 | -43.84579 | 2025-10-06 03:38:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fe13595-f7ad-36e7-90df-fbeb6dbaa0d6 | -14.64966 | -48.36091 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24e4c46b-8643-3347-8a37-be4629ff1e8e | -14.91836 | -46.83528 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cc25cdd0-7d28-318f-b1bf-7cf85bd6fbf1 | -15.32555 | -47.3201 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faff2fd2-98d8-30c4-954f-ae30f84d952a | -14.36013 | -47.73323 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 668ed5e4-82aa-3c37-b97e-db47759053f1 | -14.92651 | -46.82605 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bca841ca-568d-39b6-a7ce-b0adf816a3a2 | -13.55601 | -47.2357 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10a3b51e-dbdb-3b89-96d6-52c012d99646 | -14.91181 | -46.83678 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c651fb32-852e-33e5-88c9-040f1b41ef26 | -14.68702 | -48.28354 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6f57489-4cc4-3428-a661-137d3f47cc70 | -17.59247 | -44.45419 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50716aeb-272e-3dea-a975-38cb21d79f29 | -15.67687 | -46.2827 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README18.md)
