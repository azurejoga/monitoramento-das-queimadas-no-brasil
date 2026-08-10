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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a84dd413-df36-37e3-bf72-be40a349b06f | -6.83173 | -56.43172 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b31deeb1-bd4d-36a0-9650-6984eb98b77a | -4.45329 | -47.91846 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5d92b10e-4c97-3a8b-88c2-0d1426c1f21e | -2.65623 | -54.62483 | 2026-08-10 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59871970-043a-3160-9536-d0e9dd7b7589 | -6.81324 | -56.42864 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07124df6-5e32-3adf-92e3-ab3e3f66c3eb | -6.84924 | -56.41023 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df513f6a-71ae-3e8e-b784-1b797a440338 | -8.64459 | -45.85996 | 2026-08-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b79d36cc-b084-3f6e-bdc8-d295f72c9866 | -6.83888 | -56.40411 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2652f58-95e3-308f-8dc4-169c5154142d | -11.04796 | -44.28517 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f829a336-8a00-3248-a2f1-5de2064481ad | -7.54821 | -55.56023 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33b12afa-f86e-358b-b12a-0841820d3111 | -8.29911 | -55.11161 | 2026-08-10 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca3f6d1c-1c03-3225-9e0f-fa86b9069d07 | -4.45535 | -47.91698 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8c9732b1-c265-3e25-82dc-66ab79102e64 | -10.24973 | -45.91887 | 2026-08-10 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 11fcc1ef-b614-3a84-abd5-44e9fc63fca3 | -7.69639 | -55.16656 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca7f029f-7367-3e8e-892e-585b9a71ae61 | -6.70792 | -58.95383 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff6a6c9-fd43-3821-a100-6efe53f1a33a | -6.418 | -55.7921 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60edd87-1dd3-3df6-9afc-799faae2e3d9 | -6.14373 | -57.72215 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dca6cd1b-ff93-3786-a469-ceb94e58149b | -6.8249 | -56.44239 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c3fae7-7c24-3417-9cef-0e342bb0ce86 | -8.16663 | -61.51865 | 2026-08-10 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f77af47f-f608-3ceb-b871-f46bfdb153a5 | -7.55332 | -55.57317 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ce3a9aa-d573-39be-8350-98e198b73692 | -4.86359 | -55.81882 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2934a9d5-caa1-3395-9029-77648f18bcc1 | -7.48976 | -43.82062 | 2026-08-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27e88f51-ca7e-3e4a-9401-a46f1eef02bf | -3.93665 | -59.12822 | 2026-08-10 04:51:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae34a6a1-0187-3bc7-8e2f-6190b34a1750 | -6.84036 | -56.40155 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d442b292-0630-3b2b-aad6-b6791406edcd | -6.83377 | -56.43479 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56131401-3c3a-3d74-ac26-6dccf099bf48 | -6.15797 | -57.91285 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ce6298b-2d61-3fa2-acad-129afbb6a253 | -7.56864 | -55.56762 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35c5039e-adb1-3fe9-87c7-e45ccf03f346 | -6.8259 | -56.44431 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3dc240b-632c-3489-a871-bae8ffa91e63 | -6.60231 | -56.36491 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74e1b7c8-15bd-3502-bd51-f7e3be41ac2d | -7.11974 | -40.40005 | 2026-08-10 04:51:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4ecda4d1-b3d3-308d-9141-dd6472adf14d | -4.86445 | -55.81601 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 124cddcc-d1f5-3d6f-b16f-e93f812fba72 | -6.09826 | -57.69635 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b49e174d-3842-3c5a-bc66-0a185b59c678 | -7.15961 | -43.26634 | 2026-08-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df4cc15c-d7f1-3c31-9f13-1a0bf4c4ec6e | -9.77406 | -48.19746 | 2026-08-10 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6f8a01b-b446-35a2-9da5-cf335c058ef1 | -7.69293 | -55.16602 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3106031-0126-335e-9e22-24349f98c8aa | -7.53925 | -55.57095 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f2993b3-1ea6-336e-8f77-96154fd1e420 | -5.79773 | -51.88302 | 2026-08-10 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 144eb6bd-5442-31e8-bf38-0c6ee6bb37b6 | -8.64188 | -45.86056 | 2026-08-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d67ecd91-b90b-3c95-89da-b2bccdbcf532 | -6.10229 | -57.69698 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76cc2fd6-84ae-3ec1-b71f-0f5b8eb13a79 | -7.11389 | -40.40569 | 2026-08-10 04:51:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 65c571b8-7ba8-37f5-b1e5-b2b52ee89002 | -6.14836 | -57.71924 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 662ca07d-debf-3aa3-bddb-3f8252dd0375 | -6.82944 | -56.42229 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5827324d-825a-3ff9-9e7c-f9f3d7278187 | -6.84555 | -56.40963 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0e75701-2514-3c85-b16a-6e1002d43689 | -7.61507 | -42.76189 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2e7e4279-72e7-35b0-acff-d80fc35b0988 | -6.82432 | -56.43055 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61ee9ee1-8f7f-35da-b6a3-b516e275c333 | -6.87287 | -56.63781 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16ecd08-577c-3322-9260-559b7c74c7b1 | -2.08963 | -54.44663 | 2026-08-10 04:51:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53aa06c-db86-3627-8a61-a7f0bd5e18e7 | -5.72927 | -49.13445 | 2026-08-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56b10526-c227-35c3-b1c3-b8a01d599596 | -3.93126 | -59.13222 | 2026-08-10 04:51:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4a72ba0-e208-36a2-8621-75a2ea38c587 | -2.96312 | -49.19196 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86b442d-d73c-3d7e-b17c-533a5efeb7db | -2.96198 | -49.19702 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76bbaa80-ef18-37f1-a3a8-217e57340f48 | -3.39653 | -49.22212 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04370f5d-2ce1-31bc-bbe9-8049e7261824 | -6.83455 | -56.4141 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce6cab93-15dc-3dae-ad28-6bc2d8f91ab8 | -7.11465 | -40.39996 | 2026-08-10 04:51:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b91cb1d9-d940-3a0e-ba10-2796d146eaef | -2.90492 | -54.1521 | 2026-08-10 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf834278-57b6-34d8-9bb8-edd58cae84b5 | -6.46437 | -47.84705 | 2026-08-10 04:51:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52b47394-3629-3fb3-8dc2-425c07d59f77 | -3.3929 | -49.22232 | 2026-08-10 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e230b3fd-3091-3574-adda-ac2ca9b05d76 | -6.46339 | -47.85379 | 2026-08-10 04:51:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8772fa7f-dddd-3d08-847b-6870879c647f | -4.39993 | -54.78935 | 2026-08-10 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 854e3ae6-0c4b-3bfb-865a-986e9b3c0cf3 | -6.84337 | -56.42275 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6205da94-ae38-38d8-9d4a-a88dec7562ad | -6.82861 | -56.44297 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5191f5-b77b-3fec-9a86-78623b115334 | -7.54277 | -55.57149 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49740de6-470c-3a0a-9560-6cdbbc21d287 | -5.03143 | -56.12144 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74870c26-1430-3398-bbe8-51bcb00c031e | -6.83747 | -56.43536 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a33ff813-b170-30af-a0aa-16b99259ed4f | -5.69056 | -60.23053 | 2026-08-10 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 735239c5-d739-3496-9517-cd9a932a0d7b | -6.16614 | -57.91422 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60d23661-a70e-3e10-9bd8-ee66ed6e7b14 | -6.87661 | -56.63843 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea7a37e5-b6c2-343a-a7bc-d9fb88036c09 | -7.69084 | -55.16237 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 345df2be-733b-3699-aef8-f2fed7daa7b5 | -6.81394 | -56.42429 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51227c10-101c-39c2-b506-a0faac6ba5cc | -6.65295 | -49.6133 | 2026-08-10 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d24f021-1d62-32b1-a330-a383284238d5 | -7.55108 | -55.56473 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 02dfbea1-1c15-301c-9ba9-3868dc2ced50 | -10.24948 | -45.91975 | 2026-08-10 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ffdac9f-c1be-379d-bf08-4a10e7488921 | -6.83525 | -56.40973 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c3d1185-9b1d-3704-9e2b-bce8946ef277 | -6.8404 | -56.41777 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de5a7cdd-0605-364c-ab14-e4ea0949afcf | -10.25015 | -45.91451 | 2026-08-10 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49b085b8-2a21-3b67-a657-30a25f1ccb01 | -2.51097 | -51.828 | 2026-08-10 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68a7a3d9-14d7-3ea2-8680-cd347ae271a9 | -8.02441 | -55.11794 | 2026-08-10 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cd63e49-6a08-3fb0-98c3-8c84f776ab1a | -4.45784 | -47.91425 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4feecb25-0434-3804-9910-5ff8be4df028 | -6.41867 | -55.78799 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3efe2696-4087-3f92-9367-0237a9a4c248 | -7.69355 | -55.16221 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4bece5-00be-33fb-9c94-92176d824c63 | -7.31538 | -55.11446 | 2026-08-10 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 673762ac-eb81-3bd6-9cf6-d138b4ead273 | -6.1449 | -57.71506 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b89c79ed-5655-33dc-a72a-fb72be008d1c | -2.65685 | -54.62086 | 2026-08-10 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 014d1e07-e54a-38ce-b8b8-194342811d21 | -6.16553 | -57.91782 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f79de37-7024-3a65-813b-544eee16cc0e | -3.96161 | -48.13018 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d74d043d-f380-3dfb-a3c0-1eb2eae08e49 | -4.30313 | -59.47161 | 2026-08-10 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a9cf978-aece-3f8e-af3e-680885689081 | -6.82787 | -56.44735 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8603c29-7465-322a-97ae-38c0c81cf862 | -6.80953 | -56.42805 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b64f445-38a4-3ff4-b07a-0e71315e4157 | -2.97855 | -51.68658 | 2026-08-10 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 906cce48-e3b7-3403-a07a-098a805bdc64 | -2.90551 | -54.1483 | 2026-08-10 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aacfe9a9-bd15-31d2-9d9a-8c1835750d60 | -7.69023 | -55.16618 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d077d932-6e49-3408-b98c-6f9febdbc6dc | -10.2572 | -45.8276 | 2026-08-10 04:51:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1f20ec8-2c28-37d9-a2ff-67ab7d802a31 | -7.69577 | -55.17037 | 2026-08-10 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 194a5e96-1aa8-3722-bd55-54f430650bbc | -7.15098 | -59.62554 | 2026-08-10 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d002226-9388-3af8-9dd7-add558b32d7c | -6.14087 | -57.71436 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bc262de3-f803-3953-b144-4ee1565c5b85 | -7.65594 | -62.54813 | 2026-08-10 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24536138-c412-31a0-a69e-7ac2c1efc46f | -6.13089 | -57.77481 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e69384b-d353-3d3d-8340-95842dc6027a | -6.83755 | -56.41903 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07d1c2fc-1aa8-3ca9-9337-f8c3cc589dc0 | -4.01533 | -48.96006 | 2026-08-10 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fafb9433-5bce-3814-bef9-2e5d329c2fe3 | -11.04211 | -44.28795 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61a1c9eb-112e-3c05-9e41-45cb3fedde7c | -7.62026 | -42.76661 | 2026-08-10 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README10.md)
