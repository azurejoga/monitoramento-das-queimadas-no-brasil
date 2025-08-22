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
| d8e4daf2-b67e-3348-95c8-7b7950a4fa53 | -8.87206 | -62.4141 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56546590-ca92-37a3-acb5-0283628e7dfa | -8.86599 | -62.4032 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6395926-1271-3b77-9fbd-8e778ab3377e | -9.23637 | -61.01952 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb7140d-59ae-3ec1-aedc-2619ec7a88e9 | -9.5244 | -60.54039 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4dae2bcd-a146-3cec-a9f7-879130f67954 | -9.21579 | -60.79059 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5bb760e6-ccd0-33db-a389-c6f01508a0cb | -12.93158 | -46.18884 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a295a8a1-2e7c-3790-80fd-94f26d11b073 | -13.15137 | -46.90977 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 54a80578-8b05-3920-ba06-9764e06c3c12 | -9.21229 | -60.78998 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd879457-8e52-32dc-9807-cb0dcbfb467b | -8.87814 | -62.42498 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19aeb4e2-4077-32af-b00f-c3dea4377941 | -9.88761 | -60.29097 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cdce946-7eba-368c-9c5d-0ea8186fd376 | -9.52031 | -60.54366 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a52afcff-0de6-34dc-9263-cd1b17407826 | -6.63087 | -58.54276 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 555b172d-b528-3003-892b-7d233f4cb5da | -8.61206 | -62.62047 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cadec70b-1ad9-32a7-bd12-bd6a75e00809 | -10.86455 | -50.81739 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7031c639-2491-37fc-8655-e2012372d1a9 | -9.1855 | -59.63636 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06f2b95b-0ce1-31d1-9dad-11b978a5e797 | -9.21213 | -59.47042 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2530226-fa4a-36d3-bfaa-1804cd11ca11 | -11.35744 | -55.38921 | 2025-08-22 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f00577c-d6b2-3f8c-915b-3f12c5bf0549 | -8.58092 | -48.55107 | 2025-08-22 05:12:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25e9e0ff-e94f-36d7-ac92-570fbf6e39ef | -13.65314 | -45.71328 | 2025-08-22 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 836699e8-af23-3ac9-a10d-14de5f5868e6 | -12.99387 | -45.24295 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cbf6566f-c4a6-3c8f-8fc0-f09092cd151d | -11.73158 | -49.10521 | 2025-08-22 05:12:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3da66e8-062c-3674-b8e8-8d8cfc2c0a58 | -9.75267 | -62.7663 | 2025-08-22 05:12:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f83e41a0-d922-3575-a191-c7794af5246e | -9.21386 | -59.45964 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5261a8e4-15c8-30ca-b00e-d9e24551cef9 | -9.58816 | -55.35041 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6cc7b0a-58d0-3055-8584-53590cf00b2e | -9.52502 | -60.53653 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72a2b299-4ae8-3b2b-8287-f3cb5856bdda | -7.77768 | -66.95709 | 2025-08-22 05:12:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f096b1fa-5c16-3fa7-964c-ae8843cfe6bb | -8.86376 | -62.39294 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b1ed21b-4290-3a7a-a914-75dec06813a6 | -9.8848 | -60.28665 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aab7932a-43eb-34b4-9767-e77dba7e42d7 | -13.38022 | -47.50103 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0bc850b-667c-3af4-925a-ab68431efa8e | -9.20935 | -59.46628 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b28f10e3-bf9b-3e81-bcb0-f3b02597ad6d | -9.65351 | -59.64943 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e55cf898-c386-3735-960c-9b740e343f5b | -8.87589 | -62.41475 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d411d1f6-539f-3578-b1dc-8b36ffb78082 | -9.18945 | -59.63326 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 386b6e4d-9dff-38ad-bb35-95bae1a5fa2a | -6.63149 | -58.40988 | 2025-08-22 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92787b5a-3d9d-3a8b-a852-edd03f7489e3 | -7.84401 | -61.72624 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94c2050c-a2a5-3c47-bdff-48d8798925b5 | -9.22541 | -59.75474 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f45d78-9730-31c7-82bb-f232df81558d | -7.45354 | -59.94383 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afd6503e-9c6c-3592-a52f-77e69d35f961 | -9.17045 | -59.7084 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c8c176fa-012f-34b4-8cfb-5ff0f7358fa5 | -9.94555 | -60.17368 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9604d834-654b-392a-af4b-d1945029d6b1 | -9.16878 | -59.6114 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b06ad684-6949-3c6a-b5a6-46968d35159a | -9.20748 | -60.79729 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3b00c08-dd33-348c-b13c-953bc411a847 | -8.83869 | -52.03185 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 878a9295-ca19-3e72-8e46-46fd3edc6879 | -13.03697 | -45.17048 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df1862fb-2255-3640-855a-73996bfdf00c | -9.50391 | -60.51332 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fce18afd-be09-3848-93da-418e07e94e6e | -12.98751 | -45.23506 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b224dd4-1f28-3d5a-93be-758f17ba56d5 | -8.87126 | -62.41888 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8ca98e0-21a9-307b-9243-327560fb4d6e | -8.60816 | -62.61983 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c628d59c-9e3c-3dde-9743-93defd264670 | -7.05266 | -59.83408 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 687513df-dd14-3fdb-898d-8983c0df1406 | -12.92889 | -46.17759 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31c82dfe-8239-320c-84cf-e7eaec04dea3 | -9.31417 | -57.01719 | 2025-08-22 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8ed496a-d3b5-314f-acf6-404b37ec9381 | -9.1945 | -60.7668 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 899c0d93-6ca4-38ec-9804-09e26704f405 | -9.2105 | -59.45911 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fd29705-25c0-3454-8329-284b3e1823d8 | -12.99701 | -56.88622 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddd275a9-4c03-3951-8e53-423608d8e2bf | -13.14843 | -54.91955 | 2025-08-22 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea11fa0-1f9d-3273-a14d-8a93be2d039c | -9.15764 | -59.59475 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a2b67c5-b8f4-3ca8-92a7-fb33a8fdcbe2 | -13.37606 | -47.49073 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f70f56a-1c0c-36a2-9a08-30d52d136350 | -12.49297 | -53.81474 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6993f0b3-22ad-392b-9ff2-d57fb1428e38 | -9.6586 | -59.63913 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 620457a0-5323-3a75-98c3-4270f24585e0 | -8.54956 | -66.93703 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28c85e0a-8a31-36f2-a40a-a172855e5635 | -13.02958 | -46.31998 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e408208b-9b19-3583-8d7c-c3370c64651c | -7.2964 | -59.63116 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0035cfb-174b-3a34-bcdd-c18952bbb339 | -7.54849 | -63.85173 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0dd6870-16c9-3511-b7c1-41f55b582bb7 | -8.90779 | -47.33171 | 2025-08-22 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c001fad-16d1-3bea-ae5b-b206a3acc06d | -9.19504 | -59.64151 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce1e8c7-05db-333d-a0a9-bf7403fcb428 | -9.65409 | -63.48615 | 2025-08-22 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14783c10-20fe-32ab-b69e-451073277da3 | -11.03568 | -59.1735 | 2025-08-22 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3700e2d-59f5-32c2-810e-4f28b10a592c | -13.1522 | -46.90201 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a5ef35b9-866d-305d-99e9-f4c556f177a0 | -9.65803 | -59.64274 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89557a3d-8935-33a1-a4e6-9853d1aa6c15 | -9.27448 | -60.78399 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d87536cc-377d-31b6-9580-32dc8389ac00 | -9.15647 | -59.60199 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67eb6e8e-20b3-34b1-9981-664ddfc4696f | -8.55242 | -66.95069 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1c96dcd-ef69-30aa-a4ac-479ae824c871 | -10.11087 | -57.75824 | 2025-08-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f4b4512-212c-3f0a-8fea-d529ec665a4e | -8.28905 | -47.27026 | 2025-08-22 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbb1d09c-3984-370e-b1cb-91ff5b199865 | -13.33636 | -54.39505 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df10e3c5-c1eb-38d2-a283-e5b7d816fb83 | -12.49701 | -53.81534 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1320446c-2579-3c1e-9af6-ba4848d037c7 | -7.30384 | -59.62851 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bde37401-ab98-3f54-801c-05b6f10b8b47 | -13.02783 | -46.33643 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a08c15cd-60fe-3065-9f8f-d0e98e258b4e | -13.15 | -46.90988 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0bd468c-14fe-3408-b062-8338493ebe5a | -9.81787 | -64.27589 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9624e235-2a17-3579-a50b-944537c48539 | -9.95175 | -60.17852 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa9baaaa-2f58-3d45-afc2-c4701133a4be | -9.20207 | -59.46878 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ac0969-b7be-3441-91a9-eea656adb7b7 | -12.98666 | -56.88466 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a2c4ac-022a-34f2-8769-5f6ebefdd02a | -12.48894 | -53.81414 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c497e88-8813-3270-a44c-85bf2fae12b3 | -8.54663 | -66.95295 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a793c6fa-92bb-3461-89c2-0723622b2566 | -8.88118 | -62.43042 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5893303b-8e79-3bec-ad69-66b68f4eed31 | -8.8541 | -52.04716 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 324d6438-f514-325d-a5d7-26ddf5d3375d | -7.84103 | -61.72113 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b99d966f-9695-385d-b08f-1a3b512e7e86 | -9.95115 | -60.18222 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 835b14c3-a4b8-3a25-951b-d15d36b4d819 | -9.19003 | -59.62965 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64d294cb-998b-38ed-b24b-1bd4d86cb94d | -10.85973 | -50.81672 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f4f84d37-f91f-3408-8573-16b73cc0ffd3 | -6.31326 | -59.89069 | 2025-08-22 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52f258f-b8f0-38e1-bf55-234223587d9f | -13.14617 | -46.89764 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40f5e596-d5c1-3162-b669-518481e5464f | -12.58465 | -47.09395 | 2025-08-22 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c12d969d-ddb2-3433-a006-3e9c995da3f0 | -13.10625 | -51.90738 | 2025-08-22 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 196abded-ecad-3be5-9460-a00a3679cbea | -8.8743 | -62.42432 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73a21f33-bfa7-390f-9bad-8bddc785ef07 | -8.1261 | -47.14843 | 2025-08-22 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffe59391-72cb-3bfd-9f05-eefc292e58b1 | -10.86366 | -50.81925 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 85a03c9c-049b-307c-a800-4ad3a649b7aa | -9.1818 | -59.5949 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 513d60db-7dda-3e16-9ae0-719899fe4257 | -13.14463 | -54.91897 | 2025-08-22 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bf25216-2f7b-31c8-899b-302211fd06dc | -8.87445 | -62.39973 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
