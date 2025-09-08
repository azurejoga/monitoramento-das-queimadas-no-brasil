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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 281fbf12-cc67-386f-bb0d-4d2c6d1d7014 | -15.07793 | -50.10398 | 2025-09-08 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eae44e60-0a99-3469-a2fc-2ff3257aa329 | -9.47805 | -60.50111 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92acbd9f-465d-3fff-879c-7cb4320b0c25 | -16.34534 | -52.94868 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd9fdd29-acb1-3f83-9001-b84c8dbbdf4c | -12.79421 | -60.18494 | 2025-09-08 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c189b5c4-25c8-34fc-b494-9c8faf322107 | -11.86124 | -47.54283 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ae8412-2136-3315-a7b8-99b54b54630c | -16.52406 | -45.10091 | 2025-09-08 04:53:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f2aee7c-316d-30f0-aa5d-193c6e807e06 | -9.20762 | -65.9129 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b63f7f32-db83-3b7c-8065-c0a3cc5d72e2 | -10.02779 | -63.48019 | 2025-09-08 04:53:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c5bebd-5f1e-3640-b39b-40c8e93d55dc | -12.72147 | -56.56511 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a392a6fb-6b3a-375d-a989-d19803936591 | -15.76875 | -53.55961 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b8c1e20-af91-3453-ab71-e1f388725f17 | -17.10843 | -48.993 | 2025-09-08 04:53:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dbe1a52-56c8-3232-9244-88dc8c9db5aa | -12.62873 | -56.96997 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 665024a5-169c-3331-aaf1-c0b379fdf843 | -12.47844 | -53.85823 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e9023d-0b7e-3cf8-917d-70622a80d10d | -15.82784 | -52.27751 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4dd9f15-2891-371c-8eb5-936a39154e6b | -14.80617 | -48.24203 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 920f147f-6c41-34cc-a087-71952f065583 | -12.83688 | -52.93671 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4898e349-f88c-3d07-8431-eca83d42ddaf | -11.63437 | -52.23777 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cc96d8f-71cb-32e3-b79f-e1d692e1ba0f | -12.95146 | -54.80949 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f5b9d67-28e4-338b-b5b3-0ee39e9f58a7 | -16.33387 | -52.931 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c4e694b-7fd3-3766-940d-d123c7bcbeac | -12.94875 | -54.78361 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09b70ffd-cf2b-30d1-9357-f9fe270e7878 | -14.51632 | -48.7561 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7c820b5-84e5-3bf3-8327-b09afac12ca2 | -11.21057 | -55.01181 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 027e8780-1b22-3b97-bbea-4bc4aa0b40ef | -11.83104 | -46.7704 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f3acc8d-0960-388e-984c-65855e74a106 | -12.60904 | -56.97911 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5132080a-f3a8-36d5-b59e-be81d2c62554 | -14.79647 | -48.10495 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8424a3b1-25f8-37b9-98a3-abb8090eab4d | -12.82963 | -52.93929 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d4f097c8-c703-3686-9cd6-774d11d1b183 | -11.90536 | -64.96965 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb66b56a-88d6-33ba-a981-71c7f8964d3e | -10.88923 | -55.71394 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8762c825-47a6-3368-91ca-1bde511a6b98 | -15.14939 | -52.31898 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65f45c73-b90d-3baa-8aa8-6f17734dbbc4 | -11.41198 | -50.37476 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6d113027-e80b-3542-bf40-90608da17e8a | -12.83634 | -52.94035 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44c86500-25e8-36e2-b3be-88f692429057 | -11.31952 | -55.11806 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 010aa304-128d-39f2-b557-8c00b268530e | -16.26711 | -48.48656 | 2025-09-08 04:53:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d7dac2f-d0db-32b8-94e1-b47c23c61f78 | -11.00234 | -52.05864 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5d56c69-c0de-334a-a3d9-7bd37f9866b1 | -17.65399 | -44.18279 | 2025-09-08 04:53:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36fcf72a-1964-3c00-a508-9e9935dfdde8 | -15.82547 | -52.26914 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f216a56-cf29-3bf3-900b-4aee00be19af | -17.25182 | -46.69421 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b7e36b6-0bd3-38a1-85b8-3e2af2ae94d6 | -16.90943 | -45.8391 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de476895-f5fa-3569-9003-4c86ae3445f0 | -13.83662 | -46.24448 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a7f4c82-217a-3ead-a9f3-f72cab742ab8 | -14.53236 | -53.98664 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 551f074f-5f46-3d26-9939-f2ec1449137a | -12.81447 | -48.00128 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 487a9640-f280-3b0b-a883-2774c35ac8f9 | -15.29848 | -46.97793 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c6ffa42-aba6-3438-bcba-279da37812ff | -13.73858 | -46.89968 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d29efa4-a253-35ca-aa4f-d6a10889aea5 | -11.20055 | -55.01018 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf869cfb-459a-373e-aa05-e371106a10c7 | -14.35266 | -60.31556 | 2025-09-08 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02c36aa1-7489-39dd-87b7-75f45a485a7c | -12.95155 | -54.76593 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d28f0e5a-6175-33a0-be6c-4cf36e0648d6 | -15.25031 | -52.39459 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14c71f10-8f6c-391d-9f5b-502e766e685a | -9.62817 | -64.21149 | 2025-09-08 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51abb35b-6199-3676-b6fc-277c925e5c46 | -12.61325 | -56.97565 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be2c048a-f64f-35fb-ab99-3a195e1a2b0e | -12.60699 | -56.9912 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d244505a-9fc4-3dd9-a676-c8184c868529 | -12.93775 | -54.76729 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b62f6602-99c1-30ad-af0d-52902682a708 | -14.8785 | -55.82655 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a14ef51-2f06-3262-99de-9d8c15232f7f | -16.91051 | -45.82917 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a60124bd-b3ed-3106-910d-3ca6253bd208 | -16.28705 | -45.68584 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e17d31de-2f5a-3d41-a15e-cc76b37def06 | -13.94423 | -54.00824 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b69768ff-2b2a-3a63-b8e8-d0916a2ca8f3 | -16.89473 | -45.77568 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c3b9224-473c-3781-a773-80afea9610f7 | -11.40957 | -50.36544 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bbc20e33-5780-36d3-b34d-7d6c27e27f1a | -14.52477 | -48.7573 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9b20f79-a1ab-3483-8ca8-4b629a6ced2f | -11.83464 | -46.76751 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 226c1d21-f3c4-3857-9ab7-21f14226395b | -14.28018 | -48.9475 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b772a996-4203-3e73-b92c-f72e2ede6aae | -12.01231 | -50.38045 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af2f836d-27e3-3c73-88a3-741e51eacc28 | -12.82894 | -52.89818 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74c195bd-2d55-350e-bbe9-8e56259e550e | -16.33264 | -53.74275 | 2025-09-08 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 754d24c0-0475-39d4-a275-6f14880df3b3 | -15.83654 | -52.26705 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 749eb91d-daaa-39fb-b68d-29a846be057f | -15.76259 | -53.55477 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 070578e4-5864-3725-b64b-8e94795f18d9 | -9.47891 | -60.49636 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8661692b-6e5a-317b-868a-37db63f36008 | -12.63022 | -56.98266 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c0a6ee68-57df-3104-952f-9ea7c7de18e0 | -17.16107 | -49.0106 | 2025-09-08 04:53:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa154fc4-9783-322a-8c2e-50656e5195f9 | -11.03343 | -52.03675 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61d9e267-0506-3a45-8788-bdfa54ae5fe9 | -11.65356 | -52.22554 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0f11308-eb72-344b-b589-2c9d56154bc5 | -12.9576 | -54.77056 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54011528-f613-3d60-8e5f-8838f7a950a0 | -13.71943 | -46.89891 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 873545df-8835-3fdf-bf9e-67dadc9ac6a9 | -14.931 | -55.88393 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0356d4c-a0ed-3bce-9d47-6c0fadf34aa0 | -12.01907 | -50.38602 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb66fef7-8f26-35af-a8ee-6bc3ad59d380 | -11.2019 | -55.0657 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b53f4ca0-4089-3cc6-89fc-bfb91f017bbd | -11.20447 | -55.00713 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a249519e-1f89-3593-9789-f2bd9180a72b | -12.62737 | -56.97802 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 06127cdc-1e3d-3d8e-b87c-946a5934769b | -15.2503 | -53.82563 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5278c4e8-fe74-3485-9523-fac30f556e07 | -12.95206 | -54.78416 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6bc54da-661b-3d7b-9d26-7744ff76466a | -9.48065 | -60.48682 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d3ee25eb-2886-3262-99f6-4d7286a437dd | -16.28743 | -45.68247 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 94c24f3d-78ad-398d-bf14-a6d6627b65da | -12.94045 | -54.79315 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b352f953-60e1-3f0a-b66f-0385cf513ce7 | -12.35705 | -63.63708 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b158b4-63a5-3e97-906f-fbe46daecc8e | -11.21 | -55.01539 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 816d17a6-5522-3ce0-a361-3484a518714f | -16.3419 | -52.94818 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d4ccc1e-0404-3081-8e20-5f4a5d4a7324 | -11.91055 | -50.99286 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9213ec67-52c7-3b65-9382-fdc2f951df64 | -12.19476 | -53.90951 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5731e860-d7f2-300c-a5f0-eee9839fe68a | -13.81344 | -46.28021 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ee2bfa7-88da-3100-b390-e04c4cdd6f5c | -9.4702 | -60.49199 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213e275d-94f5-3904-8a40-cd31289d66ff | -11.4527 | -49.2486 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3efaa434-acbb-32ed-9a2c-101630f45ff2 | -11.87168 | -50.96736 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a9ed219-fa4d-3bf2-a834-eaeba0d12e72 | -11.21173 | -55.00463 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 311b6c6e-712c-38f1-bc61-a4f8314a3555 | -14.29245 | -44.87078 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b48914d-ff77-36a8-97d5-800eb0e73c0c | -13.0077 | -45.21837 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbde4827-6e6d-3f09-842f-e2fabab9a62b | -13.821 | -46.24849 | 2025-09-08 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 234944b8-a9b3-3bc3-afed-3d24e941e74f | -15.09218 | -50.11644 | 2025-09-08 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fdd715f8-1d8b-348b-aff8-de2abe5350c7 | -11.91174 | -50.98455 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdf13db2-4faf-3b75-a87a-26e6c7c33b20 | -15.76033 | -53.54681 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd159279-3a87-31dd-af6c-fdb4845172ca | -12.8171 | -56.51664 | 2025-09-08 04:53:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 686f3377-14ba-3ebd-a2f1-b8a0819fb004 | -13.3571 | -44.43196 | 2025-09-08 04:53:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README67.md)
