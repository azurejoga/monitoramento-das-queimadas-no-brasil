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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de2ecf51-64b5-3aa8-a68d-bb6dd95fa385 | -11.31193 | -54.47348 | 2026-07-05 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b47533ba-84fb-3449-99c1-0d4cb1f8284b | -8.05293 | -46.69982 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e99d39f-5a37-35c9-ab91-2bef45998125 | -13.22119 | -54.32785 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56d93434-3a12-354d-aae8-d86a4d53d9b5 | -11.66734 | -46.75073 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85571d16-c980-381e-98d3-7a2fc188706f | -11.43969 | -46.59542 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e27612d-7f63-30d5-ac6c-be9b12985fc3 | -9.26895 | -50.44856 | 2026-07-05 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 054e0f6c-2297-33ad-998b-7ce1d952b3fa | -6.98812 | -55.8923 | 2026-07-05 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 815961bb-c24f-3876-8745-12f65802ae4e | -11.4932 | -47.3688 | 2026-07-05 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23216a61-9d26-380d-89e5-f8edd8396011 | -11.94735 | -46.58794 | 2026-07-05 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7cd0b55-63ce-3e3f-96e0-de6a1736406e | -13.23881 | -54.33108 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adfaa248-582e-347e-8cba-ec51e5e67490 | -10.94076 | -43.0445 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8a37748f-6047-3dfd-848b-b78e542d2dac | -11.66349 | -46.75374 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5b7f807-77d0-3e20-a73f-eaa99ec855b6 | -8.31343 | -47.37919 | 2026-07-05 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b55e8fb8-6623-37df-bb6a-1cba10a9e04b | -6.98877 | -55.88865 | 2026-07-05 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5391650-f309-38b3-8c44-b0f011c9ca2d | -13.2344 | -54.3303 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a6a3bd2-9c26-306b-96cb-098c0627ed5b | -8.09196 | -46.70948 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1f6fe5c-460e-338a-8b91-b87e03c2d2ec | -11.52889 | -46.47908 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3997b04a-c93d-323b-9257-cec240e35251 | -11.71059 | -47.80634 | 2026-07-05 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202fa0de-5004-3680-bc6b-e74074a4d621 | -10.92935 | -43.04283 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fdd623e3-f3d4-3157-9168-e781db834efa | -13.2144 | -54.34011 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65476abb-2830-3817-8832-b22de4431afc | -9.63581 | -47.34482 | 2026-07-05 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1771c635-f093-3edf-9a77-840785fdd566 | -8.32177 | -45.38014 | 2026-07-05 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7f8df6e8-beb3-38a2-b180-4232c6fd9739 | -11.67158 | -50.3978 | 2026-07-05 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f98a815-1a9d-3e06-91c1-c08409919980 | -11.89148 | -43.83384 | 2026-07-05 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3cbefb3-1c1f-35d2-bfd0-d1a451a721c7 | -11.67306 | -50.39494 | 2026-07-05 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 892b04e0-c692-3650-8310-5318ba8bf30c | -13.24403 | -54.3274 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53ad2102-7f4b-3dc4-9457-a24781140b55 | -10.97558 | -48.12766 | 2026-07-05 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 312c7d80-7794-34df-892a-9706b1ec8dd9 | -8.08645 | -46.70153 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 207145ce-aac0-3487-b7c8-e4db2b40fef8 | -9.75047 | -48.18794 | 2026-07-05 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f96c590-e98d-36d1-b05e-2020b38348f4 | -13.2136 | -54.34451 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cf7963-d916-352e-be95-e9b375231b5c | -8.25033 | -48.03078 | 2026-07-05 04:27:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2337a8a-806a-37bd-b257-8194d3794a8e | -11.43799 | -46.58434 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13588180-b247-3cfd-91b5-6d8247690e66 | -11.89211 | -43.82944 | 2026-07-05 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a14b06b9-71b1-3b20-bcec-63f5a13849b3 | -13.19439 | -54.30038 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14a6d7ef-1d79-3581-bb6c-b36ea27066cf | -7.90119 | -48.25451 | 2026-07-05 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a214dfa-7bf0-32d4-8c7a-ccf637d6df29 | -13.20958 | -54.31667 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02cf59b5-f361-3da1-9530-7b8de52e9e1a | -11.8878 | -43.83328 | 2026-07-05 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5cb6ccc1-53b1-3032-9d89-3ac821cae381 | -10.78708 | -54.10535 | 2026-07-05 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 415402dc-7a8c-3665-b1df-5c6cf81d917a | -10.78626 | -54.10999 | 2026-07-05 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4bbf85f-531b-3beb-924f-f3ba305a5fa7 | -13.21679 | -54.32702 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8ba4048-8ff2-3ea1-ad2b-4f7888251ef2 | -10.90438 | -56.85469 | 2026-07-05 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76900ff1-8ec3-3b55-91b3-347d6d6d773a | -14.41755 | -44.59399 | 2026-07-05 04:27:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f78753d7-7bd3-3097-a395-70143be02d29 | -8.08813 | -46.71243 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8a1b760-c51d-38c3-8c96-3b8396bed18e | -11.67228 | -50.39368 | 2026-07-05 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4692b669-8829-3360-93bd-0f4bab1555a8 | -14.41728 | -44.59171 | 2026-07-05 04:27:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 003a8972-d903-3a73-87a3-52fc161b873f | -11.4899 | -47.36827 | 2026-07-05 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 109d4206-4733-34b4-9af6-e0caef5ee399 | -10.93003 | -43.03811 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 824fc46e-6769-3309-9fb7-5253dfb46f16 | -10.93764 | -43.03921 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ff9c1873-72c2-30fa-b4a0-f96ddb4476c7 | -10.61076 | -50.1188 | 2026-07-05 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21610474-c4c7-3cae-a2e1-4b4a44894e5b | -11.4572 | -46.54758 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f2a51f2-0aec-358b-8271-95563fd9b025 | -13.21961 | -54.33653 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c81d835-b16f-3e4b-be1a-5a0c390c37aa | -13.19798 | -54.30553 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30073ddf-38fa-3465-838c-b3720f9d8622 | -8.30404 | -47.35257 | 2026-07-05 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5b5f5d4-3c4e-3e8c-a464-0e84d0516c5e | -10.90303 | -56.86183 | 2026-07-05 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb074312-b92e-3550-afaf-08aff52549c2 | -15.08317 | -44.01607 | 2026-07-05 04:27:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dabcb485-2aab-3267-bec4-b1127bac8e06 | -13.2248 | -54.33303 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbf86f17-5b09-3e99-b782-12ee3781fa99 | -10.12101 | -52.0869 | 2026-07-05 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fcf4d6b-ef21-3a03-a7e3-20c4e99502b8 | -10.20168 | -54.95406 | 2026-07-05 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42a7bd58-aabc-3120-9d33-dad8fd35c137 | -13.23521 | -54.32586 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 184db068-e940-35fd-819b-c1f0abdcd396 | -10.93628 | -43.04866 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5000c2df-3bae-3495-b76e-abb88ff3ad66 | -11.01241 | -55.24514 | 2026-07-05 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e685bd0e-59a2-301d-98d3-6e2dd517f1d6 | -7.90915 | -48.24824 | 2026-07-05 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5f73701-bf2a-36b5-96eb-0a3fc1d6f4c8 | -9.39254 | -48.92038 | 2026-07-05 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89744167-a908-35e1-82a4-375ed2978a34 | -8.10922 | -47.12074 | 2026-07-05 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eab2c024-c743-384d-8605-7ca95846fd16 | -11.44023 | -46.5919 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c36470e7-0ee2-37ea-9045-fe892cc86155 | -7.38829 | -55.49166 | 2026-07-05 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e29e6df0-7b56-35d0-93d9-bf25cf1edfa0 | -13.22719 | -54.37001 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d22dbaad-29bb-30b9-8072-a95097c20264 | -8.94336 | -44.21116 | 2026-07-05 04:27:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ed4819d-c5cd-333a-b187-ef1919652fdc | -11.84316 | -49.1959 | 2026-07-05 04:27:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27c17f76-13e2-358a-9683-e9c0ecb9102d | -12.68419 | -48.21507 | 2026-07-05 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2834e3-828f-325d-a74e-a85f6157cd94 | -9.26837 | -50.44698 | 2026-07-05 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4002565d-ba68-38fc-8e94-7d25cccaae71 | -12.15108 | -44.98159 | 2026-07-05 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba2a7a9b-1bda-3bd6-b0e5-47b57e532a88 | -9.63857 | -47.34883 | 2026-07-05 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 931ee98f-9f62-3ea4-be5c-58920962a8ec | -10.97502 | -48.13121 | 2026-07-05 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a15d8f-78df-3ce7-8214-179231567606 | -8.91166 | -44.24732 | 2026-07-05 04:27:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd20f58f-b9be-3a0b-883b-548b2066ff72 | -11.66018 | -46.75321 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fd84e37-e53a-3f24-983e-227340e81014 | -11.43861 | -46.60246 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa4dbcec-2194-3bf2-8b83-89f2689214d7 | -7.90576 | -48.24769 | 2026-07-05 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee038f27-593d-36a6-b7e8-5e24c24060b2 | -10.93383 | -43.03867 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4b838799-f250-3526-aaae-664922b77a71 | -10.55886 | -48.03028 | 2026-07-05 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0eabd94-1af1-3a62-9e10-39f594497f6e | -11.91361 | -43.38268 | 2026-07-05 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebad0b41-4d77-31fb-984b-232a95af774b | -13.22199 | -54.32349 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54dfe4ab-8637-308b-930b-1a6fef4e28ab | -7.90178 | -48.25083 | 2026-07-05 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68c4d61c-023d-3ba2-bf3b-7b7b74bd0b99 | -12.55034 | -45.48048 | 2026-07-05 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af287cfd-1f81-3596-8676-3803ea54b07f | -13.2204 | -54.33219 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9de6d0-8cb8-3c33-b63f-eac419d2e0d3 | -13.21759 | -54.32268 | 2026-07-05 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6117b0f4-3531-353b-90a7-81f87f081f55 | -8.38506 | -46.90184 | 2026-07-05 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e7d9bef-d49a-3567-bd55-74ec96ca4abc | -15.2556 | -43.91592 | 2026-07-05 04:27:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fc4ac6b-9107-30c5-a690-6b613451b3bb | -10.92868 | -43.04755 | 2026-07-05 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ab806a9-1aad-3bae-a4b1-a3ca41e2aff1 | -11.44246 | -46.59948 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd752aa8-0375-3d46-8f7e-a62856d7ed8d | -8.72382 | -47.8388 | 2026-07-05 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cdd4598-5dd1-31ed-b916-7dc01ef6c3c9 | -11.44192 | -46.603 | 2026-07-05 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94227940-893d-3c51-a73f-53d035edb14c | -16.5266 | -47.73799 | 2026-07-05 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f959c82c-8d36-3c7c-b492-2b4016dc9b71 | -17.83334 | -41.96195 | 2026-07-05 04:29:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c943645d-9142-3e98-b840-837cb25bd0fb | -17.6236 | -42.28809 | 2026-07-05 04:29:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aa8e9997-34ca-318a-bcee-b07c998ee386 | -17.26535 | -49.0067 | 2026-07-05 04:29:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76d2fbfa-bdd9-31c1-882b-08446e7d3334 | -17.26866 | -49.00726 | 2026-07-05 04:29:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 02201dd9-2b0a-308e-a023-4c4baaee149e | -15.73145 | -47.75967 | 2026-07-05 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af0c901f-e5e5-3eed-aa4e-1148275adce7 | -19.25087 | -40.75572 | 2026-07-05 04:29:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ab019a74-2f43-3c41-9721-be8e04418990 | -16.04225 | -50.5612 | 2026-07-05 04:29:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
