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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47136d5-1488-3912-9972-753692a43f70 | -4.4051 | -45.8105 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262fe52e-2d07-36fa-8c0c-e2ed76ad2665 | -4.40453 | -45.80798 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c699bbf1-8a58-3bb8-ace2-518f614226a4 | -4.38961 | -45.79539 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c7d9146-3be9-3f78-994f-cacaf0a42a85 | -4.3891 | -45.79882 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce39a793-6b38-3e3b-94d8-09b96dd81cbd | -4.38462 | -45.79126 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1f58944-e28b-3a96-8365-860dbc821a6a | -4.38411 | -45.79473 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55282fc6-c63b-39c2-bebf-9a071c9af79f | -4.05727 | -45.55884 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c65a061-205e-3eab-ad06-81530ee477f6 | -4.05675 | -45.56248 | 2024-10-17 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e3d2ff7-5f56-3b3a-8929-3378662a8376 | -4.05174 | -45.55798 | 2024-10-17 05:04:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8075afb8-6e91-30dd-99ba-c9826788b72c | -4.05121 | -45.56163 | 2024-10-17 05:04:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| bd55e9cd-c2cb-3ce4-97aa-d592af8b3b40 | -3.76968 | -45.74748 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| acf16d7b-2ba2-349c-a716-4bea6b0f6cb4 | -3.76633 | -45.74235 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 646d1679-2fa6-39e1-82c8-0cfb77b57aa4 | -3.76583 | -45.74589 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 53635352-023b-3c6e-8110-f2a77afe8c97 | -3.76533 | -45.74941 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3393b040-f045-3826-b2cf-d536b0b45037 | -3.7653 | -45.73958 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c927f61-e07f-3e19-b0ba-e09cb4107526 | -3.76484 | -45.75292 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| cd013cbd-2460-36cc-bb8e-7b3e79f4d59d | -3.76477 | -45.74312 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7095252d-2a97-3e5c-88b0-a392c2859903 | -3.76434 | -45.75643 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 4d477d12-afd3-331e-800b-ce0655d9a349 | -3.76425 | -45.74664 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9adcd1f7-5207-32b6-aee9-1b72e499c7be | -3.76384 | -45.75993 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3a36bd2-97f7-394e-b5ff-17a5cd33edde | -3.76372 | -45.75015 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dba004e1-36a0-3ffb-9dd2-2e93284f1fc5 | -3.7632 | -45.75364 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| acd01213-0b37-334a-bef0-13d912577680 | -3.76268 | -45.75715 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f979362f-392d-34d5-9260-5b3a7947c141 | -3.7614 | -45.7379 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d71ca487-5480-3c47-b657-49861f1788a1 | -3.7609 | -45.74146 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ebe3a87-3cfc-3c68-963f-8c681ab79158 | -3.7604 | -45.74501 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d1ba4b30-0f01-3a55-b781-caa55c9155ca | -3.75987 | -45.73868 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 882ee0b9-6f54-30c7-922e-56992f4bbd22 | -3.7594 | -45.75205 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 38f992c6-a77b-39d7-804a-d9b058b78754 | -3.75934 | -45.74222 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f36872c-fb8d-3502-94a4-a2f6e66c498d | -3.75891 | -45.75556 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f011a494-f17d-3914-9cac-d1380d0106c4 | -2.16389 | -48.40693 | 2024-10-17 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbaf6dc4-4a67-3045-a001-93ceecbc3739 | -3.75882 | -45.74575 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7bcaf2a7-92b9-34cc-8612-b552fd3d14a5 | -3.75841 | -45.75908 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 008c89a8-e468-3d41-a6c0-5fff13c301c8 | -3.75777 | -45.75278 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a90349c5-25ad-3f71-9f38-a55060cdc510 | -3.75725 | -45.75629 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 32f04072-5a88-35ab-b6da-e5eb0f8d9866 | -3.75338 | -45.74487 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8b12b3a6-a2ee-3861-abe0-132d3af27a19 | -3.75286 | -45.74839 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7f8f2dea-819f-3e25-83a4-4fbb85a9a60d | -3.75234 | -45.75191 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 507c9826-8c36-3057-8d0d-abd8d97b3c86 | -5.84863 | -46.24016 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03ea56ef-3b54-3f02-aecb-4bd6e9bdde4e | -5.84481 | -46.24027 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fd1e0b5-06d7-3c04-ba94-82f2e94be5c5 | -5.78847 | -46.19495 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 396e72d9-40ac-39f1-a996-ed2739291d68 | -5.78799 | -46.19841 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9db77ea5-5769-31bf-8038-17f1b96ddfc4 | -5.78307 | -46.19386 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f61d367-ddb8-3f76-ac71-e551a00ee763 | -5.7826 | -46.19727 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75effa73-7183-3b0e-83cc-4ec1c012c17a | -5.75083 | -46.50335 | 2024-10-17 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0448d3bb-82d7-3a4d-8720-5fd1c2e1a867 | -5.74552 | -46.50246 | 2024-10-17 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe0503e5-626e-36e7-827f-76920d301b19 | -5.98611 | -45.36847 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c667df04-4d0a-33d5-91cf-3ed49dda470b | -5.98556 | -45.37253 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 403e0f8c-2914-3cb8-b77b-ec82fa09c8ac | -5.98036 | -45.36754 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 0575175f-4cfb-34cb-8beb-32b58a73a068 | -5.97981 | -45.37159 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dc626146-f745-3575-9f54-0d830ec1a446 | -5.97944 | -45.36776 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 05f78bcf-383d-3dc3-9afd-a59c8e20804a | -5.97926 | -45.37563 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2112aae5-fee7-30a6-aed0-c0cb73005e6c | -5.97887 | -45.37179 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ae4df4ee-8ab7-357d-92ea-16bdcd66b372 | -5.97829 | -45.37582 | 2024-10-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b97c0500-f51e-311e-ba58-a79638b2f26c | -5.7069 | -45.77554 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 384549b1-f41a-374c-a10e-06f5fca5c71e | -5.70637 | -45.77926 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c700832-2278-389a-a139-7f8aa7272563 | -5.70573 | -45.77346 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4794b2d7-6f85-3733-9748-f74ca6d12212 | -5.70522 | -45.77721 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9f39717d-d71d-3a3c-9925-a55baaf617ba | -5.7013 | -45.77482 | 2024-10-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d1390b3-64b6-3cda-ad6d-ce5e3057c2ec | -5.16851 | -45.39432 | 2024-10-17 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b1b5f3c-7072-3e30-83dd-4174f6b7f73b | -5.16335 | -45.38974 | 2024-10-17 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae54fced-5de7-3a35-bc77-b08f45ad7398 | -5.16282 | -45.39351 | 2024-10-17 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d817e37-4e55-3255-8c43-95698a1b6e2f | -5.09494 | -45.83347 | 2024-10-17 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6fe8d54-03bc-3572-9551-3264be459c78 | -5.09441 | -45.83722 | 2024-10-17 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a1778786-6ce8-3da4-b0e6-26740608aa7d | -8.28686 | -45.98605 | 2024-10-17 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c84934ae-bd9c-3d3a-8dfa-756944b3a795 | -8.28118 | -45.98503 | 2024-10-17 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10619b14-1464-3166-a748-a5f2364197cd | -8.27602 | -45.97995 | 2024-10-17 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15435f8f-fb7e-3bc4-8d7a-e137fc24e574 | -8.27551 | -45.98387 | 2024-10-17 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 773bc8df-a02e-3208-85cf-7cedd75ecfaa | -1.54857 | -46.92473 | 2024-10-17 05:04:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73818b99-1c72-3153-8671-676458f2b0cd | -3.25098 | -46.87716 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 817b716b-4d7c-364e-bcbd-089568c70233 | -3.25055 | -46.88006 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b580686-157e-3600-b71b-292ad5c50e9c | -3.25011 | -46.88298 | 2024-10-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 656b25ce-f977-3229-86d4-2201c42d5fb3 | -2.37724 | -46.48554 | 2024-10-17 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c856d0-b782-3fb1-b70f-c5570461a8ca | -2.36665 | -46.48695 | 2024-10-17 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d707f888-a0ba-399e-9b14-2c80decb26d3 | -2.36539 | -46.48667 | 2024-10-17 05:04:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2269dc72-aa9f-39db-8df4-691d52218cc0 | -4.6604 | -46.29275 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae9f7f9-e036-33b5-9ac8-55b3c1522fb0 | -4.65942 | -46.29153 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e155189-5293-300b-be11-73eec0f016c0 | -4.6556 | -46.28849 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a18b687-ed75-3954-9909-7ac3b1d8cd0a | -4.65511 | -46.29179 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac2f58f0-5b7f-39d2-a7a0-03cc7abfdcd3 | -4.55638 | -46.67394 | 2024-10-17 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e4ce3a1-6ba5-35e3-8e19-6f8dbbd45d17 | -4.55594 | -46.67697 | 2024-10-17 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c422891-adb3-3c47-9318-dadaa993bc04 | -4.55166 | -46.67007 | 2024-10-17 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 967ef3a3-ff54-3ddc-b18b-d5025c130c6b | -4.55122 | -46.67314 | 2024-10-17 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37aea175-65be-3fed-8337-9ed15d3010c9 | -4.55077 | -46.67625 | 2024-10-17 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf7edd46-bff5-3b84-840c-927e564930c0 | -4.3621 | -46.81823 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1efe46ec-259d-389c-81d1-e11096af4fe9 | -4.36165 | -46.82122 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c5cb37f-7e47-3ceb-a49d-4dd427d41a26 | -4.36029 | -46.81752 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e79abd18-fab0-329f-a060-6aae0898ef9d | -4.35987 | -46.82052 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9694d66-70c3-3a72-8067-debfe87bd97e | -4.35698 | -46.81757 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68c526ff-938a-373c-b7a3-6c9fec64c170 | -4.35654 | -46.82053 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 914265ba-5fbc-3b8d-a7a9-20ee6755f4f0 | -4.20886 | -46.43871 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a64bb7-72ec-317c-87b7-add92f2787aa | -4.20839 | -46.44187 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c532025-d558-30a2-8bb6-bcf17d3e7102 | -4.20417 | -46.43869 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48f4ae00-d221-3ab7-bc35-1276f0c85564 | -4.20372 | -46.44189 | 2024-10-17 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddc69eda-6056-348e-8d86-502c2d4dedb6 | -3.95752 | -46.43173 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c45a9bb-eb16-3b38-b2eb-a18e2194d90f | -3.95703 | -46.43504 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7de2c05-8c33-3d3d-b8d0-f1cd0aacd3d3 | -3.91256 | -46.4482 | 2024-10-17 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a822cae9-e818-3f2d-a697-d365d7ba709c | -5.75036 | -46.50666 | 2024-10-17 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff83dfc3-918e-3c33-9d0e-c3f98c69507c | -2.14023 | -47.98626 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d6c4bc7-7fcd-3e77-838d-f67c81f78ad7 | -2.13954 | -47.99087 | 2024-10-17 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
