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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d7273b5-717d-3f6a-a6a5-738c3ef7cd7e | -5.60456 | -46.1725 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c842f82-b852-3083-8870-07347080c573 | -6.27047 | -44.96909 | 2024-11-20 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87176d00-6eb7-3e1d-a667-4b472c35fbba | -3.84931 | -50.69358 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 138714f6-56f5-3e6f-87c0-6ed1970b2ad3 | -3.18704 | -54.32066 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a244a2ee-b9d6-3f80-a368-4739d7c65032 | -3.41503 | -51.65323 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f1c6086-1a61-36be-b164-c5bf6d5fb366 | -5.69581 | -45.84723 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 320b4290-7652-3896-90d4-cd2b4418664a | -2.74463 | -51.82972 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ec95c82-46bf-33e2-89ee-fa26d9783a3b | -4.07754 | -50.03506 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0c6aa05-6e11-3dde-9ac7-80d98be2b59a | -2.19811 | -53.67821 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f2f14e8-1ee4-3c4a-800a-ecf24dbb40da | -2.2775 | -53.63626 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd629732-13a7-3def-99a2-a88a4473ee46 | -2.94268 | -48.33217 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9207853-c324-3d02-81cc-ff19a5238ca0 | -2.92828 | -48.32676 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f87f99c6-a0bf-39ca-985d-c0a5a128c9a8 | -4.44518 | -46.58258 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d2569ed9-6b2e-3f65-ac3a-030d813244bb | -9.17898 | -44.72119 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d9ab102-3a2c-3b17-a6a1-7a90bf85cac5 | -2.91827 | -53.06897 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d9ea42a-32f9-35a8-a5b9-3fdfda606897 | -5.22045 | -47.08265 | 2024-11-20 04:27:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68e7f8e4-8552-3079-9b80-55cc949d3cbe | -3.58707 | -53.89602 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b9d6e75-37ab-3e09-a38d-0b54d8e76a8c | -3.97945 | -49.91936 | 2024-11-20 04:27:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8966096-093d-3763-a042-0415af43e80b | -2.59747 | -51.7947 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 727035bc-0ed0-307e-868a-e1aae890400c | -5.75775 | -46.06205 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2e43515-5a68-3e74-9c21-60b7b88c8c75 | -3.24427 | -48.44197 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c94ee29-67da-3831-9d6c-a6806c27329e | -6.24134 | -47.27647 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3418931a-d661-350c-a461-6524127d6cc7 | -4.38274 | -47.75723 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12534c6f-2ea1-3a61-baa4-cf33ea054078 | -2.92328 | -53.05759 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32705f8-5c57-31ff-a6d8-d0fe62d5243f | -3.79053 | -46.93964 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0271a7d-b610-35af-9137-10608460a4ef | -3.7825 | -44.06426 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2efd12c-3544-3fbe-a7d8-555a8528fb2d | -2.78849 | -51.72236 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1252a639-ece6-34c2-9652-e0e304823faf | -4.38382 | -47.77237 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c33860c9-edeb-3a4f-ba13-834f7ed0ca48 | -2.69069 | -51.71214 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 595a61fb-2f58-3def-b076-6d6ebd9368a4 | -2.91467 | -53.08118 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ef415a9-2b11-3953-bc7d-fe713ac63189 | -6.28198 | -44.73637 | 2024-11-20 04:27:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9373fb9-8b33-3973-ae0b-3edd5e07ed9b | -5.54067 | -43.89685 | 2024-11-20 04:27:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f00a13d3-8a74-3115-bb07-24f75dc1663f | -4.32512 | -49.39201 | 2024-11-20 04:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 099a9090-03df-35a6-90b3-a55889a248b7 | -6.98583 | -47.0843 | 2024-11-20 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd049ce6-2d62-3483-9328-44059ccdabb7 | -2.7491 | -54.01895 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fad20559-aee5-3834-916f-8f7997c95382 | -10.22004 | -42.18988 | 2024-11-20 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f07ea7c-1560-3253-9ff5-e6b68ab4de5e | -6.31548 | -41.51574 | 2024-11-20 04:27:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7d4c776-971d-330a-be04-0c566f5d4e55 | -2.93174 | -49.4306 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a4084d-9222-390c-b1c9-ad50cc9a1ad0 | -6.82339 | -46.77503 | 2024-11-20 04:27:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f662e4e0-8729-3652-b1d2-d2868b8ab02a | -3.10589 | -53.75189 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba52c111-1f40-3175-8142-e4dd28b559c7 | -3.46578 | -48.25222 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ec18ebb-3c67-358a-a905-b828e070f682 | -6.22695 | -47.28139 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fe10ce7-c8cb-3e53-8b28-4ff7f1a2f002 | -7.49784 | -47.35493 | 2024-11-20 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17891998-183c-314c-b359-913ffd73c119 | -2.91624 | -53.07138 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00a49574-6eb6-3d5c-80c5-1f252819a5bb | -3.77096 | -51.68033 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 044600eb-3609-33c2-9fd7-24a822180e2a | -2.9398 | -48.32771 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09e0760b-d897-3e6d-97ac-f9cb63d36dbc | -4.11433 | -51.04967 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 316f3316-f8c4-3337-bcd5-1479efe454e6 | -4.5838 | -43.49978 | 2024-11-20 04:27:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c91fe5b-6070-38c9-b299-2d0e87dc1976 | -3.29425 | -53.85959 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58b6638d-9d53-327b-8c36-50d2a5407942 | -11.06046 | -45.37725 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e1a1053-e7a6-3f21-b45f-1fec24e54a59 | -3.2415 | -48.77767 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c0b67c3-755f-3555-a0c6-675ba728bb42 | -3.80945 | -47.80738 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dda56d8-8e32-34bb-b37b-bdd59f482534 | -2.95385 | -48.3299 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 147b6d38-1875-3c38-865e-d55b96b15e7b | -5.18271 | -46.17275 | 2024-11-20 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f6b882-22b7-3de1-ae08-ff3c77e9fc79 | -5.25546 | -43.83974 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5197973e-400b-3640-85b0-eb3f1661f626 | -6.24964 | -47.26701 | 2024-11-20 04:27:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7944370e-fdad-3f17-9e70-dd5cc99a9239 | -7.08997 | -49.32061 | 2024-11-20 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da0347a9-ed94-3eef-883d-ffb2515bbaa6 | -3.94742 | -42.62967 | 2024-11-20 04:27:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cc24414-1757-350d-9dbe-ad3032a6c33f | -4.2452 | -53.66562 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20060dfc-6e0a-348e-8765-479c91d15589 | -3.05456 | -54.40479 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c785d98-f22c-39be-b501-2ebfa9db8be6 | -2.9462 | -48.33272 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa9b5115-2ee0-3c67-8125-76d0673c5c31 | -3.18724 | -48.57178 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53a3003c-1e45-36f6-a210-dd60e32d79df | -4.96824 | -50.47567 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2a0ba84-0ca3-3c90-bfdc-612b44f3db80 | -3.01474 | -51.01036 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e90e6b0e-b061-3b6d-bf0d-2b45b5b51a2e | -5.13301 | -45.11279 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9befb956-d85f-338e-aa42-16f99273535c | -3.01065 | -51.00971 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17be0f0a-4ef1-3f3e-bc1d-1d89b75e3aca | -5.2994 | -43.07325 | 2024-11-20 04:27:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d15c6442-b50b-338c-a96f-f90f5f8fea88 | -4.53464 | -38.57851 | 2024-11-20 04:27:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01ee7ae7-8f17-39eb-b460-1a2d06c596cc | -3.7254 | -51.23626 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05df561d-f098-3911-aa05-e9e1680d2e99 | -5.83141 | -43.65149 | 2024-11-20 04:27:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d777338f-52e3-3010-ac6e-905dc4af3a1f | -2.92379 | -53.06495 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75416006-0020-342b-b5c8-a11a0f19264f | -7.31174 | -45.08922 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8b68cea-0c01-331e-8bf2-83ede6a7b8e0 | -7.99804 | -44.3914 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bd1718d-cf93-303a-bbdc-364f1804ef7d | -6.53678 | -44.18818 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 411ca280-8a9c-381e-af25-be9c19212d4b | -5.59464 | -46.17097 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27412884-9fbf-35f9-bad1-c4a33fc0d8bb | -3.23308 | -48.87707 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e40567e-d033-318a-b4f2-3f13ce079e7b | -7.14822 | -48.31918 | 2024-11-20 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65c4de60-b857-3eca-be0c-03cb8e8ad5a6 | -4.95409 | -49.49347 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7a8cdf1-acd6-35c0-89e5-f6480ae9ea1a | -4.36996 | -50.73164 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec27e815-ecc7-31ef-886f-5a94cd91d0fb | -5.51475 | -46.44444 | 2024-11-20 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acdfc255-cdd6-33f4-8b34-4b7926e1395e | -3.51557 | -53.79697 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df386f72-a135-30b7-8b3a-efdd49f50bf1 | -2.79897 | -51.79573 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe45b381-08ee-3fd7-b37e-84d151eb4a78 | -2.59699 | -54.00349 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f21f234-fcdd-3f2c-8e41-f741b0ba13df | -2.62352 | -51.79883 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0c6ed72-2fc9-3390-b9d1-371a3254acc4 | -5.7368 | -46.19653 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7a63901-7481-3f48-a7e8-51544b133324 | -4.89436 | -47.5925 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc74c774-c5da-3bf5-b505-6e6dce3cd961 | -7.56717 | -46.45327 | 2024-11-20 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac4eb9b0-6fcc-3754-876f-1057a2d3bc68 | -5.71994 | -44.81126 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e70ecae-80a1-3e8d-a7f8-1dc332c78676 | -3.13317 | -48.59204 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb0d2dff-1997-3597-a68a-90bbf3611396 | -5.49095 | -46.2036 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ca94d40-9300-37a4-8aee-d5f8c20e8cc5 | -2.62717 | -51.80372 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 715976a8-f57d-3c24-809a-1b7775c9b305 | -4.97973 | -45.42231 | 2024-11-20 04:27:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41c0a257-7162-3d19-863e-13e1f8d3c8c0 | -4.77621 | -46.48972 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 780d7489-75eb-34de-b69e-7f242b219ba1 | -4.10968 | -46.89998 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b5070a0-f234-36a3-b1e3-485881c10324 | -10.44964 | -44.88727 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e428fee-77ca-313a-b44a-6efc7b720cd0 | -5.01592 | -41.95528 | 2024-11-20 04:27:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7e7eaa88-f077-38cb-9580-790eacd8cb34 | -8.32121 | -45.11376 | 2024-11-20 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec77924f-c80d-39ad-ad2e-e99682821199 | -5.96669 | -48.06541 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 5ab9141d-d86a-3354-922b-c424c2fc4067 | -2.85302 | -51.58665 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4740b8be-9ef9-3291-91dd-0f3498977bea | -8.74053 | -44.08905 | 2024-11-20 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
