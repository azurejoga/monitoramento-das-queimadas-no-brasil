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
| f93685fb-9285-32ec-9ea8-7514628c1463 | -12.39551 | -50.37621 | 2025-07-18 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bb175a3-2994-3cd5-a472-e9bcc4c4ebc3 | -12.66659 | -47.09414 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4759dd2-912b-3082-bbee-aae63ee0632a | -10.68033 | -56.54501 | 2025-07-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e761b54-c480-3c64-af13-30ffdbe0c019 | -11.56226 | -47.07469 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c735a9d2-1f4e-3c46-aa22-741fda45ae4b | -12.48213 | -46.92401 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1be5ce0a-9a22-3e8b-b099-4f525ff0a8d0 | -12.50444 | -57.78412 | 2025-07-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3c2a87d-4b92-3764-8db2-31c21720120a | -11.56864 | -47.09012 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7146825b-b1b6-33cc-9824-a97cbd66df52 | -10.82014 | -49.29206 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09bbf843-90ca-3ee2-9793-1cff730ed57b | -11.56793 | -47.09667 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e189894e-b8e5-370f-b52a-aac1c2df00d7 | -11.85741 | -46.75216 | 2025-07-18 05:18:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d98b90df-0411-3394-a299-9d96ac745c48 | -14.14942 | -51.02673 | 2025-07-18 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56fad529-82f4-32bc-83a4-95c8851f0f86 | -12.03509 | -48.76155 | 2025-07-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13984fcb-0e5d-382f-9fa2-4bfef0eab329 | -14.27514 | -50.50224 | 2025-07-18 05:18:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eeb8427-c5b9-39d1-8a56-673db282607e | -11.73586 | -48.19129 | 2025-07-18 05:18:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ca688403-ec8b-3b36-874c-a1e762e2ebf6 | -14.15451 | -51.03122 | 2025-07-18 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8be6911d-5f29-38cb-9f6f-6872db448fc1 | -11.57006 | -47.07701 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fb526255-cef2-315b-a625-0aeb56178de6 | -9.71893 | -62.33795 | 2025-07-18 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b960cf41-5c8f-3331-aa9e-db29d389d23c | -9.88294 | -65.17073 | 2025-07-18 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17b0cd16-17e8-3878-840d-eaab3b6bd6b0 | -10.68076 | -56.54694 | 2025-07-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1784721-d990-365f-ab49-77ff5f1ccaa2 | -11.85671 | -46.75857 | 2025-07-18 05:18:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b018296-842e-3321-8414-d1bf20c2b43c | -9.25082 | -63.63038 | 2025-07-18 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 413eb3cf-3e95-3e88-a5ee-cf45264e9d79 | -12.25824 | -63.82038 | 2025-07-18 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3549c267-9ddf-3ce3-9cf3-eceacfb8e414 | -12.48285 | -46.91731 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7338c54f-3e95-36e7-ad7e-22a8d0907c05 | -11.74228 | -48.19207 | 2025-07-18 05:18:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3f6be117-5cb5-3800-8eb4-5cf38c7820ae | -12.65921 | -47.09819 | 2025-07-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f141809e-70f0-30cd-bf6c-143f7710bcbc | -10.14257 | -67.72364 | 2025-07-18 05:18:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a01e9e0-0d70-399e-8b3b-417b1f93b784 | -10.67342 | -56.54583 | 2025-07-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 805cf540-e5f3-378e-8ec4-616b006c1269 | -11.56003 | -47.0941 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2bde9cd4-62f4-33a3-b42e-4c7b4ef51ce5 | -11.56688 | -47.09492 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9ca7507-e7f9-3169-9c8d-c90788497239 | -10.05364 | -59.10254 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adfc16b7-ba5c-32e3-8d2a-c2ea118178aa | -11.45656 | -48.16147 | 2025-07-18 05:18:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 309cb7d1-f251-34e7-81f5-114a3add94e0 | -11.56079 | -47.08754 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9981899f-6462-31e4-aa8a-a5c3d4819fb0 | -11.5618 | -47.08924 | 2025-07-18 05:18:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d300bd9-02e0-34f8-913b-ed9fbcb87819 | -10.81742 | -49.28495 | 2025-07-18 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 069a60a6-0738-3e19-92db-2857cde4fa81 | -11.46098 | -48.16489 | 2025-07-18 05:18:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b584bae1-beba-344f-8a35-7bdd4cfcc715 | -10.08485 | -60.50187 | 2025-07-18 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad3847b0-0c18-3777-ae1e-df73f3b09dd1 | -11.7317 | -48.1849 | 2025-07-18 05:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 22a6141c-45b7-33ae-a454-b31ec2fda224 | -11.7508 | -48.1825 | 2025-07-18 05:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 52071e17-025a-32d1-bdd1-854cd5b74f24 | -3.3958 | -47.4785 | 2025-07-18 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3ecbd9ac-45df-3656-8ff9-60f7002488d1 | -5.6567 | -43.7161 | 2025-07-18 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 90c100be-154f-39f1-90c9-6c221a6f80a7 | -20.19785 | -50.49539 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5a43e261-9759-3402-8c58-85e6874928e6 | -21.03738 | -55.98831 | 2025-07-18 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fc20da2-5aca-3a0f-b37f-bcebf30970c6 | -20.1917 | -50.49477 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3e7ef11f-6cda-30da-97af-0a5562b1f5f0 | -20.99357 | -49.76758 | 2025-07-18 05:21:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc5963f4-9480-31be-a5cc-357e7ebdc6ae | -20.99308 | -49.77322 | 2025-07-18 05:21:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5c6a2884-fbc2-3794-a0a4-dd87a2358aee | -21.86131 | -56.74076 | 2025-07-18 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 860f55b8-7e20-3bb5-8e6c-8946c6a2408b | -21.10813 | -55.80582 | 2025-07-18 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b80630-55f6-3afd-b26e-ff1dcbd7eb7a | -20.19173 | -50.49823 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4bbd8454-d805-33e9-8f44-000a61bc576a | -20.19128 | -50.49963 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5c119eaa-76d0-3f97-859d-846648bbddb8 | -16.45179 | -54.54755 | 2025-07-18 05:21:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f844dedc-1ef5-353b-b22a-2be92a5469ec | -20.99407 | -49.7699 | 2025-07-18 05:21:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2e4eed76-7250-3e20-8d4b-8e9162462e20 | -20.9876 | -49.76935 | 2025-07-18 05:21:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8e29d038-7f0b-39ed-acb5-3662d082ce03 | -21.86555 | -56.74403 | 2025-07-18 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2c6588a-5cf2-36a4-b314-892f17b8d47c | -21.04175 | -55.9889 | 2025-07-18 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 389db046-6df8-33c3-a624-646a9138ccc4 | -22.65513 | -53.37794 | 2025-07-18 05:21:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99ed6431-2ca1-3afc-826f-ffc8d4b3d52b | -20.19743 | -50.50019 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 88e7e657-42a4-38c8-bcf2-e954c933fbb2 | -22.05242 | -49.96426 | 2025-07-18 05:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0fbcb0e9-44bf-3a24-b11d-7de525cd82c8 | -21.86552 | -56.74131 | 2025-07-18 05:21:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebb745d7-4ec5-3262-beba-22e3f5d4f2cc | -20.20652 | -56.61354 | 2025-07-18 05:21:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 75e559a9-0213-326d-b3de-9eee231b3645 | -21.03791 | -55.98381 | 2025-07-18 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5524b245-82ce-39cb-af83-17b024daf8cf | -20.19788 | -50.49879 | 2025-07-18 05:21:00 | NOAA-20 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f1a36649-312f-32ac-89db-db4cb2f44604 | -3.3958 | -47.4785 | 2025-07-18 05:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 50137448-b3c5-360a-af91-5a815fe9cbd7 | -11.7508 | -48.1825 | 2025-07-18 05:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 06da4142-b7e3-372d-9f35-dacf4713068f | -5.6567 | -43.7161 | 2025-07-18 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| abaa0518-0fbe-3923-813c-3196ef3c3529 | -3.3958 | -47.4785 | 2025-07-18 05:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7c18a19f-c1ce-35ed-94e0-430d0618653d | -11.7508 | -48.1825 | 2025-07-18 05:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 93558939-d2f0-3dba-85dc-ec27738c2f8d | -5.6567 | -43.7161 | 2025-07-18 05:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| b6d5b4ed-7151-3442-9100-4ef56dd5ce56 | -11.7317 | -48.1849 | 2025-07-18 05:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e820757a-af49-3578-8e16-7940ab5ebbc4 | -3.3958 | -47.4785 | 2025-07-18 05:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 74a6a128-fd24-3c46-a862-45de54c83d85 | -5.6567 | -43.7161 | 2025-07-18 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6d605b77-beee-37c8-a891-2cb384f133d7 | -3.11323 | -47.0107 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 4cab91e8-0e74-3033-885b-cac098889f6c | -3.39347 | -47.47876 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 737f325e-ce17-3118-ad0a-c2156270ddb5 | -5.19122 | -45.48242 | 2025-07-18 05:57:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b5bed93c-8c5f-3e0a-acc0-bcb5f86c2555 | -4.30537 | -48.11122 | 2025-07-18 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 52c729de-b444-330d-a2c3-e3bed68d07a2 | -4.30669 | -48.10247 | 2025-07-18 05:57:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 3c50212a-6daf-364d-8185-326e3c5bec6c | -4.10665 | -48.20374 | 2025-07-18 05:57:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6f2cbb6c-68c9-3dac-8e7d-411b05f5672b | -5.64667 | -43.72061 | 2025-07-18 05:57:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2c7bd7e3-edf4-35d7-a6ab-7322457f1e46 | -3.39082 | -47.4964 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5f5bda19-3b90-355b-8bf0-86a122a223be | -5.66003 | -43.70728 | 2025-07-18 05:57:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 20ce2c08-532f-3055-8a79-33234f857fec | -5.64877 | -43.70571 | 2025-07-18 05:57:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ecbedb3c-f6cd-33c5-a908-137f7b96fbfa | -3.39479 | -47.46994 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d93209ac-41b9-3597-a45d-f92bda236556 | -2.90904 | -48.24214 | 2025-07-18 05:57:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| de8f51d0-8965-3617-b28e-c4b3e8e14f97 | -8.07464 | -43.14407 | 2025-07-18 05:57:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| c0be6c54-9a8f-3dee-834d-2a9ab17717b0 | -4.95671 | -43.23149 | 2025-07-18 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 33ef96c4-ebdf-33d4-a886-35cea5e7105f | -3.11457 | -47.00169 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b15dc60a-de8b-3720-9d5a-fc4185ba14f7 | -8.08692 | -43.14587 | 2025-07-18 05:57:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| d53d85a3-f76f-354d-a42d-878a5d8df35e | -6.77413 | -45.51188 | 2025-07-18 05:57:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e5a9afc9-0a76-3260-9f00-530807e739f9 | -5.78099 | -45.07663 | 2025-07-18 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 50008322-86b9-3165-9ef7-5fba2d3dfc7e | -4.79911 | -43.21334 | 2025-07-18 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 04d2939f-59f5-325d-883a-331bad93e284 | -6.7641 | -45.51067 | 2025-07-18 05:57:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 14940dc0-9f6d-307f-ad20-d912eed6c21d | -3.12214 | -47.01199 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 04d52a32-9ec8-3dbe-ac9c-18e66e42e141 | -3.38331 | -47.48631 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1a9a3386-f447-3a92-abb1-a063a323c795 | -6.68912 | -43.17934 | 2025-07-18 05:57:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 15.3 |
| dd00acb8-1f0b-36f3-8260-abd610a0a4f3 | -3.39214 | -47.48758 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 203a5488-fff1-34da-bee6-d19f249b7ea6 | -5.6579 | -43.72229 | 2025-07-18 05:57:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9feb8d37-df2d-3dc6-8ff4-546fec580a19 | -7.35015 | -44.19322 | 2025-07-18 05:57:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| faf3da99-7bab-3390-835e-6549039ce3c0 | -3.38464 | -47.47749 | 2025-07-18 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 43557fa1-8afb-322d-ab99-a5b70d535bfd | -5.78365 | -45.07009 | 2025-07-18 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8e999452-6b46-3be3-a107-c5ff4240269b | -6.68319 | -43.18404 | 2025-07-18 05:57:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 13.0 |
| e2bdce8e-eae6-3bb7-bc69-f1e6cc15d7d5 | -3.82743 | -47.74121 | 2025-07-18 05:57:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README29.md)
