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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33fe84ed-4a76-3e1f-ae79-ed6d6b58467f | -8.62874 | -45.72504 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28b53728-0170-3d0e-b441-16fa69d91de2 | -7.86575 | -43.57405 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 641aed83-94c3-3c60-8cea-95d10a87e3e6 | -8.08072 | -44.50947 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23e494e2-e438-3d37-8058-72d7af1bbc9f | -7.97503 | -45.66846 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a83cd5e-be90-304f-a0ad-54b0e555b0c5 | -8.95856 | -45.79003 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93306390-3c36-3418-afd1-1a2b7dd9c968 | -8.59768 | -46.3583 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d062671-56b9-3ca0-a31e-6cbdfb2c6bc5 | -9.1229 | -46.94143 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35a390ce-8e61-3c68-b85c-86ba81a0e93e | -8.96315 | -45.7812 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f555bfa-620a-3fef-bf0e-1256f11508a9 | -9.00146 | -47.0409 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e90af23-cbd9-3f3e-b7d3-2db6b7d1cda0 | -7.38707 | -49.99249 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9f1e4a9-b1db-386e-8f70-b97558e90648 | -6.5568 | -43.98716 | 2025-09-15 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1ee25c4-01ba-30cd-b2d5-1bcee3202d36 | -3.65507 | -54.05794 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 174b2a7d-5a04-3b1a-a1a6-ca2b1e743f77 | -8.97038 | -46.2154 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b1de0c80-2fd3-35f5-9093-7f3c1a723a9d | -5.86427 | -43.72083 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f876e01d-e993-3503-a575-c765b0e644eb | -8.41588 | -47.22593 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f64760e-f7f3-300f-a79a-68255bf8f290 | -6.72965 | -46.30984 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaf615a8-2251-309f-aa66-492e784a124b | -9.06968 | -44.82796 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a2397e9-0819-3643-b924-c201658e8098 | -10.16593 | -46.14656 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c5b2952-3199-36ed-a944-a34304fd5af9 | -7.86423 | -43.58474 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0ae38306-fae2-3d40-8230-761671c24173 | -7.8816 | -49.49528 | 2025-09-15 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d50045db-e43d-38a8-b006-2e6d80742c96 | -7.39715 | -49.97197 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a603db-25c6-3c3a-9df6-d6945ff1bc4e | -8.95741 | -45.79793 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15a21924-e4f5-3aa7-b665-8f221d91feab | -5.69917 | -49.20233 | 2025-09-15 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4390bf05-fbe2-37f7-a1a5-82f86b26f789 | -9.23168 | -45.67733 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e8d5b27-ca6d-343b-bcb3-d64cb703127c | -10.13481 | -46.15295 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd58601e-15ea-30fd-a209-335437edf0bf | -8.97418 | -45.82688 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 637005de-d788-3bad-83dd-84c55ad120bf | -6.30173 | -51.73858 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e49ff85c-b9c3-3fc7-bd73-fa5c9569fef4 | -7.40112 | -49.99102 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 867eff61-b880-3890-b5d0-50a040bc9c0a | -6.15948 | -41.20179 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a73a8305-8a85-3fd9-b970-0180ece5ec30 | -6.97524 | -44.54523 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5381126e-0d12-33b4-b0e0-272a5d7eb489 | -7.39044 | -49.99303 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e828bac-eb3c-3752-ad69-ff8ecac13003 | -8.95799 | -45.794 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dec3d604-9c8d-3bed-9ea9-d4f601769a7f | -7.72603 | -45.31303 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4c4e5e-775d-3a5f-b2ac-60fc64acc489 | -9.73223 | -51.88464 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ff8a6b0-7bc9-34c1-802b-a58e40e26f20 | -9.17707 | -47.0415 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66354ab8-d13b-3e15-b112-135d65d47464 | -8.90046 | -46.18727 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73adfdae-428f-3a68-bca4-9b1ec5c018cf | -10.72294 | -44.775 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0c19cc7-245d-3dfb-8ca8-af565deeccc2 | -5.78188 | -51.64841 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 228d8a3e-d17e-3190-b2fe-36147868ecc6 | -10.88485 | -45.4419 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 749831cf-624a-386f-9f6f-aea11b405b89 | -8.41131 | -47.23014 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b0d6621-34fe-3030-9677-5006b7100ea5 | -8.96283 | -45.79059 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d88b6f62-d9a9-3758-9ddd-3e1f253dd88a | -6.41019 | -46.94186 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adeb6412-58f3-3cb1-acfc-26eb928d5f2f | -6.41327 | -45.85289 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf749310-8aff-3a7f-a0ae-1cbc906b9b1c | -8.8984 | -46.1861 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1feec167-79f1-38a0-878d-b1046f4dcb9a | -5.11985 | -46.13364 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6c9d844-2c66-3c37-8079-464c0f06eb24 | -7.37122 | -44.35389 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02a6b634-4570-39c4-8fc2-a01b20e75b2f | -8.92546 | -54.44762 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8b406c9-e0b2-337f-800c-01d390c0a6ca | -5.57731 | -51.97095 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10d742c0-6368-3a39-9a3b-4acb423a7095 | -10.15271 | -46.14846 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf1b5b9b-6fc1-3a88-b1d9-332d70e91642 | -5.97244 | -45.83947 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09da6639-5160-35a4-a446-c1a3378a7959 | -9.00214 | -47.03615 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e0612f4-0164-30a3-b709-5764b182ac67 | -3.65134 | -54.05734 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2fe75b5-0f83-3f1a-9a2d-e3f5daf87a7b | -7.04887 | -44.13862 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88e24d01-c7d4-31d9-9adf-31c9a1377052 | -9.91716 | -50.29739 | 2025-09-15 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c48c4000-6fc8-3c1a-bbab-69a9e8300d87 | -7.36854 | -44.33966 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25928d1d-6341-3c6d-a7ea-8d9ae5f77c13 | -8.62391 | -45.72832 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e8a6e8d-933c-3232-9ccb-4605c91cad72 | -7.45058 | -44.38694 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbd54d81-652a-3c7e-95d0-02b99d2d625f | -8.97392 | -45.7663 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8362a05-f892-3ffb-be11-e92d1e3b796e | -8.98491 | -45.81223 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ecfc98fd-6863-3cab-b9a2-03c9ab6d69ef | -5.84207 | -44.16336 | 2025-09-15 04:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 57780dd7-6846-3948-bde7-03a2660d5d98 | -5.95508 | -42.80075 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5a1be561-77f4-3761-b8af-d477e3d475f7 | -8.91771 | -45.45928 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 001d32e8-afb1-3b5a-b5c2-8aa9e8f5cf59 | -6.52192 | -43.24645 | 2025-09-15 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37f82714-0a95-31e5-864a-71b48a27c6d3 | -8.61909 | -45.73166 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c16c2fe-d6eb-39f0-b0dc-352e5ae0fbd0 | -3.64528 | -54.04751 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cf7f5e6-5353-3276-9c86-2a52f5eb5c35 | -8.9645 | -46.04856 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cc46d84-7575-37fc-b38a-f731f2665fa3 | -6.17021 | -41.19496 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| baceec79-deaf-3f24-baa8-4cfb29badfd6 | -6.41888 | -42.61131 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e0adfac-62eb-3f44-9533-11daec6e4361 | -6.07741 | -43.15291 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 646ea5b9-650a-3ce5-a5b8-0b52b12ca211 | -9.17634 | -47.04648 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1700554-fcca-3863-ac9c-32b4699c20bd | -7.40279 | -49.98022 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a71766d-21db-3d06-9de7-297b4302a45a | -8.91336 | -45.45865 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76f27f9e-c792-3686-b2dc-92c045e9fa17 | -7.89126 | -43.58418 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1d3aa4a6-b76a-3f98-aee0-fb56b86956c6 | -6.17682 | -41.18829 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d47b7d5b-0567-380e-b66e-09d59a863cff | -8.96456 | -45.77876 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a358f14a-4865-3a58-a8a0-03d54d1c6e45 | -3.8794 | -52.17109 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe5cfcf0-5970-39e4-810f-d966351c677d | -6.42959 | -42.60917 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9bd16cd7-3f6d-37cc-9543-bc426484ccdd | -5.86895 | -43.72157 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5898883a-c391-355c-b3be-8b1feaacd5f2 | -6.97071 | -44.54479 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d00d26d0-0de0-3731-b1b7-3626f38c651f | -8.95834 | -45.78458 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9ca04a-ef91-3bfb-8a29-72d60416eaaf | -10.13844 | -46.15785 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5f7acc12-9bad-3850-96eb-ddb7cd69c50b | -7.89015 | -43.57758 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 140c342f-41c7-3ba8-81d4-8efc0b2d3938 | -5.87434 | -43.71739 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083c4226-d464-348a-80dc-1291846ed472 | -7.72171 | -45.31238 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ec35538-5f63-3097-8e85-bf5d69d13303 | -6.40781 | -42.61601 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69df0b58-3fdf-3165-8cc8-8ec72d28ff55 | -9.73342 | -46.04708 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb0e3df4-6b39-3cfb-bcc0-35553c204c0a | -7.48437 | -46.13888 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6af5a26c-ea4d-30c0-baa7-887698db28f2 | -7.79211 | -46.15437 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 879205a0-5155-34b2-949d-91bb8c146462 | -10.66353 | -46.24094 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1a0c18b-0f5d-3043-baf0-a7a918f26165 | -8.9478 | -46.04576 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8016b4f-89c1-3b24-93ce-786fd5d05fd6 | -9.10623 | -50.53285 | 2025-09-15 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1a8023e-0e6e-3654-8b17-b18e41c42d38 | -6.17732 | -41.18459 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c8510a12-490a-3c66-bb40-aff95410d314 | -7.6983 | -44.67503 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 98747f84-faaf-3c8c-8c89-0193e4100722 | -4.22097 | -50.15699 | 2025-09-15 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27700f35-7fdc-3711-8d7e-82dabf1fc854 | -7.8759 | -43.5874 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5c1a11bf-cf40-3463-9881-85fc543f67f7 | -7.74018 | -45.30687 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3795f5b2-05f3-39fa-a45c-0d424f81d0ae | -6.9439 | -46.49776 | 2025-09-15 04:49:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1396aac-5f82-3b8c-8387-126dbc5bda65 | -6.44606 | -43.32412 | 2025-09-15 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3e96b41-2af0-3ebb-ab8e-85a64d229d21 | -10.72368 | -46.45499 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a61027d6-a1db-3f2b-b93c-78da58381cc2 | -10.89771 | -45.44817 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README44.md)
