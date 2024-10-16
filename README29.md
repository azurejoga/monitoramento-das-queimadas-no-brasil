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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4379a758-98b3-3395-ad82-40a0bf9ff596 | -14.55619 | -43.13293 | 2024-10-16 03:47:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e26702b9-9e06-30ea-a136-d1c734164183 | -14.55536 | -43.13279 | 2024-10-16 03:47:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cef93fcc-cc9e-353a-a783-611190330561 | -14.55194 | -43.13212 | 2024-10-16 03:47:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 159f515b-2cf8-3078-a2fb-45288dace0e9 | -16.06079 | -43.79603 | 2024-10-16 03:47:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45d226f4-92b3-3a5e-80ed-481517c7e847 | -15.71225 | -43.64641 | 2024-10-16 03:47:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d122c9-d03f-3f05-87a8-0d5b1b6d5ba0 | -15.58834 | -42.8474 | 2024-10-16 03:47:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c22a934-bb21-3f33-8191-7d2d58d9d9e8 | -15.56139 | -43.54824 | 2024-10-16 03:47:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c2e79b1-f18d-325a-aecd-02ef841381d9 | -18.76608 | -43.82196 | 2024-10-16 03:47:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c51f82b3-0ad2-355b-abf1-e8df72c6f592 | -20.49466 | -44.03675 | 2024-10-16 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4aa96e00-9813-3f99-94cb-384338fd7143 | -19.8814 | -43.81081 | 2024-10-16 03:47:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e8a3e9da-157d-3a42-82f7-ef974d00c463 | -19.88071 | -43.81449 | 2024-10-16 03:47:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cd5032bf-f565-3bb4-8c02-2a9f80da9c97 | -21.45168 | -44.93731 | 2024-10-16 03:47:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ea44e987-d1b2-3676-a6de-e54c30988113 | -21.44835 | -44.93195 | 2024-10-16 03:47:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0eda9afe-b0a5-3edb-bb7e-c2b0c839f818 | -21.31773 | -44.56957 | 2024-10-16 03:47:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c98a018-f945-38ab-bca2-5a9b6d71ae7f | -16.58288 | -44.51331 | 2024-10-16 03:47:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c5a662c-d28d-3a78-89d7-c215f0e7c068 | -16.58082 | -44.51374 | 2024-10-16 03:47:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24103b94-805d-3a61-bbb7-f1956add84b0 | -13.94233 | -45.82492 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55eaa65c-6804-300f-829a-8a4c1a68a256 | -13.93907 | -45.82538 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4837c7c5-7fab-3f4f-9dcf-f6f61d1107be | -13.93845 | -45.82849 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06f8c5eb-6105-32ef-85ff-955b54603c34 | -13.93721 | -45.82388 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe726f3e-bc92-3df7-b1f6-7a81430f732a | -13.93661 | -45.827 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15ee93e7-447f-39e2-ab59-5195782cd2bc | -13.93601 | -45.83012 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b473996-4b66-3278-9da2-1cbb1f6622f4 | -13.93457 | -45.82122 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6e4888d-d5be-3f35-b805-47b40347303a | -13.93395 | -45.82433 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 979d4204-2531-343b-b68c-eebf79192055 | -13.93333 | -45.82745 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d812152a-e0e2-31d6-b9aa-45f7ff18e460 | -13.93271 | -45.83058 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dace3c40-7c2b-3260-81b4-f36347b281b2 | -13.93209 | -45.82282 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a11be31-f049-3c01-adb5-8b114652086a | -13.93208 | -45.83371 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65b60c40-248b-3d79-be1e-a8dbaf23e427 | -13.93149 | -45.82595 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37428335-b943-345a-b780-a6415319ecce | -13.93028 | -45.83223 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cb58e9c-5acc-3052-a59b-f1c6f5cc83c5 | -13.92967 | -45.83538 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49ab7bbf-e9d2-3235-adf0-c12d5d9d93e1 | -13.92696 | -45.82178 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9200740b-bc8a-3cdf-b0ba-49a17a57e957 | -13.92636 | -45.82492 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65c73aaf-ee05-36a2-b621-1fb3bc1a6037 | -13.92575 | -45.82806 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fb8f231-be4d-309d-99b6-f9305b847a86 | -13.92515 | -45.83122 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3a63a3f-8788-3472-add2-933ace41224c | -13.92454 | -45.83437 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d7daa0-e2c0-3956-9c85-b9cda1a60ad5 | -13.92062 | -45.82706 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e677958-cf08-3f61-9dae-d6afc3cb37fd | -13.92001 | -45.8302 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87e4b122-227c-3bc4-863e-0ba1788640eb | -13.83859 | -45.57911 | 2024-10-16 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e82874-a6cc-3005-8f3c-75d525cfc2b0 | -23.27121 | -50.87096 | 2024-10-16 03:47:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9679e52a-5cf6-3846-8d33-5c3a105394a4 | -22.94781 | -42.78037 | 2024-10-16 03:49:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8a23d1ff-d879-3b5e-a0bd-ed57462e37e3 | -22.90033 | -43.7528 | 2024-10-16 03:49:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1f4e1adc-7044-391d-bdf4-76a4b065e1f6 | -22.46409 | -44.04731 | 2024-10-16 03:49:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2664a5cf-2f18-3756-bbb2-c93b5ae3fa72 | -22.46311 | -44.04885 | 2024-10-16 03:49:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 42d32856-4965-3e92-b19c-2b77e036302a | -22.73112 | -45.51321 | 2024-10-16 03:49:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 99d80b07-9625-3839-9ee8-ab91c536932b | -22.72965 | -45.5126 | 2024-10-16 03:49:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 870c73e2-02b6-3fa8-a02a-10fd22f5308d | -23.57211 | -46.92076 | 2024-10-16 03:49:00 | NOAA-21 | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 26519e10-6269-3487-b79e-620739d359fb | -23.40574 | -46.55499 | 2024-10-16 03:49:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6781524-1ae3-3e97-b060-08db3bd79379 | -23.40379 | -46.55686 | 2024-10-16 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa80815c-3451-33b3-a9fb-4fbc61c37b28 | -22.70143 | -46.47914 | 2024-10-16 03:49:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ebddb5e2-f1cb-3438-82de-fc8513c5118d | -22.12391 | -48.27476 | 2024-10-16 03:49:00 | NOAA-21 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa0ad35d-e33b-3425-9958-a0c71714be9e | -22.12025 | -48.26689 | 2024-10-16 03:49:00 | NOAA-21 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79b5c733-ecff-3230-81fc-b4df88a92080 | -22.11963 | -48.26977 | 2024-10-16 03:49:00 | NOAA-21 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00220a18-b3c7-338d-8fc0-2faea58ee672 | -22.82712 | -47.4266 | 2024-10-16 03:49:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 968187fb-6776-3040-8ac6-b7219ae882b1 | -29.91969 | -51.11119 | 2024-10-16 03:49:00 | NOAA-21 | CACHOEIRINHA | RIO GRANDE DO SUL | Brasil | 4303103 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 8250ea23-2f80-3cab-b1d3-baaa07877ac2 | -20.85396 | -49.87094 | 2024-10-16 03:49:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1c8f0cdb-07ef-3492-b4d0-993e1ebdabe3 | -20.85294 | -49.8754 | 2024-10-16 03:49:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| ed36e87f-7eee-3312-acd0-e57f949c9256 | -21.15116 | -53.633 | 2024-10-16 03:49:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d193b583-282f-3710-8ebd-bce49f672ab1 | -21.14742 | -53.63221 | 2024-10-16 03:49:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 784f1dc9-f42d-3f50-b790-479820be0ed1 | -21.14409 | -53.63132 | 2024-10-16 03:49:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d61c6848-9fe0-3f70-98b7-562f205424ad | -3.0687 | -50.3746 | 2024-10-16 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d7bd9b6c-7a24-358e-a036-f0faa29927cc | -3.0872 | -50.374 | 2024-10-16 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7c3af29c-cb7e-3bc7-8925-c39d8ec23023 | -3.1098 | -54.2464 | 2024-10-16 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 44223f32-0d90-3cd6-9326-f7f1d3b184a8 | -3.1099 | -54.2263 | 2024-10-16 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| be62e8eb-56b5-32c2-9b61-9aadc5ca6a36 | -3.1282 | -54.2459 | 2024-10-16 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| b1cfb438-330d-3dbd-a759-d0a7b4316a46 | -3.1283 | -54.2259 | 2024-10-16 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 93d030de-649e-3c0c-a989-e44113910b1f | -3.958 | -46.4442 | 2024-10-16 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 9fa730ea-eefc-30eb-874f-57d15bf883a6 | -3.9581 | -46.422 | 2024-10-16 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1a3da1a3-5619-3931-ba0b-7808af031086 | -11.6917 | -65.2243 | 2024-10-16 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9ee90c2e-fc46-3f89-b296-bf4119abfec3 | -11.7103 | -65.2424 | 2024-10-16 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e15a33a1-cdec-32b1-9964-563953e8f17b | -11.7104 | -65.2235 | 2024-10-16 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0642f8b3-bd46-3ef2-8745-009da3bf1578 | -17.1664 | -56.8439 | 2024-10-16 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 6ce8db3d-9744-3606-a7b8-a458eaa26f94 | -17.2081 | -56.6946 | 2024-10-16 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 9b0b6a60-6ede-37c3-a64c-fb9d409d9d12 | -17.2177 | -57.3102 | 2024-10-16 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 45d3dc1d-9380-3610-9fb8-c4e39b997cde | -19.5808 | -57.0071 | 2024-10-16 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 716469c1-d62d-3b1a-9b32-a567a0296e53 | -19.5812 | -56.9862 | 2024-10-16 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 195.7 |
| 7eb3c503-6c48-346c-b7da-d932e73c948c | -19.5816 | -56.9653 | 2024-10-16 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 44dbf2c4-65fb-3120-b7f5-561a70ee57d0 | -19.6013 | -56.9834 | 2024-10-16 03:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.1 |
| bfc582e7-4b2d-3e8e-9c51-b3f78463ae04 | -17.0 | -57.48 | 2024-10-16 04:03:48 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fae58bdd-a341-3de5-a4ae-31c0549526ae | 1.01218 | -52.21774 | 2024-10-16 04:04:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f1627803-87bc-3f8b-a827-8876ee9337d9 | 1.00839 | -52.21821 | 2024-10-16 04:04:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1ef95263-4eb1-34ff-a665-6a38e000f504 | 1.0075 | -52.21255 | 2024-10-16 04:04:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8d423264-739a-3644-bc59-e37a20f058d6 | -1.4901 | -47.3288 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ed013e-974e-3662-b45e-5f50ea461469 | -1.48546 | -47.328 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 308848be-ac5f-3b06-b1d5-703b4e90299f | -1.43864 | -47.4099 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41bacc86-f1e3-37d2-a0c9-5594c1b581bf | -1.43681 | -47.40776 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dfb93da-d3be-326b-a562-66cc4dd47cf0 | -1.43605 | -47.41266 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcb5d2eb-3925-3234-b5b7-6d7dbdb4edfe | -1.43397 | -47.40915 | 2024-10-16 04:04:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ee7d729-92c0-3a5e-accf-83297afa62ff | -0.77546 | -48.70048 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cd094cf-a9b9-3170-9143-5598052a02ea | -0.77401 | -48.70971 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67f080e8-aed4-306d-a6fd-f2c96d54dca4 | -0.77353 | -48.71279 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02e61e10-e73b-3b9f-bfb2-5e8f8751cdcd | -0.77078 | -48.69655 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc222817-a17a-35e3-9cb4-ba590619678e | -0.77029 | -48.69963 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26045892-3c57-3469-a147-4e4e84549911 | -0.76981 | -48.70271 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ffa8699-0818-3103-b2d2-07b6f231a732 | -0.76933 | -48.70579 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67838024-c355-3aef-bd24-9f2d04409db5 | -0.76884 | -48.70887 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82fc69fd-96ed-3dc5-9a21-9362d6027273 | -0.7661 | -48.69263 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edce060e-3ff2-3de8-8d7c-ca4e079c647f | -0.75723 | -48.68174 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68a63487-dadf-3fc6-a87c-d3a35b6f2909 | -0.75674 | -48.68481 | 2024-10-16 04:04:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15eaaa7e-60b1-3f86-877b-0c54b4a351f4 | -1.14724 | -49.19429 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README30.md)
