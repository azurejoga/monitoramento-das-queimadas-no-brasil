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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90f63225-9d14-3acf-92e8-7ba3cacfd902 | -23.13019 | -46.83025 | 2025-09-09 03:47:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e45c3c75-6f1c-3689-84ab-01c4e2970d0e | -20.07394 | -47.36123 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a93b2b0-2a0d-3b3e-a7e6-fac639f147ce | -20.08146 | -47.35909 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be5c1e3-daa3-3251-be1c-7a9a8085bcd2 | -23.15552 | -46.14212 | 2025-09-09 03:47:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1b8bad2-ddab-314b-967f-a0c4903ddc05 | -19.82842 | -48.17224 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5cc3d07-609a-3193-8cbf-766ba4850397 | -21.43255 | -48.8681 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d52f8a14-c9b7-3661-873f-60078bf4154a | -22.92919 | -49.16564 | 2025-09-09 03:47:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d6962fb-e4df-37db-957c-283e3f1258aa | -21.43746 | -48.84593 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af44cae9-cb79-3614-a607-9f82afc8c6c5 | -18.82665 | -49.69524 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 80434379-0337-3a77-8c79-159ccd73fec9 | -19.79067 | -47.99507 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2efa28-629e-3f16-a1d8-17c72adb1f41 | -23.56279 | -47.17085 | 2025-09-09 03:47:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c373dbb4-12ca-323f-bbee-3eaf1c086805 | -20.34073 | -42.24678 | 2025-09-09 03:47:00 | NOAA-20 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0068ba86-e577-3eef-9a2c-05758065fb9e | -18.7881 | -49.66035 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 846ef79b-ae50-3447-bf34-0f1123ab44a3 | -20.07324 | -47.36447 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8bfd307-7533-362e-8ddc-d6dd213b5e9e | -18.4716 | -49.56223 | 2025-09-09 03:47:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28703896-3b36-333c-a1e0-4364681ac976 | -22.32401 | -48.81291 | 2025-09-09 03:47:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7a6bc3-97ff-3959-aa67-5a0f95a4d3b1 | -21.62878 | -45.39803 | 2025-09-09 03:47:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5eb1c7d-71b1-3c14-af3a-2a9f1ee8be59 | -21.43291 | -48.84097 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5779543-faea-3afb-ba31-4b9ec04491be | -20.1735 | -44.79948 | 2025-09-09 03:47:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8133f156-773f-3193-b8f4-7d7aabd130d0 | -18.82886 | -49.68544 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| da29ad0d-99f1-34e2-8e4b-9990a3ec7c74 | -22.68546 | -46.35381 | 2025-09-09 03:47:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d360f024-5470-3a19-bc72-71322af9ab98 | -19.89402 | -48.20483 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fdbf016-24ba-36fe-9a61-cf565adddc7a | -19.94006 | -49.28631 | 2025-09-09 03:47:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4917c194-feb3-3949-95cc-91fe45f75457 | -21.43931 | -45.34307 | 2025-09-09 03:47:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6388f0b7-98df-3edb-aac9-0d5d4a2a9404 | -20.00335 | -46.957 | 2025-09-09 03:47:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77b75c6b-744e-3aed-8721-e5a2ae740557 | -19.90838 | -43.8512 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5ad06112-4734-365f-800c-081464cc87ad | -23.5731 | -46.32351 | 2025-09-09 03:47:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a20c6231-c822-38b2-8634-3b6c2d763b01 | -19.65187 | -44.90653 | 2025-09-09 03:47:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f9f05661-a3c7-3dc8-85ac-d09cfe05ed4e | -23.70794 | -47.33424 | 2025-09-09 03:47:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e433fe44-89dd-378a-84a5-216da0f529c1 | -21.09533 | -45.93007 | 2025-09-09 03:47:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f640f74a-afaf-3666-9680-2d35f8cc0de3 | -21.44408 | -48.86712 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0c2db30-bbe5-35dc-a046-f9c3d93402e3 | -19.70917 | -43.52763 | 2025-09-09 03:47:00 | NOAA-20 | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fa6f206-ef16-316e-829f-847d3b0535de | -18.82505 | -49.67463 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cf7a3103-a9a2-3e51-b5fc-851998f9c108 | -21.44978 | -48.84124 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 2c9164c8-f98c-3693-948f-ce1560347a4a | -21.01855 | -48.41985 | 2025-09-09 03:47:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb075532-ae48-3db0-bcc6-bb9b23374cb7 | -23.21064 | -44.9356 | 2025-09-09 03:47:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb82bd8a-55c0-3bb2-b949-075abef92946 | -20.03072 | -48.53568 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d8b1e3b4-7e97-3032-8678-1ee935ae8a3a | -19.3632 | -47.46576 | 2025-09-09 03:47:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30054168-842d-39e2-a2f7-b86f67eef4fe | -21.44037 | -48.85832 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ea642ed8-7cfd-3096-a3b7-dab772012cc4 | -18.73177 | -49.63319 | 2025-09-09 03:47:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36bdbf7f-97a6-3ca8-8ab3-c16d626d02e8 | -19.47357 | -46.13181 | 2025-09-09 03:47:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4a68723-8282-30e2-8836-0a681a493fbb | -22.22252 | -49.72538 | 2025-09-09 03:47:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 25e7615c-a3ed-35ea-b4c4-734a8f1926ae | -18.82821 | -49.67652 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2c341299-faea-390f-b385-e51aa21e4315 | -19.90376 | -44.55053 | 2025-09-09 03:47:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df5c6219-eb61-3754-a0ac-98a41e80dfa3 | -21.00358 | -46.05722 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5035f962-f43a-30f8-ae8f-50f66b516a72 | -21.00305 | -46.05774 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fec5e936-c3a2-34bf-aa43-e72b4c6b656a | -18.8191 | -49.67332 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11da98de-eac6-3f96-bcc0-fb64e1cdf20f | -20.07464 | -47.35791 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a731024-be73-3603-89d6-230fda1fe0ae | -18.82397 | -49.6794 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0be3f570-d6fe-3c7b-b6fa-6294f51181b2 | -18.83151 | -49.7014 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7fea4773-cd50-3a86-8f18-abcd828d5415 | -19.90429 | -43.85052 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2786f181-42cd-3799-bba8-2f95fd5e7986 | -19.89477 | -48.20128 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b73e254-9665-3fac-9d6f-5b8fd1190d51 | -23.1297 | -46.82729 | 2025-09-09 03:47:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2f8e842d-942b-3879-ac97-82691a9230da | -21.44523 | -48.83628 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1375a1e3-89a3-3df8-9d6b-101c8d42074f | -19.99353 | -46.95476 | 2025-09-09 03:47:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c8f4218-59ff-3be3-8985-8207d7b24bde | -19.90468 | -43.85142 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1e0e02ab-4365-38a6-9f61-7b71a2c8f0e3 | -20.17434 | -44.79521 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 643386ed-b078-366f-a543-31fef56a5195 | -19.9313 | -43.61733 | 2025-09-09 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6ac8852d-feec-3654-b91e-c8a611f08732 | -23.48799 | -45.43341 | 2025-09-09 03:47:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f90be090-a588-3ad2-ba85-807cb130c8fc | -22.32928 | -48.81408 | 2025-09-09 03:47:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7e7da645-1e3d-3387-9f31-b7da3ff243f2 | -21.44201 | -48.85087 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 13e76d51-7a86-3c8d-9701-b6ff7426b13e | -22.32324 | -48.81635 | 2025-09-09 03:47:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd57aa9c-052b-3ae9-a14c-d38df78fc983 | -19.73355 | -43.91171 | 2025-09-09 03:47:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d9a3ea9-4607-38fa-b3ae-3f774e751bdb | -18.7891 | -49.65582 | 2025-09-09 03:47:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0ba0da9b-58a7-3186-8eeb-5db80c904c48 | -20.0299 | -48.53936 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c5cefa8f-9a90-3bfe-b036-84a808d79a53 | -19.92637 | -46.17191 | 2025-09-09 03:47:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d143fe08-a870-399a-8657-b6bf315de037 | -23.08745 | -46.96796 | 2025-09-09 03:47:00 | NOAA-20 | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e9a5acf-0380-3c3c-9216-fa5ea5188970 | -23.22276 | -46.61072 | 2025-09-09 03:47:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 70bf9b6f-2c38-3b58-be7e-535a730241e8 | -20.53166 | -43.97438 | 2025-09-09 03:47:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ac995bdc-18f1-3173-8bfc-e93284f361ca | -18.8326 | -49.69659 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ec854bef-4932-3cd5-950b-1d0cb832d854 | -21.23364 | -49.88776 | 2025-09-09 03:47:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3b1e85f-6768-3ec3-b223-08ca87f436fd | -18.81736 | -49.66911 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 014c749c-6c6a-3777-aecc-3ed77b7cf990 | -18.82609 | -49.68623 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f9cadeb9-42d6-3f4d-b24e-42c13b28ef4a | -19.92799 | -43.6128 | 2025-09-09 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9703b88-87d2-3a9c-affd-6e6c001b9e6c | -18.81326 | -49.67153 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0acef13-976c-3285-87cd-815a5a6a2573 | -18.73673 | -49.63886 | 2025-09-09 03:47:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a7e13e2-78eb-3c42-a820-3dcda3d6e3ff | -20.53563 | -43.97457 | 2025-09-09 03:47:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ef24f5f7-2e6f-3377-9638-614d5ca0821a | -19.7254 | -43.90999 | 2025-09-09 03:47:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a3de57d-addf-3856-979b-bb1659ad4ef2 | -21.62964 | -45.39365 | 2025-09-09 03:47:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0bd6c5f3-a589-3d5b-aa41-4db163aa4a4b | -19.93199 | -43.61359 | 2025-09-09 03:47:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d0721e8-8baf-3c9d-92c7-829fb9c38c33 | -19.99844 | -46.95588 | 2025-09-09 03:47:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 213543da-b5e8-3b7d-8b72-3fbbd3e19df9 | -21.90944 | -46.66457 | 2025-09-09 03:47:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8dfbd53e-75e1-3554-8b0f-7afe802d24d2 | -20.53162 | -43.97356 | 2025-09-09 03:47:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1f9b6f58-89e8-3d5f-83ba-cb5400651afa | -18.8337 | -49.69167 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73149588-9c03-386f-9ad1-88e45076d121 | -18.81635 | -49.67374 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaf2a3da-6d16-3f21-8c17-af80d0278940 | -20.02447 | -48.53479 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8184a4d-1caf-3acc-93d0-d3d7d1814b0e | -22.89646 | -43.58564 | 2025-09-09 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f28c4b2-c996-3e64-bb4d-a8b081b1c552 | -20.53567 | -43.97539 | 2025-09-09 03:47:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 876d8bde-ce97-3192-bb62-295ba637f7fd | -18.82399 | -49.69587 | 2025-09-09 03:47:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3e372241-0012-3f0b-8afc-7cd6ff30a8ea | -20.912 | -44.0488 | 2025-09-09 03:47:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8b5a7fbf-2d8d-38d7-8f79-6d594583bc6e | -20.02906 | -48.5399 | 2025-09-09 03:47:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d0ebc0cf-f31a-3c9e-a326-82be2594fd2e | -20.17009 | -44.79417 | 2025-09-09 03:47:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca8f78fa-83a9-3d3c-b67e-70d7f9e34c1a | -19.07854 | -47.26324 | 2025-09-09 03:47:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4aa7187-b0b1-3e82-913a-8892b87bd788 | -19.90354 | -43.85447 | 2025-09-09 03:47:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ac8e565a-f4f5-3a21-8cd8-9d519ee50301 | -21.32272 | -46.69357 | 2025-09-09 03:47:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d7567e50-f74a-3013-9754-1eb6d749fb4a | -21.6302 | -47.02946 | 2025-09-09 03:47:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 591912bc-955d-3d1f-974e-1afcf1e6076a | -21.44283 | -48.84719 | 2025-09-09 03:47:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 91284617-ad97-3b19-866e-d02e5652e1a6 | -19.78542 | -47.99378 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be2cad1-1524-34f1-a5e7-37ab8cce632d | -20.0701 | -47.36311 | 2025-09-09 03:47:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9555c0e4-6556-3365-b226-64b19f303fdc | -19.82391 | -48.16726 | 2025-09-09 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
