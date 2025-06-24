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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e0bf6d-8f6c-37c8-bfaf-8e321b2efaf4 | -4.543 | -47.9934 | 2025-06-24 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 76214f50-1af7-354c-9a69-aa35e3006dfc | -14.1476 | -50.438 | 2025-06-24 00:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e69fc92f-bcd4-3c0b-a648-78b66c440990 | -5.7887 | -43.6134 | 2025-06-24 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| b340086f-9f9e-3605-8c00-cd660d688735 | -13.0793 | -48.8196 | 2025-06-24 00:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f21f3bdb-dbc8-399b-892c-c389b17c236b | -8.5909 | -51.5746 | 2025-06-24 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c58125c5-c71f-3afb-b82e-fe04675266d0 | -14.1669 | -50.4353 | 2025-06-24 00:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c77d8f88-066b-3186-ac17-dbc2566c0212 | -4.5429 | -48.0151 | 2025-06-24 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 75e51660-2dc9-38c0-b8ae-906a6c8f1db9 | -8.0703 | -43.0981 | 2025-06-24 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 27f59b2c-0800-3a9f-99c7-fcb13a9ac45d | -13.0789 | -48.8417 | 2025-06-24 00:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4c155a05-5f7a-377f-b547-ff1c3cccff6d | -7.2028 | -43.0936 | 2025-06-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 66cd8f8a-f812-343b-8a6b-5dd243eed1db | -17.3435 | -42.6581 | 2025-06-24 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 250.8 |
| fac417cd-131e-3c62-9c48-541f82c55654 | -10.8828 | -56.4767 | 2025-06-24 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 06b007c5-590b-3d77-85fd-09c01bd16d18 | -10.457 | -46.99 | 2025-06-24 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| a5312cf1-3101-306a-8512-46415aa07e49 | -8.572 | -51.597 | 2025-06-24 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| bfc33d13-56dc-3146-ba92-e0c1f8a7c6df | -8.5722 | -51.5761 | 2025-06-24 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 016b7be5-bd1f-3e22-9ddb-9fcecdc66c17 | -10.883 | -56.4567 | 2025-06-24 00:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 6c77340f-261b-3fe3-905f-01dc2e4dd7ee | -8.07 | -43.1216 | 2025-06-24 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| a3075548-84c9-377d-85c3-40e77a533fcb | -5.77 | -43.6148 | 2025-06-24 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 330eef76-1c56-3659-8d02-d8abc2ae3ef2 | -14.4467 | -48.9063 | 2025-06-24 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 3f4853f1-3dba-3480-a635-a10f35aa7d82 | -14.4273 | -48.9093 | 2025-06-24 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8058cbcf-1dba-3ead-8b55-55b599c87b58 | -17.3442 | -42.6333 | 2025-06-24 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9550f999-7e37-3394-a8ae-6e27b0d12f17 | -7.2025 | -43.1171 | 2025-06-24 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| f9ebea88-5aa8-3e76-94f3-fc3f3cb5e3de | -4.543 | -47.9934 | 2025-06-24 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 19b46499-cd00-315d-b70a-7784b43418a1 | -14.1476 | -50.438 | 2025-06-24 00:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e1d96a4d-89a7-30f7-a39a-80e291e7431e | -13.0789 | -48.8417 | 2025-06-24 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 869add14-c4d2-3d8e-9855-bcbfe72a5ffb | -8.07 | -43.1216 | 2025-06-24 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 4c5fd434-10e7-37c5-a432-2d98841cdbdc | -7.2025 | -43.1171 | 2025-06-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 7d48194c-ed20-3637-b4e7-3b6a36eb9764 | -14.4467 | -48.9063 | 2025-06-24 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2dd1fc6f-0f9f-32ff-915b-bc9d8496e2c6 | -8.0703 | -43.0981 | 2025-06-24 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 2289e5f7-56a2-3ad2-9d9c-9d3d6f2c0874 | -14.1669 | -50.4353 | 2025-06-24 00:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| eeba01b6-f12e-35c7-9f64-4c51977759c3 | -10.883 | -56.4567 | 2025-06-24 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 2ad29dc1-0cd6-3cc5-b78f-77b0602278bb | -14.4273 | -48.9093 | 2025-06-24 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3f4546cf-a839-3dca-9345-4f4e87611dc7 | -13.0793 | -48.8196 | 2025-06-24 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ab263b9e-561d-3918-9d6e-c281ef1e4389 | -17.3435 | -42.6581 | 2025-06-24 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 190.0 |
| fa0277ad-9e72-3869-b545-75f95c7b4705 | -4.5429 | -48.0151 | 2025-06-24 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 46d4a087-13b0-3389-9b39-2f3794e8edc7 | -5.7887 | -43.6134 | 2025-06-24 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 17b5d6e4-383e-38fa-9254-263888c61bb7 | -7.2028 | -43.0936 | 2025-06-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 14f527ea-62fd-30c8-bfeb-b3de0835c1ef | -10.592 | -49.4545 | 2025-06-24 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| aa4c2103-20dc-328e-a49e-331ab6d46e31 | -17.3636 | -42.6532 | 2025-06-24 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5888adfa-e1ee-30fb-949e-ec4583939c35 | -7.2217 | -43.0917 | 2025-06-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 8d943680-381e-3a29-b911-39b159399542 | -8.5722 | -51.5761 | 2025-06-24 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3a3da782-5c59-3efa-a92e-9ff696191d5f | -10.8642 | -56.4582 | 2025-06-24 00:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| cb2dde0e-ad9f-3d68-ab77-d6f65a359953 | -14.4467 | -48.9063 | 2025-06-24 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 877d39e0-f1d0-39a0-8fc4-f6d8a9daef08 | -7.2028 | -43.0936 | 2025-06-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| ee848246-6a95-3e24-8732-a3825adb7fe9 | -14.1673 | -50.4136 | 2025-06-24 00:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 210d8a8a-4095-343c-946d-e9d3d3800622 | -4.543 | -47.9934 | 2025-06-24 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cc7efb18-b665-3210-be24-c214200613ad | -10.883 | -56.4567 | 2025-06-24 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d4479d05-c4fc-381a-939e-50aa3575753b | -4.5429 | -48.0151 | 2025-06-24 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 4d7608ba-3350-36b0-aae5-1bed68c5f45a | -17.3435 | -42.6581 | 2025-06-24 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b1bed03c-3aa8-3792-a4e0-7be13dc20a10 | -14.4273 | -48.9093 | 2025-06-24 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c025b7d2-f10b-35e3-8124-58d46f997358 | -13.0789 | -48.8417 | 2025-06-24 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0e294b74-d902-383f-8ac4-e99c27d444fa | -7.2025 | -43.1171 | 2025-06-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| f7b9e404-fed9-319c-887f-a84edb6abd1b | -7.2217 | -43.0917 | 2025-06-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 2274b473-fa62-3436-92f2-f05c8a04c3c8 | -8.0513 | -43.1001 | 2025-06-24 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 9dc8caab-0f46-3aeb-9630-dacc199aa3ed | -8.07 | -43.1216 | 2025-06-24 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| c64d6c32-70b2-3ad5-ad8b-68ad9d4e7ffc | -10.8642 | -56.4582 | 2025-06-24 00:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 8d79feca-73e9-32b0-9c08-f1867f9192e6 | -5.7887 | -43.6134 | 2025-06-24 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 65f744fe-42e7-3067-b32a-c3c2c3afb8b5 | -13.0793 | -48.8196 | 2025-06-24 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 74a8950d-656f-3cc1-ba7d-0236a071f31e | -17.3235 | -42.663 | 2025-06-24 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9fabaa64-6d04-350f-b194-0132523ec471 | -8.0703 | -43.0981 | 2025-06-24 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 26d2b10d-442f-37d6-8ed9-93f6ed77bbc4 | -14.1476 | -50.438 | 2025-06-24 00:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 720d9073-b7c0-3492-89c2-685a9a66a280 | -14.1669 | -50.4353 | 2025-06-24 00:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| d41a5c24-dd63-32e7-9e32-bb10a4d106b7 | -17.3435 | -42.6581 | 2025-06-24 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6f5c76cd-c530-3197-88a5-ed754c10d2c1 | -7.2025 | -43.1171 | 2025-06-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 76e641ae-8b04-31ec-a084-16f3d0b52ef0 | -8.0703 | -43.0981 | 2025-06-24 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| d7ab6904-dd2c-3df9-b0af-22b9d631d7bf | -14.1673 | -50.4136 | 2025-06-24 00:40:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7d6fdafd-ae9f-3cc7-94f9-80859f209106 | -8.07 | -43.1216 | 2025-06-24 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| ad1a5326-e56b-3b0f-80e5-23064761f6cb | -5.7887 | -43.6134 | 2025-06-24 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| c930d9ad-d301-36c8-93ab-6b02d7c55211 | -14.1476 | -50.438 | 2025-06-24 00:40:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9037762e-a944-32ce-99fc-7e1dac7187ee | -7.2217 | -43.0917 | 2025-06-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 540f247d-274f-3920-83b0-28180495be3a | -14.4273 | -48.9093 | 2025-06-24 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2ab8a98d-5c77-39b0-af27-60e18457ef7f | -7.2028 | -43.0936 | 2025-06-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| e1e3b3a5-64c9-3050-b0ea-fa7ee664a522 | -10.8642 | -56.4582 | 2025-06-24 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9942916c-aaf0-35b0-80ef-ab50cb92c630 | -14.1669 | -50.4353 | 2025-06-24 00:40:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 8f45d8bb-a28a-37ac-909d-298b2d3eb492 | -8.5722 | -51.5761 | 2025-06-24 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bd396b5f-94af-3827-b56f-bae89068a31b | -4.5429 | -48.0151 | 2025-06-24 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3cc9da17-404b-39fc-9240-55969eb311e3 | -14.4467 | -48.9063 | 2025-06-24 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7a81614a-9c34-3daa-a2ee-34a04ea1b5e7 | -10.0784 | -52.7393 | 2025-06-24 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| cb066b11-6eed-3bf3-9e76-82faaf46de80 | -10.883 | -56.4567 | 2025-06-24 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3b3ff3ca-cabb-37b0-9f4d-e33d6c2aa9cc | -7.2214 | -43.1153 | 2025-06-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 54ba3b26-3e2b-3c76-b761-559883e03c49 | -14.1669 | -50.4353 | 2025-06-24 00:50:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 84121469-c59f-38ea-a7a2-3a547384a9a3 | -10.476 | -46.9877 | 2025-06-24 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9e7680be-8358-3973-818a-bdbd1cadf6b9 | -4.543 | -47.9934 | 2025-06-24 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3d332aca-c150-335f-b94e-bc52835042af | -7.2025 | -43.1171 | 2025-06-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 00918ec4-fa7a-3b0d-b36a-e66f77f436f3 | -4.5429 | -48.0151 | 2025-06-24 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3d86c86d-1bf6-3df9-90c4-e7f6cd5a4ed0 | -5.7887 | -43.6134 | 2025-06-24 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 9d237d0b-94ec-3c7d-930a-508983fe50f7 | -10.883 | -56.4567 | 2025-06-24 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b9a69898-1841-3747-93b7-c963fcdd625d | -10.4757 | -47.0101 | 2025-06-24 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 198ac009-95e7-3de4-8153-5dae8a6fc451 | -8.0513 | -43.1001 | 2025-06-24 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 4004223a-1e24-3388-94ef-d2e080c65c6a | -8.051 | -43.1237 | 2025-06-24 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 55f17014-3d0a-30ea-8f22-b1eb0a36dd82 | -17.3435 | -42.6581 | 2025-06-24 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 67b926d4-9e12-3115-89be-972b81df40c5 | -14.1673 | -50.4136 | 2025-06-24 00:50:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ebde5437-857b-3583-94df-bd66b18ee6b5 | -10.0784 | -52.7393 | 2025-06-24 00:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 392daaec-9747-3891-a947-e23f88ff2ab5 | -14.4467 | -48.9063 | 2025-06-24 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 424ba53f-2f23-34dc-aa28-32c937018fe6 | -14.1476 | -50.438 | 2025-06-24 00:50:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 427bdab9-516e-39a7-863b-89807dfe9583 | -7.2028 | -43.0936 | 2025-06-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 009117a2-7f9f-35ad-90fe-8fdfb06356fa | -7.2217 | -43.0917 | 2025-06-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 17c1a4a7-d047-3266-a1fd-8ef9387875ef | -14.148 | -50.4163 | 2025-06-24 01:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1d747fad-6545-35ae-b26b-65556c09f574 | -7.2217 | -43.0917 | 2025-06-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 87359148-c9da-3394-8def-2223529c026c | -14.4467 | -48.9063 | 2025-06-24 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |


[Clique aqui para ver as próximas entradas](README3.md)
