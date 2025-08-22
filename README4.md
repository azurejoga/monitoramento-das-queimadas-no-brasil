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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f81afaf-4b48-37cf-9280-2d85ef7419fb | -5.79989 | -59.2244 | 2025-08-22 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f93c876b-0137-3a93-b17b-75a6828b0639 | -9.21337 | -60.7974 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d878cd19-6330-3bdc-9bdb-8b14b332f651 | -9.1581 | -59.59021 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 49ff58fc-d381-314b-bc66-3d577801e1fe | -12.9776 | -56.8976 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ff905d02-1db1-33d6-9aec-d9d55349a44f | -6.43685 | -53.38503 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 87bc48f5-1ace-3f8e-8283-b7831b553725 | -9.52881 | -60.56387 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 467118a1-402f-3eba-9cdb-900fe52f74c9 | -5.87721 | -57.76281 | 2025-08-22 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8cb1a4a1-b926-3cf8-8934-bb3b68acf187 | -9.21168 | -60.78455 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 71a42e22-4a57-30f0-83e3-1859454afbf4 | -9.52718 | -60.5514 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| fb2e2585-dd2e-3185-a223-9fd5814e88b3 | -6.89608 | -59.89347 | 2025-08-22 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72e1f60c-1b20-3621-9c17-f1bced98849f | -9.21153 | -59.4742 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6b8439a6-a99d-3151-9816-1045fc5fa7bb | -9.17008 | -59.70495 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3242d0bd-20f0-3d48-99e4-0c942ea4b99d | -10.46289 | -59.13195 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fb2f0d97-19a4-3e6c-920b-a4e1eda27112 | -4.32617 | -55.13952 | 2025-08-22 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 15c6397e-d6c6-3c0f-b1b0-2353ca71027f | -5.88893 | -53.63722 | 2025-08-22 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| f4fb308e-89f6-3d16-85b8-5f60521d4782 | -9.50164 | -60.51672 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 30fa801d-50f0-384d-b399-c404495e8738 | -8.86319 | -62.42201 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6a1e0b3c-c650-3912-b7f4-20cd76ef88c3 | -9.51198 | -60.51539 | 2025-08-22 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3676ab78-7e29-3bfb-828c-8e4497c1a5ee | -11.31742 | -55.22948 | 2025-08-22 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6aa15df4-119d-351b-9347-7fd557e4f991 | -12.4959 | -53.80717 | 2025-08-22 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 696bec5c-6acd-3d6f-9a2e-1d40a4041123 | -2.93025 | -53.69692 | 2025-08-22 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 517aa696-21df-3697-a7af-dd7c43248e56 | -8.88912 | -62.43574 | 2025-08-22 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| fa27657f-30be-3643-ad31-4b4447e305c6 | -9.23083 | -59.7687 | 2025-08-22 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae90b33d-0c5a-30f3-86e4-1ffcf19df590 | -4.83199 | -55.76365 | 2025-08-22 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8db828c7-8a69-3f3b-8c22-5819a8b56951 | -9.59387 | -55.35881 | 2025-08-22 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b3e586a5-720c-3d21-829a-4d707ebb145e | -12.49741 | -53.81762 | 2025-08-22 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1e69aba6-c6d1-3094-a136-cc968f69cb1f | -10.11312 | -57.76321 | 2025-08-22 01:09:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dc8d6ab0-a0ac-35ba-874e-e30e17bfe275 | -8.5943 | -62.6315 | 2025-08-22 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b92e4007-aadd-3edf-b895-42872e39605f | -8.8735 | -62.4305 | 2025-08-22 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d768004f-1c20-397a-b9b7-43547d37b584 | -18.8798 | -45.0334 | 2025-08-22 01:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c3e23139-d51c-3c4c-8f41-ee05335deda3 | -8.6129 | -62.6308 | 2025-08-22 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 5cddfe48-a0d3-307a-b8c1-4eb781e9fd65 | -8.8922 | -62.4107 | 2025-08-22 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 06b3c6dd-30b4-3faa-a1ca-4107b886e4bd | -18.8805 | -45.0093 | 2025-08-22 01:10:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 90561649-5dcf-3e41-90a6-3903c7cfa0b2 | -12.9921 | -45.2252 | 2025-08-22 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6a631090-5a23-3d96-925b-a6e43d70e9ec | -13.0114 | -45.222 | 2025-08-22 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c7227761-57da-3f59-b5ad-631a2f7c8cb0 | -8.8736 | -62.4115 | 2025-08-22 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 94d09095-42fd-359c-b15d-ad8e33b2dc7b | -8.5944 | -62.6126 | 2025-08-22 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| f42aa114-9416-3a48-ab08-d99d1e03318d | -9.5365 | -60.5451 | 2025-08-22 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d8558d3c-2989-3435-b490-45eb6f0922bb | -8.8921 | -62.4297 | 2025-08-22 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 42feb608-e75b-3d2c-9210-0c61d38f442d | -9.5179 | -60.5461 | 2025-08-22 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| e128d9fc-bb5b-3b9b-8a3e-f2940fe4ba89 | -21.5032 | -47.2204 | 2025-08-22 01:10:00 | GOES-19 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 1ed9e62d-4699-3ffb-a127-9128416d308e | -8.613 | -62.6118 | 2025-08-22 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3cc9adc8-4ab5-3fc0-955e-accb23c52a02 | -12.9528 | -46.2647 | 2025-08-22 01:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3d85facd-6507-360e-b139-0e8a6912bd63 | -1.97054 | -56.51797 | 2025-08-22 01:11:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b98aad8d-b6b1-32e5-bd4d-13f9061f9a68 | -8.8735 | -62.4305 | 2025-08-22 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b920800d-08f5-3cbb-bd38-1f9037a76f0d | -14.9205 | -49.473 | 2025-08-22 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 014888fe-34b2-3043-8a9f-4db366e3a373 | -12.9528 | -46.2647 | 2025-08-22 01:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a4703fdd-0b29-3f9f-945f-5ae975a47d39 | -8.613 | -62.6118 | 2025-08-22 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 54328a9e-4985-371f-bee0-0383e570bd1e | -18.8805 | -45.0093 | 2025-08-22 01:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6206c981-8d13-3530-a8ed-3c2c936c7812 | -14.9214 | -49.4289 | 2025-08-22 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| dec92edf-db7b-308a-b7ca-b3e30761d25b | -8.5943 | -62.6315 | 2025-08-22 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b79483e5-7359-3723-91ef-5e4d72c7ecc8 | -9.5179 | -60.5461 | 2025-08-22 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f0fc6699-692b-3065-9233-49aad1328c66 | -8.5944 | -62.6126 | 2025-08-22 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cfe25180-6fc0-37b8-8540-5b3497b41d76 | -8.8736 | -62.4115 | 2025-08-22 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b9247639-bfc9-3a7e-85b5-cd5a7bf050d8 | -8.8921 | -62.4297 | 2025-08-22 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| fd82699c-1515-3d7a-8be8-87897879ede2 | -13.0114 | -45.222 | 2025-08-22 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0af405d2-4166-3587-9c2d-2a2799805155 | -14.9019 | -49.4319 | 2025-08-22 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 8120434c-22ec-332e-a859-ffdcd6719b2a | -14.9209 | -49.451 | 2025-08-22 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 301.5 |
| 742d46ea-3d47-3d28-8681-8a772d43ff2e | -14.9015 | -49.454 | 2025-08-22 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e487f952-1c4b-328b-bb5e-53117bde2980 | -12.9921 | -45.2252 | 2025-08-22 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 6a092816-e148-32fe-b657-3ba336901add | -14.9205 | -49.473 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| dffe3b2b-3827-3ba0-bd59-51a01fad9d17 | -14.9019 | -49.4319 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 44c9924e-fa04-3fea-ab75-14a446ad0cc9 | -14.9214 | -49.4289 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 57f868a1-b1d7-360d-94f2-55aa5b3aa435 | -8.5944 | -62.6126 | 2025-08-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 18dace4a-af3c-3e48-b1d4-0d76c2bad282 | -8.8736 | -62.4115 | 2025-08-22 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| edbaee5a-8541-3d93-a4aa-8b0635b460c3 | -18.8805 | -45.0093 | 2025-08-22 01:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a9307096-4dfa-369e-b269-719b5129cde2 | -8.6129 | -62.6308 | 2025-08-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e83cf8d1-913a-3369-8704-6fe582d70472 | -18.9008 | -45.0044 | 2025-08-22 01:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9f1f6905-ad56-3138-a401-be60d640bfb2 | -8.5943 | -62.6315 | 2025-08-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 07fee862-39c6-333c-8802-a2b1e26b947d | -13.6582 | -45.7161 | 2025-08-22 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9f6d4292-b859-3400-af87-5205247b0c34 | -18.8798 | -45.0334 | 2025-08-22 01:30:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f811ce8d-6806-3458-8de3-a0033be0b2b6 | -14.9015 | -49.454 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 189.6 |
| ca043cf1-c5f9-37df-b488-19083991b3f2 | -12.9921 | -45.2252 | 2025-08-22 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f6a99ef5-ab95-3309-a40b-bce09babec72 | -14.7979 | -59.6542 | 2025-08-22 01:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 87f92783-d912-305d-aff5-81d80c1ff575 | -8.8921 | -62.4297 | 2025-08-22 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 819c7398-1cd4-3d0b-a760-2703dbeb4cf6 | -14.9209 | -49.451 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 559.0 |
| 08193680-eb24-35dd-9069-06c9390d8e97 | -14.7787 | -59.6559 | 2025-08-22 01:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 7507a151-5bcd-3624-9dab-e2869ab00d3c | -14.9404 | -49.448 | 2025-08-22 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 964e560d-d729-3715-9a07-8deebe507edd | -9.5179 | -60.5461 | 2025-08-22 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d40f211d-5a39-3268-8a43-231fce58e522 | -13.0114 | -45.222 | 2025-08-22 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bd5d341e-b161-3afc-988c-80eef51187e3 | -8.613 | -62.6118 | 2025-08-22 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 30cc2aba-94aa-3eba-9a86-1af7c1f2f13b | -12.9921 | -45.2252 | 2025-08-22 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cf71c2c8-076b-3f2b-990a-8139bb30700a | -13.6587 | -45.693 | 2025-08-22 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 533c600f-390c-32a3-9f7f-1a577f4ec5ed | -14.7979 | -59.6542 | 2025-08-22 01:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| e4ff2f65-5030-3124-b05c-c0ac8a165a60 | -13.0114 | -45.222 | 2025-08-22 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e7a54b88-7622-33ce-94aa-0b0ca2a42f9b | -8.613 | -62.6118 | 2025-08-22 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 32cc5d59-ded3-3d20-a49e-59fd6dcf4516 | -14.9996 | -54.855 | 2025-08-22 01:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 26bb5022-91f0-33c7-a701-05c7b0adec12 | -18.9008 | -45.0044 | 2025-08-22 01:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ae06b353-11da-37e3-b2a0-b8e9f13d33c2 | -14.7787 | -59.6559 | 2025-08-22 01:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a2bbcb6e-085b-36b3-8cce-e7fbd350ba9a | -18.8805 | -45.0093 | 2025-08-22 01:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| b20168f2-e3dc-3c85-94d9-3fd9b5c20ca3 | -8.5943 | -62.6315 | 2025-08-22 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a6207fb1-19d5-3905-95d7-4b5a8ee259ed | -14.9209 | -49.451 | 2025-08-22 01:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 96018c2d-1785-38b5-82c2-7607fd112cc6 | -9.5179 | -60.5461 | 2025-08-22 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 455a10f5-97a8-3432-a4e2-8ef9b14e0424 | -18.8798 | -45.0334 | 2025-08-22 01:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9d085608-5a1d-3514-9cde-2eff629b3e78 | -8.5944 | -62.6126 | 2025-08-22 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f7ec77cb-91ad-3f5d-8536-384e53987785 | -8.8736 | -62.4115 | 2025-08-22 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f3349f55-5022-3dbe-8b76-cd3fd21468ca | -9.5179 | -60.5461 | 2025-08-22 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 823d2a3e-f87c-3e52-9715-6ed438b50ef5 | -8.613 | -62.6118 | 2025-08-22 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d9a97f81-d2c5-3eef-8cd0-242458c18492 | -18.9001 | -45.0286 | 2025-08-22 01:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 103dad10-4ce1-3e78-a921-8217ab5115a0 | -8.5944 | -62.6126 | 2025-08-22 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |


[Clique aqui para ver as próximas entradas](README5.md)
