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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 968c8271-1f38-3160-a8f9-1193955bf71b | -5.16082 | -49.47958 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55525fe7-5572-3dac-a1e3-32cf10a6126c | -5.01874 | -49.75465 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4c46a7-4664-3346-86dc-f19892147dbf | -5.01543 | -49.75413 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 454fd983-0d82-3a5e-8b92-82992bfff596 | -5.01488 | -49.7576 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7801b48e-58c8-39d6-b67e-7c9e83a0c224 | -5.01013 | -49.96001 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9b09afd-9320-3a9d-8e75-ac4a908466fc | -4.96528 | -49.89941 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd7d1bc6-439f-348f-8cc7-6be1890d9efe | -4.96196 | -49.89889 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f161500-88b5-357e-85a7-a12f8f11f38b | -4.96141 | -49.90236 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 991c3692-f56b-31e5-9d7f-c7e513000273 | -3.58875 | -50.5543 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50bdfc40-78c6-31d3-84a8-20f2289ee938 | -3.58869 | -50.57671 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff10b566-0937-31f7-93f4-559d2a55aa21 | -3.57636 | -50.39193 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b1a5c72-b0ae-3839-a044-62e877179309 | -3.57578 | -50.39556 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4dd03d2-9788-39b0-8185-7dbf6531104c | -3.57529 | -50.37693 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 199599ce-6448-31dd-8400-3deb13256ab5 | -3.57298 | -50.3914 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 773fbd4c-f1a5-33da-a7ca-c997645ccd44 | -3.57249 | -50.37278 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecf24ba5-fc73-3f70-a24f-040f8c4ba471 | -3.5724 | -50.39503 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af6590b7-83d5-34fe-a6c0-ea5ed92ed052 | -3.57191 | -50.37637 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e17e9337-7452-31c9-96d1-1028bf7ad751 | -3.56911 | -50.37225 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e49e84-2453-32f1-95df-b357bd7bab2a | -3.56854 | -50.37585 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ce627cc-3cfd-3a1a-b9af-93b7204ea659 | -3.56829 | -50.57347 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77f9f74e-cba3-3e92-b839-ffe32b78d2e2 | -3.56515 | -50.37534 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdcc8180-feeb-35e7-bed2-b598089766d1 | -3.5649 | -50.57293 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a9770bb-457d-3051-9235-61603591f105 | -3.56458 | -50.37894 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9ef915a-afb5-39fe-bccc-5ea23230dd92 | -3.564 | -50.38257 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d012c71a-9032-3ff4-97bf-501b58d7c419 | -3.56342 | -50.3862 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d78957d4-cbba-3c5e-bb6d-fdad3340a0a2 | -3.56177 | -50.37482 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd45e54a-9e95-3571-9117-2a06ab721782 | -3.5612 | -50.37842 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aee4efd6-0960-30eb-ab4a-361841f95a52 | -3.56062 | -50.38205 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c5afe06-97cd-38c9-8143-bbadad86256f | -3.55839 | -50.37429 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d46a4c24-b7a9-3258-99e9-d6153e07ed12 | -3.55782 | -50.3779 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1de5481d-f965-3e7d-99f3-36c4cdbcc7bc | -3.55724 | -50.38152 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc86e18-bb73-3407-8db9-de5159d2adf4 | -5.38901 | -50.68035 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5fe7ada-4663-3352-b4ab-62e3e18983cb | -5.38843 | -50.68394 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aea56998-a18c-3c0f-a946-c06bf1aab00b | -5.27079 | -50.71723 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b023a3e6-7574-31f0-ba65-4db0ac224cb1 | -5.02464 | -50.76361 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe476bef-132b-3bf9-80bc-30764033a39d | -5.02405 | -50.76725 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c66458-d8a6-3734-b36e-7394dba14b66 | -5.32205 | -50.9678 | 2024-09-27 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d17e2d3-eebc-30fc-b87a-01767eb38143 | -5.17072 | -49.48114 | 2024-09-27 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a15940d6-306c-3779-b0e3-dcf167fc9a6c | -5.02802 | -50.76414 | 2024-09-27 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b25274-42fb-3501-ba56-1ac45aa8f904 | 0.99027 | -50.06438 | 2024-09-27 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b22aefbc-0a48-3fe2-af20-ebbd43d2cf52 | -0.16629 | -50.40512 | 2024-09-27 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca1ad3f7-a037-3a8b-afb0-72981a6cb7c2 | -0.16431 | -50.40538 | 2024-09-27 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 761ee31f-3b39-3549-ae98-a61fd7b91d7d | -1.62471 | -50.53679 | 2024-09-27 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2f51a97-563e-358e-80c7-12ebaa33474f | -2.12704 | -51.12552 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d43ff258-7c4c-3ad8-8a18-4629e23b3de2 | -2.11091 | -50.83629 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ee832e5-ea17-3928-8931-5a554f55fe55 | -2.10743 | -50.83575 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7984ec2-0ca9-39af-8568-699fb5f006f8 | -2.10682 | -50.83959 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb8fa30b-21cf-3e84-9d18-68511714a56e | -3.46682 | -51.36805 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2017887d-fc73-3c6b-86e8-825832347e0e | -3.20125 | -51.14066 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d7a5b0-c13d-34e9-b817-ef7617958c31 | -3.20003 | -51.14838 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40cfcf58-ed7e-305e-b587-78fc5f48121a | -3.19943 | -51.15225 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3e640fd2-321b-368b-bf1e-bebf4494529f | -3.19882 | -51.15612 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eae789be-c98d-3c0b-9d03-39ad7ce3d982 | -3.19776 | -51.1401 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96483d7d-7e52-3592-be38-bf787aa41c12 | -3.19716 | -51.14396 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55f4cbe1-fb4f-39e9-9719-0e174be5a223 | -3.19594 | -51.15168 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 00d7bb98-0638-38f4-9380-54c1792469d9 | -3.19533 | -51.15555 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d99b76b3-e91b-3b44-8968-56d1bba4dca0 | -3.18672 | -51.48738 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17984355-c8ea-3b6b-8a16-47c393feb0f8 | -3.09544 | -51.28748 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 346b9e73-4af5-32c1-b514-9e9b89feb8fe | -3.09129 | -51.29086 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0773edce-3cf0-3f6b-9165-ad387431ada6 | -3.07246 | -51.34046 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f0c0c26-25b9-3379-83b4-7b0b51ab37d3 | -3.01952 | -51.06073 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 63f328d9-a8f2-3cb9-bf4a-6c84e1959723 | -3.01666 | -51.05634 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 451933d5-0538-300a-a521-6f5889f04324 | -3.01604 | -51.06019 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c1cfd978-ac02-335a-a11d-161461b4e132 | -3.01542 | -51.06403 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3ca33424-112a-3cfd-9bbf-006090704593 | -3.00945 | -51.0789 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81cb4292-c0d9-3ab8-b069-654cd087b0bf | -3.00819 | -51.0867 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ae90a32-fb16-36b2-9582-b639a7f16f63 | -3.65625 | -50.94841 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19cb261e-67f3-3621-8e5d-0218fe02b3c9 | -3.65566 | -50.95219 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d3f617-883e-3374-8b67-9c2769a89302 | -3.47033 | -51.3686 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92188b8f-42b2-3931-942e-85f28aef514d | -3.45068 | -51.22187 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2555c34-4885-3ac2-b10e-e162e3d15b22 | -3.30454 | -50.66436 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f0426be-83cd-35d5-8f1a-469400907569 | -3.30395 | -50.66805 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8381676-fa5d-30a0-a7c3-97c1e4921483 | -3.20064 | -51.14452 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62a3a57c-571f-3e80-a89a-f72e06199df7 | -3.19655 | -51.14782 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 377736be-84be-3e9b-b2d9-ee6b0b5c3baf | -3.19306 | -51.14727 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c9600c04-70e6-3d38-8749-ee5aa6879ad5 | -3.09895 | -51.28801 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06d7cc75-fa7b-3fee-a52c-ccde53ac70d9 | -3.09832 | -51.29195 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbf193e-1dd5-349f-895f-df97c716635f | -3.0948 | -51.2914 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 585be270-3731-350f-8e57-4fd6a4afc97a | -3.06894 | -51.33991 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3939fbe3-16b3-3ba8-a95e-1aa0e03c3983 | -3.06842 | -51.33982 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7cd84a5-76dc-3353-b7ba-b80fa0588177 | -3.0189 | -51.06458 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 533b2c26-3095-3e46-ad85-94bf389d8509 | -3.01318 | -51.0558 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3cf7abd-90b7-3576-a2c5-bf819e05d1ba | -3.01256 | -51.05965 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e105e853-50d1-3b7d-b5a5-4f53433d5370 | -3.01231 | -51.08331 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9114a101-b1d4-396e-9ba9-043c04a057e5 | -3.01194 | -51.06349 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d7d4bbdc-5629-31c4-9f7c-479cf77ae5bf | -3.01169 | -51.08719 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6491eeed-7175-34e8-a315-b9a4b3cf8f9c | -3.00883 | -51.0828 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 397d03b7-c8c8-3ac3-b483-477061c4b3ee | -2.88738 | -51.68345 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6efc4b8-8aaa-3a75-9391-8121e4477b6e | -2.8815 | -51.67412 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5ff67f3-cf03-3b4f-8b5e-36b415c2a18e | -2.88086 | -51.67823 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f89617e2-82e7-3a35-9300-b5ac438ba297 | -2.87792 | -51.67356 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cbddeeea-575b-3859-82ac-a6801151eeea | -2.8773 | -51.37983 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b10f5b61-4c86-3056-a0c6-ad702e80f392 | -2.87563 | -51.66481 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 027699c1-d35f-3bd8-8264-75199a7a6e1c | -2.87498 | -51.6689 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 159f0076-d4b2-33a5-a105-5a284d2b1b6d | -2.86423 | -51.66723 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b41af4f3-7beb-320f-be20-fd083812b1fa | -2.86358 | -51.67134 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85f7d35e-59e9-3961-921a-eb98546408db | -2.59812 | -51.94889 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff26f003-12c0-3029-949e-69fcd68c091e | -2.58399 | -51.92035 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 447cba83-6ac8-3298-94c5-a9ac54588d6e | -2.58331 | -51.92461 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad016f1e-3b19-3b82-8e7a-0452d4486272 | -2.4149 | -51.29859 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README77.md)
