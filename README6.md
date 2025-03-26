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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a0e4eb-71dc-332f-afb7-b24183baa5de | 2.60967 | -61.50304 | 2025-03-26 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56fde3b3-b9f0-30a3-9dc0-030f0da7427f | 3.97498 | -61.50539 | 2025-03-26 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53eb5437-75d7-3a8e-9094-3a16fc771fcb | -1.7255 | -54.3365 | 2025-03-26 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d7e742d-e35b-37a2-a986-18c10bbb3c95 | 2.19222 | -61.80838 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3eb06464-a73b-33dc-b32a-dcb584047479 | 1.52786 | -60.71038 | 2025-03-26 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fde9e6a-8734-3a76-a98e-4d8cf5f61f1c | 2.19714 | -61.80769 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df82c2e2-7e3b-3263-829a-4bea479c306a | 2.11429 | -61.82515 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d765510-f76d-3c28-b2f9-987edf023e89 | 1.11023 | -60.54177 | 2025-03-26 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17d2b967-72ad-3f21-82ac-76c0ac3d6f8b | 4.68154 | -60.90437 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab6f6f3e-a563-3acc-ade4-967a946cb051 | 4.66783 | -60.91122 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16a4b173-49ab-3e5a-93c9-c750083f3cf9 | 2.61453 | -61.50237 | 2025-03-26 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bf77e93-c8aa-397e-935c-54a8211774f9 | 1.3869 | -60.80804 | 2025-03-26 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60cad31c-1385-31dd-9251-9798b44c4169 | 3.96295 | -61.50302 | 2025-03-26 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f393e0f6-b600-3927-afe4-41f11b85e9a6 | 4.65444 | -60.92028 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abca2dfc-4f16-3939-8e8f-4b468b679a9b | 1.38334 | -60.80592 | 2025-03-26 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8700a24c-856e-3859-8541-8c48a9b7cef6 | 4.66306 | -60.91208 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4a6707d-8bde-3316-97f5-94d01e9d617b | 2.16928 | -61.82278 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e4701e3-e25a-332b-9454-c77625162528 | 4.67678 | -60.9053 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8de10c08-4977-3b30-abed-379780b49712 | 2.60888 | -61.49777 | 2025-03-26 05:01:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbc00eb0-328d-3bd1-a449-c4b9a6ed1baa | 2.198 | -61.81321 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20018139-b1cd-3e81-bf28-69a17d85d1b0 | 4.65841 | -60.91381 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f5885d2-3b31-3318-a0da-7a7f3c51e083 | -1.59868 | -53.92785 | 2025-03-26 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0809c8a4-7eb0-358d-a00e-cdf6baffc58a | 2.19969 | -61.81119 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d06043e-15a9-337e-b0f7-8e70577808b1 | 1.38787 | -60.80523 | 2025-03-26 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f6a5d3-6f9a-33db-8247-c628e690c478 | 4.65377 | -60.91564 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d860529-18dc-3ce4-b95b-bae8a892ccf7 | -1.72881 | -54.33701 | 2025-03-26 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11c043b6-d732-320f-accf-9a1390f7b457 | 2.19394 | -61.8063 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ed2b633-3a5c-33f7-a9f1-64a0fc1ac60c | 3.97418 | -61.49979 | 2025-03-26 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87dc1b89-21d4-39ba-8c9e-4eb6402f949c | 3.97284 | -61.50154 | 2025-03-26 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a78c9241-860d-3d8e-9f98-6a6b7f8a26d6 | -10.57959 | -45.1394 | 2025-03-26 05:04:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdd519ed-8d6b-3caa-b23a-e0a88411cda0 | -8.13617 | -43.14171 | 2025-03-26 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b09019f2-b7ac-3a19-9075-9716df11c78a | -10.579 | -45.14445 | 2025-03-26 05:04:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e15ede1-aa29-329c-b339-f956393bbe74 | -7.06154 | -44.38273 | 2025-03-26 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0beb1d01-8e55-3320-aacc-0d93e3262363 | -6.73509 | -44.81569 | 2025-03-26 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d076dc77-ee0e-3a9f-b0dd-ec0cf46d134e | -9.23323 | -47.91412 | 2025-03-26 05:04:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e1721f0c-6693-394b-be9b-cf63731627a7 | -2.5303 | -57.08012 | 2025-03-26 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35f420ae-112d-3c60-8b97-67d1f7877d6b | -9.84174 | -45.50833 | 2025-03-26 05:04:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 434f3078-76ae-3128-b55d-5dbf9be96bc4 | -4.56052 | -53.20248 | 2025-03-26 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c35cd837-a394-3dd0-8679-5f90cfb6b31b | -6.2118 | -48.05554 | 2025-03-26 05:04:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0bf1546-5932-3640-929b-e2307c32cb42 | -8.13476 | -43.14283 | 2025-03-26 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e40b96c-b989-36e9-a5c4-eaf945ddcd3d | -7.06222 | -44.37751 | 2025-03-26 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ba3e2b7-10e2-35a6-a2e6-a1282b0e7761 | -6.21543 | -48.05688 | 2025-03-26 05:04:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91d50c03-5829-3aa3-9fda-904f3248c999 | -5.35636 | -54.80344 | 2025-03-26 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8e4ece8a-b4f2-3cd8-86b7-f47061f0615f | -6.01786 | -47.10992 | 2025-03-26 05:04:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| fcd51007-6b23-394f-b17c-4baa6e5e0b4c | -0.63504 | -65.50922 | 2025-03-26 05:04:00 | NOAA-21 | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| d90fb9c7-9c68-3f3d-bda9-8a448e988209 | -6.56496 | -44.78599 | 2025-03-26 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1473aae-5812-36b4-b68e-b48b3f730d00 | -6.65318 | -61.29421 | 2025-03-26 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 352f1d40-4ef2-39c7-aa83-1bd4e60973da | -3.95956 | -51.45689 | 2025-03-26 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35719dd3-6e7b-33b6-964f-d5171da1cce9 | -5.15822 | -57.60011 | 2025-03-26 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ce93422-5919-31b4-bb1a-ba35225569f1 | -5.63221 | -44.31941 | 2025-03-26 05:04:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 129a3077-6a8e-3ac6-9da4-1a955c5b0315 | -7.66417 | -46.24625 | 2025-03-26 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 24b00e22-a446-3778-b085-172b64f5146d | -7.48715 | -50.51129 | 2025-03-26 05:04:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| e5960e72-5a3b-31a5-8a43-af1d0b1295fc | -3.9435 | -47.99069 | 2025-03-26 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dc41e1a-fb91-397a-9456-3f08febefc3a | -6.56353 | -44.78336 | 2025-03-26 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94b7503e-7fa6-3df6-9c00-4c65884d9a7d | -3.00637 | -48.04115 | 2025-03-26 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0efb9d2a-9d4f-330b-b5ae-f806b4e70af1 | -13.5127 | -60.38694 | 2025-03-26 05:06:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fd7a1c3-f43e-3b6b-bbeb-a5ffa5260d86 | -16.0723 | -47.738 | 2025-03-26 05:06:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c02b2400-1d00-34d1-904c-107a5a0b1b9c | -13.77935 | -55.90675 | 2025-03-26 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8291ea87-b2b8-3b07-9c47-ceffaf4f9c1c | -15.64916 | -46.63864 | 2025-03-26 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b1c8cb-c7f1-3c3d-8853-4d57f55c2d3a | -11.84339 | -46.3212 | 2025-03-26 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47a048e8-e407-39fb-8572-1245310b4663 | -14.1713 | -55.26486 | 2025-03-26 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| dddd450e-cbd2-3c5a-95b2-002c4eb492be | -14.42709 | -45.57542 | 2025-03-26 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f1613f7e-c997-3416-96eb-68ce8215551f | -13.38314 | -60.33586 | 2025-03-26 05:06:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76f6f469-24cb-320d-abd8-23c7363f2ee7 | -15.08642 | -49.86849 | 2025-03-26 05:06:00 | NOAA-21 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68b28547-4916-347f-ba33-e8ed05436b4c | -13.1832 | -58.13766 | 2025-03-26 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 91e2c47c-2e42-38fb-9e42-d21212b45270 | -15.496 | -44.27704 | 2025-03-26 05:06:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c953c03-8350-3f0c-b93e-936c7cb3715c | -12.89705 | -52.93898 | 2025-03-26 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cccd64f6-c3c8-3a32-aa93-0c6f02845fa2 | -13.8767 | -58.27045 | 2025-03-26 05:06:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 10781d49-849a-3cde-a9a0-89b5b6ba5bc3 | -15.49143 | -56.47072 | 2025-03-26 05:06:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64041c01-a949-3f45-809d-3180f4a88c39 | -11.7024 | -58.44368 | 2025-03-26 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 857c4d99-5bc6-3bd1-bc71-7e33c8dd3b15 | -14.67202 | -44.92856 | 2025-03-26 05:06:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c8c739fa-991d-32b5-8eab-03ebe266c43b | -14.53073 | -52.80914 | 2025-03-26 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec47f7ac-415f-3c3e-8cf5-f17828d65b2f | -15.44496 | -57.1549 | 2025-03-26 05:06:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5062d27d-a039-3615-ae2f-ae9e40140e6a | -14.6203 | -52.97609 | 2025-03-26 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9ba1f1a5-382a-30d3-8fe5-8bd2d59c9da5 | -14.47266 | -56.10019 | 2025-03-26 05:06:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1c353cc-9830-33df-bc90-3245badfef17 | -11.86481 | -58.04411 | 2025-03-26 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ae8e8b68-fae3-35a7-af8e-f70ddcc0d9f8 | -19.40615 | -56.633 | 2025-03-26 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 4a028def-6102-3cef-8589-d1157bf23263 | -17.26732 | -55.41565 | 2025-03-26 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 1472a89f-f426-3859-a4d3-d8861ffab381 | -15.81745 | -57.45097 | 2025-03-26 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5e83cace-9839-342c-afcb-8fa08f104777 | -19.74657 | -54.79161 | 2025-03-26 05:08:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a2cbfef-a673-3f9b-950d-2d3f0bcd9028 | -18.57067 | -47.54884 | 2025-03-26 05:08:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76a1bb5b-c875-3a29-9038-a5d176d85a60 | -17.10283 | -54.94527 | 2025-03-26 05:08:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 82815c8e-22af-3450-8d04-0b6dc3a902ca | -19.89223 | -48.35656 | 2025-03-26 05:08:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a22987e-c1f6-3adb-a26b-15b6f0d4bfe8 | -17.1298 | -51.59148 | 2025-03-26 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5998f8ad-8c69-3d2a-b38d-1233c95140ee | -22.18741 | -45.32897 | 2025-03-26 05:08:00 | NOAA-21 | CRISTINA | MINAS GERAIS | Brasil | 3120508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 09f777c3-da02-3e4b-8e8b-cd501411fa62 | -19.03956 | -57.27397 | 2025-03-26 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 8897ff5d-36b6-34e3-b056-9bffa1bafd44 | -19.44885 | -55.11001 | 2025-03-26 05:08:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2949fa7-b38f-31c0-a9d2-96024edf57cd | -18.53485 | -56.17618 | 2025-03-26 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f94ee574-cc43-313c-832e-c57c06df8c8d | -18.03335 | -55.56095 | 2025-03-26 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9cef5a51-8676-3143-af22-515d053b9846 | -16.92269 | -49.72614 | 2025-03-26 05:08:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 856d16ce-5b03-34a0-8afd-d3732ff7f744 | -18.99638 | -54.65837 | 2025-03-26 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2324d423-dee0-3a34-9b6e-8967ad87df20 | -21.6886 | -56.54753 | 2025-03-26 05:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba25440c-d624-3f99-920c-ace1ecfd5500 | -23.50503 | -48.74582 | 2025-03-26 05:08:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 6d6c1a26-eace-32f3-8568-2feefd20a2bf | -22.76434 | -44.76929 | 2025-03-26 05:08:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| f090c96e-3ffa-373e-86f2-b2f380ac12b0 | -19.68389 | -45.37888 | 2025-03-26 05:08:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e818c405-8980-3b0d-adc6-f015b8a80bd5 | -15.55556 | -58.10775 | 2025-03-26 05:08:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 526e3653-fd58-388c-81ff-2c796b3c7e28 | -17.11292 | -47.90419 | 2025-03-26 05:08:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ca247a72-b76a-313a-9439-55f7b2fc6eaf | -16.18543 | -55.07347 | 2025-03-26 05:08:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8bb64bc-27da-3473-a980-a40bfa0662a4 | -19.52204 | -55.52642 | 2025-03-26 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| ea99f8e2-f3ad-3716-8813-bdb260862468 | -16.983 | -53.02069 | 2025-03-26 05:08:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |


[Clique aqui para ver as próximas entradas](README7.md)
