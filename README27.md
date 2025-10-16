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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a244179-8865-326a-bfda-0d1b12743281 | -8.81239 | -47.31152 | 2025-10-16 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 944a9c63-7661-38ca-a687-715fd407f182 | -3.61019 | -41.5861 | 2025-10-16 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b26216cb-bbe2-3850-a7d7-f7efd19e5c84 | -7.68598 | -36.3874 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 543d4e9e-3426-3f4d-8812-c081ee66556c | -10.12332 | -44.56239 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 439ed385-2f74-3890-b225-48383dbe3454 | -12.22651 | -43.31058 | 2025-10-16 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e4d8c7f-d1b8-3941-ac25-7d08d4c67b28 | -5.32853 | -45.03217 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfa9c2cb-41ed-3f36-bc9e-6e17e6026467 | -6.38686 | -41.48067 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d9e19f23-cc28-393d-97cc-c4e4e51f422c | -4.39612 | -43.39836 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30861254-67fe-383d-a32b-b9eaa57e613c | -6.06731 | -41.91482 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4513711c-2bec-3e5e-a0a1-76c9b422022f | -10.63432 | -44.42231 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85217bd0-21c3-3f07-8ae2-0fa37b483d43 | -5.40759 | -40.91346 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ba4b08b3-c9bd-3e0a-98b9-084fa27d6262 | -6.37427 | -41.48224 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 707c2733-7d59-3fc9-b998-ad4dbe020ab0 | -6.04681 | -41.89614 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 99758d28-16eb-3d92-b11b-43c47b67bd2a | -10.12796 | -44.56311 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7470c3f-ef89-32c9-88ae-91666d0a5436 | -11.43766 | -44.15987 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7ab29b-9d30-349f-925a-2e60ff023896 | -4.87284 | -44.57616 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 168778d4-8d55-3f8b-8087-7faa49851617 | -4.91343 | -41.55283 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8591f5e8-b319-3cf6-a970-5e37dc742f5a | -9.37418 | -46.94997 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9770c76e-bc2c-33d1-b396-a82be3512373 | -2.79509 | -48.94816 | 2025-10-16 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd057e51-d890-3f8b-8fef-588a898193b9 | -5.30029 | -41.17933 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e92832e-32e6-380e-adfb-8e176c2ff15c | -5.88267 | -42.81178 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07ede5bc-5ea7-363e-81df-50202e4d37dd | -2.93935 | -40.10019 | 2025-10-16 03:47:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d34f8788-ad26-39bf-9d0e-3900586a236c | -4.82765 | -45.65717 | 2025-10-16 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55ac5869-8f06-3f81-baf5-5410df9cbf1f | -5.86254 | -43.87841 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca3e9f65-aed0-3767-a5e2-2397332be937 | -4.65477 | -44.10559 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d76452b-cbe2-32b4-89d3-2944e49ebdff | -7.65206 | -34.98691 | 2025-10-16 03:47:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 43c39e3f-503c-3df1-a37a-b9fd233bd317 | -1.37949 | -49.30589 | 2025-10-16 03:47:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fad083fa-aa96-3ca8-a4e2-2d4027ad0020 | -11.45191 | -42.04598 | 2025-10-16 03:47:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a63d7135-9434-36ef-9e70-80aa6b5d4c54 | -5.44363 | -44.26883 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4aad700b-9cd1-39b3-bf14-540356d8bdb4 | -4.78402 | -38.47049 | 2025-10-16 03:47:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c4591f5-55f7-38e7-bb3e-5d059dc4cdae | -6.43157 | -41.88591 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eda2566f-d506-3bf9-abe6-e95d28112cc3 | -6.90802 | -38.26622 | 2025-10-16 03:47:00 | NOAA-20 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8f7d83cb-c079-3fe6-89fe-0eb8615227b4 | -11.43688 | -44.16421 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a50d1d2b-98a5-3d56-b15f-1da36bc9653f | -4.82707 | -45.66059 | 2025-10-16 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec1c719c-70d3-32e7-b90a-de135f1e0ed9 | -10.053 | -43.83285 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b27858ff-80d5-375c-b4d7-b4af03e2ea8d | -6.18448 | -42.60392 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3de87d22-9a17-3d09-ab7c-ee8773e7af81 | -4.81474 | -46.83867 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a87d004-b1e5-3df9-8ee7-331a74253f64 | -4.86725 | -44.57841 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9a82dfd-6f62-3cda-aebd-f9eff4217e7f | -11.42926 | -44.13136 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5da7dd65-fd7e-36bb-9688-c6aeadc652eb | -9.37286 | -46.95721 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dcf19ea-5897-3e6b-ad73-3081c3dbb2d3 | -5.83551 | -42.23225 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 413b9cb0-e76c-3cb5-93e5-f0334e81ade7 | -4.3657 | -43.39665 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 80c361a0-4d96-3d8a-b8b4-7c127ea13d0b | -6.12599 | -44.2905 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 647c27c7-d8b0-36c1-98e3-60b38b0ae946 | -9.25578 | -45.26476 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f740633b-7f66-39b6-8f25-1c3108f84510 | -6.2499 | -42.90852 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62a6d042-bc3d-3422-870a-0771bc347140 | -1.37432 | -49.30975 | 2025-10-16 03:47:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1684ef32-7366-308b-be45-06f6221fd637 | -6.44272 | -43.38209 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d85342c-e01e-3f77-88e6-f4b751b4e9f4 | -6.06085 | -44.31946 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 548eea3c-89fc-3064-8fd7-cd7b3f53faa9 | -10.30529 | -43.99102 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ad99e17-35b3-390f-a8f3-e5fa609a9cb9 | -4.38587 | -43.40178 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b8ed0739-15fe-31a7-beb1-245189fab403 | -6.15508 | -40.91605 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9cc5a22a-9582-3caf-847b-c3daab9aeb36 | -10.87832 | -48.80816 | 2025-10-16 03:47:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4e1213cd-74c7-336e-88a7-b4697db5c99d | -4.15009 | -43.13357 | 2025-10-16 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c69f2df7-581e-36d2-9335-2afb0d231fd8 | -9.08076 | -47.94897 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6710fa6-5cd1-3065-9c37-9f68f3c53286 | -3.22699 | -43.45399 | 2025-10-16 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a89a4fb0-1080-3471-ad2c-4c7324f57416 | -9.36804 | -46.95256 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94f22380-bc3b-3eab-a811-016d9e6b0561 | -5.32637 | -42.90352 | 2025-10-16 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d91ee93a-84e5-33fa-b21e-c063802e63d4 | -4.24299 | -45.76362 | 2025-10-16 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30daa3bf-bf54-3735-a59e-cfd20b4db62a | -10.12857 | -44.58006 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c16f21eb-ed62-3fe5-89a2-0a7faf84f682 | -5.43175 | -44.23378 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8528cd4-c71d-36f1-9256-f8a84e1f3b19 | -6.32749 | -44.31823 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55689ca7-b2f3-322d-8816-264e484c5662 | -6.0206 | -43.39637 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f856d60-a5a1-3b5d-8beb-c9cfe263fed5 | -10.62137 | -45.2481 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca054d01-8a53-360a-a9aa-5678f49a4cc3 | -9.35987 | -46.96616 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 094c6b17-d035-3320-8b85-8bd75478f044 | -6.14875 | -41.78215 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42e0f053-335a-3020-9fe1-a36b5d44ae88 | -6.16057 | -40.9069 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 0fe51047-4d8c-3892-9bb2-078a3bcd23be | -5.86366 | -42.8171 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2800f759-b102-3164-9d01-64fab21ebe5d | -3.01285 | -45.37471 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6eb5a54-b74b-3819-8891-766151805592 | -10.71486 | -47.58686 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f767fd7-b570-3a25-9d3b-48edfc28a633 | -5.06858 | -40.47667 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bda8ef51-0b24-380a-aa45-efc6c213c46f | -6.36968 | -41.48504 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2699fcfc-5d52-3962-baf4-8a435747f9b6 | -5.09476 | -42.63829 | 2025-10-16 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9aed067-32a8-3e99-8062-acb71c259d2f | -4.3837 | -43.40477 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fe908b3-a9ee-3dc7-93b9-d040609efd55 | -4.39474 | -43.39632 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 96ae0e05-b683-326e-b121-244a029c018b | -3.43372 | -39.65337 | 2025-10-16 03:47:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8f71d335-d828-3949-ba0a-63f26a1fb009 | -10.52381 | -43.36857 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f5e58d3-afa5-3cde-9d61-a358fa02eccd | -4.36092 | -45.53341 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f746b3ee-1497-363c-8465-a3bc6b4f6fe7 | -4.38922 | -43.40055 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7807c218-1b49-3d75-836b-e508485cbb99 | -10.05223 | -43.83727 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b1dcb72e-38fa-30e6-bd6d-2b88ab74e520 | -10.65202 | -45.2429 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d9d13c79-79c5-33a7-b163-a3367003abaf | -5.74472 | -44.98638 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f19e9f5f-282b-3c25-8008-d9ecdc4aa3d6 | -6.13721 | -41.75042 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 32044dee-6c80-350e-b986-47de0dd66760 | -4.3729 | -43.38228 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 55d5674d-5ed2-3b7c-829d-46487862c08f | -10.51599 | -43.36344 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 022f2f8b-d37a-35d7-b048-6fce4d2004bc | -4.83146 | -41.47088 | 2025-10-16 03:47:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0864cc1b-8f32-3158-aced-cab4023d0ad1 | -9.70922 | -44.5248 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd89be1a-92a6-3841-9c5a-89efd8c6cf0e | -11.57029 | -48.5614 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d274394-3626-355f-b3cd-e30f5752c283 | -5.32315 | -44.83484 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24b8c1c2-2f21-3f41-8c13-0f2dd3927bbd | -10.83229 | -43.95253 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd86bd19-35df-394a-aad4-f0f27a2510b1 | -4.38759 | -43.39176 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 663227fd-06cc-37eb-bec5-75b7f11f572d | -6.21921 | -42.50353 | 2025-10-16 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0469bfd-0695-3bc7-accc-385185e00eda | -11.43328 | -44.15904 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b30d6522-6274-3891-b5ac-76671a8fa57b | -4.77696 | -43.93234 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5d3bc8fc-2c5f-3cae-b31a-7acc85959541 | -5.26851 | -41.04926 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9517e645-29a0-325c-b06c-430d2c2615de | -10.61177 | -45.24643 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b5335af-65b0-3ad7-acef-f80b80c4df4a | -5.88315 | -43.87202 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5321d46b-6b16-3850-ba86-2309bcf326df | -6.04626 | -41.93842 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4aba8a73-eb05-38f8-857f-ef7ec79f359a | -4.91413 | -41.55734 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b45afbf8-2c2a-3352-959a-ca5746ab2042 | -6.19643 | -44.11084 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa37cc1b-c368-303f-bf55-676b439d4401 | -10.03387 | -43.83846 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README28.md)
