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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa9dfe95-48a7-3d10-9120-dd902da90f35 | -14.18614 | -46.28178 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85b2171a-b722-33a8-b4a1-d2072876fb99 | -11.1805 | -55.08815 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7159c4b-6d03-3824-9d4a-5ad1b42f5bbe | -13.58539 | -44.88277 | 2025-09-13 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa331b94-b6bb-33dc-870d-9d8136840446 | -11.71633 | -56.88424 | 2025-09-13 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e942ff29-164d-3740-8a0f-b3db92df1a1c | -11.99972 | -47.76823 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0ec5154d-5764-3e56-b01b-f40b8fece516 | -9.88802 | -58.33197 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43e9f511-8837-3461-bf0d-0334ee39939d | -15.21276 | -56.68762 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a945b3f7-d01c-3f15-b925-cba56e8a896f | -10.76176 | -50.54586 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd97c9c7-d0d9-3c7d-979e-5e6d510d4eb4 | -12.91549 | -54.74693 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2dc04f1-9bcf-30a1-adfa-01309d5a4aff | -11.9951 | -47.7567 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 38989b97-0458-3f0a-b566-97716e810d2e | -15.07685 | -48.02326 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d14ef925-2ac2-3d14-a5cd-b7f150596172 | -11.41469 | -50.74285 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| ba6416f4-a0d5-3309-9a1a-cee82a93d8e2 | -15.78626 | -52.22987 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e41d9680-a5bf-3f80-85c9-f2a2c502cfb9 | -12.95347 | -48.00687 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 89404a50-be0b-32e0-97da-09600fd361ae | -11.4384 | -43.56071 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f7c01ca-d28d-3324-a9c8-4245d2ed15dd | -15.55432 | -54.79832 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1c349da-cf77-3780-af74-3e7c3079c3c1 | -14.46616 | -47.34204 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aed840d3-c2f0-3fa9-92d7-cbeb9a043187 | -11.58305 | -50.57064 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d8329894-0966-3ea6-a5cf-3db11550a07c | -11.82638 | -50.55199 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57f96ace-3f88-3982-922f-cf1287afc1c0 | -12.92884 | -54.74904 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17d4c1e9-8839-38e7-8911-5ad2311499d6 | -10.45631 | -50.60736 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33d4f430-5290-3925-9b5d-c3ed6b2904e3 | -14.18331 | -46.25807 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b0da9e76-eb56-3b0e-b6eb-6da3cd23cba4 | -9.90728 | -60.21216 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3d90b2-28fb-39f3-9dbb-0d84947d5a8a | -10.51321 | -51.54925 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 780f0c39-bf1c-311d-939d-c5dea69f464a | -11.84097 | -50.57861 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49639d22-0b6a-36cf-80e2-5834a67fe16d | -14.75051 | -55.61559 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0be0b711-27a3-3fa2-8959-9a7df267eaf9 | -10.15924 | -64.73001 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2592014c-f8ab-3dd5-8526-03d580fcac0e | -12.2697 | -53.91703 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74b4b7b3-f6c8-35b9-bcc2-92d3b76f1f40 | -15.15577 | -50.11843 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7eab2885-7d43-3154-b938-0198bcbc4930 | -11.87796 | -50.57681 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2cf76561-cfbe-3bb1-87d6-1d180e110890 | -12.91495 | -54.75052 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6eb62f1-0055-36f5-bdd3-a1edf803462f | -9.80276 | -61.51896 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3abea2b-fad7-3181-8a5b-3fd7e8a68b23 | -10.1611 | -64.73221 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 609b117d-13de-3006-8f3a-7b6bc16fd727 | -11.36152 | -43.50205 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d88608f-d00f-3866-b70c-bd8592809da5 | -11.80635 | -50.54908 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f0bb343-8625-3d23-99aa-0d3bfc3c56b0 | -10.50885 | -51.55334 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f797d171-6aa7-348e-a67a-2beda75d09b8 | -9.82348 | -54.53831 | 2025-09-13 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58a0ae66-ea60-36f3-961a-9bf897fc9f83 | -11.07446 | -51.43562 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95371549-24a3-3b1f-8872-530f83c1564b | -9.25556 | -57.06302 | 2025-09-13 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa98564d-b79f-3ee5-a89d-1cded725e212 | -11.74094 | -44.21397 | 2025-09-13 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42a7da8d-09e8-3c1d-8f07-d848cd488b87 | -10.7644 | -50.5221 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1e902a9-830b-3f5f-9d63-36aa9d8df672 | -10.32955 | -58.01865 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e41451df-95ee-376c-b6cc-37b1f8b9caf0 | -13.58488 | -44.88731 | 2025-09-13 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f2063350-8308-3057-8054-2f2407d80a1f | -15.78245 | -52.22927 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a345377f-7d63-31e8-b5aa-5a997c7f8524 | -12.66089 | -44.23801 | 2025-09-13 04:59:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb7d37d-d6e3-3d6c-91e2-00e9aa467a43 | -15.13971 | -52.46994 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c22e9a7a-1092-3769-abd0-5715cb2f3ba8 | -10.4203 | -50.60754 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfe19e91-8c1e-3647-b3b7-128b0b026642 | -14.17138 | -46.16681 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ee2c7fe-2a62-3d2d-9996-534c1242c64d | -10.35892 | -50.50238 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a73d917d-b467-3f09-b115-43a04bab65bf | -15.59681 | -54.75414 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2773ba55-43b9-3320-b68e-3f6915d27016 | -14.21761 | -46.25259 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b18a2e6-eda9-31b5-9d74-ab9ba24924c9 | -11.06479 | -51.50457 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76a3be90-3bea-38db-9880-fdb4e0cac339 | -14.21578 | -46.26797 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4f098d5-e13d-3944-a3ce-0dd570a016c1 | -13.15588 | -47.13749 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf78754b-2560-38d7-a785-3acf05ef317f | -15.12438 | -52.45971 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 826742b5-ffa1-3d6c-adbf-a5d8440184cf | -15.12065 | -52.45914 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5de6b39e-8e75-3a55-b322-6293ab1437ff | -10.90838 | -55.67426 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 626814c1-9882-3068-84ac-ecde2e37adab | -14.22359 | -46.29745 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b74e2381-95f2-3d4a-8422-30dc94f9be6d | -11.60361 | -52.22977 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76aa728f-5d5b-3134-8b68-5c11198b63ce | -15.77865 | -52.2287 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5aceb3d7-bbb3-3d6b-b395-86110363f1a5 | -14.4324 | -47.31671 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3aa8cf3d-e504-33e8-8e4a-5c78f9ae99ab | -11.8349 | -50.54962 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cd3f73cc-bb73-3e92-a205-e857b1dee577 | -9.27801 | -59.39672 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b47a8e3d-d7d6-37fd-97ba-9634200228a5 | -9.28721 | -60.18828 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8b12386-4738-3bbe-bb7e-5fc88799d12b | -15.06082 | -47.99477 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b95e3a4d-a5c4-3229-b376-e13728a18426 | -14.21394 | -46.28341 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3b56f65f-1690-3167-90fc-19e5b3e89ac4 | -15.12371 | -52.46441 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d437358-bd88-305c-8b9f-e5224776cc72 | -10.20068 | -58.22795 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8e88e71-8c29-39b0-8947-0f5dd958f4c7 | -10.72276 | -48.61438 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a760345a-4b97-37ff-8482-2496925ba8f2 | -9.27891 | -59.40434 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f849b6f5-31b9-32a6-90cb-a48262cb4e0f | -12.39588 | -43.82227 | 2025-09-13 04:59:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 842c7e59-9a5b-34ae-8f2b-da7ecb605329 | -14.21806 | -46.24876 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45fb1eaf-180e-30c8-986e-0ef6422bf1d0 | -10.70102 | -48.65528 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 163cbc50-bc03-3bf3-8ac5-188148741269 | -9.79505 | -57.44371 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7aca760-5031-3253-9dc9-43243e261c4e | -9.24039 | -60.4105 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adb57a9e-e5a4-30bf-a654-64ef08d9e722 | -15.27154 | -51.42583 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a4ffd6-9a34-3066-a86b-5ba72222ad5e | -15.16333 | -50.12818 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11f568c7-b03e-3ceb-a473-08adc2af6346 | -12.11502 | -47.59451 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 52a33983-1038-3468-8e80-a0fdd38c0976 | -11.82287 | -50.54787 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 27bcc12d-7022-3192-98c5-01687b55d1a3 | -16.30203 | -48.9126 | 2025-09-13 04:59:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67c25a1a-c364-31e1-91c5-fbe5e38b5668 | -11.10453 | -51.44011 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b9d1f3f1-7182-3641-b89d-cbad627b75b4 | -14.21483 | -46.27596 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 010b0008-feb3-3df0-912e-a0e7577a8c4a | -13.78106 | -46.29116 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d1e50a3-4bba-38b9-b8c3-9f52b8d8499b | -12.57734 | -45.66913 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf780a0c-2a0c-3703-9ee8-35984a422de1 | -11.99442 | -47.76221 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 389b6326-23e5-3f42-9a0c-1355ba921d67 | -10.20532 | -51.66722 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba6c2972-2919-3484-94ad-f14e9bacb82e | -15.37466 | -52.10564 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3275f59e-794a-361f-a302-c7513b68b2c1 | -12.57549 | -45.66688 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64ab28ac-ff78-34ae-9782-93ccc2a08da4 | -14.22526 | -46.28262 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bff133d2-8dd9-3da8-bd4f-ac677fae1a4c | -12.99476 | -46.73864 | 2025-09-13 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b51ad229-fa01-3b99-9248-5a15d08691a9 | -14.29246 | -46.08773 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ca57941f-7c67-3683-8731-0500439262ea | -14.41323 | -46.40092 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0d585e-c33b-3268-b191-78ff95d2af21 | -12.71988 | -45.07531 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cee51b95-5775-39a8-b9d7-2c75d140d1cb | -9.62705 | -64.17928 | 2025-09-13 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 473bad82-e464-3e0b-b0f9-239458fec65e | -11.88294 | -50.57031 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f86472f8-0652-375b-a055-04a39b2d73d4 | -10.75367 | -50.54154 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 906b9643-39f3-3e14-bd01-c18236c3d763 | -10.69812 | -54.44569 | 2025-09-13 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8178a05-cc80-3364-9aae-1277b4eddaf5 | -15.2155 | -56.69173 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e761022-6398-3792-ab3c-7509d70cf8d7 | -11.56214 | -50.57473 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c20a8b82-93f6-37b3-97a6-3cb6e8dce2bc | -11.36751 | -59.14095 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README90.md)
