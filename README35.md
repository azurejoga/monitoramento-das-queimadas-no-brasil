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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e1df6b8-6e71-3b65-983f-cb074cff2629 | -3.65613 | -50.25594 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2922ca1c-bd42-3adf-bf31-a17218c3db14 | -3.48609 | -52.09981 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14addbd9-1f19-3a3b-9a82-7428ade3d7c4 | -3.12002 | -51.10869 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 496f2e3b-4241-396c-a135-89b6dfbe5838 | -2.82804 | -48.46384 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6cef04b-0162-340d-a8e8-9b2f4e6afc33 | -2.74018 | -54.12298 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38dbf4d8-9551-321e-9019-c402d62629d1 | -3.11863 | -54.25165 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47bc625d-8b9a-335b-bdf8-6c0b4d318643 | -2.85743 | -49.22882 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 610febda-cb28-373a-b31c-7c92bac0e2cb | -3.1054 | -50.29888 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa2fc126-447e-3d3b-bef1-bcf4337c4030 | -3.96188 | -48.14597 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9b262c-cd14-3eb5-b07a-3a4371f2dbaa | -2.81299 | -51.48849 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a477d5f-d783-3c56-8583-c5ef3ebb87ff | -2.01337 | -46.80629 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2faa21e-d91f-3b65-a4a4-c13b547e5cc1 | -2.96007 | -51.06157 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1da0d11b-6065-37c9-b138-40bacc153041 | -2.03169 | -53.58041 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e881e8f-a6df-3664-82a7-35f3a675ea48 | -2.89994 | -50.70734 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc457148-8f4e-3d23-a8ea-814a8cb08709 | -4.35913 | -48.64753 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42679ae0-1e77-329f-892c-d65cbde25deb | -3.83333 | -45.95834 | 2024-11-06 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d983b541-1845-33a5-9651-332de769a702 | -4.05398 | -48.25242 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ecfefbd-807a-3ef5-873f-30e9044660e3 | -3.21808 | -50.38345 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0618ccb9-2fbf-3690-8def-10a56e0db827 | -3.53717 | -51.15243 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7a27635-5d0b-3ec7-b031-3c056373b2f1 | -4.95426 | -47.59299 | 2024-11-06 04:36:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fb4b551-9ef2-3530-a1d9-87f6cee8dcc1 | -2.49848 | -49.11235 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c13866b-66cd-35f9-93a9-d4dd14d9264c | -3.0529 | -51.07089 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a79ad9d2-fbc3-308a-a6b5-90643244a0a0 | -3.25002 | -53.40785 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7e46d4a-d014-3231-96b7-bd39bd7017e6 | -4.41994 | -45.47548 | 2024-11-06 04:36:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2dcac72-4a17-3250-ac85-1d7af47fdf19 | -4.36152 | -45.76313 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f48ff0-7a7d-36ba-be24-acb98a07d66a | -2.39623 | -46.16986 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86d7f1a6-b158-3543-b8f0-5be045cf72e0 | -2.51229 | -47.46708 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fcdf2ab-7cb1-374c-b45c-24b98dc2550e | -2.84585 | -49.23763 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19f9db16-caaa-367a-be7e-cb91ab63089f | -4.44178 | -50.97924 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e670c0d-72c9-3c1e-82a0-e6033f5e2a29 | -2.75879 | -53.21314 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3a2e26b-3e69-3c61-b140-e45d0252175c | -2.7902 | -51.35884 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec40be8a-773b-3857-a2c9-6238d70996c6 | -3.58965 | -50.27163 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54cba9d4-0336-31f8-aa8f-0e68090e8019 | -2.08454 | -52.29603 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d53f3cf-5a1a-3491-abbe-1e4540211521 | -2.40172 | -50.3098 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a8cac57-a59e-3b5c-9680-fcd86bd43095 | -2.7893 | -51.61285 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69925b1-75c3-346f-835d-ab77c431ec65 | -2.58246 | -51.87029 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7636d219-216c-3774-937f-c36021a1d0a2 | -2.59999 | -51.30193 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098798a9-93b6-3877-bf18-aac20ebaad3c | -4.34752 | -48.63514 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1bb1fe-f8da-3cf3-90ac-1c1fccbe18ec | -4.27568 | -50.72311 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99e078ee-16eb-3e70-b0a8-faf250dfb011 | -2.49094 | -49.18192 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b80fa914-d82f-3258-84c7-ee8c96ba7302 | -1.48787 | -60.38182 | 2024-11-06 04:36:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a76f897-9443-34a7-b3b1-c44619e3cff4 | -3.55958 | -51.50972 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 80ba315d-781d-3668-b063-86c9b4fed74b | -2.64869 | -48.56944 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83812acd-f14b-3e01-bbaf-4d5e8284da0c | -5.27514 | -47.28221 | 2024-11-06 04:36:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969e25ac-b4b3-342b-8064-d7ad51c38e6c | -3.97682 | -48.13734 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8abc8a-39ee-3eff-a763-02d71703c9fc | -2.07416 | -47.05886 | 2024-11-06 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07dc5854-0ffe-350f-a289-f852e89c8c3b | -3.05985 | -49.36715 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f424112-8b07-3177-b39e-97beb7751dd8 | -4.35213 | -45.89831 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2acad63c-03d3-3b75-8354-bec7bd16144d | -2.8245 | -52.95431 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 93e679ca-38f8-31f7-9840-4aca189ee49b | -4.07842 | -48.31305 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7a8d910-f483-3dd1-bcb4-aaf38653e15e | -6.05287 | -39.43814 | 2024-11-06 04:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e9df3b06-c8c8-3b99-a87c-6f332c7e6345 | -2.8242 | -48.46676 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 772e984b-95ac-3fcc-9aa6-19bb8c9f347b | -2.89477 | -49.40135 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0112c51b-e804-39cd-adbc-6b03921ac4d3 | -3.22146 | -50.38398 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 391ae006-fb65-3235-b51a-103a541f3988 | -3.05116 | -47.69362 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95feebd-37f3-33c2-aa6c-e7fa5a6c6506 | -3.96917 | -48.16463 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a61b8e9d-d794-3b2e-902a-346fcc88d624 | -2.23187 | -50.69727 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de51a104-b89d-36a3-99d9-2227f179b2f2 | -2.5818 | -51.87448 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d8b4b8-75f6-34fc-980e-3a233d0d0303 | -3.10383 | -50.26537 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa78c2d-d708-3008-8bc5-9b3339062e9d | -2.79656 | -51.47756 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e92b40c-33a0-3f33-b9ae-4289ecefea8a | -3.08488 | -54.50855 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8193a68-91e4-308a-9f44-729abd83db65 | -2.74519 | -49.14406 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265b7fdf-8ed4-329a-bf63-fbb9aa941f93 | -3.97187 | -48.14727 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f850756f-1d6c-344d-a005-2322ac2fab1d | -2.7405 | -46.07423 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb45c479-1425-3143-8908-711e86869296 | -2.92017 | -51.04346 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 43a26106-6c42-3434-ad83-d62ee01dc76d | -2.74683 | -49.13372 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a233fe4-571b-3894-8220-7b31dea56364 | -3.14489 | -51.19969 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59b112ac-27a4-3401-a286-ded6bfb8a8ca | -2.65242 | -46.74963 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b607478-de6a-3ffd-98d0-1cb30aecca0a | -3.7465 | -51.31463 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57bb7e12-9724-307c-b49b-70544198411d | -5.90787 | -42.9073 | 2024-11-06 04:36:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 531f6cdb-8e15-3069-ad62-75328164fd0e | -2.81605 | -52.95782 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 712155e7-cb55-35a1-8fab-83b51f3a3cbe | -2.83065 | -52.91608 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b21f8fe-57ca-3227-9105-8bfb8caa52f3 | -4.22355 | -50.62888 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc5c59c-80cc-3c6b-ae55-b52b6452b7c2 | -2.90324 | -49.23951 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0671246-567a-3beb-a4d9-4017c1b8dc13 | -2.89467 | -49.3587 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d9496a6-d631-38b5-9e92-06e922089119 | -3.99991 | -43.25219 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f212f64-ed69-3cc5-8b9c-cf57059c6b0d | -3.04071 | -49.53134 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdba1d53-470b-3656-b07a-ab16fd87a14f | -2.63438 | -51.72906 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 271c23a5-9e19-3f6a-a69f-e432ee12eb8d | -2.88809 | -49.37898 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63602345-e712-37b7-a472-a81a106e0a17 | -3.03139 | -53.26644 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7a7e6d6-49e3-3406-bf11-ee53af85cceb | -3.10054 | -50.24271 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1d3bde1-18a6-3427-84f5-7361b28cf8a8 | -2.34566 | -48.89796 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882e73e4-3454-37bb-9f7f-9173e6d75690 | -3.89139 | -50.25271 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec1781e7-0f74-374a-983f-0170872d4773 | -2.81911 | -52.9144 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7dbfc014-ed6e-3716-9d9b-615478ed2fcc | -1.86178 | -54.70182 | 2024-11-06 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00b3c427-bee7-3ca9-a87c-dc8bdc3b1e13 | -4.27228 | -50.72257 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9615263a-edfd-3c8f-b098-602388db962b | -3.03061 | -53.27137 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 68b21ed9-9aad-3db8-b188-97a1c09e3d94 | -4.26255 | -53.53168 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ff4c0c-18ff-38a7-aaa3-1f3ce35395dd | -4.13012 | -48.87215 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddc53dd6-c116-3a0e-b36a-046bee04cd52 | -3.95672 | -45.76671 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcc6e9ec-ec12-3ce7-a952-fc417741d0df | -4.18966 | -51.01983 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac500b02-99cf-3cc6-a64d-ecb94a6a1c1b | -5.55422 | -43.69952 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5708902a-0244-38d8-a4d5-47353d335787 | -2.64194 | -51.75147 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f573a733-759d-3e8b-a7b3-e10b3ca4c1ac | -3.86086 | -50.19295 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbad18fb-44aa-39a2-8003-4dc18f08b0d0 | -3.0908 | -53.7126 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 978131b6-938a-3326-ad14-76807457304f | -2.34187 | -48.92202 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a17e3b7e-6006-3fb9-930c-be4c873f36ed | -3.95802 | -48.14892 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d15e778f-2861-3245-9256-ebbead8bb82f | -2.84697 | -51.78158 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d7b264d9-cfcd-38eb-bac8-8f83364dd88a | -2.87263 | -49.39078 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a0af2d-ab7a-3652-b3ed-0db92bf695cc | -3.06962 | -50.98743 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
