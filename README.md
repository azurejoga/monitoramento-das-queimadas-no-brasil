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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a008d50-5679-36c2-a0b8-61fa55c5a0cb | -0.9815 | -53.7192 | 2024-10-27 00:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| c23f8958-9ebb-35b4-be8d-da5e46611ab7 | -0.9815 | -53.699 | 2024-10-27 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 391.5 |
| 2809dfd6-5024-3d48-8dd4-4945f0b8144a | -0.9815 | -53.6789 | 2024-10-27 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| f625f67b-d6a1-33a6-bc39-36e405c7fb78 | -0.9998 | -53.719 | 2024-10-27 00:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ebe80a0c-3aed-3270-96aa-3d4004500e31 | -0.9998 | -53.6989 | 2024-10-27 00:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 351.3 |
| c042013a-5897-3563-9b7b-9bf4adbe2d74 | -0.9999 | -53.6788 | 2024-10-27 00:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 540ea516-0e0d-3657-a546-f32fc329bcba | -1.1831 | -53.8985 | 2024-10-27 00:05:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| acaf4667-44b0-35c0-a657-4c2fb0ff82be | -1.1831 | -53.8784 | 2024-10-27 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6970998b-f59f-30c4-a7a0-d2ded885983c | -1.7874 | -46.4065 | 2024-10-27 00:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e9e28c2a-1a45-30f4-8c29-a79ea85dc959 | -1.7875 | -46.3844 | 2024-10-27 00:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cd960b06-2889-3aef-ab6a-dc8fb635a639 | -1.8059 | -46.4062 | 2024-10-27 00:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d4d03f24-bf5e-3f40-affa-0bcebf888254 | -1.806 | -46.384 | 2024-10-27 00:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f59d4e50-2ccf-3b72-b8a0-581605e05988 | -1.906 | -59.9839 | 2024-10-27 00:05:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 171be707-b162-3f60-8912-a04e0740f194 | -1.9243 | -59.9837 | 2024-10-27 00:05:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ca7c0b09-4dbe-3a80-91d2-3b3d4343ba1a | -2.3578 | -47.6641 | 2024-10-27 00:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 16457558-aefe-3fd0-8398-ec05e8409bff | -2.4598 | -50.412 | 2024-10-27 00:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4afd665f-c87a-3e3b-be90-936d6751c8a6 | -2.4786 | -50.2858 | 2024-10-27 00:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2f09185a-91fc-3438-90eb-6f070c47c0a5 | -2.486 | -48.0507 | 2024-10-27 00:05:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 90fd7ee6-5b0e-3084-b245-dc362ee4029a | -2.6321 | -54.2975 | 2024-10-27 00:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f1da457e-3eb8-3ed4-b196-3fff2c7cf613 | -2.6482 | -49.2465 | 2024-10-27 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| dd571214-2ea8-3b08-a42f-a2ba469c4df0 | -2.6483 | -49.2253 | 2024-10-27 00:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8437d287-2e47-3405-b918-75edaf3fcc36 | -2.6505 | -54.2971 | 2024-10-27 00:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5923b23a-b5da-313f-a65e-ede1d638f8bb | -2.7033 | -49.33 | 2024-10-27 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 3d5cbb19-a404-319a-ba46-fca96b159ec3 | -2.7034 | -49.3088 | 2024-10-27 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 260527b0-cdfb-302b-92d0-4a91e42df739 | -2.7611 | -48.7098 | 2024-10-27 00:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4c48d882-980c-3eb7-a7f7-6089dc655a81 | -2.8145 | -49.2418 | 2024-10-27 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6c5cf7a9-b327-32d6-8496-92e99d498ee3 | -2.833 | -49.2413 | 2024-10-27 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 5864ca6a-e487-3e41-b794-8f77411128ee | -2.8501 | -45.0131 | 2024-10-27 00:05:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 267.4 |
| c9b95bfb-e925-3a08-bb3d-34329e956977 | -2.8502 | -44.9905 | 2024-10-27 00:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 338.7 |
| acdd5dbc-5ed9-3e29-925b-9adee471ab8e | -2.8422 | -51.8148 | 2024-10-27 00:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7faf6148-6db4-3bf6-8daf-011f1962dde4 | -2.8423 | -51.7942 | 2024-10-27 00:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e18c735c-e986-38ee-b4fa-0ea88bf6fb8c | -2.8687 | -45.0125 | 2024-10-27 00:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 285.8 |
| 6bc98c4e-145f-341a-bb34-705227c053ea | -2.8688 | -44.9899 | 2024-10-27 00:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 334.6 |
| 2f79fabb-eb8d-365d-8638-68e9238a1bf6 | -2.8939 | -47.8655 | 2024-10-27 00:05:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| dd19973b-15e3-3ee9-abed-1352749974da | -2.8939 | -47.8439 | 2024-10-27 00:05:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c386cf24-67b0-307f-9f0b-6adfaa000c0c | -2.916 | -51.7716 | 2024-10-27 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| d2b18192-6e38-3e3b-9dae-c22034f5c099 | -2.9161 | -51.751 | 2024-10-27 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 48a8d377-f747-3ed6-8b17-369ffb37d901 | -2.9214 | -50.295 | 2024-10-27 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 988a758d-bd04-3d28-bf75-9c377b025101 | -2.9215 | -50.274 | 2024-10-27 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 226c1abf-9572-3157-b30b-78c56c87ce4f | -2.9345 | -51.7711 | 2024-10-27 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e2b19f2b-2337-335a-af3b-204fbfd13b00 | -2.9345 | -51.7505 | 2024-10-27 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 77c301af-fc1f-37f5-b404-166398476f89 | -2.9399 | -50.2735 | 2024-10-27 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 06c5ae5e-6098-3e3f-afd8-e8bd60ce7b7b | -2.9669 | -53.0389 | 2024-10-27 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| e55a5d4f-9e63-3568-8ba5-0bdcb4759060 | -2.9853 | -53.0384 | 2024-10-27 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c4ddb29b-998b-3f8a-9697-38019e35d0d8 | -3.0703 | -45.6575 | 2024-10-27 00:05:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| d158a34a-11b2-37a9-b3e0-fbe23d9bc4ae | -3.0888 | -45.6568 | 2024-10-27 00:05:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f9c32f3c-ae0a-3000-9cef-7f8be2314501 | -3.1106 | -44.9809 | 2024-10-27 00:05:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8f63ba01-f1df-30b0-b1dc-7e035abcf6da | -3.1292 | -44.9801 | 2024-10-27 00:05:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 98255a0f-3c93-3481-88ea-dded7258a971 | -3.1242 | -50.3519 | 2024-10-27 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 364d1180-c010-373b-b4f7-6d5f6f939131 | -3.2486 | -51.5558 | 2024-10-27 00:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 53559c59-f4eb-3d6e-bb6f-19211cf87014 | -3.3256 | -50.7641 | 2024-10-27 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 83f9b23c-fb9f-368c-b803-f2be76ccbd65 | -3.3256 | -50.7432 | 2024-10-27 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| efce7d19-dea5-3ef2-a2de-312526356d9d | -3.344 | -50.7635 | 2024-10-27 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6ebb54d3-0a2a-3662-a2f8-f06b73163a30 | -3.3441 | -50.7426 | 2024-10-27 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 13a0c44c-96a5-3177-aead-8c9ac318507e | -3.4392 | -50.0896 | 2024-10-27 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 136128f9-1197-39b4-8c09-c4d4638f9b9d | -3.4577 | -50.089 | 2024-10-27 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 161536dc-0a44-30e3-b674-4267ff52fc8a | -3.4762 | -54.5772 | 2024-10-27 00:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 9f7ed5fa-b9bc-335e-8843-5ef6992deac0 | -3.4763 | -54.5572 | 2024-10-27 00:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0dc2868a-5636-3e36-9efd-5df88c9ed83c | -3.5626 | -51.4217 | 2024-10-27 00:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 8c371b20-42d2-35f4-906c-f139e859a8d5 | -3.682 | -45.9455 | 2024-10-27 00:05:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 503f8a27-2553-3d53-96bf-a6807a378167 | -3.7934 | -49.4849 | 2024-10-27 00:05:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| cdb2e8c4-84f3-3559-a200-9c512241c1d4 | -3.8149 | -48.8874 | 2024-10-27 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 19cb0773-7762-3b71-a6f1-d1612ebf1d60 | -3.8334 | -48.8866 | 2024-10-27 00:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 18274d40-1ebf-317c-8592-a7ac5e62a6cd | -4.3841 | -49.7571 | 2024-10-27 00:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 687715a2-9ea9-3950-be67-9f16a835e1cd | -4.4696 | -50.9926 | 2024-10-27 00:05:31 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| cb317dbb-f3c2-39c0-8201-2381d374cd47 | -4.6258 | -49.5977 | 2024-10-27 00:05:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b2596f90-50a3-3ece-8f2d-bfa1d7a902e0 | -5.0072 | -45.4275 | 2024-10-27 00:05:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4840ad7b-4e32-3f22-9e66-01fb698f793f | -5.2896 | -60.1632 | 2024-10-27 00:05:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b477283b-21f6-31d1-a0ef-d98b2d94c123 | -5.4068 | -46.8076 | 2024-10-27 00:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0877a202-25a8-352f-b73e-44678edca11f | -6.8534 | -45.8794 | 2024-10-27 00:05:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4466b2d0-1a79-3e9e-a717-1db6cd1622ea | -7.2264 | -46.0498 | 2024-10-27 00:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d2108b23-9f65-3ded-b163-a86237fb53da | -7.2267 | -46.0274 | 2024-10-27 00:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 04739f90-f905-35a2-91fd-94c0bfdc2d03 | -7.2452 | -46.0482 | 2024-10-27 00:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9968ca39-3273-35e7-addd-2d4e0ff74348 | -10.5234 | -45.1488 | 2024-10-27 00:06:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 7897f2a2-9695-3af8-bfeb-4b91a44179d4 | -10.5424 | -45.1463 | 2024-10-27 00:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 7a552733-542a-372d-9a67-51be5df46b7d | -12.6646 | -44.2297 | 2024-10-27 00:06:16 | GOES-16 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 08103e74-3fa6-301c-8219-4255a3418dd8 | -13.3803 | -45.1149 | 2024-10-27 00:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 93c6e5a7-1742-321f-894f-23f6ac59a61a | -17.2358 | -46.7619 | 2024-10-27 00:06:41 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 41efdab1-a094-3f61-804e-134e8e309c67 | -17.52732 | -39.47034 | 2024-10-27 00:07:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 33b07ad1-216e-37f3-901c-a499b96accd2 | -14.23796 | -43.08576 | 2024-10-27 00:07:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 3d4f2f0f-7c5d-3c2c-b630-0474065c6f0c | -13.48323 | -42.45956 | 2024-10-27 00:07:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 753f319f-42aa-35fe-98b7-ff08381c67f6 | -9.79242 | -36.54626 | 2024-10-27 00:09:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| df7ec006-cca4-3452-bbc7-b62d4ed7d8ab | -9.65119 | -36.06295 | 2024-10-27 00:09:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 2b142404-4ae1-3aa0-b973-2c31321d050f | -9.64995 | -36.05404 | 2024-10-27 00:09:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 50.7 |
| 95ec1c42-9ce0-328b-a42c-927ed9b0f99c | -9.64111 | -36.05532 | 2024-10-27 00:09:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ee47794c-6b02-37a9-aef3-66f0a2413824 | -9.62317 | -36.1852 | 2024-10-27 00:09:00 | TERRA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| bed42bb4-026a-327a-aa44-17951fae390b | -9.46917 | -40.38929 | 2024-10-27 00:09:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 03a81434-8c7f-3f6b-b4f6-5ce18a32b981 | -8.79818 | -40.87542 | 2024-10-27 00:09:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4acde5b8-13ac-31f0-abc9-ec36f7640be1 | -8.63057 | -41.17403 | 2024-10-27 00:09:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 42.3 |
| cf07ca19-0d91-3a4f-b4e6-d57214c75b0f | -7.95383 | -39.34227 | 2024-10-27 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 5658d723-1bd2-379f-bd1b-3786829ae364 | -10.533 | -45.15213 | 2024-10-27 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 8e6d6589-4f0b-38b9-9344-b104d1d8a342 | -7.95238 | -39.33138 | 2024-10-27 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 17.0 |
| cf3e27a3-f556-39a5-bd8a-459b58893d5e | -7.71372 | -37.43732 | 2024-10-27 00:09:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9ac35e9b-38bd-313e-8a12-1896ecd7323f | -7.71247 | -37.42828 | 2024-10-27 00:09:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| dc349bb6-1049-3c29-9656-b65b2d6dfdb7 | -7.56116 | -38.75644 | 2024-10-27 00:09:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 4f1ab0c7-c7bd-36be-a96d-9f2e0cd17365 | -7.55982 | -38.74641 | 2024-10-27 00:09:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 843b83bf-58da-3739-a746-66e551ce2c63 | -7.55181 | -38.75782 | 2024-10-27 00:09:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 53a18f57-2ceb-3c8c-818e-81d7b9a4df45 | -7.25119 | -41.2271 | 2024-10-27 00:09:00 | TERRA_M-M | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| fde76f59-e350-326f-a174-27551cc73fbd | -7.10916 | -35.28922 | 2024-10-27 00:09:00 | TERRA_M-M | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 16d33226-9a3e-3958-a5ae-1f50010c48fa | -7.10783 | -35.27987 | 2024-10-27 00:09:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README2.md)
