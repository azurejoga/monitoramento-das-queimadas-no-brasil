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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00336b1b-3a15-3f33-a767-862dfede1652 | -3.4247 | -53.2808 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc9522b-ca02-31e4-996b-0058730fc7a3 | -4.2555 | -48.717701 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519f5e0e-e63f-3811-8d27-d528ed04b5fa | 1.8368 | -55.930901 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f035100-e96f-39f7-b3b4-3aa33595b051 | -20.257401 | -49.674702 | 2024-11-25 01:01:00 | METOP-C | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80bedb49-03c5-3a42-8b5e-d3d290164699 | -2.3578 | -53.710602 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6bc3787-892b-36f4-8bd4-a52c9dfd3d0b | -0.7467 | -51.9562 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4d89397f-688f-3997-9c15-e85af343ee27 | 1.3682 | -55.904999 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7fd1162-6020-3772-a12b-fd69f6d2bee2 | -2.3127 | -53.604 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df446ef-8b10-3a81-b3ed-acc8236c2813 | -3.1166 | -54.139198 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a18ab1a3-3d14-3475-b03b-bf7c56173ca8 | -1.4504 | -53.3988 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f068a2d7-7edf-3537-a7b1-b2818a9094a0 | -3.5427 | -50.458199 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379e4e0d-0117-3e12-954b-3ae1722d1f1a | -3.1131 | -53.9893 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caa66d61-7fce-300e-bdda-51777311dc0c | 1.3697 | -55.898201 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebbe0d4d-ab49-3fad-867b-10142ecee205 | -2.4575 | -53.695499 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4abea05-4121-3ebf-bcee-4baafae8f34d | -3.508 | -53.821602 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57e89efd-6b40-3d83-a09a-829fd42acb82 | -3.526 | -53.810299 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45fce85-0826-3b68-af91-ee562ac3ca2f | 1.84 | -55.917301 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d863e34f-c56f-3104-aa3b-a554b865163c | -2.8603 | -53.966801 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e550e965-c475-3df9-92ee-36436b803955 | -2.7996 | -54.016399 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e91e859-7c2e-3aa2-a751-cba29c523cea | -3.4263 | -53.2878 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 813dd85b-38cf-3e35-b70f-637e95db78e4 | -2.579 | -54.044201 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 803450c8-d355-30b0-8487-627e1b751dd6 | -3.2563 | -54.208199 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5da567ce-9b37-3903-a686-cc159291e589 | -3.4777 | -51.993 | 2024-11-25 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53978b99-c1fa-3f1f-9f35-7a52848a607b | -2.2127 | -53.662899 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b94c2d0-eac4-3a53-ae7f-a6025883964b | -3.2578 | -54.215 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59fd4768-08d5-3e40-98ab-eb33bcc365ac | -3.2484 | -53.276402 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315bff38-d9a6-3b61-9b2a-414a4d6ad187 | -2.4591 | -53.7024 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d5c761-ea41-361c-ae8e-8a447f258f0d | -3.4646 | -50.829399 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 907ee8b6-e996-3d74-8ff1-a12a558ea1f0 | -3.5014 | -50.458199 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2622549f-3cbf-37b8-9b83-5ed61f448766 | 1.8642 | -55.901299 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf74bf39-548d-3620-ac5b-b9f9bfc16e05 | -2.7615 | -54.075199 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac1bac28-503f-3187-82bf-1867036faed5 | -0.2843 | -51.604 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a6cf87f4-e59b-388e-931a-f6ec9b1c0af7 | 1.8415 | -55.9105 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4290dbb-c475-35ba-a220-a9bdf707cf93 | -3.5495 | -50.399399 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd6941e-4418-31ce-ad78-fc67592250c5 | -1.1497 | -51.692799 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ef1d69-c128-3b02-ad8c-f0219b8d242c | -2.6292 | -51.759701 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b5ecd9-28ce-3023-89dd-4979d6e0453f | -2.8056 | -53.0121 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b34df3d-b18f-39ae-9c0d-40f0bfe343fd | -0.9268 | -52.6483 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccd6a50-b7e5-3962-818e-816bc7255636 | -4.0322 | -48.0825 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1642c0f1-5ce4-3ff2-9c0d-530971685462 | -2.3265 | -53.753899 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8288d86e-e2c5-31c6-9448-cab8ed3e6f3c | -2.6263 | -54.384899 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4cbf558-847c-3221-afe4-c86535c7fa60 | 1.8462 | -55.889999 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87cbe58f-2534-3b93-aace-7db99bee37f5 | -2.1778 | -53.779999 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebefee5-21cf-3bfe-96d8-06870013eda3 | -2.548 | -54.043999 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c146fa7-b6bd-3c55-b5a3-11eee00d1ec6 | -3.2206 | -53.8284 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e607f0b-2ae8-3195-9c10-5e9080bf8cbd | -4.5102 | -49.661999 | 2024-11-25 01:01:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961148f0-18de-3375-a852-0f07bb99b9ba | -3.9567 | -50.861099 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5436524b-4bb7-3c81-8228-cb53a07fefd5 | -2.6138 | -53.9716 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cad8540-451f-3209-872c-89842bd3eb80 | 1.8301 | -55.9151 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a2c582-f73f-3141-aea0-0ca3e70231db | -2.8094 | -54.014198 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b87f0c-e907-34ee-bd23-4fd57161ff3c | -2.8012 | -54.0233 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed0f5360-4d6b-3fa8-b87b-2e4523ad3ed9 | -0.2863 | -51.612499 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a6c232c4-be62-32b9-9155-a8d57092f079 | -2.8934 | -51.564999 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1288c87-ae44-3a0b-9b2f-3fbb34887383 | -2.1924 | -53.798599 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc80e27-1c6c-38f1-ba25-a7dd4b04221a | -2.6329 | -51.775501 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cabc19e5-d466-39e2-9523-e72aa55e32ac | -2.173 | -53.266499 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b21171-fafb-3967-8c5e-8d33cd610ac5 | -3.2222 | -53.8353 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b1c33c1-f418-39b8-8220-2ff948f28a02 | -1.1982 | -51.7687 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c254fe51-6b10-37cd-b09b-8d6fd9faa16e | -3.9436 | -47.9701 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a711915-5124-3c36-9691-b61679adc9c4 | -3.1052 | -51.499901 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea57a03c-926d-337e-8190-769fec7d0b4d | -3.2852 | -51.1213 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df063bab-943e-3c0c-b0ed-80a59faa4c52 | -3.0476 | -54.018299 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da809593-d78f-3cbb-9288-c35cdabc7aa2 | -3.592 | -49.352798 | 2024-11-25 01:01:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68ae8c1-df5f-35e9-bdd6-db1890057ef3 | -1.7545 | -52.659401 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6634bb16-e063-3a31-ad0c-798ccf060e83 | -1.7716 | -52.733601 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebb11ab-7243-348f-80e6-5da78ec90fa4 | -2.5452 | -53.987 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faefa411-74d3-3f7e-9e7d-aecc9dc4904d | -2.608 | -54.260201 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ead4ba-9928-3e6f-a6b8-94dc018b0c5c | -3.9369 | -47.9851 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febe0e95-4bdc-34c3-b49f-7535ab211cea | -1.7699 | -52.7262 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 053f12b9-b6d3-36b4-82b5-d017de95f410 | -0.343 | -51.545601 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 291c27d8-cd17-378f-bf68-70db4844b266 | -2.7016 | -51.9827 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd806397-1409-397a-8f89-b4feeaef1051 | -1.107 | -53.386002 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b339cb0-e4a0-380d-9a75-f44f64871eec | -2.6709 | -51.716702 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82302733-9507-30c1-9c05-d6ab59c87b1d | -1.7245 | -52.484901 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8cfb778-11c1-35dc-9347-b4720c02da3c | -3.0899 | -53.260502 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f11932a-b38b-3a8c-aee5-f28040029e80 | -3.7163 | -51.777 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cdb24ab-c722-36d8-8126-71229f97098a | -3.7189 | -52.410301 | 2024-11-25 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4e52a2-5585-3aff-9eb2-12d24e9edb09 | -2.2538 | -53.617199 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8240298-a7d3-313b-9315-d199bdda3941 | -4.2421 | -48.661201 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b4e2e7-1d96-3b7e-b6fd-49a7468cfd9f | -1.2219 | -51.7374 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97892373-8513-31ab-884d-469a9211b10b | -0.9891 | -51.711498 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b9a2e46a-9ce9-3e9d-89e4-7e1aeb6a9506 | -0.991 | -51.719799 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a97b0a17-a463-3892-99c7-c0ee49ad0dd0 | -1.7243 | -52.751999 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e0d215-4dd4-3a7c-b56a-a6e9f4a848eb | -1.4469 | -52.443699 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af244a0-eebb-36b4-9135-719990f75bcf | -1.4956 | -52.5205 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37722a8b-9faf-3e2f-893a-265184407939 | -3.9466 | -47.9828 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7782606-62a9-3b3a-85c5-5705c599e133 | -3.6434 | -51.1535 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e55262d-0efa-3939-83d4-4dfcb8d423a6 | -2.9051 | -51.570801 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e74c4aa3-0028-3e6c-8846-a2b5027be685 | -2.8007 | -54.066502 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a31a04a8-458c-3e1a-b24e-2b5e36a83548 | 1.8446 | -55.8969 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be411f2e-a0fa-384d-88b6-119717e2bd05 | -1.7665 | -52.711399 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1701a566-a141-34c9-9e6c-a65340638302 | -3.6556 | -51.383099 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba30b2f-050b-3a8c-9e08-cfd4866373de | -3.8038 | -51.1777 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 859f6bab-a27b-38b5-a5c1-57ff2cd17c52 | -1.6415 | -53.870998 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8c5bfe-a117-3e23-b482-80735eefd810 | -1.3138 | -51.734001 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24b4366d-171e-3f11-a167-c357ebdd35c2 | -3.0492 | -54.0252 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bedf394f-a861-3bdb-aa6c-abcd2d36c04b | -2.3111 | -53.597 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 264387b6-58ae-3db5-8939-d06bdb6da550 | -1.2042 | -51.750099 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082f6239-677e-31de-97db-cef4fea79795 | -1.5728 | -52.006599 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb8afe7e-f76c-3189-ae81-90325a0427ec | -1.484 | -52.515202 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
