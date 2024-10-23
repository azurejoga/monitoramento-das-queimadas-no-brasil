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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c6b5c25-b02c-37e1-9909-9048b2ce89df | -11.12057 | -48.10691 | 2024-10-23 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 771d9850-06b2-397f-9078-bda44d96784b | -11.11169 | -48.63906 | 2024-10-23 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efe0fdb6-eeeb-3f2a-8661-9dcc583348b9 | -11.11166 | -48.63749 | 2024-10-23 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a79f3945-ca72-3370-ab58-583f7e2c17e1 | -11.11073 | -48.64275 | 2024-10-23 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4eb075f6-f40c-3eea-a273-d48072dc234a | -11.10694 | -48.63818 | 2024-10-23 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 101ed56b-9fbd-3f06-bb4f-f4fdd10ef8f2 | -11.10598 | -48.64183 | 2024-10-23 04:02:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 000d2084-f72a-367f-bd73-5c6a66d29142 | -12.19921 | -50.36634 | 2024-10-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 274eca31-e9af-3bb9-8f1c-784daa2869b2 | -12.19858 | -50.3696 | 2024-10-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5104e959-0bda-3bfd-8893-c72ab348966e | -12.12772 | -50.28668 | 2024-10-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cce284e3-ffc4-39c0-a43f-0e9a3b56efb4 | -11.46027 | -49.61533 | 2024-10-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55fa10ff-2a18-342b-88fb-7f4f391bd4b8 | -11.45971 | -49.61826 | 2024-10-23 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6449d62b-5448-3cf9-aead-2c39c608e27c | -14.2632 | -51.12491 | 2024-10-23 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe4d6161-a430-36ea-bd8e-0c0ec7ada7ea | -14.26253 | -51.12834 | 2024-10-23 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52f649e4-33f3-31af-8687-2c62c056233c | -14.25857 | -51.12056 | 2024-10-23 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3111525e-2dc7-3992-8f07-10000ca8b17e | -14.2579 | -51.12395 | 2024-10-23 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 027f1dc8-1037-361e-8485-0ba243484d4b | -15.85889 | -50.53576 | 2024-10-23 04:02:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62d17bec-943b-3d3d-bd8c-8832569ef33f | -15.85835 | -50.53375 | 2024-10-23 04:02:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c7b2ac5-7129-3f86-b4ff-8db9add2b470 | -15.78377 | -50.81206 | 2024-10-23 04:02:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb0463e-3296-3286-b9eb-5ae67d15bec8 | -15.78289 | -50.81028 | 2024-10-23 04:02:00 | NOAA-20 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dbb3fea-086a-3a3c-b242-df5e21dbba16 | -15.69579 | -50.46839 | 2024-10-23 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e307bba3-0f38-3767-9fb4-427278b95f0d | -18.16511 | -51.63739 | 2024-10-23 04:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fb48c25-2ab4-38b1-94d4-e96385d39cac | -18.31126 | -56.21812 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 7c41ff0c-5e20-396a-b333-e814b1eb4535 | -18.30981 | -56.22424 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 5c1f4af1-e1aa-3b31-a854-dd8e374d77c8 | -18.30842 | -56.21509 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 80582064-1054-330f-9a44-fe3723a484c9 | -18.30701 | -56.22121 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.4 |
| e64bb0c9-2e8f-3e2f-b80e-45e7b2322351 | -18.30611 | -56.21027 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 8c9fb3b8-1702-307f-ac73-1293f6fc6b1c | -18.3056 | -56.22738 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.9 |
| ef0c5dc1-8175-3cae-8b05-1bef4ccba507 | -18.30467 | -56.21637 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 78ba3662-9e3f-3f2b-af9f-9290c51412f9 | -18.30322 | -56.2225 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 3b7cdb1f-3ae6-37bf-b621-c3f1a140672d | -18.30184 | -56.21332 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dd15a504-680e-32a9-a1c9-56628172f32e | -18.30042 | -56.21945 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b4bbab39-37bd-3585-9997-50411cb9f4f8 | -18.27088 | -56.07637 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 58f28ab5-e9e5-3790-b71c-b6bacdc34e40 | -18.26912 | -56.06625 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9153c1c4-a0e3-3340-8c37-ce63ba13c4d3 | -18.26776 | -56.07226 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e5359358-abee-39b8-a545-4ca405cc166f | -18.26713 | -56.06266 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3dfc7dd3-8f92-398a-888d-c0481533131d | -18.26573 | -56.06865 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 79e4b6d4-60e5-3819-b0ca-4c1075bfa159 | -18.26433 | -56.07465 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 583d102d-62da-3870-b49b-cf3206672391 | -18.26292 | -56.08068 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a258cddc-8287-356b-8847-be1d2471d23c | -18.26258 | -56.06451 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1523702a-bf37-3252-a572-ded367336f3c | -18.26122 | -56.07051 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 98b3dfe6-3df7-39c7-95e5-c05e50c43d71 | -18.26059 | -56.06095 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 80953cb7-1389-31d8-a867-ca9d8b710e69 | -18.25985 | -56.07655 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7e26ce70-7742-30b2-8fc1-0284a2357739 | -18.25919 | -56.06694 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 94e2e880-581a-3694-85ac-597b184b3640 | -18.25848 | -56.08258 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 53844ac4-c5cd-37f7-ac39-1d1e2f9a0526 | -18.25779 | -56.07294 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a1aedb6e-f6b5-3410-b6c0-477041a55ac6 | -18.25637 | -56.07896 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 46f2b6bd-f567-3ccb-a62b-34fa5bef6eb9 | -18.25468 | -56.06878 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0231999e-0311-302f-bec0-7872c2a5e1ee | -19.64242 | -56.75826 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2e377cde-4b70-3cee-846b-d7ff8aee78ee | -19.64092 | -56.7645 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 366fe4ce-0d85-3f3e-b9f6-e15e8a92cb10 | -19.63581 | -56.75642 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c63fa6b4-88ce-3732-b953-2658b9c6c2bf | -19.63431 | -56.76268 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c238b388-5e78-3938-b2ed-540e39b1a8b4 | -19.63341 | -56.79583 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| bd31be73-a3ec-3f92-8521-87f45f193b92 | -19.6319 | -56.80212 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 120119ae-ab6a-3c52-b296-44d92fbc9ae4 | -19.63039 | -56.80841 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 27da7961-f56a-3d6d-8523-2deed6aee12a | -19.6298 | -56.78145 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| d657a719-7d49-323b-9d9c-6129810ad9bb | -19.62888 | -56.81472 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 8f4f325c-f397-3210-a51f-3b623f58f705 | -19.62829 | -56.78773 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 9003734e-1142-393f-8fa9-269877b02db1 | -19.62678 | -56.794 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 1f6ea3e4-8db3-3e7b-871e-ffb5dfac9c7d | -19.62619 | -56.76711 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 150fd88f-a3b1-32f7-be53-87ebfb94398a | -19.62527 | -56.80029 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 038c0588-1122-3620-aae7-5dcbea07a808 | -19.62469 | -56.77335 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| eec159cb-342c-3d69-9ca0-70c3671896cc | -19.62376 | -56.80658 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| a308831b-9d93-3d82-8153-26c24af2b864 | -19.62318 | -56.77961 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 58d80942-bcef-3dfb-bd62-7a73f26c2094 | -19.62224 | -56.8129 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 573d848c-f7d0-36c1-9808-b40f64e01f23 | -19.62167 | -56.78588 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| cba2305b-cc11-37c3-a921-2667378057f0 | -19.55928 | -56.62315 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 61f68622-09e5-3b1f-b016-276e030e4aeb | -19.55409 | -56.67426 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| af4dac52-d1c0-31c7-b12e-3b6771824f6c | -19.55271 | -56.62136 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4b1c3aaf-ec21-365c-a826-bbdbc2d0e093 | -19.55261 | -56.68046 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9f8aa95c-b970-3574-9c7e-d398651150f7 | -19.55113 | -56.68667 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 340e3ecd-a480-308b-9fb9-7bec3ce8241e | -19.54964 | -56.6929 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| bd62a1a3-bd34-3188-b865-c67137e161b0 | -19.5476 | -56.61343 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f5ce6336-331e-382e-9396-f13cad3534b4 | -19.54601 | -56.67867 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 258c8b0f-7d16-33bc-a829-28bbd69425d3 | -19.54453 | -56.68488 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 37cad662-cd3a-3a04-b8c9-56092abfd22e | -19.54304 | -56.6911 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 16a97466-5120-312a-a14b-6ad0c6ccf55c | -19.54155 | -56.69733 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 3d27720e-93d9-3a29-98ff-4fb02edc1a2d | -19.54005 | -56.70356 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| afc9e5ca-9b19-37ad-9b3a-e6bea5ebded7 | -19.53941 | -56.67686 | 2024-10-23 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| f1f5ff6b-fae0-3421-9acf-a0f5dba4bb9c | -19.53793 | -56.68307 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 4946a42b-ba1c-34fd-bf03-cf4c391ef99e | -19.53539 | -56.68016 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f27b0a58-d45e-357b-a7ca-5b8785149e83 | -19.53282 | -56.67506 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 746f4b56-c8c8-395a-b76f-c2b3ff4288ae | -19.53025 | -56.67212 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7766c766-4114-33ab-b6e8-8b1778b0d125 | -19.52879 | -56.67835 | 2024-10-23 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5d4d1b24-19fc-3a86-b5eb-f43bf6136c80 | -20.34845 | -40.36133 | 2024-10-23 04:04:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5184917f-c004-346f-8f2c-fabb1dc717b7 | -22.30674 | -41.88075 | 2024-10-23 04:04:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b40fec6-c710-39db-a877-3c3cfe7831d4 | -22.30334 | -41.88015 | 2024-10-23 04:04:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c638801-60e6-330a-b89d-8706bf24c85f | -21.94122 | -42.27121 | 2024-10-23 04:04:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 55d4e98c-5d5e-3512-9882-58e300d9c2da | -21.37668 | -42.14292 | 2024-10-23 04:04:00 | NOAA-20 | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cbbf0ace-50ec-3e7a-8ecc-4fc2a6682814 | -21.62588 | -43.46518 | 2024-10-23 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2185af1d-489a-314a-a37b-fd1544470ce8 | -21.62529 | -43.46888 | 2024-10-23 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37f0186b-d398-3705-b3dc-5399ccde452a | -20.90054 | -43.81875 | 2024-10-23 04:04:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 47eef846-c3ca-367d-8625-fca4e3a69931 | -21.18097 | -44.27349 | 2024-10-23 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d7b89dd-8290-39de-ab8c-6d5b79250f12 | -23.06004 | -45.71815 | 2024-10-23 04:04:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aabb118c-dcaa-3495-ab33-b32c489d316a | -22.92155 | -45.41357 | 2024-10-23 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23e8f06c-e290-3a57-94e6-484bc2c70532 | -22.00107 | -46.80415 | 2024-10-23 04:04:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a3c4358-b68a-3439-b4fc-6d5997ea29dd | -21.99884 | -46.80519 | 2024-10-23 04:04:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98e73283-74e5-3fec-9a82-075908dd3690 | -21.83564 | -48.00712 | 2024-10-23 04:04:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2df7443-42be-3e39-98b9-8d1e856617f2 | -21.83184 | -48.0064 | 2024-10-23 04:04:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea3ab824-5fbe-3e01-961b-3f290381a708 | -26.12344 | -49.48764 | 2024-10-23 04:04:00 | NOAA-20 | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ec98ea1-063b-30da-b585-b69f82d8ea0a | -22.24223 | -49.17473 | 2024-10-23 04:04:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
