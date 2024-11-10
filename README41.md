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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd1a2875-df05-3383-849a-f9f00643c485 | -4.21194 | -48.12402 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce382ce3-143d-3684-9391-195617eb5a3b | -3.82105 | -44.84736 | 2024-11-10 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b32855a0-ba33-34ef-b01a-27554599c274 | -3.75179 | -46.13945 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf80cf2-245f-3cac-a184-f43f12cdaf41 | -2.02483 | -46.35196 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f4957c-320f-3a0a-a238-a5ad42d813d0 | -2.56796 | -47.34171 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac84a3c9-377d-3ad4-b335-b95bd578ca79 | -5.71929 | -42.67026 | 2024-11-10 04:14:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 06f86bf2-e4f3-3412-842f-60f318356b83 | -6.207 | -41.66776 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| eeac260d-cb8d-30fb-bd6a-7f03938b3046 | -2.64303 | -46.80247 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83eddc39-fe1f-3647-a940-b0cd646cf676 | -3.54659 | -43.55653 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dcc80a3-cabb-33ca-97a5-7bf494a5cc52 | -3.96049 | -48.12613 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e6a12bee-bbd8-3560-8a59-a8122df2e815 | -1.53946 | -52.21381 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 436ffd90-9623-3113-852e-184838e261b7 | -3.63821 | -50.1896 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 819edba4-956f-3679-b62b-dd5a193b05c8 | -1.32441 | -54.63951 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54feda5f-d001-348f-85f4-ca9f5212f83d | -2.69601 | -51.70112 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c48010d-9692-3224-a24b-a3eccb7d2fd1 | -2.63227 | -46.77107 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7e53fcb8-5226-3862-ad21-ae838b292f22 | -1.30614 | -54.66823 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f644c10f-5fe9-3598-a07d-5a11722809c1 | -3.97557 | -48.18977 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8ac4fa9-cb66-3378-96cc-aa6b9a2adc34 | -4.21225 | -48.68164 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d815c46-1d5a-39e7-984b-225e3b216ef3 | -5.55727 | -46.34344 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5942b883-499e-303b-9da5-2e6dec90ca51 | -3.23277 | -50.26589 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb9b1fb4-53b4-3e34-9c43-9c44cf892488 | -2.08791 | -48.8251 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7a034b1-26e2-3d8d-bfb9-3ddeb513140e | -3.70155 | -47.64294 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3318615-a40d-3bcf-b584-8e378554b5d0 | -1.55444 | -46.25872 | 2024-11-10 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04bb860-fb0c-3cde-9553-29ea266db552 | -3.5146 | -44.03699 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd56b5c-4268-31eb-bb32-3fb3db5d4009 | -3.69564 | -45.81071 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c886de45-af38-3209-8b42-c6cf717ee113 | -5.20883 | -48.26067 | 2024-11-10 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 155a58f7-13cd-3ec6-a0d3-3e99100785b8 | -1.17564 | -52.09393 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 49dd4273-2db3-3adc-82fa-cd2294ca351d | -2.45369 | -53.68938 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a465b0cd-7fec-3446-9b74-9ed3cc936845 | -3.34839 | -42.36606 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83cc0490-2a24-3290-978c-10d09c0f7d7c | -3.03435 | -50.31178 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4ac85ba1-1fb0-373a-a94d-a83585796c78 | -3.90028 | -50.30123 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b294d196-22ff-3ffd-acab-c6d28adbebf6 | -5.72446 | -42.72417 | 2024-11-10 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc08856b-5e70-36ab-8229-8412f8055b02 | -3.23987 | -50.28345 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bd7c342-a880-3a87-a4b5-7e92977a2d25 | -2.94229 | -49.49946 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9643758d-23f7-31f3-af79-4a26f585d615 | -5.80077 | -44.04089 | 2024-11-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ad7d546-f776-31c7-983c-e5a41af3b8ed | -4.05859 | -49.20504 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 529e71cc-e8cf-3773-8e1f-ac616b650a4e | -3.2376 | -50.26672 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9ea0f8c3-320c-3244-a4d3-53e85e270b31 | -3.74919 | -49.89621 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ebb0e6a-437c-3668-9021-e5ccdfe63bdb | -2.39598 | -46.50726 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a8cad8e-c898-310c-8a08-8b3ec2d7c966 | -2.15135 | -48.34342 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f82c90b7-6cba-3444-94ec-c471c671b1a4 | -2.20575 | -48.37619 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0020b9d1-a456-3b1b-9a1a-03988c56c7d3 | -3.22448 | -50.28637 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 07fca535-b67b-3fda-b136-780523ce27c1 | -2.23633 | -53.78075 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c6a8b28-0edf-3469-82c6-d16b2e2696b3 | -0.29571 | -51.73042 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b20f14f0-4b97-399f-b424-4994c27fe7d8 | -5.40281 | -46.60049 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f1e1891-9512-3664-896b-daeef5ceb9f8 | -2.65318 | -49.39655 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| efc9ef7f-5362-3b95-b30a-3968af4ce91f | -1.64699 | -52.05053 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 994917df-7b20-39b9-8128-c606584c4f31 | -2.92361 | -51.67637 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccebfa2a-e27a-3a98-95c9-a31007a725f5 | -3.03338 | -51.52724 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db91cfe-d699-30ed-a287-92c59d2eb3b9 | -5.29795 | -46.22705 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23b31fe5-8ce1-397b-b410-4cf9f9b7b00a | -3.86272 | -52.37767 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be98ea68-0156-3efd-85cc-eec254638cac | -6.23406 | -44.14149 | 2024-11-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e818ab4-d4aa-37df-b5f9-365f6eeca80e | -0.85077 | -47.65057 | 2024-11-10 04:14:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32f1390e-452a-3dac-9698-27414e37a844 | -1.21822 | -51.75923 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a78b1ed-2c47-33e4-a187-207a2da7251f | -0.04044 | -50.78307 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 249032c3-0652-3eda-beab-76d1c216dafd | -3.91402 | -47.95265 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef6cd7ae-47f5-35a3-b5de-c8d7a0628f9f | -3.12404 | -50.1489 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d0441460-e1d4-302b-9456-197e0cafac77 | -3.23663 | -46.54196 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2cbe4fe-feb2-3f7e-a386-061ad131eecd | -3.10142 | -45.96136 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 574872fd-26b4-3ef7-b9e0-c2f6fb9e9024 | -5.12629 | -49.3308 | 2024-11-10 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3d9f9d9d-921a-397f-ae67-a830f9143d8a | -2.4199 | -53.66489 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15755ee5-6ac3-34d0-9029-f076ddf5d321 | -4.30565 | -48.61381 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b34f0df-7e30-3d75-8b44-5cab51d1c81d | -5.32249 | -45.05653 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 28228309-3b20-3519-9f9d-2cad1bf22899 | -2.11441 | -50.57137 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 650dcf53-5e29-3af9-866a-5bac8b7f4b17 | -2.4095 | -46.30104 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b31fa96d-047f-38e2-a2bd-b510fee06eb2 | -3.24034 | -50.4519 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 514712e3-9446-39fc-824b-7d11108f211f | -1.3991 | -52.36827 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 426edbc6-21a2-35b8-9206-6cdb91e162c5 | -4.71032 | -43.79303 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f367cfbb-2b7a-38a7-b0c8-10fdab347376 | -3.24666 | -48.7534 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc842b72-5c9a-3b39-829d-8a5fab8b4de0 | -4.23259 | -48.02261 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce1e9a4d-702a-38dd-ae7d-98978cc6c77f | -4.93753 | -48.51837 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80729c4b-7530-3b9a-b7fb-607d7d1d3900 | -4.84636 | -48.60183 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83481101-89c4-33ff-b8ef-1f7ec7e7ca9f | -3.12317 | -50.1542 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c556933-c606-3038-a2f5-1264674ee52c | -2.68335 | -51.94268 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24194cc5-25f9-39cc-941d-ccd2dd2a5fbd | -1.27968 | -53.7156 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 09744c8e-95aa-32ff-a77e-8b846a61eaa4 | -4.24278 | -45.38131 | 2024-11-10 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 004a99e9-bd2c-31ad-96b7-9e44c7ab39a4 | -1.51591 | -52.16299 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5adad31d-c49a-34cd-a0fe-a264580160ec | -3.2724 | -46.32037 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07bf1d41-0a0a-3630-9aac-9f224bd1eeaa | -4.85317 | -48.48421 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3057c13-f6c4-305e-97ba-945f1c5c989e | -6.2055 | -42.05153 | 2024-11-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 285efed8-f975-3932-9dbf-26c737e06b37 | -3.05722 | -48.0414 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19dde163-9be7-35cf-974f-309c92297c6b | -2.68093 | -46.78859 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06b20bdb-4337-3601-b3ae-883c119b0579 | -6.22766 | -42.92294 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17d8e1fe-d77a-3619-a2d7-5cd2e9b4d67e | -4.51838 | -45.70293 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d9c2df0-4a5e-34e2-ae64-dffac6a86c1d | -6.44859 | -42.74872 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce871bb7-e59f-30cb-8374-36305dcae45a | -2.71698 | -51.70791 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c8d70d-cb27-3c08-82c4-5e1c72ddb109 | -4.92377 | -48.52385 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71ac0818-0edd-32bd-bdae-7b5384272f9d | -3.03521 | -50.30634 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c05ca3a0-cdce-3709-bffb-ed1e1d0e7721 | -2.18084 | -48.3387 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5aef361-6c9e-3157-9570-60fff2a769d8 | -4.60519 | -45.96987 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a286fc80-c1dd-3201-bf12-cecc42360725 | -2.04164 | -51.16574 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73669833-c469-38f5-824c-128ef96edbf5 | -1.25083 | -51.76804 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32565e6f-ba2c-3840-ad8a-c5d30656ff99 | -3.24051 | -50.30197 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd7a9f8b-bc1f-3875-867a-16fca977c859 | -4.84169 | -48.62972 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22123849-21ac-3756-84f9-cc3f5d49ea98 | -3.3072 | -50.0811 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fa1f774-d942-3c7e-8ca6-ac25b2d0dee4 | -2.87522 | -51.47149 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7d28b35c-e2a6-3acc-a058-0ff302eca234 | -3.72855 | -54.74507 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5278a671-058c-3894-ae39-77673f1c2948 | -1.34704 | -54.62552 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 051e0074-f07c-3df2-ab24-9b252c281fe5 | -3.96912 | -48.17716 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35317cec-3267-3a70-9dc0-b1fd9e36ee21 | -5.89441 | -42.83534 | 2024-11-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README42.md)
