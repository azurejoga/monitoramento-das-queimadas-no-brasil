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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 180e5ab4-c884-30b5-93c0-89fe449aedee | -11.25301 | -46.63932 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0170786-b548-3472-96e1-3b7b660d6943 | -8.8337 | -44.79163 | 2026-06-18 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 347f1b90-c9be-3935-81f8-c649fa3519ea | -6.03388 | -43.99512 | 2026-06-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71e8bb12-dc83-36a5-9f41-bdd59aa93ef5 | -11.81419 | -52.52427 | 2026-06-18 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6314ca3c-dedf-35c4-9c73-5748f26b9ae0 | -7.7969 | -46.45089 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04094e46-1824-3e84-9841-f3c917923ddd | -10.05491 | -48.09739 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2305102-0560-328d-b6b6-626f82672317 | -9.60016 | -48.18984 | 2026-06-18 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b6fab14-5b54-37e7-858c-3003920de78d | -10.15255 | -56.61698 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e524f172-fe6a-37f7-9c3c-1d9e83a6de51 | -8.6133 | -45.99303 | 2026-06-18 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52f59623-6909-3ad9-9bd2-9c41a27e3977 | -9.19037 | -58.05149 | 2026-06-18 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29128f5e-c3ba-3016-b1ec-fae823177b37 | -5.80975 | -45.07359 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b053922f-7a7e-3eae-b3ca-8fcc4c50d1d2 | -5.79541 | -45.08357 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db05d914-7161-3cbf-be91-ff2370f9890c | -10.1574 | -56.61247 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8b37f19-ded1-3584-bf99-a8a2779bb42f | -10.52576 | -48.17372 | 2026-06-18 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e42dad95-5a6b-3ded-9fa0-8644558869a6 | -12.0725 | -47.5545 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a89896b-b710-3253-89a2-04e49ddfe016 | -10.54686 | -53.72145 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a9f616-e19f-3ac8-98b4-bc4102f69470 | -8.84396 | -49.86174 | 2026-06-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 714bea83-b519-3e2c-b0b5-fc734fe196ba | -6.97844 | -42.8856 | 2026-06-18 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 971f7e9a-3bc3-3e0a-b7a8-931d644b527a | -7.36313 | -49.85764 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20aae5c7-4c89-33b7-9a2a-ce7bd4146613 | -8.91343 | -46.97086 | 2026-06-18 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9311ca2c-396d-3307-aaf8-89f4d3f9026f | -7.72146 | -44.15862 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41d621ea-5aed-3f0c-aee2-cb79d277aa44 | -9.21489 | -47.93026 | 2026-06-18 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 856ba910-bda3-3170-a02f-03e2f1a5adc4 | -12.83533 | -44.37409 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 38f9e378-e3e7-3a57-8c91-4cffeffb93ee | -9.70092 | -47.03894 | 2026-06-18 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6450254-04c9-3f7a-9ff1-a687d6b826a0 | -9.7801 | -48.97166 | 2026-06-18 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00749a65-1e0a-303f-8d5a-8d7790b6123d | -11.24841 | -46.64248 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddc28063-b947-31d4-877c-cc797b53d0a5 | -10.9927 | -47.74737 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b881ab7-8582-3191-8d1a-099e6fa51c8c | -8.50911 | -49.73636 | 2026-06-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cacecaf6-c0f8-38e3-bae3-e53222ab4411 | -8.93915 | -48.00177 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bed9b247-0d6d-38cb-b658-329ae5a41532 | -7.83999 | -48.387 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d06ad7-ea06-339c-a44d-f7b8923e5eae | -10.05122 | -48.09686 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58a58827-f113-369c-8918-266f4f0a3446 | -8.97226 | -47.98019 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f71c4b0-9cd5-3579-984a-5346a94622b2 | -9.74807 | -47.86967 | 2026-06-18 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6526788-cd8b-35f4-930a-e511fa065b81 | -9.74741 | -47.87416 | 2026-06-18 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9e7d699-fb88-3ecf-bd0f-24f485060d86 | -8.80481 | -46.63296 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43c75600-0bbe-3b4b-bb25-739ef5ac266c | -9.21794 | -47.93525 | 2026-06-18 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95841a92-d86e-3567-9ea3-cc8345d99d44 | -9.22552 | -48.58407 | 2026-06-18 04:46:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b0196e1-3a99-3805-8145-af16bd15b358 | -12.63175 | -44.60347 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb7b69da-c470-3f46-988f-30d9e88f59e8 | -12.44776 | -44.75266 | 2026-06-18 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8832084c-2d76-39cd-9b82-5e02f040789d | -11.26087 | -53.95694 | 2026-06-18 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b234429-0a0d-366e-b81a-ebcb31c0b1a3 | -10.04471 | -48.11139 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| efa433de-1f53-3c79-8ec8-c05fc042fc7b | -12.08869 | -44.97366 | 2026-06-18 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc031fb2-8ab8-3e9f-8a63-76abee4a6982 | -12.84577 | -44.36999 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb3b3eee-c9b0-314c-8173-3cb59e211021 | -12.77132 | -44.54278 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1967727e-76b4-36a3-b145-c1fc7af4e82f | -11.25399 | -46.63209 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45100f5e-2641-3fc8-a613-71ca77ac4720 | -12.7727 | -44.53197 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02e528f8-043d-35ad-bb12-feb707959665 | -12.836 | -44.36856 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8d037e53-b8a5-35cc-85b9-079899d63255 | -10.77272 | -54.10306 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de530fc7-eac7-380c-9f65-c58d2bab20ba | -10.70883 | -49.5373 | 2026-06-18 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b8289dc-a4ea-32d6-8118-62be2258c5d3 | -10.56132 | -46.22997 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b81448ef-5d14-3f86-ba20-7faa51a4f071 | -12.77063 | -44.54823 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d8b8654-25da-3ba5-9bf0-217f1ea4c777 | -10.40595 | -49.44557 | 2026-06-18 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6321fa9-6b4c-31e4-bd84-aa343b042dc4 | -8.68724 | -48.31286 | 2026-06-18 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 087ea6d7-61db-3041-861b-4fce022999b5 | -9.41386 | -50.69663 | 2026-06-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36dd5ccb-0ca9-32ce-ac96-1a7b2e90517b | -12.74534 | -46.31973 | 2026-06-18 04:46:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9ecd9c9-0f5b-3196-a2d6-90170987a3dd | -12.05579 | -49.76052 | 2026-06-18 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcd53107-b0c5-31e1-ad17-29e46b3fbd00 | -9.06841 | -44.75204 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3491d2c9-d77b-344e-96a0-b0f4ae364de9 | -11.26367 | -53.96125 | 2026-06-18 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56388945-07c2-35ed-95ad-94ad352e3964 | -11.21213 | -46.57755 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ffe8b5a-a8f1-3de3-81e8-0307017192a7 | -11.80758 | -52.5232 | 2026-06-18 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7972379c-021a-32cc-83fe-8bb0221b64fa | -8.93146 | -46.98346 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c6f1a9b-14e4-3760-a402-4633591bac58 | -7.84011 | -48.38631 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cce85e4-1315-3766-9a29-e01668130f03 | -7.83473 | -55.40224 | 2026-06-18 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368c7235-28a2-3104-8b19-b8550145f6d6 | -9.77659 | -48.97112 | 2026-06-18 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 685f6cd0-95e4-3bb6-a517-ef424606052f | -12.84021 | -44.37478 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 812c5a4f-98b2-3d23-afb3-c2d7ff2ba25c | -6.15918 | -48.50674 | 2026-06-18 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8556b71-3767-35a9-b889-273ceb676473 | -10.67305 | -49.68118 | 2026-06-18 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c3d8af4-6cfd-315f-bdcd-ff58a8e7adbb | -9.00106 | -49.67936 | 2026-06-18 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45bc1a13-4f10-3377-9726-50415f998a91 | -7.83774 | -55.40759 | 2026-06-18 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a99a1d2f-0ba7-32c9-bdf4-d32a9c1c2d9f | -10.90214 | -46.3843 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1be5f408-a1e3-3b70-b540-ee570f0bb07f | -11.25351 | -46.63568 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cad76db-eb8f-3536-88f8-e7fc8cb32264 | -10.71836 | -59.27444 | 2026-06-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d86a567-2658-398e-baaa-f800afbef087 | -8.80085 | -46.63239 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6d5dee5-1692-3e48-bd16-30723813a6ba | -5.80918 | -45.07745 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9812d119-c88f-3eab-9ea7-d36daa34525e | -10.98129 | -47.74563 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c155916f-e521-3f9e-8002-d10e66a09120 | -7.84248 | -48.39487 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a755c3f4-f2a2-3caf-93fe-3131bfb42b58 | -7.79978 | -46.45376 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3feb2ba7-2235-3e05-8467-76d77da6ab93 | -8.35675 | -49.71763 | 2026-06-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e303e08-fa57-304e-9c59-dfa94eacfaf4 | -7.60094 | -46.4717 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78757383-5a46-3215-9ae9-ced011053150 | -10.70987 | -49.66697 | 2026-06-18 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40be1879-9d78-3fe5-8602-a15d72fe2bd3 | -7.83952 | -48.39034 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c32aa15-9021-3d6c-80d6-408c5ef6403c | -9.00671 | -48.00089 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a60b438-01a8-336b-b8b8-4353c35f17ee | -10.57521 | -57.31831 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7373c4b-12fe-3a04-b374-6cfa1f4678f8 | -10.91611 | -46.37507 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3100359f-418c-34a5-b10c-5d96f37e891f | -10.59333 | -53.52007 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5929467d-c6f9-3601-a4bd-097fcb6fe753 | -10.59731 | -53.51692 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aabd120b-e643-3bdd-a967-8fda334b92de | -10.05188 | -48.09242 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e99c066-5fcf-3f37-b471-6daab7f7b665 | -10.77209 | -54.10688 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb509285-0a31-32f2-a83c-61ce67194930 | -7.59629 | -46.47617 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 025160f5-46b9-30a3-9a10-417f615ae0f3 | -10.91205 | -46.34327 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45791a26-ee01-3d7b-81f4-dce6edbe7c2c | -8.97957 | -47.98135 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c34eb52-ee29-30bd-b2f5-60f0cd9a5dca | -10.81242 | -48.77039 | 2026-06-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd445a5a-c1d1-34b5-8687-a9ac4a4be34b | -9.894 | -47.85952 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61f0b892-bbc8-37f6-ae88-1e1119fbdd17 | -9.37391 | -50.53474 | 2026-06-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 629098a4-6c7b-321a-975e-de33890cfb80 | -8.59446 | -47.04157 | 2026-06-18 04:46:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e57fa441-a7dd-369f-af62-5a6fad1ceb64 | -6.83872 | -47.91362 | 2026-06-18 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab61b10c-0c3c-3409-98ce-02311f1e532f | -10.98196 | -47.74081 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bc09163-11d0-3cfd-9624-23b63eb04d8c | -8.44813 | -51.55293 | 2026-06-18 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55c72868-a9b5-3b87-9cda-8cb45f0159ae | -12.07751 | -47.55132 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98b5b0c9-6613-3b95-9df5-ed54400b397f | -10.15075 | -56.6274 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README10.md)
