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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e2520f3-1324-30a0-8892-7b40d3c62626 | -18.02313 | -42.07572 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cfbbd8f2-a98f-3df9-a9c8-dfe3e6770b45 | -18.02913 | -42.07774 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa9f4b0a-b3ad-3338-b463-6b716be039f4 | -18.02197 | -42.08087 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 33f7e719-80b5-3275-8f37-8fde69a8c516 | -18.01318 | -42.12009 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2b0d6761-e1fd-32a9-8ff5-dda6a1bce16f | -18.01197 | -42.12549 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| de40d037-957e-3891-b7ef-88a28966af5a | -18.00716 | -42.11808 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8aa51c11-dd20-37ee-b16c-d02431bfbcb6 | -18.0061 | -42.12281 | 2024-10-07 03:15:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2037c192-4b7e-30d3-9a18-9435f7498bc9 | -17.84076 | -42.22884 | 2024-10-07 03:15:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 254a0f2c-679f-3feb-850e-16a73e08260e | -17.83677 | -42.22821 | 2024-10-07 03:15:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 93e31d91-8df1-31e5-9b3c-93d86950e0d8 | -17.56651 | -43.72245 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f80179ef-62cd-3d81-aadc-a7176a137c9c | -17.56099 | -43.72105 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5bb85dd1-67d6-38f6-911d-24905d034abf | -17.55979 | -43.7206 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b83c0010-f15c-3b12-a26b-325d84246746 | -17.54947 | -43.76507 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1578ab7b-90b1-3023-af57-6a19a9972670 | -17.54414 | -43.75719 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05c9acf-2d23-319e-89f8-6063eabb643d | -17.5373 | -43.75579 | 2024-10-07 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 52c5dec6-061b-3c72-af4a-da41e504385b | -15.79402 | -42.28049 | 2024-10-07 03:15:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6fe21c0-ee7a-3378-bd12-23490d08e82e | -12.71143 | -40.22345 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d16d9456-4df1-346d-a0b3-2b5fc3f4b87a | -12.71176 | -40.22592 | 2024-10-07 03:15:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6a59bf94-f58f-3728-a718-152c26edb3dd | -1.0365 | -53.7389 | 2024-10-07 03:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 5a16a675-7f52-388a-8588-6507c13b7b92 | -2.2297 | -53.7026 | 2024-10-07 03:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b9b793fc-be5b-373a-9fa8-2314ca3bb9ce | -2.857 | -52.8993 | 2024-10-07 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1d9562e7-57b0-3c2d-a2c5-f6ac67c60cc2 | -2.8753 | -52.9192 | 2024-10-07 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9182ca51-6f94-3432-b651-500dd17dd10f | -2.8754 | -52.8989 | 2024-10-07 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e40e030c-8423-3e36-8d30-f887a02dfba3 | -4.2729 | -43.737 | 2024-10-07 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f3d57127-8cac-3f38-aeaa-67b915235e9c | -10.8754 | -63.9169 | 2024-10-07 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c428b376-7227-303d-a6a7-17ec594d2996 | -10.8755 | -63.8979 | 2024-10-07 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 06331af6-6d83-36e9-98f0-047770d2cb28 | -11.266 | -51.3686 | 2024-10-07 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 83f66ec3-53d9-356a-b7dc-c71d0d2f5601 | -11.2847 | -51.3878 | 2024-10-07 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 399c3238-444f-3ebc-9d1d-94fe82b6cf29 | -11.285 | -51.3666 | 2024-10-07 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4b6deda1-0b8e-34dc-8b09-e0fee438df20 | -11.7566 | -44.4897 | 2024-10-07 03:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7b33aef0-327a-3cfa-86f2-740d5be7556d | -12.1274 | -50.9118 | 2024-10-07 03:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4a1ba795-ef9c-37a4-bf02-2745ff078497 | -12.1277 | -50.8904 | 2024-10-07 03:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 48378a7b-1d3e-3a24-8daf-cadeeb3cdec4 | -12.1468 | -50.8882 | 2024-10-07 03:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6e530c1e-1a5f-3745-b16f-beb808a51395 | -13.7342 | -60.6471 | 2024-10-07 03:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| abd78447-56ec-3810-9abc-f0a135e87aa3 | -16.4164 | -57.3006 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| e3ede87d-e1b7-370d-86e5-e6b35f3e8037 | -16.4362 | -57.278 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| e1c994a8-90ff-34ff-ad51-0f8976152d7d | -16.4753 | -57.2735 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 6621675e-bb53-39a5-acaf-a9a4d632b45e | -16.5072 | -57.7387 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| d0ceef5a-cdbe-36b1-a50d-58d77ac5a3f1 | -16.5075 | -57.7183 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 175d16bf-130a-3495-91ea-34a5cbc788ea | -16.5267 | -57.7365 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 15cb3aa3-9767-3569-a45f-6835a032cc8c | -16.527 | -57.7161 | 2024-10-07 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 66ff98e3-462e-357b-ac26-986d9ec47bac | -17.012 | -56.698 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 6017f3cf-1ce5-3c2b-a92e-3c3ff5cdf603 | -17.0685 | -56.8352 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 7193ee12-10d9-3579-b3ee-3f994efcea14 | -17.0881 | -56.8328 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 51428a90-c7f2-3337-9794-8f6fb0c77c7e | -17.1078 | -56.8304 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 1203d494-e8e0-3230-875d-33c9bae9cfd5 | -17.1274 | -56.828 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| d4d2db2b-fcc9-37c9-9a99-0a2fa343f00b | -17.1278 | -56.8074 | 2024-10-07 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| d2196c3a-4033-3223-a102-a4d171c7839f | -17.1581 | -57.3582 | 2024-10-07 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| c8bb1afe-3859-3834-acc6-27f6f8015d9a | -17.1584 | -57.3377 | 2024-10-07 03:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 1fea2392-4e17-3045-9dc0-89989705d413 | -17.6279 | -53.1094 | 2024-10-07 03:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3bd0a21a-66bd-32ce-8a14-01e4150689ff | -17.6283 | -53.088 | 2024-10-07 03:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 24f2e855-8e83-30d3-8aea-23e5b4ae42eb | -18.4718 | -53.5134 | 2024-10-07 03:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6ce615dc-52dc-3131-beb9-e52a7acad2cb | -18.6387 | -57.2785 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 821b36a9-fcbb-3bf7-add3-ed2b7ef4fb5e | -18.6391 | -57.2578 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 9a19a26a-46ad-3e1f-8ac2-00a8af90ecdb | -18.659 | -57.2552 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.6 |
| c397443f-ca2c-37b5-93b3-5f1e90fe7941 | -18.7176 | -57.3097 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| aba94d6c-34de-395b-aae1-031d653b31d8 | -18.718 | -57.289 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 22575625-ce8b-3131-a064-015c62adcd89 | -18.7375 | -57.3071 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 7bfe036f-255c-3f14-98f1-85676d41d047 | -18.7379 | -57.2864 | 2024-10-07 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.1 |
| a6972e85-cebe-3d5f-a83e-5fb6e82fc57c | -19.8838 | -42.641 | 2024-10-07 03:16:55 | GOES-16 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.6 |
| 723fe9b2-d231-32ec-b189-94d1360b2769 | -20.5848 | -48.5137 | 2024-10-07 03:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 131.4 |
| ea87d63c-e5b7-3049-8b46-4cb86725dc7e | -20.5855 | -48.4904 | 2024-10-07 03:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 177.0 |
| e06f8d07-26c1-30a6-886b-0049b94892c0 | -20.6053 | -48.509 | 2024-10-07 03:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ffe7b0eb-801c-3322-a4c4-c012fa94870f | -20.606 | -48.4858 | 2024-10-07 03:17:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 182.7 |
| a38e24a7-49a7-333a-96ee-c2ea698b053c | -21.80465 | -42.51488 | 2024-10-07 03:17:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 86e721d9-6346-31ff-8aef-9b435cfb4490 | -21.80062 | -42.51327 | 2024-10-07 03:17:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 45eebc4f-4ac8-327b-aeb3-2b8695659939 | -21.71104 | -42.29319 | 2024-10-07 03:17:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1e1d003a-2d60-3792-b7cc-fa385927c811 | -21.7101 | -42.29732 | 2024-10-07 03:17:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0f4fcefb-37d6-3698-bbd6-026ffe33ab75 | -21.70542 | -42.29106 | 2024-10-07 03:17:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| fc316ebc-0e05-3d93-9cf5-f12510cb7876 | -21.70449 | -42.29515 | 2024-10-07 03:17:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ea81aa19-20bb-3a88-ba5d-fa3ca9f27148 | -21.70341 | -42.29987 | 2024-10-07 03:17:00 | NOAA-21 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6ac45207-ab02-3e94-b5c4-83b592ca68bf | -21.67246 | -44.00447 | 2024-10-07 03:17:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28ce80ea-0c6a-32d1-846a-74d7ca8941fd | -21.67173 | -44.00273 | 2024-10-07 03:17:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 71c0ec55-16a2-3373-9f44-4b669c48769a | -21.66612 | -44.00278 | 2024-10-07 03:17:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 121f38fd-5f4d-3213-bb9a-0c72c5103d92 | -21.55499 | -42.3366 | 2024-10-07 03:17:00 | NOAA-21 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 023ac373-fb85-32c2-b0a0-7297ecc109bf | -21.54665 | -42.34613 | 2024-10-07 03:17:00 | NOAA-21 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 66e1e585-0f61-3f64-bf7e-0296ceb3b5fd | -21.4029 | -45.34552 | 2024-10-07 03:17:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f526e211-8e79-3863-a69a-51673c790764 | -21.40287 | -45.34873 | 2024-10-07 03:17:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bcd3db0c-373d-35f9-b43f-cad8c9b2795f | -21.40107 | -45.35593 | 2024-10-07 03:17:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 557602c0-5834-35fa-8b18-c0fbfe9307ef | -21.40107 | -45.35267 | 2024-10-07 03:17:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 38295cba-d893-3ca9-8ccf-7a986d194063 | -21.38917 | -44.27325 | 2024-10-07 03:17:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd04eeb1-a2dc-3968-9cbd-7a4749c6be13 | -21.14202 | -45.83235 | 2024-10-07 03:17:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 99b1a346-ac93-303e-956d-5abde68e32f3 | -20.63859 | -42.90718 | 2024-10-07 03:17:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b194e4b8-0927-342d-81a1-9a0629297356 | -20.63738 | -42.91234 | 2024-10-07 03:17:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d64d563b-5107-3600-ad1b-1ad89aec34b5 | -20.4974 | -42.29463 | 2024-10-07 03:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7cc55088-abaf-3833-a80d-2b4a0fa1c3a3 | -20.4964 | -42.29903 | 2024-10-07 03:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4127d3be-ee36-3496-b912-31360daeaf5c | -20.44999 | -43.10476 | 2024-10-07 03:17:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ff0dc83f-124c-31b3-b43a-268474207e20 | -20.44673 | -43.1016 | 2024-10-07 03:17:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46172539-11ba-322d-bd8c-1260642c6c07 | -20.4456 | -43.10646 | 2024-10-07 03:17:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49f6970e-5acf-34ed-aadf-392ab51e4009 | -20.42367 | -43.7538 | 2024-10-07 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30571e6a-20c6-3601-b69f-b7ffd4f05348 | -20.41707 | -43.75286 | 2024-10-07 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| eedd1338-411a-34ee-860f-d9c81d718095 | -20.41665 | -43.7543 | 2024-10-07 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 19e0d7a0-adfa-399f-8bcd-0a5d18fe2dd8 | -20.39154 | -43.91932 | 2024-10-07 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 22bedc04-34d6-3a95-9b00-f3b0551760c3 | -20.39094 | -43.91754 | 2024-10-07 03:17:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ffe223f7-46af-3caf-b867-23d4fb3782a7 | -20.34756 | -44.68683 | 2024-10-07 03:17:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b027186-5ee4-3946-98a8-1b5a19b26cd2 | -20.34077 | -44.68522 | 2024-10-07 03:17:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20544a1c-5c88-3c79-885d-a6262acae124 | -20.33907 | -44.69214 | 2024-10-07 03:17:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52b422a3-3bde-34e0-9216-b060c1050109 | -20.26151 | -42.92443 | 2024-10-07 03:17:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 90721116-fb66-3366-b652-9bdbbc463aed | -20.26046 | -42.92885 | 2024-10-07 03:17:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c699e08f-d6ad-3a4b-b085-c940baabf394 | -20.19621 | -41.83153 | 2024-10-07 03:17:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
