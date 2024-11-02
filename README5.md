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
| 994a4657-b4be-3118-a3ba-6a713cb068bb | -2.25373 | -50.4627 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b1926f91-56a0-3512-a0b9-866674d57c01 | -2.25112 | -50.44368 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 79c43173-db62-3985-881b-46e0619c4c56 | -2.24982 | -50.43419 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 16c2199d-d73c-3d6a-97aa-56424200fa17 | -2.24582 | -50.54169 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edf233c0-7732-3437-9faa-e931761cbb2b | -2.24451 | -50.53211 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57af6f68-ab5e-3c8f-8300-21edf3df0686 | -2.18803 | -50.79341 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 870e6e02-3d29-3aa4-b3f9-b67877269fe3 | -2.16812 | -50.51007 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eb70c528-1c9f-3712-a0d4-e7fafe01743c | -2.1601 | -50.91388 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b9e57200-592e-3b8c-b011-c826fa965709 | -2.15873 | -50.90395 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7b3cd57d-8b33-3bd1-a08d-8a43606f148f | -2.14077 | -50.70627 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 73ecfacc-cb72-3e9b-b207-f5496148a996 | -2.13942 | -50.69657 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 6e605821-6841-382d-81cc-8c6c36f692c8 | -2.12117 | -50.83867 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e7c7fd67-ea2e-33e0-994f-dbd2106d651c | -1.8703 | -51.02356 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b31aa7b7-c4f0-31d2-a62d-294ee25a0ca1 | -3.59281 | -50.76004 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08175599-2319-3019-b138-eb66731aefe3 | -3.51328 | -51.6772 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 97f41d94-0eb3-3b8b-9268-2cce58dd9ef8 | -3.51175 | -51.66582 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0055c584-4928-379b-b943-99517b581ebe | -3.49648 | -51.18682 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4c47b4c4-74b5-395b-af4a-898c802b86fb | -3.44212 | -51.53284 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a4732ba-69c7-3f57-a9df-d8bc9d957d83 | -3.44059 | -51.52169 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| f67760a1-0188-39a5-86b2-d516a632ec17 | -3.29527 | -51.20518 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3714741a-251b-3639-a5fe-eeabfb23e2cf | -3.29382 | -51.19461 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8c55f4c6-16e1-3ea1-86af-f13309ba1858 | -3.28522 | -50.92038 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 1df88ed2-a3af-3997-883a-e9e4a5799076 | -3.2838 | -50.91016 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 7f44ff83-dff5-30e1-abc1-4c2a42646a14 | -3.20814 | -51.16988 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5ad399f-1383-3260-a721-0d87d77a3814 | -3.17747 | -51.08879 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a2e2045a-0e11-3cca-89fd-95078f078c9d | -3.17605 | -51.07838 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ab3976b7-aaf6-3e2b-a835-6d293da95f1d | -3.17463 | -51.06797 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4c3935c0-56ff-369a-be0b-6bca81578ce9 | -3.16649 | -51.0797 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c9c21a2c-17ce-3062-aab7-425eb5ae7fcc | -3.16508 | -51.06933 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 152b14f3-8f07-3327-aaba-363ea825ec8c | -3.1527 | -51.15125 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83a2ef37-7aca-34a5-a38c-b41b1179ee97 | -3.14039 | -51.0306 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1cba48ed-2234-3ef1-b0f3-7a182230937e | -3.11144 | -51.13565 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 70efaf45-5597-3227-aae3-696cd6161cd5 | -3.11 | -51.12518 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| a1f4f95e-812c-3d97-a3b4-88130a7b1646 | -3.02348 | -51.38105 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| aa0146ab-1537-3dee-8699-4e1fca375713 | -3.02202 | -51.37031 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 89cadba3-61a2-3007-ad15-bdd325f5842f | -3.00986 | -51.58876 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| cc5be419-b369-30a1-8adf-6100b334ef00 | -3.00833 | -51.57774 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 30640c88-6aaa-3631-b63d-af5ce948470e | -3.00002 | -51.59013 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2d75991a-fce6-30b6-92cc-b22578eaf9fa | -2.99849 | -51.57906 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b8ccd752-7379-31db-aa4d-c78f292f962e | -2.9691 | -51.43845 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8173c3f7-5bfd-350e-b946-dc67471cdace | -2.96761 | -51.42765 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e64747f6-0d35-3752-a751-02d7c42e7400 | -2.96003 | -51.05721 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aab9b1ea-f4fc-3c0c-ab9a-2daddff89264 | -2.9548 | -51.05333 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ec4ad3d1-2659-304a-b740-78255582d214 | -2.42622 | -50.51413 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b6e1200-89df-3034-b065-17829dbfc6b8 | -2.42491 | -50.50453 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 13641265-8c54-30ba-9f1c-54de0783ffb9 | -2.41684 | -50.50213 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ab2a6e17-9309-3e88-b1e2-ea9bdad97e98 | -2.41578 | -50.4376 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4c8c7580-63ac-3a61-85f7-a97ba13a67df | -2.40746 | -50.4353 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2346d42e-8cbc-36c1-a55b-fb7732633f90 | -2.32882 | -50.47545 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e989911c-d886-3223-b1ee-45165f4b6005 | -2.32752 | -50.58906 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24cc6abf-b49d-357f-b8f0-9567dd9677cf | -2.32491 | -50.44685 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57856638-9d4f-3f8f-a61a-dfd6f7ff21f2 | -2.31309 | -50.62063 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a125c9df-9d05-3f10-9373-6e15a65592eb | -2.3013 | -50.67168 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 33c9e1fd-b617-3126-90ab-36e7894fc596 | -2.29996 | -50.66198 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 73952c94-9b8b-3317-8f98-4f552ab4a8ff | -2.29204 | -50.67298 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 0c47bb96-049d-385e-8122-7ad51c7fb790 | -2.2907 | -50.66323 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 298eadb4-1426-3ee0-85cf-0f0373596260 | -2.28314 | -51.13748 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 963452d2-384f-3210-b6d4-c4eedd2085ef | -2.26557 | -50.68658 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 43f0b2f0-de93-32b2-98e1-bbe8c97ac54f | -2.23436 | -50.71709 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e6d18458-94ac-3488-aef7-44363d4c625b | -2.233 | -50.70734 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d4beeac2-4ac9-3931-aafa-f3a8f90cd12f | -2.28085 | -51.93303 | 2024-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4d5e2641-e2d5-3656-b103-ef3089f8b7de | -2.27929 | -51.92164 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4c0a6ab6-d437-3db0-8169-dce9ead6bb5d | -2.26933 | -51.92303 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5852f0d8-8ae9-34cb-b8e9-f224c9a5dbc1 | -2.90362 | -51.48701 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d9601f17-a930-3193-91d5-0d3181bd95ae | -2.87971 | -51.31516 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e70a0f2d-9746-3b37-8445-0cf6bf3a1d7b | -2.87823 | -51.30455 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e727c6b4-1566-39c5-9553-95ee8e6f5424 | -2.85601 | -51.28604 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5ccd7ea0-463e-3f8a-821e-1f75ce6bc078 | -2.81497 | -51.34584 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 79246825-f3ec-3b9a-a365-c2ec99a7315d | -2.81257 | -51.35203 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c80cca8-0fac-344d-9349-1d498c8c5912 | -2.81108 | -51.34139 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 67266417-2519-3104-9516-99eb0685fb65 | -2.79843 | -51.60796 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 74011408-a6d0-31fc-a498-3af9dbfe535a | -2.79692 | -51.59696 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e88d16ba-590b-35dc-85e0-d4bc37300e9b | -2.90395 | -51.78122 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| bee7c7a9-22bd-3eea-90f9-e98680dd9925 | -2.90242 | -51.76997 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 20ceed48-6134-3d45-908f-6b4ca8dc6a24 | -2.88708 | -51.65744 | 2024-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0fd76afd-674c-34c5-90f1-756e9c37e176 | -2.88018 | -51.83089 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 55b24617-9ed0-3c51-b884-1a30171972ee | -2.84596 | -51.80647 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31d17199-cd45-3f27-bc92-c6a49be3891a | -2.83599 | -51.80783 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8226af85-b91d-3ee0-abe3-e298483d9b1e | -2.82603 | -51.80923 | 2024-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a5230cb-2fab-39b6-b751-2ad1a7bf6c46 | -2.80989 | -51.76531 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 17743043-564f-3251-8f2b-933eb980b111 | -2.80835 | -51.75403 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 59320047-0aff-37af-806d-ae5e6e38b339 | -2.79843 | -51.75542 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| af70d7be-f017-3b7e-83cc-6af5cd07c976 | -2.7969 | -51.74417 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6021cf8d-467c-3b5c-8195-19ff1d9a6941 | -2.76656 | -51.66879 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 797bd479-2f08-336b-a7a9-fbbf6a2abf5d | -2.76589 | -51.67526 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 922a0b13-169a-3b8e-967c-5b60ef03470b | -2.74556 | -51.74627 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cd061dcb-2889-3c47-b82b-91a6d047bd48 | -2.74402 | -51.73508 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7f685f98-53c9-387a-bb51-180cf277adf6 | -2.73411 | -51.73642 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 49685a11-b406-31ad-b009-5bf4064fe51f | -2.65454 | -51.7533 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfbce774-847f-37ec-8209-778c358e4c78 | -2.64989 | -51.71978 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8d0a406f-eb50-39fd-bb48-53f75bad8e39 | -2.64834 | -51.70864 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1d8884b2-fb54-3a78-a79f-6adaa5076694 | -2.64463 | -51.75468 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8770fe53-42ac-39bb-b30d-d3bd33e68a21 | -2.64155 | -51.73231 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4a04c55f-65c8-3d28-bbaa-b4aa29b862f8 | -2.52698 | -51.78879 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1f7f6993-d226-392d-9d04-a6ff2a74f7c2 | -2.52546 | -51.77762 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00e0c4dc-74b8-3019-a1d7-f6fb97ccdba6 | -2.51706 | -51.79011 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9b502e8e-b8a4-356d-aef1-3d348362a5e0 | -4.12578 | -51.07848 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 84d0e5c9-7a11-3568-b56a-f10325c670cb | -3.98014 | -50.90126 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 80c698b4-281c-3c8d-94ee-b8ff6b1ebc93 | -3.68953 | -51.18049 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 4032f4b4-a40a-315f-98fe-74f31713e305 | -3.68806 | -51.16982 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |


[Clique aqui para ver as próximas entradas](README6.md)
