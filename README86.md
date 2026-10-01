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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cda0b24-ec31-3231-80fb-77bc0ba57dbc | -6.06787 | -57.61002 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d515dff7-4a65-31ad-bf4b-e2d4cd1f0d6c | -5.85511 | -57.76628 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 375343c0-1395-32ee-8e0d-22fd4831ec33 | -7.73001 | -54.79253 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d75685a-3b19-3550-b85b-004b31b52f70 | -2.91201 | -51.30839 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56d94953-86b8-308d-b7cc-129d37adea03 | -7.49707 | -54.99244 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 296708a2-b117-31b4-af56-1861790c2f70 | -6.54792 | -55.28017 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e9da157-4b9b-3d75-876f-3b7a62cd0c6c | -2.89826 | -54.13807 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cc968a7-7f37-3816-8235-803037d98d16 | -6.43329 | -55.80556 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c88447b3-1049-306d-8eed-2c18e90a90fd | -6.68777 | -58.86504 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3efc808-f4c5-36f1-aca3-537a6b0565ad | -5.1192 | -56.01027 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d63c9d76-24b2-326d-bacc-0942f097e33f | -6.67314 | -58.87186 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 407fa99e-2d60-36da-bc2d-9a46fb8a609f | -3.00942 | -51.06298 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9661b68-a8d9-34c7-91bc-0c15c7c5c770 | 1.10763 | -59.47472 | 2026-10-01 05:53:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb42d52f-8cc1-3c57-b743-9d79edd0cf85 | -7.71809 | -54.79078 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8931d2cd-d8e4-3a59-8138-e0cc9f5412f8 | 3.27897 | -60.61816 | 2026-10-01 05:53:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01ea6f06-26b5-3673-b345-ad08727405af | -6.84967 | -59.35798 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f7cabc3-6bd9-344c-bd9b-8ce451082cf7 | -3.38228 | -50.94131 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e8e29e8-edd9-323b-8023-e6fc5f1a2ec7 | -7.72405 | -54.79167 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92fedb0b-b056-3990-9b85-c798f6b10535 | -7.72345 | -54.79608 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1964ad-9c9f-3ab2-b3c5-dc845e072678 | -5.1143 | -56.00674 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0be3f2cf-1d1c-38cd-96d5-56090c99e51a | -5.86541 | -53.48603 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b606bb69-fcb6-3648-8a4b-7afba15edb06 | -5.86271 | -53.48885 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce9566ef-4012-3816-a57a-34b45291dd79 | -6.7475 | -55.0823 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c944349-bb32-393b-9604-bf8080469ff5 | -0.44664 | -52.01001 | 2026-10-01 05:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10366ae7-ca9c-35f0-992a-db346a9731ac | 1.84455 | -55.56241 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59345401-1607-3fda-b6b8-997fb3cd0a7b | -7.73539 | -54.79768 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa3c59e0-00b4-3bc1-ba3c-9708ba6a36af | -1.63661 | -55.127 | 2026-10-01 05:53:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efae97cb-f284-3b20-9325-ae5563b7199a | -5.11875 | -56.01339 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6eba154b-e23e-35c4-a99b-8b539c77662b | -6.08125 | -53.30849 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f199f289-a6eb-306d-ac63-7b2388a62b7b | -6.36875 | -55.13902 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b2212e7-2e19-3751-aac1-5ce1ae2a8621 | -6.68406 | -58.87117 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5975b299-bcdf-3018-91e5-c626aa5171d7 | -3.37414 | -50.94707 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2ea3eef-373d-3f93-98f8-3aa6c516c9bd | -2.89837 | -54.13634 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bab2c70-96c9-30db-b0e2-f0acedaa560a | -2.98722 | -51.0399 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f1a347a-a07c-3e75-b942-280ed2d86327 | -5.12408 | -56.014 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fef42e15-1e20-3099-980f-43a75bb18c7b | -2.90298 | -54.14535 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 83d975d7-495a-3f32-958d-bc6a7797ffd3 | -6.4921 | -58.53235 | 2026-10-01 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d51ea4ea-4efc-36a6-b915-6eb64690c6db | -2.9056 | -54.08731 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abe99edd-124f-3dcf-9a20-ad7222dd9c76 | -1.44768 | -54.45888 | 2026-10-01 05:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b46c87-2a41-3869-97ee-b7d19e0a70b4 | 1.71311 | -55.91793 | 2026-10-01 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e52023e3-1a96-3f7a-b7e6-12023a6e5769 | -7.49539 | -55.00482 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 698b4c83-5184-3461-b43a-42ac37dab4a8 | -6.69896 | -55.05241 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3f067d9-dc63-3f41-be85-1ff5bd858ce4 | -6.70517 | -55.04729 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ff18e93-50d5-39d1-b66e-07cf37dcd42e | -3.37809 | -50.94652 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e74ca454-e01f-39d5-8264-714c476224ac | -0.44103 | -52.00382 | 2026-10-01 05:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 174a5fad-0d96-38a6-b5c1-abe70889dbfb | -6.36821 | -55.14299 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eb85df5-5dec-37d0-9caf-875a346feea6 | -5.86424 | -53.49456 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94b61b16-9982-3bed-8505-67bc99c518c7 | -3.37711 | -50.95327 | 2026-10-01 05:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f92f553c-b3f2-32e3-b927-0b1c1b5c75c8 | -6.54223 | -55.27942 | 2026-10-01 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a3bca9-731f-3920-a447-ce74b0677865 | -5.86114 | -57.75784 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de0415bd-82fa-3df3-a5c5-d1a7d4e71af9 | 0.13786 | -60.40411 | 2026-10-01 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b6ed6d7-af96-3c7c-8a85-c1b1b66ead54 | -2.97515 | -51.02425 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6c572d-bdcc-3ef8-bd7f-fda1fc525e86 | -2.91077 | -51.31464 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60e81798-9c4f-338a-9a71-1233421b9865 | -1.63713 | -55.12366 | 2026-10-01 05:53:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68be8d08-879f-3291-9074-dadf1960e0e1 | -7.55537 | -55.03306 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96be601b-b48b-36b9-8cac-a50a7100b870 | -7.34536 | -55.59814 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7bc0d8b-19df-3f9a-8918-75842e2e0574 | -8.26563 | -54.74199 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 246974a5-e4fb-36d5-a616-973863ebe36f | -7.49174 | -54.98768 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7551b48f-380d-350e-b768-931f9280f424 | -6.6796 | -58.87051 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b094374-9a43-3d19-afe3-dd7c31a22d1d | 1.78631 | -55.64999 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8b90443-6e7e-38ca-8c0b-54e07a5de80b | -6.65601 | -58.87605 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4e2bba-8a75-32a1-a6fc-054214276879 | -6.68026 | -58.86613 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54134721-470f-36bc-bdfc-9d35e8f85c2d | 1.81124 | -55.61847 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a47499d-48ac-30a0-ae94-7835992bfa41 | 2.54193 | -60.60915 | 2026-10-01 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a91a1f-fc79-3a0d-b967-4b03fe5b1b08 | -6.14107 | -53.06063 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea3285bc-a1b8-3a17-839f-a192f258fd50 | 1.70579 | -55.90332 | 2026-10-01 05:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f8e2036-bc50-31ac-a9cd-f3abe40183bd | -7.55211 | -55.02674 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| caee29d5-bbef-3f6e-810c-24d73c9cb694 | 1.79031 | -55.64383 | 2026-10-01 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c2b2c18-81e2-3383-8f83-f82a63612a2f | -6.67514 | -58.86987 | 2026-10-01 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 108c92d4-ab1f-3ca0-b62c-f4cf2c4610db | -2.97921 | -51.04539 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b78fb34-855f-35e0-baed-22ead09901ba | -6.75276 | -55.08682 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b91acaf9-de77-3ca2-a0aa-ecfe8450fca4 | -5.85668 | -57.75569 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8be42ee-70cc-3a9b-b058-7f3e2e318d93 | -7.51419 | -55.0419 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91734e5e-ba09-3919-8161-1af922542a3c | -7.54952 | -55.03221 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e827770-4acd-3398-96c3-ea48c57f8acf | -1.81701 | -57.10017 | 2026-10-01 05:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fcf6573-e4b9-3d70-87d9-5d49f37a9533 | -3.18176 | -51.24251 | 2026-10-01 05:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 844ac755-e26d-34e6-aaa1-989b0a389d08 | -6.14035 | -53.06598 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07a93164-843e-3217-b1cf-5ebdd5d66d62 | -2.89763 | -54.14211 | 2026-10-01 05:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11d2fc7e-c14f-3fdd-83e9-17d6d4d6cb23 | -2.05661 | -56.87232 | 2026-10-01 05:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a52a5a5-9a9f-3b07-80f7-c4721ee10a01 | -6.13168 | -53.27424 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 624a2c28-189a-315b-8c5b-4bc9dd35d6ee | -2.96811 | -51.02318 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a07ff4e-838d-3c67-af6f-8218aedea2be | -2.90584 | -54.08919 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aec7419f-c1b7-35bc-b03b-2c8d8a6ee366 | -2.89916 | -54.09057 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b84ae961-71d5-39c8-94d2-721bbf09ee5c | -5.86041 | -57.76306 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd3a8e39-b540-3079-8cb6-e71d6e0a5232 | -5.11965 | -56.00721 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d89d5c65-dcaf-34c3-b6e4-9d056ef7e41e | -7.34868 | -55.59169 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d73329c-f324-322c-a648-9d048d7a2daa | -2.91769 | -51.3157 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8e52343-f4b8-3f48-8d66-cf8fb9732ac4 | -6.13664 | -53.28574 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15bac9da-8e6c-32a8-80f6-84dba3d416c8 | -6.1352 | -53.29619 | 2026-10-01 05:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69a45929-26e0-3141-8754-40d4b1269f0f | -6.69954 | -55.04836 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0ab3103-032f-342f-91f6-f1a5fc2b6a8e | -2.97316 | -51.03769 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 336f34de-05a3-339f-a6e0-be9092fd2962 | -2.9 | -54.08836 | 2026-10-01 05:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8b1daff-1e35-343c-b053-0132aa157c5e | -6.70461 | -55.05139 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c7cfc05-8b23-3623-b9fc-a244ca8ed06c | -7.70559 | -54.79338 | 2026-10-01 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a132a28-0128-3fec-a214-c6f9ddf9b0b2 | -5.11385 | -56.00987 | 2026-10-01 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8047689-f0cc-3988-9ed4-124138ac1613 | -5.8559 | -57.76094 | 2026-10-01 05:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6281c7bf-c77f-3164-807d-f6707893c8a7 | -6.48756 | -58.53165 | 2026-10-01 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0032ab40-f1bb-300f-bf9e-01bc1c9cd9fa | -2.98923 | -51.02642 | 2026-10-01 05:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 492decdb-b3dd-334e-8e8c-8dcea50f8d78 | -6.05761 | -59.91809 | 2026-10-01 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2c8f0cb-dab8-3463-b664-94590163afb3 | -7.34759 | -55.59941 | 2026-10-01 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README87.md)
