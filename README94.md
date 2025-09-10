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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eca2dfb-284a-32d8-a6c2-5211eb7b7aaa | -11.11467 | -48.36155 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c91e5f84-a7fe-3185-9ffc-a0007e1a39bc | -9.56058 | -48.01488 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f45f171d-42f6-3e57-a79f-842c16fd34ac | -10.1439 | -46.17818 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adefd6ca-8f93-3407-829c-547315c2d92a | -9.45116 | -46.71265 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5f81b0-699c-3d76-af05-b19964c5e0ea | -9.45072 | -46.71611 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 797e7090-2482-3bdb-ac5a-1b7a16c71763 | -11.11381 | -48.40802 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7563a4c-88ef-3f39-bd4c-d9bb5e0b65ae | -13.01955 | -48.01828 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 141852fb-b4eb-3eb0-90ac-7e90515ce7dd | -8.04693 | -48.67877 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7e18b315-f4f1-35c5-b381-3f51e6cc7305 | -12.0703 | -51.06269 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9d089525-b836-3c03-944b-346c28f3577d | -8.74837 | -47.09874 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1c2f4f4-9b74-31ba-9b1b-79544c72a536 | -10.88057 | -55.70507 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6dee57-c9ab-3d28-a60d-740010f7281f | -8.19435 | -47.16063 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 805db095-5ed9-3b57-a791-5345b1d3affa | -8.49026 | -45.67219 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a87426da-e8b8-38d9-aec5-36d802dab198 | -8.85258 | -47.27623 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 387dfc69-dcad-3af6-aa5d-9e1cb2195d04 | -11.21473 | -54.99091 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d571342-5574-3be8-90f6-8e280ef326ab | -9.28061 | -56.90067 | 2025-09-10 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d2c10d5-8a84-3b0c-af84-380adb2da5fd | -10.88837 | -55.69173 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a8263a7-5e4d-3c83-ba66-f430f5e4e20e | -11.46245 | -49.27344 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a650061c-55cb-3ce6-8f3b-a36b4ce5e61c | -6.84775 | -47.91664 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23e1c174-a858-367e-91fd-d28e045fc99a | -12.21014 | -53.8994 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ad16262-00c3-3c30-84ea-5265dc1a3804 | -11.13618 | -48.35551 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d34d485a-32d5-34cc-8b35-ad5146a64414 | -11.45227 | -49.28108 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25641a10-6acb-356d-8ab1-31d67eefa60b | -9.60751 | -48.03865 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1e58a5b-bde9-3118-bf7a-84ecaeb3f174 | -5.41674 | -51.53659 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46475067-69ef-34c8-babf-3d70e9913d8d | -8.86184 | -45.85658 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b63fe7c3-c878-3eb4-a62f-e0c7968a7e5a | -12.86724 | -47.96518 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a564c23-fc8a-3ab0-be73-71cb0c0c3de6 | -9.07515 | -45.7109 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aae9cb3d-48e8-3899-9695-40c160c55097 | -7.75072 | -50.72603 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96272828-1352-3c7b-ad25-449d87ec6d37 | -10.72605 | -48.29882 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbddafb7-04f8-3eb3-9680-ea7214023c76 | -11.12072 | -48.43419 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1872cfc-99d1-3bf6-a9ab-6251d4ccc30b | -8.20049 | -47.15521 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8f0bebb-3e7b-3f96-9679-a89472a0e72a | -10.01819 | -51.70628 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ade33834-b519-3fed-9c2d-3919dfa22351 | -9.10356 | -46.9771 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cdad4890-71c5-3a04-bc1b-7ec07c441f78 | -10.01515 | -51.69899 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5788ca3-0231-35fb-8bf1-13c90dfb9d30 | -8.49552 | -44.7236 | 2025-09-10 05:04:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88e815e0-154b-38df-9d42-d5d89aa4b9ac | -12.18366 | -53.87809 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 196dfc70-5ff6-3bef-ac88-f3d9724d20fa | -9.06222 | -46.98343 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c45da4d-9c5a-36b4-a2a1-0739aae9d3fe | -6.44166 | -47.02796 | 2025-09-10 05:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 885007f0-5268-38db-8975-0041f674239b | -9.51793 | -54.64214 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9e8421e3-b974-38a4-a0de-2bcba8935f19 | -10.01868 | -51.70284 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baf35ea4-2bce-3f8c-ba23-c281e1a838ad | -10.41469 | -57.181 | 2025-09-10 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c14e1cbd-f22e-306e-a720-6f17b19d2800 | -11.20962 | -55.00167 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8a98d4c-e4fd-3299-9efb-5d3f494efa90 | -9.7505 | -45.40181 | 2025-09-10 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 38b5c621-e3be-382a-83ef-c4f0466ded6d | -6.87946 | -47.88282 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ea836c9-19d7-35e3-a622-9e7f8e5a50ca | -10.00993 | -48.08915 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecefbc54-5728-3bea-9058-78b157c20bfa | -10.54838 | -51.50815 | 2025-09-10 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb9d6086-8b08-3f6b-be52-01abc2cd2598 | -11.67681 | -46.89836 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f010c111-1092-3e62-abe9-7fd6822f3c4d | -9.69589 | -46.81845 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50bb5a46-6d32-3eca-9958-3873325f8759 | -9.60903 | -48.04037 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccc8c1ea-70a8-37e3-8898-8f36bf656878 | -8.52443 | -51.38235 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12275b10-30a3-3f16-adfe-64f742d2a4fa | -4.88456 | -56.04556 | 2025-09-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3face3b0-9f47-3e01-ac92-124027000372 | -9.10257 | -46.97126 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3850b181-1e56-3091-bba4-8790f8b4666c | -12.05164 | -51.03909 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4365c6fa-dfbe-322f-b453-5a4cf16cdfd1 | -12.0479 | -51.03435 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 019b323c-1082-325d-b794-e84dc0d721c6 | -7.70633 | -44.84337 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98e56855-c84f-3b81-91b1-50f2603f2cde | -9.51258 | -46.54246 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82b44e53-26b0-3cba-bae7-12afa753bee0 | -9.79838 | -47.79611 | 2025-09-10 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 191312b0-0eaf-378e-8ac3-1e205f876298 | -13.01327 | -48.04055 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 665a2fcf-94ce-337d-bc81-c45d8f98e7b5 | -12.18977 | -53.86157 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23811208-d31c-39db-86b4-a6a4a6ae8171 | -7.55555 | -44.66221 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d197f3c1-e739-3dd8-b45d-73853978f875 | -8.20671 | -47.14924 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ce74829-a51b-38a8-b5b1-9e5cb5b6ec8d | -11.11225 | -48.45957 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 047a2012-7b98-3fe4-81e1-e114252b6482 | -7.73975 | -50.744 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22fb7923-3094-3078-85df-01a315b85f7d | -8.08526 | -54.75835 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f12f138-40bb-3a9d-8962-d35220d0724c | -11.6666 | -46.91365 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ee1c9f7-09ed-34e0-b5a1-2f182d6718e7 | -13.02153 | -48.01794 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad6ace45-9f63-3cd8-8d05-db05fb0a7ebf | -8.05102 | -48.68432 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8fe1293-658c-3fc8-88eb-f6bcace9a765 | -13.18204 | -47.25931 | 2025-09-10 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 495615aa-bfff-3805-92ca-1d5f6bc059ff | -9.69179 | -46.80652 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9115f8e-8032-38ff-a218-69b402463c84 | -7.1099 | -50.7659 | 2025-09-10 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 257b68c2-8a44-36fe-9556-48366ccf9ade | -7.77726 | -46.05264 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2eec6b94-8ebc-3a25-a804-8f0fa5f31c5d | -9.06919 | -45.71056 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 047168f1-7e1a-36bb-9023-490342ada20c | -11.18861 | -48.37517 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0f6ccda-d525-3b55-892c-5c78ef1ff3f6 | -8.48072 | -47.29605 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47ea4bf5-e3c7-3beb-a48d-a8a9f32a7f22 | -11.20784 | -54.99003 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12878d62-1abf-3550-946e-1f266269e3b7 | -8.08133 | -54.76144 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af16ab4b-072d-3806-a09c-fca681c2316c | -9.76465 | -51.12357 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed97bd81-becd-37af-9c5a-5ee5826f068e | -8.08301 | -54.7506 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d844c2f4-65c1-374d-94d0-efc1a47734c5 | -5.79739 | -51.67895 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bbd93a7-0073-3b77-958e-aad8606a235f | -11.34418 | -46.54423 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abfdacdc-874d-3747-a265-dde6faa4b1a1 | -9.04947 | -50.48094 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 53464868-4bd0-3ff9-b0db-8573314ce562 | -6.44209 | -47.02479 | 2025-09-10 05:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1dbff71-dd98-3bda-afd8-65f5fdf9ba93 | -13.02492 | -48.01885 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 845269ac-bc41-3ccc-a4b1-b1754e0966ad | -9.21653 | -50.54624 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16fc231b-4014-316e-acc4-1c37418ac32a | -10.02777 | -51.66788 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ae0562f-182a-3c96-b7e7-b338c2b2fa38 | -11.45017 | -43.62256 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dfe5256-f69a-34d9-a7fc-37e17da28023 | -11.46191 | -50.32685 | 2025-09-10 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4abf52cb-7de0-3804-b3e7-4b3afb5bcc45 | -9.20436 | -50.19065 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8a977e3-dfc6-39e1-b50b-92bf91ab4082 | -7.75018 | -50.72985 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b5ce4f-22d7-3b18-89f8-845cbd56ae73 | -10.57822 | -52.03945 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dedfeebc-fc89-31f5-a6ee-c41fd1afa309 | -10.65407 | -48.61086 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdba2d32-9aa4-31bc-af15-ad11db374ab8 | -8.20625 | -47.15263 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 603b4de2-0d4b-3d29-8fa0-89342e638e76 | -9.10267 | -46.98408 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4a2531c-5f1a-30fc-b91a-5724382949b7 | -12.01527 | -50.98337 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 48e98a12-b7d2-396a-978e-53a452446b2b | -9.68574 | -46.89736 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 181a673a-5c1a-3048-b908-48475b9dbe68 | -12.87845 | -47.96252 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce7fc13a-f0ee-3395-b98e-e3a3e4d5d7ad | -7.18123 | -44.93829 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d4afdc84-5b57-3b9a-9802-10f6d8b2553b | -11.10884 | -48.36658 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d760457f-0201-327e-83b0-fdcbb9f02417 | -9.66924 | -46.64109 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4544c80e-9c82-3fb2-9831-ad8ef86710b8 | -9.09704 | -46.97119 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README95.md)
