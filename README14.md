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
| fb0970ed-768e-3ac6-adf9-e3d33142da9e | -2.2299 | -53.6219 | 2024-11-16 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 73439ca8-bfac-377f-a954-995b2260818d | -17.2547 | -57.4493 | 2024-11-16 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| cc0a9e0b-fc53-32a5-a918-16f6b496f809 | -17.5675 | -57.5351 | 2024-11-16 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 521ab70c-cc27-3f34-93cf-8224d37b1788 | -5.6793 | -35.6688 | 2024-11-16 03:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 61.7 |
| e17391da-19e9-33a2-9076-546aee292e26 | -3.74 | -45.68 | 2024-11-16 03:00:00 | MSG-03 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5258f97-eb9c-337d-82cb-b29bd12635b1 | -5.67 | -35.63 | 2024-11-16 03:00:00 | MSG-03 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| af0e0b63-f48a-3c6b-aa4e-e9c023f39d99 | -5.67497 | -35.65108 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 25b79407-53b9-3f19-bba0-9697d78984fb | -5.66578 | -35.64318 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 39.1 |
| ce5a00cf-16f3-36c5-a713-80fa22ed3bb3 | -6.98298 | -38.8744 | 2024-11-16 03:08:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 009c4e82-505f-3941-b79c-f425dd185b1d | -5.67445 | -35.65415 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 344b5b4c-cecb-3062-baee-d0ea93134531 | -5.13826 | -37.70663 | 2024-11-16 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6b0645a-dab5-3ce4-8dd3-21e26d17bf65 | -7.62048 | -35.10192 | 2024-11-16 03:08:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9165d423-3cef-3468-a407-083e043b4f97 | -5.00517 | -37.53997 | 2024-11-16 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d1a2609-bc27-37b0-a2bd-a6252e381eb7 | -7.55844 | -35.23185 | 2024-11-16 03:08:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 603f4dc5-1380-3f5a-9f5e-9e5b3e183728 | -4.01793 | -38.25475 | 2024-11-16 03:08:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b013083f-cfb2-3ad3-b11c-f43231921814 | -5.67089 | -35.64408 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 39.1 |
| d2f7581d-f41f-373b-8560-5ccb2e6ed423 | -7.5527 | -35.23624 | 2024-11-16 03:08:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0e80ef7a-1614-32a7-be9d-cd062f6b5513 | -5.14251 | -37.70444 | 2024-11-16 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 79a3f942-50fd-36a4-8b97-bb095f02a69d | -5.67549 | -35.64801 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 12.8 |
| d643b61e-5ee3-347f-b5d4-dd67ee6002c0 | -7.55361 | -35.23103 | 2024-11-16 03:08:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 2c06b987-8785-30d8-b87f-0ae0b4ecdf22 | -5.66985 | -35.65023 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 37f0baa5-85b7-3490-bf4c-968065992844 | -5.00443 | -37.54422 | 2024-11-16 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a91f8c0f-26fe-3e43-8d0a-1ee5705b53aa | -5.6688 | -35.65636 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de277efd-d622-3baa-a62c-5e8a540f2f60 | -5.67601 | -35.64495 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 12.8 |
| f7cabe3f-9a48-3a79-812e-bb85c820ae8a | -6.98206 | -38.87937 | 2024-11-16 03:08:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aad0da3c-91b2-35d9-96ee-4a14cacd76a2 | -5.66525 | -35.64627 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 39.1 |
| 357b1c50-7fb9-3e26-bf19-7c8cae2b0166 | -5.66367 | -35.65553 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da641c7f-d603-3afb-97da-df43cbda6e5f | -7.62196 | -35.09327 | 2024-11-16 03:08:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2db1f563-24f3-39ba-920b-072c6d0b6297 | -5.66932 | -35.6533 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 945dee76-95cb-3f46-b5e8-9613930d63c1 | -7.62136 | -35.09682 | 2024-11-16 03:08:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 21a74264-09d8-34f3-9030-43df29e76254 | -7.62105 | -35.09834 | 2024-11-16 03:08:00 | NOAA-20 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 912fe6a5-b0ef-3dbb-8e8f-47eb150223cc | -5.66472 | -35.64936 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 83bd20b3-dd1a-3d63-95c8-2a6c5705a7fd | -5.13899 | -37.70232 | 2024-11-16 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4144dd2d-d2a4-3751-bacb-71b6362c18c9 | -5.66419 | -35.65246 | 2024-11-16 03:08:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e5582ac4-c84b-3b89-a6c7-3d5a22116473 | -5.29859 | -40.88773 | 2024-11-16 03:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91ad463a-d5cf-3af5-94d2-efb9e4afb74d | -6.20008 | -35.40503 | 2024-11-16 03:08:00 | NOAA-20 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82736cba-f6db-3418-b88c-8859830d7920 | -6.97883 | -38.48378 | 2024-11-16 03:08:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c0582daa-edce-3b6d-b757-2159808e73a6 | -3.758 | -45.6514 | 2024-11-16 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 55b1b9fb-9cf5-398a-829c-dffe96b156b9 | -2.7801 | -48.5592 | 2024-11-16 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2c56d6d6-4b63-303e-b1b6-4d8e38ad515e | -5.6796 | -35.6418 | 2024-11-16 03:10:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 157.3 |
| d8ab7eed-1118-338a-b2ae-ef481e1fef61 | -3.7394 | -45.6523 | 2024-11-16 03:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 459.1 |
| 66de6951-557d-3a5b-939b-5129ea0641c0 | -3.7395 | -45.6299 | 2024-11-16 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8c7cd80f-cabf-3fc4-a7c6-76775b3c3992 | -17.2543 | -57.4698 | 2024-11-16 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| b62c90e9-3ecd-30cf-94a8-20a8b321b710 | -5.6793 | -35.6688 | 2024-11-16 03:10:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 032f6dcf-2498-3043-bf57-437fafeac704 | -2.2299 | -53.6018 | 2024-11-16 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 56dec76e-c92f-3a1d-bcd2-136b17414b4d | -2.78 | -48.5806 | 2024-11-16 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f55ca701-1b8d-38ae-9ad2-619f1e9cbc0c | -3.7393 | -45.6747 | 2024-11-16 03:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 185.5 |
| f2f022ec-34f8-3834-980c-09c39a83641a | -2.7615 | -48.5812 | 2024-11-16 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 07554f4e-b8c5-3cb9-82bc-724c8775ab7e | -5.6606 | -35.6437 | 2024-11-16 03:10:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 69.6 |
| e2387513-f584-3327-bd2f-426bf4899e68 | -3.2008 | -45.5629 | 2024-11-16 03:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a1cd8925-ae2f-3549-b8b4-370b0eb27b72 | -6.1366 | -42.5544 | 2024-11-16 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 612f76cc-6b11-3236-88fe-a00d4f0bf5a8 | -4.9971 | -44.3149 | 2024-11-16 03:10:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 883c5461-6bc1-3a34-94a1-06952eec131a | -3.7208 | -45.6531 | 2024-11-16 03:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| b80f2439-ab5c-383e-9b2f-2c58b89c325e | -2.1562 | -53.7039 | 2024-11-16 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0d6b148b-20c8-3347-8b50-6a05f19dfa70 | -6.0303 | -48.0376 | 2024-11-16 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0b887b74-b4dd-3b2d-96b1-aac31e1ac1b7 | -3.2009 | -45.5405 | 2024-11-16 03:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2c983f93-cd5a-363e-b91d-7eb6478217f9 | -2.2299 | -53.6219 | 2024-11-16 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4183a9f5-402b-39a6-9aa1-6d4ca196722d | -6.1363 | -42.578 | 2024-11-16 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 1c2d9a2f-fe4a-3448-bb09-467ea6efeef2 | -7.44771 | -38.41967 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c4efb5d9-5da6-3d9b-b213-1ddb3901ee5d | -7.44854 | -38.41525 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f6e9ab1e-e8da-323e-a9dc-5cb03df7b124 | -6.94437 | -40.02482 | 2024-11-16 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ced88b1-cc97-3e44-9a79-90e4a0bfd65f | -7.45138 | -38.41793 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fe596ee9-0308-343b-93c8-e223872f57b7 | -7.45452 | -38.41618 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 419329fe-4244-3379-a011-b7406b2d41c9 | -7.40387 | -40.39128 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51b6b2d3-d247-38d4-844d-f6042e33a966 | -7.39605 | -40.39595 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b3e6989d-168d-3d9b-afaf-2761736760bd | -7.39718 | -40.40481 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 12952050-de41-3827-be55-c00d57a5980e | -7.3995 | -40.39286 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a17f0dd5-2331-3f60-8574-8d14222c5054 | -7.4537 | -38.42057 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 1efbcee1-927b-3fca-bc6a-af4637360887 | -7.39834 | -40.39882 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f1e29dcd-b8b2-37b8-911b-ebed487361b5 | -8.62479 | -35.07762 | 2024-11-16 03:10:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b7d14e8-c488-3085-aeb1-43c12bf10a7c | -6.9434 | -40.03007 | 2024-11-16 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d71cd0ce-5b76-3407-a18a-e988e6d14b49 | -7.39493 | -40.40194 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 54e4ab70-0257-3a12-977c-af76a0f2aca9 | -7.39717 | -40.38998 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b59d5269-69d5-3cc4-a39e-de973cbdb668 | -6.94172 | -40.02473 | 2024-11-16 03:10:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 74c5a737-898d-3018-92ba-6bd2770bd006 | -7.45058 | -38.42236 | 2024-11-16 03:10:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1be41937-eab2-3cb6-a889-aacd83e37f98 | -7.40276 | -40.39725 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 225084af-1e5e-3cc7-8183-41da2bb5e661 | -7.40164 | -40.40326 | 2024-11-16 03:10:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b6a3d042-82f0-3f6a-a30b-67b142445544 | -3.2008 | -45.5629 | 2024-11-16 03:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5e61f497-c1c4-3247-ba63-47d0e0a5574b | -3.7394 | -45.6523 | 2024-11-16 03:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 354.6 |
| 9a66dbda-5c7c-3606-b379-6a4b4032ccf8 | -17.2547 | -57.4493 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 01f516e1-6afe-363f-8f09-3f85e980d8b2 | -16.9384 | -57.6291 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| ae44f96e-15e3-3fcb-a8b3-15104cff53cb | -2.2299 | -53.6219 | 2024-11-16 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 648974dc-9a3f-303c-b0c8-fc3358c72cc2 | -17.5865 | -57.5739 | 2024-11-16 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 284e5d55-bc1f-3bb6-9532-ed713114858d | -5.6796 | -35.6418 | 2024-11-16 03:20:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 158.8 |
| ba64d33a-f35f-3580-90f9-51b477663c7e | -3.7208 | -45.6531 | 2024-11-16 03:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 975a37dd-5c3b-386c-95d3-8cd68435d9ef | -2.78 | -48.5806 | 2024-11-16 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6a9fe1fe-451f-3fa9-9911-348f7012b270 | -4.9784 | -44.3161 | 2024-11-16 03:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a400035e-eb01-343b-a782-3ab07214cf3d | -2.2299 | -53.6018 | 2024-11-16 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 72f23690-77e9-344f-bc51-29d141dc7d20 | -17.6063 | -57.5715 | 2024-11-16 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 943e6c64-8819-33fa-8eb4-c0a3a12fa1fa | -3.7393 | -45.6747 | 2024-11-16 03:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| ed875336-c9a2-3ded-84e7-b35afa537a8d | -2.7801 | -48.5592 | 2024-11-16 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1744a969-8393-34f5-8030-b97743d80ae6 | -3.5851 | -50.5255 | 2024-11-16 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d55bafb0-89e2-31f5-8429-91bf13669ab8 | -17.2353 | -57.4311 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 584f0d6d-b021-32a0-a14b-dbc4c8d314df | -2.7615 | -48.5812 | 2024-11-16 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f4db8572-de1d-3f90-82e1-a0aa31e6a00b | -4.9971 | -44.3149 | 2024-11-16 03:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 447f81f1-3b1b-3897-a55f-e9bdf42394e4 | -3.2009 | -45.5405 | 2024-11-16 03:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cd826d38-cb5b-3b1d-a99d-c7bc386731aa | -6.0303 | -48.0376 | 2024-11-16 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ee087d54-7f18-3076-81cd-5ea4a3f75ed8 | -17.5862 | -57.5944 | 2024-11-16 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 32a6df46-cb46-36e3-a550-714f5e56d47a | -6.1366 | -42.5544 | 2024-11-16 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 3c532afb-8f4f-3a94-8107-b2c51eeca0b4 | -2.5767 | -54.4188 | 2024-11-16 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |


[Clique aqui para ver as próximas entradas](README15.md)
