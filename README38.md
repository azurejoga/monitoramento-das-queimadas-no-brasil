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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b15591-181a-333e-8e30-309b46b408e6 | -5.19288 | -49.60896 | 2024-11-18 05:05:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01f3872-a955-33ec-ab33-f84222737cc4 | -4.95659 | -49.50381 | 2024-11-18 05:05:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecb942d8-3087-3dd1-9d40-7a54073e01f0 | -7.71364 | -45.66273 | 2024-11-18 05:05:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f7de93c-8365-39ca-8392-aa6f1942afd1 | -7.13249 | -46.63473 | 2024-11-18 05:05:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65f21949-c4f1-34fc-95f0-32cb5c05ab0d | -3.88059 | -54.34975 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f053077-9e0b-36f4-9dda-3597ca5cad43 | -4.70268 | -49.62713 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62bf622d-8e13-31bb-9662-156f1e45c311 | -4.3777 | -50.51594 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 823edef5-5c3a-3728-8c67-d7e21c47a9b0 | -12.57657 | -57.77425 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63cf4b1c-d2c7-3ab7-92cb-4ca1f66d1831 | -13.99515 | -60.34717 | 2024-11-18 05:08:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00b14215-9b45-36e0-83ff-88b793388ead | -12.56172 | -57.71762 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42588434-33b5-3c40-9178-84ac86105f63 | -17.36615 | -52.00389 | 2024-11-18 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d47d967b-af6c-358f-99df-b82121b89b90 | -14.2914 | -57.63817 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab64af5c-14d1-36b7-b551-279d8705ff5e | -13.01777 | -56.46241 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8655556-b4e7-3680-a8ac-3a0dc7075e1f | -17.10988 | -57.49026 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b10a6e2-6ef2-3b5e-a298-f839cd3f6560 | -17.36561 | -52.00834 | 2024-11-18 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5ffe02f-7ef6-3303-89f0-22a9f298056c | -13.92891 | -60.19738 | 2024-11-18 05:08:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 169fc4f1-a32a-3606-a85d-337a91f80d3b | -11.86371 | -49.86762 | 2024-11-18 05:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee621765-0544-38bb-8be1-6b174294a33e | -11.37395 | -49.79707 | 2024-11-18 05:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85c1a7ed-2b87-3f9a-9070-b581275cd7f4 | -13.02111 | -56.46294 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f68e0337-8186-3ece-8986-03b15893c5ad | -11.53706 | -51.27776 | 2024-11-18 05:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873b83e1-ffd6-3e10-99a4-5c414a7cec27 | -16.90828 | -57.49956 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 812aaada-b978-3653-9bdd-874cfe3238de | -13.01608 | -56.45106 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 011662bb-9c87-324d-a645-b7a5b93e16bc | -11.43569 | -54.29453 | 2024-11-18 05:08:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f02cfc2c-54e4-3055-9f3a-60571fd939d0 | -11.81519 | -47.06899 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07b59caf-ce2c-3862-b582-d644bc3bea90 | -17.10709 | -57.48604 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3cf4042f-2b30-3c84-8076-7e4de3b0f350 | -11.81858 | -47.06771 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7446524-c4d3-3eac-9f3f-b82120f89d05 | -17.08621 | -57.47181 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fc2dc406-2a01-37a3-8003-917563a0daab | -12.57329 | -57.73034 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3052e4a4-719a-3f3c-912f-75c530e76fdc | -16.94782 | -57.62191 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d94ff7fc-7bdb-3634-bdb9-af664a31fa9b | -12.55613 | -57.81792 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16030e07-81c8-3644-a0c7-22f6b4831061 | -17.09289 | -57.4729 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0d951c90-4199-3ed8-b055-643afebc5a11 | -17.08899 | -57.47602 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 10fa68bf-6dbc-3485-98e6-775c5c174da9 | -13.22237 | -54.16071 | 2024-11-18 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d5d500-6289-3b10-ba56-541f9d13e216 | -12.55446 | -57.82851 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fef6a7bf-b266-3cb7-8ee5-c06a75ce9067 | -12.55501 | -57.82497 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3607bc7-2589-3393-aa6c-6f18db68fc96 | -17.09011 | -57.46869 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3cf561a4-fab5-3da5-9239-4cb5fcf2b107 | -12.55668 | -57.81439 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31651abd-846a-3a7e-96a1-5edd0198dedc | -13.41856 | -56.61791 | 2024-11-18 05:08:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be62b116-99ec-37ca-b1eb-1a445418fbc4 | -13.01832 | -56.45881 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c270a94b-928e-34ba-948e-4f01f93cbf1f | -17.11378 | -57.48713 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c2ec8ae-f64b-3e1e-b9c4-03e18224d79c | -11.85371 | -46.93727 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c433fef4-1250-3587-bf5f-5ef173be5e03 | -16.07906 | -60.09564 | 2024-11-18 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e37572f0-21fc-35cf-861c-bd533def99ba | -17.11656 | -57.49135 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e414dc67-ee4b-3bea-91e7-044ca8093f21 | -16.90215 | -57.49481 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 30db1b7e-e811-3d0d-93fd-a505b2b6afe2 | -11.82378 | -47.07227 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ae69dba-88a9-3bd1-b38f-a4177bda2bbc | -10.78325 | -56.03217 | 2024-11-18 05:08:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4149710-69d1-300b-ad37-ca536ebe7ff3 | -10.95958 | -49.57369 | 2024-11-18 05:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7e1dcf0-34d3-3405-acf3-50876462af0f | -14.28809 | -57.63763 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd4f227f-7561-37ee-8333-d383b138c846 | -11.65292 | -57.35344 | 2024-11-18 05:08:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c031c3ab-1e91-3281-9f84-88f504cd723d | -17.0851 | -57.47914 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b1ea5d7b-d617-35ba-9ed9-c0c513e6a4d8 | -16.93506 | -57.63847 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5b630cdc-7dd1-3e8d-b18f-88e511bbebc8 | -11.42058 | -58.9892 | 2024-11-18 05:08:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dae8abe0-e354-3a1c-bd93-43b7db4d4639 | -13.01942 | -56.45159 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd11e050-b017-338c-9fcd-739785525ffe | -16.07288 | -60.09064 | 2024-11-18 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47658b48-3c92-3c67-a00f-f8e48af1e019 | -17.70248 | -54.08853 | 2024-11-18 05:08:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58c018c7-1a52-34b0-94d8-05a3724d003a | -14.61944 | -59.52572 | 2024-11-18 05:08:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02a5c900-c71e-3e73-a272-e2aee02f4a98 | -12.56502 | -57.71816 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97b0671b-2aca-37de-9c2a-dc7e53949741 | -17.09344 | -57.46923 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f0ed3813-edd1-3707-aaff-074ee078ad9f | -13.22601 | -54.16128 | 2024-11-18 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527554b5-a511-3290-96d5-e3550527876d | -9.92261 | -57.51927 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98bf2365-ebc2-3d1f-9255-6b57dddd88a2 | -16.90494 | -57.49901 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d126936e-d4cd-32f9-a515-9983e8885253 | -12.55281 | -57.81738 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2767f8df-8e1d-3232-a96d-e80ee717a495 | -17.11323 | -57.4908 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f5470de8-0a41-3328-83de-9e1c16c3b1d6 | -12.57437 | -57.76666 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c785175b-3543-3625-b3c9-12f4159f0948 | -17.08565 | -57.47548 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d1af134d-c66a-36ec-9159-eb798f7ebbc5 | -16.08587 | -60.09683 | 2024-11-18 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f2495ec-a1ee-3b5c-be10-e26eec777a3d | -16.95115 | -57.62246 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a0db65a0-0f9d-3350-9dd1-9c727b402f2f | -10.3605 | -56.34949 | 2024-11-18 05:08:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38cca8b8-e31a-3462-8c3e-f2fb044ee158 | -14.28864 | -57.63409 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 766e9acb-0a32-3aba-bc53-267caeac1f8a | -14.65277 | -59.61977 | 2024-11-18 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81a4af2e-1925-3698-8f22-474f0ebd3b60 | -12.57713 | -57.77072 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5054095-d495-3805-9bc4-93830c19d3e9 | -12.55115 | -57.82797 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8469ea10-0bd4-3c8c-9bb2-43c2f9901384 | -11.83608 | -47.08732 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fce2dda-3b05-3e48-a13b-e6d2f6505145 | -11.65623 | -57.35397 | 2024-11-18 05:08:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97547f23-ad06-321f-954b-a2303dfcec63 | -17.11712 | -57.48768 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bb64f2e8-e971-38ae-b1c6-39144afa4588 | -11.85419 | -46.93324 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d750cae-6945-3995-a09b-6642158cd79f | -11.82427 | -47.06833 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f59ef4f-51e8-39ee-9b4f-91f6c5045d22 | -13.02166 | -56.45934 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1844cc3-9dfa-3e74-a2b7-9c5746ea48bc | -17.08955 | -57.47235 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c420bea6-2123-3703-a6f4-e740bc85520a | -12.55226 | -57.8209 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b58f084-87c1-3ccc-b5d8-c59bc8a303c0 | -10.96087 | -49.57464 | 2024-11-18 05:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ad6aca5-3d24-3ca8-843e-c7ac5d78e409 | -15.29874 | -56.52528 | 2024-11-18 05:08:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db6f1e93-706a-38b7-85af-67cd3fea1634 | -14.65216 | -59.62352 | 2024-11-18 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c482dde-9ce7-3158-9a9c-4d8a5d780715 | -16.9517 | -57.61881 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69b69682-49b0-3bf9-9331-b26becd6e82a | -13.01887 | -56.45521 | 2024-11-18 05:08:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53958b1e-7d1a-392d-8bd9-05ee06e0b993 | -11.82088 | -47.06965 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b21665c-ca6a-3a9d-b9c7-ecb8c14b42c3 | -17.10654 | -57.4897 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8debacff-9131-3a27-8c62-9b72dc60a12e | -17.09233 | -57.47657 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2e73b20c-0865-3916-a1ec-d0ef73582afe | -12.5517 | -57.82444 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d69f624-2f5f-3bf9-ba90-6d7982a4f3ea | -12.58043 | -57.77126 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf847237-f0dd-3882-b461-ef7e44e56b8c | -14.28533 | -57.63354 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9d7da54-de01-3f58-a049-6ca580c903d8 | -17.11044 | -57.48659 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 002618fb-b024-31d6-a9ab-1c04f13f2844 | -10.15403 | -53.71767 | 2024-11-18 05:08:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b289112c-15f5-39c4-a7f5-a2c1573cbebd | -16.93228 | -57.63428 | 2024-11-18 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cbdeb5e2-ee0d-3269-95c9-13e21250eaa8 | -12.55999 | -57.81493 | 2024-11-18 05:08:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 549127d0-054e-35a6-99ef-5874d8ebd134 | -12.87976 | -56.76309 | 2024-11-18 05:08:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8d15082-28b1-31fc-8b9b-79ee8ee7ce85 | -11.41718 | -58.98863 | 2024-11-18 05:08:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc991559-b1b9-3aa8-bd8d-498655b54938 | -11.83562 | -47.09121 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 27898d9b-989f-316d-85c9-a326bccd9a34 | -11.8181 | -47.07162 | 2024-11-18 05:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 416e8930-8501-3707-a924-661d3ef0e739 | -16.09949 | -60.09921 | 2024-11-18 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
