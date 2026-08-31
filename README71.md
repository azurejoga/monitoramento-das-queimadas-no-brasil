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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d196aeab-e912-33e0-b7c1-b38ad59158c8 | -7.44207 | -61.42679 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dcfbbbd-4dec-3811-81e2-1f330f3fc3ec | -1.60148 | -54.4017 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81daf956-9d89-32d2-abec-fc72e9186069 | -7.30244 | -60.59456 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03e178bc-d105-3e50-8f40-5c33c1616432 | -5.25621 | -55.91438 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f59c35da-590b-307f-9561-e1a8800eece1 | -5.85721 | -57.55733 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a446e29-0b24-3f11-b458-1697ac107d35 | -7.30823 | -60.58634 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 328107f8-54e8-3bf9-b580-65a452cd7f21 | -5.87215 | -57.77782 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d03c5aa-1c3c-355f-a760-44938a1c0e7c | -7.3076 | -60.59076 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2860d6c0-aae8-3b09-8e35-5139bcc3eb71 | -6.08812 | -57.72428 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 226372f8-f0a6-36b6-8321-4970583acfde | -5.87651 | -57.78568 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa3d72b0-60aa-3776-be73-64cac536a80c | -5.57073 | -60.22824 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41141a7b-3bfb-3e4b-9bac-1e910dfc788b | -5.24757 | -55.91461 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2198f704-b112-307a-af38-01e8b8ade204 | -5.88806 | -59.98303 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efd20223-d936-327c-87f9-1b8e6faafc32 | -7.69117 | -63.33112 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29599ea8-d345-3823-a74e-ffccd12251e8 | -5.24419 | -55.89574 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| baada24e-6e51-39a0-9485-65cd1109579c | -1.60701 | -54.40737 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0eb21bb9-c34b-366e-8288-0e1ff485038c | -7.52937 | -55.32907 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d53595a-a490-3f08-90fb-6e2531f71034 | -7.52077 | -55.34446 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d93db9cc-581a-3b4a-9b0e-6773a7d6a235 | -5.57605 | -60.23488 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ecec6c2-1aae-39d2-a010-51f3a1f66db6 | 0.14518 | -60.40406 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 681e2df9-69c0-3992-b6cb-07a37cd77114 | -5.48218 | -57.14932 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934e10a5-98b7-3541-9de2-1816aa1bd3d5 | -5.48217 | -57.1548 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d345406-8055-3fd7-8a50-5d37b49217d3 | 0.14813 | -60.39617 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ed37522-df2f-380a-9ea0-592443ad6bdd | -6.76036 | -56.34015 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c8941f-6eff-37bd-9164-c4a48fd4da56 | -5.48776 | -57.14996 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e655b5e0-1847-37b7-b0b9-319f0bd57f9a | 0.14053 | -60.40106 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02755848-d29b-3eda-a42a-530359798be5 | -5.9469 | -57.69265 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f9f946e-ec13-33ef-9df6-8addbeb16540 | -7.69497 | -63.33168 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4985459-7481-3ede-a730-019db89b7787 | -5.24822 | -55.91018 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b9d63cf9-9f5f-3aa1-abe6-8549e9c33158 | -7.61942 | -55.29919 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b72d1c7-92e1-3607-82cb-ddf7ab40ab52 | -8.03407 | -61.25598 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edf0bcb4-c65f-31c4-a99b-e3e33458ca96 | -7.32565 | -60.59337 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca44f96b-6129-3239-a9dc-24293ff0b798 | -6.12302 | -57.67241 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b97a3621-ba1d-3bd3-b061-0e6961af1c02 | -7.58512 | -61.3381 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0d4c6a3-b3f1-3990-ad33-d073661cd618 | -6.60821 | -58.5976 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b5117e77-4226-36f5-ab78-f5bcddc9509c | -6.7768 | -55.63671 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a68c70d0-ecb1-3e03-9511-d3d44c38fe6d | -5.95328 | -57.68634 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cadda05-73fb-3250-9501-411f2101d4b1 | 1.52354 | -56.06314 | 2026-08-31 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b16f87-0cf1-3ab8-9ca5-7ad0f0c24024 | -6.90688 | -59.4913 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7490f1e-2134-3f52-bad3-87cdef613768 | -5.95915 | -57.68374 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1ed2013-c4c4-3b93-8ee0-d9192efb1b1e | -5.25016 | -55.91384 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6636b94e-11f1-3e2b-9e91-eef49b226a48 | -7.44147 | -61.43084 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945d1d36-4033-3371-8b13-3f58c511ce4b | -6.86628 | -59.47235 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e3c9a66f-0a00-3a9d-b9bf-f1b6d1ad0184 | -7.30696 | -60.59523 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3ecfa1-dd55-306e-8002-2d8a60e67bf9 | -6.78215 | -55.67873 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ec4bd31-50ee-3f15-80a0-f54846dd12e5 | -7.58569 | -61.3494 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b95c3a-81b1-3640-8a6b-ea0a16ed856a | -1.58808 | -54.40526 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44175d2c-b0b7-3c12-801f-9d42651744be | -5.24288 | -55.90471 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1d71bac5-eddb-3f19-86a6-402940a73b6e | -7.52867 | -55.33429 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd93ad6e-2255-3608-a556-6d73abd88897 | -7.30885 | -60.582 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e889109b-8a9e-33de-bdf8-0f985af2d92d | -6.775 | -55.637 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e047bd6-396e-347a-bea1-12790f2fc243 | -5.24541 | -55.90388 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d3c9b9d5-c7c8-38b8-a20a-e3ff47010d40 | -7.5236 | -55.32328 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 429f001d-1edf-316a-a67e-bac6087a3e2d | -7.91914 | -61.33993 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7178e8-1f28-3cd3-901b-05408eda6b0c | 0.00922 | -60.59667 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 422df32e-6cd5-3df1-b3bb-1584282df986 | -8.61072 | -54.77908 | 2026-08-31 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01b79709-5228-3eff-bc1b-64ed9cf8e6f1 | -6.93139 | -55.64017 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7334e92-beaf-3585-928d-ba5b543a508e | -7.52218 | -55.33394 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14fb9aaf-bbf3-35a3-9efa-03c4076b3b22 | -5.48989 | -57.1408 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8ca6f74-da43-3bca-ac90-9053587cfff0 | -6.8599 | -59.48223 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29fdabf6-9751-39ff-86c3-484e74191d0a | -5.95962 | -57.68039 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f46095d0-7c1c-3b6f-96cc-384ac1e475db | -6.15095 | -57.8825 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b88e034a-b720-3408-aabe-64a5e7146791 | -8.61148 | -54.77303 | 2026-08-31 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95014afb-c174-367a-af09-1fefd276b4d4 | -7.58512 | -61.35347 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba56b20a-4bf8-35ec-8cb3-c043310a23f8 | -6.94835 | -55.70247 | 2026-08-31 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b7780ba-7a23-3ab1-9765-342ad3bee05d | -7.92464 | -61.33226 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2019ea32-8e7c-315f-90a3-1b956cae4a28 | -7.30434 | -60.58131 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| afc9d90c-58fd-3d6d-81e5-8c261bc4ea12 | -5.48326 | -57.14733 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e94c6c07-d8a3-3400-b0d2-dc9125a2778d | -5.48883 | -57.14804 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faf508d4-9cea-3233-a6dd-b89fb945aa4e | -1.6007 | -54.40667 | 2026-08-31 05:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7672a386-c1be-3571-b022-7c4a4f37db65 | -6.60737 | -58.60366 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2757e134-4bc5-3827-9fcb-2c632e245233 | -5.57524 | -60.22889 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eec80af-c299-3474-97fa-3e74e41f0854 | -7.57766 | -61.34404 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5da014bc-7b9a-3185-adf2-3c28b8073538 | -5.9601 | -57.67691 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56ad533e-9d68-34c3-ae48-8c3725eb8325 | -7.34373 | -60.59587 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05d72cb3-a8dd-3560-9dd2-488fc1587b79 | -6.60224 | -58.60291 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 225f9df6-d4ae-3de9-b237-20d5a3c6efb3 | -7.51838 | -61.37413 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a86808a8-d160-3282-abf1-f989ca3ab098 | -6.56348 | -58.5621 | 2026-08-31 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecd298af-88e7-31b7-9272-87186fb33fe5 | -7.34307 | -60.60038 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f18ade80-804d-32c0-b39a-c3775610b027 | -7.79109 | -61.57502 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ee3f851-c496-3731-a04f-5ef3fd4a5bd8 | -6.89964 | -63.06211 | 2026-08-31 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66a9a79e-a2b0-35de-8ed3-f175a9047040 | -5.25078 | -55.90935 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c3de4eae-d42e-3ece-bcd2-d5fbfbb20730 | -5.95868 | -57.68713 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e52832ec-3953-3c78-affe-52b6dd7f92c3 | -7.31336 | -60.58268 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7aa3ddcf-3579-3867-af76-d9fae29789c9 | -7.33018 | -60.59398 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9274ab68-f005-3b2b-aadb-1909e1cffbe6 | -6.61486 | -66.33676 | 2026-08-31 05:53:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f84e2fc-c703-3f42-a00a-3e06c1696cdb | -5.49432 | -57.14358 | 2026-08-31 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79bdf338-ccad-3f50-b7f4-5f0b4727e076 | -6.66797 | -60.12668 | 2026-08-31 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e54197ad-8143-39e7-a4fd-483b8e6e7c20 | -5.24478 | -55.90844 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f340a380-8d13-3223-ad8d-a382a0312c5a | -5.2549 | -55.90641 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0a13e30e-d4a7-375e-a3e2-02b87d089eab | -5.94739 | -57.68916 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f012ab44-ba0a-3547-8f1b-027e4f8ed3a6 | -5.94504 | -57.6906 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b07d099-79e1-333c-990a-bc42f760a121 | -5.93915 | -57.69324 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ddd8d98-ecd7-326a-8d33-2c4ae4615cb8 | -1.40645 | -60.33207 | 2026-08-31 05:53:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b43c87ce-ef8d-354b-aeae-0a44faa71b08 | -5.31335 | -55.8574 | 2026-08-31 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c97944ec-f72b-3a52-a619-da63f051f3ef | -7.52209 | -61.37883 | 2026-08-31 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 267b96fe-1a0d-3fec-aae2-5e44ad4cb6b9 | -6.86477 | -59.47428 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e8658c7-b24d-31cd-a308-62c1bb007f1f | -7.621 | -57.61799 | 2026-08-31 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b863eb-dd56-31a6-9f79-3a0c1e22fac5 | 0.14109 | -60.40468 | 2026-08-31 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6570d67c-0c32-357b-a564-a4a294a126a6 | -7.33404 | -60.59909 | 2026-08-31 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README72.md)
