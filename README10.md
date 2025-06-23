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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 720aacf8-65cd-3c1d-bdce-59f5eedadb63 | -19.52226 | -45.31212 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2cf5e32-26fd-398f-91de-e2a25d504988 | -19.51652 | -45.31767 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 977d2efa-afc0-38d5-b2b7-71839acb9ab1 | -20.41855 | -43.55338 | 2025-06-23 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27cf111b-6292-38c6-ac31-912186e95482 | -23.04555 | -49.89257 | 2025-06-23 04:49:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c14a7333-390c-363e-a226-4fd35d93f177 | -19.52193 | -45.31525 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d41ea834-fac6-3034-9210-14fbd72ce8f4 | -22.2541 | -50.03881 | 2025-06-23 04:49:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6288da7a-5365-3387-b54a-9530bf6ab9f5 | -19.51719 | -45.31147 | 2025-06-23 04:49:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 537b01d3-df28-3416-b749-a80265cde289 | -20.70658 | -50.06356 | 2025-06-23 04:49:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 87f5bfc7-d032-3e44-b294-2c0bcc0a6f35 | -21.39086 | -45.50333 | 2025-06-23 04:49:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c618a7f-67b5-3111-81a4-43f89965472d | -8.07 | -43.1216 | 2025-06-23 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| f4b81a38-adc9-3bed-bafb-93e25e37074c | -8.0703 | -43.0981 | 2025-06-23 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 95d3fe3d-3bbc-3b97-bf19-4d80b990c76d | -8.0703 | -43.0981 | 2025-06-23 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 1152eddf-dcec-39ed-9e11-975d3b392593 | -8.07 | -43.1216 | 2025-06-23 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 48fd1810-5300-36b3-9471-7682d301fa81 | -8.0703 | -43.0981 | 2025-06-23 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.4 |
| 6467a846-7d93-3a94-9433-8f89c13378c7 | -8.07 | -43.1216 | 2025-06-23 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 15123176-b5e2-30f1-8635-8aa255b6da3d | -8.0703 | -43.0981 | 2025-06-23 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| bb30a70f-dee0-3f17-9743-b1dc570f8935 | -8.07 | -43.1216 | 2025-06-23 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 9e9448a0-57cf-31b5-97e0-a15cc7835398 | -8.0703 | -43.0981 | 2025-06-23 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 06bafdaf-8944-379f-92ec-05e50665d482 | -8.07 | -43.1216 | 2025-06-23 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 60a07efd-0f06-3a58-8246-24583f806552 | 2.74982 | -60.36622 | 2025-06-23 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3ff85806-deb1-3cd2-a37a-0167cbe7ed9c | -5.11795 | -71.65144 | 2025-06-23 05:36:00 | NOAA-21 | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33cf33d7-79f6-35c1-b43d-8975d753a4ae | -10.38714 | -67.79056 | 2025-06-23 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ab2e83c-ad99-36f6-b5ab-0d4858ba43a9 | -10.89438 | -56.46316 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 97558235-9612-3fc3-bab0-d30af99d2897 | -10.89362 | -56.46918 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 203c7192-f800-3aff-a458-f6c30018d600 | -10.86657 | -53.76281 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1d64efe-c8be-3b08-96f7-4646d09231a9 | -11.00008 | -68.54618 | 2025-06-23 05:38:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b471fefb-83e8-3c36-9e55-50a19b9b9aa4 | -13.08122 | -54.84756 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2acdf97e-4705-3a49-8d19-ec6d7ea037cf | -10.894 | -56.46617 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73ecc819-68fe-3d04-918f-bd543272ee67 | -10.93224 | -57.12129 | 2025-06-23 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 692efc88-dc5a-39c0-bf2f-8f1704ba0273 | -13.07951 | -54.85511 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7065b0d-f585-3b15-bb6c-5a851b9224a9 | -10.86713 | -53.75831 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c434075-c32e-398a-a799-6a9eaaca91da | -10.92741 | -57.12067 | 2025-06-23 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f182b206-6ca2-3330-8f02-1d1a8620a430 | -10.86936 | -53.75885 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7f22497-7eba-3544-be01-37b467753712 | -13.08627 | -54.84759 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8c429b3-4948-3dd2-bc36-b647cd2af4c6 | -10.88858 | -56.46849 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21bdca3f-ee20-3ee6-8b9e-07c164b8f0f1 | -11.13945 | -53.9401 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c140e39-3010-358e-8589-9b9fc2046c10 | -10.86883 | -53.76336 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a941390-108f-3dcc-9a9b-ae100e8c1f07 | -10.5078 | -53.58887 | 2025-06-23 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cb125f4-33d3-314c-b084-f48af3fb975b | -13.08577 | -54.8518 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 999cc64a-e58f-3de1-8f3c-3feec7160128 | -13.08698 | -54.84845 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f99fc528-d23b-3856-9343-9cf10123f605 | -11.18308 | -54.4068 | 2025-06-23 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67947001-5dc4-35d9-be61-8f801de6be91 | -11.95164 | -58.73843 | 2025-06-23 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a31d382b-35e0-3490-8ef5-ad02f16c5fc1 | -10.88934 | -56.46249 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdae7a16-6b59-3a09-a407-f94e3df2e952 | -13.08075 | -54.85175 | 2025-06-23 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9ef42cc-48ef-39ed-bd17-fb76cbcf17a2 | -10.88896 | -56.4655 | 2025-06-23 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1692ca72-9f4b-3e6b-942a-9b207382948b | -10.93154 | -57.12664 | 2025-06-23 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b0d1edb-18a8-3f52-b840-41b06450fcbb | -10.50834 | -53.58437 | 2025-06-23 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e40b543c-e547-3b04-8f66-f5ad796ff0d3 | -8.0703 | -43.0981 | 2025-06-23 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| fd9569b1-f401-3992-8b93-6b2ac8d1bc4b | -8.07 | -43.1216 | 2025-06-23 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 8ebe7cfd-128b-3b8b-a42c-a79e87b5cdf2 | -8.07 | -43.1216 | 2025-06-23 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 25952d08-507a-39a6-9a4d-f1a1e9b7d679 | -8.0703 | -43.0981 | 2025-06-23 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| b6f08f7d-0f5b-3dd8-9c2d-f9c7f5619789 | 2.75395 | -60.36549 | 2025-06-23 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b53754bf-e99e-3ecc-bd25-25f34303ae58 | 2.74911 | -60.36628 | 2025-06-23 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5bd1700-3b36-303b-8a94-33290f58761b | -8.0703 | -43.0981 | 2025-06-23 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 7ac5934e-5754-363d-821c-8b66a4260a18 | -8.0513 | -43.1001 | 2025-06-23 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 6740d9ee-a048-3fcd-873d-28a535a4df7e | -8.07 | -43.1216 | 2025-06-23 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 2efff446-943a-3c9f-91fe-8b767144c611 | -10.92609 | -57.1288 | 2025-06-23 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03a7b281-8c04-3fac-b7a1-9e5b27f98ab7 | -10.93079 | -57.12691 | 2025-06-23 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a79da6fe-2495-34f6-a2a8-2e1f10fc40f8 | -10.93333 | -57.12941 | 2025-06-23 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce27bba3-f2c4-312f-a0f0-94ff80c3841e | -10.92997 | -57.13377 | 2025-06-23 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8147d8e-7ac8-33bd-9cf5-f3e713c89213 | -8.07 | -43.1216 | 2025-06-23 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 8740c62e-393c-314c-95e3-87d7dcb64010 | -8.0703 | -43.0981 | 2025-06-23 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| a55ab56b-2d38-31cc-9873-194e256c759c | -10.50378 | -53.57904 | 2025-06-23 06:10:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29a5003b-8e29-3305-9c0a-43b661d9d451 | -10.89483 | -56.46893 | 2025-06-23 06:10:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c3a10f5a-c5fb-3bfb-9133-ec4d514ef33b | -9.41282 | -48.41702 | 2025-06-23 06:10:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d472f691-d4a4-359f-bdfb-1f8b150416ce | -10.89665 | -56.45757 | 2025-06-23 06:10:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c52658b8-f85b-3813-a8ff-13f86a86ff3f | -13.24207 | -49.8292 | 2025-06-23 06:12:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8792c2ff-8aee-3a06-a933-1d4ec389ecb2 | -8.07 | -43.1216 | 2025-06-23 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.3 |
| e9c1bae3-4e78-3eac-8ed8-f1ca3282e7a4 | -8.0703 | -43.0981 | 2025-06-23 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 211b643c-1444-3ab6-870e-3bdb40dbc154 | -8.0703 | -43.0981 | 2025-06-23 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| ef1eea8f-efba-3e5e-a174-5a789c07ec8c | -8.07 | -43.1216 | 2025-06-23 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 0cf14890-f4be-3ffc-966a-e8ae990ac1f3 | -8.0703 | -43.0981 | 2025-06-23 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| a55a37cc-c901-31e1-8c6b-29771fb7e0c2 | -8.07 | -43.1216 | 2025-06-23 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 045efc73-641d-3f75-92a6-d81858dadfb5 | -8.0703 | -43.0981 | 2025-06-23 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 4ca442b3-c6df-327d-8255-eebf8abd3727 | -8.07 | -43.1216 | 2025-06-23 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 3345384f-6301-3275-a69d-9d1ca08270dc | -14.0973 | -58.9208 | 2025-06-23 06:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 0f4041dc-81ba-3ebe-a14f-4395a063db3b | -8.0703 | -43.0981 | 2025-06-23 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| ca2dc996-7789-3b61-a44a-d97c20dd7a90 | -8.07 | -43.1216 | 2025-06-23 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| d8b578df-8478-335e-b72b-ab1ead0b57cd | -8.5909 | -51.5746 | 2025-06-23 10:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| bc454f27-beb5-35d1-b40b-264daf0c4e98 | -8.5909 | -51.5746 | 2025-06-23 10:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| c019295a-b036-33e8-be7a-10ce9787011c | -8.5909 | -51.5746 | 2025-06-23 11:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 64b8c697-24c9-34dd-acf6-f89813d5889a | -8.5909 | -51.5746 | 2025-06-23 11:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 2dbf3201-9e7f-37c7-a6f5-19a3a5b39353 | -8.5909 | -51.5746 | 2025-06-23 11:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| a15e43cb-3bd1-325d-b864-476f043bf768 | -11.5812 | -44.6554 | 2025-06-23 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 66e556cb-547c-347a-b38f-590dbde13a1c | -11.5812 | -44.6554 | 2025-06-23 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8335bb12-4ac8-3d09-8e87-4546d8ef7e87 | -8.5909 | -51.5746 | 2025-06-23 11:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| e1847b1c-b848-372b-adc2-e7cc0463f258 | -8.0703 | -43.0981 | 2025-06-23 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 9f983023-5d65-3a02-be9b-fb8c3731fc4b | -8.5909 | -51.5746 | 2025-06-23 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 5fba591b-c039-3571-9e64-d416d3ed6067 | -8.0703 | -43.0981 | 2025-06-23 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| c18c4633-5f69-31dc-9919-03b727cd95d4 | -11.5812 | -44.6554 | 2025-06-23 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| cbb9355a-dd3f-3615-a902-e1b3453ae1cc | -8.99317 | -42.67104 | 2025-06-23 11:47:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f40309d7-a530-3901-9091-eab4bf2f0534 | -8.41163 | -44.60178 | 2025-06-23 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 4f8f6123-2d4f-3843-981f-2d85c7ede01b | -8.79573 | -45.00581 | 2025-06-23 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 29665705-a0be-3e79-9f49-b9e77b51118b | -7.83466 | -44.19956 | 2025-06-23 11:47:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6d76de2e-bfb9-30b1-900c-1cb6c3d6d07c | -4.19441 | -38.36749 | 2025-06-23 11:47:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 5dcfbc1f-052b-3aa1-88a5-6374e26394c1 | -5.66765 | -37.75052 | 2025-06-23 11:47:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e955c420-9307-3b24-b342-a9537ed08804 | -8.07195 | -43.11219 | 2025-06-23 11:47:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 1808817c-b253-3b29-a04d-50763765aa5c | -4.19577 | -38.35812 | 2025-06-23 11:47:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4230c93f-909e-3ce1-83ec-aa5733ba736f | -8.06014 | -43.11034 | 2025-06-23 11:47:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 39685e20-cb3e-3c7d-81c2-bbe05e4cb0a3 | -7.44223 | -45.5361 | 2025-06-23 11:47:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |


[Clique aqui para ver as próximas entradas](README11.md)
