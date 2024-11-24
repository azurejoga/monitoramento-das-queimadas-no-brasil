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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c19c6b5-ba27-37a0-8dc6-c39952ae819e | -5.38474 | -45.76132 | 2024-11-24 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ce79581-6449-3971-9f96-42faabb23695 | -1.42714 | -46.05815 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc8065dd-e161-3a9f-ab10-206a2f0006a1 | -0.9162 | -51.65076 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72b45cba-b677-3458-ad32-9f0139f58164 | -3.55279 | -51.53695 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6205fa70-cf8a-3c18-862b-c37a9e276bbe | -3.68343 | -50.11496 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a561375a-b413-3de5-a17a-7d668e27aac0 | -1.42997 | -51.12548 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60b5c1d2-9d75-3c29-8826-67453ca7a94f | -3.86129 | -50.05637 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e238983-40e6-32a3-a295-740c735a8ba4 | -2.70458 | -46.2864 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfeaffeb-b5ed-3647-b952-c5527bfe6989 | -1.16991 | -49.46824 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b05fb52c-899d-343a-9825-3ae9f98e02b1 | -4.34926 | -48.88773 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4717b295-c4fb-38b3-828a-7b58cef09367 | -2.86353 | -53.93703 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbec68c4-e2cf-321b-b8a1-8de2feab7d88 | -3.50759 | -53.819 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 75d2296c-4444-3d9b-b72b-b0a8fc523b79 | -3.49266 | -54.02223 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff4605b7-f4bd-38bd-a9a5-ac23488ef465 | -1.95117 | -49.52238 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b39a4fc9-66bf-3292-bcd5-0367f120c6a6 | -3.51097 | -53.81957 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d12417ff-1ce3-3fba-8cbf-0a3107d696de | -3.84568 | -52.38763 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 843660f1-a2e7-3349-ae38-aef67097a46d | -2.09773 | -50.36871 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5970a1-bba0-3348-a214-85a2b6ee5e62 | -6.84035 | -44.38908 | 2024-11-24 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60bc600e-c909-35f2-9d06-86339803349a | -2.99381 | -53.73597 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e04dd60-32a2-339d-be7a-1cbbef859aa1 | -3.04908 | -53.04193 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f083d16-7fc5-39ba-9a1c-9b7df0268b45 | -4.64041 | -48.84219 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c750e7bf-5b8c-3006-b3e2-212442503668 | -2.91377 | -54.28469 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd578ea8-5067-3f93-ac2b-0f83af6f47c1 | -2.79669 | -48.68343 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b04b28b2-cfbf-365c-b5a6-347e4439a2af | -3.85448 | -51.14742 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e25dbb92-4088-382e-a110-bab092fe4b16 | -3.13675 | -55.1175 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e37717ee-a0f4-365a-8414-a44657d4be69 | -2.96048 | -53.88022 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a877d465-cf37-36db-b5b9-c99cc228969e | -1.28898 | -51.74417 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34b10849-1571-3cec-a1b5-bf759acab9db | -2.83296 | -54.01936 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daa520c2-3084-3c9f-a6a8-cc7c14bdd6b0 | -3.79101 | -51.92792 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ad79cef-a944-3d6a-a924-b8ec98d68bba | -3.48065 | -49.90354 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab0f2997-2706-3249-83ca-9a91820cfefd | -2.71377 | -46.28337 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc24f5f9-d927-36e9-a355-0f53db47f636 | -2.82611 | -54.0183 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8927f8a7-9abc-3795-a5ea-343167abd97a | -4.21776 | -50.40469 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c162d71d-25ba-3d36-a168-fa90a43de54a | -1.44851 | -53.40113 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30ebeca5-7b57-38b5-ac0f-b7953677629a | -2.99225 | -53.36131 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd18b057-8592-3c3f-ad45-c6e5828b845b | -2.92274 | -48.95772 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2b395a-efe0-3f00-b3c6-2a55a55611ba | -2.08104 | -48.873 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4cda432-3efd-3d7e-a64e-d97920018e2c | -9.81316 | -48.1673 | 2024-11-24 04:53:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f208192a-3f81-3b51-bd9a-f2e9c55a3469 | -2.21639 | -46.39238 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5606baca-1cd6-3d93-80e0-67814c8c4888 | -2.81183 | -54.01986 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 062f77cb-f95c-368a-9c16-975a95aeb968 | -1.22706 | -51.79432 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31fac87a-67c7-30d9-b6c2-c384b8ab5a7a | -2.62307 | -54.25986 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c678f49e-17ba-3533-aeba-9e5bf410a60c | -3.64567 | -50.22402 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afa274ca-4469-3ad2-9049-9e58b07afd45 | -3.47364 | -43.88783 | 2024-11-24 04:53:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54e2e63a-c6d2-3d24-b27d-f9a4d864cd37 | -3.29972 | -45.72945 | 2024-11-24 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e0582f8-30e4-37e6-969c-9dbd4329ef72 | -1.77463 | -53.62676 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f9b3019-f0a0-3697-bbe9-c65560d38b70 | -4.51576 | -45.80656 | 2024-11-24 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b60f4394-5a93-3765-a3bf-40fd98341310 | -1.27341 | -47.86567 | 2024-11-24 04:53:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffedae47-825e-3e5b-8006-12f22cc32d00 | -2.6699 | -46.14405 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a37f31-d761-3a54-a95e-f4fc6114da27 | -1.04419 | -51.74433 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6747aba-adce-35a2-bffa-de598956dc2c | -1.69991 | -48.73041 | 2024-11-24 04:53:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13da9a7a-106d-39ce-ab6d-90165da1febe | -3.31454 | -46.66794 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e806b5b2-7a7e-3034-8466-891e6144ab5b | -3.29399 | -49.91096 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 475f38b1-2838-390f-925a-ed290c92a2a8 | -3.44404 | -50.43948 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4928840-fcf2-33a1-a78a-bc1e54a1044c | -2.22732 | -50.76702 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9b9b53b-18e8-3085-865f-1786f4b70afc | -2.9431 | -54.07779 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f132000-8cc3-32f1-9f89-91e18de4ec1c | -2.32227 | -51.31407 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c8490e-97e8-31e1-88c4-59496ecbdd22 | -4.48532 | -48.11344 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97883ac5-a5c0-39d1-8980-a684a3d36ecf | -2.54819 | -54.04452 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7469d962-1f34-3a53-add2-7b0a04c27736 | -2.63605 | -51.89881 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cd1c2e5-3174-3d20-8b4c-cbb61969891b | -1.29005 | -51.73731 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c2ee6e1-00d4-312e-a656-8c2e7a61a4f5 | -0.25515 | -51.59298 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049a28cf-9afd-3f67-84cf-6c28b90ca1bb | -3.5183 | -53.81703 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e249f929-86a3-35ac-b0d0-af1541612395 | -5.10272 | -43.14787 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23865ddb-0462-3313-938d-19de92e86fbe | -1.22322 | -51.79724 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8307168c-e916-363a-9ebe-6b81130338c6 | -3.08937 | -51.32313 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f0d8ee4-3d31-398f-8623-1408598da339 | -1.73608 | -52.73668 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f59f2347-1f92-347e-8745-26cad3ab9274 | -3.67877 | -47.13287 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8afc8512-a0de-3a02-8551-6f36c32e2a4a | -2.70036 | -46.28574 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42dbef50-44f1-3579-8868-75402df6a74e | -3.28806 | -53.82996 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f0f53d-b02b-3f4e-a338-ebdb0b68541f | -5.58929 | -45.21041 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0799fac8-fc91-392f-b9a2-b9c60bfcb6a4 | -4.30932 | -48.0774 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e99ab142-df13-365b-bb5c-18158b089781 | -3.60708 | -47.5133 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28313946-03db-3e42-bff0-25dcc1610924 | -3.42211 | -53.28712 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f96c15d-7785-3e9b-94fa-a058b6021d2b | -3.21919 | -53.84126 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9cc3ee7-e324-35a0-bed4-182673276633 | -0.90066 | -47.91211 | 2024-11-24 04:53:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b61f864-7da1-3c74-8fed-03dbb527f33a | -2.85329 | -53.93547 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f47d9e9-2c99-34b7-b04f-55c3911239ef | -3.67795 | -50.81445 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07085a98-3c3b-34fa-a65a-80e8a2a11348 | -3.48071 | -50.43334 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c89f6b52-d308-364b-b68b-7d17c1533a46 | -3.6 | -54.05416 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798658a6-689b-356e-8ce5-680addda84ef | -2.12537 | -48.95747 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a580620-6fa5-3794-a647-75f24289d743 | -2.53725 | -47.36393 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 636ae48e-ab5e-3c08-8a96-4746edca2a96 | -5.14578 | -50.64187 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76d3fca-3308-3494-b9bb-b27afeb4a000 | -2.03563 | -51.188 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66a5d0b0-400e-3d5e-a4ad-4c48e8505adc | -3.15895 | -50.58529 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4df149b-b557-323e-a660-fe7c34c5527a | -3.16289 | -50.5822 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66fb58e2-5bbf-39c0-939f-30f6010b2b65 | -2.44164 | -46.13611 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45375792-b773-3850-97fe-2f65b6c76ca7 | -4.51378 | -45.72392 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ed2ed60-76f5-341f-b84f-22f1674e6ddf | -0.92931 | -51.63172 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f801482f-3a93-30b1-9882-0607635e94c1 | -4.05972 | -53.64822 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0045c84f-00fa-3b19-b2f8-6b8f44b18e1e | -2.56496 | -54.00485 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b37943d2-9b5b-3e4d-b51f-f8b1288f0c88 | -2.5126 | -52.1222 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e9f6193-310e-3bbf-89db-279c57d72478 | -3.85088 | -52.311 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3e16582-bd6e-3ec0-84c3-067f10d13aae | -3.27125 | -53.81951 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4cf61e28-ef1a-3a6e-90b1-3c29211d57d7 | -1.30063 | -52.28078 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cc6154f-645d-354a-ba8c-4e3c5fb4ac1d | -3.93997 | -48.14314 | 2024-11-24 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23d0b00d-2251-3976-bb7a-90bafbe63ec9 | -8.47308 | -63.93628 | 2024-11-24 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56ca7aff-2204-3fb3-a1ec-fa9861a08cf1 | -2.14566 | -49.10852 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e5a44e-917c-3048-ad8b-b9b4c60efc57 | -3.9873 | -47.73155 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| efdc6860-4efb-371e-9953-8a9f59b0b80c | -1.37112 | -55.40382 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README51.md)
