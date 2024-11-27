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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a7e9289-9a48-32b9-90a0-18337dfe0f6a | -3.84768 | -46.65181 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84cf2a50-155b-3659-9e85-f2f6e1d565db | -4.27201 | -48.61346 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bea71aeb-b7c1-3cbb-9e8a-aed3768fcfa0 | -2.77681 | -48.55969 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e2f854-01cf-373f-89e6-7bd2b85ded53 | 0.63128 | -50.57279 | 2024-11-27 04:42:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037c9cd4-45c9-362b-93c9-474974e34fc1 | -2.47727 | -47.96478 | 2024-11-27 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738a58fa-f413-3d5c-a1a3-2d17e0359bf1 | -1.98724 | -53.29745 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1744d51f-e4e6-303f-8fdd-e2b899ba1e34 | -2.03683 | -51.19329 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe6532c6-3a2f-3bea-9312-d2eada1ffbcf | 0.69758 | -51.44211 | 2024-11-27 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84cbbae4-0d29-36ea-8a0c-5e4d0deb51b4 | -2.21989 | -53.61988 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 468d1c98-e5eb-3049-bb3c-6c9922581e11 | -2.68868 | -45.65435 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fee6e0a-561f-3067-b7c8-cb350a906562 | -3.5053 | -49.4584 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8bf34e6-75a5-381a-ba8c-e49c5ae70081 | -3.71169 | -50.4384 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15bc97c6-dcb3-324e-b995-7c39663e7664 | -2.57992 | -54.05326 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bfb9a40-5983-37f9-a6b2-4290d990a75a | -3.18562 | -48.43513 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf088df-6be2-3044-b74f-ba95b81522fc | -3.38048 | -45.85309 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bedc61d3-1d41-3ef5-aef0-ea6eacadeef9 | -3.65524 | -50.23582 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afbebbbf-7fbc-351b-89b9-e089ee038b5a | -3.90161 | -50.11604 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f594960d-93cf-3170-b5ad-db6441f1ba0f | -1.48162 | -52.53829 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe7628f8-763c-3e47-a39a-375f17898f88 | -2.25315 | -53.62506 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63408ded-c980-3a0e-8a07-625766125bb0 | -3.84397 | -47.73386 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d3e9fb2-6475-3e85-9f8b-9e715289f43d | -2.48112 | -48.83988 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54d6a434-0674-3c3f-885b-54b3c16a540f | -2.82933 | -52.94577 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cee1b96-a93a-3dbe-94d3-6087c298d481 | -3.28573 | -50.61828 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8f1e9a-a955-35b3-ac08-200f80d0ac4a | -1.95821 | -54.13429 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45a6a819-b5eb-3e09-8a93-ea9d85a67931 | -3.37571 | -50.11103 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9c99f2b-4b93-3be1-bcc0-0afe2cf609c0 | -1.35246 | -54.63147 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cae6b32-1732-3088-89c5-ced99bf4830d | -1.71696 | -53.25457 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f7377a4-9ac1-3370-b948-3cb4f931ec7b | -0.35317 | -52.00298 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07a7dd6d-2820-3ec5-9d04-38b265c5f9e6 | -3.83408 | -52.18084 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c9cc001-8069-30af-95c5-e86a08492119 | -2.82573 | -46.83632 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffe64869-5002-3d64-adb3-da4983f65da1 | -4.59066 | -46.12012 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62159b20-3677-3237-9495-c495364f512c | -1.44894 | -52.4486 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 072915a3-a2a0-3bdc-b600-47ef01be9b71 | -1.63027 | -52.26219 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7275f15-34a7-3250-9d92-e65f5d382e3c | -3.511 | -53.81372 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e1165c1e-0af5-37c5-8274-587c3058b7c4 | -3.70564 | -47.66882 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93aa2346-0e61-3943-b531-2be488681ee3 | -2.71341 | -46.11557 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a88c157-9274-357e-8523-40fd3384941a | -2.25545 | -53.47029 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4955d0d-77c7-34aa-bdb5-70d5e4726086 | -3.84277 | -46.64838 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e73c4dc-3b7c-3a83-8fa0-3ccc92204d42 | -3.22533 | -54.08552 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acc598b7-1cc7-364d-96f8-dc29c8c2ac23 | -2.23996 | -53.63638 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7161fdc2-db96-30e1-b1df-e345feff307b | -3.39652 | -50.30477 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6956de35-ea68-31ee-86ad-0d567ba09be8 | -3.49584 | -50.49285 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| adfe526d-b79f-3285-bc30-425bcda15c00 | -3.54951 | -50.38853 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 521cec71-d51a-3a50-92f2-4efe8bf4dd69 | -1.62814 | -53.87159 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b24af58a-9c29-3e7e-bcba-8bcebd735c8b | -3.96684 | -48.06846 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1ea9d14-ace3-3d3b-bc4e-404d9235beb8 | -3.10224 | -53.25538 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fb2924c7-de7e-3b41-982b-0826e8e829a0 | -2.82188 | -51.79607 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4297614-c846-3be4-bcbc-fd891c945b5d | -5.71299 | -46.77136 | 2024-11-27 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e60dcb-4f66-326f-a6f1-16c2ecd421a0 | -3.96336 | -50.62967 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d0a452-f478-3e5c-9639-8b306095c4d8 | -2.78729 | -49.20758 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d04d8022-7bff-36ac-9d46-c23f0fe4e5de | -4.21002 | -50.89799 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 175a10d3-5da0-30df-a98b-28ae7c726788 | -1.5156 | -51.19589 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1acd1fa1-c37f-3513-8356-2e0a15c1f2d5 | -3.50245 | -50.49388 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cc4e24c1-2765-3ecb-80b5-627dbde6a361 | -3.06402 | -53.28719 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba7fb781-c24e-3391-84a2-013295f27a90 | -3.58889 | -50.52835 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff37ba98-daba-3899-8669-17b7bf01aa15 | -3.03531 | -51.77698 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc2e7635-4358-3a7a-a429-e0edbdefc2d9 | -2.24945 | -53.6245 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a957c03-9c0c-3190-bd75-beb91be89b06 | -2.55141 | -46.41166 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 538ecf32-b11f-3199-8e49-7bfcbe497b4d | -2.84095 | -46.83433 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a57002ae-d233-3f12-a4c1-0e4da66fd2d6 | -3.93693 | -46.71531 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b8655e-1af0-38e6-b67d-82e1b7f5f2eb | -2.82244 | -51.79247 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 323293c0-8ec3-35fd-8b1e-2ea0691c25e6 | -3.08659 | -53.26129 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a018bac0-f553-362d-952b-d34cec246e1e | -3.18795 | -50.82927 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc0278c9-93d7-3090-ba4f-3ecd66ae8cdd | -3.05977 | -53.29069 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a72dc49b-7a30-31b3-a59e-9351e68fd87d | -0.98598 | -51.72408 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae863760-8ee0-362a-8821-b8a0ad1dd4d9 | -1.6672 | -52.716 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53ee8728-2170-3c9e-bf13-5a8117604301 | -2.93772 | -54.7891 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c2c00ab8-cbb8-3fca-9fcd-bb905845e5ba | -2.96082 | -53.72256 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10a4eda5-02a5-328a-a903-7ae6a6ad7d43 | -4.00388 | -50.3506 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55d826c8-1983-3771-b02b-b8c30c5a6a24 | -3.39544 | -50.31164 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3bb73bc-75ad-3a85-9949-f52f973512b1 | -2.54672 | -47.97162 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3722bc63-d422-3a8b-ba31-95ebf9415602 | -1.68708 | -52.61304 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11889216-49de-346a-985f-8e687932cf18 | -1.20499 | -51.75775 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4db97f19-81a7-39e4-870a-9947f3fee1c0 | -3.09244 | -53.2707 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75bc89ab-09b8-3cfb-9c6f-e0ccd1d79158 | 0.33685 | -49.71576 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2ce0b1-371a-3de4-bd1c-e4305600770c | -3.27598 | -48.75376 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5ad955b-23be-3d67-baca-3e823f1c95a1 | -2.84437 | -49.40554 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d973b9-da36-3f1d-b337-7d18bad9dfef | -2.56926 | -51.88746 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306b05ba-2a13-3bf7-b112-ac2fb94f1cf0 | -2.60385 | -53.97753 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adff8c45-9e26-3d60-9fc9-9f37b11483d9 | -3.23753 | -48.00807 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a228e612-7922-33e1-92bf-4b9b6523f0fc | -2.8945 | -54.16957 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1fbcd1-02f3-3fc5-8bf2-8884b41d9db6 | -3.17711 | -48.44506 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2085c83d-cf03-34b6-ae81-884c287e6bb6 | -2.81482 | -46.83465 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 32a0936c-0445-3990-99b4-9fa5c4760746 | -1.73539 | -52.78773 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2599acc-de02-3238-9075-f261bca12482 | -2.26959 | -51.24057 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eff0034-c906-3506-ac57-a468814cd278 | -1.31186 | -51.74714 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80c823b8-a3fa-3795-ac55-373bd257876c | -2.38542 | -48.60283 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d171ae-14bb-3cb3-93cf-4dd10a522e2e | -2.835 | -46.82473 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a910e48d-5cca-319a-abcc-60ab439ec19d | -2.24136 | -53.62767 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed42665b-ef94-34e2-8e81-6e421e10657e | -0.55 | -49.52126 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d04e4c0-66c6-3c53-8dc1-d091ffff93f0 | -1.64123 | -52.49281 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d648aa96-c2de-36f3-8175-b772e6eba0d6 | -3.27654 | -48.75016 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea90c0f9-6887-3e7d-8540-3372421aa173 | -3.37354 | -46.65653 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72982ffb-d60f-325b-918f-ab562aa34831 | -2.68403 | -45.65864 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 5d70280b-f094-33cd-b3cb-c37d63ab563f | -4.29482 | -48.21481 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0145a6af-d5e0-32b9-b73d-3e17fb472603 | -3.09995 | -53.24666 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 140771e7-9205-3f26-a476-54b4abcb1cfa | -0.87421 | -51.72229 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15e245e5-1bfd-3dd8-8de8-fbd33ce20148 | -1.0616 | -52.42364 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 257679e9-a538-3df9-99c3-93904724c861 | -3.05688 | -51.05742 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee991198-7bfc-33fb-9a81-285844e019e6 | -2.44609 | -48.61217 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README71.md)
