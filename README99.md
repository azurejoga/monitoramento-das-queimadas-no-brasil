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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b89029c-f0d4-31d3-aab9-f4c850db40ba | -9.1197 | -46.98248 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b1cd7e9-c6e9-35b8-8dd5-89101e3b1893 | -11.16113 | -52.02759 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23549083-2eea-3e61-bfec-710462c996fe | -8.52558 | -54.76534 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 133114e3-d274-34b3-8bb3-c9036f14368e | -13.67132 | -44.22364 | 2025-09-11 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7badb0b-df50-3c45-b65c-1cc0df6222a7 | -15.10299 | -50.13655 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 929fe01d-f95a-370b-b11b-382929f7f65f | -11.60258 | -52.22095 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b284fb2d-56b8-3d8d-920c-006028d678c7 | -11.12305 | -52.05378 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d36e20-0323-3f8c-8aaf-741313bc484d | -15.22155 | -44.04791 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 809508eb-4f92-3cad-9691-7df63193df13 | -11.13077 | -52.04784 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486140fa-f643-35fb-b54a-9e027300cfb5 | -11.72303 | -50.62661 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| b496d8d5-7efd-3266-a487-70a58f671433 | -15.1479 | -52.45086 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42a8f486-baf5-3d33-88e6-aa7599402ed7 | -11.22621 | -55.00047 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36069041-3f9b-357f-a7d8-42ddf39e4740 | -12.96934 | -46.73335 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3006ff9f-a39f-3cb6-b3e3-564f795afa29 | -14.14315 | -45.40536 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6da3f11c-7fbd-3072-ab62-71c55ce46fb0 | -14.51079 | -53.96394 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bffe22a-388f-3274-8110-eae7a32155be | -14.91305 | -55.86849 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cc399df-f01a-35c6-b6b9-a471398f8cbb | -11.14071 | -52.04945 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ab3eb7b-595f-3bc9-bcbe-2ca359cb2006 | -11.12428 | -48.39997 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 113d8515-344f-3b7f-9c84-d5d41974749d | -9.72169 | -51.00627 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3769a76-33dd-3124-aa05-afd921f02af5 | -11.15972 | -45.30852 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79b0c79a-4577-3a72-b654-844c7e94725d | -11.48172 | -43.63981 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f011b1f-c99f-3842-a486-f22494a487c9 | -14.49977 | -53.94715 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55034863-e717-3412-9e8c-46d2a3087ef1 | -9.086 | -49.85329 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5049b4b6-8eac-35a6-b3c0-8b5a1fb0d55a | -12.94229 | -54.75501 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b74be3c1-eb56-32f7-b948-73c8814f1e8c | -10.57082 | -51.5052 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46978703-a4d0-3b8a-9ebf-17fa19ff54df | -15.80443 | -52.23847 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f1d64cd-0979-3a52-8427-66534705bc1b | -10.66339 | -48.64236 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bede5500-adfa-3fbf-8c4d-599c8b62be3f | -15.08868 | -50.0592 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 725cee88-9805-31c9-a257-52d0b3bb64ed | -12.12502 | -44.85592 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 923c75ab-3485-3464-98d9-e2a71e87b95a | -11.43498 | -49.28259 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 455b7b99-457d-3bb2-9390-479f4cb63d4e | -12.41434 | -44.72419 | 2025-09-11 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 932ab0ef-8057-31a2-901f-e56509c4a16f | -9.20162 | -51.81233 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cba3e54-e5ed-3d4d-a6ea-75476a50e633 | -14.28519 | -54.76381 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 934e0b75-cc9d-3470-8de8-96f8aeeb0841 | -15.7998 | -52.23025 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bf797a6-0904-3fd3-833e-7151af8893b1 | -11.26119 | -51.1244 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b6a7cfa-ace2-3a2b-9ea7-7a20da40c981 | -9.87855 | -50.1878 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d38c46-9720-301d-9a3f-a6a63d3405d1 | -11.69639 | -48.26359 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e34f94f-34a1-3330-a964-0d3760e63708 | -8.87502 | -49.5616 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 794fda24-7094-3247-a7d9-5f1a721c2bf9 | -11.4601 | -43.60636 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c8d39ae-52b0-3cc1-affe-2be6e242ebf9 | -8.57081 | -51.35486 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0599ba28-8e56-3ee1-ae14-d689f93dbc68 | -15.14071 | -52.4533 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4e5976e-80f1-3b27-b89c-b25cc55eae1f | -12.85597 | -52.94927 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04aa1427-5289-3afa-b23c-2713917b766f | -10.72936 | -46.13459 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bddd7f5e-de0c-3e76-98a1-0723c070c5b0 | -15.16703 | -56.35497 | 2025-09-11 04:46:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9032f2ed-44af-344a-a876-b189aa6da46f | -9.70218 | -46.88249 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91a6eb2d-feb3-3d14-bd87-ce3abac233c0 | -11.87759 | -58.80883 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 718bf657-ff0d-37b1-8c0c-b8efbce230ec | -11.14016 | -52.05295 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f95ba93c-3a34-37ff-9cc8-9c4cb5d04770 | -13.00121 | -48.01134 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 725ac5d0-f97f-310d-9248-4fb93f991a33 | -11.48637 | -43.68333 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22e1a369-4362-39cc-b5ff-684eec5728b5 | -15.6257 | -47.53965 | 2025-09-11 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b1d77751-53c6-3cb3-9ee6-900a49053396 | -12.96429 | -54.7509 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df032039-3ac4-3d37-8cfe-c9d478d8dda5 | -10.54013 | -49.88556 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 780e9e2c-0888-39f2-8253-015d8bc8ab07 | -11.42108 | -43.54457 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab7d5c10-ecc1-3b11-8803-93c2eddd0bc4 | -15.55759 | -54.77353 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 901e59fb-64a3-3111-8b79-13efbbc01f36 | -11.3251 | -50.75378 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 559b94b1-dafe-36bf-8184-637e5bd0a5f6 | -13.218 | -51.76637 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84ee8e9c-dda4-3d97-9e70-f5b556b4c2f7 | -11.36352 | -46.53834 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e8e2bfff-dc65-3b3c-b3c1-c4ea99c43b25 | -12.88103 | -47.95581 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efa4865e-c34b-385f-86a9-d55498483981 | -11.07661 | -51.35023 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff9e5232-084b-30ad-b6b8-7f1abffa3b08 | -9.06473 | -50.49355 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d7d22ff-e314-3b4d-abfd-6a0510fdd3d0 | -8.62805 | -53.12198 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f59e151c-d88a-3478-85de-418777f1baa2 | -11.72586 | -50.63083 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f23893e-91ac-3dcf-8c26-02ba191b6fec | -14.57393 | -48.75797 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7f2f994-a47c-3427-96b0-adf473a8eef8 | -9.90672 | -49.91105 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3b67996-86ac-36cd-ac12-a2486007cd60 | -12.86154 | -52.93565 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52668648-df46-3f6e-85d0-c7ff5469c3d6 | -10.01959 | -51.72942 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0016f190-1816-3ed6-be73-85404ea0cdda | -15.13075 | -52.42955 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2364b052-dd12-3323-841e-7be8ece372e1 | -11.35475 | -46.50889 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8a27b38-fd6d-3c21-b476-8e9e3c2d6878 | -8.08023 | -54.73968 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c2daa1f-a4e1-3f8c-a7f9-1c2551f75dd7 | -13.34374 | -44.00151 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b06ad20-9a33-3c15-aa74-4fdcaba076ed | -8.87158 | -49.56105 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1152d9f7-8e5a-3563-85e4-f13c58aac6ef | -11.14561 | -48.46129 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4176eec7-b6bc-387f-b7d3-9addaf16f3e0 | -10.5443 | -51.5226 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5c5e2fa-5675-3e99-a415-e47f70dc9e8d | -11.44276 | -43.57923 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dfcda6b-f86e-3d14-8319-3abc211928a5 | -11.94581 | -51.10937 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aee43d7a-14a8-3a0b-a247-787de66c235c | -9.07645 | -50.48431 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b152f8b9-4c03-3015-b5df-0c8860f07a85 | -11.43214 | -43.58086 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d4f4cf5-d099-3c03-8545-6579f475aa5e | -9.67717 | -47.52121 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ceb31353-4aff-3849-8035-0f6c2e27a4b4 | -10.17436 | -46.19174 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f89097d-d917-3693-af71-1f4dba2bfd43 | -11.13464 | -52.04488 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a85f390-f184-38f7-b5a0-913ee6ded361 | -12.10056 | -51.02208 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63f3f6a7-5e2a-3bbb-ade6-075fa6595b54 | -10.13952 | -47.89394 | 2025-09-11 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ca09469-0364-3eea-af58-1f6163ce7031 | -11.77492 | -46.49093 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e71f986-8fec-3cf9-b852-1c57b5587f63 | -15.80558 | -52.27579 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0980611-d51d-3b94-a71b-5027eebd2676 | -15.16777 | -56.35067 | 2025-09-11 04:46:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23c77ff4-1a7a-3f55-b915-39ffbe8f844d | -14.36639 | -47.29915 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ca89fef-e6cb-3746-95d5-a0b4960f1707 | -10.3959 | -48.58368 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de84d950-aa77-3b40-9073-ffc30b727329 | -14.31225 | -54.74875 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef38297-8c5d-3992-b755-25530fe5342a | -10.54707 | -51.52664 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9af1d770-6198-3c4d-bda9-a851d07126c2 | -10.66889 | -48.63034 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71846043-ed68-3f2d-bd4e-6ddeb52fbf9d | -8.5719 | -51.34791 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430deaba-a7b9-336a-b0c9-c26caffb13d9 | -9.71793 | -48.08816 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb3ba0b7-e7d3-3508-ab41-0e25f46eb38a | -11.37965 | -43.52179 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e919fad4-e2dc-3dde-b440-c040021deab3 | -15.28291 | -53.78941 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c74d05e7-9a67-314d-b59f-d569f5dcd7f0 | -11.40505 | -45.60642 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1914a783-9772-339d-ad8e-433444701056 | -11.14415 | -45.28733 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bede4263-4789-3914-81f0-d7fd65b02772 | -14.93296 | -55.94468 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f93ca50b-08cc-3279-b4bd-4c42e1fae719 | -14.38223 | -47.33897 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3d4caa3-5f6e-3fb1-8b37-ea04d350f12a | -12.52884 | -45.33931 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e7813bf5-8257-36bf-ac30-7638b442736d | -9.72675 | -48.33727 | 2025-09-11 04:46:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README100.md)
