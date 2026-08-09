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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6052d7c3-21e3-3fc9-99df-abde02af73fb | -2.09016 | -54.44271 | 2026-08-09 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2af1dfb5-5721-32e8-8483-3af99372d1f3 | -4.459 | -47.91782 | 2026-08-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a5937c24-38fd-378a-ae1b-2b432285ef62 | -4.34792 | -55.13335 | 2026-08-09 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 690b2c92-2cbb-3d5c-a482-252d4e5a99e7 | -4.96113 | -62.34373 | 2026-08-09 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084a6417-b725-3c5d-a3b1-72583f7ac184 | -2.97897 | -51.68721 | 2026-08-09 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7db166a4-084e-3423-b86e-1fc27f39b878 | -4.26885 | -48.19129 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 109a8026-d90c-3824-9387-2448f6b518b2 | -5.03437 | -56.12181 | 2026-08-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5dbd87-ee0e-3d7d-9b1a-25049af924c4 | -5.72968 | -49.13549 | 2026-08-09 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2e202ee-e784-36d7-85a6-70aeff88a1d7 | -4.27559 | -48.56359 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| abe5c06e-3186-3d87-ba66-b1bddbfac976 | -1.83189 | -54.66377 | 2026-08-09 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8cfef63-6493-31ab-bb32-6248947354b5 | -4.26365 | -48.19052 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3f675f78-9b31-3b66-8141-82b7c505bb88 | -7.58865 | -45.20823 | 2026-08-09 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2dd5c16b-5e60-32a0-9b29-79af668a273d | -4.26839 | -48.19447 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6dd450a9-8fcd-3b8c-8a90-3924bace3c10 | -6.11702 | -55.76136 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89706a52-5f57-3a3d-a260-b5dbc876d6e2 | -5.88553 | -57.64638 | 2026-08-09 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 644f85ce-3cf2-3960-89e6-7028eee0e745 | -2.37944 | -48.22467 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9843d458-ce69-35b8-970d-9966b52ea290 | -3.07692 | -51.53508 | 2026-08-09 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 212032c4-3096-3511-b7b1-146fb7a691dd | -3.8203 | -50.63531 | 2026-08-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 455a3164-5731-3454-aab0-5bc92229602e | -4.28065 | -48.56449 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 933cd3e2-32fd-304d-9fb7-0a49594971b3 | -2.55961 | -48.42669 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9135a62-8adc-3246-ad50-fbf294493261 | -2.38006 | -48.2261 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1462b6e-b0be-3098-a7f3-7814f0f9b78e | -5.8883 | -57.65035 | 2026-08-09 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8194126e-9e19-3d8d-b269-8a2419ec6118 | -4.26931 | -48.18811 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a0d2409e-8b04-3b64-b70a-5788e9deac48 | -3.59122 | -53.30719 | 2026-08-09 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a703a84-7bbb-3a15-ba7d-a541a552c401 | -2.37917 | -48.23191 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e857ce7-89e5-3727-8121-6f8b7d96cf5a | -3.02824 | -54.52501 | 2026-08-09 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 042d74a4-e74d-3624-8da0-2c851332c083 | -4.28108 | -48.56149 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ca60d051-f17c-3826-b055-73a9dc3b3e63 | -2.37961 | -48.22902 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e9f0de4-9395-3384-8991-dcc6fa99e711 | -2.37901 | -48.22758 | 2026-08-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11372c50-6fb6-36a2-8947-47e578c3d0e0 | -5.73426 | -49.13913 | 2026-08-09 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f766003c-91f9-3ab3-95e0-31314492fcdf | -4.80476 | -56.13355 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c9c279-1a60-3dcd-b290-86d6ea0df3d2 | -4.96078 | -62.34369 | 2026-08-09 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21736010-6092-3809-bcba-b1b09183976e | -5.78676 | -57.18858 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b49db000-5e6a-37d4-8ab7-6088732ca6e6 | -6.10242 | -55.81108 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56d3829-825e-39b6-a608-0e7618d29070 | -4.26319 | -48.1937 | 2026-08-09 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f0321185-2db9-3b1e-8bde-d7e1760b85e5 | -1.83133 | -54.66741 | 2026-08-09 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c91177-0acb-3b01-9bcb-8b5f28ff1847 | -4.23193 | -55.57117 | 2026-08-09 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5611435-cb7d-3d7c-85f4-89656d81a077 | -4.22119 | -56.25721 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 496f23e7-d545-36be-b530-cbce18ba3632 | -5.88566 | -46.50323 | 2026-08-09 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f35db7d0-08e8-3426-ad32-bb9401d2e192 | -3.39915 | -49.77979 | 2026-08-09 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 024d2b0e-5a1d-3f24-bbcc-29ec07aab629 | -5.72887 | -49.14127 | 2026-08-09 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df524bb1-8985-311b-847c-b45f3b990df3 | -4.80142 | -56.13303 | 2026-08-09 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 998becc8-41b6-3dd9-b61f-ccba60cb81da | 0.96834 | -60.41138 | 2026-08-09 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eb61b92-185f-312c-9039-a5830fe32ccd | -4.45791 | -47.91672 | 2026-08-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 17d1500b-9f3c-3660-9598-66e3dd8a0624 | -3.82094 | -50.63103 | 2026-08-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b6e2272-eea7-35ba-ba64-37a18537420e | -4.10634 | -49.27395 | 2026-08-09 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef8a5f62-ef9d-3f4f-9c77-5933354c453f | -11.27204 | -44.87043 | 2026-08-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 094bd066-95a9-3bcd-b286-c94c541fe62c | -12.3487 | -53.15444 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2203f4d-e8ce-3bc8-b75c-f6b70a0295ca | -12.33201 | -53.15205 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 910592af-f9d6-320a-ac26-cb68eede700d | -8.62939 | -66.53466 | 2026-08-09 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 820939dc-ed43-304e-b8e5-d74fc2818a68 | -10.92521 | -57.1234 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0448fd88-32d7-30b6-b4cd-cd3e47927efd | -9.27167 | -60.89219 | 2026-08-09 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca51e102-d7bb-3875-b84c-66f2d4ab2fd7 | -10.249 | -45.81457 | 2026-08-09 05:12:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa71c77d-a06a-3231-80ff-c86e11434406 | -10.07672 | -60.50113 | 2026-08-09 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 184ed7ab-09ba-36a6-a7a6-7cb8a60a6308 | -12.34924 | -53.15057 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92ab7b74-887b-350d-a8ea-5f90dec633d8 | -8.67823 | -62.86999 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d874638-6bec-30e4-b3ee-65cac743b7db | -11.19503 | -54.83547 | 2026-08-09 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d210c76-2cd6-3cd6-b34a-283f6958d878 | -10.9224 | -57.11924 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60baf011-fd90-3652-96d7-4ea51f3f4e1c | -12.34453 | -53.15384 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a213a94-6a89-3515-84cc-638d715e31fa | -12.61421 | -52.46392 | 2026-08-09 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91f90d2f-c08a-39d8-a119-1ed09b55f69d | -8.51402 | -63.35979 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92c78daf-5798-3bc2-914d-55ae1e9d082c | -9.33557 | -63.45133 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78abeaf2-3c06-3c67-a027-2cf26014562d | -12.34817 | -53.15831 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3d08a0-bb68-3bf5-bdbe-366cfddc146d | -8.17327 | -61.51772 | 2026-08-09 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64615221-e0f6-3c72-8f77-79c033380a3d | -11.25313 | -54.03335 | 2026-08-09 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11ccce19-a75b-3100-a838-83e9a9905c03 | -12.35412 | -53.15749 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9f714e-528d-3ac2-998b-bfdb6c4c96dc | -8.15106 | -64.09145 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78df2b84-775c-373b-a570-24f4487c1f90 | -8.33584 | -64.01839 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360770ef-1219-3bfa-8ab6-e7b1ccacd4a4 | -12.3531 | -53.16523 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d208013-db9a-36c5-bef4-fb804c88e832 | -8.92123 | -64.29972 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9261716e-792a-3c58-96d8-52d2aaa88f47 | -8.6856 | -62.87479 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d600235-c361-3270-90c7-ce565082b570 | -11.84183 | -56.94333 | 2026-08-09 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d09f1792-dad5-3770-b615-939d3f731147 | -8.67763 | -62.87346 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ecf96b9-1c22-3ca3-b40c-83e3713b2ccb | -12.34944 | -53.16076 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c523dca-92b6-338c-b0a5-ecf548527061 | -10.92185 | -57.12288 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d6bec8b-da6b-3151-9bb3-cabbf19ee722 | -11.99704 | -60.51044 | 2026-08-09 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba9230a2-2527-3997-9eca-408252394d1f | -10.25543 | -45.81682 | 2026-08-09 05:12:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e397293-6398-31be-a8cc-59fba311d087 | -10.91903 | -57.11872 | 2026-08-09 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a452a842-335b-3445-9c19-2b313513490c | -8.67883 | -62.86653 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45a7b063-c4dc-3ec2-a395-2bb0d23d87c9 | -8.67562 | -62.87206 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| de7fd9c5-7a2d-3baf-a6a1-8d7265c932c9 | -12.35463 | -53.15362 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1da9950-b07c-3ddb-bab6-19d3b86ff960 | -9.33146 | -63.4507 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c76f9d0-b02e-3668-b764-134143ce17b6 | -11.25242 | -54.03167 | 2026-08-09 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9b0bd17-9bfe-3a2c-8bba-e4dc951311e3 | -8.6868 | -62.86786 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a93a920c-2476-3645-815d-e4168d2f8312 | -12.32784 | -53.15145 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 27a10e28-3718-3532-aebc-bc9b6bae9de3 | -11.24852 | -54.03115 | 2026-08-09 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11d4020d-613a-3c08-a65a-73f86ee733a1 | -8.15201 | -64.09151 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49032961-52de-3158-ac38-ca023fb27eee | -11.62644 | -51.09124 | 2026-08-09 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 57eaf4d9-a7c2-3c0c-a5a2-65aebc7d5433 | -11.84467 | -56.94757 | 2026-08-09 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05dac4fd-a461-3260-b3d8-aa64b25522b2 | -9.06152 | -60.39766 | 2026-08-09 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 620cc317-0405-32f8-87fd-8bb721cc9369 | -11.28491 | -53.94667 | 2026-08-09 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cadbdcb-34fb-3761-bf75-7048dfdc8ef5 | -12.35045 | -53.15301 | 2026-08-09 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c079095-79c0-3cdd-87b0-fab4027fb88f | -11.19438 | -54.83996 | 2026-08-09 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7b5b465-2384-3473-ad93-62aa7dc93650 | -8.16883 | -61.52153 | 2026-08-09 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98d84ed6-21e3-375f-9156-eb3ba90724da | -8.63448 | -66.53555 | 2026-08-09 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8680cc5-a40e-3d7d-a4c4-56006c3fab1b | -11.19808 | -54.84053 | 2026-08-09 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6ef42e-0a94-3631-bf30-acc999d27227 | -8.69078 | -62.86853 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98de070a-fb87-3311-af3e-910fb69ed345 | -8.68019 | -62.86924 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efea172d-580a-3b33-b0b7-bd166da1353b | -8.15636 | -64.09225 | 2026-08-09 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32bdfbe1-b6c2-3321-9c27-efc73f49e961 | -8.68221 | -62.87065 | 2026-08-09 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
