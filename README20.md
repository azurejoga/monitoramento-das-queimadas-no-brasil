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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a700f91-df63-32c9-9611-b850b18dc23c | -13.06229 | -52.72581 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb7fd4c-b710-357b-aa7e-a982ebfa2ac4 | -13.26185 | -54.3642 | 2026-08-01 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7660a1-1415-35d5-a3d8-3af20dce1909 | -14.08528 | -46.2349 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d2d5916-d8fd-395b-8e5a-ece8ffc8795a | -12.20063 | -52.867 | 2026-08-01 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8dc5dd2-57a2-36ab-b73d-376661ed931e | -14.41317 | -48.04647 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e883ac2-e6ee-3bd8-9e9c-c5d68fe01270 | -14.08035 | -46.29171 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fb200d8-510f-3b55-a0d3-ee00f3a35880 | -15.02678 | -47.05469 | 2026-08-01 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 804355ce-4df5-3953-beac-31a2d3b2d845 | -9.90792 | -45.74637 | 2026-08-01 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f21c5783-e883-3655-9929-1166452f43a1 | -11.88603 | -57.14357 | 2026-08-01 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd2f23b-e8a7-36c1-b14c-630e3ee5707d | -11.23739 | -54.87067 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac4560d0-ec4f-32c6-a048-8a059b7968c2 | -15.82821 | -48.18161 | 2026-08-01 04:57:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 949f6846-ef53-325a-9172-e5a6ecffa030 | -14.81972 | -48.5092 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cca16760-be0c-3332-b049-29a3c448fed7 | -15.34224 | -47.85713 | 2026-08-01 04:57:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e3480bf-90a9-3a15-8bb0-41a24c8dae4c | -11.76396 | -47.06435 | 2026-08-01 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b32853c3-3948-35b3-96db-87388a48690f | -11.29652 | -47.03479 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ba7c47d-d43e-3b19-b89c-6b1353844707 | -11.23322 | -54.87405 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c23c6244-c226-3725-9a27-ee7385c5317f | -14.08198 | -46.24554 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bbf0ad2-3569-3e3e-b4ed-f6c3bf7344c4 | -11.23389 | -54.87006 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2fcadd-92c9-3312-9cec-1df087f33769 | -14.07526 | -46.29562 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb9a1e01-66bf-3693-877f-1fa860a42f13 | -14.08255 | -46.24132 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7eb81fa-7254-38e1-8124-efb7a14ccbbb | -14.08625 | -46.29915 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4dba330-691c-3484-b07e-b0c308a0343a | -14.07238 | -46.26441 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a2fd1da9-6004-32b1-af83-9c643bde1520 | -10.47623 | -48.49375 | 2026-08-01 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c381f9b-833b-37ec-a5a1-756853a910c3 | -9.59446 | -48.5465 | 2026-08-01 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6efe4ef0-1c11-3286-a9c7-55591cd39a63 | -14.07005 | -46.28286 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae8a82ae-2de1-36ca-ad14-077cd9986801 | -8.62321 | -50.0264 | 2026-08-01 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c94b91-7533-3683-8fa2-58e27b5c674d | -11.77146 | -50.16853 | 2026-08-01 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b70a7dc0-986b-34de-b515-715e0f031dee | -14.07628 | -46.26971 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eee9b50-e1bf-3cb7-b745-eb8cb1409344 | -12.06973 | -45.81182 | 2026-08-01 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c29d85a-17d9-390d-ab08-2c54ffb37b45 | -14.07858 | -46.25159 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f700e04c-a6e3-3581-85d6-a7f371738c47 | -14.08018 | -46.27505 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efe44f0e-669c-394a-9d54-3fbf1a4862ed | -14.3479 | -48.03966 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a12d8d9b-2183-3c15-aee6-cc7e1f10e9af | -14.08749 | -46.25354 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6c4c82a-c4b4-3432-8960-5a3612f0965f | -14.06789 | -46.26377 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cec52d68-3299-3cda-80fd-7fedbdb4f2ed | -14.06754 | -46.28506 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 86f8d7ad-6b62-314d-a710-4d1ba1f49154 | -11.24486 | -54.8475 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91845817-0a4f-332a-a0ee-575a39750d1a | -11.21966 | -54.84712 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42ce778f-2407-3744-98c3-9a428e906071 | -11.29394 | -47.03532 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59d15ac2-bd7e-37db-be90-985f9a491372 | -14.83668 | -48.50238 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a527815-22d8-3893-b37b-421ca2b881ff | -11.44222 | -47.24005 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7f2a55f-f3cb-3515-bd7d-8bfd83571531 | -14.073 | -46.24418 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac08b805-2322-3290-a699-d4d4dd284c38 | -14.08467 | -46.2757 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 50a3085b-c0ae-3043-9c18-51b81359a5e5 | -10.07818 | -49.12373 | 2026-08-01 04:57:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 762edc0a-e6bc-3a1a-a98b-7db5d42019ff | -9.26358 | -50.69328 | 2026-08-01 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe574ae4-7b5c-3ec4-9ade-10c63a593305 | -14.33713 | -48.02872 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4d34c0aa-bded-3c11-b2ef-138d4bdfd11a | -8.44984 | -51.51016 | 2026-08-01 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74825adc-a34d-34eb-b533-bb5b36ae0c8e | -14.08134 | -46.22977 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5c9fce9-6c5f-3cba-82b8-337fac8bf772 | -14.08134 | -46.26587 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02201e27-befa-347f-9567-110f79782897 | -14.08431 | -46.22817 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c988186-6bff-32c6-8a8b-a7a5f5bd102a | -10.08175 | -49.12428 | 2026-08-01 04:57:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efd39480-801a-3d7c-a7e4-e7ad9eb0699c | -9.26694 | -50.69382 | 2026-08-01 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0811332-42f0-302f-a39a-55309b2b7ec4 | -13.95695 | -49.14756 | 2026-08-01 04:57:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94ce194b-d870-3319-933f-3d3854da0e5a | -20.70229 | -54.58982 | 2026-08-01 04:59:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60bdda84-892b-3bda-83cc-30d5287890b7 | -22.23405 | -43.1176 | 2026-08-01 04:59:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2a88011c-c2c1-3ea1-8186-e99f86e60acc | -20.88144 | -48.98422 | 2026-08-01 04:59:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca50f84c-eb0e-360a-bcdf-b7b91e0b0ff5 | -20.60554 | -57.29956 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4ad0660-5ebf-3aa4-9e83-aaca04c47b5c | -20.38467 | -47.74899 | 2026-08-01 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e39498f-f07d-3c40-9a0a-e7235cd74e11 | -21.70471 | -56.52118 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43b820e6-7a01-3734-aa9f-ee1319f53768 | -20.11355 | -50.74596 | 2026-08-01 04:59:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| cf476b37-f3c7-3cae-894e-05b07bd85772 | -17.90096 | -44.30999 | 2026-08-01 04:59:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 548bd9dc-8a9f-314c-b57e-eae61927e3de | -21.66702 | -56.32959 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8ce93db-bb57-348d-b054-f04297de7123 | -18.49439 | -51.61708 | 2026-08-01 04:59:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c96f0acc-111e-358b-a4b3-c947c48c18d8 | -21.6643 | -56.32505 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7262e3b-09d7-375d-b483-199832dc0f59 | -20.57021 | -57.31422 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea0cc85a-67f0-3f68-aedd-81984be4043d | -20.10986 | -50.74536 | 2026-08-01 04:59:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| f394cf08-b5fd-3c66-b178-aa4987a539dd | -16.39609 | -53.3465 | 2026-08-01 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6be91e83-8b40-3c58-be97-714e8eee372f | -21.70745 | -56.52576 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35c59ab1-98ce-375d-b649-31ae0650602b | -21.42846 | -45.48034 | 2026-08-01 04:59:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91f104e8-1f5b-33a7-89c1-46262e85c7c2 | -18.48693 | -51.70109 | 2026-08-01 04:59:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e8108c1-bc1c-35f8-870b-595eca8452f1 | -20.43091 | -56.99001 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70beb6d4-2edc-3717-aebd-1ae8d8987377 | -21.24534 | -49.16324 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db4136b8-94d7-38c3-bfe8-b4573fd7c5be | -20.60482 | -57.30376 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6fa46ae-0b20-3b31-a1ac-1863804f8b3b | -18.48751 | -51.69708 | 2026-08-01 04:59:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9f29960-9c7b-358f-8a85-5e82c41cf017 | -20.56241 | -57.3171 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5ed2b0e-7073-321d-9dae-276966504a75 | -19.2006 | -49.62155 | 2026-08-01 04:59:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6dedcdf-b877-3c63-aaae-51e6d0269c06 | -18.49558 | -51.60901 | 2026-08-01 04:59:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e93cf402-d2cd-3648-a1ef-39c0ac5daa0e | -21.03975 | -55.82941 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3713221a-17d6-37c4-8dff-8d084cd09b1f | -21.04709 | -55.82689 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b1ea71f-462b-3bb7-9e64-78a9fcfe8891 | -19.81978 | -54.6471 | 2026-08-01 04:59:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01e69e9a-0f32-30bd-9d49-9137276e23fa | -20.56168 | -57.32132 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eab72ea8-70c8-3151-ac27-6d332160e190 | -20.3852 | -58.02539 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e6f67173-4105-3979-bae9-c1187d85064f | -21.41341 | -48.07203 | 2026-08-01 04:59:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db23904e-e778-3b64-b1a9-72459b7ab445 | -18.48541 | -51.70202 | 2026-08-01 04:59:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11172f9d-c1aa-3d33-9958-ce95a06f7edb | -18.49499 | -51.61303 | 2026-08-01 04:59:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3168271d-36dd-3ff9-aa69-138c4e029603 | -20.42819 | -54.5867 | 2026-08-01 04:59:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bed926cc-d47d-356e-9e12-85ebb70579d3 | -20.38155 | -58.02466 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8e9966be-7148-3fc9-b88b-05d04393a0ba | -21.24582 | -49.15937 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8f29d078-b855-34af-acf0-209a415fec0a | -21.7081 | -56.52186 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ac164fa-069c-3613-9c90-50e26d48e835 | -19.20168 | -49.61822 | 2026-08-01 04:59:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ea61373-e152-33fb-81ae-1ad5d01fe426 | -21.26327 | -49.15365 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c291427-ac20-3c29-924b-018db4e41ee8 | -16.40438 | -53.35176 | 2026-08-01 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d159dabf-43e6-3aac-bd0b-7789edba882f | -20.55962 | -57.31222 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b22b99e3-e347-3f92-888b-135f01512377 | -17.43037 | -42.62616 | 2026-08-01 04:59:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be88aa1-ca8f-389c-91c9-f7903a1959c8 | -21.66768 | -56.32573 | 2026-08-01 04:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 349d3849-294e-34ae-a84e-ab1a8e52ed48 | -20.38458 | -58.02296 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6d267d50-8ad1-388a-8d68-5b06ccc08b88 | -20.31754 | -58.08669 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80cfac2a-6290-3cbe-a4f7-65497f269206 | -20.5649 | -57.26123 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 514c53e8-32c2-3113-b39a-ee91990b886b | -21.24123 | -49.16262 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6f6aa290-7bf3-3b8f-b025-d4f00b5e04c4 | -16.40494 | -53.34817 | 2026-08-01 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ca78a90-258e-3b8b-843f-e5e369b68dd6 | -20.51849 | -57.17627 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README21.md)
