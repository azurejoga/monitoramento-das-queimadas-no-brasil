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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7816e5e4-d5ca-39a4-946e-c0b98bfea84b | -3.71383 | -57.26628 | 2025-08-27 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65a0794c-cd89-3ab4-9b8f-eca8e723ec9b | -3.85195 | -55.81153 | 2025-08-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d11ba12f-c5b2-397f-9a9d-e10e19bb31bb | -5.75901 | -53.76667 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab386ec2-f356-3087-be07-d87a7c095bb5 | -5.7601 | -53.75933 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ceb040d-617d-3f5d-8c10-14afd5bfcece | -5.76256 | -53.77084 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7029a192-987b-36d4-a110-85b9840094d9 | -3.79749 | -51.19088 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2143afe8-8d5b-3a78-876f-81d6855dcb82 | -4.96309 | -55.81256 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6faf4fa-9dda-309a-abda-4284c8494a07 | -4.96187 | -55.82071 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9c86fca-6663-37b1-97b9-3ad6775e423d | -4.55715 | -55.96083 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 626b2c1c-745f-3a34-a453-1cdb7611afe0 | -3.42053 | -49.04237 | 2025-08-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f7ee206a-5905-35b8-8096-735b3839b8b8 | -4.95952 | -55.812 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a561584-a6e0-36e4-ab7d-acd8cd15a8f1 | -3.79906 | -51.19194 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0806dc6d-d642-346c-a660-e8ae9de7b909 | -5.75792 | -53.77408 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5af2d977-5511-3d5d-8964-651398a03286 | -4.09501 | -55.80867 | 2025-08-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e227a467-91ca-37a3-a23b-6faeb4dbc445 | -4.1126 | -56.34102 | 2025-08-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a1a7f75-4989-3c08-b958-9446de04a3b7 | -2.91768 | -48.30801 | 2025-08-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9012a996-848e-379b-aded-abd69584087d | 0.77604 | -51.33255 | 2025-08-27 05:16:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 322ac373-227b-3b7a-a20f-ae2222d1c248 | -3.85256 | -55.80755 | 2025-08-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac89a72c-e60e-301c-acd9-ef9c25210538 | -3.20004 | -52.25558 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a053e12d-0135-3c69-9129-7133cf4968c9 | -2.4442 | -47.33235 | 2025-08-27 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32c1b1b-b5f4-3a75-b9bf-817453df3b6f | -5.23207 | -59.99837 | 2025-08-27 05:16:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31109476-e90e-362a-923c-5113434449ae | -5.62227 | -45.72483 | 2025-08-27 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d1e4346-b49e-322a-9c52-986e223a7c54 | -4.31463 | -55.26799 | 2025-08-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0bac0e8-2c36-359c-bb13-a39f1cd3c050 | -4.70062 | -56.06659 | 2025-08-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2252d5b2-d5e0-3da0-afeb-b687e5067e21 | -5.62172 | -45.72663 | 2025-08-27 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eeddbe6-d192-3f8d-ba31-d46ae9ca0eb9 | -3.19398 | -52.25567 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e56c720c-77d7-38af-bc76-625ecc88f003 | -4.31287 | -48.09827 | 2025-08-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 165eb47b-a2fc-3be7-bb08-eef1d18c3c40 | -6.57102 | -47.38575 | 2025-08-27 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76ed4c3f-fa17-3e55-ac75-eadfa45b7db1 | -2.91822 | -48.30418 | 2025-08-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88611b75-0a0d-3bac-98cf-84ff78b2fbd5 | -4.96484 | -55.82526 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f3e8a47-88ab-3a82-806d-fdba7d2bc7f0 | -4.13021 | -54.90038 | 2025-08-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d1b72d-2936-31c7-9fd4-9a4709a2284b | -6.57167 | -47.3807 | 2025-08-27 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53c8be96-4622-3183-8141-e8eeb3a67a40 | -4.96013 | -55.80792 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab70a991-1682-35bc-85d8-3877ecb0a41b | -4.56069 | -55.96137 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b31469d0-d8c7-377f-bc9b-c4a914ba035e | -6.57486 | -47.38342 | 2025-08-27 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d045c15b-6e14-3309-84ee-ef39ef930393 | -5.62865 | -45.72742 | 2025-08-27 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9801ab86-aba6-3a01-adec-58e31c917355 | -3.42001 | -49.04594 | 2025-08-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d0cff8eb-c586-312a-99bc-be719a348183 | -4.95891 | -55.81607 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a663ae92-e57a-34be-9f1e-4eca4233588d | -4.70414 | -56.06714 | 2025-08-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6069926c-29a5-3380-b50f-f2f6c23b1963 | -3.98395 | -51.06102 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10b92552-8dde-3a3f-b526-231b36ee5ffd | -4.11606 | -56.34156 | 2025-08-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcb33050-60e1-386f-895e-ae59b42f8c61 | -3.98678 | -47.88507 | 2025-08-27 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c1c15a0-3a73-3b57-a47a-7745611b431d | -2.92124 | -48.30335 | 2025-08-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5820e867-c69f-36c8-be81-39c212f1924b | -3.97993 | -51.05514 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3be75f09-3d21-322d-b6b4-fb6612e6e8ef | -4.23349 | -54.88359 | 2025-08-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afce47dd-2311-3295-92bd-176ae729e360 | -6.16256 | -53.82388 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae2ebe89-56db-3a3a-bc0b-cd2c92b5516a | -1.42534 | -60.39923 | 2025-08-27 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecd82356-2ca9-3b53-8e11-7817fac8e02c | -3.74677 | -49.05056 | 2025-08-27 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08289d6-9532-3ec1-ac79-5b9e16abbdc9 | -3.74132 | -49.04964 | 2025-08-27 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bdea605-d990-3722-801d-ec38ce8042d6 | -4.48116 | -47.66668 | 2025-08-27 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2127f612-4d0b-3d46-8e4f-ef61b6948885 | -5.75846 | -53.77039 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60a8e32d-0f1d-3bf9-8dad-22f60e4091f0 | -4.31227 | -48.10247 | 2025-08-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 40b8b750-564d-3350-9be5-84f95c655c19 | -3.79977 | -51.18703 | 2025-08-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c45bd90a-d820-3b79-8f2b-fd30491d584e | -5.66486 | -47.49197 | 2025-08-27 05:16:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c26bbaf-d9b0-3490-ba04-0fe8453e4e28 | -3.78797 | -52.38368 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52e85db1-9bc0-3cf4-b21d-f2b19a107c7c | -4.96842 | -55.82577 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd2a235-313c-3810-8bd0-4fb60fbf8c46 | -5.76202 | -53.77448 | 2025-08-27 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2897eef-e0db-32f9-823e-438f89c286ce | -4.9637 | -55.80846 | 2025-08-27 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 814259c8-c7be-36de-b59e-6ab3e059a2b2 | -7.7437 | -61.08172 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 242bcb7f-85ee-37c7-b39b-6b72e741d86d | -11.03167 | -52.02756 | 2025-08-27 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c852f30-85f7-3624-8950-6857f4527543 | -10.03057 | -59.35474 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b83e5e0-7fd5-376b-87ee-1891f6ce5621 | -9.12831 | -60.72589 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f4de06-d8bc-3a0f-9e75-0a9a04b61cfe | -9.20878 | -59.436 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6550da9-2659-3ea8-8136-9437fd298a3e | -8.07814 | -61.53378 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837b8787-078e-36a1-b0a7-2416952f9344 | -9.57311 | -55.38165 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19dbafe6-3cda-3374-b741-fa08f4aa49cb | -10.15498 | -64.24535 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a4d14f7-1c78-3808-976a-d71d4f1e0762 | -9.16292 | -59.46742 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14cc1481-7f43-37d8-8064-b3a71c70031a | -9.20804 | -60.8224 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd3385c6-cfe9-3fd6-8049-aaff36793ceb | -9.26801 | -59.77662 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8d45161-3fde-3805-8435-f06b007099ca | -12.87047 | -48.10029 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5a1e31d-18e7-334b-adc8-42c3727f8168 | -9.16545 | -60.77187 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a899abbb-d80e-35d3-9199-a97e178ac42e | -12.49882 | -47.23679 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d321b647-7641-37fa-adc9-4a70cb4d2af4 | -8.95688 | -65.95943 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aa9f55ea-e6e5-3b07-8bb6-3459e93b5eed | -9.41855 | -60.5054 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7023b599-9d9f-321c-9ea8-87e3ff5678ad | -9.41523 | -60.50488 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16cf548e-0b94-3a1a-849c-66e82a66f938 | -11.81618 | -46.80947 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a211d24-feb1-3ab3-a56b-acc85bbd0f93 | -9.79082 | -64.26664 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a591a809-054e-3795-9968-8d963cf2b4e7 | -8.90073 | -60.55142 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c813a05-3934-37b6-8e52-8990025d54c9 | -10.09062 | -62.89175 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 47aaebe0-4d29-3403-9957-4310597d775f | -8.56101 | -51.3582 | 2025-08-27 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dce9a681-7e53-37fa-9322-561df8476979 | -6.69009 | -58.85972 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11bfa979-a77a-30ee-8a13-8ce6901bfc26 | -7.25835 | -57.67077 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 40a985eb-965a-32f4-8962-8510952d4832 | -9.17968 | -59.47067 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68eb9896-867b-3e7c-bd05-f377b95851b5 | -6.79225 | -59.64115 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2efbbf-ecde-3842-b89f-2d956d5f607c | -6.24642 | -60.01828 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f98bf98-1652-37d3-97f6-d74ba18cf506 | -10.49037 | -51.59717 | 2025-08-27 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a0aa0d7-3ab0-386d-9546-b6ec3ec575c6 | -8.90108 | -47.33103 | 2025-08-27 05:18:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 305f0752-129c-33ba-addf-fcc300d712e3 | -8.94024 | -65.95219 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d00ca00c-8932-331e-a8a1-894a5f0645ec | -9.16122 | -59.56752 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b715cfd1-7a32-33a2-8808-54b3e4e21e65 | -8.85267 | -62.45112 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a813993a-41c9-3e1c-8fc2-e8ce4ad4bae2 | -8.99342 | -65.41634 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74ba5d92-93a1-3c82-ab07-8214d0c705b4 | -11.31584 | -55.21144 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8def6ee8-69eb-32a1-991a-cfb0b41fa7b5 | -11.8035 | -51.46733 | 2025-08-27 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d47b30e-5082-3a18-8f5f-587bd5ab06ac | -9.58614 | -55.37344 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97066e8d-a390-34f8-beb3-b379473658b5 | -8.33801 | -62.9306 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00885fee-e28c-397c-a38a-08d3723ed44b | -9.14 | -65.27174 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f697c7ad-b431-3438-bc4c-d8dc0e6b2687 | -7.40357 | -64.34617 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17719d68-5cc8-3801-81b1-ca7cfbd75c4f | -6.76802 | -59.66577 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3f81eba-203d-3a78-a0fc-c423903e2341 | -6.81269 | -58.96731 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f9514ff-5d6c-363a-8136-229adc0dba37 | -5.79684 | -59.22031 | 2025-08-27 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README54.md)
