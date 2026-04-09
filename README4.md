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
| 9d13901c-7d9a-3d70-916b-b87d8fa9b2db | -12.30001 | -57.40224 | 2026-04-09 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 353e54e6-0521-3510-9043-1f43f2de2fbf | -10.72635 | -56.04549 | 2026-04-09 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f03e36-d835-319a-944f-20079000ac98 | -14.92464 | -55.97828 | 2026-04-09 05:31:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31c645e8-fbb8-3f23-ab31-d8d21f02154f | -18.49854 | -55.49372 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2b63c3a3-04fc-33c0-aa3a-f23c75c9227e | -18.50567 | -55.51696 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 010f32c8-eccc-35fa-89af-b26fda8bb528 | -18.50504 | -55.52245 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a62e0a82-40e9-3897-b6e5-af5fafa786b7 | -18.50631 | -55.51147 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7c143257-aa84-3031-b920-d587e4e30743 | -18.49307 | -55.4986 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 775ba90f-8b65-3734-b829-d3c10cf8aad4 | -18.5105 | -55.51759 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 10dc14d0-8ad4-3eea-bf20-57556a5f4a67 | -18.49791 | -55.49923 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b9c9c91e-c5c0-302d-8bd1-8e705f6f2170 | -18.50211 | -55.50533 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4899f6a2-f377-3ede-bc9f-0b3dc5971e72 | -18.50147 | -55.51084 | 2026-04-09 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 41a4f2c8-fd4c-3877-bbcc-0ef6ebde4368 | 3.08593 | -60.8531 | 2026-04-09 05:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 914b10e0-9a3e-39b9-a0eb-3bdbffd3decd | -18.49358 | -55.49247 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57177c5a-32a0-303d-befc-08b5ddcf2446 | -18.50975 | -55.51662 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 79dbaf79-17cb-3e2e-8ff4-f85930f955c5 | -12.30051 | -57.40464 | 2026-04-09 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95eab3da-1d58-3761-b6b9-f0fe5c5546ea | -18.49294 | -55.49971 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4997ed31-0d3d-3210-afc6-95a3c9c293ae | -11.93736 | -58.07286 | 2026-04-09 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5481e341-1c03-3153-9c4f-049afc132a56 | -18.50323 | -55.50873 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a3314bf4-3111-355f-81c1-9010b23a9780 | -18.50202 | -55.52318 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 919e4c45-dec7-3be6-a1a6-baf75bd78613 | -12.30102 | -57.40028 | 2026-04-09 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c31d68d-9958-3bd4-abd0-a55177c70812 | -18.49669 | -55.50086 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1a5f5d5f-ccce-3a5f-9dfc-df801450aac8 | -11.93689 | -58.07674 | 2026-04-09 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba8a3c1-511b-312f-a304-1f6b60c019f1 | -18.49729 | -55.49362 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 0466d542-b003-334d-aab7-9952b0699155 | -18.50262 | -55.51596 | 2026-04-09 05:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 848e829d-27c0-3282-8e28-940dac23584d | -11.20335 | -56.87753 | 2026-04-09 05:53:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4613718-9cb1-3d35-ada1-2123899924b2 | -12.2939 | -57.39985 | 2026-04-09 07:14:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 20af59c6-7f5a-3288-84ee-d6ba3905db5f | -18.5063 | -55.52134 | 2026-04-09 07:16:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 67fe02eb-f426-36f9-b525-082b089de854 | -18.49586 | -55.49385 | 2026-04-09 07:16:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 17d7d8ac-64b8-37c3-ac0c-19140f48dc9a | -18.4958 | -55.49895 | 2026-04-09 07:16:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 8536f56a-b4b3-337e-8451-4e035d028800 | -12.04317 | -45.34089 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2008c0d7-5948-3685-b65e-2a3d7e0dadc5 | -12.03132 | -45.23508 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 447f4296-8ac6-3acd-b381-6f0f5550c5d4 | -11.83774 | -39.17134 | 2026-04-09 11:45:00 | TERRA_M-M | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 40.5 |
| b0abf590-bc07-35c3-85a8-1c6546d21ece | -12.04026 | -45.23641 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba1fd665-41ad-3d01-97a8-d313e16178c5 | -11.906 | -43.73682 | 2026-04-09 11:45:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 501f54f0-bf5d-3213-8ed7-bd0e14ea301b | -12.02995 | -45.24432 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 343cfd45-badd-3b2d-bffd-377a44a5398b | -12.0389 | -45.24564 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 06f43b9a-10d6-3192-94df-48d874a5e78d | -12.04454 | -45.33161 | 2026-04-09 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4fc0eb47-0e1a-3dad-a4a8-1defa006c167 | -14.12572 | -43.41574 | 2026-04-09 11:47:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0cb9eddd-15c5-3d39-bada-868c98172891 | -13.9647 | -47.42231 | 2026-04-09 11:47:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| aed9ef8a-c83b-36d9-8bc1-e9b81c2511a3 | -17.40428 | -39.64504 | 2026-04-09 11:47:00 | TERRA_M-M | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 3e4fef39-565f-3727-ab87-8523f71ed276 | -15.02682 | -45.12567 | 2026-04-09 11:47:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3c84d323-fb59-3a1b-a8a8-7a46acc05b93 | -19.58785 | -40.07542 | 2026-04-09 11:47:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 85f2de58-a1a8-36f5-9186-d05e5a02f8bc | -15.02945 | -45.10749 | 2026-04-09 11:47:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 11bcf8ce-f5ef-3673-b591-12ded0a5cfdc | -15.02814 | -45.11658 | 2026-04-09 11:47:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 59115a45-a208-3e50-889d-8be185fe1abd | -13.96634 | -47.41161 | 2026-04-09 11:47:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e98d350e-434d-3715-a7bb-7b2a8e41af6b | -26.97279 | -49.83096 | 2026-04-09 11:49:00 | TERRA_M-M | DONA EMMA | SANTA CATARINA | Brasil | 4205100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6defa5a6-9665-3938-a36a-6c771b706ff1 | -12.0306 | -45.2363 | 2026-04-09 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| adec6d70-96cc-3dd4-bd28-4e2a1b429225 | -12.0481 | -45.3258 | 2026-04-09 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0f86014b-9975-3fa6-813c-4ceaaa2b00d7 | -12.0481 | -45.3258 | 2026-04-09 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 4eb2d94b-0b51-3124-ba84-f85c6df74ed4 | -12.0481 | -45.3258 | 2026-04-09 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| f3ea4eef-78f9-3915-a519-b86913beacf6 | -15.7867 | -50.9569 | 2026-04-09 15:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |


