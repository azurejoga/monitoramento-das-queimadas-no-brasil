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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df4586ce-299a-399d-93ba-3d01c2481c94 | -14.1932 | -45.4603 | 2025-05-12 00:34:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0bb9992-b091-380a-9f87-482114ec5574 | -11.4074 | -52.942299 | 2025-05-12 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bab2c04-b2e1-3ba0-a518-4581a7503288 | -11.3945 | -52.93 | 2025-05-12 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a189297-ae78-329e-85b7-41c04d58e388 | -14.1959 | -45.471401 | 2025-05-12 00:34:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 498929a8-14ac-38b4-bd5d-6a8e1cb6d0aa | -13.0521 | -53.719299 | 2025-05-12 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5a030dd-227e-308a-aa73-82aa957018d4 | -13.0505 | -53.7113 | 2025-05-12 00:34:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 857995de-d9f1-33af-8a93-baea15ee9fc8 | -13.04745 | -53.72783 | 2025-05-12 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e064708c-949e-3e4d-aeaa-9a881dc005e8 | -11.91866 | -54.4072 | 2025-05-12 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b771a311-f639-3325-a668-329ea72b2e1a | -14.25262 | -54.55574 | 2025-05-12 01:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8424cf85-62fb-342c-8a74-ee546a6bedd9 | -12.17107 | -54.23686 | 2025-05-12 01:11:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5ee03a5c-a06d-34a5-a2e0-c660ece16079 | -13.05651 | -53.72639 | 2025-05-12 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8c8fd051-018e-36fc-9759-9d90f75f24eb | -13.04606 | -53.71829 | 2025-05-12 01:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3b9f1081-f629-3d4f-b8fe-6ae4a0712f60 | -11.40303 | -52.94902 | 2025-05-12 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3792030-949f-3c70-a59a-2a6272ec148f | -11.8938 | -56.41445 | 2025-05-12 01:13:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2e64fed5-e93b-34ed-816c-d7d5a3a98286 | -11.39188 | -52.93988 | 2025-05-12 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f73abe63-59d2-31c4-bb61-0779b986aea3 | -6.57689 | -51.11575 | 2025-05-12 01:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7a4f8285-359d-3224-9c35-7385fa9d397e | -13.0509 | -53.726799 | 2025-05-12 01:25:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 454c80ee-0313-330a-a3cc-8024226dba91 | -6.5917 | -51.124401 | 2025-05-12 01:25:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e2ee485-6f03-3785-8055-14428e66d36a | -9.3548 | -62.583302 | 2025-05-12 01:25:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 276a335e-1c47-31c3-8847-8e4a75727576 | -11.9065 | -56.412601 | 2025-05-12 01:25:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d2c6618-3f1d-3b14-80bf-83d983994e06 | -13.0606 | -53.7243 | 2025-05-12 01:25:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea9049eb-a7c2-3373-8dca-04c3279e48ed | -6.582 | -51.126801 | 2025-05-12 01:25:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec491544-7268-37f2-b1ba-a84b31d4de5a | -9.2496 | -40.2446 | 2025-05-12 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 33ee90b1-fada-312e-921e-59e05794e79c | -9.2492 | -40.2695 | 2025-05-12 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| a16cea34-bdfe-36a1-9bd7-35341ad4b443 | -4.91399 | -37.48487 | 2025-05-12 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ce24993-05e5-3af1-a602-2824c8617c15 | -8.25931 | -35.71185 | 2025-05-12 03:42:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63ed7dae-03b6-32c8-8543-d72a411d3ec7 | -5.06893 | -37.71641 | 2025-05-12 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bba88e20-f3b6-33c3-8134-de8c603ad403 | -8.94447 | -37.30931 | 2025-05-12 03:42:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7098f09-3939-336c-934c-d44a14a4ad3d | -4.91751 | -37.48542 | 2025-05-12 03:42:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 854308e3-70ad-35ef-8892-954651200db0 | -8.07454 | -34.97573 | 2025-05-12 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1aac9793-28ad-3959-a36e-329faff5875c | -5.16913 | -36.57144 | 2025-05-12 03:42:00 | NOAA-21 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b3a23dc-cec1-3357-9e4a-da9574f661d1 | -8.90551 | -44.7816 | 2025-05-12 03:42:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6bd7944-6b8b-325b-8bee-a60b76b41e0e | -8.90218 | -37.9603 | 2025-05-12 03:42:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 676ed083-838a-3816-920f-db9cbf0cc34a | -7.59335 | -45.85927 | 2025-05-12 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da0f03a8-ad4f-3389-9b45-05652c9650d2 | -8.25601 | -35.71134 | 2025-05-12 03:42:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8d329bf-d177-378f-92c5-02081b36405b | -7.47654 | -34.84229 | 2025-05-12 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3475c970-805b-377c-819d-559149b598e1 | -14.19614 | -45.46893 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dea4b4cb-f48f-3a37-8af1-328a10bd30cf | -16.68201 | -43.88451 | 2025-05-12 03:45:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7b6bbdc-d2e4-3f4e-a8ff-e3ff8c006303 | -14.20441 | -45.47979 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 263d203e-dc4f-3605-8631-f77d8affbb13 | -14.19172 | -45.46497 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5479477-cda1-3cc3-a613-ec60248224e7 | -17.09356 | -43.80582 | 2025-05-12 03:45:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36f77c09-8c7b-3a30-bde6-d131d97aa3b0 | -14.54953 | -49.11438 | 2025-05-12 03:45:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0729894a-87c5-3250-98ce-87d7887cb571 | -14.65594 | -45.1333 | 2025-05-12 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f43b3f2-d3bd-303e-87ed-359a8860fc19 | -14.20114 | -45.46988 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fea5b26-ee75-3bbc-b732-835d2ea28b17 | -14.19729 | -45.46297 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45277590-dda0-3ad6-816f-92ee47283a7e | -14.19672 | -45.46595 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1761f7a-52e2-3b51-8f33-00e7b4e3f5bd | -14.19058 | -45.47086 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65bf5d45-bfa6-3826-b77d-c5f714671555 | -17.7507 | -42.89527 | 2025-05-12 03:45:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35473b3c-2bab-36ba-aaaf-fddb55d91317 | -14.19999 | -45.47583 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcdee455-bf6b-378e-92f8-81d80d488482 | -14.20056 | -45.47285 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c9274cf-8a87-309b-86db-c992b6faed10 | -14.19115 | -45.46792 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97161d8e-f029-3bac-9f92-6aef6c1f4f19 | -14.19557 | -45.47189 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54587809-764b-3846-9f65-2ac4e6907b0e | -16.7018 | -42.34647 | 2025-05-12 03:45:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ebabe23-e568-321d-8a6a-af46b71bad27 | -14.20498 | -45.47682 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94677efc-c2e1-3e05-a485-32a384e74cd5 | -10.49075 | -46.18148 | 2025-05-12 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41690f84-e0b2-3630-9637-2ff54ccb2535 | -10.49148 | -46.17763 | 2025-05-12 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be6d6ecd-aed2-3b8c-9cd2-bc6d5b405d5e | -14.20556 | -45.47383 | 2025-05-12 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d042bb4-20cc-38d3-9ce7-4d53a51c7ddc | -20.17197 | -46.83517 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7067b61c-0b8d-36b1-9e1b-cde1e5b1d4f7 | -20.20353 | -46.72982 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32050751-8489-3fe2-84f6-9c9f7831bb9e | -20.17497 | -46.83298 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d1df092-ab4c-348b-ad06-17b385d101ce | -20.17372 | -46.83887 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 726da7d9-fee1-39cc-aa14-2fd26a8f9595 | -17.81508 | -50.92409 | 2025-05-12 03:47:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67385893-3962-3a75-85a9-48fc990b62c0 | -19.88357 | -43.96373 | 2025-05-12 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed8ff03f-ad73-3a9d-8826-4ccbb8db8e03 | -19.88508 | -43.96072 | 2025-05-12 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7f6652a-49ab-34f3-becd-62b324fbd302 | -19.43892 | -44.33966 | 2025-05-12 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5254cf9-fba7-3330-89a0-8862654b2e1e | -20.19648 | -46.73103 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b16912c6-cfc6-3a89-9940-3c429b780b69 | -20.20128 | -46.73223 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a92387db-b1e9-3379-99c1-8e5efe237ef7 | -19.41629 | -44.34345 | 2025-05-12 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e170da83-f3d4-368a-8061-0c0226182ffc | -20.19992 | -46.72272 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be5c1714-7f98-39da-8875-30d41de691a3 | -18.19534 | -45.60841 | 2025-05-12 03:47:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77c1ba20-f511-32d2-822a-091c548b58fd | -18.64898 | -40.58372 | 2025-05-12 03:47:00 | NOAA-21 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a9a030c-25df-33d7-8dbf-8bf6a598c6ea | -23.98074 | -48.91772 | 2025-05-12 03:47:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed161e5e-fd8c-34e8-801a-a76f9a774ed0 | -20.20245 | -46.72666 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13949fa6-1ede-374f-8a1f-8f66e56804bc | -20.19873 | -46.72858 | 2025-05-12 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1bb96449-77cf-3e8c-9b64-288b5a21ac55 | -23.98586 | -48.91897 | 2025-05-12 03:47:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0af0c99-6335-30cf-9368-e9440b033859 | -26.93558 | -48.75186 | 2025-05-12 03:49:00 | NOAA-21 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e6aeea7-4e53-35e3-8129-fd10142f993c | -8.07313 | -34.97417 | 2025-05-12 04:08:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2975761d-5e10-3e9a-8747-bcaf38be1c25 | -5.07107 | -37.71669 | 2025-05-12 04:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b282d100-bc69-32ad-a82b-f66afeeef795 | -7.59202 | -45.86174 | 2025-05-12 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7288b090-6d40-3df3-9806-17bc9afb3ca4 | -7.58822 | -45.8611 | 2025-05-12 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c249e43f-479c-3611-a32a-2283b5d101c1 | -8.25824 | -35.71133 | 2025-05-12 04:08:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a7083cf-72d3-3c3f-9b7c-75a88b5f1a01 | -4.91295 | -37.48808 | 2025-05-12 04:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aca5a50b-b8d5-3525-aa89-68a700bf0ae0 | -9.49238 | -40.34291 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e7258aa-dbe6-3ae3-90ca-346b2a54b78d | -14.19458 | -45.46994 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a48a6f0-58ce-3c2b-a04b-33949b999f4c | -14.2015 | -45.47114 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a7fc82-e3b0-3b8e-91b3-23b315c99f24 | -10.48885 | -46.17827 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c83f649c-a317-32f9-bf7b-42dd2cc6d3af | -10.48765 | -46.18019 | 2025-05-12 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2504c22a-f5f5-346a-b6d9-32914303e69d | -9.49468 | -40.35097 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dec46926-7bc0-34f3-8613-4e834404afd9 | -14.65991 | -45.13371 | 2025-05-12 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6211c417-c05b-3f32-bccc-1004c91c7138 | -13.04974 | -53.72031 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e216b4ef-e8ed-3b45-ac91-74da5f16bd7e | -13.04236 | -53.72712 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6d5d9fb-3736-39b8-99ee-c14314afebe5 | -15.07902 | -48.94614 | 2025-05-12 04:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574993de-e2d6-30d8-9a7c-395c94499a36 | -14.19869 | -45.46666 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0babeb9-c6f0-3e6d-984d-a9a32688755e | -9.49411 | -40.35472 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a82d0cca-37ab-3fa1-8fe2-e3c1269dd10d | -13.04318 | -53.72302 | 2025-05-12 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10a6c30c-c62e-3540-b863-2b0e26beda2f | -11.89639 | -56.4119 | 2025-05-12 04:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cbcd7be-60ca-320e-a5ef-8d160c2f70e7 | -14.19178 | -45.46546 | 2025-05-12 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb26c258-202f-3d2d-8ca9-8a0fd2dc0250 | -13.60659 | -47.97149 | 2025-05-12 04:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d092bf2-c7ae-3f74-821d-34de6b612de1 | -14.6565 | -45.13311 | 2025-05-12 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75ad6329-11f5-394b-bd0e-ca17e22ac293 | -9.49869 | -40.34774 | 2025-05-12 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
