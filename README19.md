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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e5d5a61-74a8-3897-8034-f0639c2c0785 | -18.70027 | -43.3927 | 2025-09-13 03:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6d5941d4-ccf3-3366-bd86-2fd362d8d1e2 | -16.8535 | -41.53799 | 2025-09-13 03:19:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4333d7bf-2c7a-396b-af9e-105572fe531d | -12.40025 | -43.81975 | 2025-09-13 03:19:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f97497d-1489-36b0-82bf-6a94d442658b | -17.34853 | -42.63583 | 2025-09-13 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 578af31a-91e7-3ec6-b294-8d2fb247ffc6 | -17.46735 | -43.72695 | 2025-09-13 03:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72d41c23-838a-35fa-b376-d20423d0b74e | -18.05701 | -45.46006 | 2025-09-13 03:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba563c12-8360-3c86-9076-b0fa5281610c | -18.4363 | -45.93238 | 2025-09-13 03:19:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86420b31-acc7-31d7-8463-a212a1a0e4c8 | -12.39398 | -43.82207 | 2025-09-13 03:19:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8d4d804-09eb-3906-b0fe-16350402cb85 | -16.65787 | -40.84253 | 2025-09-13 03:19:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c4f5eac-d6ba-34d4-8e04-cb39b1a9760f | -11.73683 | -44.20966 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2e0b05e-f8ae-3ee2-8618-52bc4ac7fa4f | -14.70234 | -45.15376 | 2025-09-13 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42ec56aa-6df1-31c9-995b-2be10f513213 | -11.73097 | -44.215 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ba017cd-1acf-31b5-a92c-84c7a2093483 | -15.23704 | -44.06374 | 2025-09-13 03:19:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ac4b910-04e3-3191-ad8d-1a3769b06954 | -17.94724 | -42.52507 | 2025-09-13 03:19:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e972620c-b4b8-3ea7-a7e7-b95e1fbbbdd5 | -18.47307 | -39.766 | 2025-09-13 03:19:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| f3ecdb38-2333-3f88-8df1-578f7f526403 | -17.28047 | -46.11376 | 2025-09-13 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c239334e-b80e-39a0-a8eb-3de6cfcc31f6 | -17.55025 | -44.55183 | 2025-09-13 03:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b8007fe-327e-3f01-9369-cef8a544f1f6 | -17.28555 | -46.10706 | 2025-09-13 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f1c3b1dd-2a17-325d-9636-7580041d5aa4 | -15.83588 | -42.59919 | 2025-09-13 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0404a903-a938-3bfa-9e28-27b6adfbf435 | -16.3703 | -41.38387 | 2025-09-13 03:19:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5cc0256f-97b0-3777-b8e6-9836aefdd829 | -14.70388 | -45.1469 | 2025-09-13 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b47bfc2-5d74-3093-9621-f3197d3c7b92 | -12.65628 | -44.2393 | 2025-09-13 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cccfdcfd-63b7-3775-85dc-c23b23563bfd | -17.36278 | -42.70656 | 2025-09-13 03:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3a6bac02-73ec-3e6d-b34d-daca0eb3f2cd | -17.4685 | -43.72186 | 2025-09-13 03:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ad48504-56ea-3809-a0a3-5d8869575f13 | -18.06331 | -45.45435 | 2025-09-13 03:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1850430a-64c5-38eb-acb4-597c3785ad3c | -16.6537 | -44.92847 | 2025-09-13 03:19:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ab472b4-08be-3615-beb8-91d593e8248a | -17.95131 | -42.52863 | 2025-09-13 03:19:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6f230352-931f-3a09-b649-42793855f153 | -14.69692 | -45.14505 | 2025-09-13 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58028784-f30c-32e3-b0e2-016cb61d1c81 | -9.2843 | -59.418 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b37d94e5-3030-30ec-b643-45a5b33ad364 | -11.8281 | -50.562 | 2025-09-13 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| bba1c9d2-587c-3d38-b79c-489503bc2d14 | -12.8263 | -47.9263 | 2025-09-13 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5d8424a1-26d7-3c58-b5cf-f5f3ca14ec9a | -9.5322 | -54.648 | 2025-09-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0b4da4c7-6fc6-3232-b57b-6c8f329dce08 | -9.2658 | -59.3997 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 1f2d0a1a-112a-3670-8fee-f5a98ebad6b7 | -9.5004 | -55.9788 | 2025-09-13 03:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1fba9ae9-a96d-3330-8e66-dfc84f40d1d9 | -10.7667 | -50.5086 | 2025-09-13 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| eaca815e-345e-3493-a74f-95fbeae49284 | -10.7664 | -50.5299 | 2025-09-13 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 1d4218f9-b66d-3ccd-ab0f-7324dbeb027a | -15.2229 | -56.6782 | 2025-09-13 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 59128dd7-e7ef-33f0-ac27-808f0e5a9343 | -15.2036 | -56.6803 | 2025-09-13 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d3fd1fa4-15dd-30f4-8e84-eb1957c9a904 | -9.247 | -59.4201 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 82759945-dd9a-33db-9892-dedfe9ef9a3f | -9.5135 | -54.6494 | 2025-09-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 29be3ca1-70df-32f4-bd02-f2cee22bda31 | -16.3418 | -51.5434 | 2025-09-13 03:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 75c468e1-fca7-3fb0-9f2b-7dc895c02f65 | -8.1004 | -50.1821 | 2025-09-13 03:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 11ac9da1-9b96-3eb6-b4b9-9920a5e7abb2 | -16.1001 | -49.9457 | 2025-09-13 03:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 6e9ab23b-b4da-3385-b57a-3c5bc3d2f53c | -9.5324 | -54.6277 | 2025-09-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 270.2 |
| 46e43a2b-0133-3472-a71c-4aa61996ceee | -9.5137 | -54.6292 | 2025-09-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 402.7 |
| 564a2132-9966-36df-87d5-6c018066c1e2 | -9.5326 | -54.6075 | 2025-09-13 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 14d41756-d4cf-37a0-a87e-dc213ee699e8 | -9.2472 | -59.4007 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 72902f0a-3cf9-3059-868f-c8841ec7c082 | -11.8468 | -50.5813 | 2025-09-13 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 89b212be-28de-35c6-bee7-e0021b258163 | -10.7477 | -50.5106 | 2025-09-13 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| dbdfec50-5723-31cf-8dd0-74d45778e58c | -10.785 | -50.5493 | 2025-09-13 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b38a8a51-4739-36b9-9bf0-654e0f307df1 | -9.5139 | -54.6089 | 2025-09-13 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 6aa6d0e2-d04f-399c-b130-a77c705ce251 | -10.7853 | -50.5279 | 2025-09-13 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d3e6e28c-14af-372d-8ec2-f3cd17942209 | -16.0805 | -49.9489 | 2025-09-13 03:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3718c319-b62d-3ddb-9c52-9de68de84f37 | -12.006 | -47.7505 | 2025-09-13 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| f68fe732-dfbd-33de-8b79-f9589f07ab7f | -11.8472 | -50.5598 | 2025-09-13 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| a0222543-f5fa-3dfc-8c11-0677876d241f | -11.8659 | -50.5791 | 2025-09-13 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 78e598f0-7483-389f-a503-4f7dd8d552a4 | -15.1165 | -52.4918 | 2025-09-13 03:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f8633f37-02cb-3c15-8559-125d9f8264d4 | -9.2656 | -59.4191 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 25079b49-3612-37d7-8e6b-fd7597cdab37 | -9.2844 | -59.3986 | 2025-09-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 77c355d6-3581-3d60-973a-b651632b1433 | -9.5006 | -55.9588 | 2025-09-13 03:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 812703bc-b3a3-3832-801a-4cc387b1c256 | -16.0997 | -49.9677 | 2025-09-13 03:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 35.4 |
| bd8d3408-89eb-3111-8d9e-645ee037893c | -21.6187 | -46.8115 | 2025-09-13 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 0ac99ec3-e177-3467-bd87-ca3978750bc0 | -20.33535 | -46.67074 | 2025-09-13 03:21:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8635db76-e835-330b-910c-80877772dc65 | -20.10437 | -46.92672 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96856ca2-85f6-3d22-ad0f-d028725c37aa | -20.29004 | -46.58895 | 2025-09-13 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b35bf998-cfde-3f5d-b86f-a15e3a840583 | -19.98669 | -46.90299 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed45591b-43e9-30aa-948c-e0a0e6d760f0 | -19.32908 | -45.1118 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ae85ca0e-5054-3340-b2b0-7844802e3ad3 | -20.28966 | -46.59193 | 2025-09-13 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15236bfb-d42c-3b1f-85b6-fa38d497e445 | -19.98939 | -46.90346 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6730ca73-b6ec-35d3-b804-b8e22694071d | -20.44976 | -46.44289 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5098b1c3-443a-3b31-8fd9-797accbbb880 | -20.25792 | -44.18748 | 2025-09-13 03:21:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 080b681e-2c7d-3281-8dad-90f1e7fec326 | -20.2879 | -46.59916 | 2025-09-13 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8c7a3a-5f92-32fe-8e28-eb91ad69dbef | -19.33414 | -45.11932 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6541bbc5-6287-36c4-8f08-3f23ec30257d | -20.28828 | -46.59601 | 2025-09-13 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1f376d3-ff7c-3f9b-868c-262ae207d6da | -21.62501 | -46.80191 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9a3caa98-d2b7-3725-82b8-3461f965e17a | -19.32798 | -45.11615 | 2025-09-13 03:21:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a3d8b74-2c05-3f4c-aaed-5a54961ee590 | -20.09347 | -46.91098 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea544ea8-778e-3444-a316-9b40fed874b0 | -20.44538 | -46.45631 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 74635b7b-9ce4-37af-a714-aadd48f5f362 | -19.64269 | -45.07804 | 2025-09-13 03:21:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 13aa28a6-d06a-3378-a748-5c1a0b8494f1 | -20.59683 | -44.90681 | 2025-09-13 03:21:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6b6326e7-a31f-3e59-be56-c1320c41700b | -21.94636 | -44.85163 | 2025-09-13 03:21:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 08b396c3-b558-3c7e-88c5-152b0b4a3eb9 | -19.63209 | -43.73423 | 2025-09-13 03:21:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e9961b5-d536-3818-a5f1-c2630849b602 | -21.62081 | -46.81285 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| f3b217c5-7384-31f0-974b-6454dc18aeb5 | -21.6135 | -46.81338 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2b9dd6f6-cc0d-3630-b0cf-c7bf2a292bd4 | -20.45783 | -46.43933 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3dfe83d-d7b2-345c-8472-470026fd71a6 | -21.63057 | -46.80244 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 47f0b195-563d-3479-9348-c9156c642455 | -20.55781 | -41.01825 | 2025-09-13 03:21:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f29aca28-e0d1-3562-be1a-f3471f3f93b9 | -20.59346 | -44.90465 | 2025-09-13 03:21:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 97d5ba57-d21c-375e-82ed-2e2d0f522357 | -21.6189 | -46.82056 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| f8046119-4452-300e-a305-e88a72f36e19 | -19.98053 | -46.90932 | 2025-09-13 03:21:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc3dead6-b987-3a58-b475-597e442d2942 | -20.44656 | -46.45583 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4fef7911-35de-36fa-996f-a31fa2a18857 | -20.09875 | -46.91951 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36899b77-ec9f-35d1-bcdf-ba1a01e89531 | -20.39095 | -45.54056 | 2025-09-13 03:21:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab2c2e9d-f3fb-34d0-93c1-bb44e96c9c0e | -21.32181 | -44.99683 | 2025-09-13 03:21:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 00511158-4f00-3691-b024-8145806b3776 | -20.44719 | -46.44879 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40e2c3fa-a44f-3322-a499-37b915166b15 | -21.32009 | -44.99628 | 2025-09-13 03:21:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cbe4f384-d355-3fe0-97db-6a8eb1705ae7 | -20.08004 | -46.94621 | 2025-09-13 03:21:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 065edecc-7d4c-336e-98d0-473723e3d422 | -20.45111 | -46.43743 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5629eed5-010c-308c-a125-a5515494774e | -20.59589 | -44.91078 | 2025-09-13 03:21:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6c8a000c-c779-3ad7-81a4-0091df535c7b | -20.45663 | -46.4394 | 2025-09-13 03:21:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README20.md)
