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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94271f51-fb97-3515-9aad-9a20d1ae7055 | -10.457 | -46.99 | 2025-06-24 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1bbf5016-1512-3f10-a4b1-47a0eed3cdc6 | -4.5429 | -48.0151 | 2025-06-24 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 78580582-a89c-3502-8386-3434e3b51b6d | -13.0789 | -48.8417 | 2025-06-24 01:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| bab0d93f-44b1-3c1f-96c0-7aa30cb770dd | -10.883 | -56.4567 | 2025-06-24 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 19fc18e1-40c2-3a44-989b-08fdea0a1cd8 | -17.3435 | -42.6581 | 2025-06-24 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7d3776ca-b174-3159-9175-197c4440bd10 | -5.7887 | -43.6134 | 2025-06-24 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| ce5370a0-348a-32ab-9951-90b69f14e22e | -7.2028 | -43.0936 | 2025-06-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| aa3956ab-a0d7-30be-bc33-0cb653a98012 | -10.476 | -46.9877 | 2025-06-24 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 41d205c2-950d-3ace-98c0-25c196228d3d | -7.2025 | -43.1171 | 2025-06-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| e302c571-45f4-39c3-a996-549b3deaef65 | -14.1476 | -50.438 | 2025-06-24 01:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 8bc3c10f-e577-35bd-bcdb-cc46255c20cc | -8.07 | -43.1216 | 2025-06-24 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 799c7d64-893a-3f5a-8524-dd77d986609a | -14.1669 | -50.4353 | 2025-06-24 01:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0bd5c88d-af05-363a-a2a1-5b33257dd74b | -10.0784 | -52.7393 | 2025-06-24 01:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 61d67ad6-deb8-308c-80e4-ce669dd59292 | -14.4273 | -48.9093 | 2025-06-24 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 56c52774-2af5-3168-afec-9eb7bf581ddf | -14.1673 | -50.4136 | 2025-06-24 01:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 0505d1b6-f877-3b43-89e4-5a9eff9e5f10 | -10.4757 | -47.0101 | 2025-06-24 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ae4d6019-ec12-3dc2-940f-647d8e074649 | -8.0703 | -43.0981 | 2025-06-24 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 1ee0f942-7129-36e8-ae4b-c1e8e2b969b7 | -14.4273 | -48.9093 | 2025-06-24 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0d07da07-c89b-376b-a5ad-1777a132ed3b | -14.1476 | -50.438 | 2025-06-24 01:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 5d9d8756-7729-3d97-b93a-3ad97146eb51 | -14.4467 | -48.9063 | 2025-06-24 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8749c41c-fc1e-3729-a33c-eaf1511c528b | -4.5429 | -48.0151 | 2025-06-24 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1aeb407e-3c7e-39e2-85b0-db03eeffc3e1 | -10.0784 | -52.7393 | 2025-06-24 01:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ab930702-005e-3e34-8410-5acfe1b7d519 | -7.2025 | -43.1171 | 2025-06-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| c7f39b77-1cdc-31e6-a675-12dc04d03400 | -8.07 | -43.1216 | 2025-06-24 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| ef135db5-61c9-3a72-939f-4b104f3a04dc | -14.1669 | -50.4353 | 2025-06-24 01:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 6fbd068d-3642-358c-a7cb-f19fcd03818d | -5.7887 | -43.6134 | 2025-06-24 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| cc40dfff-90ab-30b7-b9fc-fc53aa486509 | -14.1673 | -50.4136 | 2025-06-24 01:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0d909e3a-aaea-305e-9284-a370cecc21b2 | -8.0703 | -43.0981 | 2025-06-24 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| c85237ea-d290-34d5-9f2f-794392acca1c | -7.2028 | -43.0936 | 2025-06-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| 4fa08213-9570-3fe8-bb35-ea3b5afe2840 | -4.543 | -47.9934 | 2025-06-24 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 10d5b8c4-8d5a-354d-b142-abe0824c6362 | -17.3435 | -42.6581 | 2025-06-24 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 83f88593-4321-388f-90b8-b17dd2106ce7 | -14.1669 | -50.4353 | 2025-06-24 01:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 53308918-02fc-3d75-94bb-52f7d36bf728 | -7.2217 | -43.0917 | 2025-06-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| e3564de3-fcce-309e-97ca-7cc1425fa5b6 | -14.148 | -50.4163 | 2025-06-24 01:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 66b3cac4-cf0b-34bd-bb8b-64f216d8e13d | -7.2028 | -43.0936 | 2025-06-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 5c86d177-e21f-35ec-85c0-2b0b5a5be8be | -14.1673 | -50.4136 | 2025-06-24 01:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 860eadf7-23fe-3d63-a309-08bf2364378a | -14.4273 | -48.9093 | 2025-06-24 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 43f92472-a031-3538-8002-54e9d8edf2b1 | -7.2025 | -43.1171 | 2025-06-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| d137d52b-4160-38e2-8166-c1d6b7d1ccc7 | -14.1476 | -50.438 | 2025-06-24 01:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0bc3ff87-8167-3c06-92b4-473145dfc11c | -14.4467 | -48.9063 | 2025-06-24 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 97ac6fa0-f047-3fdf-a2ed-01aea1dd6c85 | -4.5429 | -48.0151 | 2025-06-24 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d0090d63-07ef-3b40-80b5-d3be8cbf1944 | -10.0784 | -52.7393 | 2025-06-24 01:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1fab27ca-8f47-3a12-811a-599ce5d05b8c | -8.07 | -43.1216 | 2025-06-24 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 6295780b-a2d4-358c-8f5a-fd193d8da43f | -8.0703 | -43.0981 | 2025-06-24 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 6d0a26af-6f4b-3307-8b43-aa17c5e9a32b | -5.7887 | -43.6134 | 2025-06-24 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| fbe3ce9a-81ca-3a6d-96d3-fbfc90103cc7 | -7.2028 | -43.0936 | 2025-06-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| d4e46e82-6a60-3942-936f-07e7f84e4064 | -14.1669 | -50.4353 | 2025-06-24 01:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 96258e1f-424c-36ba-967a-ae20333eb44a | -10.457 | -46.99 | 2025-06-24 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 8dcdee95-830a-3dc7-90b0-6f661447a540 | -8.0703 | -43.0981 | 2025-06-24 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| d6219ad7-bdf0-3c3f-94c8-8b7efe95e6fe | -14.1476 | -50.438 | 2025-06-24 01:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 603a27ce-48d1-30be-aea6-2b5053f54f46 | -4.5429 | -48.0151 | 2025-06-24 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 57c5047c-14f2-339c-b22d-9d570ba7d077 | -5.7887 | -43.6134 | 2025-06-24 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 1e03063b-0e4c-3a85-94e8-f77e73711eb5 | -8.07 | -43.1216 | 2025-06-24 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 6b5a2dd2-9247-3f6e-8e76-ef6df2a687a0 | -7.2217 | -43.0917 | 2025-06-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 2400cb56-a6b2-386a-978f-5bccbe82fa5c | -7.2025 | -43.1171 | 2025-06-24 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 34657a26-0058-34d9-8f9f-a0c69806201d | -10.0784 | -52.7393 | 2025-06-24 01:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e4bb2ab8-1d4f-349d-871c-1d661041e19e | -10.0784 | -52.7393 | 2025-06-24 01:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e6b9e79f-7f00-32ab-b93d-a94ed657725d | -10.457 | -46.99 | 2025-06-24 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e8ec27de-8444-37dc-a5bf-eed2d1c8924d | -4.543 | -47.9934 | 2025-06-24 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 921130ee-5dfc-3de3-b191-782ba80e4163 | -8.5907 | -51.5955 | 2025-06-24 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| de963b21-1233-37f5-b2fe-8e630d89f2ad | -14.4467 | -48.9063 | 2025-06-24 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8e70463e-dd6b-3622-81ca-5e6a799aca1a | -7.2025 | -43.1171 | 2025-06-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| bd4c8059-2243-35fc-8892-92cc4c6cd1b3 | -4.5429 | -48.0151 | 2025-06-24 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 897561a2-6107-3220-8cc9-c408f50f0277 | -7.2028 | -43.0936 | 2025-06-24 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 5494d1df-d6e5-34ef-89d0-91f6bd85ebce | -8.0703 | -43.0981 | 2025-06-24 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 4047f9b1-b693-3467-a44c-d4b594a5deaa | -8.5909 | -51.5746 | 2025-06-24 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 75ea9299-fa8b-3972-bf22-8f62c97b8120 | -10.476 | -46.9877 | 2025-06-24 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f1568cc6-9ed5-32a7-b9a8-391681adad99 | 2.75192 | -60.36961 | 2025-06-24 01:43:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dc89de10-d385-3472-89cd-7047205063b9 | -4.543 | -47.9934 | 2025-06-24 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 20be6142-8c8e-34cf-ae2f-a6c2d2fd9643 | -8.07 | -43.1216 | 2025-06-24 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 2a623fc8-ae17-35f3-b51e-17347c5c3362 | -10.457 | -46.99 | 2025-06-24 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2d209add-dd40-3851-b800-35e0dbb3a165 | -8.5907 | -51.5955 | 2025-06-24 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6c3ff4a1-997e-3593-932d-97c452c86c94 | -14.4467 | -48.9063 | 2025-06-24 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f73267f2-4dc8-3de6-a4f2-5ae08795e954 | -8.5909 | -51.5746 | 2025-06-24 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3e445370-947d-3269-ac1d-e3ef17115177 | -4.5429 | -48.0151 | 2025-06-24 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 056ebfe3-2186-370b-b14d-a45db460a719 | -10.0784 | -52.7393 | 2025-06-24 01:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f3c69e58-7cb4-37db-b235-bc235828db77 | -8.0703 | -43.0981 | 2025-06-24 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| aee02a70-888c-381a-bc68-982f9ef7064d | -7.2025 | -43.1171 | 2025-06-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 49afd11f-a45b-3bd2-8e36-d0bfd391ca9d | -7.2028 | -43.0936 | 2025-06-24 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 1aafcdb4-5cc6-3781-8a8b-a9f2814b16e3 | -8.5722 | -51.5761 | 2025-06-24 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 286d1815-03df-358a-b712-2a3dab5f4b47 | -8.07 | -43.1216 | 2025-06-24 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| e41a4b92-c645-357e-b5da-18371595ef84 | -8.0703 | -43.0981 | 2025-06-24 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 9f55cbc8-0414-36d5-9e3b-0a14d4a3db42 | -14.4273 | -48.9093 | 2025-06-24 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7709cd3e-aa58-3eb5-b975-a9663494fef7 | -4.543 | -47.9934 | 2025-06-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| cba18aff-c912-3742-9511-9646fe64cfd1 | -8.5907 | -51.5955 | 2025-06-24 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 69cba9f3-9bba-35ff-ad9a-c520654fb013 | -7.2025 | -43.1171 | 2025-06-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 94f5f812-c307-30ab-b5a5-4d3a9f68ce1a | -4.5429 | -48.0151 | 2025-06-24 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 94f8efce-9eb8-3216-a029-64f6c3f40da8 | -10.457 | -46.99 | 2025-06-24 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9fa378db-3ff9-3f34-8b32-51a386f2fad1 | -8.5909 | -51.5746 | 2025-06-24 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3076ddf3-7a50-3ca5-9f5f-bb1cc85e41c6 | -14.4467 | -48.9063 | 2025-06-24 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f568d40d-221e-3dc6-9644-c076ff80f09a | -10.0784 | -52.7393 | 2025-06-24 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 53ee8225-93d4-361e-be5a-999f2e455796 | -10.4574 | -46.9677 | 2025-06-24 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| b63ed2b2-9327-34c4-a7ee-13db200aa3c4 | -7.2028 | -43.0936 | 2025-06-24 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| d6514f77-668e-38de-b1b9-dfe5ebb01865 | -8.5724 | -51.5552 | 2025-06-24 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 81fbf7a2-f5c5-3f2a-935a-6e86d470ea5d | -10.457 | -46.99 | 2025-06-24 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 497ae927-aba5-36ce-9d74-4389d5e80c60 | -8.5909 | -51.5746 | 2025-06-24 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 99627119-7abf-3394-b319-a1607b760834 | -14.4467 | -48.9063 | 2025-06-24 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cb56cd09-e881-32ae-b0cb-68307cb8d8d0 | -10.0784 | -52.7393 | 2025-06-24 02:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| cc7640ac-6f72-35bc-af86-70cc851a8e04 | -10.4574 | -46.9677 | 2025-06-24 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 37bfe7de-e12c-3a43-bcb2-3a14c81a79a9 | -4.5429 | -48.0151 | 2025-06-24 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |


[Clique aqui para ver as próximas entradas](README4.md)
