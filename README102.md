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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af538e48-d8e3-3fe6-8d94-040457335e2f | -15.84825 | -59.59955 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1d34995-0ad0-305c-a293-e78d0ea10b63 | -17.39642 | -47.14171 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3faa797f-d3d9-3a74-a877-5d55f7eaa54c | -13.60761 | -48.03296 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2470599d-4150-305f-85d4-87a19464d801 | -15.27213 | -49.26738 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b7cf303-6f81-3a49-9578-3ea753095bca | -17.73407 | -46.67357 | 2025-09-30 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec0d9675-b1ec-3e63-9181-924691429d31 | -15.92926 | -46.21344 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39a62a5a-09dd-37c4-8c78-f543a98a3f53 | -14.72148 | -45.2398 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59a70701-75c0-324b-a4d0-48c7816d7b72 | -14.66689 | -48.14117 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70c939b-d9a0-3278-b313-7f2436a41448 | -13.7551 | -47.92478 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a770737e-9a82-3237-9755-a3ad6b8b6491 | -13.60359 | -48.03535 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc58cba7-6052-35bc-a346-5f6acfb2ff0f | -14.81471 | -59.69954 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e78bb2c9-6974-3488-ba08-057761d9feb8 | -15.7961 | -59.51276 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bb4e307-ca3d-38ac-8658-1c1609b1c9ac | -20.62479 | -46.18061 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0091fe3c-13cf-3221-b317-00dad62ea550 | -13.75614 | -54.73204 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0afd93c7-ac3a-335c-82fd-0c5bb60069e9 | -15.37735 | -47.07587 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b7309b-e98f-3ab5-bc67-1f520e0cf875 | -13.85217 | -47.95569 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95161af9-8179-3a67-8cb2-6e884bb68fc0 | -16.4299 | -47.03092 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5776cbee-ac98-349b-a8c8-22faa0190009 | -13.72893 | -48.68055 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae0f3df8-7277-3454-ae9a-b45cfedf2bba | -15.76488 | -54.66866 | 2025-09-30 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a9b93c7-750f-3f34-a983-6fdd59390c3b | -15.24991 | -48.74555 | 2025-09-30 05:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 416b9e2e-f6f9-3542-9787-1505e503e90d | -14.76569 | -45.7566 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc0f82a-f52f-36ab-be1c-e0e88732245a | -17.397 | -47.14817 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3adeeee1-a604-3108-96ae-e994388cc3f1 | -14.52274 | -48.44887 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad78d172-9dd9-3c25-b6a7-603a52f1da4a | -14.51485 | -48.44725 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6923c4b0-6c04-3d27-a630-0914c1d17f56 | -16.41948 | -47.01463 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6413e7aa-fead-3676-8bfd-695ae604b33c | -15.27645 | -49.24969 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4660e21b-2143-3af9-9b03-e1a8cf7d5d79 | -15.8641 | -46.23067 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84b5f348-7206-375b-9824-84178a2ad58d | -17.39793 | -47.1386 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51c404dc-462b-31e1-917b-139fdb66bdb0 | -13.65129 | -48.05091 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fd2bfb5-784e-3e04-ab56-97faf39210f7 | -17.92489 | -57.59228 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| be261d56-b9ef-35e6-b4e9-9617e91a3a39 | -15.85746 | -46.2336 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93e2f60d-92e7-3df4-9b13-d509ad0dc531 | -15.71219 | -51.78291 | 2025-09-30 05:10:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0adf1bb0-6856-30c9-922d-74e82d8fc2c9 | -17.89468 | -57.59941 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c46bdf3f-8c73-3ffd-a07b-f6e33d3639ba | -14.51214 | -48.40213 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a0c1eb-7b33-3fea-93e8-05470f69c0ad | -14.54537 | -48.26339 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d23ed02b-1195-318a-99ae-4fb535d3654d | -12.79631 | -56.9613 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a7c8970-0b02-3aa7-a819-90038512561f | -14.52609 | -48.3769 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fcbfed4-7ea3-3e95-a79a-47343c0cb694 | -19.86479 | -44.56554 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2c8b96a7-1549-3b31-8ad9-b2c18b772406 | -13.84541 | -47.49097 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2797207d-b10f-3989-942a-68622081087d | -15.25112 | -56.79449 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5b02b84-98d0-343f-bc7e-d12fd87733a1 | -13.8063 | -47.48311 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64da385e-86ed-357b-99b0-3bb62297dbf8 | -16.66063 | -49.53404 | 2025-09-30 05:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cf4484e-85f9-35df-a95a-bfdfd06ce00f | -23.23385 | -46.78204 | 2025-09-30 05:12:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac9f18ce-5e59-320e-b7eb-e0625c3a1d60 | -24.40672 | -50.67982 | 2025-09-30 05:12:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 24b71798-b80f-34db-be37-21052049349d | -21.31792 | -46.76457 | 2025-09-30 05:12:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 360e8572-75c1-3e55-a66b-202b88ef6fcc | -22.17523 | -46.74102 | 2025-09-30 05:12:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 210d5f65-dc1f-3cbe-b59c-1abb9f94c96a | -22.5176 | -44.6034 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e55c9337-1b31-3596-b58d-da2c38e78081 | -22.16875 | -46.74039 | 2025-09-30 05:12:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2cb36cfe-0dab-357a-9f4e-ecd80470ec4d | -21.31982 | -46.75693 | 2025-09-30 05:12:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 68c802d1-c4f6-3e48-baef-dc26765daf93 | -22.09054 | -55.97124 | 2025-09-30 05:12:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e68d5024-d416-317a-a889-eee1916d50c6 | -23.15637 | -45.73284 | 2025-09-30 05:12:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 05beaa04-a765-30c0-bcbb-83e5ef22c3f5 | -21.85945 | -57.10845 | 2025-09-30 05:12:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6930d127-c35d-38f3-be14-059fc5409b83 | -21.31837 | -46.75929 | 2025-09-30 05:12:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5eb3a4aa-a366-3d1a-a1fd-8160146eea4e | -21.31886 | -46.75372 | 2025-09-30 05:12:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5db702d8-231e-353e-bd29-0c51a17f3870 | -23.15514 | -45.73157 | 2025-09-30 05:12:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 486fdb79-1ad3-34c9-a29e-56cda3673b56 | -22.51715 | -44.61061 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b6735f89-71ec-3a83-a24f-b0b1d9472f46 | -22.38382 | -50.03664 | 2025-09-30 05:12:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bfa975d0-bcbe-30c1-8529-98fdf2baf9cf | -22.09422 | -55.97172 | 2025-09-30 05:12:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 030d3353-bf3e-34ec-935d-c3a9a61be47f | -22.51682 | -44.60568 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e7ffdb72-125b-31a3-bb56-11ee11010976 | -22.50944 | -44.61621 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 23861a35-6e3e-37d0-819f-999792673397 | -24.4064 | -50.68323 | 2025-09-30 05:12:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 023cdd2c-71e7-3cab-93a7-836dd29a4cb4 | -22.51671 | -44.61761 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| a2046ffe-bdba-392c-95d7-c136b4204e34 | -21.31938 | -46.76249 | 2025-09-30 05:12:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 636ad018-2f3e-3a01-b64c-5cce7ced90e8 | -22.52483 | -44.60556 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ffc5ac6d-3707-31a4-b34b-13d56247c868 | -23.16206 | -45.73227 | 2025-09-30 05:12:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 763304ab-7ce0-3667-ba51-7050220f91b7 | -22.38159 | -50.03498 | 2025-09-30 05:12:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ce3afa1-3d44-3586-9c22-9183ffe21211 | -22.33349 | -49.48083 | 2025-09-30 05:12:00 | NPP-375D | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cf1f6839-9c76-378d-9c51-ee1c1b892b18 | -22.38126 | -50.03849 | 2025-09-30 05:12:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b19913c1-2587-3646-ab48-52ee87b7229e | -22.52404 | -44.6079 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d207b8a4-a498-371f-903c-22bb11c389db | -22.38687 | -50.03598 | 2025-09-30 05:12:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a66f0849-9133-35be-84c9-d9d4e25e449d | -22.5091 | -44.61102 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b34bad72-d69c-35c3-b591-b35116acd225 | -21.31339 | -46.75637 | 2025-09-30 05:12:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e0e95f44-e837-3f8d-9ecd-fa40ce5588f7 | -22.51635 | -44.6127 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ba16ca80-85ea-34b1-9e95-965519b3a2eb | -22.17509 | -46.74067 | 2025-09-30 05:12:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 25ff6386-b152-3377-858b-21985ace48d5 | -21.31241 | -46.75333 | 2025-09-30 05:12:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa344611-08f6-3201-bb25-5516d7324bca | -23.11312 | -51.51385 | 2025-09-30 05:12:00 | NPP-375D | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b501802a-236e-3691-8e66-b3ece5050277 | -22.52437 | -44.61294 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d7cb2154-eb32-3691-bdae-2321fd660ffc | -22.1686 | -46.74006 | 2025-09-30 05:12:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 03417b98-ff00-325f-a1a1-019568cec63b | -22.51587 | -44.61982 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 88cf5738-960f-30e2-940c-8e1bb8d63a32 | -23.15685 | -45.72616 | 2025-09-30 05:12:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 20782e98-7156-3289-aa6f-14055be12c08 | -22.52356 | -44.61489 | 2025-09-30 05:12:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| baf9213c-7a61-373c-96a1-79f4558beb55 | -0.0951 | -51.27545 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26a50f53-2eac-300c-bbdd-301e23637ac6 | -1.29015 | -54.18362 | 2025-09-30 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae5b1a5f-9706-3bfe-bbad-1dbe9728adca | 3.1957 | -60.70602 | 2025-09-30 05:25:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dbca630-b460-3a2c-a010-4fed1e1e23a2 | 3.89003 | -59.97757 | 2025-09-30 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25a945c1-4282-3252-aa9f-58d33972ac3c | -0.09619 | -51.26851 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ae8ab2a-e486-3399-aeed-d67d1cabc4b4 | -0.09455 | -51.27893 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dac3872a-40f5-3ca7-ae0b-d617bec1d014 | -1.39359 | -55.17894 | 2025-09-30 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c7b660-85bc-386d-a596-bc29325f66d5 | -1.28941 | -54.18838 | 2025-09-30 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76b090df-5ff4-3d23-8587-4014d9195a62 | -0.09997 | -51.27977 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 409e083c-c9ae-33cd-aa31-64a2b908a6f0 | 4.15795 | -60.01679 | 2025-09-30 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca0e34d8-624a-3404-9d00-d2476c42bfe4 | -1.29092 | -54.17876 | 2025-09-30 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee18f192-a26d-37f2-a9e1-aebad30d7de6 | 4.15741 | -60.01334 | 2025-09-30 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8d47055-6098-35f7-87c7-b509c69eeef3 | 4.15687 | -60.00989 | 2025-09-30 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ec7acd0-0eae-3cf9-bc8f-c57c9306e31e | -0.10051 | -51.27631 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7735d4d4-a695-3a26-9ee5-8de247725d97 | -0.09565 | -51.27197 | 2025-09-30 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 378d4301-15c7-34fb-ab76-c48ae44ce958 | -3.28329 | -50.03862 | 2025-09-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a4fbea8-5414-3a29-b450-c5417f10ec49 | -4.37215 | -55.88877 | 2025-09-30 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 290a27e2-7bdc-370d-a6f6-304333213763 | -8.323 | -50.88061 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 288555c0-e280-3190-b52a-c5daad42a3b9 | -3.25077 | -49.12934 | 2025-09-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README103.md)
