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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d34152-341d-3973-b71f-6a57e5adadbc | -20.12145 | -44.39882 | 2025-10-05 04:49:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d8da4f41-b579-3787-b723-029ace16979e | -14.97118 | -49.97395 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26f66cd3-be62-34d9-9d60-23189f655e01 | -15.31993 | -47.32063 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7efa8c4-e078-32f1-a243-ebb2c8063c61 | -15.97553 | -50.86191 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d86b2c0f-ec03-3b64-85ad-d0715f1c8237 | -15.13896 | -45.74827 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 37348f3a-49d8-3062-b4ff-03975290aba2 | -14.67097 | -48.35656 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6817eda2-562d-3224-a636-0188064c3d43 | -18.24289 | -53.36813 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3919c4b-bc61-3560-9b11-efd1805027f7 | -14.99201 | -49.98161 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a28076c0-2ae4-34c1-b8c9-b4880b5ae652 | -18.19727 | -53.28982 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1b4b655-2eeb-380d-9d3b-4d1e8cb01567 | -14.95907 | -49.99022 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b25c600e-15fa-3454-a429-8689464d763b | -14.61056 | -52.51544 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4629818-2df5-3d30-8991-524c4bb52a50 | -15.58561 | -52.49819 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce11e874-84ee-3171-afe1-de383a8fcdd4 | -15.30128 | -59.23594 | 2025-10-05 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a939b33b-4d80-3b18-84be-87cab8a965d8 | -18.24843 | -53.35419 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f49efe4-09de-3d33-9266-310a1299f98f | -14.88235 | -47.23303 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc4dde89-7b97-3feb-8014-83ac33f05b0f | -15.98308 | -50.90767 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3d4254f-3673-328e-957b-4ebf5c004699 | -14.31816 | -49.91648 | 2025-10-05 04:49:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5fd421a-ed4e-36c6-865d-f77fec78a759 | -14.33627 | -47.68705 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 849ed17c-c4c1-3d06-9c99-8f7f59393e77 | -18.25453 | -53.33664 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1b9c089-3ad3-3dd0-a989-63ba024f5b59 | -13.74697 | -47.93636 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c272b261-ef62-3c40-ad61-9f6326b99e58 | -14.93834 | -46.84138 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfb37d7b-bf0a-3d9f-ad61-a52836502386 | -17.84616 | -57.62967 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cb901afd-7b5e-31ed-908d-40c9286c7903 | -18.25723 | -53.36314 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 544debd3-bdf0-3ca3-9160-d12d842d4664 | -15.24501 | -53.78342 | 2025-10-05 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 417bc2aa-1bdc-3ef0-9303-9176553385af | -15.54017 | -46.8064 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f85328ec-5b2f-31d8-8d66-e76b734c8721 | -14.30135 | -53.25255 | 2025-10-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4995021e-bd13-36e4-8747-f1a51aa87fd3 | -12.94479 | -54.72747 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03f9d2f7-3afa-3cc2-8939-14388307e215 | -18.25336 | -53.3662 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a7da755-51c0-3b81-8a88-da5fd43a1312 | -15.30115 | -46.32085 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90317540-c2ec-3255-bfef-f7702147de9a | -18.003 | -45.00027 | 2025-10-05 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 210b6041-dbde-3c57-8c3c-b3da1b1efd92 | -18.24076 | -53.33794 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a19d60be-14f3-3810-a645-29217ba161fa | -14.33114 | -47.66344 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7755aa94-715c-33f0-9708-327067b42261 | -16.01382 | -50.95623 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b7b936a3-8313-39aa-8f40-9e5598ba97b7 | -17.88727 | -57.64606 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 40c75b12-3ba5-37e6-92f5-89a9504c9001 | -18.98266 | -48.36871 | 2025-10-05 04:49:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91ca5d4a-226d-31fa-aa97-06edf4bc4bb4 | -17.72483 | -56.77581 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0d819dc6-ba01-34af-aa7f-39f904169529 | -15.13088 | -45.73695 | 2025-10-05 04:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47923321-7304-3545-a716-ce7d40ffd00d | -14.60727 | -52.53675 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 031b8ab6-30e8-3ef3-bea2-78871a6aabb9 | -14.3224 | -47.6985 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ace4634-85fe-3cc3-91ff-6e894fc2bac3 | -19.24282 | -47.85283 | 2025-10-05 04:49:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fea08aa1-fcb5-3b37-9f33-1d7b58fa06bf | -14.64664 | -48.33022 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 60e6017d-1e68-369f-a408-9f573d3c9fd9 | -14.82453 | -52.93197 | 2025-10-05 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17814498-cc45-38f3-b251-4df236e2fab9 | -15.5751 | -52.47797 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abc463f8-c255-3430-99a7-794032ea0780 | -16.53698 | -47.76712 | 2025-10-05 04:49:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68254657-ea90-38c5-bfe9-b1c24e6079ea | -15.31264 | -56.9441 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3259c8e6-4505-30f7-806a-a05b24717a24 | -15.52208 | -46.88007 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad4b7df1-043e-3b40-b7b1-7f8e01b17e70 | -14.68471 | -48.3429 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 708c5ead-00da-3484-ac94-0434f5010d62 | -15.57233 | -52.47383 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a5ed59e-595a-3b98-ba27-3bf0470d70f0 | -17.91364 | -57.62703 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ac8b95c6-8c8f-3885-aae0-f73f288d1f9b | -18.23802 | -53.33376 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f3cfe4-6eef-32ba-b57b-ba2ce4109dd9 | -19.94694 | -44.64327 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 837a856e-f817-3538-a3f4-06d3cc8adf0b | -15.29154 | -47.33523 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91358727-4280-31fe-951d-8bbb441f1a79 | -17.919 | -57.61842 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ce56531e-7eb0-3deb-83e7-203f63a3a8fe | -13.91574 | -48.2002 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3410e53f-2cd4-3214-a3af-7dce9f991306 | -15.53581 | -46.80588 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dc14f0f-c391-335b-bc07-8f927c66cfd6 | -15.37297 | -47.97692 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b1ddae9-0f7b-3ca5-930a-6b6f314b8ce9 | -17.96317 | -57.58452 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2f860d02-ad0d-3f67-8f8e-2c1a355681d4 | -16.1097 | -47.4759 | 2025-10-05 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7e506fd-8a5b-3f5d-8a8c-c7b8648df48b | -15.24158 | -56.76897 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae1749b7-5ce2-37f1-9622-3e767ddfe458 | -14.4184 | -46.17581 | 2025-10-05 04:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 127f5634-205c-37a9-bf4e-fea81aacfb57 | -15.18549 | -52.77658 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5468642-80d7-3d3e-b7b7-b9fa250a0c71 | -15.35287 | -47.97385 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 861f3c31-5a45-3fa1-b064-9f9f819498c0 | -16.12586 | -53.98083 | 2025-10-05 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ba98ab4d-3b83-30ab-89f2-e255e76eeb40 | -14.74636 | -54.65728 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0be2af9e-4d3c-323a-bb01-0f6089e169fa | -16.39219 | -52.15144 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8e86534-ac7b-33d5-aaff-9a8a8eaf3783 | -18.19992 | -53.36076 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b7bc1db-8a56-3fb2-b214-4510c3b363ab | -18.24127 | -53.35666 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7590592c-fc9e-38e0-9999-a2a9abba366f | -14.61331 | -52.51954 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6768bf9a-6f5e-3cf2-9cc6-6d1175455845 | -14.94852 | -46.84886 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bbb7de3a-9d50-3d97-8c79-8c53c6caeff4 | -15.57343 | -52.46667 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee6bc22c-eb17-31a3-b067-615a47f5ba62 | -17.94436 | -57.60469 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 2a5b4792-c92c-3cb3-a831-03bc583b3306 | -14.29788 | -45.86547 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a5afc3f-30ec-31d3-8cf9-4c61f9c54152 | -19.94791 | -44.63363 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bff83936-c117-3607-bed7-4eedb1665c2e | -14.97836 | -50.00071 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96899510-8c78-33bd-9255-79675da0da79 | -18.20267 | -53.36494 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0b02258-2fbf-3aa4-8157-ace1a1eaa5b0 | -15.29256 | -47.32752 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46f39b6f-0837-3d73-ab4e-b0d44331ba80 | -13.73594 | -51.2724 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7e4ab6-64dc-3968-af66-d555f7621300 | -15.28987 | -47.94349 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 491f7686-003a-30b3-9aa4-4fdbec307689 | -17.86924 | -57.62896 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b855a9ac-ab4b-3b40-a023-a6a7ec2ec9c5 | -14.66531 | -48.33943 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 42d49868-2044-38e4-a2fe-007db674daff | -14.64986 | -48.32973 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1265cdc1-3eb0-376d-a69a-85a0f3a349de | -20.12111 | -44.40225 | 2025-10-05 04:49:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5bad0913-5c17-3e7e-870f-8a342250288c | -19.52364 | -46.4502 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b042fb0a-383b-3025-993e-6b1295d1273f | -15.12623 | -45.73627 | 2025-10-05 04:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02766e1f-0dea-32a9-ae82-4f057551359a | -14.74697 | -54.65352 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84eb1ac9-c320-31fa-8b8b-6b5e713bf6b4 | -16.39887 | -52.15259 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b73a93e-acaf-3312-ad3d-65f2161e3346 | -16.35094 | -51.4789 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3a0d0b3-949e-38d8-8e54-e11b1753ed17 | -15.30279 | -46.30781 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbab5891-a0a1-3401-84c3-63fb68f929c5 | -14.65687 | -48.33645 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7280a347-a6d8-370d-a0f8-6a62df45752c | -14.66075 | -48.34383 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60c28fe1-2876-3340-baea-349288132dc3 | -14.74975 | -54.65778 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b60665c-721a-3027-8481-4241279c82b4 | -19.50348 | -50.37079 | 2025-10-05 04:49:00 | NOAA-21 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d829ad3-d777-335c-a4f9-04254f8c2123 | -17.88306 | -57.63751 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f913ebeb-6d9b-36c9-b7df-76e540488a95 | -17.88217 | -57.59865 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ec402a64-80f2-3c6d-81c7-84147c8b47cd | -14.89166 | -48.26185 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c7d65ef-1daf-3153-8d63-ae1dffaa32a4 | -18.2457 | -53.34997 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a865ed0-d5f1-36dd-ac19-bd0ae3914af5 | -15.87866 | -46.25793 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f1a11bc-0dd9-3a4d-b835-1fac9c7d57b7 | -16.94766 | -52.6825 | 2025-10-05 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb65f72b-e46c-3eed-96b4-47b5e4067c88 | -12.42538 | -57.56384 | 2025-10-05 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a3026b-443b-37b5-8442-7ec13b13f42b | -15.20147 | -47.19989 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README111.md)
