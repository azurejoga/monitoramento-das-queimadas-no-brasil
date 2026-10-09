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

## Dados Diários - Página 219

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf3606a3-409d-3508-823d-34d4ae79fd6b | -4.30031 | -60.01355 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf50158e-4a10-3ad8-ab30-60cfb00b241d | -4.74546 | -55.65181 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ade92359-acf9-39a8-b137-b9acd71d47a5 | -5.69998 | -53.47978 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4815475b-2f20-395c-a768-a69727ee5886 | -5.09643 | -56.19538 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85af6698-b93a-35c2-b32f-b0703bc321a5 | -6.21774 | -52.88488 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77dc6dec-5584-3883-835e-d8dd62e2c757 | -12.21662 | -57.13005 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 735a2647-e720-3546-b25b-9e04511e401e | -4.73645 | -55.66267 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67fd62ca-0a8f-3c43-91f7-558488f2e660 | -5.70027 | -53.45984 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cada54d9-7914-3318-91c0-5a98740ddb08 | -6.47287 | -55.47908 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af5231d-3267-3d90-9e03-cf3375fe30e4 | -5.88003 | -53.52178 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c76509b-869f-38b4-87ac-4e8891306175 | -5.88988 | -57.72304 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6b9eb6ab-c4f2-3f42-97f0-5cce73033a33 | -6.23012 | -60.03662 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a419482d-51b7-34be-b692-32b89e7e59a6 | -12.21973 | -57.1085 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2de84ac9-8f8a-38c5-bc26-0c1525d28e33 | -6.39056 | -55.25843 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4271f374-6ef0-3738-80b2-5b51c5f04ff0 | -12.20881 | -57.1068 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d08c7011-b596-3116-a618-f532b7606b75 | -6.34035 | -59.94298 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf24ae0-02de-3ef2-afcc-7a8f09a1a170 | -6.49888 | -55.30957 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42be620b-4af8-3296-b9c7-e72c0efb5697 | -4.52034 | -61.12498 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d04031-44b4-39d8-9077-8e09dd08af3e | -5.92959 | -51.8337 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bba1e97-edc1-3986-a498-7a38327a29c9 | -5.37323 | -56.06492 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91a0cffb-ff0a-3f33-8e40-56954b36f353 | -5.70918 | -53.45711 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 170f76bd-9588-3445-80e0-55528e67d454 | -5.85984 | -53.45729 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25ce7be6-8135-37cd-b3bf-bb476506c356 | -10.3665 | -61.22277 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0af5a1d-3b96-37c3-a737-a860912d1fb1 | -4.02905 | -59.84279 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ab17673-a1db-38b1-aa4d-1fc9dd783c31 | -6.42426 | -54.96078 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26ca8a29-738e-31e5-a814-e389ea035dd3 | -12.42625 | -57.22808 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b83950d-3e1e-389e-8ccc-c04c223cb37a | -6.04996 | -59.91039 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a61164-56f0-30fc-ac49-5bbd7ae94503 | -11.76963 | -62.76755 | 2026-10-09 05:25:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3debaff-4d84-358b-87e8-db2265b95dfe | -7.18483 | -52.62971 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1c78b09-a16a-340f-b204-19b22f816524 | -4.29701 | -60.95306 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d291252-b91b-362f-95b3-e8c5c944f901 | -6.37818 | -56.22859 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b78e2ea-5216-383b-a860-afa5b6a69c84 | -4.7974 | -56.14105 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d392824d-bdd7-3084-afc3-cd34b58e69ee | -4.74537 | -55.67658 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6aa67bea-f14d-3edc-9fe7-4fe4f6d028de | -6.42225 | -55.20232 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a18ac75-4de7-3888-a8cb-2a5f4cad0148 | -5.95102 | -55.34724 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b70f405-fdb7-38b1-96c5-ff5108fc1c92 | -6.50791 | -55.40979 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37d64b1c-4163-3b14-a365-0364e4c93ea2 | -6.07165 | -59.88155 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0759fa70-ca72-3439-bcac-893e145c54d0 | -5.96012 | -55.36208 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d8ab44a-3a5b-3637-9831-c4fe129facdf | -6.45602 | -55.49007 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75bf4336-224a-3338-bf89-a2d2732e42c2 | -5.82444 | -57.74582 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ba5d0c6-3aa1-3ae2-9984-20133961587d | -6.13263 | -59.96706 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be31a304-859f-34ac-a749-d117990b4bef | -6.73132 | -48.11722 | 2026-10-09 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db344a30-a689-381c-9648-4d1c41c97042 | -5.99284 | -55.36108 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30ffeeb3-2d9a-33d6-b5a7-b02ef96180b7 | -6.8865 | -45.91413 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 64fa4f9b-e890-3691-b888-e3705907175a | -6.31966 | -54.80734 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e5fb100-b1a0-3fe5-b016-bf88437b0443 | -12.20764 | -57.089 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a565acb1-5ff0-30a5-83b2-c039063e08bf | -6.41243 | -55.19431 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6571c3a-a333-38af-9322-00ad4dff50d6 | -6.87834 | -45.92203 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1839fc39-f7ba-35ee-8b30-7d28c99d73bb | -4.19284 | -59.4109 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 019ed74a-1262-3f60-81d5-732a24a0c57f | -6.46984 | -55.47414 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e2b8b1-a51b-335a-bfc7-2372eaabc999 | -4.07695 | -59.83566 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feb72405-5dea-3951-9a9a-44e79b8f3b8f | -12.20809 | -57.13765 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56753a9d-9d13-3630-a346-85130859d660 | -4.07916 | -59.84328 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d623fa-7187-3898-8d63-fd472311eac6 | -17.82988 | -52.34362 | 2026-10-09 05:25:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57852ed5-bb93-3ef8-9f5b-5cb6388ccbae | -12.22586 | -57.0918 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c48f5d3d-8d74-36fa-852d-b54b3a79f9a1 | -6.72464 | -48.12083 | 2026-10-09 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8aa68d2f-0fdc-35d5-ac90-1c2c2dbf670c | -6.45972 | -55.49064 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaf91b51-34d1-3b4b-bb70-0c50e2dd3caf | -6.45313 | -55.04927 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c07626-9f1f-35fa-9b0a-8a4fbc13e0ee | -13.18066 | -54.3646 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b6b26da-d695-31b7-847e-61907e1d1633 | -6.12735 | -55.6837 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f995551-441d-3b2d-a143-f35aaa9f857d | -4.75691 | -55.64923 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4baa1cd0-3b37-3da4-98ca-b393c86fa621 | -6.50616 | -55.39583 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0df98952-fc4c-3011-aa0c-988b2765a6c2 | -4.12601 | -59.89445 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a262616-8a8e-35bc-b921-622d2183efcc | -13.16376 | -54.35778 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a2f53cf-4a0a-3efe-8114-2a18c4ca64b0 | -12.21252 | -57.08092 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| f9b4b4a6-75b4-350d-a4ef-fd718f1079f9 | -13.20193 | -54.37191 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f60c499a-d63f-3c78-9d72-05e9b2d8b9f6 | -6.01416 | -53.4893 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a757267-7a4d-3125-9123-d77e9922c868 | -6.09912 | -53.50177 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1204d1f-a511-389c-a207-a0b7bce31161 | -5.22934 | -60.23752 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec311510-e87e-3218-92c7-67f7841b1f1f | -4.07524 | -59.84629 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98d0f76a-bd76-3865-823c-df5355fd9bc3 | -5.931 | -51.82416 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d313a12a-991c-3807-8b96-053cf2e1e1a2 | -6.06621 | -53.60847 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c988976-428a-3f4e-8530-16519b8cb613 | -4.06541 | -59.83037 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7ae4898-4bc7-3e5d-96a7-2ce1e541ea24 | -6.12418 | -55.70496 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 412bf7fb-d1ee-3d95-b0f9-c18cc3c5a4a7 | -6.45244 | -55.05393 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a98c1d07-664e-3c24-8466-2503ded874dd | -6.48389 | -55.30733 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63eb7bb-b91d-332b-aa42-d23d374359c4 | -4.74599 | -55.67254 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12aec67d-b05f-3e5b-94f0-59ca7cf6b566 | -12.20996 | -57.12465 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35204a55-343e-3bc7-bd30-cd308bd2f19c | -6.18905 | -52.8679 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45e887e0-2793-385f-8a8d-091cb8aa79f3 | -6.1533 | -53.31275 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd8e573a-8555-362a-b0f9-2b72bf824dbe | -6.39278 | -55.19349 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34b89d53-1d3a-31c4-8e4f-31d4b069247e | -13.45583 | -61.11197 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 980e995d-22ee-3c26-9e27-7dd7ba11a64c | -7.09999 | -55.7291 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e55a0f22-64c0-33da-ab1e-4724cfc68511 | -5.6951 | -53.45594 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b00820c2-0758-3e4c-ae8a-f1877317aa4d | -6.72525 | -48.11635 | 2026-10-09 05:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb0034e4-30e0-35e3-9b85-fe9b500f09bd | -5.93309 | -51.82657 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee558936-ef99-357c-a7cb-0620cd9c046e | -7.61425 | -46.53961 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03c7e039-bef6-3da1-ba15-fb9ce23f2f1d | -4.7388 | -55.67138 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cc1f0b3-d409-39f7-96af-da84c6fa5577 | -5.27789 | -55.95654 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f04ab93-8682-37f3-9f8e-5e9dccc2da43 | -7.08282 | -52.68614 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffe34127-2891-38cc-9c77-dc93c096325c | -4.30517 | -60.94653 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19474a0-d699-333e-8d4d-1aa4b0b98a70 | -4.75737 | -55.67032 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3967826a-647f-37c6-9494-c270d891101f | -4.29293 | -60.95631 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0d8b28a-f7a4-3473-a841-d2eefc2554a8 | -12.19417 | -57.13113 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c74e5e-13c8-3811-8437-51039110cbe9 | -5.29866 | -60.10601 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac6b1fa-4e15-3626-81e5-8d09523c9b11 | -6.38532 | -56.2296 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49b184cf-73cd-39f8-abb7-8603dc074c9b | -4.74622 | -57.4812 | 2026-10-09 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dec02111-efe5-3354-bc7f-6eb1a7deaadb | -5.86752 | -57.75608 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a548c8ce-f368-3260-b6fe-4c96c7240edb | -6.00825 | -53.50023 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c54f9afd-48fb-3bb8-9485-6a0749e83e6c | -5.6975 | -53.46817 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README220.md)
