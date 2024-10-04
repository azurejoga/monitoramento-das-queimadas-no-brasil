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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9b98115-ed4d-3d43-b375-f7a2cfdffe04 | -12.0124 | -47.371 | 2024-10-04 14:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c14d7d02-d70f-3f00-9a8c-1804d99886ca | -11.9674 | -50.1595 | 2024-10-04 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 35953236-a415-3233-b9fe-7eb0abe46959 | -11.9487 | -50.1402 | 2024-10-04 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 2fed467a-442f-39d4-8251-00b920f5d0fa | -11.9296 | -50.1425 | 2024-10-04 14:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 0455393f-a479-3e12-ab63-7622fb3f04ad | -12.7815 | -50.5758 | 2024-10-04 14:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 275.1 |
| 6d77effc-93c0-3503-b193-a5efaf503302 | -12.7812 | -50.5973 | 2024-10-04 14:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 51d40160-dd97-31a4-8dfd-e8218b7ed5be | -12.6826 | -54.6763 | 2024-10-04 14:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 2ae97f6a-2ed6-3222-ba3c-a005b514998e | -13.1779 | -48.6737 | 2024-10-04 14:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 64ea8f5e-4c0b-3728-94b8-161112b4b520 | -13.1443 | -46.3261 | 2024-10-04 14:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 98592ce6-e1ac-3b6a-914a-a888c47725e2 | -13.199 | -45.492 | 2024-10-04 14:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c552adc0-be3d-3cbd-a5b6-25e564517a4f | -13.1787 | -48.6295 | 2024-10-04 14:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| dfba9054-479b-3935-ad60-c6352b28b8f9 | -13.5062 | -48.6046 | 2024-10-04 14:16:22 | GOES-16 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 99bdc93f-49db-3750-bea4-e7a1bfa49e57 | -14.0382 | -45.1414 | 2024-10-04 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 293d5316-80b3-327c-abe2-b5e3d3ee8896 | -14.7935 | -48.05 | 2024-10-04 14:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| da1a65d2-7d94-3cce-bc14-0053452abc2b | -14.7939 | -48.0275 | 2024-10-04 14:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f586e5de-1a1c-32cc-a2ea-96db4065ffdd | -14.8548 | -58.1922 | 2024-10-04 14:16:30 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b96f47c9-eeb7-3ae9-ac5e-c0021037cb7d | -14.8355 | -58.1941 | 2024-10-04 14:16:30 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 4f066512-00ec-3128-98e8-8c2cd6fae8d7 | -14.8024 | -53.9014 | 2024-10-04 14:16:30 | GOES-16 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d4fa806e-b4ff-337c-8dbf-82880394bd76 | -15.6112 | -47.1869 | 2024-10-04 14:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f250d017-9ce9-3161-a61b-a6fdf4aaeda0 | -15.6304 | -47.2063 | 2024-10-04 14:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| dc87b8a7-8b56-3534-83ee-b290eaf2cbb4 | -15.6309 | -47.1834 | 2024-10-04 14:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 9199594b-e292-341e-b8ec-cb89bfc6c2dd | -16.9296 | -47.1455 | 2024-10-04 14:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b5fe6b77-824f-3122-a238-164b71ee5d17 | -16.8626 | -57.4744 | 2024-10-04 14:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 9840763f-78af-3d5b-9056-0be62dda8a7c | -16.7862 | -57.3606 | 2024-10-04 14:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 01b52006-0ae5-3bbd-b7a7-b29b24fec7a0 | -16.7471 | -57.3651 | 2024-10-04 14:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 9cfebb4c-c3ac-38d1-a71a-74fb463cd31c | -16.9179 | -57.6926 | 2024-10-04 14:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| aca6eb05-4274-3f08-b6f4-0d35f284824b | -18.8613 | -43.5837 | 2024-10-04 14:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.1 |


