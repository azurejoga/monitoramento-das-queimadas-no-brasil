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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa0b49f5-6c4c-39d0-a4d2-26bf5b8ff823 | -9.46146 | -60.51729 | 2025-09-06 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c92673d6-acda-3571-8eee-15db581ca0de | -8.35358 | -52.54445 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d07df6de-44c1-3cd2-8fa2-9a6b6eb1ca0d | -9.06801 | -62.35421 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbce38ab-4655-381e-9386-173a90138797 | -5.00865 | -56.03351 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fa94e6c-b5f4-3f00-9669-3cbdc495878c | -8.3683 | -52.56473 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 30bbc6b5-7399-305e-a9f7-53c7b8e15d6c | -8.06068 | -52.38352 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1d60936d-f618-3d2a-aca0-eae245fe8a54 | -6.69113 | -63.12897 | 2025-09-06 05:29:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ff1acc-932d-3e62-8527-4c02173f0398 | -10.47245 | -53.62322 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 512e926b-0923-3a6b-a429-fd199df7d4b8 | -8.47921 | -62.64222 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 822ff1d9-4552-37f1-939e-dd653f2438e0 | -5.78327 | -57.55217 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1739d71-56a9-3318-b5b4-6b1bcfe778a9 | -6.85028 | -52.8057 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51c45a22-35b5-37f5-86b3-6cd2e91d9c2f | -9.46495 | -60.51783 | 2025-09-06 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9eb7c3a-07bc-3665-9bbe-d3dcbb98023f | -6.16322 | -53.68902 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df71c5bc-a130-383c-86bd-4b410a6c7e1a | -7.79224 | -52.12868 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0985679-035f-3929-bdda-6d61eac8b0ed | -5.90057 | -57.73363 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fb9d1565-7f7a-33b6-ad94-33743c381631 | -7.72036 | -61.52522 | 2025-09-06 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65385be0-bc99-399a-bd86-c839d230dd2f | -7.79808 | -52.13072 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 778f900e-ac58-3191-bc1a-ead77b8bf437 | -6.27978 | -53.43378 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc59093-ab26-3766-9464-baaf3f8a1b23 | -6.62866 | -53.15695 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce4e267-fb65-3a9e-89ed-2f62fa1d3373 | -9.9754 | -51.65525 | 2025-09-06 05:29:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4f4a60bf-38f9-33ff-b79a-47f5b2422d51 | -9.21245 | -57.09645 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f534788-cb86-3451-96de-05d9bd2a8aad | -6.86423 | -52.78602 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de297236-1a74-32c8-bf49-6bee607b35af | -6.54049 | -49.50314 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edc959d3-e985-39bb-a894-faadfa53147c | -10.13873 | -55.16225 | 2025-09-06 05:29:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68e5fb80-7029-370a-8d54-41fe8a78d155 | -8.70849 | -62.39023 | 2025-09-06 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9134a60-2994-3e68-8d5b-652b92a8fdfd | -5.14934 | -60.31384 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5e16a76-e129-327f-bd3f-e4e671dda953 | -5.92488 | -51.99931 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 443d436b-0802-3625-a98b-2b956f784459 | -6.53971 | -49.50927 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4c8312b-5bc9-388a-9248-2bd297118777 | -7.38805 | -59.66196 | 2025-09-06 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3baa55ad-8b7e-3b5e-99ea-f0287299badf | -6.18722 | -53.25077 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20fba928-d19d-3507-958b-8424e69095e4 | -6.26948 | -52.81281 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20f05b09-3871-3355-9beb-0fa95003d436 | -8.06553 | -52.39096 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1d3a2f9d-76d3-326b-8a65-7b05692a7fbc | -10.13946 | -55.15673 | 2025-09-06 05:29:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bbdd93e8-4748-3070-b3c2-58b4acccf58e | -6.27368 | -53.4394 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12143de0-8a25-3208-86f4-d40b857c93ad | -6.46407 | -55.88793 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b39e91f5-4e33-31d0-9c69-7c95c57a8e03 | -6.26758 | -53.44507 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c04f3a2e-ded2-328e-ae96-97c5262cf159 | -10.46791 | -53.61523 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08f2ae30-077b-3dc2-a622-4b53b412a52e | -4.99779 | -56.25893 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e2efc11-3953-3226-9ada-201af74e59af | -6.27845 | -53.44338 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c125023e-ea32-3ce4-9e12-8e7ab5e47659 | -4.86723 | -50.8286 | 2025-09-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dc22b43-e142-3891-baae-58e06585742a | -6.26846 | -53.43863 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80de4def-bb0c-355c-aeab-447a0d527518 | -9.07133 | -62.35474 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0851de4-dda8-3e9e-885a-b9877840907d | -5.94857 | -53.79728 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 247f6bb3-feb4-3f29-a5c2-9f5aab49da35 | -5.4858 | -60.13124 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171a9d9f-3c9f-34c9-a21e-d029107b6a57 | -5.94985 | -53.78832 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc9d466-ac14-3f32-a674-def801e15022 | -6.27456 | -53.433 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 007645e8-02ad-3efa-96a4-890440b86493 | -5.78718 | -57.55275 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313a42ea-a304-3acb-a7f9-a9e394de18d0 | -9.46553 | -60.51392 | 2025-09-06 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861c4231-bfab-3be7-a728-b70d2a859846 | -9.20821 | -57.09585 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289e8de8-2fb4-3e50-90ea-9a1b70456a99 | -6.40287 | -55.55802 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707888a8-63b3-3822-8c13-f59b000a4086 | -6.42099 | -58.03744 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a9178ad-cf68-3515-9e16-ed8dafd17fc7 | -10.47561 | -53.64186 | 2025-09-06 05:29:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78b823c6-5c35-3a05-b1d7-ef4b00985bff | -5.97204 | -53.59644 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a14862a4-f572-39e3-99f5-5a8d1e91f95f | -7.42621 | -63.06415 | 2025-09-06 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e223fc-81e9-3600-b53a-321f9a89d97f | -5.9013 | -57.72871 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3f012e3-bac5-3650-a3b2-8fe2d128796b | -5.49376 | -60.12487 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b9e940d-aa10-3a43-9598-791d0970784f | -5.95534 | -53.78608 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19941098-2f0c-348e-867c-bdce41764c94 | -8.92959 | -62.41458 | 2025-09-06 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9da9adea-3f54-3793-847c-f941178d0eab | -9.11606 | -61.48751 | 2025-09-06 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ce11de-45a4-3a76-a953-6adca3f9c1c5 | -9.25078 | -57.06993 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbc6eab3-db39-31ae-9f65-411b3a1565b5 | -6.18679 | -53.25391 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4716c3ef-7148-36fd-9926-0f348a75321c | -6.16407 | -53.68294 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b2b03c4-0703-3a25-b8b7-8c358de92f1a | -4.64076 | -56.09761 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc36a01f-9e01-3e02-b65f-26c4d6f8d0d2 | -5.98189 | -53.60081 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a33f0ce0-971a-3051-82f8-bdae701b5959 | -6.32695 | -58.17261 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19becaa1-fbad-36dc-b26a-01d0dabc7ed8 | -5.9587 | -53.79868 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c37b3b65-10ed-39d3-8814-6c83c589a314 | -4.89344 | -55.99279 | 2025-09-06 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b46392b-bf39-3f5c-8e2c-193501e265a5 | -6.82137 | -52.81249 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbe28f7b-d7f4-36ad-b7b3-7af4caee4f8d | -6.28499 | -53.43453 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4709cc12-0870-34e4-8bbd-7b6d2eae002a | -6.1801 | -53.2634 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a38655-ccb2-32ea-9fbe-6c1394c7170e | -9.20875 | -57.09194 | 2025-09-06 05:29:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a5ed6eb-c89d-3416-a500-980b5faa05a5 | -6.28367 | -53.44407 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb94ff9d-c024-39c7-9008-272312abdf05 | -7.73111 | -63.33089 | 2025-09-06 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d3ef2e6-0ee1-3d80-ba9a-c44ae1bbfbd6 | -6.18586 | -53.26062 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6292b49-c2dd-3da2-8489-1faa01d5937e | -6.26585 | -53.45764 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d16254f7-97dc-3e50-ae8f-f2bb921e91d0 | -10.14363 | -55.16294 | 2025-09-06 05:29:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5daf54a3-bbce-3b93-bf09-7144551f1ff4 | -6.27878 | -55.95639 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c849a5da-9c71-3c4f-a8d4-6006f13eeed1 | -10.22426 | -50.53045 | 2025-09-06 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd3ac807-5545-3f44-a09f-073617a23df7 | -6.8713 | -52.77968 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a098f54-0957-3c95-bb6c-8a8dae209c83 | -5.98744 | -53.59865 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f48b2ba4-908a-3398-8a14-f4b389ec5ab9 | -5.50575 | -60.1381 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc0992d6-51dd-3385-94ef-6135f926b801 | -5.49207 | -60.136 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba081672-6594-37c9-bcfc-22e63da14ca1 | -6.44057 | -57.77363 | 2025-09-06 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6d2aaed-7dbf-3361-b0d5-1801521f0d9e | -6.54352 | -49.51089 | 2025-09-06 05:29:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1e5f644-c23d-347b-8483-81a3dd5df46f | -7.71811 | -61.51764 | 2025-09-06 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b08a057e-0811-3bb3-8ae2-818bf58ffe96 | -7.38527 | -50.90934 | 2025-09-06 05:29:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5cc574e4-7bab-34e0-9de2-2a59b54f942d | -10.22492 | -50.52459 | 2025-09-06 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c046410-e04d-3ead-9489-69ed79c0d6ea | -5.98319 | -53.59179 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64575aa6-860e-3d66-8eae-dce9fcde87dd | -6.82185 | -52.80906 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6c436e6-570f-35dd-abb3-7c0cec705d3f | -6.81039 | -52.81107 | 2025-09-06 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72778635-563d-3c67-8315-07426a01f532 | -5.50459 | -60.12273 | 2025-09-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f26ea9fe-61e8-32fc-b18e-0e7b7c722c8e | -6.40739 | -55.5587 | 2025-09-06 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc69439-8fcf-3c6f-827e-5e5e5b66f79e | -6.26671 | -53.45139 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66a8f79f-61f1-39e1-9697-6346f13ac038 | -7.3867 | -56.68906 | 2025-09-06 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 774f3617-c338-34c7-ada4-aab2b9a47ba5 | -10.21969 | -50.53058 | 2025-09-06 05:29:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88f7edea-697a-35fe-88b3-346bdea62f1c | -5.96691 | -53.59564 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57b0abd4-9258-3ecf-993d-a9593c51326c | -6.27933 | -53.43701 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ac74c35-beb7-37ec-aa28-75eb0b9b1339 | -4.50394 | -42.88723 | 2025-09-06 05:29:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e7245877-ff72-3247-acfd-1efd61bb4d2b | -6.275 | -53.42978 | 2025-09-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349cdc4a-e1a6-3b3d-9d09-2dd5653982f0 | -7.76068 | -50.74128 | 2025-09-06 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README81.md)
