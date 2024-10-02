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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db0c567f-82a6-396e-8190-9ab1d590dc13 | -8.46388 | -62.71538 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e627a0f-380d-367a-a696-ef7d0e8ea4c0 | -8.46384 | -62.72331 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b7916dd-6579-3315-af0f-17e3fecde394 | -8.46305 | -62.71989 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a9a3de9-5f84-3fd7-bec0-fb3c223abb4c | -8.46219 | -62.72455 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 48cd8d11-4ed1-33e7-bc2a-a8e9317383df | -8.45867 | -62.71766 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5c126e8-41e7-378c-b077-521179d1eab7 | -8.4578 | -62.72223 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46366325-3eb1-3bc0-9d2c-83ad4e2aeba5 | -8.457 | -62.71883 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7d1c68f-c47e-3f1c-a25a-003e1d57a483 | -9.5455 | -62.80607 | 2024-10-02 04:46:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 58f82bcc-9572-3268-862f-192f65ed543a | -9.5446 | -62.81071 | 2024-10-02 04:46:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dd233436-10a5-36a0-85ba-2300a9655c7a | -9.9367 | -64.9179 | 2024-10-02 04:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a538a47e-b8f2-3163-bf9b-237d6fe1e990 | -9.9553 | -64.9172 | 2024-10-02 04:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4d2b9d45-5a69-3b05-9dcc-48007c0aa633 | -10.867 | -69.495 | 2024-10-02 04:46:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d5a0be9b-be58-3a93-b07c-bc1101a007ed | -11.6742 | -65.0172 | 2024-10-02 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c92ebe1f-0349-3a35-bdb5-327c221e7daa | -11.6743 | -64.9983 | 2024-10-02 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2d0c12f0-075d-3b9f-959d-601d61dc0d7e | -11.6931 | -64.9974 | 2024-10-02 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 87dc3d3e-4431-3d10-b467-8f019d4edfe0 | -12.6486 | -63.1022 | 2024-10-02 04:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8a85818a-2b6e-348e-bc52-ecb7e2bc6976 | -12.6484 | -63.1214 | 2024-10-02 04:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 06c89ae3-dcdd-3977-bf6b-518e9f930709 | -20.35406 | -42.75775 | 2024-10-02 04:49:00 | AQUA_M-M | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d0765acf-5786-3e74-b5b6-9d2e1026a8ad | -20.34495 | -42.75617 | 2024-10-02 04:49:00 | AQUA_M-M | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d9b330b9-e41a-3b14-b935-f474fc128868 | -20.00691 | -44.51404 | 2024-10-02 04:49:00 | AQUA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| f9a7705b-81a7-323c-b89c-5032e5c78a6d | -19.99512 | -44.5188 | 2024-10-02 04:49:00 | AQUA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9e820eaa-5b28-3314-af17-e447dd8f1e5d | -19.99483 | -44.52447 | 2024-10-02 04:49:00 | AQUA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| bb29fae5-3449-35f2-8fcc-11b79ac3273e | -19.50365 | -42.87153 | 2024-10-02 04:49:00 | AQUA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 02cf47db-9f26-39ac-93ef-d10a3b5fd9e7 | -19.43301 | -41.37088 | 2024-10-02 04:49:00 | AQUA_M-M | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6f3877e2-50fe-3d86-8866-ff0a653d9f07 | -19.23048 | -46.8541 | 2024-10-02 04:49:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1dbd46e4-6663-33ee-ac45-c5f8ee075dad | -18.52329 | -42.23382 | 2024-10-02 04:49:00 | AQUA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| d60c8e3d-5d32-3d9c-90e2-1337e9828210 | -18.34248 | -44.01477 | 2024-10-02 04:49:00 | AQUA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 37ec35b9-4b6d-3edb-bf2c-219cdd01321c | -18.34035 | -44.02736 | 2024-10-02 04:49:00 | AQUA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 0ea789b3-cb18-3ecb-b95f-79e3c856608c | -18.32668 | -43.23326 | 2024-10-02 04:49:00 | AQUA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 3ac69d6d-c3ea-3ede-a7f1-13554df672c3 | -18.32602 | -43.05783 | 2024-10-02 04:49:00 | AQUA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 03c0e2b1-bac3-3e8b-9d44-84410afbb339 | -18.32504 | -43.24329 | 2024-10-02 04:49:00 | AQUA_M-M | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| f08ad236-58cf-3cc4-8261-ddd534576719 | -18.05646 | -42.61398 | 2024-10-02 04:49:00 | AQUA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 22b005e8-0c32-340c-9836-d98780988287 | -15.90818 | -50.12837 | 2024-10-02 04:49:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| d84ec29f-b309-3160-b866-dd97424cce01 | -15.90101 | -50.16525 | 2024-10-02 04:49:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 4667222a-f17b-37f9-b39a-962a09bd51c1 | -15.8961 | -50.13326 | 2024-10-02 04:49:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 91b2661f-de33-396c-8c17-2684dc275560 | -15.27867 | -47.51161 | 2024-10-02 04:49:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5244dc1a-8548-390a-a287-59ea562c2854 | -14.38583 | -43.27526 | 2024-10-02 04:49:00 | AQUA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 2e214848-9df8-314e-811e-4e18a071b453 | -13.20302 | -48.60741 | 2024-10-02 04:49:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c0270d58-5e53-392d-9a6f-25fe1d7ef38f | -13.19708 | -48.63915 | 2024-10-02 04:49:00 | AQUA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8f1da5f3-5e9a-348f-b926-a5777e289da6 | -12.43716 | -43.71627 | 2024-10-02 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 25aee038-5a2e-324a-86cd-67981da539f5 | -12.43491 | -43.73003 | 2024-10-02 04:49:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| d449186b-ae6a-3b43-80a3-a78b22944ed7 | -11.88151 | -43.80542 | 2024-10-02 04:49:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 33c58e70-d589-3494-8de8-7a7ebb42ea5a | -11.87871 | -43.81282 | 2024-10-02 04:49:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0f6dc95b-ce1d-33a0-81b0-823e1a321da4 | -10.66117 | -44.49044 | 2024-10-02 04:49:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| aacd3c38-1475-3c75-8583-d51be501f1b2 | -10.65446 | -44.49613 | 2024-10-02 04:49:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5ac30876-c8cf-374d-9d87-9f3f7ec50d63 | -10.99575 | -46.55716 | 2024-10-02 04:49:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e255f180-ffaf-3b07-87a8-022ca771add1 | -10.58736 | -48.05738 | 2024-10-02 04:49:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b3cfcca0-daa5-35b3-b5d8-aacff32e69e2 | -10.57903 | -48.04782 | 2024-10-02 04:49:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| e86c5396-dc81-3a79-9604-f42fef79df38 | -10.23233 | -47.67146 | 2024-10-02 04:49:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| fa165d9b-87f6-3058-adf4-1792b6e2fcea | -10.23014 | -47.67596 | 2024-10-02 04:49:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| e18e2d6b-334a-3614-9fe1-893c880bd402 | -16.41633 | -44.08907 | 2024-10-02 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 905e3ff7-55d3-35f0-803f-cadc7a6b6f35 | -16.41595 | -44.09241 | 2024-10-02 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bffbaa-9516-34d9-a35f-4064dbd1949a | -16.42986 | -47.00607 | 2024-10-02 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b118bc02-2078-3a03-836a-821a80d35835 | -16.42555 | -47.00526 | 2024-10-02 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85ddd7ad-7460-3ed6-88d6-cf7a6ec8262b | -16.58984 | -51.31907 | 2024-10-02 04:49:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cee30a4-8c1e-38ce-9316-2d388d5f51af | -16.62688 | -52.58329 | 2024-10-02 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd483bbb-ceea-33f9-b22f-c02089c2df23 | -16.62744 | -52.57967 | 2024-10-02 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15974817-e442-3f0f-829e-36fed2352797 | -16.62412 | -52.57911 | 2024-10-02 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcccdc77-d9db-3b42-940b-caeb3a508111 | -16.62301 | -52.58635 | 2024-10-02 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5558b081-3a78-3724-abe3-4232c7d7bd19 | -13.71293 | -44.66862 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b4da0d-706e-392d-a3af-6c1465053ad3 | -14.19089 | -46.4635 | 2024-10-02 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e80218e0-0702-3820-9a90-7c1e2bb2a381 | -14.19036 | -46.4676 | 2024-10-02 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f09e8539-b866-35cf-a518-61161464efdb | -14.18602 | -46.46691 | 2024-10-02 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8035788-60dd-3f9d-9dd2-3c1ed331dcf4 | -14.17232 | -46.47005 | 2024-10-02 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45607a68-421f-3cb0-91ee-57aa29ae4727 | -16.67922 | -43.88594 | 2024-10-02 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16e0315e-cf45-3fc7-a639-cf6987bb2c72 | -16.69113 | -47.82424 | 2024-10-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eda68e15-b8d9-3501-bd63-066e8d8e3737 | -16.69065 | -47.82794 | 2024-10-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1537691c-bad9-32d6-a368-8afcb118aa16 | -16.68699 | -47.82376 | 2024-10-02 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f1a10aa-ad98-3702-bee5-e0e007a5aa58 | -16.61969 | -52.58579 | 2024-10-02 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93cc1fb0-9c4e-3598-b482-a190646aad9c | -16.11116 | -50.41355 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28e9e532-58f9-3743-b48c-88eb2ad79633 | -16.10761 | -50.41309 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea9dbee4-fe69-3fca-a4b8-31cb242918d2 | -13.22929 | -48.62061 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50e71a70-efa7-3a4d-9122-ea8dc2a4b98f | -13.22553 | -48.62018 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f7b4249-8055-3553-9a45-43a4dd8c2537 | -13.22308 | -48.61024 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b9727ff-358f-3b29-897e-edd5b0e57951 | -13.22242 | -48.61498 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bbaa301-539c-3748-a245-ea5c61d33baa | -13.21867 | -48.61443 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a640b48-07e9-3a68-a063-f75c2fba5b49 | -13.21492 | -48.61383 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7bd412b-2bab-3d10-bbcb-24c05ccc34a3 | -13.21428 | -48.6185 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9b6e721-4bfc-3a30-8d92-863ac9636dcb | -13.21364 | -48.6231 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 224b1f93-2f03-37e6-8c25-ec40403eddf6 | -13.21313 | -48.59908 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 915ea3dd-d048-3a7a-8b8f-68a90eb5235d | -15.07777 | -48.94384 | 2024-10-02 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b09d602d-5eec-37b8-a9a0-2c5be1095f93 | -15.08935 | -50.28045 | 2024-10-02 04:49:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5afb1a1-29e1-320a-8d1a-97e8856a4699 | -13.66024 | -50.35748 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f52f0795-a6cb-3661-ba83-83399bc23fba | -13.65678 | -50.35693 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a45b46f1-0c86-3ddb-95a2-53052c15e41d | -13.6562 | -50.36085 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ac1a78-a090-31d5-aab0-4acf5f143fd7 | -13.65274 | -50.3603 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd3d3f71-c721-385d-8e19-20915ccb195b | -13.65216 | -50.36422 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dcb2093-94ed-3508-833d-5b994a0527f2 | -13.64928 | -50.35976 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3bc642d-37c3-379d-8641-26a6b1db16b8 | -13.6487 | -50.36367 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 053d07d1-f09f-380b-a138-05535de59a53 | -13.64061 | -50.34638 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af4d2979-730b-3bc4-821f-eb587c59987b | -13.63772 | -50.34193 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b58045-35d1-3581-85de-c65e9902f41c | -13.63715 | -50.34584 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f84e09-3091-3b01-841c-9577eb1f9386 | -13.63658 | -50.34976 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db674b59-0616-3fe7-a47e-68ad0b5193de | -13.63483 | -50.33747 | 2024-10-02 04:49:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cba9018-dfb8-308e-94ca-eb23a473c9fe | -16.10598 | -50.29957 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcfdfa30-a8bd-300f-8bf3-6d55ab494ad5 | -16.10562 | -50.29852 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8535fd8-4b0f-3034-8b2f-ba6453bfa326 | -15.76685 | -44.65628 | 2024-10-02 04:49:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1da69245-e73c-3a4e-be4b-e61c74ac4f0f | -15.62458 | -48.11102 | 2024-10-02 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4500005-5ee4-3c23-ab24-52efeaf4c937 | -15.38729 | -47.43293 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcd008e8-d1af-3604-9b5c-b8862442ad2a | -15.34409 | -46.73726 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README94.md)
