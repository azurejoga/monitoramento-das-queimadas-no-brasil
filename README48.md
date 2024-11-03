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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19a8c4b1-974f-33ec-b722-299a9cfb3772 | -3.27151 | -50.33455 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9692f7af-bd78-30d0-af70-1e21a78e7a3e | -3.27107 | -50.35906 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340e758b-a2ce-3bb6-89c1-8040ffe63fba | -3.27098 | -50.33798 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad2b2601-377a-39af-bb27-82a9ace32eef | -3.27044 | -50.34141 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27fb8b73-1a3c-38a2-9a82-a6f1356a66ed | -3.26991 | -50.34484 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 607f8f91-5125-3ae6-b620-19812e3670b5 | -3.26768 | -50.33747 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bec39faf-849b-3b4c-9186-ba39ed57e66e | -3.26661 | -50.34433 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8128cf07-62b2-3f24-8cf8-7bee46c72971 | -3.26438 | -50.33696 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bcbf9a2-2ba1-351a-a97f-dccb4ef77515 | -3.25287 | -50.34572 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fd3a560-d41d-37bf-b562-f6df7b8689dc | -3.25054 | -50.18728 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa3369e5-c2fc-3b3e-b122-9dca9b1dc58e | -3.25011 | -50.34179 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b591829-d4c8-30a2-9d33-23368b72f09f | -3.25001 | -50.19071 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29af0a7f-b198-3852-bd5c-bf7fb3c0cf76 | -3.24724 | -50.18677 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a408f03-07d5-371d-945e-0916af325ba6 | -3.23074 | -50.57425 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3081bde-3925-34b7-a8bc-f5c6c4e02b3d | -3.21487 | -50.19936 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a3c89fc-7f44-3483-a26f-cc2362f21b24 | -3.20864 | -50.2827 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2d64ada5-9a3d-327d-aaf6-419eb250783a | -3.2081 | -50.28614 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b703125b-5c1e-3cbf-973b-80ddc250ac74 | -3.20587 | -50.27877 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4e8704a-e5de-34b9-b7c9-e1787c174d8f | -3.20534 | -50.2822 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 807fa498-d1a1-30ee-9aed-0588bb369e08 | -3.2048 | -50.28563 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff0b4e02-e2e6-3b26-ada3-13a07ac4da62 | -3.20427 | -50.28906 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3093d04-73cc-305a-9dda-77f1ff0467da | -3.2015 | -50.28512 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c26d36b-8ce3-3a9e-942f-4cec0e783ac7 | -3.20097 | -50.28855 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c8b31993-0672-3ec8-9269-28b39613c6e6 | -3.20043 | -50.29198 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78cf5fc5-3308-379c-a711-eee37dd093f2 | -3.19767 | -50.28804 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12b16ac-ca02-3653-8be7-f6a38f1fe671 | -3.18291 | -50.57743 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54e38669-a3fd-330b-a3e6-b3bdf6c18764 | -3.18237 | -50.58086 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 515951ba-7400-315e-b89a-94a9ddd62ab9 | -3.14277 | -50.35325 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd63419c-e205-3c2c-b1df-b7adf18b2974 | -3.13448 | -50.34143 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2734da26-33ac-355d-bafc-d76235e3ba45 | -3.11441 | -50.27512 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8299a34e-c4ae-39bd-94ba-64b37602d599 | -3.11334 | -50.28198 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d98d7d30-6b64-3bd7-88b6-5a958d6d44cf | -3.11281 | -50.28541 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cfdb8acb-7238-38f8-99f6-42408c25398d | -3.11227 | -50.28884 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b9f3b75-0914-31bb-be71-aeef1a276198 | -3.11174 | -50.29227 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b43895f6-5062-3793-9e9d-e60fb24282c8 | -3.11111 | -50.27462 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13080a1b-cbb3-30e6-8178-0b073ff4bdf2 | -3.11067 | -50.29913 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8adf04bb-af0b-376a-9225-09ad77576487 | -3.10951 | -50.2849 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| df1f73cf-3b91-32af-94cd-52bfc0271ae0 | -3.10781 | -50.27411 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c79b71ef-6269-3162-8217-360df2ac4751 | -3.10683 | -50.30205 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 091a3c39-26d8-3f4c-a7d3-f3c6bcd00faf | -3.10621 | -50.2844 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 673418fc-7b93-3e17-adfe-1cea5d29d9e3 | -3.10407 | -50.29811 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 50564d9a-a3c1-35b4-95be-0de2059d454f | -3.10398 | -50.27703 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d837d8ac-6c88-3e02-a959-f9c4f4d72276 | -3.10353 | -50.30154 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2fa46b6e-60d2-3ba5-b749-efee629963d5 | -3.103 | -50.30497 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce031b7d-54f2-3155-b10d-393309c0259f | -3.10237 | -50.28732 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 65e1a43b-b11c-3603-b568-9c1a2c2a1632 | -3.10184 | -50.29075 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 19f27fcd-1281-327d-b764-fb61edd683a7 | -3.1013 | -50.29418 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64a188d0-b63c-3827-ac4d-1b049401eafd | -3.10068 | -50.27652 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| de97c948-0203-3338-bba8-479784c52a83 | -3.10023 | -50.30103 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3f8c5aa-c847-3472-a53a-f783c0cfd00b | -3.09854 | -50.29024 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 70b361a8-1e77-391e-a8c7-4635e4f5e42e | -3.09684 | -50.27944 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a770f18f-bdc2-3f70-a58b-be2dee257947 | -3.07576 | -50.50104 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10dbfaf4-1337-3b2b-af15-87aebc169f8a | -3.06256 | -50.499 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d148f1a1-0afa-349b-8c2c-42f06f2d4093 | -3.06149 | -50.50587 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1db9e0cb-b32d-34fe-9dd3-e85eb3fa38be | -3.05926 | -50.49849 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7eff53c5-e640-3e9e-87a7-a6fbf0145c31 | -3.05819 | -50.50536 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 913d7af7-fd0e-3db8-8cfb-cfd8743a470f | -2.66696 | -49.25809 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fbf848d-a0dd-35e1-8226-47cac1a0b70b | -2.65861 | -49.24608 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd287008-f183-32ed-918b-164b197d60f1 | -2.64453 | -49.18303 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3abaf2b-76e4-3901-8e68-b6346107884a | -2.62462 | -49.20147 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0442d5d3-c8c2-3a94-a1a0-6f59df79b545 | -2.62337 | -49.16544 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43a4a980-66f1-30c2-97a9-200a97fa9f53 | -2.62129 | -49.20096 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213432ea-7b12-3d51-8107-ab491e40a44f | -2.61904 | -49.19345 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00db02e9-4c52-319b-b175-ccadc374d1bc | -2.61571 | -49.19294 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea763189-353f-3cd1-9665-28c156cf3eed | -2.61517 | -49.19643 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53553a26-66f7-3297-ac45-a98a36a6390e | -2.61103 | -49.26735 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6348328-011b-3973-bb72-c7d90e4914cd | -2.61058 | -49.15989 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0a0aeb6-4c6d-3825-a314-da0bf4e7f038 | -2.60518 | -49.1949 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffd2a1c3-d250-3471-95b2-86af64a0fd99 | -2.60266 | -49.25535 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bf7b3f1-77d7-3e05-adf9-96bf3e8d7dda | -2.60239 | -49.19089 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bbeaa68-650a-3515-bdaf-c0a6bf15ff45 | -2.60185 | -49.19439 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b1610ad-ba7d-39b5-9362-32f296278df5 | -2.59934 | -49.25484 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a0bb32-aa18-33bd-a1c2-301059a724a3 | -2.59259 | -49.23236 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5404fb8-02b7-3853-8587-3ab2ed9f7b3f | -2.58926 | -49.23184 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65175c8f-8007-3818-875d-d7afbe9cfbff | -2.56411 | -49.24175 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cff04c1-46a2-3157-a47e-ccb008ce600a | -2.56356 | -49.24524 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cce2509-f4db-370f-bee6-558de13fa397 | -2.56302 | -49.24873 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb5fbe2e-d600-30c9-b8e7-87265ddf8ec8 | -2.56078 | -49.24125 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f2db8c5-5e87-3222-98ee-46d929d1b6b6 | -2.56017 | -49.22327 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c368f636-f5f4-3fd5-abd1-bb4f3f57aaa6 | -2.54856 | -49.23222 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d528fd0-0ab6-30c6-8d2e-22a787b3bf91 | -2.52086 | -49.23511 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5071069-e79a-34d1-9e5b-6a931b9b9190 | -2.51753 | -49.2346 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc93acc4-df53-3b5e-b6a5-0334c70c8e4a | -2.51341 | -49.17314 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 827ed3ea-e2f5-3cba-87fb-0931286c6722 | -2.50693 | -49.21509 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4487bd2c-6c0d-3470-8eba-8390659dbe20 | -2.3814 | -49.38836 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57314d9d-a3f1-39d1-a088-624861d26567 | -3.0747 | -49.56687 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f0e3494-edd7-3e40-9dd4-da83c6fd65d7 | -3.07416 | -49.57034 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a45ebae5-3842-3a08-80ff-43d65db169d6 | -3.06976 | -49.57676 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c13deff-1202-3272-ba87-c158895eaef1 | -3.06861 | -49.56239 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb394703-3006-35c9-b23b-ce4c2527c365 | -3.06591 | -49.57972 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed8a8d56-ac3c-3a1a-ace2-7913d5bd2b9a | -3.04362 | -49.52658 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8314c263-09f9-3ff9-8bca-2bc0efdcc979 | -2.99 | -49.52189 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 32014748-91ec-301a-a19c-1d508282409c | -2.98946 | -49.52536 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d77e745-82f1-3a1d-b51b-315e51c7986b | -2.98668 | -49.52137 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b1fbee01-5ffa-3a9d-8f9c-1c324684676b | -2.98614 | -49.52485 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f6e6ae9-cea2-318d-9816-cd04c9cb2fe9 | -2.98336 | -49.52087 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 311d9cd3-78d5-3c8d-93ff-4a60cba14fe8 | -2.98111 | -49.51341 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1787028b-ae8c-31f0-af1e-7c0d3a3f07c2 | -2.98058 | -49.51688 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d0996f0-b1ff-3118-a2d9-af9c8d8e02f4 | -2.96843 | -49.55056 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c44a360-e7d0-355b-923f-ad1c796b827a | -2.89091 | -49.50314 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README49.md)
