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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8392a00-a524-335a-bc0e-0fac5a8f1a2c | -3.08073 | -45.36164 | 2024-10-26 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc8ab1ce-a6fc-3367-bdf5-3f4537a097c4 | -3.07891 | -45.36312 | 2024-10-26 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55fdda2d-c1c5-33ea-92f2-73f8088c237b | -3.60997 | -45.81062 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 4cf6eec1-00d5-3600-8b2d-fdfe9f2e6ef0 | -3.6095 | -45.81343 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| cf5a4536-8415-3a46-945e-8d417eaac081 | -3.60903 | -45.81628 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a332f56c-a62e-3207-b0fa-3668fc876e56 | -3.60501 | -45.80977 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 2de9ef55-497d-37f4-b32d-b9677d79e040 | -3.60406 | -45.81543 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a99a748b-c5f0-3d47-b160-135509131c61 | -3.60359 | -45.81827 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| b7026407-36a7-3c08-9932-5d02f1bbae75 | -3.60004 | -45.80895 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7c2d2dc6-946d-3898-9987-e9349ad36120 | -3.59957 | -45.81177 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e79df783-1a00-399c-9371-eedbaa645db4 | -3.5991 | -45.81456 | 2024-10-26 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02bc0ebc-e87e-3291-8c9b-6b3ca3079f72 | -3.29916 | -47.02225 | 2024-10-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bd289e1-f0c5-348d-a17c-385a51b5a605 | -2.03793 | -46.97123 | 2024-10-26 03:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 21ed56d2-99dc-3031-8f97-056d7e3c96d4 | -2.03241 | -46.97039 | 2024-10-26 03:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 756e81e2-c2f7-3e07-bc16-298400c3dd88 | -2.03181 | -46.97406 | 2024-10-26 03:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dade9d2c-37eb-3a4a-83e7-1d9e4c56ec57 | -2.00971 | -46.54989 | 2024-10-26 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc44be13-f5bf-3007-881a-69a576e34b51 | -1.95812 | -46.62934 | 2024-10-26 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30d2acf-081d-35b1-aae2-fd0f47b29f7c | -1.95755 | -46.63279 | 2024-10-26 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa19f908-1b53-3d01-ba8d-d53bf0c8558b | -1.77887 | -46.30929 | 2024-10-26 03:53:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89eba9d1-4baa-31f6-942c-18de21f1ebfe | -3.29858 | -47.0257 | 2024-10-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a69e92-76fc-392b-aaa6-4fe407635b4a | -2.57408 | -47.25457 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cf0a371-d059-36b4-b0a0-f976048e3274 | -2.56942 | -47.25432 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fd9fde4-e201-3353-a474-689885c070c4 | -2.56882 | -47.25804 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ac596df-7e1c-31da-8ee3-77ecd53d5f55 | -2.56851 | -47.25368 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0176ccbe-a292-30fe-b8fc-835dbb1be60b | -2.56788 | -47.25739 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fa0dd5e-c1ae-3985-9bf9-779f92e7091c | -3.33196 | -46.27708 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ad8bc2b-89c4-320d-a5ab-4e1acb658abc | -3.19316 | -46.17793 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0085179-3dc2-3036-9d01-d8354421461c | -3.19264 | -46.18101 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb10cc2d-6870-330b-93c0-d90d746ae7da | -2.3145 | -46.62894 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 585dd7c8-3a5f-3e2b-aff8-03e731b74266 | -2.31396 | -46.63228 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2afb3525-d04f-3771-a32f-fb986b12677e | -2.31342 | -46.63563 | 2024-10-26 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9221ad0-ba7f-3c9e-8717-816a99ee4366 | -2.19164 | -46.42078 | 2024-10-26 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a1ae414-d859-3154-9423-ce52b67f2ba5 | -2.19109 | -46.42405 | 2024-10-26 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3641b3a5-ecd3-3984-b4ff-e629d482c42a | -3.54826 | -47.36045 | 2024-10-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b84e9603-1b87-3e98-a403-24a4141d8dcd | -2.81541 | -49.25 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b62394f9-fdbe-3f4d-9e2d-aefd6e61431e | -2.01023 | -48.52861 | 2024-10-26 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b2dd38c-f818-319e-84ac-b60e2485e8fe | -2.00412 | -48.52763 | 2024-10-26 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 246eebe0-6645-32e9-8335-91d1dbc6358f | -1.97864 | -48.68297 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcee48ee-f139-3547-ad69-90ce93b7d783 | -1.53294 | -47.29021 | 2024-10-26 03:53:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fcab015d-8f37-38a2-8860-d5791126fc14 | -1.5323 | -47.29416 | 2024-10-26 03:53:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04e8a272-6921-368a-b78d-2eb2bd4bd15b | -1.52985 | -47.2028 | 2024-10-26 03:53:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06d29025-a26b-379f-b1e9-c0ac7889f3f2 | -1.022 | -48.07024 | 2024-10-26 03:53:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 84210e6f-3e49-3995-83be-aae5044e5976 | -1.01956 | -48.07174 | 2024-10-26 03:53:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c5f130b-ddd4-3d6e-a008-d98968f02eee | -3.46023 | -47.67245 | 2024-10-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37def0b3-0403-32f5-8182-14900d608c41 | -3.45714 | -47.67226 | 2024-10-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f184017-ae4e-325e-9392-be4cdaf405e8 | -2.9748 | -47.99075 | 2024-10-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 237e9572-70d3-3e68-87ef-129c35a72432 | -2.97476 | -47.99171 | 2024-10-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10a5cca7-4d3d-3a96-8c9d-0105f6f8fe1e | -2.89127 | -48.27686 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9df8caba-fe1d-3ff7-b5f0-ee7f298cbfa1 | -2.88982 | -48.2855 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| abf041da-5294-372a-a371-203e008f698f | -2.88911 | -48.28976 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6c9865be-9f21-3bc9-86ce-4912f6e3fa70 | -2.66887 | -47.39821 | 2024-10-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9518bde-c9a5-35d8-87df-7ab529071d9d | -2.66823 | -47.40201 | 2024-10-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8474ddf-1f5d-374b-9d41-8328580cf8ab | -2.56939 | -48.12947 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b54ec26a-0398-3a2e-9798-e58a659d3b66 | -2.47502 | -48.05248 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9af9ccd1-b957-3259-8ef4-43d8f753a1f0 | -2.44213 | -48.396 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28e364ed-648e-31f8-ba11-3fe059ada655 | -2.37071 | -48.29067 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73e1e81a-a609-3f78-8c09-22ca9f5f0db7 | -2.36473 | -48.2897 | 2024-10-26 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8f166d9-4710-3552-82ab-4f3d6b09c8c8 | -2.34647 | -47.50024 | 2024-10-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1368f38-9d63-3804-bcb1-53bc47037d37 | -2.34582 | -47.50417 | 2024-10-26 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6aead511-e86d-33bb-8660-650d031fa6ef | -2.19585 | -48.81895 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 285ec6cc-d97e-3abd-a33a-61f65ef907ee | -2.19506 | -48.82379 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c1a33be3-8329-3c25-b7e4-abd7cf99adf4 | -2.19506 | -48.81679 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4fce25c5-632b-3803-a2fd-987b9a99b10e | -2.19423 | -48.82164 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8ce66265-7e93-3ad7-bd56-237804a4e7a9 | -2.16947 | -48.82461 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bc3729ab-2a86-345d-8d9a-29ce73222465 | -2.82801 | -49.25206 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f1156ca-8d4b-3d74-86ab-756848a823b7 | -2.82716 | -49.2571 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b228745-0ceb-3e4a-8716-1f6c20de1cc6 | -2.82171 | -49.25103 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0efd37f1-c5f1-3c8f-bc14-a0237c9dce8c | -2.82085 | -49.25608 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 26ba4b36-08ff-33ee-b026-a2c7c602e6af | -2.81999 | -49.26115 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdc605ee-b600-3c43-aafa-7dbe1375cd6a | -2.8091 | -49.24899 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfe241e7-3e91-3b6e-9c5b-52b3eae4bcad | -2.74626 | -49.31227 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68255908-71d3-3f54-a001-0a1cec157f8a | -2.74401 | -49.3096 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b499f20-a291-3f71-9ffa-7c91d55831c4 | -2.66122 | -49.28083 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e521fa45-d041-34b2-9fd6-17566ab2efa4 | -2.658 | -49.27965 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a22b076d-e230-396c-8aa7-c15b12c56fb8 | -2.65797 | -49.50943 | 2024-10-26 03:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78be84c-651b-3d1f-9d46-3a519acc55d1 | -2.65707 | -49.5147 | 2024-10-26 03:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1f07862-479f-3087-8daf-95f45b386ac8 | -2.65155 | -49.50838 | 2024-10-26 03:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58ac4eda-9300-34d4-9f3e-b365e069c8f2 | -2.65065 | -49.51365 | 2024-10-26 03:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65180215-f71a-3029-8f07-4ec83fb9ab7c | -2.60181 | -49.09511 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5333002b-4ec5-39b0-a30d-4aa2e081cb75 | -2.60094 | -49.10024 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| afa0cb24-35f6-3f5d-a482-f66a684d6d08 | -2.59746 | -49.0969 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3e37a34-7575-3c86-9e95-50f51a8d0aaa | -2.47608 | -49.10583 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 161c5a28-077a-3d77-af3c-d3d105727171 | -2.47326 | -49.10741 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4181834f-16a1-37a1-9a34-c76b411dc5d6 | -2.46979 | -49.10484 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23a86442-641b-3871-8c66-9a3eaa1b9bf6 | -2.46897 | -49.10987 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 56c9b74c-bb4e-31f5-9515-0640d9c57fbd | -2.46698 | -49.1064 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9142eb99-6b4b-34a6-8744-ec661f9cb786 | -2.37133 | -48.93699 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc876e31-f63e-3b79-acd8-e206c0141db4 | -2.37052 | -48.94192 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3be769e-5df0-3f5b-918b-08ac4abd8ca3 | -2.36975 | -48.93631 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e91125b-e84c-3455-8e17-13f755cce9e6 | -2.3689 | -48.94124 | 2024-10-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6005ce40-a630-31c3-a2d9-604c96023096 | -3.01799 | -50.48202 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2f5f8f03-a820-3fc9-bc40-6e1920112247 | -3.01694 | -50.48809 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4a26e260-71c6-3c8f-bf4b-fff1c6252847 | -3.01122 | -50.48094 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ea93c31e-c0e5-356f-81b5-5356c2a48a54 | -3.01017 | -50.48697 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bbf243f7-3c01-3871-9650-5914df84cf4b | -3.00934 | -50.47911 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 65d4b00f-7c19-33b7-8020-bbf09ba11875 | -3.00911 | -50.49311 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 008275a0-34d9-3c36-9e6c-1094e1e5b03c | -3.00834 | -50.48514 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 764b815b-85e2-31c3-a979-34ff5c016fe0 | -3.00732 | -50.49126 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d28d072e-0cff-3a76-818f-07b58593dd3e | -3.00445 | -50.47987 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ead45e0e-7530-351b-9579-e81fc478b7b0 | -3.00341 | -50.48585 | 2024-10-26 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README28.md)
