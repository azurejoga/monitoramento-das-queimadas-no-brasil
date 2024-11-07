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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dea8f8a9-b808-3f2a-abc0-420d4bc88aa8 | -3.45639 | -52.01373 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4427169f-a76c-34b9-8330-7c546b22cd03 | -7.43415 | -42.90548 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1711b17e-886f-3e01-81da-b84533aafb67 | -5.82592 | -47.34822 | 2024-11-07 04:18:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0012743-b803-37e0-837e-cfeff5410fcd | -2.23698 | -53.67188 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0191c431-156b-3bca-8d90-f1ddf4c254a8 | -3.21807 | -53.1071 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f0e723-1a5c-3187-b796-d42522b2576f | -2.91862 | -49.35915 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46cac3c5-ab1b-38e5-b691-caacbdef216d | -8.35682 | -43.67266 | 2024-11-07 04:18:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8b91306-ebe4-3ca7-afec-288fdf359bee | -3.21496 | -50.30243 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3e684382-5220-325f-bf66-696d536f2893 | -3.24717 | -50.46541 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 46d411cb-2fd0-336c-a9c7-1a8f6fd0a1d0 | -6.26161 | -44.13385 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6efe0a4e-8021-3763-aa60-32e490b7137a | -3.1281 | -51.10859 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e0992b-9e76-3753-8bf4-f559f6fc688e | -3.74568 | -50.06304 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba49a7f0-623f-3377-94a3-6edb7ba3d743 | -2.18638 | -51.74001 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26839b5-9f02-3faa-b26d-d3a35f1df75a | -3.186 | -50.58691 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b56b19f-dcc6-38d1-8f0e-bcb86e7d626d | -3.19173 | -53.39739 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38afb3fb-543b-300f-81bb-6a268c763d2b | -4.30165 | -48.6193 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac15b678-2297-3634-92ff-79b4ddfa4611 | -5.39923 | -46.66473 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84eae8c9-30bd-30d5-99ef-6f553894d4da | -3.51147 | -50.47279 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ebc02dc-7ab7-3977-adcf-14a021390851 | -6.4875 | -44.68599 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 189de67a-afee-3cbe-a953-484c2a74c6e1 | -2.60424 | -48.20555 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5de1fbe-898a-31c4-ae9a-f6d237f91486 | -5.20744 | -46.32839 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78b31fdd-41db-3147-8e23-7e184ab18d35 | -3.00934 | -53.4419 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18ea70da-997a-3242-b7ee-5971b0365d1f | -2.60304 | -51.7686 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a19d3f1d-2faa-3824-bdfa-2ec4517a9d16 | -2.80393 | -46.60662 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2bdc3a2-a749-388f-af2b-464b16fdefe6 | -3.21003 | -49.22809 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57529f5b-0d85-3184-a634-731ab8080626 | -5.70667 | -45.94816 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c42701f5-af57-3dc5-a5e4-1a9ba3ed7a23 | -4.42139 | -44.47322 | 2024-11-07 04:18:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7af5e025-27ae-3a0b-aecd-60a613744510 | -8.49715 | -42.08245 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 840efa3c-ab9d-359e-b170-2d9955568645 | -8.30331 | -43.61615 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac969b60-a61d-3d6b-bcc6-21d30e459209 | -3.23711 | -50.1629 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb9b464-5133-3b12-b405-3e2dd0064665 | -3.32988 | -49.03066 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4195ef-1b5d-321a-b18f-2cd73b255252 | -5.15468 | -45.25204 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c92ae51-07f9-3f05-aa24-fcbf0897d97a | -2.72469 | -46.67153 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1197aa73-cffe-34ad-8bd2-52312a8bd2d9 | -5.16522 | -44.12828 | 2024-11-07 04:18:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1adb2f4a-183c-3543-b2f5-7ef0265b7ae0 | -2.20532 | -53.72505 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e111cf9-1298-345a-a58b-bc190e00105c | -6.07865 | -44.71727 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 77613151-c437-3c9b-9059-5abd54c25629 | -2.43016 | -45.8196 | 2024-11-07 04:18:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db248b1f-1db5-35de-a8f2-8bb55d3a5aeb | -1.33417 | -54.60772 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c4fbc3-afea-39fd-854d-fe1e68f32c44 | -3.32719 | -50.082 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d49fa6-7480-3d39-98bf-884851c098a6 | -2.8183 | -52.92205 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 292f5a09-9807-38eb-b128-8074406697d4 | -2.90181 | -51.47052 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74a491e1-091d-383a-a89f-6e8ae494bbe3 | -5.94089 | -43.77301 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ee5c59-5cd2-33b2-b2d8-e5a62d1060c0 | -8.49774 | -42.0785 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 398b3051-8b12-3573-b49a-b04b181a9fee | -2.60971 | -51.30704 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 621cbe46-b18a-3e8b-b357-3be6a0863483 | -1.51853 | -52.15158 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b06a6660-76dc-3753-8d69-ae51c45f4e6c | -2.64175 | -45.76873 | 2024-11-07 04:18:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffe495b0-b625-3c71-ab40-5d6a6e6ad5ee | -3.02572 | -53.26868 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33df9f5d-c4d2-3c85-baa1-ae010a3b3275 | -7.47614 | -47.18451 | 2024-11-07 04:18:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fed4298-e96c-3e9b-995e-e305bea3b6c7 | -7.62141 | -43.55674 | 2024-11-07 04:18:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72013a2e-2cea-311b-a8d3-97870272056f | -2.76245 | -53.22429 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80a8de0a-0769-358a-80c9-bb24a911dd01 | -3.16223 | -50.21112 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aef05596-4b44-3b0e-853e-a8299be33bc1 | -7.22827 | -42.9013 | 2024-11-07 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 75f81acf-8746-3c8b-9e29-9b9a41b36f47 | -5.29876 | -46.24059 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d180b571-333d-3ac7-a72f-933fad1162b4 | -3.16659 | -50.21187 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 686448f5-481b-3d67-a447-3e12ddb7e7ad | -5.95818 | -46.30633 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eaaf66f7-3928-3aad-89a5-13515809ba71 | -4.95332 | -46.49096 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4e19198-016f-32bc-810a-50727411ba34 | -1.28124 | -54.13469 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69c014f2-7f9c-3e7e-b133-8ad153bcddf6 | -2.18377 | -48.31997 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebb2339a-9fc5-3d74-a5be-847c6c7a5faf | -2.81984 | -52.94558 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 301ec96b-8cb3-383e-bdbc-4e7e167de3b3 | -3.80348 | -52.1574 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 441d9067-f2ff-3040-a828-5770820e2709 | -3.03852 | -48.03704 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8db6dcf-4fbf-362b-b163-7c52e7607a0b | -1.52294 | -52.22137 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44e447bb-cdbb-3987-a779-d40e69d81c4a | -4.77115 | -45.7417 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b764cf46-9afb-310a-b179-d7973462b9e3 | -2.72913 | -51.71778 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3d5b42-29b4-33df-af99-6c3a41f9af17 | -4.73544 | -43.24923 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7927fa4b-5142-31ad-984b-ee86b3c36b39 | -5.4386 | -45.13311 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c284473e-250d-38fa-b65a-8b641b08e127 | -5.01991 | -42.77332 | 2024-11-07 04:18:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59f38f46-c1fb-3ecf-a318-00abbd8b7759 | -3.65898 | -52.34364 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9ffee8f-747a-322f-955d-5f047b9e53ef | -2.8194 | -52.91547 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f98ac1bb-e8f1-3a2d-a844-ed76f2307e5a | -7.75412 | -42.23936 | 2024-11-07 04:18:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8d5424b9-9d07-30f3-b023-8f08f044c58d | -7.16641 | -35.09775 | 2024-11-07 04:18:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e5b11dca-c548-3b7b-bc31-8a477670fac4 | -3.17839 | -46.16471 | 2024-11-07 04:18:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bb22dfb-de21-3311-88c3-d6f98051d153 | -3.53283 | -51.60276 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea788deb-b1ce-394b-a634-9ef3808a3628 | -2.88134 | -48.73114 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c0f9e9b-722b-306b-a63a-e66ee8f62921 | -8.89616 | -35.7305 | 2024-11-07 04:18:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73347d68-5539-323a-a2a3-996a756b27f7 | -1.0606 | -53.66617 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da8b481e-8678-3d02-aac2-55cc4d1e36bd | -5.6146 | -45.92961 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 965be005-082a-36e9-97e4-b97989239be2 | -2.75584 | -53.2306 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b63bbeed-2252-35b7-84c2-6e9a4950898e | -2.87833 | -51.31382 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0fef30a-7f9f-3e6c-9593-74feafdb47c0 | -3.11802 | -51.11177 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae473e28-12db-39e2-8b7f-0981cf20bdea | -7.62196 | -43.55315 | 2024-11-07 04:18:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7c3027d-d5a6-3c66-8597-dbf390180625 | -5.29934 | -46.23699 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97c9c6a-86db-3345-a609-64c69c748239 | -6.37457 | -44.77781 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0562f6f2-1488-3390-9447-d23100e85cdc | -6.69712 | -43.95538 | 2024-11-07 04:18:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0857ba97-f6cf-391f-8919-87f210e1fa6d | -3.23023 | -53.40083 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa54c108-05e9-352b-81a5-8bd5deeb551c | -2.43412 | -53.67283 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 018ab0b9-402a-3d4c-afe0-12ea07f877b3 | -2.84469 | -49.44784 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b629db1-b049-38ae-907a-4e95f77a70c1 | -5.23174 | -44.91536 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 26fae928-f15f-3c39-b800-ecc8800d7764 | -6.71968 | -48.72713 | 2024-11-07 04:18:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b775f314-ee4c-3dd8-a2c7-6310e613d4e4 | -5.03311 | -46.84774 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5640b26-33f1-33af-aff8-ce9a2b40346a | -5.83611 | -44.03113 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26c63b87-d27f-3cb1-b972-1bcb183e01a2 | -1.14441 | -53.73819 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89e8ec29-eca6-39df-86f7-61776b53186c | -5.83246 | -46.26095 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fd47098-6bb7-3015-b1cd-e963c69f4be6 | -3.01092 | -53.42759 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f6bcaab-a3a1-32c8-b34a-c20d6994b779 | -7.40649 | -44.8066 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4449056d-3fac-3626-af02-2b2bfba98df1 | -2.41192 | -47.78798 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de6b07e8-ee24-359a-89f0-794995771357 | -4.5152 | -42.86994 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56e1bf16-91f2-3f2c-91aa-953e74b7de6b | -5.15754 | -49.63977 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1b4a92-4cce-3502-9956-95658cfc1da3 | -3.31637 | -51.57499 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2e25b67-8650-3a14-8582-cefc30f6a0e9 | -4.76499 | -45.73709 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README37.md)
