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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04092118-4999-3f13-99a7-3d353028fa60 | -3.22683 | -45.37396 | 2024-12-17 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b8dc60-ca2d-369b-9805-b7fbb8af67a9 | -5.32264 | -44.70034 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22e3de1f-563f-3505-b49c-40d5ec315691 | -2.84268 | -46.76598 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f3ea48-316e-3478-951c-5ce7508812ea | -5.51327 | -36.83428 | 2024-12-17 04:21:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c200356a-deae-3b33-8581-2965334b9984 | -3.23074 | -45.37094 | 2024-12-17 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ff8ecd-6b91-3e9a-90b7-6c7e163f7cfb | -3.78427 | -47.11856 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a4b1b046-101f-3743-b549-19109647268d | -1.37402 | -53.47306 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 032c95ff-b285-346a-a44a-390b3697db68 | -3.7028 | -42.1282 | 2024-12-17 04:21:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 734aba9a-6751-3cf0-bb6a-85c19c5e6a4e | -4.05236 | -46.68238 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5dffeb-787a-3acd-ada4-210914d4b930 | -3.80234 | -46.70721 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f867f732-890b-33da-9143-ef2bdf4f146d | -4.72161 | -46.51175 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b0fa8b2-d0af-3876-949d-e054cdf5bafd | -3.7567 | -48.00173 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5959ac6c-26ff-3042-b28b-e39cef40c6dc | -4.06935 | -47.10392 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c461093-9ad2-37de-a4c5-d7ca30db74de | -4.10344 | -46.70996 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2d0d9f7-353f-3573-a1cc-22af2bc6e63d | -3.23353 | -45.375 | 2024-12-17 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2df86004-d443-3fe9-97ef-c38b095352b8 | -4.59274 | -47.05355 | 2024-12-17 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9622de4b-a083-3e31-8031-31b7a8ceca38 | -5.31462 | -46.49362 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c4cc845-7329-323e-a630-354dc4357016 | -1.3734 | -53.47688 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88d6a678-fb73-30bc-a87c-97ff3820569d | -2.47047 | -49.03397 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08b233e1-c4e3-3ebe-97a8-80b04b877bd2 | -2.01459 | -46.61382 | 2024-12-17 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4cd4730-54b6-3cd0-9a2d-feb47e3eebd6 | -4.79592 | -46.39819 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 00ddf15c-e705-3323-8cd1-e88ac4276a9f | -4.00638 | -46.92867 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ced565c9-673f-32a8-b470-8871c39f5a1b | -2.17876 | -53.74236 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b56bff6-7dee-3e50-86e0-035a59eda10b | -4.05735 | -46.90845 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df858d68-8a62-38b7-b1e8-d516d0126210 | -5.53167 | -39.1776 | 2024-12-17 04:21:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6bbbae8-8e2a-3cc4-bf12-ddbfa724a188 | -5.32595 | -44.70085 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71bdb039-0543-3fb7-8781-722ef5d85d5e | -3.44096 | -53.98574 | 2024-12-17 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d583089-f14e-304b-9249-57d4f39823d0 | -5.24521 | -46.35535 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf0f331-932c-312c-bce4-1f55f31b27f9 | -3.6644 | -47.16603 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887548a8-0e4a-3767-8e90-8b6f96541d05 | -3.87598 | -47.04232 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10e4d4c5-d2e7-337a-80fe-c03fcda9f314 | -3.96078 | -47.03448 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 944c2add-deb7-3adf-897d-b9dd718ca24d | -3.77219 | -47.16916 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecdc5779-e4df-3104-815f-91655094f6a9 | -3.58315 | -42.40765 | 2024-12-17 04:21:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5544995c-ce0a-3395-b317-966040a34021 | -3.66395 | -47.16559 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d47acd58-2a9e-349b-bb0f-1d4dba036f10 | -4.57933 | -46.58916 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 630eae63-e067-3fde-a39b-0b8fddecce08 | -4.77089 | -45.72092 | 2024-12-17 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87ed4ae2-35e4-3150-be46-f6e141c27b90 | -5.36294 | -44.04909 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b66a1786-b72e-3fd2-ad9b-89924caa6d98 | -5.1195 | -43.20458 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc76b381-cfb8-34d9-8192-7b69697a857e | -3.924 | -46.92043 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdc86dbe-6c51-388a-b9c3-b64b90641c92 | -4.67326 | -44.04413 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad87bc1b-c1a3-35c2-9f2f-d4dd68edb8e7 | -4.12481 | -43.56805 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5367ad73-184f-3f90-aa61-d4109f29d43a | -4.03971 | -47.0181 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9588341-2a04-3660-9c3d-3ee57259693e | -3.73481 | -48.97005 | 2024-12-17 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ed2e8ef-9df0-33e8-a36d-8232a3b18c14 | -1.72831 | -53.31504 | 2024-12-17 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0ada0f-5073-35f3-bbc0-79d8f51c6406 | -4.18709 | -46.66822 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26237d10-4490-3a51-9077-2ed721260100 | -4.0501 | -46.47277 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e49394ff-5c9a-331a-9cbf-6e390ac32f7c | -3.67523 | -43.57317 | 2024-12-17 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a453897b-38be-35af-bff8-f33e163e2c29 | -1.33573 | -48.32809 | 2024-12-17 04:21:00 | NOAA-21 | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55e7f0ca-2d6b-3435-9644-697e43799fd1 | -4.10119 | -46.70179 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68f04359-e522-3f84-92c0-550c58dae31b | -3.46627 | -53.46022 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b19e343-cbb3-3682-979f-909d7c6c02b8 | -4.01431 | -47.03846 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d96d4a6-bed4-37ec-9a69-5546b91ad0d6 | -2.65491 | -42.71808 | 2024-12-17 04:21:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1880e219-73c3-3e1e-8760-446864b6e088 | -5.14704 | -46.17997 | 2024-12-17 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1952821a-0aa7-39c8-bf89-742cefe40080 | -4.04784 | -46.92291 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e712328c-c6c7-3638-90f6-9965a8f27451 | -5.21039 | -43.29873 | 2024-12-17 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93ebd09d-0c62-34a2-929a-9c36073048a2 | -3.67007 | -47.12984 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc0c05d3-f623-371a-9779-f06f6be5725e | -3.87079 | -47.02942 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3e0068f7-42b5-30bb-b9cf-fe03394457a3 | -4.10241 | -46.69421 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7c8ac9-3273-37a7-855e-b7b688c58fa4 | -3.30766 | -53.37066 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3196fc7-bc2b-3a94-868a-eee5bbed2c5b | -3.78552 | -47.11058 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b59f406a-d645-34b0-a3d8-43856b30bbad | -4.08933 | -46.73141 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4272fa85-97ea-331e-847c-d2542c7116fe | -4.05134 | -46.92346 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbf39359-f70f-35a2-ab05-86d878b9ba6e | -3.85833 | -47.03963 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51a527df-2d79-3f8f-b8dd-14f96f4395bd | -4.02949 | -47.03674 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7163413-bb2c-37f5-8da3-23c0ab0a4958 | -4.10648 | -46.69096 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7901be5-7261-3504-af74-47f0c114fbf8 | -3.79545 | -46.84107 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8edaf5f6-cfc9-31e6-85db-f1d182a8a92f | -4.3956 | -44.10314 | 2024-12-17 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b8698f5-702f-31bd-b2bb-0b8b79be5a0f | -1.45831 | -53.47884 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb970d8d-d5ae-3bf8-a899-04dd1b009913 | -2.65628 | -45.56277 | 2024-12-17 04:21:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3e4791-1756-3382-be0a-7e4c05276a71 | -5.48842 | -39.12415 | 2024-12-17 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71d6c64b-60c7-377c-b425-a2dc1c77cac1 | -4.33841 | -43.55136 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2a136cc-de3d-3a15-8376-e26ecfff4f9f | -2.32746 | -45.77566 | 2024-12-17 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9a6efac-6da9-3336-b49a-0ac2655f5848 | -4.10037 | -46.72921 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df000c32-1e1e-3a9d-969b-6fd65e48dc66 | -4.0322 | -46.9086 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 677dfada-9645-3136-ad2c-e1719f3e5780 | -3.76545 | -47.16895 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91987121-f202-30e5-aca1-2c390abb8446 | -1.54608 | -53.73495 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecb98f84-2641-3501-96f3-6adbc5fb0f0a | -3.18464 | -46.68922 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24c91511-ccd0-3d82-b023-f67e9e7e555f | -3.87017 | -47.03335 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 33f35928-1dbc-3387-8b60-2d11c77a3d72 | -4.0969 | -46.72865 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57f5e7b1-dbc1-32b4-be03-a3377654d1e5 | -3.83441 | -46.68466 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d8b79e-69ab-3b64-a493-a9becc33ea6d | -3.23917 | -46.80508 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0132227-ce2b-33f6-a8f8-7fe21eb02277 | -5.21374 | -43.29926 | 2024-12-17 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fece9008-6852-39f9-84f8-85b778e878d3 | -3.83153 | -46.68032 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93ea7a2e-1f08-315d-ae07-2aaf961bc4ef | -3.78417 | -47.11771 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c0a2b5f7-d52c-3127-be3b-e1fcd842c906 | -4.01662 | -46.8185 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90bbc71-97d5-3646-87f4-3e369eac47b9 | -5.3038 | -46.49568 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d930fe-8208-3c09-9402-b69f3410b1c4 | -4.38701 | -47.77066 | 2024-12-17 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e68cb0e-7a67-3bb0-87db-1d01c67b0bb7 | -5.0881 | -43.91367 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3937583c-364e-3102-b1aa-b97117729b51 | -5.26443 | -43.76294 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a7bcf85-5019-3e99-a3f3-082af1138670 | -3.76901 | -47.16951 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a8a1992-e00b-36ec-840e-efd73afad3df | -1.69546 | -45.77656 | 2024-12-17 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e00910-00e9-3817-9ff3-c59719479da2 | -4.048 | -47.01145 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3046061d-f698-35f9-89fc-7c28a5014e80 | -2.77927 | -48.58035 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74fc886e-d9fd-3ce6-b34c-40e157efb462 | -4.79933 | -46.39875 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bd490d6b-2252-3387-87ea-c59c0a7750b0 | -2.93143 | -52.71654 | 2024-12-17 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e43bc7b7-86a4-3598-80e8-a75749a3702c | -1.81907 | -45.6371 | 2024-12-17 04:21:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb8a5dc-9067-36d5-aa29-7889d352778e | -4.67988 | -44.04515 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 230fbc67-582a-37d8-9071-db9edb075d75 | -4.02469 | -47.04412 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7825657b-7a9a-35be-a190-e21ed20db2d7 | -5.36016 | -44.04511 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9c6880-a4f1-3f9f-917b-e910f7f949d9 | -4.01072 | -46.90119 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
