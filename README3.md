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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42bff5c7-4e8d-343c-8a3d-c8a53aefa4af | -15.05374 | -42.43144 | 2025-02-22 03:51:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01489f6d-a414-3cd9-b8df-a1b9373f6ef7 | -15.05452 | -42.42702 | 2025-02-22 03:51:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 642de335-fc13-3bc9-8feb-c56731ed2097 | -20.13029 | -45.44552 | 2025-02-22 03:51:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d925e912-d5b1-3eb0-9e18-2171f5b3bf1c | -20.76662 | -45.84051 | 2025-02-22 03:51:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9ccb376-8b48-31fa-8754-78898e912ba0 | -20.77071 | -45.84137 | 2025-02-22 03:51:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 333982d1-49cd-3428-83f5-22bf4015b815 | -20.1131 | -40.64761 | 2025-02-22 03:51:00 | NPP-375D | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4ab22fff-cc6d-37dc-86c1-95bd38216618 | -20.88598 | -46.17182 | 2025-02-22 03:51:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 703717f9-67a8-3585-8dc1-be4026ba8546 | -20.76588 | -45.84438 | 2025-02-22 03:51:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b8a1cb1-a8ab-30a2-8e55-ead79014e396 | -20.55592 | -42.36556 | 2025-02-22 03:51:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d59618cf-a6cd-3d64-9e17-a858c4768dc3 | -17.77908 | -39.57131 | 2025-02-22 03:51:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f46b73ef-5074-379a-8c32-a1c0a593d5ac | -20.29423 | -40.88893 | 2025-02-22 03:51:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7df462e6-e193-3132-b00e-d7970be3e788 | -15.05005 | -42.43084 | 2025-02-22 03:51:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 99d2e3ef-f898-3c3d-8392-d7580a290ba4 | -18.04018 | -39.92641 | 2025-02-22 03:51:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a91fb5fc-e4e8-3e26-9719-8d0cf6a08561 | -14.43176 | -45.62836 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cc1bd4e-d5d7-3486-a913-a052f5d076e0 | -20.12629 | -45.44454 | 2025-02-22 03:51:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f8bf972-b906-3c68-9215-bfab7c32f335 | -20.12672 | -45.44581 | 2025-02-22 03:51:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f67a8ad7-e4ec-3721-a803-04d0bf4e4649 | -14.44087 | -45.63311 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d82fe480-8e18-366f-857c-444cd9fa5dde | -14.43628 | -45.62926 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86af7c4f-a9e5-3573-8171-bf97c5a18fe5 | -16.34787 | -43.69614 | 2025-02-22 03:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58b1a8f7-a80c-3f3a-a20e-15c0cf78f2ab | -15.5573 | -46.27703 | 2025-02-22 03:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d4eff1-4a8a-3fd7-b9bd-56cf3891d0cf | -14.43263 | -45.62369 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a485ae1-a56b-3f7f-a106-d8ee83f4467e | -17.05457 | -45.04508 | 2025-02-22 03:51:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca22718e-3d87-3b76-956c-ae09b8f93596 | -14.44079 | -45.63015 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c85fa0-2cb1-308d-a564-7c0d244745bc | -20.99641 | -44.16099 | 2025-02-22 03:51:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9db112ef-57df-314c-8ee6-0b6733d86805 | -14.43993 | -45.63483 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d185f5af-5c91-328c-be4d-45b2da901bd8 | -20.13073 | -45.4468 | 2025-02-22 03:51:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91bd201c-61dc-3270-b9be-b8a2856bddd9 | -14.13391 | -41.69302 | 2025-02-22 03:51:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa01428b-ac90-3664-b700-f5177347e3e5 | -14.44444 | -45.63573 | 2025-02-22 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22b7e9a9-cab6-3b30-9299-69cb54106737 | -17.05531 | -45.04119 | 2025-02-22 03:51:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18fad9b3-c532-3060-8abb-37e4814da728 | -20.61919 | -42.48572 | 2025-02-22 03:51:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 20c954a2-d9cd-354c-99c6-1222ca9f22e0 | -15.76455 | -43.23057 | 2025-02-22 03:51:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 809050d1-2b1d-38f4-9ae1-d50107eb09fb | -17.0078 | -49.78297 | 2025-02-22 03:51:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c2992a9-8ad3-3163-9b35-407f4c6b74c2 | -19.71704 | -40.35143 | 2025-02-22 03:51:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c925761-a033-3cb4-8885-57b31abff53d | -21.18203 | -44.27299 | 2025-02-22 03:51:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3da13c97-68f0-3144-aecf-780324ec668a | -22.86394 | -42.96741 | 2025-02-22 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1a36c779-6695-3241-9ee5-d3c7bcf767d0 | -22.62287 | -43.20681 | 2025-02-22 03:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 461a4cc4-6bf8-3a02-af04-37e7ed837417 | -23.33703 | -46.77318 | 2025-02-22 03:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c1456cd5-8fc2-3b7a-af2a-d42e30425fe7 | -22.68493 | -47.43813 | 2025-02-22 03:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90769baa-08f0-3433-8fbe-5578fa0c66ad | -22.75467 | -43.51001 | 2025-02-22 03:53:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bb38730a-418f-3b47-934d-1dd981af2080 | -22.85904 | -42.02619 | 2025-02-22 03:53:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eb378214-dfff-3eff-9aae-f39fb8a99265 | -22.90005 | -43.75401 | 2025-02-22 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fdf0f95f-8bec-3b0f-a0e6-fd65fb96b47d | -21.20156 | -48.62481 | 2025-02-22 03:53:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 238a4d76-373a-36bb-99ba-0634e7f01d9f | -21.91343 | -42.26233 | 2025-02-22 03:53:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b06c3f36-bbf7-312d-b73c-e68b71cea0fc | -29.89084 | -51.23432 | 2025-02-22 03:55:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 42b6d2e5-939a-3e68-862d-83de2f5a37ad | -7.89348 | -43.55087 | 2025-02-22 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e3b803-607e-376b-bf9b-00762c1cddef | -10.15888 | -36.46969 | 2025-02-22 04:12:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3daf8ba4-c391-325e-adb9-91dcc5568925 | -6.86779 | -44.79057 | 2025-02-22 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5392ace-069a-3880-809e-b4df4de03630 | -5.56886 | -39.25322 | 2025-02-22 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 758a982c-49e7-3f93-9af0-8be848c9ea73 | -10.56884 | -37.97498 | 2025-02-22 04:12:00 | NOAA-20 | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 41225ce7-8d33-346d-9546-0cf064ea3327 | -7.89402 | -43.54741 | 2025-02-22 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a260b3f1-964a-304d-8687-1aa6382d22d4 | -6.87117 | -44.79111 | 2025-02-22 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a85a553b-7c4c-31c2-8058-a74ed5dde245 | -8.72717 | -44.0153 | 2025-02-22 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb05c99-19b6-3b4a-95c6-bf89ce74b219 | -10.46728 | -38.45927 | 2025-02-22 04:12:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3469506f-ccda-3ed4-a2d3-03baf10ea703 | -7.89126 | -43.54342 | 2025-02-22 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da1f9403-196f-35e2-9642-3e6838bc15bd | -10.15922 | -36.47142 | 2025-02-22 04:12:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 78b70a40-595f-33c0-8a71-1cb1896a8643 | -10.15816 | -36.47488 | 2025-02-22 04:12:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3dca5169-c0ec-3b33-b7a5-80459a48d7bc | -5.56755 | -39.25147 | 2025-02-22 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fde1b359-da6a-3e87-8b24-3b0567f2be03 | -14.43112 | -45.62706 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d61614a4-bc44-3f45-9e07-d593616bf953 | -17.05407 | -45.04036 | 2025-02-22 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f4d2d12-d6c3-39d1-98d3-6a3a0899ea40 | -14.43775 | -45.62817 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dace09e6-79a9-3e37-991e-bee2131a6a30 | -14.83616 | -45.19437 | 2025-02-22 04:14:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60c7beec-8f26-38b1-bab2-e34ce16a638e | -15.5565 | -46.27629 | 2025-02-22 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079686dd-32b7-3dbb-a1d9-71a8d7cda90c | -14.44324 | -45.63644 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b5dccde-a9b6-311a-9286-c51750c0e2f3 | -15.28817 | -53.20536 | 2025-02-22 04:14:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da91a760-67d2-3065-981c-9f5e1c0fb671 | -14.83673 | -45.19082 | 2025-02-22 04:14:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 403d2f6d-d3d2-3dd7-81af-ea4791679f82 | -14.435 | -45.62405 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dae8dc0-241f-3982-a06e-385d861bc38e | -12.833 | -44.99377 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb6a5ccc-4ab5-302a-a6ec-868e934cf6ce | -12.82695 | -44.98915 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6d335a4-839e-3ac9-9331-16865fa3389c | -10.43332 | -44.89143 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4201bed-cce1-3ec1-80ad-90c8d79b4309 | -12.8169 | -44.98821 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f735913-6ed5-3870-8180-f6534cec49c8 | -12.81746 | -44.98468 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaa52355-6c48-313d-95c0-ce70c3a734d8 | -16.13723 | -46.2184 | 2025-02-22 04:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5881e50-4a2e-3721-834f-aa84e6bfc5a9 | -15.28704 | -53.21103 | 2025-02-22 04:14:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41b12ab4-898b-3bb2-8724-a18219fd72a8 | -17.29646 | -41.19347 | 2025-02-22 04:14:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ccd65a7-4b96-3f18-93a0-019dd514fec6 | -12.82351 | -44.98931 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5102561e-d4f1-329a-9f76-66733508f22f | -11.57725 | -47.63311 | 2025-02-22 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64534832-e26e-3e01-9171-ff9dc2c1cb93 | -12.56465 | -44.73695 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 122f51ad-1a45-31a8-b098-529a04bca5ee | -14.44049 | -45.63231 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d25b91af-d0b2-3822-8d85-3f4ebe73bc0b | -12.82638 | -44.99268 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9fdbcb7-c600-34a4-99c1-0d5b349986ca | -10.35723 | -44.91888 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d634db49-228a-305c-9441-75303a49b2e5 | -15.0765 | -48.94485 | 2025-02-22 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cd55619-1c01-3d76-8f72-fbc014d095b8 | -14.46564 | -45.81283 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3784a0cb-a220-3dce-a742-e25556606295 | -17.45406 | -46.23122 | 2025-02-22 04:14:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8867053b-247e-306a-b3c8-86f8471ee446 | -10.58246 | -44.61547 | 2025-02-22 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 611fcc7a-3cb3-38ae-a03c-66720d9caec3 | -12.82076 | -44.98523 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b331abbf-e577-35f3-b772-5eac36ee8594 | -12.81965 | -44.99229 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beaf4383-45ca-387d-85ac-aef31f431098 | -12.82021 | -44.98876 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421e0469-f66d-39b6-ada3-7765db18618c | -10.58578 | -44.61601 | 2025-02-22 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c7950d-8d1a-3889-84a7-d4b86e351017 | -10.43275 | -44.89497 | 2025-02-22 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd81585-1c2b-32a3-bfbc-eda4a5172e4e | -15.56714 | -47.85722 | 2025-02-22 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc2e9773-1497-396e-adcb-d5811abf5077 | -12.15288 | -54.99304 | 2025-02-22 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 646a61f8-0e71-34a4-8a68-f55d33ff124f | -14.43169 | -45.62349 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bc276a5-6889-31fd-b02e-7b327eab7391 | -12.82407 | -44.98577 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41f31ffb-1611-342e-9235-2ce18aa98254 | -17.05677 | -45.04393 | 2025-02-22 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90cef433-c07b-31a2-9f70-632609c6edbd | -16.68121 | -43.88558 | 2025-02-22 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b143e00-da8e-3358-b99a-84dae0bea212 | -14.44381 | -45.63287 | 2025-02-22 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd455f61-40a5-3670-be2f-bb450ff8e479 | -12.81802 | -44.98116 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e718a118-79c4-3228-8209-295ba6284580 | -11.56927 | -47.61415 | 2025-02-22 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0398f46c-5e7d-3a99-a9f2-1d783ee270a7 | -12.56134 | -44.73641 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c81ea9aa-78ec-3f52-acd9-4fc95255110d | -12.83026 | -44.9897 | 2025-02-22 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
