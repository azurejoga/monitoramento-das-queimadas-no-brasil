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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0117dd62-aa1c-3385-a845-6965e97df822 | -3.57156 | -50.5544 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfaa38ff-af09-3394-b849-20a6bd61cfac | -3.57128 | -50.39465 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63522e22-8dad-3c4a-a063-83f700960384 | -3.57083 | -50.55874 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b93a06-a2ce-3a47-8d6e-b9477b2d83bf | -3.57046 | -50.56943 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63e4b4b1-0c48-3fd1-ac92-307236f89316 | -3.56976 | -50.57381 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b661ed72-e09c-3799-a33c-d0a0814093ad | -3.56906 | -50.57819 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca1aa4fb-a148-3634-8825-18517011bb9c | -3.56864 | -50.5718 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c821614a-6b2e-3573-aa4a-08c4e6e4264b | -3.56791 | -50.57617 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0dea1f2-1195-3c1f-bfbd-876e8901a794 | -3.56717 | -50.58054 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86211bc5-22d2-3c26-986d-24cb697baa41 | -3.56529 | -50.37585 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2339c027-6e91-3ca7-ae40-5f440df6c1db | -3.56461 | -50.5774 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82f129fa-eaf1-3f46-bdb7-9fc81dc23c63 | -3.5639 | -50.58179 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5c53668-4bca-3869-bb9c-cf6af9ae31c8 | -3.56346 | -50.5754 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64072d4-09c3-3670-a360-7eaded89d753 | -3.56272 | -50.57977 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 270d607f-aaa8-3b1a-83df-22894c49d338 | -3.56087 | -50.37521 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc448491-a63c-390b-9c5c-85662ac9ef2b | -3.56018 | -50.37946 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3ea6af8-a35a-3d9f-9fdb-4e3bc37482fd | -5.52676 | -50.5364 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbec94a5-88b3-3f3c-b765-c318b76f4f26 | -5.5249 | -50.53492 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dac5c05a-fc90-31c7-b12f-ad62a3ae0766 | -5.02393 | -50.76537 | 2024-09-28 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81fbd903-e8d2-3627-9109-1412fd18dfde | -5.97775 | -49.66523 | 2024-09-28 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f58f20c-805e-37e6-993b-5c7046015e13 | -5.51973 | -49.55508 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e8fc69-0be6-3c06-b67c-43f6a4804e78 | -7.81084 | -50.23299 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 824559d4-e015-3dca-acd9-e2769edb6022 | -7.76731 | -50.16967 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b3c9478-a9de-3786-8f84-331844d63cac | -7.76669 | -50.17326 | 2024-09-28 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be1e5ef-a64b-3250-94f0-6eff10456cef | -7.32706 | -50.04982 | 2024-09-28 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5960285a-881c-3054-b375-8a7726f97784 | -7.32646 | -50.0534 | 2024-09-28 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 901acde2-c515-370f-9f23-b3e8555354ed | -8.08418 | -51.02784 | 2024-09-28 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fe2d503-e1c8-326a-b616-1d149e5b77a7 | -8.07987 | -51.02732 | 2024-09-28 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 308abea2-9385-3386-8ef1-8b8618a6d3a9 | -8.07012 | -51.13458 | 2024-09-28 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b23e7a7c-f661-3bca-b8ff-b2feea367abb | -8.07003 | -51.10952 | 2024-09-28 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71329d24-ec3c-3fb4-b84d-d41bf84f0fda | -1.62307 | -50.53656 | 2024-09-28 04:19:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2d7c47c-4f59-3170-8855-d7011bac04a3 | -1.62266 | -50.53906 | 2024-09-28 04:19:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52abfcb6-a5cf-31c1-9800-9c1963b121a7 | -3.46829 | -51.36879 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ffe530f-62aa-3d24-bbdd-7dd346c94729 | -3.40945 | -51.24485 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2380548e-c17c-3310-bd46-ae3f51c9dc7a | -3.30203 | -50.66227 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d43c46dc-330e-3dd5-a3b2-dd634cdd733a | -3.3013 | -50.66678 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7580a6-bfd7-3efb-89a4-de2d48a07db1 | -3.19816 | -51.15427 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6df6828b-9289-3d33-beba-c4bed0bd59ec | -3.1943 | -51.14857 | 2024-09-28 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2667fc0-1851-3f19-8b6b-08a3a73a06ae | -3.10817 | -51.24922 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f32bebd2-4c8b-3aa8-8831-464f905ca8c2 | -3.09696 | -51.28854 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3af0dfbd-4651-3247-9dbb-a2f107379f19 | -3.07362 | -51.34246 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 298445e6-f91b-3cb7-ad2d-92fe41d0d22e | -3.01776 | -51.05037 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d80245be-7b65-3af5-87fe-85c9f38910f2 | -3.01697 | -51.05523 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d5e41ba-4ae7-3f6e-a46c-8cf7eba566e9 | -3.01618 | -51.0601 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3318394-0a98-32c2-97ea-a7dbe487fdb6 | -3.01538 | -51.06498 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46541b3e-21b3-3de8-9a8e-5f346345b230 | -3.0131 | -51.04964 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 84e709bb-ba34-3b12-8816-e06f7feba41d | -3.01231 | -51.05449 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53ec9551-d7de-33ce-a6c6-878ab8730af4 | -3.01152 | -51.05936 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5afadc9-2050-372e-b068-cb0fbdc5d82c | -2.58312 | -51.92284 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74253782-b997-32b8-b5dc-60e472112567 | -2.58267 | -51.92109 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fba3d82a-1078-38e7-9cda-c353bc40a7f7 | -2.58221 | -51.92397 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46413730-fae2-30bb-ac4b-da0838d4e909 | -2.39525 | -51.28236 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d079c858-8c10-37d1-be4b-4ef3311a68e4 | -2.39133 | -51.27646 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69c25d54-87e6-30bf-90aa-7f4b6e84dc24 | -2.39048 | -51.28159 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7739a3d8-0137-3379-bbf6-a149c0a12db1 | -2.96026 | -51.64892 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1993a7d5-e0d4-34dd-9778-22c8e63e48ca | -2.95858 | -51.65039 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8f587fd-f953-3ff4-8efd-20f29d360319 | -2.9554 | -51.64814 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e39d9f41-43f8-32ff-ad8d-dda15ff8a65b | -2.88523 | -51.38393 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 544be528-1c62-3016-87e2-35664807c997 | -2.88452 | -51.38563 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 489d9914-12bb-3ff4-8f2a-805bec505976 | -2.88119 | -51.67498 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c68ed96a-6777-3fe9-82fe-53a25f112f95 | -2.88059 | -51.37961 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96a06d48-9ec4-31ac-964d-f4ffa280b1c1 | -2.88047 | -51.3831 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 181d599e-1344-320a-97bd-06b77b62b2bb | -2.87976 | -51.3848 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cef5203e-e546-3501-99bf-a51036bfd177 | -2.8781 | -51.66349 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87a3c03c-33f9-386b-953f-3a2d0f271340 | -2.87722 | -51.66882 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4651a268-2b4f-3ad4-be0d-c3916e715193 | -2.87658 | -51.37714 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 773266c3-d62e-3ed4-9a99-045ede0f33cc | -2.87632 | -51.6742 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e69b0f6d-a5a6-3b1d-96b7-17906ad8e905 | -2.87582 | -51.37882 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a001213-0d7a-376b-82a2-36f62c1bf606 | -2.8757 | -51.38231 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f0344e2-ee3d-38ae-9fe7-2f057f46407a | -2.87543 | -51.6796 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 81128cc8-6c21-30d9-8b9c-6bc7eb73698e | -2.87499 | -51.384 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb902724-b7f8-3a84-8890-86031271c245 | -2.87235 | -51.66803 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7600f6c-5b7c-35a3-84b2-813a030f6a84 | -2.87145 | -51.67344 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9797e445-af59-3f27-b92b-f7be558c24e2 | -2.87056 | -51.67881 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| c6e9f4ba-ca7b-353b-bc15-71211a429399 | -2.86748 | -51.66728 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c4e3ed5-2335-3cac-87c8-2361f7f905a7 | -2.86351 | -51.66113 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3d60499-49f5-32a7-a646-dd1dbe5d8af7 | -2.85864 | -51.66039 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04977d24-487a-3ff9-ac60-2883fb45c47d | -2.82282 | -51.34392 | 2024-09-28 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba4b969e-9d3e-349f-8a10-39f4fea168af | -3.88212 | -51.90112 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 975269ce-7a0c-3e89-9128-41ea6fa77b7e | -3.88127 | -51.92487 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6d7084-60c9-3198-83a3-6d5ebdf7c4ea | -3.87861 | -51.92263 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6586aa7-8019-39f2-9578-ee187846cdfd | -3.87777 | -51.92781 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf421006-732a-3c4d-8751-4200279397ee | -3.87639 | -51.9241 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59343b05-6134-3fd7-b6c6-fcd619c59d89 | -3.87551 | -51.92929 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fc689b8-d362-32fe-8aaa-6b8c3874751b | -3.77584 | -51.85873 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96420dc7-e23a-3fcb-a1cb-4b93534a7e34 | -3.77481 | -51.85611 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf77fa1-92fb-3f03-9527-546ceb6a0ee3 | -3.77388 | -51.86154 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecfa8cbd-a76f-3c47-9458-c026bf2028bb | -3.77003 | -51.80296 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbfc63b7-79d5-3c53-b6f8-1400b35c4338 | -3.76519 | -51.80217 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e9f9895-2f8e-3b49-8830-5d526a8b5374 | -3.73434 | -51.80826 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2cfdc54-ce57-35eb-b2cd-ed4941f3341f | -3.64004 | -51.78535 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fab5292-8a84-3f70-9187-aff5fbe66363 | -3.63609 | -51.7792 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8164f11f-a8bf-30b6-8aa1-f68878b5804d | -3.63519 | -51.78458 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3970b969-0272-32e4-8dd1-da4ca8a4f414 | -3.60916 | -51.7914 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cab1455-1ced-34eb-a989-ff04ea76d809 | -3.60826 | -51.79681 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbd2b795-3feb-312b-bc8b-bfc2eb9950f9 | -3.57266 | -52.1301 | 2024-09-28 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fb1133b-2849-335f-b098-ccade4444448 | -4.60278 | -50.95479 | 2024-09-28 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a5dc794-d9e6-385f-9988-ab05386316de | -6.14534 | -51.25197 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f06bfdc0-7e52-39a1-8b60-deb186a7f395 | -6.14083 | -51.25142 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a5ac15d-096c-30b5-864c-192a7ec9ae30 | -6.13561 | -51.2551 | 2024-09-28 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
