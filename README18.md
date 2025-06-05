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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18c858b0-f755-355d-8319-d9afbf54f740 | -7.90138 | -50.35826 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba33ac90-ac9b-3c6e-85e2-f489299a649b | -11.06873 | -55.04699 | 2025-06-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cbffaa6-964a-3e3e-9c6c-1088677c7133 | -10.65746 | -49.43896 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dcf8e09-d7ba-347b-987d-cd66cf10ab33 | -11.54953 | -56.43346 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb7f820-f523-3f90-8467-63462a494bb0 | -11.53678 | -56.43537 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7eafac30-66e7-33f0-8e3a-75b620d41a86 | -11.54493 | -56.43658 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4886890f-f665-31a4-9ba3-b54c693d2420 | -11.49941 | -48.37846 | 2025-06-05 05:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 385978c4-d4b7-32a1-87f6-a4cbb269a875 | -11.54033 | -56.43966 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24e6ed65-f06c-3286-940a-884739d48015 | -10.65678 | -49.43079 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6612c7a-e6b1-3c5e-93f0-63cd3cab5406 | -7.90085 | -50.3624 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5acca3f-e2aa-3e69-831c-4493c7a581ca | -10.6561 | -49.43628 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db623431-2280-3256-9df8-99ee2eb00720 | -11.53626 | -56.43906 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 061dc62d-3d37-3f97-9a38-c04ef08a92ee | -11.6335 | -55.37746 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36b813c6-6bad-3f32-8e7d-c5db472e2ac1 | -10.94506 | -55.32745 | 2025-06-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1167e581-28c2-3bb3-800b-dc4388920fd4 | -10.65167 | -49.43277 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92c4f0cb-478f-357e-bc92-3cbc88fd6087 | -9.2467 | -63.28764 | 2025-06-05 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c49bb64-9659-301b-a187-95a1ee736338 | -11.55108 | -56.42242 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29732c1-bff8-3028-ac30-1591eb2bb09a | -11.62287 | -55.38592 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a565884-bb06-3ec3-8976-a7252dc12fb2 | -7.90131 | -50.36404 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55168f08-486b-3669-a750-8315bf5f1b50 | -10.70878 | -48.78106 | 2025-06-05 05:23:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb7f4eb3-ce97-3155-9f32-7424d8ef701a | -10.8195 | -56.95592 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 904892cc-f1aa-3e7e-baef-96637eaced45 | -7.90771 | -50.36073 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e7a3221-5a12-3f83-91ae-80f2a54fac5b | -10.93955 | -55.33521 | 2025-06-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24b485cf-00ca-3b1e-b65a-37d44211786c | -11.5516 | -56.41874 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cefe8f4b-b2f6-38c8-af5f-27e518c7c4dd | -11.1298 | -54.21906 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc927962-ccc3-3fa5-a840-6562ea743650 | -11.14238 | -53.94751 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bb221f1-b088-3499-838c-2110810accea | -10.55803 | -59.20392 | 2025-06-05 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 914e6fe4-3abc-3ba7-955b-5c9de4475169 | -10.65546 | -49.44156 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea3c98d6-fe5b-33e0-880a-bd5a982d2fbb | -10.29573 | -57.13872 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56524ce-59a3-3b9b-ae28-5b14534f5a9e | -10.65105 | -49.43816 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa3af69-aa07-3bfb-8fda-8f79097ea59b | -9.96421 | -64.93642 | 2025-06-05 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfcd3e24-f805-3131-b3a9-b53844d9b32d | -6.20511 | -48.55958 | 2025-06-05 05:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1283d4a9-4f5e-34b7-8303-5ab20240c349 | -7.90187 | -50.35991 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 16d15ca7-6cc9-32d3-a418-60055b6e3bda | -10.29503 | -57.14351 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9453117-a38a-3d7a-8b5e-3a4710b2446c | -9.43153 | -62.11203 | 2025-06-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 937e153c-630d-3338-a553-61d74d6ce101 | -11.13828 | -53.94157 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb43197d-8eaf-3084-a1a1-28b66c4c25f1 | -9.68262 | -57.18132 | 2025-06-05 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03898fe5-ce47-3521-b982-093f53b3f4d0 | -10.69268 | -57.64809 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33194cb3-c1b0-3980-9fce-acb230075974 | -8.96736 | -47.96834 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9620c940-e752-38a6-ad5d-4454763f8e75 | -8.96126 | -47.96933 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a44e18ab-e2fe-3142-bd14-477f8df52497 | -10.94013 | -55.33099 | 2025-06-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26edd434-90d9-3946-90c2-56eb217c809f | -10.29391 | -57.141 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afe3f487-0e4b-3c5e-a322-b7f039ec4698 | -7.90722 | -50.35909 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8232002c-5c14-37bd-a695-2b4a85cd117b | -8.96656 | -47.97456 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1825950c-4b36-3de3-bcfa-981ad5a8ff83 | -11.53219 | -56.43842 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e056cb7-f2cf-342f-b350-48311730fb1d | -8.96812 | -47.97022 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd0d7e38-35e3-3ce7-b7d6-2b6c0a1be1ec | -10.64906 | -49.44069 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f48b76f-483f-393f-b072-15ba043ac499 | -10.81169 | -56.95477 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed0c2fa-52d1-33e3-acef-0d8197083496 | -10.29886 | -57.14408 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 165c7b8f-e53a-31cf-93bc-7f0021786f99 | -10.69643 | -57.64861 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d420c1fd-29d4-3697-8fdd-b377b1c4cea1 | -11.13199 | -54.21661 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ece5465-4e91-3b7c-b4c7-878bb2ce4884 | -11.13759 | -53.94679 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b63956-e430-3067-9330-0c94d39bfac3 | -10.47307 | -55.59185 | 2025-06-05 05:23:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e141ca0c-7840-33b8-bce2-652c2a8199a5 | -9.24201 | -63.29465 | 2025-06-05 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fcee73e-a829-331b-9184-e564cb9df151 | -11.49906 | -48.38168 | 2025-06-05 05:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97620514-a48f-323b-bbcd-f9b1d4a25eaa | -9.60526 | -63.22141 | 2025-06-05 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f06476b-f8c0-35d4-968d-0db212812cac | -11.06934 | -55.04253 | 2025-06-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59e49476-420a-3ff4-a728-dc7033b85afe | -11.54849 | -56.44083 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4fdb53ae-1d15-3df5-bae2-42ac41ead57c | -9.41095 | -62.4524 | 2025-06-05 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddde2a85-3d92-3063-8c2e-30ec61efa7b7 | -10.81878 | -56.96093 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 709ecfc1-3dd1-3ccc-9874-707d51e0107b | -11.13604 | -54.22236 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 565db7e5-6fda-3b61-8855-509da19d2697 | -11.62416 | -55.38058 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbae93d3-deef-327a-a9b7-4e6153632ea8 | -9.39057 | -48.41021 | 2025-06-05 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8d3e1f-083d-3d11-ac9d-a371e23ef1e4 | -11.37804 | -55.11029 | 2025-06-05 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5257439-9b7a-3874-a46e-f0179421a68e | -9.24263 | -63.29086 | 2025-06-05 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c07189f-1f42-33d4-a360-a35c5b485834 | -10.30158 | -57.14217 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fccd956-681c-354f-93af-325e2db952d9 | -11.62854 | -55.38118 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a6ce044-292c-3ea4-b584-de5a3615350c | -9.26499 | -56.29982 | 2025-06-05 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14adc01-a825-3a43-8777-dc79de376dc5 | -9.38461 | -48.4032 | 2025-06-05 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989b76e0-e25e-365f-907a-9ddf0d37148e | -11.6236 | -55.38485 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25c3e551-363b-3e81-8d7c-969e1b856fa5 | -11.54597 | -56.42917 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 143784b3-15aa-3a3f-81f9-3009206792ee | -10.6523 | -49.42728 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dbc6262-91aa-393e-8d7f-2f40ba3cd5ba | -11.54137 | -56.43227 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d48b1253-5597-3a96-8da6-57a574af7c13 | -8.96051 | -47.97551 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e73e62f4-91c1-333d-8eac-4aa06ea1c6e0 | -10.81559 | -56.95534 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ab76962f-1e13-366a-b987-c6724fa7a0de | -10.76319 | -54.78504 | 2025-06-05 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6250cd08-9599-3b35-b98b-227d2820b566 | -9.45728 | -55.94173 | 2025-06-05 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caa74614-516c-3162-9860-3240c4cc548f | -7.90714 | -50.36486 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cec791f1-7b59-36df-8434-230797f3771f | -10.75869 | -54.78437 | 2025-06-05 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb0f03d3-a9e9-3038-a041-a6b4a218fa6c | -10.30926 | -57.14325 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 496e83c6-629f-3856-abf9-2f250c691192 | -9.96265 | -64.96793 | 2025-06-05 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daafa191-ee23-3585-b309-c56b8f2aa6c6 | -9.40818 | -62.44825 | 2025-06-05 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af5fcb2b-7b8a-3767-929a-5d398748fd66 | -10.65809 | -49.43354 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aea7ba79-8a2a-32c6-bcf3-0f4865d36df2 | -10.29774 | -57.14162 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44ed4664-d09d-3988-b7f1-f670fed50959 | -7.90668 | -50.36325 | 2025-06-05 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fb9ed8de-b509-3163-9b1c-d4abbcf6cbb2 | -9.50264 | -57.14496 | 2025-06-05 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6865ab90-c9c8-3ea0-a5a1-590e91f48b73 | -10.49315 | -53.65966 | 2025-06-05 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4e27327-ca1f-3492-bc1d-685bc537f69b | -10.81488 | -56.96033 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 19da6d9c-2ed9-3d5f-a82d-d759e41b8aa4 | -9.49884 | -57.14441 | 2025-06-05 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b066c3e1-e870-3498-9aa1-d14b35e89c6f | -11.54901 | -56.43714 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32cc6234-5b6a-385e-8a02-70aaa50bf7dd | -11.64846 | -58.2622 | 2025-06-05 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e628171-492e-3f40-9311-095e7592edd7 | -10.49872 | -53.65493 | 2025-06-05 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71432367-105c-3c88-b946-61a0b997eb22 | -13.507 | -56.56523 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c9dfcfe-df14-3273-8007-13269386de0e | -13.52465 | -56.55996 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d302168-ff99-3626-82d0-3fbaf7680ba6 | -12.01678 | -63.79294 | 2025-06-05 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0052be9-1349-34f8-a740-35fb1d1c78ef | -13.52413 | -56.56387 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2df7a7fa-8660-3006-aa6e-09e71b030ae4 | -13.51429 | -56.57423 | 2025-06-05 05:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6c44ae8-db46-3e72-81ac-69609858cd23 | -12.66579 | -58.21408 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 37204d86-9764-395f-92dd-ee259df8d607 | -18.83699 | -53.63359 | 2025-06-05 05:25:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e91698db-f4ab-3ac0-a1fd-2d3c5d14f0e8 | -12.67258 | -58.21965 | 2025-06-05 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
