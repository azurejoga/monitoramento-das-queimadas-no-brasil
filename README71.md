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
| bf9340fe-ef93-3589-89cf-4e625a369bf3 | -3.35017 | -50.51193 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57afe183-768d-313a-98e8-0f164121655a | -1.19276 | -53.67889 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25398e04-789d-32ea-80d0-21be36e9ab97 | -1.69356 | -55.15609 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 931fdfef-3c7b-36b4-9121-61fdf424e618 | -2.28951 | -49.20107 | 2024-11-24 05:14:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d15b6b2-c0f5-3339-914c-6a50b9045e58 | -1.4853 | -52.5172 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bdcbae8-32c4-34d7-85d1-0e2cd24856c5 | -2.74098 | -49.11785 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b14ffacd-e08d-3b6a-aa55-88a516354bd7 | -3.31005 | -50.02736 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe84d55-83ea-3adf-9c47-aa1c22f7a68b | -2.57809 | -51.88744 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32abf6f3-9000-3cc9-8519-96c06e3b402c | -3.06418 | -49.2015 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76d4ecb2-ab5b-37f7-906d-7853d678c1d5 | -1.86831 | -48.16829 | 2024-11-24 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03ba0c78-548e-3867-bcfa-c7affe61528a | -2.24355 | -49.2228 | 2024-11-24 05:14:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe236ba0-4d92-3547-a6f8-bec460d60158 | -3.27245 | -53.81555 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3789289e-d1a3-333e-b5f7-e774fb7d80ab | -0.81074 | -52.82745 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d5374b-41f7-3ce1-82b3-6fe9521203d6 | -1.19583 | -53.68401 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9256132b-f3c6-3785-8774-70776a4d04e3 | 0.87542 | -54.63568 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 021c7cf2-7011-39fb-8cf1-f6a9b329f4dd | -1.63454 | -53.31726 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4a36f05-a533-39cc-8ea1-ed27190651e6 | -3.49108 | -49.9152 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a28256cf-5afa-3689-b6f0-9f711b372f6e | -2.62482 | -54.9313 | 2024-11-24 05:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fe896d8-6a48-3478-9b9c-8692d55ec810 | -3.23075 | -54.16466 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 868fb82b-8d0b-31e9-9a23-89557df56886 | -3.63806 | -50.22342 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7beaa1b3-8a7f-3524-9279-5c2ea45d7c9f | -1.61577 | -53.30945 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e529cf68-1ac1-3023-809c-7c7f39cb135a | -3.47666 | -51.99002 | 2024-11-24 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dee259ca-3b89-3f4e-b3d6-5342dd90a959 | -1.41315 | -54.90064 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97a52945-265f-3edf-a1d7-4ac3c6eb3e46 | -2.30293 | -53.8785 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25b4d8fa-0dfd-3a34-a111-c95e9617dcab | -2.47512 | -47.08918 | 2024-11-24 05:14:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1a555f40-b009-396b-abe4-d791b97680db | -3.8572 | -50.05386 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2152d227-9625-36ac-acb6-c4facfbfd1eb | -3.75731 | -49.93403 | 2024-11-24 05:14:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0be2bd0c-ede4-3b43-b384-84e6712b4dcc | -3.21327 | -53.84077 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5005583d-5919-36d9-9e61-2a551adeb60b | -2.5677 | -54.06217 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fde571d-abfe-333d-8547-cb5979794378 | -1.19878 | -51.76036 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a07263e0-1b57-356b-8d1d-6d3b42ae352b | -3.70408 | -47.60493 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a74c02f-551e-30b1-9bd9-abab3b50f976 | -3.29156 | -50.54038 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27b201fd-19a5-3862-9dc7-80821a6fc0e6 | -3.64288 | -50.22621 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7ccf6ec-7c68-34f8-aae3-8ff8d3d9d23d | -1.22877 | -51.79378 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 454df712-220b-3a38-b118-47c369e35bfe | -2.53584 | -53.99427 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15be213f-f040-34c6-9735-f8b5a6d30ebe | -2.62324 | -51.79601 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89608e44-b8a7-3988-a6fc-8c5cfbcd2f00 | -1.24291 | -53.39497 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1474473a-a73a-3045-a07c-3750ede688eb | -1.41511 | -54.48649 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 756e2c69-e83f-3ea4-b3b0-2248823b0064 | -1.68675 | -55.03748 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83c22914-6d3d-32dc-a160-b0b6e6ec9c35 | -1.98094 | -56.57384 | 2024-11-24 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47aa791c-523e-3b01-8b1d-6a6b94b8127e | -1.27085 | -52.69402 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbbd5fdc-f7d4-32fe-857a-459da45067a2 | -2.9708 | -51.57391 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fd7c0a9-3107-38d4-91c9-d54dcbcae309 | -3.54558 | -50.1913 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95a588a2-6bb0-3374-ba38-1a8e642904ed | 0.40182 | -50.85648 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9eab2432-c39e-3550-bbd7-f7e3e4d24231 | -1.51375 | -54.19018 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 98da945e-e43a-3556-8b8a-51eba7bca1a9 | -2.72932 | -54.11352 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfdb5ebc-f6c9-3185-bf72-b9129f23f397 | -3.10587 | -53.10896 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51cecebb-5beb-35c9-905b-d2038ae1020c | -3.25812 | -52.85196 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9bb91b5-a42e-3037-9b3d-48631f104c07 | -3.29127 | -49.91112 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e116eab-b8af-31a3-974c-d9ddb36c170a | -0.84535 | -52.54867 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcd028ca-0b72-34f2-8ce8-40027dbc29ef | -1.51443 | -54.18588 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9d283a78-ed7c-3988-bc1a-e7c911d374bf | -1.83595 | -46.64302 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 686cfa14-48a2-3860-973a-c1ce6d4f7f07 | -1.9815 | -56.57028 | 2024-11-24 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c6e2da6-79cf-3407-8a9a-05c6fd1cbe7d | -2.20583 | -54.50475 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c69633e-e16d-3914-abdb-273484e1096b | -1.40201 | -54.47475 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 629ad714-150f-3c1f-a1b5-77e053b12e04 | -1.46002 | -46.04294 | 2024-11-24 05:14:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcbb89e5-9cfd-30e6-a2b0-69f549429f44 | -3.10095 | -45.78004 | 2024-11-24 05:14:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 231e790e-3ff9-3ad5-a3aa-a3bd39c28e39 | -1.6198 | -52.60801 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 530e223d-0ebe-3596-98c4-d64dcc9279f7 | -1.24921 | -51.74747 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d514ed95-6704-33f5-a76f-1214fe3a5005 | -3.24955 | -50.126 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f701d5c6-4763-3a27-911e-67416ac54def | -1.20494 | -51.74891 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9191716-c4b0-3001-a4aa-a02243956063 | -2.69877 | -51.36161 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df9550b3-1d45-3fd0-a472-24a1d2d1a0e6 | -3.0317 | -49.45192 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd680f4e-a390-33a3-89e5-e9cf0412aee4 | -3.23532 | -54.23539 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df3bf0f7-ba19-3c7e-b1a9-edce0dc3079b | -0.03553 | -49.6438 | 2024-11-24 05:14:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bff2609e-bdaf-3d30-86ca-837083586a09 | -2.74822 | -48.67024 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b636bbf2-fb11-3d3e-9084-3876546caef3 | -2.45026 | -53.70206 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 560d9eda-7ee7-3847-97d0-59bfa3d503e3 | -2.94722 | -53.71999 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f5a332-3ca8-3d71-83f5-e19ef66780a5 | -3.13741 | -52.98649 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d57a6e4-9d27-3f64-9ed4-56bc4b19a9b7 | -1.35838 | -54.65398 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4a262e5-013c-321f-bab2-16ec0f8036f9 | -3.27171 | -53.82038 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e224a46-1784-3792-a39c-6e370ca43dcb | -2.86835 | -45.83204 | 2024-11-24 05:14:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 798151a0-1b20-3819-a24e-43bfa73d5670 | -2.75914 | -54.07146 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cde33534-cead-3ec6-86c1-920ada829fd5 | -1.77291 | -53.61335 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fdc7a4b-ae20-3f3f-9f80-c67010bd5b63 | -1.4639 | -51.12083 | 2024-11-24 05:14:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11c1f1d3-c7ed-3847-93ee-1d4905aebf68 | -1.12954 | -51.68062 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90969c68-c12e-3e27-ae7f-d195ca486514 | -2.54711 | -54.04492 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2df4d72-04c7-36fe-a3e4-bd35905fcea3 | 0.08507 | -51.48998 | 2024-11-24 05:14:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6512974f-a189-33a9-a84f-2f5182ca6791 | -3.2842 | -53.84227 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0fed0dc-c4c3-3ef1-bd9c-eacbc254b3da | -2.51285 | -54.11636 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 33958cf2-ec7c-3ff0-8354-f909fcae2447 | -1.95676 | -49.5321 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42bd1c26-94d9-351d-a40c-885e4b68fa2e | -3.24555 | -50.62289 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3adcedb5-2c69-35e6-a532-926bddee05ee | -1.61744 | -55.13744 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6d28ec8-7dad-38df-acfc-528bdbd57cd5 | -2.86439 | -53.96709 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d99d1a21-b209-357d-ae03-9b14ede32d29 | -2.14955 | -50.91617 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bc2fa30-60cb-3c42-b07d-54472db1b20d | -3.10849 | -54.00172 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2889c44-9e54-3d32-837c-d59873cd9933 | -2.44627 | -49.08501 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3021faf3-4f3f-340b-a055-5b7599a1bfd6 | -3.38817 | -50.32521 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58a95b70-5d89-3bdf-bf5e-78af1bb6b6fe | -3.06465 | -49.19827 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7d6dd25-4c0a-3959-b2f9-c53a094803cd | -1.25351 | -51.74813 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc391c45-09bd-31d4-8a1e-3a47a9762baa | -1.95256 | -49.52547 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c48811-3322-3583-92db-f7bdcc2b8fba | -2.45026 | -49.09063 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e47fe8fd-1a09-3a45-b8d3-0eaed85b85d6 | -3.01352 | -51.38336 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6d87758-6c8f-3096-aba0-e0d1b55a9acb | -2.28788 | -47.30725 | 2024-11-24 05:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e47f0d7-3ba1-353d-9d9c-e1f993969ee9 | -3.10397 | -54.00575 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 222a627f-7465-34f7-bd9f-ac7e1205a510 | 1.77257 | -50.95237 | 2024-11-24 05:14:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8168362-23ef-36e6-a3de-651a1fa70447 | -1.2714 | -52.69044 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68ce33b7-bc12-39d2-a998-f9f889dd09c2 | 0.69496 | -51.4417 | 2024-11-24 05:14:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0981aafb-bd19-366f-9fd0-ae25ce5be628 | -1.05517 | -53.16099 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d750eba4-864f-3274-8cd9-07a0f978b939 | -1.77675 | -53.61394 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README72.md)
