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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43f18c79-a7da-3091-aee0-68574b35281c | -20.48241 | -44.0745 | 2025-10-07 04:10:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a60db99e-73f9-33e7-9cb8-dfeaab1b23b0 | -19.04291 | -48.14031 | 2025-10-07 04:10:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bbe2ab-c0b0-300c-b339-bf12f9907d16 | -12.97308 | -46.77833 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e7ea324-27b5-3db8-80ce-e972572990e7 | -12.94126 | -46.78654 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40228de6-8529-39a5-b1dc-ab915eb57b65 | -15.14634 | -45.81366 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d48aeaa2-c881-3efe-b780-b0187e5060ba | -13.05605 | -48.71086 | 2025-10-07 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbc65a9d-eef7-37c3-93cd-4f93ac243098 | -14.7738 | -46.06607 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7dac33d6-3952-372b-901a-76177a6f5107 | -13.06296 | -47.92909 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4c3aa46-f205-37b0-824a-1fff4156c69c | -14.61849 | -52.54845 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de39490-e598-3dd0-939a-c4d56bf80082 | -14.90463 | -46.83464 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31bed866-e6ac-3102-99dc-b069b67c4185 | -13.27395 | -48.06024 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| caabf3cf-f8ef-3629-b2ea-f0e1d898cf05 | -18.64168 | -43.84224 | 2025-10-07 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d6a018a-cc23-3589-9db6-24ca7b2d5e8c | -18.1209 | -53.34824 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d77cccdc-af4e-3d34-8fae-1c58073d901e | -15.38976 | -47.99946 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bde7295-f675-31c5-8b87-0b1675a8ee8b | -14.9982 | -42.01458 | 2025-10-07 04:10:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40b4f3b7-f778-37a5-aed6-9fd079c4e61f | -13.35386 | -47.56649 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83fe96cc-0f12-3788-94e1-01683f9515bf | -13.98399 | -53.91504 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e8db3b8-0ce7-3619-a968-626ef72c50f8 | -13.36622 | -47.2517 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b0e5fda-90ab-3275-a5db-b80d890783c3 | -19.81705 | -45.32927 | 2025-10-07 04:10:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09b4b9f9-e255-3b59-bfc9-959d6e8e6718 | -13.66529 | -44.3053 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b1f3f95-ef47-3875-a45c-230e5342f80e | -13.08386 | -47.81231 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07382a72-00f9-3433-8b50-7897d7366ee1 | -20.09583 | -44.20238 | 2025-10-07 04:10:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1dac37ce-51b6-39cc-8f44-e1950b72b27a | -14.5563 | -46.62371 | 2025-10-07 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7434f9e1-b791-3293-9459-cb057001b8fe | -12.72688 | -47.93995 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 504dc8fc-397d-3f4c-8427-a957e5e2b886 | -13.35527 | -43.66751 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c37cc34-b9a8-393d-848d-e43d4d9c56b0 | -13.33946 | -47.56755 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d6cbcdc-773f-3de3-afdf-8b42391b6632 | -15.82274 | -41.89623 | 2025-10-07 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdc16e0-34b0-3043-a060-67022a821a32 | -15.79751 | -43.717 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2da0086d-e497-3f82-af24-c1b128436801 | -16.28873 | -45.24263 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5f65540-4dff-300b-ac45-b51fae567c80 | -14.93034 | -51.41967 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d595f5a-1a74-3fca-8efa-970da8079dd9 | -12.73144 | -47.93719 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37b91a37-a12f-3a13-934a-b9aa6888437b | -11.87067 | -56.89196 | 2025-10-07 04:10:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 890b7bab-6144-32d8-b928-6e2dfbd92ff1 | -13.27518 | -47.5731 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 624277ca-a360-3ed7-b217-f61111873a75 | -13.50053 | -43.67319 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c2b64f32-99b8-3eea-9b6a-88777dc906a2 | -13.37329 | -47.23309 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7b8f09f-a6f1-3d75-b5fd-f5c48e124dbd | -18.10767 | -53.36092 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aae3627f-66e2-334d-b8b9-7f621854b1d8 | -12.90732 | -54.7398 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c7be3ed-844a-320d-b24c-bf3131a79d1b | -13.34142 | -47.56968 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d7ccb93-d547-346e-89dd-956e1f351f72 | -13.71888 | -48.19486 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96795f46-d427-39c8-9a7e-39c48cfada70 | -13.25812 | -48.05741 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7842aaa8-b7f1-3351-bbda-42f16a07f67c | -13.09094 | -48.00047 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a24b720-9636-3ee6-8be3-c8ac6fa6292f | -13.51763 | -48.61738 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b6b30d8-a940-3e7f-928b-31c393e2a8c1 | -13.73753 | -48.65381 | 2025-10-07 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 192a73e8-59aa-3409-a831-be554ef98762 | -14.70656 | -48.38935 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cec467be-fff2-3241-a487-55e9036d01fe | -14.66215 | -48.38697 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70f35f8f-f3a8-3f98-9ddf-0d3c379192f9 | -13.06153 | -47.89183 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93d5d6aa-5e38-3c0a-969f-c44068cd0f0c | -13.59243 | -48.68998 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 183e6911-4c79-3784-9544-58e626f723b0 | -16.32054 | -47.91351 | 2025-10-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eab82895-e2fe-3ec3-a50e-20e19ae74b3a | -13.22878 | -47.81433 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40f7bafd-e51f-3358-a0e4-e5b9b1b06f4d | -15.27348 | -46.33812 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10f3fe90-40fd-3352-9c5b-2b4bc9cea031 | -13.99057 | -53.91188 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 207ed027-46f7-3d77-be20-baaac82ceab0 | -14.76883 | -46.05282 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b6d7b8d9-c034-325d-97cc-2f89e4211556 | -16.3168 | -47.91279 | 2025-10-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4488768-8899-3670-8d51-07f24ff74720 | -19.95858 | -44.62909 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c068f088-13de-3086-a179-a04376cb1fb7 | -12.54663 | -48.16039 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4582d560-0957-38e0-a3df-4eee4cb3b35f | -12.7665 | -50.4871 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d6a2ea8-7bfb-3a28-9918-b43241131a54 | -13.0712 | -47.95121 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c013bca-79fe-3e16-a7eb-c1d28a4e40c3 | -15.3609 | -47.32628 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0809bfe9-64f4-3dc8-8adb-90944f0f1943 | -14.75463 | -46.0092 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f9c890-36b2-30ca-819e-b1544bf7e26b | -14.92948 | -46.79835 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 23916094-de25-3687-9312-98541527c612 | -13.07474 | -47.88744 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a4418b2-335d-3d43-b536-dd16abecb45c | -15.53652 | -43.84126 | 2025-10-07 04:10:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b5df6bb-8070-3265-a8bd-94e6584b5f2f | -14.76372 | -46.01905 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e61b2d17-b200-3809-8f95-a3059f365868 | -15.60307 | -42.3737 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e2ecdc9-ed9e-3e86-9ac6-fac055523a21 | -13.66805 | -44.30943 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f194ee9-7265-3c86-9186-ab56268e243a | -15.79434 | -46.24854 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89997a37-0627-3fcc-9548-a7cc5b1f4972 | -13.24729 | -47.17456 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 151c6f4c-433f-3c8e-92e0-fbb5c20cc87d | -14.91414 | -46.82271 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d115e310-68ef-3143-88d4-ab5505bff430 | -18.92616 | -49.48808 | 2025-10-07 04:10:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1911e7bc-0db8-3444-bfd8-71ad5dc283d2 | -17.57175 | -44.42067 | 2025-10-07 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6950eb34-3931-312a-9add-4947a7b0f5f8 | -19.02998 | -44.73406 | 2025-10-07 04:10:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3022ef4a-a78c-30e8-9cc4-b2447689de73 | -14.91903 | -51.40271 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac51ff39-6087-3a79-93a9-09dba2b3d9b8 | -17.03225 | -43.45261 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73245dd6-2177-3334-abb4-cab495651d8e | -14.76668 | -46.04424 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a6686b36-74a3-3b8b-b178-02810a96ec37 | -13.08716 | -47.86158 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5286589-0794-3e54-bbd4-4272a0f13dbe | -12.95232 | -46.78854 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73c45d90-9cbe-3d17-a96d-07de8c2bed95 | -17.87473 | -48.23174 | 2025-10-07 04:10:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf414420-0729-3307-a2b2-84fa7767dcd3 | -19.71047 | -44.12203 | 2025-10-07 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 278d9a53-1699-3ee8-b107-714ab73cd955 | -12.13504 | -50.87789 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0340e46b-4848-33f3-8862-6b6c87769c63 | -14.7652 | -46.03165 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0a75119-a4cc-3f10-89b0-8bf5766e74bc | -13.26211 | -48.05797 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dee1cab0-b0a2-374b-89d3-0de06f0dec84 | -12.1785 | -47.77266 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c03b1e55-8019-3b10-840e-ffaf39498cf7 | -14.63304 | -48.32654 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a8d7d34-53a6-3c8f-b8f7-439ecfd7e3cf | -16.25519 | -47.11237 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f12b47a-6108-3952-b8cc-0cf84fab2603 | -15.59695 | -47.2681 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82dd8462-0b34-33f4-8ebd-c3c033a090d8 | -15.51369 | -46.83192 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a121c007-176a-3061-a5ca-eee056719093 | -16.0074 | -50.82849 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 77b2662e-2c02-3d96-89ea-31ed27751cf1 | -15.61689 | -52.56171 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1239586b-9a4c-3a9c-8867-3a3d220a5969 | -13.72636 | -48.06112 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0c3125f-cef0-3b3b-a8a5-eb78f9e4fb7b | -14.38682 | -45.93056 | 2025-10-07 04:10:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26e04654-ebe7-3d1f-8c76-6c93688621d0 | -15.3821 | -47.99824 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9cc9161-a0f5-3924-bcad-ecba145ce14f | -13.39917 | -42.64809 | 2025-10-07 04:10:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1631a01d-edfb-3a35-b5a7-323172087b0f | -16.18281 | -43.42614 | 2025-10-07 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9980eefd-4641-3b69-a8e2-8afcfec5ef8a | -18.51553 | -43.91027 | 2025-10-07 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9193f8c-4c70-3829-9acd-7c5e1c2fefe3 | -15.8459 | -44.44423 | 2025-10-07 04:10:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 392e6953-cfa3-3983-a06c-a36af15fdb91 | -13.08398 | -47.83414 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d109209c-ae29-3029-b2d0-744ade3f13c7 | -17.54708 | -46.76521 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85f9698c-2fe3-3c69-893c-de649b5fbd70 | -16.19849 | -43.65566 | 2025-10-07 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf9d87a8-fabd-3267-a628-dc78e64a63ab | -18.28919 | -45.408 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b40161c0-3a2a-3061-be16-c97c6180bcd7 | -12.95423 | -46.82146 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README46.md)
