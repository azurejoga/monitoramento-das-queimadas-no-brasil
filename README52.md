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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10fbba13-1918-37f5-bab9-90976c81e7d2 | -22.17931 | -43.44954 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8335ee4f-c76e-314d-836c-feb7da5e1f52 | -22.17855 | -43.43993 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cca506c9-8e21-3b70-b8c7-8827a3b296a2 | -22.17762 | -43.44394 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41df8682-54a8-3c43-baaf-6ad00d22190a | -22.17668 | -43.44802 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 28cb86ab-90f4-3925-b70d-89e156c838b3 | -22.17553 | -43.44006 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 668474fd-bef8-36cf-b364-5bcdc0cd465e | -22.17464 | -43.44406 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 459ef042-e962-3f14-9261-830c8c258b07 | -22.17195 | -43.44291 | 2024-09-26 03:21:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e6b5507-99bd-315c-ab91-79134144da9e | -19.63355 | -44.18236 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5aa17824-c8c1-36fa-aa0d-14b11c9a1d30 | -19.6347 | -44.17738 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83ca2735-a0dd-3fe0-8115-d2a437d20981 | -19.63918 | -44.15804 | 2024-09-26 03:21:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fa263c6-3f40-34de-845a-c0c03706043b | -22.73598 | -44.78845 | 2024-09-26 03:21:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ff69853c-df7d-3965-b59c-98de59724b66 | -22.74001 | -44.79111 | 2024-09-26 03:21:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| cfcb0c41-d1c8-3a0c-81ef-492e6b294cb0 | -22.74166 | -44.78408 | 2024-09-26 03:21:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d9b5d4e6-485f-3f77-aa6b-90b1aa030702 | -22.7425 | -44.78773 | 2024-09-26 03:21:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a3344024-7a9e-30ab-adea-a6ff590bc407 | -21.93535 | -41.55691 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d787d4c9-4569-3e93-8a60-11ad7c53caf1 | -21.93444 | -41.55457 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4631c21c-a4c0-36f6-99b0-9914f1b275cd | -21.93376 | -41.55769 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94a22136-19f5-34f5-97b4-42613a8255af | -21.93034 | -41.55566 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e92291d-feab-3ff7-a170-6972405bea5e | -21.20816 | -45.75938 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14666511-d354-37e8-8b34-c1993e23f4af | -21.20666 | -45.76023 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 075b43fe-d1ef-3e7f-bb8e-9c077a83a789 | -21.20645 | -45.76656 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| da973a96-9c66-3ea9-b8e8-724a203e6b91 | -21.2049 | -45.76743 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| db2afb55-68d7-3052-8122-62efdab94b24 | -21.20055 | -45.75702 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb9da499-845e-3c72-a45c-8e4be93f6081 | -21.20022 | -45.76376 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 71471d74-633e-3078-9f7d-b9d3a01e9c3f | -21.18674 | -45.75709 | 2024-09-26 03:21:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89b3f0b4-bd72-3058-b84f-c697658b2ce5 | -21.17445 | -42.07741 | 2024-09-26 03:21:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 25087e2e-fe26-368d-9303-d9614a1acc1c | -21.17371 | -42.08088 | 2024-09-26 03:21:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1cd77e0d-777b-3b27-972a-80f874085183 | -21.17306 | -42.07727 | 2024-09-26 03:21:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0c687002-ba9e-3552-94ea-92ca6c7edc7e | -21.00026 | -41.2751 | 2024-09-26 03:21:00 | NOAA-21 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b2e1f03-5313-384a-ba21-0aac7e5b765f | -20.97278 | -41.40593 | 2024-09-26 03:21:00 | NOAA-21 | MUQUI | ESPÍRITO SANTO | Brasil | 3203809 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17670a6e-d78b-3d2f-8404-da9e9d6f458e | -20.6226 | -41.21141 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f151bc72-e7fe-32a8-b7a8-3575b7109ed3 | -20.61695 | -41.21309 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6b475578-9e20-38b7-af2d-6c9a14b385cb | -20.60464 | -41.24585 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a2153a52-60f5-36bd-8b36-a68db151d048 | -20.60224 | -41.23232 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| adaf082f-d1de-36e9-9000-97d5692a2f72 | -20.60173 | -41.23471 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 277ddd3c-ff5d-37b2-a428-e3f79cb4c26d | -20.59665 | -41.23367 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d49bd7c1-98ba-358d-889d-67d7b672ee4d | -20.59609 | -41.23625 | 2024-09-26 03:21:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f570e1b6-fc51-3224-8e99-ae64f90e99ae | -20.53879 | -46.37303 | 2024-09-26 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 927fe832-a1e8-3024-9749-1f8986923689 | -20.53682 | -46.381 | 2024-09-26 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77ee9755-3720-308d-a1ea-0f750bc28eea | -20.52325 | -43.93562 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 797306fb-aaae-33b9-8132-c9f12c4a2be3 | -20.52221 | -43.94019 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 23d4534e-3ce2-37d9-883b-cb751b44f977 | -20.51943 | -43.93486 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bef23477-8662-3558-9cc1-db3fc7f5f2c8 | -20.51836 | -43.93941 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 43cea786-80b9-3297-bb11-2568d79a98eb | -20.51736 | -43.9339 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b4d784b7-62f2-3385-9841-de7afbe8c187 | -20.51632 | -43.93845 | 2024-09-26 03:21:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8113e4aa-3a1a-3c0c-ba2d-c49921a493bd | -20.50793 | -43.49207 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6ae09e8e-1b1b-3541-9e2c-23b6b1c2d072 | -20.50747 | -43.49057 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 335abcb3-356a-3a98-9107-e2ab0e964147 | -20.50707 | -43.49589 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 377a35bc-1bda-34c0-9412-523cbf108122 | -20.5066 | -43.49434 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 99dddef0-6e37-3bb4-b16c-3be1d0ad37ca | -20.50567 | -43.49835 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a3253177-c355-3c5d-9317-dd531c82f1dc | -20.50288 | -43.48732 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6bf07311-5795-3e5f-b90e-6e115e6ea72c | -20.50196 | -43.49141 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2bf37b3e-2881-3068-990c-f681c99a4ea4 | -20.42977 | -41.88189 | 2024-09-26 03:21:00 | NOAA-21 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 20426fbb-cc1d-3472-b30f-2ee552df1a8a | -20.42895 | -41.88574 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b3ef5082-9945-3d3e-9f31-8d53cb492803 | -20.42833 | -44.10176 | 2024-09-26 03:21:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8d451655-fdf5-3c42-8819-7c8a04b46ee7 | -20.42802 | -41.89013 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 966017ea-e6f6-3031-8256-19aa98f6ecbb | -20.42724 | -44.10646 | 2024-09-26 03:21:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e8b4eac5-e29b-333a-9a84-71323e05e615 | -20.427 | -41.89488 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 47182204-0fb6-3b28-a8cf-49b841a08659 | -20.42425 | -41.88182 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| e67b7b6c-bbd2-33e2-9617-c119d66104a5 | -20.42326 | -41.88643 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 0f372f08-6692-38d0-8dc6-689a40fc3717 | -20.42229 | -41.89096 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 886d4421-90e5-3eb1-9a68-1b4eabda3522 | -20.42142 | -41.89504 | 2024-09-26 03:21:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8114b340-4f87-3b5b-9972-34146ca753a0 | -20.3433 | -46.16625 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54703efa-e854-3686-adad-8799ed41c8e4 | -20.34167 | -46.17284 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b57b46d7-8b6e-3c42-9d27-cbc12a462a9a | -20.34129 | -41.88955 | 2024-09-26 03:21:00 | NOAA-21 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 350210ef-85e2-36ea-b18c-59e623aecf41 | -20.34121 | -46.16877 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f40faaba-8993-31b4-884c-fb53bcd20040 | -20.33959 | -46.1755 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49f6b58f-46e8-39ec-8f7b-7664c97ebce2 | -20.21183 | -43.43661 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 7fd5961f-2335-3347-b55f-323a4164a454 | -20.21088 | -43.44085 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 42a53c9b-6a11-3251-b8b8-faab3ea76190 | -20.20995 | -43.43901 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e7897ff9-78b4-3b44-9953-f437426d6c86 | -20.20989 | -43.44532 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 19882e13-a987-31f8-bdd4-7e833a8659be | -20.20896 | -43.44335 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 20d069b8-ab24-3670-8e91-b0734c7c1859 | -20.18776 | -43.54458 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 938381c0-0a7c-32aa-bdf1-b37159d88f70 | -20.18665 | -43.54958 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ff6c56e0-f208-32f1-85f4-9f71fa4d14cb | -20.18616 | -43.54253 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f2af9540-a8ca-3b04-846d-326302dc4905 | -20.18531 | -43.54624 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c50bfefe-6627-356d-a126-1dbffe2ef24c | -20.18277 | -43.53936 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5d4464b5-0945-3b62-9904-2bf3b44a6be4 | -20.18204 | -43.54262 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cb7de4a2-7d88-36f4-9fff-b297c4c24524 | -20.18107 | -43.53785 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0b899414-ef1c-3047-b59b-8e0e67d77ff0 | -20.18036 | -43.54092 | 2024-09-26 03:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bee2f050-0f45-3940-9654-2521687d47be | -20.16735 | -43.5531 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f3feef80-bc6d-30da-87b9-0c0522ee6ce2 | -20.16555 | -43.55156 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a5cccca6-9aea-38a5-932b-c992b425f3c3 | -20.16217 | -43.52126 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| bc484f9f-1aab-3397-ac4d-61afbdbc0162 | -20.16138 | -43.52477 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ce98408d-982a-376f-9292-4c8100a0b00e | -20.1606 | -43.52822 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5bf1fd85-1bf2-3014-a31d-e57a301730f5 | -20.15982 | -43.5317 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b50dfd2a-c26d-3cb6-99cc-00e941dada05 | -20.15976 | -43.55941 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f11e0a80-5755-3e07-9b1f-19206e5d01fa | -20.15625 | -43.52018 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4884d71c-16be-305f-bf42-1f01c371bbbd | -20.15404 | -43.52997 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5922c32a-9e75-3d44-95cb-e2b89a24c503 | -20.15287 | -46.58284 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c768c53f-b7b4-3011-818b-81d8c1fe97c8 | -20.15135 | -46.58898 | 2024-09-26 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3bd5ad1c-cd71-3af3-bcbd-cbd8b3d37c3a | -20.13441 | -43.5349 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b87d3968-d1d6-38e7-a6e9-2c40e135c3ff | -20.13379 | -43.4833 | 2024-09-26 03:21:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f0395551-7639-3408-ad0b-0da4293b9fe3 | -20.12846 | -43.53392 | 2024-09-26 03:21:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ffcfb4c0-c22f-3ce8-80a0-3f78c0cba89d | -20.12771 | -44.26558 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d192290a-9dbb-35a2-a2e5-0f0495d4bde0 | -20.1267 | -44.27003 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d82ace29-f8d2-312e-85b8-5f0f1ea1a431 | -20.12622 | -44.26907 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| adaf10f0-85ee-3717-b12f-a812df74b169 | -20.12566 | -44.27458 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0946f9ec-5c0e-3233-bd44-8c4434bfa426 | -20.12516 | -44.27357 | 2024-09-26 03:21:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b01f54bd-63a9-389a-8402-7afaef5d9ace | -20.1247 | -43.44218 | 2024-09-26 03:21:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |


[Clique aqui para ver as próximas entradas](README53.md)
