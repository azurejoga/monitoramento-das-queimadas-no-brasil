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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4df3b93-6441-3bf3-8184-3bcfe878a5eb | -3.27203 | -50.20612 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 19a33149-6d95-3292-8276-711fceedb586 | -2.35467 | -54.58469 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de3e224a-ffa8-3fdf-9bf7-e8e5c187422d | -3.33843 | -53.36964 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44cf7314-5283-334c-91c0-a0bece5b8da3 | -1.32605 | -55.67038 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b705165-356f-3dbc-b77a-5af0283e6a7c | -4.5512 | -45.71874 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4d66a81-4aea-38a5-bce4-b54f510eaf4f | -3.28119 | -53.34918 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffef4bf5-d768-36ec-bbc8-1363acd64739 | -3.69175 | -51.0887 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea7f7cac-4670-3da6-8d57-9d0f078b0d8f | -3.33714 | -53.37799 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d45b6e-3546-34dd-8b65-e49ef5d94e8c | -2.53197 | -54.04897 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98e80ad8-4301-36ad-a31d-10553f5ddef1 | -2.98702 | -53.3455 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25ebb24-7fb6-3e82-b76a-12c8e16a8fcf | -1.44 | -55.22649 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad74e6a5-5b22-37f3-ab9c-094967b50c20 | -1.35666 | -55.15275 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fe4a368-47bf-33b7-a11f-bf2f67eacc69 | -2.80727 | -53.05405 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 845338eb-99c9-3c9f-9611-27ef063518a4 | -1.66869 | -52.50237 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aa92a81-fddc-3a28-bb5f-97431da4232d | -1.4367 | -55.24745 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a09734c1-143e-3d57-b025-0a4b043be913 | -3.21338 | -54.1773 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09bf3521-f931-3599-9d3b-e57f5a446ddf | -2.8663 | -53.9915 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0620fa2d-1d00-33ce-a824-7b29ebf2b592 | -3.84372 | -59.57901 | 2024-12-01 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 866bbca3-ffe4-3678-be98-00a62045f6f1 | -1.94656 | -53.34121 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78b939fe-a79c-322b-ae53-b07a48fd80ff | -2.98509 | -53.90144 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5c3cbd2-a45d-334d-9245-027a3b3e3341 | -3.71619 | -51.06891 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de4da6c3-eaf1-304b-a59c-1ffd4d4a4658 | -1.70458 | -52.46698 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 376f34f6-a5d4-35d5-9526-4a693391009d | -2.62441 | -54.22233 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0700628f-af7e-3359-9d50-1f1dcf107146 | -3.11802 | -53.8117 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e46f0355-1930-328e-a8aa-7b3c99843514 | -2.79768 | -54.05752 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99722cf7-678a-3303-8f52-7ab8eb036e9a | -6.86554 | -47.24508 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb0ca006-f658-3047-bbe7-7f2806b49c76 | -1.64188 | -55.06393 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b4d3a1a-eab8-33a9-8751-b39e5f10e59e | -2.77167 | -55.35332 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da414783-1a84-34eb-bccc-88f464f860da | -2.68357 | -51.72949 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a0b373a-f5a6-3e55-9f62-ab78e1360b86 | -6.28951 | -43.84976 | 2024-12-01 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d9101dcc-c4d8-3b25-9d53-a542f1220aee | -1.50022 | -52.60677 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aac1b81c-070b-31fc-898a-e4f0b8cdc9cc | -3.15976 | -53.2422 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 410745d6-805c-325b-94b1-ed8d10fab7f3 | -3.3324 | -50.22284 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92fd327a-45b1-35c5-bfc8-2cf3b02ed512 | -2.53084 | -54.03315 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c101b0b-c7c4-3469-8d17-a27de985dfd5 | -1.56507 | -53.8329 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6b584c4-320c-3774-b764-5da30c166dbf | -1.50044 | -54.9516 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b81403-a4d8-3a2a-9d90-9bd0f24af951 | -2.8692 | -53.99591 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50c1207b-0bb1-348d-a057-7df1786f8b1e | -2.63361 | -54.23145 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ad1edc-d6ed-3938-ac8b-6995f9ebc272 | -3.5234 | -62.84851 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69145885-3ad4-393e-bb52-328d11391467 | -3.09271 | -50.34721 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd8ead0-9771-3e0a-84cf-d8ac309f8302 | -4.48846 | -48.21839 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b01e4ada-ed8c-3784-a789-a910d0c8209a | -3.2648 | -51.62505 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42145e90-fc5b-3d2c-b59d-d5a4f642517f | -2.6343 | -46.88422 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cb36bd4-4057-39b2-bb55-a334a1fceb35 | -3.17649 | -54.32359 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32687bc0-c8d7-3683-91eb-44bb70cd2ea0 | -3.11449 | -53.81111 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f255114-404f-3b4b-93f4-47cdecb3bcf6 | -1.65806 | -53.22143 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b1573d8-620d-3a0f-a4e6-50c70f65e5fd | -3.0376 | -50.23946 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfb681aa-41e5-3fd4-ae91-3213b7548749 | -2.34775 | -53.92799 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0ce713e-fbc7-38ac-8209-4a2a0c785fa3 | -4.19389 | -50.68429 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39ab04c7-15c1-33da-9fe7-f0be41b947fa | -2.75769 | -55.33314 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc27abe3-0086-32b3-8383-b1c6edffc0dd | -3.76249 | -50.17854 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96b757c1-3161-3650-8f96-487704c208eb | -2.81114 | -54.03987 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ba870dc-3d52-3aac-83f4-4d965eca8cf4 | -1.26191 | -60.28979 | 2024-12-01 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd621730-8b48-3eac-aba8-f4762a2e0a71 | -2.52439 | -54.07515 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe058e8-48cd-31b5-8f1b-5166c9f391a9 | -2.88796 | -53.96702 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e635c17-ebe1-353f-88e9-8185da9b2137 | -2.76658 | -51.69024 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4953e5be-9934-3e96-bd53-7b5d8ce6ed79 | -2.84662 | -54.04134 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5327a0bb-926d-3f4c-a4dc-b1c711701e5e | -2.62362 | -46.95866 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4419be29-bbfb-3cdd-b811-bd9f6b646e25 | -3.07873 | -54.56972 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f690373-df4e-3926-b333-13ca5908db22 | -3.47933 | -53.81523 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55bf3f5e-4339-32c3-b71e-52c1acbb9d69 | -4.03517 | -46.93197 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c138bfbe-ee04-33f1-baa0-20bf81847710 | -3.65459 | -54.17866 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d723cafc-3f98-3921-9365-bddd74f95dd2 | -1.6293 | -53.86572 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c16ec90-c6f9-35d6-ac4e-11f329d15ed5 | -2.69147 | -51.73071 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86865fe6-1dbd-3409-8cd2-52cbc4a91040 | -2.82978 | -54.03481 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa506e1-2418-3bb9-b633-3d73cc6c79df | -1.30957 | -55.68899 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb86885-32b2-3f2e-99c7-509f5e314d12 | -2.76827 | -55.33117 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa2e9198-86a9-328b-b8b6-441685a9b8d3 | -3.1067 | -53.27288 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 287a38ba-4606-302e-9acf-c105cdd88cbb | -2.87294 | -51.82878 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16498a2b-f446-3f03-93a8-ad96be7ba998 | -4.18586 | -50.67876 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f6fbbf0-c235-3663-9f7d-c6afe6779a08 | -3.0112 | -51.78957 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c7b3ca3d-55c4-345d-9472-a61b372364cb | -2.83465 | -54.10506 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5efff60-3004-3fad-b6c0-35cc899f0236 | -4.31215 | -48.20943 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e49410-b5d0-33ef-9be8-b81f11843834 | -2.97438 | -53.89631 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b5489f0-c76e-32ee-8e1f-5021224659b9 | -4.24887 | -54.81686 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33667c61-176e-3c1b-abb1-d83f299aa594 | -1.19791 | -53.86857 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 341253e2-7754-3aca-8e32-ebc84cd99f9f | -2.63191 | -54.21957 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5630e1c3-e1f9-31c4-b3b6-18b8e7822e45 | -2.84931 | -54.03244 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d13edcdd-b949-3ba3-b4ee-51eb832d3d90 | -6.86802 | -47.24005 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01d34160-0efe-3a00-bd6b-cce5a4136551 | -2.84274 | -54.12198 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43b1dca0-e8ae-309e-915a-4e6b1dc89a29 | -1.8967 | -53.01459 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fe90d2a-298b-3a23-aba7-cf3a7d7022d5 | -2.82476 | -53.90649 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b3b925-e1c1-30aa-bf14-f6a717df2a52 | -2.76887 | -55.34929 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70db58f0-1328-3c75-89fa-6978a152a826 | -3.24754 | -53.6507 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c2344bf-cad3-3430-95f5-4d8fab8e5b97 | -3.17936 | -54.32793 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fadef2d-b8a8-32dd-bf1d-6c74918dc691 | -3.02892 | -51.53664 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105bf89f-0e15-341f-8658-b36277fa2485 | -1.99317 | -53.29277 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e89c49c-f5c6-3404-98d3-e993ad84f875 | -4.20193 | -50.68975 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b639bf6c-b0ba-36d8-a5ec-a00283799ecd | -3.38472 | -50.11496 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 877019ee-241b-3b50-831d-63a81d8d7651 | -1.48568 | -54.45008 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34ada7fb-9817-35d4-86d1-f95fd7ad7e6b | -3.64013 | -54.67636 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e30d0939-50fa-330d-a9d4-70e4a335453b | -2.89996 | -54.16598 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5529d434-60bd-3fb5-abbf-338c733715c9 | -2.5941 | -54.2648 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63a24c73-6ffe-3a42-b9d3-c84e2dfa4ca9 | -1.49289 | -52.33369 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64268b8f-b7d6-3c53-8e76-82939ec47b38 | -1.48835 | -52.43822 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af6719b5-9b38-35e7-ac04-e4e6711a978e | -2.98008 | -45.57847 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8ed9ca-b1b5-3bb9-a721-1a92a009b22e | -3.4966 | -53.79753 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411dd517-636a-386e-b440-a824d5eb3bf1 | -3.18164 | -54.33608 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d913d9b5-5bf7-3503-aa2c-49bd3bce68d0 | -3.30054 | -50.49829 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36006c2b-e0a5-3e0d-9649-33ce0dadc50e | -3.02375 | -54.02313 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README85.md)
