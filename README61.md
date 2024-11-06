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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66ae25c1-67bc-3ae4-abbf-4b963ccadf27 | -2.68076 | -51.83395 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e73285ef-913a-32af-8dcc-22aaf71a25d7 | -2.83255 | -51.80163 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6afd04a0-ffdb-398f-9d0d-b6001d0f5b04 | -2.82583 | -52.94548 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6bf12e18-af58-3a8d-9ee8-c0f63fbbe004 | -2.81839 | -52.92547 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fa824043-1e84-3524-a29d-06c0f348ef80 | -2.87742 | -51.31491 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3bf2abd4-46aa-36c6-9ca3-c6b9f01814d8 | -1.29593 | -54.66969 | 2024-11-06 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74825ea-5677-3a4a-aa2f-b088ba968ab4 | -2.91745 | -51.04952 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3f804f76-b3bc-3f54-93fe-746998b5dd70 | -3.15513 | -54.47115 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c117eefc-bfb8-3ddd-80e0-c8a194a292c7 | -3.53281 | -50.33366 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb2c020d-a392-324e-8222-04d704181562 | -3.33083 | -50.08227 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a5a1adff-014c-348c-b88c-8b56963a7558 | -2.92903 | -51.05133 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ff7c24fe-e5d4-38eb-80fb-3f144adfbccf | -3.12885 | -51.1078 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bb3761d-44fa-336b-ad3d-5649a5aac8e8 | -2.85774 | -51.78341 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6845886-742b-3700-b2b9-7bb680e7fda0 | -3.16445 | -53.07319 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36fb115d-3771-386e-8fdc-82d6579187af | -2.91109 | -51.05088 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1022c325-9386-3132-a516-177e0777970d | -2.97323 | -53.2633 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 499c9bc6-707a-390f-a0d7-e1ec6f83ec8e | -2.68129 | -51.83038 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d5a23e5-7ca6-30cd-897d-bd478332ccc0 | -2.71843 | -54.15559 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2f62ecb1-6ea5-3dae-904c-9a97e6361e67 | -3.59296 | -50.26565 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b0c3b5f-7070-3761-872c-388226917fba | -2.95112 | -54.80191 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c803d52-ffb7-39db-93fc-fd6140e5fd54 | -3.04411 | -53.26895 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e6c851-409d-3c50-9d3b-ec0c29fce700 | -3.48751 | -52.10547 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 507d36c3-48fb-35f1-a67e-9a7aa8b9f8ad | -3.66684 | -50.22704 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2dc15ce-d65c-3f74-b7c5-49afaf4f9e13 | -3.00851 | -54.0883 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee564713-5f92-3c76-abbf-a3f4a9eda887 | -3.02953 | -53.26376 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eab74071-946a-3e0f-b15c-eb261192a3b8 | -3.22973 | -53.3964 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8ea501d6-c8b9-33f4-8104-c1336ff0423c | -2.8175 | -52.93143 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8662f408-2555-37f7-9845-694acc1c66f4 | -3.22512 | -50.38414 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 46d8d99a-c311-338f-a511-c71259e7c96e | -2.82392 | -52.9234 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a411f82b-7784-3388-96d3-3cfadee61e4b | -3.03359 | -54.08186 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37be6dd1-d644-3dfc-8654-7be65630e0cf | -3.12202 | -53.12357 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd10ea23-fb4c-306c-89fd-5a9bd1ab99f1 | -3.29183 | -53.11457 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87654830-0a71-357e-9dc8-40ba267c4827 | -3.52266 | -51.67052 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a63e3fe-0ecc-343b-b0a5-580306e0c6a3 | -2.82568 | -52.91156 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d369b63f-dfad-361c-a31d-11e5bc9ef291 | -3.17697 | -51.26367 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4792a3b-9ccf-3a45-918d-52e2482fe726 | -3.17106 | -53.07307 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65443787-e04a-3fb4-a914-533b321f67bc | -3.59459 | -51.57238 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e27acd9b-1492-3051-a330-c4be78f83330 | -3.16146 | -50.21365 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 090124fd-b197-3cf0-bfc9-0e38b2883a08 | -3.96553 | -48.16519 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54d0da29-53a4-3ca2-bc5a-b15edf5f0dc5 | -10.57812 | -67.65536 | 2024-11-06 05:31:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d9b2e4-0048-3e79-b242-21508779edbc | -3.18844 | -50.58315 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e18450f-3c3d-3f65-9fa6-adf7db81b0b0 | -3.76747 | -51.77533 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d03b2295-4ca0-3cff-8a7c-c6208e2e3053 | -2.45268 | -49.03179 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cfcac71d-e936-3489-adb2-28bbeb24334d | -3.95791 | -48.15495 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79541cb9-1963-301e-a55f-5a693140d2ea | -2.83681 | -52.90705 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 38788e7d-6fc0-3f2e-842e-df7f9d245a16 | -9.41357 | -68.7123 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6ca7047-6e15-377e-8171-a338bd1c7af0 | -3.2167 | -53.10615 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f121f4b4-396c-3cd3-96e7-51403c0552af | -2.87918 | -51.3032 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8638c5c-dd56-3fef-bdd1-780a6573ce68 | -12.24888 | -63.44471 | 2024-11-06 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b727efef-7346-3ba2-9485-a08e4621d855 | -3.6792 | -50.23367 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 841ddd04-23e5-32ef-9f00-08cf0b26097a | -2.81464 | -52.9156 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1e10740d-3e81-38b5-8fa0-ccb2b5ff84fc | -3.2125 | -53.09947 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71f8e19b-a82f-359c-bc37-fbc55d5c83b0 | -2.77602 | -51.61042 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d9cbb9b-78a8-3054-a94b-62598c0d5e7c | -2.84265 | -51.35326 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 771b0692-f981-3a74-a441-adc765e6476b | -3.64167 | -50.14384 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aeda0891-db6b-35eb-aacf-f0cb4309d394 | -3.23074 | -53.39546 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7498c1fc-e565-3039-a1c4-df8b29c51af3 | -3.61314 | -51.20725 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f79e041f-80c1-34ff-b35d-0d7b93ed73db | -2.83203 | -51.80526 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8c10078-6cd9-3774-9e11-aa68683597f9 | -3.20357 | -53.23001 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cba7afec-ae2d-3166-86d6-c208f53fc14d | -1.07158 | -62.64906 | 2024-11-06 05:31:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52530113-17fd-3ac7-894a-953d951ef200 | -2.93943 | -51.06136 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9628d9bf-e458-3443-be72-74f3c7528748 | -2.82496 | -52.9513 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a42703b6-e07a-36aa-94bc-18e66e6899fc | -3.69032 | -52.29861 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bd153a3-9ed6-3840-92ad-35e940b558be | -3.52666 | -51.31735 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61fc0f85-a71e-3291-8e42-70b4c0b97b6e | -2.82614 | -52.90851 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e19d21f3-10e2-3316-95fc-b7359baa8141 | -2.83822 | -52.89759 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14009cbf-d7d2-337c-9e6b-f827e507e6ac | -3.23058 | -50.38191 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0b51f480-0c10-3b4d-ae9a-ce0fa260bd1c | -3.34373 | -50.25496 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03003b2-f7c3-3ab7-8ae6-890d7ee80fa1 | -3.08517 | -50.95799 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cbc79d3-118e-3d10-8408-325ef685d178 | -1.3369 | -54.60511 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0304819-09d8-39ba-9a6b-8bdff6947f55 | -2.82348 | -52.92632 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2c03ca1-b32c-35b2-9b4f-82e13e7fa0fe | -3.23569 | -53.39632 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3a78c58-c697-30a9-8363-22a456e7380b | -3.95948 | -48.15744 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bf995be-51df-3778-805a-469bb184a657 | -9.44847 | -68.52991 | 2024-11-06 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5306a5ca-53d0-3a5d-8d8e-6f1b6353d5cb | -2.71052 | -52.96142 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30b775cd-9854-3cbb-824a-2dfe75de85e8 | -2.84407 | -51.79983 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 753c4bf4-3252-3160-8aea-0bad39b5f02a | -3.17432 | -54.46897 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5dce9d9-7aa3-3197-8f4b-702ea5a90c37 | -2.84442 | -49.48122 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95e1c645-80b7-3359-bc81-e405483c7a68 | -3.5301 | -50.35229 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01667ede-c320-3e14-854a-97d8c10555a4 | -3.0341 | -54.20955 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0222954c-4fd2-3a3c-9cae-3cac3660b50f | -3.1653 | -54.46385 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba93daf3-d222-3622-ad42-121bf81df4c3 | -11.77372 | -64.98497 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea7589bd-9d6f-319f-8154-45d73b469ea1 | -3.18712 | -50.5921 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 069f6a8f-b613-381f-a32f-decb3559bcd3 | -2.80761 | -51.77929 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85cbbed6-bcbe-335e-9721-e1f5fa2fe0c4 | -2.45347 | -49.02622 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3bf5f754-99c5-38c4-b253-bcab991552a3 | -2.92962 | -51.04718 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7ccb93b7-8a4a-3fdf-af96-699b0f802b87 | -9.02755 | -68.5062 | 2024-11-06 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2db97b1-c7a9-34a4-be8a-affaeea51feb | -2.65698 | -48.56263 | 2024-11-06 05:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd778e67-47be-3c8d-90ba-44753c28a17f | -3.45224 | -50.37342 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 151cea2c-0382-3d98-bb11-bf5b54971f47 | -2.83587 | -52.91332 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07e3962b-7cf7-371e-90af-abafccb632cd | -2.81287 | -52.92754 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a513d23f-a724-33c1-8bc8-5614beee0f9f | -3.03868 | -53.27117 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5c47e715-8361-3e24-ac6e-59634644c4eb | -3.15653 | -50.20311 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 0ea8c5c7-69b9-3d8f-bc9d-ee778f2356e2 | -2.42861 | -53.66684 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39b098cd-ac6c-3d8c-8412-35a824792f67 | -3.67847 | -50.23407 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3c22c79a-23b0-3118-b7c0-3b16c6dfc55b | -3.17756 | -51.2597 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 761cca9e-6a1c-31a6-9429-7bf775553fc6 | -3.17645 | -50.58139 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6c3909d-b191-36cc-8c22-65b79657b15e | -2.8452 | -49.47601 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4119fffd-4595-37a2-8690-4bdd58070734 | -2.85437 | -51.76786 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 183b980d-d433-34fc-86cf-3c317319cc5f | -2.71985 | -54.14605 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |


[Clique aqui para ver as próximas entradas](README62.md)
