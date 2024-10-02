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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f60c34e0-01f6-3b85-a3c7-fb17d5e67171 | -10.39186 | -67.95632 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bb1d1db-50fa-3aea-96bd-f6ea1db35c70 | -10.3369 | -67.74891 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a61ec798-6eb7-3abe-962d-be7e30a67dd3 | -10.33619 | -67.75313 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bc3d10b3-9543-3206-b9cb-37ea14b3c4d5 | -10.33042 | -67.76521 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a11881b1-c4dc-31f1-9c15-a3417cec9408 | -10.32681 | -67.7646 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 668049c2-85c0-3ceb-a9e7-88be98a47a99 | -10.32636 | -67.7614 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98fcbd87-86b9-39b9-8169-1d9730a3a9ef | -10.32609 | -67.76883 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e1f0b2-589a-3514-a2ec-0da76bab36cd | -10.32566 | -67.76564 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7343a602-79e5-329f-a20b-46e708a34ff5 | -10.32173 | -67.7507 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9a459d6-d6df-3949-b4e9-16cb89b585a0 | -10.32134 | -67.76929 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfd0b94-c60b-33a4-bbff-e45a38f50652 | -10.321 | -67.75494 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d40c334-0416-3bb7-ab95-0e161ef342f9 | -10.32051 | -67.75172 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b11bfee-1162-38ae-865c-a6a3d7c4de14 | -10.31981 | -67.75596 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e543c217-7839-358f-aea8-756bc205f8ce | -10.31956 | -67.76343 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e35a9cd-aabe-3159-8542-63cdc08c7da7 | -10.31884 | -67.76765 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5eb6d56-4bb3-3dd2-839b-e8935712230c | -10.31842 | -67.76446 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f75b9927-4589-3d3e-83dc-3c7cfcf1c670 | -10.31812 | -67.77189 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6b31203-bf7d-316f-82b1-d44758dbf80d | -10.31772 | -67.76869 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fe6b148-d430-3867-a5ec-60809dab7427 | -10.31702 | -67.77294 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69cba8f7-d424-34d4-bca6-ec6369c2c452 | -10.3141 | -67.76808 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a88f84a-75ef-3cf8-ac99-3e79d50a5f88 | -10.13891 | -67.89896 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cce7193-b288-3150-a6d5-0b37a4a79c12 | -10.13454 | -67.90265 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1544881-40d1-311e-90d9-374ec18ad2e1 | -10.13161 | -67.8977 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e08658d-2730-3230-a52c-2a8c355ae163 | -10.13089 | -67.90202 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e954d2eb-039d-301a-a4ac-9b016050218d | -10.12723 | -67.9014 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c6fc3e9-e3bf-33da-b4dc-5d2e956ef93c | -10.11044 | -67.88962 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eebf93c4-beb0-3fa5-a13b-1b807d41a986 | -10.10971 | -67.89394 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f965052f-9224-32e0-97ca-9148bf6fdad6 | -10.10606 | -67.89333 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7bc753-dbc0-3600-ab77-32786aad844c | -10.10241 | -67.89272 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c274f91-68b8-333d-8e23-d66f38a73ebf | -10.10097 | -67.85696 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e444906b-a516-35a3-920e-942adfa459bf | -10.09805 | -67.85207 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f2e805c-1889-3dfe-ab71-a459747c15b1 | -10.09368 | -67.85573 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1ab71da-5625-35f4-bb10-783d2cd89a12 | -10.54805 | -68.42443 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19848e11-15df-38be-8b0c-af5cc66f5a2f | -10.48332 | -68.39188 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58eb2b82-bb81-3b28-9e30-d6eb60b0c7bc | -10.47959 | -68.39124 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 552c25bf-76ca-3aad-833d-c17ff6c69f2b | -10.45431 | -68.24804 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dc7ba17-9dc0-3673-bada-360741613607 | -10.45272 | -68.2448 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7be80c15-4bfc-3156-a24c-eb1d6c037390 | -10.42846 | -68.02751 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2047a808-2a7a-3ae9-9801-d8d4d9b59834 | -10.42772 | -68.03189 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58a019d3-5137-34f5-9d7a-fa255b8a007e | -10.41 | -68.11444 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a667a303-0769-3b02-81f6-9c098695ed6e | -10.40925 | -68.11884 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b93b97a0-62a4-3f55-8d5c-ea7878d92530 | -10.40632 | -68.11382 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa0f69a-bc3d-379d-8ae3-cb03ab03de76 | -10.40557 | -68.11822 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec5bd97-c431-3ec7-b312-a1426b2f1287 | -10.38711 | -68.1377 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfd93b28-1aab-3db7-b151-5e52d7303d0d | -10.38544 | -67.99519 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91041914-6e78-32c5-be12-27fae0d5a020 | -10.38472 | -67.99953 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab89e01c-bc01-35d5-98bd-c86a007a7ee7 | -10.38386 | -68.22378 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1544382-0ee6-3e38-9b90-df14b041d8b7 | -10.38363 | -68.06931 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50d28e9d-ae1d-3829-ba66-7114e56bc4af | -10.38311 | -68.22822 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d652d9b-5c7f-399e-b2a7-4489496c9de9 | -10.38109 | -68.17301 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95711811-9676-3d58-9d77-e0da324c844e | -10.35034 | -68.00261 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b408d0-bdff-3b00-8eba-274d2f88c6fd | -10.30936 | -67.99995 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b03a6a-e4f3-3a1c-9552-494ef872cc11 | -10.30493 | -68.02605 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29f94aca-e922-3b99-8443-def35ca6acd2 | -10.27482 | -68.76978 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d9016bf-9a79-36e7-af3c-84c4aec68d9a | -10.27182 | -68.76435 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d2893ac-25f9-3afd-84c0-f2935bca74e7 | -10.271 | -68.76912 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 617175a5-e3c5-3116-b96b-a0523e8fd9ec | -10.26989 | -68.76196 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e6be1b-75e8-3d54-9451-d79f1ceaa59b | -10.2691 | -68.76673 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9706981-1e55-3e21-8592-90fa83171fce | -10.268 | -68.76369 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 398f4ab5-db5d-3cdf-95fe-c0e44ffd2787 | -10.26528 | -68.76607 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d0647b-5c67-3fd0-a800-0ca63affe910 | -10.2583 | -68.01504 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78846fa-20b6-34ca-82d4-817b92dc1579 | -10.25758 | -68.0194 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 312c383c-61a7-310d-b8c8-660db74a3745 | -10.21847 | -68.30052 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f834bd3-89f8-3c00-946e-5b8a2ec5d576 | -10.21475 | -68.29988 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f2574c-d5e6-3259-aeaa-c9e3ebe7cfee | -10.12372 | -68.406 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1463d0e5-5319-344c-8901-175cc7c2af45 | -10.11997 | -68.40533 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cadf2b-63e3-3425-a140-4632886d6e4e | -10.11919 | -68.40988 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe054fe4-bfda-3ee4-94e5-9975116881a3 | -10.97759 | -68.45801 | 2024-10-02 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73fb7402-4050-31e2-8673-e78cdeea5559 | -10.90585 | -68.28671 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f5377a8-ce86-3753-a305-458daa044901 | -10.87658 | -68.21944 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b4571c5-c20c-375a-a740-105c79f388e1 | -13.58996 | -51.13261 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8338c04b-9d2f-307f-8d75-d6e44e5883fd | -13.58775 | -51.12939 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eae38861-b850-3363-b3f9-e93c80430e93 | -13.58697 | -51.13663 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b2295f33-878f-36a7-8db2-181f65dbd969 | -13.58277 | -51.13183 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acd29541-23b2-3bcd-bc59-7e90ac2020df | -13.58204 | -51.1391 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 31ca3b6b-1979-3ba9-aa4a-a7bf7ed7aea2 | -13.55852 | -51.19938 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 386fd456-b8e2-3115-9941-a3569f5e08df | -13.55777 | -51.20654 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c8ba12a-2529-37b7-9073-2918f1565c29 | -13.55472 | -51.19464 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30f60505-f10b-33c5-8ac0-79c8d9ad91bf | -13.55401 | -51.20184 | 2024-10-02 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e40ea703-b5fc-3d87-a5bf-374f61f107ce | -13.2115 | -51.20438 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 71e24343-189e-364c-b385-71cb4a8d3beb | -13.21079 | -51.21158 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 113c00a0-d982-342a-997f-4d5d2ec98209 | -13.20791 | -51.20275 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90fc4504-204c-3b51-9994-3080dc516499 | -13.20716 | -51.20989 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4489b91b-ddd3-3147-ae2b-bada611bb463 | -13.02508 | -51.15712 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a3f82a4-268d-327a-bae7-40e113e24313 | -13.02188 | -51.15401 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d854b2cb-5db4-396c-af57-65a1d111c777 | -13.02116 | -51.16115 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 605e5b07-a2b9-31ab-ac52-353b8849eae8 | -13.01794 | -51.15635 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 826439d7-f4e8-3b18-a188-52c94ce994d0 | -13.01717 | -51.16347 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ecf5c6dc-e29d-3f38-95bd-988ca4269deb | -12.99878 | -51.13263 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e928dd83-7975-311e-b61f-4a8611bdfac7 | -12.99802 | -51.13977 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd89b4b-2f54-31f3-b572-314c546ebda7 | -13.1806 | -51.25705 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 51e30f08-54d6-34e1-a7bd-51f052b48bf6 | -13.17422 | -51.24921 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0108ae50-66f2-3639-babc-326752d7587e | -13.17348 | -51.25628 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7b0d3487-cc4f-3210-8e0e-ec041bbe1bfb | -13.1671 | -51.24844 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c5a3ee9-85f0-35fd-bb12-e4faea54cbea | -13.16072 | -51.24059 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 279b36cb-08b3-3210-b43e-077195eeead9 | -13.15999 | -51.24764 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6fded3fb-ab90-311e-9546-8fc60a664a0b | -13.15702 | -51.24055 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6cb17ee1-2e52-38ae-9247-a27babc644f8 | -13.15624 | -51.2476 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e955ec33-9ae4-307e-bb2f-eeed1a3bf277 | -13.1536 | -51.23978 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b7bb1b08-0bf6-3791-b6ef-de6886e9b947 | -13.15287 | -51.24685 | 2024-10-02 05:36:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README174.md)
