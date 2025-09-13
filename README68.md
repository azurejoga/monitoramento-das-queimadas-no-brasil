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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af34adb8-5f63-37db-a7a1-312975a25d48 | -21.62911 | -46.80026 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 97b65d1f-e7ce-3b09-bd31-ac142ba1284b | -20.59524 | -44.90649 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| da236791-8f4c-3814-a072-737f833141cd | -19.14388 | -48.78654 | 2025-09-13 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd3079e5-949f-351d-bd7b-33ea783c5fe3 | -20.2598 | -44.1885 | 2025-09-13 04:10:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 36137aa6-9540-3161-91fd-08c9aefde625 | -15.02563 | -50.14573 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebb7f624-67a1-34fa-abc9-2794b7f9fa30 | -17.41391 | -49.24796 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34d7b525-1893-36d4-84d2-ab8abecd667a | -15.12371 | -52.46121 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f20c142-a11c-3390-bae9-12aae545eaf3 | -17.4218 | -49.22743 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 009806d6-961c-316d-a676-90d58a706d0f | -16.35923 | -51.54212 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 335eabbf-4316-3ef7-baf3-cb4163e556d0 | -17.948 | -45.26725 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ad16a58-1ff2-37ca-9442-69f601ca7fd1 | -15.13627 | -52.47842 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 304be2fa-355d-3984-b9d4-bda97a3780cd | -18.97541 | -48.59709 | 2025-09-13 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4ab6e8c8-0cd4-3e0c-aed7-41cac9e441e8 | -17.12882 | -48.48042 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52102b8-238c-33ca-9684-58d784d6ed8c | -21.63185 | -46.80475 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46ceb94c-8dac-387b-9609-5281e115e1b4 | -21.02097 | -48.41985 | 2025-09-13 04:10:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c03217f1-b620-3f99-87df-0bb00812e7e5 | -19.97888 | -46.91949 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33d55f22-3ff4-3c8b-968a-4e601a027cc3 | -17.24442 | -43.87142 | 2025-09-13 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e381f895-f833-3667-86b6-654470e02580 | -21.68961 | -45.43772 | 2025-09-13 04:10:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd8f6584-f770-33ad-9f99-766856ba36b8 | -19.65184 | -45.87078 | 2025-09-13 04:10:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 065592ec-9da0-34aa-bebd-b7f898b5e940 | -15.59944 | -54.76981 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7302dfd6-0efb-3c82-b83b-948031dccad6 | -15.2388 | -51.40442 | 2025-09-13 04:10:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6fda93f8-6c8a-33e2-bd76-bf488c2a7e18 | -16.36029 | -51.53682 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95aa2a8a-49ce-3137-b114-2cda6b8d42ee | -20.09761 | -46.92402 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87ac712c-0aa7-3987-9c30-2ae9b1681e80 | -18.34052 | -52.05426 | 2025-09-13 04:10:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35a6f8e6-12e7-3f15-a544-ea1cf0dfa543 | -15.75712 | -53.50272 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b1ff572-5e0f-33b8-a527-b407f1fe5a31 | -15.50688 | -47.29811 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc710a7-af36-3236-a5f6-1c795f77ff5f | -20.0204 | -47.6485 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58f93761-4448-31f5-b538-2c719af750d2 | -19.98918 | -46.90074 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eba04df5-2ad3-3d69-88f4-4aceaf89a2f5 | -17.91282 | -44.45458 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5056c6d9-e5ae-35cd-9b53-37c79ee6c18d | -16.49783 | -55.14319 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0c086f5d-0f9a-3fdb-a149-4ac256d43362 | -22.17926 | -49.61538 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85835b54-21b1-388e-9e8e-cba4077fe5a5 | -20.60696 | -50.40881 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9379d926-a5d9-38aa-b559-1ebc2ab61f34 | -16.07294 | -50.00029 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfc28db7-112b-3901-a168-651ee6f98004 | -16.55511 | -49.22551 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aa7a3f9-dc9d-3978-b42b-379bb8d5608e | -16.87312 | -49.3415 | 2025-09-13 04:10:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14a1b75a-6393-3149-81d7-a4e2fa7ac383 | -16.49734 | -55.13229 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 81450d46-0a1d-3b2e-8ed4-3153e6bbdfc4 | -15.5454 | -47.95422 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4dbad9d-dd78-3817-b56a-d109bfcc4b79 | -21.40547 | -45.1099 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 961fb76c-c1b9-3ac8-b92a-c2abe6b5db38 | -15.14365 | -50.12075 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a46854dc-8a3a-3222-8d5b-616e51da5ab9 | -15.23983 | -51.39906 | 2025-09-13 04:10:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 12a519d0-bbdc-3568-a1c8-02ce6d43444c | -20.10241 | -46.91666 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6cd2ddb-39fa-3128-922b-e70de3eb458e | -16.6474 | -49.79173 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9e0e1fb-13b6-3fb3-a62e-84d540124cba | -15.12999 | -52.48316 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4693489-75f4-39f7-b11a-459498e7d067 | -17.41855 | -49.2452 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a586c70e-4c05-3aa4-8e4d-375836e2ec46 | -17.33537 | -46.66563 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 616f1f93-3665-3d4d-9c52-2f53a6957b5c | -20.87371 | -49.33849 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f8426452-5da1-33aa-89c1-7f9c4a8dc815 | -19.98002 | -43.39282 | 2025-09-13 04:10:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a493c2c-6b3c-306b-99fa-ec92b7f4e627 | -16.65042 | -44.93338 | 2025-09-13 04:10:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6843cb7-c6be-3ec4-99e7-c3433f2ddeb8 | -16.64409 | -49.78617 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83bb732a-15a0-3f8d-9ca2-00c12196e6cf | -22.25089 | -46.14673 | 2025-09-13 04:10:00 | NOAA-20 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d004100b-722f-3bfd-b291-90fbe6764713 | -18.34139 | -52.05665 | 2025-09-13 04:10:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3af004c1-516e-3d21-a98b-31610eb9873d | -19.07079 | -46.64096 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dff2769c-f849-3c6b-aa0f-19e593b78521 | -18.70415 | -51.78502 | 2025-09-13 04:10:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbd453cf-dacb-32b8-bc92-deba9ee6ea89 | -17.23217 | -50.22982 | 2025-09-13 04:10:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 645c83b0-587a-36ab-9e7f-e228879f2c25 | -17.27745 | -47.25136 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef4f391d-463e-33bd-ab18-953d6dee4bac | -16.11593 | -46.94759 | 2025-09-13 04:10:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74c865bd-8f6d-3040-a3a8-ca90a3f01372 | -20.59479 | -50.40611 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ceba7c61-d8d1-31ee-87b1-b8cd4437902f | -17.30534 | -48.73391 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e6cfd0b-f26a-363d-adb7-c9d0aa3ad6f3 | -16.24673 | -50.0686 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fa86833-3ec7-39cb-8499-68e09910e598 | -16.41391 | -49.03687 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21d1f941-888d-389d-b766-3f353f497950 | -20.44866 | -46.44399 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7427f1be-a93d-3f77-b3c0-d5432e1ff018 | -15.17066 | -52.49332 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3460106-d8ca-3afa-81c7-2e41149184f4 | -16.49146 | -55.13091 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3a5932a6-c080-3b62-92d1-f683b50ad8fc | -16.43184 | -49.05236 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbea5ce7-5c84-3dad-8b18-01624ae2e540 | -15.0989 | -52.50491 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de01e4ac-cc2e-3cfe-8462-fff4ccd2fef6 | -15.71386 | -50.58145 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7e3ab3b0-fdf3-3ef7-a3ae-1f278a018f36 | -16.25105 | -50.06934 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6177702-f28d-35c9-a90a-465f97c878d2 | -15.55696 | -54.80616 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9db69d1-a517-39f1-bc3c-6c7ea607e677 | -15.11859 | -52.46014 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e4a053e-8087-31e9-84c9-a2917aa5b0b5 | -15.15163 | -50.1268 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30b3871e-46ed-387b-833d-f14f05c5b7b9 | -17.71389 | -40.26163 | 2025-09-13 04:10:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0fcbe9f5-2a48-30e6-a8ee-484c642b5d0b | -20.64784 | -48.69587 | 2025-09-13 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b86eb6a7-a9ed-35e4-858d-d841170f17e5 | -18.61241 | -48.20706 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 96a53c43-7204-3641-b817-0f67cf213aa9 | -21.58501 | -48.41887 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 92db1d56-3e89-3730-8f0d-574b48eb5df5 | -21.5822 | -48.4137 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1d95a19-ef48-322d-82e6-21657a2e16b8 | -17.43042 | -49.22549 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80f9fceb-717c-3e9e-9fa2-b6501b46cb6d | -15.1386 | -52.4935 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31294c93-46ad-34a8-9213-97f5ab96ca7a | -17.90938 | -47.02401 | 2025-09-13 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 642ab945-2f21-3000-9a53-0e68bdae7e78 | -17.43035 | -41.17053 | 2025-09-13 04:10:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf56c495-601a-3257-a89a-341b58a2f085 | -16.06862 | -49.99963 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 380f1893-4f23-3956-ab21-007e7c679131 | -17.13976 | -53.89654 | 2025-09-13 04:10:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92077190-2c9d-3ead-9d2e-5af20b707d5d | -18.44154 | -45.93185 | 2025-09-13 04:10:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f22bcec3-1214-3027-97c8-8478a0bca4ab | -17.35931 | -42.70048 | 2025-09-13 04:10:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 915ba9c2-6449-367e-8e0d-5d84592cf1e2 | -15.60486 | -47.92958 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78d91e61-3a29-398d-b990-a62ff66747e7 | -18.88835 | -47.05268 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e7bafc86-c80b-39ea-a0f5-7dabe5243bac | -16.07214 | -50.00461 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b67d7d8-2e8b-3336-bb0d-66e23f8a2272 | -17.90586 | -47.02333 | 2025-09-13 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ee3fecc-22b0-3b53-a03c-1045d6c26723 | -21.93047 | -47.56719 | 2025-09-13 04:10:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70ed23fe-537e-3b1d-a14d-508a31a31214 | -21.31377 | -47.39346 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4399691-8052-3d0d-b284-ec6c18ffe16f | -16.49559 | -55.14032 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 54893068-d59f-3fdb-bc14-6e3b22fe5b17 | -21.62507 | -46.80347 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14caf7b7-48c8-32ed-ad3d-d167fdd8c64c | -15.07816 | -52.49401 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a5c2ca4-3dc9-3cee-aabd-9bc69be32da1 | -20.41788 | -50.74284 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 19a836a1-cd93-3e8c-b453-116bbf2bbdf5 | -16.16711 | -48.87189 | 2025-09-13 04:10:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00080e1a-294a-3949-b2f0-cc6edfea78de | -19.06865 | -48.72594 | 2025-09-13 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dcaa353-6c17-35cd-8ebe-90379fb5afd6 | -17.43789 | -49.25276 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68287e3b-062f-3c81-8cc8-fecd9b88bf72 | -20.09214 | -46.93529 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a0a1490-2511-3042-859c-f2912280190d | -15.1009 | -50.17747 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29cb6c6d-3a8d-35c2-b930-f61920bee0c9 | -17.83467 | -50.40684 | 2025-09-13 04:10:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069b6853-862c-3a98-bc1e-f22dfb6448bb | -20.26312 | -44.18907 | 2025-09-13 04:10:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README69.md)
