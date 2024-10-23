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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fcb66e9-4bab-36b0-afc4-c58bae80747c | -5.0791 | -42.56593 | 2024-10-23 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| abef9887-9dae-3e3d-a6ff-fd0180f725a0 | -5.07694 | -42.5622 | 2024-10-23 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc430c26-dd5b-3cfa-a0bc-58236ad109c6 | -5.0763 | -42.56625 | 2024-10-23 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d75a9ce-80f6-3d68-aff9-afb57ab4166d | -5.07274 | -42.56566 | 2024-10-23 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74149c94-dd70-3fd5-90ad-1a6489b25cab | -5.23083 | -43.19327 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db2b720-7c31-33f9-b9d2-ee3373eff06f | -5.22858 | -43.18394 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 178e8ad2-cfee-3247-ad1b-2fc448d39e90 | -5.22787 | -43.18826 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4baffa4a-0f06-355c-ba0c-4d46951449f1 | -5.22716 | -43.19264 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d539bd-d482-3c08-aae4-34e867c4e8e2 | -5.22491 | -43.18336 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d294769e-a651-3af3-a12f-07ac82692665 | -5.2242 | -43.18766 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cbb26fc-bec4-338a-b879-00e5534175af | -5.22349 | -43.19201 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1460275a-db40-3d15-8e30-28c3d3f8ebf7 | -5.22124 | -43.18277 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 580c50e1-a3ce-33c3-8230-2d7b5789e509 | -5.22053 | -43.18706 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa856981-085c-317b-ac8d-38847d0f796d | -5.21982 | -43.1914 | 2024-10-23 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 535c02b2-7cbc-3bb9-b748-d8f1f20027aa | -3.66149 | -43.39445 | 2024-10-23 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8b69684-a4c9-30f1-8d90-fff70341242f | -3.30742 | -43.51839 | 2024-10-23 03:57:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ce483f-947e-3873-9cc8-8417c6170804 | -3.30437 | -43.51296 | 2024-10-23 03:57:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24158f1b-780e-3bb5-81c6-30969d3a5b1c | -3.30359 | -43.51772 | 2024-10-23 03:57:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab62fd9-ca86-362c-8535-20adba107188 | -3.30197 | -44.15124 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f393b69d-193a-3550-8128-8c6d98be140a | -3.29974 | -44.15135 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 9331853c-34dc-3347-826d-04cbc218afbc | -3.29797 | -44.15058 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 59ee6312-2799-38a4-a128-b8a7b383b52d | -3.48717 | -44.19523 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c20b85c1-86bc-369f-8c7c-f214e600484c | -3.48317 | -44.19458 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0533cdb4-f090-33cd-b5b3-3a55097fff4a | -3.48261 | -44.19807 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16813c4a-e303-38ad-b18c-0195d4efa266 | -3.40527 | -44.15799 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e8670de-88d7-31c3-a774-c18d82fd9112 | -3.40127 | -44.15737 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9872762a-dbdc-395e-bb2b-cd5a901afbd3 | -3.40073 | -44.16081 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5895447-e4bd-33b4-8411-3a2ba5cb9a1e | -3.31973 | -44.3826 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 377347f9-a329-371d-91f2-20a411a1e48d | -3.30142 | -44.15469 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 021f0db5-c236-369b-864f-7d6b04033b9c | -3.29916 | -44.15481 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 3c53e408-4498-309c-a5ef-7a511ad81097 | -3.29743 | -44.15404 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f0f121ff-5124-360f-a76a-cbe1e91a39a8 | -3.23904 | -44.41722 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f25b21-a7f4-3d15-a006-0fbd723af31c | -3.23846 | -44.42087 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c658aa1-37cd-376a-8c30-06559cef51ef | -3.23497 | -44.41656 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5d390f88-4e61-39b5-9bb3-149d65d128f7 | -3.2309 | -44.41588 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 09f4b750-8c9d-397a-93bb-d03a14f7a4d3 | -4.85734 | -43.26111 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7515a300-844c-3313-952c-fdff75d3f797 | -4.85595 | -43.25893 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 629b4c8e-23dc-32a6-8daf-484579d90b45 | -4.85523 | -43.26332 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9043ab88-9295-32d5-982a-8bde3eb6a0a1 | -4.85433 | -43.25612 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 703d62a5-19db-3d26-ace9-24fca9983073 | -4.85363 | -43.26052 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5f335676-5c40-31f3-8488-9b8d7e091521 | -4.85298 | -43.25395 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32a4e5dd-75c9-3e6e-9b71-53bd36896080 | -4.85225 | -43.25835 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a2f5a35-8db9-308c-92b3-8995c91066a8 | -4.85152 | -43.26274 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8be26c5e-3862-3b00-9c4d-3ce875abbb9e | -4.78318 | -43.65349 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7c492d5-a98f-3594-80e2-087406c742c0 | -4.7643 | -43.36469 | 2024-10-23 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec56b4e9-ffa8-3d7b-8862-d520966ae528 | -4.40665 | -43.94688 | 2024-10-23 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b18d13d6-fd30-372d-950e-1ebbcf01e8c8 | -4.05534 | -43.98387 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 593db178-1bbf-3060-bc05-6e9dedc28f99 | -4.05454 | -43.98887 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdeacc3b-c630-35c7-952f-0d9e34d71a44 | -3.88378 | -43.14338 | 2024-10-23 03:57:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c68d8746-6f0d-35b4-88a7-e83fcc9b8c5e | -3.80054 | -43.23141 | 2024-10-23 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1edecac7-8fa7-3c5f-8821-26355bf8071d | -3.96298 | -44.05605 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e4e63a3-577e-396c-ac74-47418fda9669 | -3.96285 | -44.05962 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55cf9c1c-d6a7-3fe6-8897-a3474229249b | -4.1073 | -44.23268 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baed6f09-fb52-3465-bb1e-14920b7acf9e | -4.10647 | -44.23777 | 2024-10-23 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ef34a92-3102-3906-bb13-a3e7ac178cac | -3.68297 | -44.40414 | 2024-10-23 03:57:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bc21404-fc51-385b-b3dc-3b3dd40a2fa6 | -3.64541 | -44.32909 | 2024-10-23 03:57:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f996506-25f0-3953-9683-1f1277ea1342 | -3.64484 | -44.33261 | 2024-10-23 03:57:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2538100e-76a6-3b37-9685-e985b7ba7ad6 | -4.81804 | -44.35788 | 2024-10-23 03:57:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2764eaa-6307-37c3-85cd-c0a42636ba8f | -4.79185 | -44.74241 | 2024-10-23 03:57:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adcab0b0-aec0-3729-ae81-d565958ed274 | -4.67657 | -44.60621 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e914aef-6575-314a-b8c3-b2fbb8b29e83 | -4.67599 | -44.6097 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cbed97e-5093-37d1-8080-adc4d930e6d3 | -4.67541 | -44.6132 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d5e4873-9204-31c3-a0ff-fef2a988ad1a | -4.67369 | -44.59855 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e151414-0318-360e-bdf3-8c9ebb12b6e3 | -4.67311 | -44.60205 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2817c410-e2a1-392c-9b19-a86a17f3e0b8 | -4.67253 | -44.60556 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01228e27-24ad-33f2-8b02-32a3c5ca1c29 | -4.67196 | -44.60905 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f88adb05-786d-30fa-92ea-ab7bd6244e25 | -4.67138 | -44.61253 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00576a2e-b2f4-332d-9920-aab0971e6006 | -4.6708 | -44.61604 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bed35ec-4c8b-3a4c-b1d5-3edbd5a4ffb2 | -4.66908 | -44.60139 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca51e23f-ce93-377c-adc1-76710776f4f1 | -4.6685 | -44.60489 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e88011a4-90d9-3f42-aadc-dbd4d7430f10 | -4.66792 | -44.60838 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 708161f5-68d1-30f7-a7c4-d681205178d1 | -4.66734 | -44.61187 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d1e5e4-dd20-32fe-a06f-1dc76da82d1e | -4.66676 | -44.61539 | 2024-10-23 03:57:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72d209bd-fc3b-3ac7-b5b5-32f3ba54ab1d | -5.52584 | -43.47514 | 2024-10-23 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 031a6c30-0e76-37a5-8185-7459a821c016 | -5.52512 | -43.47959 | 2024-10-23 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ff64904f-31da-3c8f-8ff2-657e9612638b | -5.48745 | -43.6627 | 2024-10-23 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 717f3fb3-b81d-31cb-a6ba-7db12917b539 | -5.20323 | -43.92657 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6bba330-0bb2-39ac-8899-854b66cb4294 | -5.16002 | -43.96124 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831cb480-2e49-3c61-a377-ac7e61587157 | -5.15924 | -43.96608 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e60e90f9-26ea-3863-91aa-7c9cc5d94204 | -5.15617 | -43.96064 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 721eea91-0ac1-3055-9999-e903ece29ed8 | -5.15539 | -43.96548 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55e7edb2-ea3a-3c0d-ad5d-a6f456158712 | -5.15461 | -43.97032 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdfc95a1-137c-3d7f-be8f-25e194b07fd3 | -5.15232 | -43.96004 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c917955d-b44f-3d66-b5ce-c509f2cd26c5 | -5.15154 | -43.96487 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5003e39-de82-39d3-8d86-34c8d940c78a | -5.15076 | -43.96969 | 2024-10-23 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48273baa-1fd5-3678-8668-5451e023c772 | -5.29431 | -44.29914 | 2024-10-23 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 065e28f7-f11b-3b31-bf36-ca49bf7fd6f4 | -5.26812 | -44.2387 | 2024-10-23 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 466ae34e-5de1-39ae-927f-8582ba0cd0c6 | -5.16316 | -44.36251 | 2024-10-23 03:57:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5eb96bb-4b74-3784-ae26-9d21da48d131 | -5.15921 | -44.36191 | 2024-10-23 03:57:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac816bf4-e013-3dea-bd2a-dd86a1f7e53a | -5.09483 | -44.21596 | 2024-10-23 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e640155-59cb-3cb3-a751-be9e20aba0a4 | -5.09403 | -44.22085 | 2024-10-23 03:57:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce3997c7-bcfd-3998-90d5-02b3258efa9b | -5.00319 | -44.47697 | 2024-10-23 03:57:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 255a8fca-070d-3104-9011-2c7a0a705e32 | -3.09046 | -45.62605 | 2024-10-23 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1065f83-b8d9-38e8-975d-9fa1e3e2fc23 | -2.59071 | -45.76794 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e7b0079-34d9-3ba5-94e4-1790a0960252 | -2.36629 | -45.67506 | 2024-10-23 03:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| af7ab02e-2f65-32d6-a838-c447aa9f79cd | -2.3618 | -45.67434 | 2024-10-23 03:57:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d510326-2b84-3d98-a4d9-a140e67739fb | -3.60026 | -44.78873 | 2024-10-23 03:57:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5cd8c7e-01f7-3ff7-988b-c90b75abb306 | -3.4229 | -45.52533 | 2024-10-23 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55327508-5cba-3db0-85ef-2a4049235e09 | -3.40096 | -44.49816 | 2024-10-23 03:57:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c6a4aab-2eb2-3b28-a089-a700e7b54ef0 | -3.11616 | -45.30811 | 2024-10-23 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README20.md)
