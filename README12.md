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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41a73b7a-4440-36ee-b6ae-9f6b8a0431be | -10.1669 | -49.31396 | 2025-11-10 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e71a509-61bf-3931-8a5b-e17ade3ea6d4 | -3.49971 | -50.04799 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3545f3b4-4890-3697-bd5f-cc917940e797 | -7.41362 | -40.06947 | 2025-11-10 04:21:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ae7a9e99-2f3d-3304-bba8-32771a70b858 | -3.94769 | -47.05881 | 2025-11-10 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e95b7f1-df89-33b3-bdc6-5687243e1239 | -7.92932 | -55.01588 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f51f6e07-b340-3082-8cc5-2fbbe99ceb4e | -5.84043 | -38.34829 | 2025-11-10 04:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e8779255-120b-3652-b3c7-9de938d46120 | -3.30459 | -50.15928 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ca06c17-afa0-323f-bba8-1afdfc5bd380 | -8.04366 | -39.68785 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4b92d28-fa76-3556-b597-dc2d6374d9ac | -4.85727 | -45.78307 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b7aefcf-80d8-3285-a238-b72d391f25c2 | -6.22241 | -44.40137 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0e99a5-1aed-3f8f-93bc-7648cd119101 | -4.7082 | -45.6572 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f499b99-c9b9-3929-83f1-aeb1c286ed1e | -3.44957 | -50.48294 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d4683dd-efa4-396d-8b0c-8407728442d1 | -3.07852 | -52.92397 | 2025-11-10 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e13569b2-f022-393b-8305-f46a3331d1b6 | -5.21836 | -45.03522 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66595953-bb4c-376b-9836-e85d9ca0306f | -5.8905 | -43.96277 | 2025-11-10 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 160bac50-b2ae-38b3-ae7a-10616d0cb79a | -2.94747 | -51.57835 | 2025-11-10 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35381c18-8183-34a0-973f-23904c1dcc71 | -4.4396 | -50.11237 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42f93e23-4da6-343f-891d-b4d1afef65d9 | -6.21192 | -44.382 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 080b2a92-5de6-3eca-b9f2-e8003edf6f1d | -3.34202 | -50.20435 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a0e73e-11c9-3f18-a2c2-8ce22ed54cac | -5.56532 | -51.20464 | 2025-11-10 04:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315bd42f-a1ee-3193-a38b-ff9a7321d946 | -10.45813 | -44.94354 | 2025-11-10 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2173990e-692d-3508-a178-e57cd1f56d6f | -6.8568 | -43.62457 | 2025-11-10 04:21:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83a61cba-e02e-32b4-ba25-80be04b77fba | -5.36879 | -44.72927 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fe56d36-5760-3679-a1ca-c8e905fea41c | -9.12835 | -50.08948 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29ef980c-2401-317e-b693-ea720fe3b5ce | -5.35804 | -45.80358 | 2025-11-10 04:21:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fa17237-db26-3ba1-9780-ab1269962240 | -3.32596 | -49.92213 | 2025-11-10 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae17acc7-5e57-3ba0-8494-b5ca108c3f9b | -10.48277 | -46.79958 | 2025-11-10 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a037f92c-178d-31e6-a8a9-4310c8ec15d0 | -4.59558 | -45.55145 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49249382-0836-3e7b-97a2-4905d0539ed4 | -3.40504 | -50.45536 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 920ceddf-6ec8-33e3-8fc4-07188eca70fd | -6.15054 | -43.29785 | 2025-11-10 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c6cf7b6-a2e9-387f-a567-d6b04161d883 | -4.11043 | -47.28407 | 2025-11-10 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5db8069-ca0a-3c9b-9dda-4cd125b68a26 | -2.93537 | -57.78402 | 2025-11-10 04:21:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df74df10-ae27-32f5-bdf3-9b890ed2da2b | -4.68346 | -46.55833 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa0105cf-41d9-374e-8bf0-66f90fbbdf78 | -3.69143 | -50.18833 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 44feaded-f0d1-38c9-a5bd-cd5d9829c48d | -6.21962 | -44.37613 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01853b18-94f0-3090-81fa-225280c5949f | -7.63294 | -39.82335 | 2025-11-10 04:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0db6e9ba-fc74-3cb3-99f5-e50169b9c413 | -4.01054 | -47.76149 | 2025-11-10 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eddd1087-ed1b-3ae9-bac6-8c1bf294a582 | -4.53322 | -46.61803 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f95e46d-286d-3032-a1cd-75ae82a4c7b8 | -3.34569 | -50.20934 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cef3c661-0eea-3edf-9904-2e0dd806b409 | -3.47309 | -48.98015 | 2025-11-10 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e17cce5-d5eb-3b09-964c-115bc019309c | -8.65286 | -38.14341 | 2025-11-10 04:21:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a0892c72-0690-34ae-ad70-f0ae461a38b6 | -4.91416 | -46.73149 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e08698a-7a70-3e00-9044-1c25fc10b412 | -3.83652 | -51.20543 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69a1235-f22e-32ca-87a1-c982dd798975 | -3.32958 | -49.92688 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f16a567-f2de-3961-989d-e36b926a013e | -5.18369 | -43.44465 | 2025-11-10 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eeaf9fa-40f3-3b21-af2b-38220d1fde87 | -4.43054 | -50.60858 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce17116e-5d6e-3df3-80c4-f4d8e30de71f | -4.05227 | -46.42657 | 2025-11-10 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c20c78-d1a7-3e5b-9a6a-dd46988a8c1c | -4.74739 | -49.5019 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e23621da-c734-35dd-af12-00b768384327 | -6.8738 | -40.73584 | 2025-11-10 04:21:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 83b32a02-c1cf-31e8-9b3d-ec07e4cdea11 | -5.64471 | -46.38218 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0422775-813a-3749-9ae2-0b5dad67f459 | -3.47023 | -48.97251 | 2025-11-10 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc3c8bc9-290a-322c-b2f2-fd8d3417e99b | -10.33632 | -49.64135 | 2025-11-10 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6d90346-0ffb-3fd8-8caf-d65016c7aa25 | -4.43896 | -50.11634 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9a0dac1-6792-38cd-8bc7-e9ca12674195 | -4.20928 | -49.77396 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 194adac6-d8e5-30bd-9694-b1fddea24fc7 | -4.20116 | -50.63084 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 969d54e0-c08c-3925-aa20-6ecaa7d65551 | -6.21523 | -44.38253 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 059bfeec-1e49-332e-b779-58c838c36474 | -4.57861 | -46.66885 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91066611-7a71-369f-897e-4dac06c26457 | -4.09587 | -46.28601 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96e31296-0330-3649-9533-1a6c3c72c794 | -4.12962 | -52.06572 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb43941b-8dfc-30d0-9b80-ae80ed6583fa | -9.9085 | -44.21719 | 2025-11-10 04:21:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ebecaff-975e-34d0-83e9-8d2864333b26 | -4.91508 | -46.70398 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a00eff9-3b75-3830-aecb-4780445b5255 | -8.01042 | -41.60219 | 2025-11-10 04:21:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 04438009-e7d0-3e04-bab2-1800c789fd3c | -3.49901 | -50.05212 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379bd067-806f-345a-9058-85a9fb258e13 | -4.85104 | -47.09533 | 2025-11-10 04:21:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41c9d29-bdec-39ed-b8b4-21fa917d9e7e | -4.80323 | -45.39885 | 2025-11-10 04:21:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87243fbe-97a3-3da1-8dd1-eaa4607b542c | -8.04657 | -39.68773 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf3200cb-4cde-3816-a307-910a5640b06c | -5.12366 | -44.73259 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 612d6f48-f21e-31dc-808c-225747b847fe | -4.75145 | -49.50262 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54a15bd6-9799-3134-b1b0-b75ffb9cba0d | -5.18967 | -46.15564 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46d65ed8-0165-3d3b-8303-8a122711ce7a | -7.05442 | -43.94822 | 2025-11-10 04:21:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36c9a6d5-6cca-3fbc-9d2d-9b3252599cb0 | -5.20012 | -44.91506 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9341057-3478-3d60-91fa-ef04849479f8 | -3.34938 | -50.21427 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b6fddd6-1d4e-3f81-bea6-6fb48ef08027 | -5.61176 | -41.07779 | 2025-11-10 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 801ca83e-3c71-3102-bc8e-9eeb11cf5bce | -7.92149 | -43.30851 | 2025-11-10 04:21:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85fb37d3-b1af-3fbe-a1bc-4ae92076dbfa | -6.06236 | -42.73494 | 2025-11-10 04:21:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| de86913a-1267-30d9-802c-f2b0e4e1c88e | -4.83835 | -45.85758 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47186b2f-91e0-3ed3-b960-28355f49f144 | -11.90798 | -43.82171 | 2025-11-10 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a22257a6-780b-3806-9c22-dd207ed2e65e | -3.84338 | -50.74633 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51fb75e0-fef1-35bf-a3e9-00eea60032e5 | -6.13154 | -46.14753 | 2025-11-10 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b56ce681-3915-31c3-8b82-80e906496c1c | -4.57799 | -46.67274 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd4cec7-f348-3c67-90c2-c9beac31af95 | -3.86902 | -52.27684 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656d0d5d-7cfa-3a8b-9a1a-08c0eeaab89c | -5.63585 | -43.91898 | 2025-11-10 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fae85de-6263-3958-b8a5-2fa6a5728419 | -3.78746 | -50.07251 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38c9d74-9917-3eb5-9da0-dfd562e828d8 | -3.42558 | -50.44088 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f78c0503-4c39-3830-9ccd-d01260a076f2 | -8.04203 | -39.69886 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c728cc03-702c-373d-8fa7-8ef47916cbe5 | -3.47366 | -48.97667 | 2025-11-10 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19d3cf4b-b865-36cb-a20e-31549ca20612 | -3.3253 | -49.92616 | 2025-11-10 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af4ddef-d3df-3a17-8323-467ec7707eb8 | -5.5914 | -46.2979 | 2025-11-10 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09fbc6f6-32a0-3683-afa7-d886e65d89e7 | -4.57661 | -45.54101 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0f126ac-2509-3fcd-97e0-a23fcbe42143 | -4.11393 | -46.12775 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d11cc6-baae-31e8-ae34-43b8be0ae553 | -6.53305 | -47.80608 | 2025-11-10 04:21:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b05ecc2-6606-356e-ba2e-2279a8401288 | -4.64073 | -49.59376 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f8c4f3f-1eca-3317-9aee-75aa0fb63ecd | -4.39537 | -45.97092 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e36f38d4-e234-32c1-ad4e-18d0783b77f9 | -8.04777 | -39.68842 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0dbe953b-24d4-3449-b250-7c5d0eeaaa76 | -10.15965 | -44.78815 | 2025-11-10 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e860833c-bb5e-37fe-b7f8-f8e003c01c72 | -4.63883 | -46.3959 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd177d09-6527-3790-ab86-778e31c58c50 | -4.27169 | -50.50518 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c27b5975-ba83-33bd-a94f-9ce06a54e25c | -4.8878 | -45.72189 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b15fe954-4446-3132-b3d9-556abe7107d7 | -4.76883 | -46.50556 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 544e123d-61ba-3384-b9a0-422a0fd9f47a | -3.46046 | -50.03078 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
