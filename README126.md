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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50ce52d7-d341-3da6-bdc3-8a13f6b8ccbb | -1.68952 | -54.38435 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 303b5b3d-89f5-3988-9336-e16f43e47cbf | -1.23109 | -54.15712 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24b99cd-af8a-39c0-b5a1-6f50986040a4 | -1.2014 | -54.22295 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e5c310c6-3a00-316d-9242-0c3b0edbb2e8 | -1.19841 | -54.10868 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e479943-4c4b-30ce-85a6-20dd624a1d26 | -1.19799 | -54.11139 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deba1da0-a298-37ad-a43c-5281efac9cdb | -1.19636 | -54.22214 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d5f93a6-52d6-3284-bd77-5c1aad0285ca | -1.19372 | -54.10537 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f24ef92-888a-3dbf-afcb-104fe4a8bb69 | -1.19329 | -54.10813 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd8e9766-c141-39b8-87c3-6fc2c12d9454 | -1.19286 | -54.11091 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ee911d8-3f9d-35b0-98c4-1c4069d4c748 | -1.18907 | -54.10178 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59d2dcd5-053d-39e5-abeb-2709a4d0bfb0 | -1.16335 | -54.20177 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0835ea6f-99f1-34a6-b4e8-8f6b0df7aa32 | -1.13367 | -54.22723 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94306a8-01d9-34ef-b2ad-895f38737d16 | -1.1325 | -54.10638 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee82eb8-ddc6-3194-99dd-c39965c05d87 | -1.13123 | -54.10591 | 2024-10-10 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9763936d-1a14-3a13-b059-5c662c950c63 | -2.19577 | -53.74374 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8120f554-73d5-307c-b848-a48aaf65887d | -1.15716 | -53.7812 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3e4e70-229f-338d-9ad1-026b70c0cde5 | -1.12915 | -53.4455 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6d0f74f-7dde-3ab5-8a2d-8c25faca2590 | -1.12862 | -53.44885 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26f16e2a-4753-35f5-8060-d48b2c72dd78 | -1.12792 | -53.44462 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc5629eb-3889-3d26-8ee2-414409ef1602 | -1.12742 | -53.44795 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebb6cb47-8eb2-3281-826e-01f19f5a7d9d | -1.12384 | -53.4447 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2038d255-1c4f-37fc-9834-d405ce7f9ca4 | -1.12332 | -53.44799 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2319a10-e54f-3df6-a224-5bd655802bdd | -1.12279 | -53.45132 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42d4913b-b917-3d94-806d-3fd52feda023 | -1.12211 | -53.44709 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c18d6837-5e48-3f99-87bc-23a86c9acc2d | -1.12162 | -53.45043 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe13c8e-a020-3301-8e0b-64962fadf44d | -1.11795 | -53.61867 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03dc93cc-c934-3e27-bc01-a6871c3da6fc | -1.11313 | -53.61501 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40720376-1253-3722-b5af-0566805893b4 | -1.1126 | -53.61858 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93e4d23b-dde1-39e6-a2f8-eed97fb192cf | -1.10792 | -53.61393 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70014418-fd82-36e4-a9e8-225917273f27 | -1.10787 | -53.61442 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17c138e6-7e9f-38ae-b6bc-7863fe9bebc2 | -1.10742 | -53.61729 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9148b251-66b7-3968-912c-d775c499b586 | -1.10734 | -53.61777 | 2024-10-10 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5edf5cc5-2264-329c-85bb-65dc1015d529 | -1.03063 | -53.73224 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7133323-3d78-367c-95c3-dacff9c9b4ec | -1.02596 | -53.72794 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e07daef-9f87-34c8-94ea-73d2e6119f5a | -1.02542 | -53.73151 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2909c577-1490-3759-9ff1-59c051b5fc0f | -1.02015 | -53.73117 | 2024-10-10 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34396af7-a4a4-3647-b064-441079084b83 | -1.61702 | -54.92274 | 2024-10-10 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bbaf0fc-0682-37dc-b8ba-23e19512474e | -1.52127 | -55.42013 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 634d7813-1af1-3287-b7b8-d6a1f965ff76 | -1.2983 | -56.05124 | 2024-10-10 05:33:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d7b866c-093e-3631-a4b5-8b55960ca015 | -1.25281 | -55.70071 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a38f59f3-4bd3-3c88-8e23-de9e1fae7f3a | -1.25209 | -55.70541 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2424304e-d8b5-39e7-a3f1-60c95d584f71 | -1.24897 | -55.6953 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74f7c84b-736e-34f7-a51b-3932aea5e6de | -1.24824 | -55.7001 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c388ce3-f75c-328c-89ee-bdfc76b49d44 | -1.24751 | -55.70488 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4acac95-2a24-3f45-a48f-6cf70bd88b3f | -1.24127 | -55.68464 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52810d2-4291-3033-9b27-d774fb8060da | -1.24057 | -55.6892 | 2024-10-10 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6f4bc47-872f-3d80-aee4-409e67be5c5f | -1.39399 | -60.21442 | 2024-10-10 05:33:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acb7f494-1fc9-3b15-8372-7c73abfbf196 | 1.88126 | -60.58757 | 2024-10-10 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 682e106e-bc23-3b4a-b3ea-40511c6f1f26 | -3.40964 | -50.33099 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66d878d3-e6b4-337e-898e-047e3608eba8 | -3.40584 | -50.33207 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e3d2112-6dd7-3bf2-91a2-cb7aae51a17f | -3.40294 | -50.32998 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 193808ee-d65b-33da-83ba-d3fb604101ba | -3.33735 | -50.12521 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5080c318-b6e9-3452-85be-a35de5a69c6b | -4.87706 | -50.5435 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3395f5e1-63e2-3e6e-ad2d-b8b36fed14f6 | -4.87476 | -50.53897 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d55ba0e5-2df3-3a0b-9c06-6ea28a8a582a | -4.87391 | -50.54488 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44b1113c-93be-3efa-a354-52791d7be9ed | -4.87033 | -50.54248 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e4f32d3-5296-39bf-84f2-31ae4c872624 | -4.86952 | -50.5484 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82551379-a171-3b3c-8bf0-506129c91584 | -4.83167 | -50.79296 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 774240d9-aa02-3b03-a3b2-da65da87e529 | -4.82978 | -50.79106 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e8a6184e-7d23-328d-a8c2-bc3bb1aea0c5 | -4.82897 | -50.79704 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9176e86b-a1df-367d-b110-4f40f9f12a50 | -4.82506 | -50.79179 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d12c624e-57ba-31ed-a6dd-fc2d71d72918 | -4.82422 | -50.79766 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5dbd042a-6d31-37cc-9471-fbebd0922148 | -4.82318 | -50.78978 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e33b8c46-ba1b-3ecd-bfb7-8372556063b5 | -4.82238 | -50.79569 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a790e42e-c0d2-32e6-b03a-0fa8968393f5 | -4.44982 | -50.49726 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61cb8fee-7e66-3a14-9453-1c65151a44a7 | -4.34751 | -50.5193 | 2024-10-10 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 849000db-33aa-3617-8e6d-261025bc45b4 | -3.7059 | -50.17437 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38670810-8604-332a-b8bf-e67ead3880b7 | -3.70503 | -50.18044 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c968532-b6c2-321e-b444-2869fcf920b1 | -3.69252 | -50.12244 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c43d300-4c79-3aac-8c33-3cc3656f2f71 | -3.69163 | -50.12867 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a829bf28-aa69-3be0-9e63-78fd8d3e2dcd | -3.68574 | -50.12126 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 811cd195-73ea-3eb3-8f73-b7a6671f07b9 | -3.68487 | -50.12737 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9fe040a8-3de4-333a-91f7-279189cec588 | -6.31723 | -49.98148 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f332272-561f-35c2-8970-4d1ad04e9030 | -6.31628 | -49.98883 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e04d0f94-caaa-3e54-a827-863252a5ed2f | -6.31562 | -49.99398 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9bfc387a-6f37-33c4-a684-5b628e33e8a6 | -6.31318 | -49.98107 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5fd14157-467e-330e-88b1-b195260d3ff4 | -6.31214 | -49.98878 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cdb51e4-3f9a-31f1-89f4-e039f35710cc | -6.31149 | -49.9936 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78d538b3-f334-38c8-ad25-bd65ba9598a1 | -6.30957 | -49.98484 | 2024-10-10 05:36:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1781d0fc-ce61-3038-b72f-3c9202ab3df5 | -8.5654 | -50.52855 | 2024-10-10 05:36:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bceeefb-85ea-380a-8fbc-fce2888753a7 | -3.5434 | -50.7925 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49071a7f-ccc7-337d-9d5b-cde58426b895 | -3.49551 | -50.80305 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bb984bc5-2c0a-3d1b-a288-21ee819ae38f | -3.38754 | -51.3479 | 2024-10-10 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28045c2e-16e3-3b27-bc17-1d4bd850f07f | -3.38681 | -51.35273 | 2024-10-10 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ab608c2-8866-3bc0-b594-397ecdbbe80f | -3.23648 | -50.84952 | 2024-10-10 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f60ad85-ba37-339d-bab1-2f619d6d9881 | -3.23612 | -50.84964 | 2024-10-10 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32238ff9-e83f-320a-a001-8c6bd4492368 | -3.22999 | -50.84869 | 2024-10-10 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a58d3a0-180e-393b-b7fe-55b60307241f | -3.22962 | -50.84883 | 2024-10-10 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42ef51f2-6e59-3d6e-84dc-5af338f2547c | -3.18096 | -51.23816 | 2024-10-10 05:36:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50e37466-30bf-3b73-839b-0537ce5c95e3 | -3.03309 | -51.10224 | 2024-10-10 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5589c19f-8f2f-3f3a-998d-8afe25fdc662 | -4.09483 | -51.02396 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1cc5f03c-7aae-3709-bd75-d8ed9a9a0bc2 | -4.0941 | -51.02914 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 08354c63-2062-3f2b-9cf7-1f893bf2608b | -4.0898 | -51.01274 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61fc13c8-19f0-31dc-85bb-c58b32a02fb0 | -4.08905 | -51.01807 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 05680a1d-4cff-3926-a6b1-e9ab7b8decce | -4.08832 | -51.02321 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9ad3dc3d-0b45-30b1-ad2e-26388ff04c9d | -4.0876 | -51.0283 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e7e75e2d-d09d-3732-9308-746c3d887965 | -4.08689 | -51.03331 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8ac84b9-3ca7-3db5-b593-038943f68acd | -4.08333 | -51.01167 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ee00dd6-b7a1-3e70-b11f-679733dcaafb | -4.0683 | -51.1184 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a33eaf92-d20a-35d4-ada2-37b078d8fe79 | -4.06178 | -51.118 | 2024-10-10 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README127.md)
