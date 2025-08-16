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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9305f679-1dff-3cd8-9334-ca2d2c073c84 | -14.94687 | -54.76133 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 494a4414-f302-32dc-b498-d7c9c1e1b9fa | -20.4056 | -42.39921 | 2025-08-16 04:12:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9a133af3-7cf5-3d87-ab1b-1acda0ca5b42 | -14.94233 | -54.6945 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ebb05efb-4b33-3fae-a6e4-38d5814d12fc | -16.2406 | -51.12854 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7455e78-d152-31c8-a3bd-ccb220388843 | -13.1127 | -57.13665 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dadc4185-b5db-34f7-98d6-22430265a734 | -17.61173 | -46.67961 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 06d7cf35-4c39-3a57-8016-e4d4f032942e | -17.21559 | -49.59346 | 2025-08-16 04:12:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e73f62d-a599-358d-b666-e7649d283f1e | -14.96541 | -54.73306 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88b01cc1-4bed-378e-a4b3-6d0dd939ad72 | -14.59189 | -47.90961 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2b64b1f9-611b-3af6-b4a4-1d23306c8502 | -14.49268 | -42.17949 | 2025-08-16 04:12:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f21e1e35-2522-38c5-93ed-52375dafd5a5 | -17.5089 | -44.88492 | 2025-08-16 04:12:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21bb0fbe-c8c2-3df8-b1ba-6f43491b63b0 | -17.21484 | -49.5975 | 2025-08-16 04:12:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0d11384-1bf5-35bb-9d8f-9595fc2591e8 | -13.63153 | -49.84081 | 2025-08-16 04:12:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d94f21b3-5701-3429-be07-d7a2b6bec63d | -16.23229 | -51.12151 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0f280c5-9473-3e33-bafc-7797344f8c08 | -14.58798 | -47.90892 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bdd924ad-a3dd-3338-84c7-1864d167de0f | -14.61347 | -47.92453 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d05b6845-3c50-3d2a-b296-6dc7105fb77c | -14.95674 | -56.23988 | 2025-08-16 04:12:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88a991fa-a82d-3291-8901-ad00e333b13d | -15.62363 | -47.84993 | 2025-08-16 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7772294-91ee-33d8-ba04-637b00856e47 | -20.29566 | -41.34996 | 2025-08-16 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bed89363-7279-3312-9176-d8586fc10399 | -14.58735 | -47.93525 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42bf1ddc-9f5a-381f-9414-7065d417baf5 | -16.87454 | -44.13703 | 2025-08-16 04:12:00 | NPP-375D | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6423da34-22a9-3635-8058-b41acc46e583 | -14.93822 | -54.70853 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0a1ffdc1-0db3-3e59-acff-31e4ea503b3c | -19.64918 | -40.20072 | 2025-08-16 04:12:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d47497df-f4c4-30d9-9838-7ec81308354c | -17.21632 | -49.5895 | 2025-08-16 04:12:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bfa07ac-b412-349a-84dc-8200a33f8835 | -20.04709 | -44.6321 | 2025-08-16 04:12:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5eb8aee-f3bd-3e8b-aea7-ee807677948c | -14.93927 | -54.70343 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 04c3122e-000f-364a-bff2-2bc3ff3beaa6 | -13.00391 | -56.87426 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e5cd008-46d9-330d-a7e9-d407c34fef10 | -15.62189 | -49.27119 | 2025-08-16 04:12:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40b72b19-8707-3d5a-889b-87feb266a1d9 | -19.53418 | -43.62654 | 2025-08-16 04:12:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99f8caa6-53b1-3aed-a0f8-e3cd910f90da | -14.94039 | -54.69799 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 617260a6-de22-3a35-b94f-fa11a2d53235 | -14.94114 | -54.70008 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc00c8a9-6a80-3c07-9e39-dba3da3e0dcc | -13.12563 | -57.1333 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f1c7f77-b35f-31c5-aaef-2d5f180e94ab | -14.94737 | -54.70016 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 455e3548-76cf-3414-ba61-c47fe4e4ac44 | -13.12144 | -57.13076 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 695a23ec-b99e-33d9-8bd1-d6c5405178e9 | -14.52626 | -48.58006 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c025ef3a-af5a-3c7e-aa56-eb4fc0f49d75 | -20.29984 | -41.34654 | 2025-08-16 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c0d62f52-0c75-3d48-890a-8e2356ab0fb6 | -13.12744 | -57.1709 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b413f9f-300d-318c-9cee-844fbac0e96a | -20.2926 | -41.34531 | 2025-08-16 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9210ff84-dac0-33bd-8267-4f200f80d58b | -13.99345 | -49.64537 | 2025-08-16 04:12:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f168f74-b9a8-311d-b529-5e4f0135582a | -17.61525 | -46.70148 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae82213c-f38e-3e18-8f16-6f926349f50f | -16.68248 | -41.349 | 2025-08-16 04:12:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 00d99c4c-c7fb-34a2-8e7b-7359b862caa4 | -17.57054 | -47.99954 | 2025-08-16 04:12:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6d54dce-f2fc-3dc6-a30f-776de4102280 | -14.53034 | -48.58081 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c86126f-5309-3048-9bf8-29f4418952e6 | -14.60778 | -47.93391 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c01d538a-f64d-39de-a528-b110978cdd11 | -14.97537 | -54.71556 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eba4a7bf-5c38-3875-89ef-9cdda3310293 | -18.12259 | -45.00282 | 2025-08-16 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ed86a2c-59e9-3fe2-bb1b-33dd9b2498e6 | -14.94791 | -54.75641 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10eb57c8-4634-34ac-b049-21c803790858 | -14.93324 | -54.70237 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 871a961f-0d1c-3915-bf52-279b00a86a28 | -19.91982 | -44.7076 | 2025-08-16 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de3d7d87-6bf2-35cf-b95c-70c5f02ee110 | -14.94688 | -54.73184 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 34c9bc8d-5890-34ea-8ff6-cdf854a8f888 | -17.61878 | -46.70213 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbefe38b-5838-39b2-a17b-26f40bad821d | -17.73254 | -43.51963 | 2025-08-16 04:12:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b58e832a-0ec0-388b-950e-0d41a523b580 | -16.23701 | -51.12215 | 2025-08-16 04:12:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61e801af-5646-3d8a-8c30-6425e67e1dfb | -13.11985 | -57.13796 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f68011e9-98a3-35ce-9e07-2b8b66e408a2 | -19.53474 | -43.6229 | 2025-08-16 04:12:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1facfd56-9598-3b90-8b5c-d757571eec55 | -14.94533 | -54.73471 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9166505e-eb6b-317d-b322-b97db5cd2dea | -13.45223 | -56.66808 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e78399db-a6b9-3024-997f-f264646a917e | -18.04634 | -47.72525 | 2025-08-16 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 936423fe-379d-3274-b092-9a16f99d060d | -17.33589 | -46.56056 | 2025-08-16 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 478e2b85-08e5-3607-b2fa-9c8eac5f0a0a | -14.06199 | -46.29189 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e70c1f66-6dd0-35c8-b858-bf184665a5d9 | -14.61438 | -47.91933 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0222220b-c589-3bce-af41-1bbff2636df8 | -19.53084 | -43.62598 | 2025-08-16 04:12:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7845126-8b48-3547-b88c-0ef966eebb20 | -14.05043 | -46.29428 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15609b27-f27c-3cf6-ac30-beb10993e10b | -14.94439 | -54.73928 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f9d7ae26-31dd-31db-a3ea-a2800b4bb355 | -14.94093 | -54.75975 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80159d45-0901-3807-b0e2-4dd46ae44bf8 | -14.94197 | -54.75486 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61e479a8-80d4-34a2-8ee9-347b721f3a26 | -14.94587 | -54.73658 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cca01ebc-9f72-3e28-82ab-3013f2af403b | -13.44211 | -56.68772 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28675524-b5be-3763-9e26-28811d8ffaee | -14.93223 | -54.70725 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a8f38b58-3d3f-398b-9849-81fe778fad01 | -15.893 | -48.31685 | 2025-08-16 04:12:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c3e0d43-e1cd-3828-851c-b865945c9154 | -17.6068 | -46.68717 | 2025-08-16 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4235437b-da38-3f12-9f08-cd928a279ec0 | -14.97039 | -54.70955 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebcfe020-7b3b-361b-8f0d-7db2b3d96fb4 | -14.05116 | -46.29008 | 2025-08-16 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7d21803-f9b1-36f0-8c36-c099db4c0186 | -20.29927 | -41.35062 | 2025-08-16 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4365b699-a948-35b5-b49c-1b3c455e8b17 | -14.59097 | -47.91484 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3920e268-2aad-38a3-8f0a-061492ecb83b | -18.72499 | -39.81562 | 2025-08-16 04:12:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d28997bb-48fc-3be2-bc91-b98c4f538f04 | -17.21291 | -49.58472 | 2025-08-16 04:12:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d70dbb5-6c92-3050-8c79-04fda635d946 | -14.94087 | -54.73066 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 26d56b41-37c9-324f-8fef-b2cdd09b4b98 | -20.40436 | -42.40039 | 2025-08-16 04:12:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 893f832a-7394-39d8-bccf-a7fa3b9b908f | -14.53441 | -48.58158 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df488d47-f220-3b91-bae2-c27d63a995c1 | -13.10988 | -57.1375 | 2025-08-16 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a3530c-f71b-3924-be30-4017507673d7 | -14.52016 | -49.38899 | 2025-08-16 04:12:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baf19c4f-c879-36b5-8349-24d9108acf58 | -19.36407 | -42.93356 | 2025-08-16 04:12:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 69c69090-3713-31cd-bc39-e6bc834df50f | -16.30483 | -52.92242 | 2025-08-16 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05bf6e28-38fc-327d-91f6-f8222b37a202 | -14.94492 | -54.74103 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3a751a03-f738-341c-bd5b-17ae99e8e328 | -17.33585 | -45.0293 | 2025-08-16 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 18850ac9-7de3-30b1-927c-5386f480c59a | -17.59563 | -43.19767 | 2025-08-16 04:12:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba5e7f12-da03-35f0-85b3-e85d147c4c82 | -14.96945 | -54.71399 | 2025-08-16 04:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0914536d-f2e3-3cb6-8e54-2095a8efde8c | -20.00697 | -45.5561 | 2025-08-16 04:12:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bfa914ac-a085-394c-8420-0a80a4946175 | -14.93394 | -54.7045 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3a5d78d0-61d7-3cb5-b387-9c7a90f22865 | -14.94224 | -54.71935 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17412a32-c432-3946-b635-639712ae34e2 | -14.58435 | -47.92937 | 2025-08-16 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf726260-2d38-358b-94ec-49ae98138b96 | -15.8969 | -48.31769 | 2025-08-16 04:12:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 071aaa85-7df0-3a51-9bb4-8647a22636e7 | -14.95042 | -54.7404 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1deed7bf-e08c-38e6-92d4-df9b78672d8f | -14.93933 | -54.73346 | 2025-08-16 04:12:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88cbc667-a3eb-3760-8e54-8c7502e42356 | -18.60715 | -45.35459 | 2025-08-16 04:12:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce8dca59-b2d4-34cc-a16f-d52040e38dcb | -15.90471 | -48.31939 | 2025-08-16 04:12:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac463122-a3cb-3afd-ba82-4ff8530be875 | -16.73572 | -49.16083 | 2025-08-16 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d0a0e8-0fcc-3658-8c80-7e147d3b3f5e | -18.48276 | -50.42857 | 2025-08-16 04:12:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bcb0d42c-4744-3348-9cf2-8ab955c92391 | -13.43521 | -56.68629 | 2025-08-16 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
