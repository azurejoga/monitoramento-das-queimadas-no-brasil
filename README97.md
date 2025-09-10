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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df48179c-d989-3f55-9419-826fc78aad2e | -15.13678 | -52.38691 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd1664a5-177f-3c98-b138-fb41b2f2705c | -14.56074 | -48.77225 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d1bdecb-22dd-3b71-9010-af0236489092 | -15.25425 | -56.46095 | 2025-09-10 05:06:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a858c1a-5d55-3e94-a6b9-e366c41c60c0 | -17.2366 | -46.0799 | 2025-09-10 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a5e9211-fff4-3871-9469-5e1bb90ba72e | -11.78024 | -64.94051 | 2025-09-10 05:06:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06d9e52b-6f7f-3caa-b9ae-c0991d7de88d | -13.28895 | -51.72187 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7c62124-4c92-3845-92bb-ebd793840070 | -18.35508 | -49.34425 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bda3faf-bb48-334c-968c-bbf1eb95de8a | -15.81138 | -52.2454 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cae91d9-15f3-354a-a2b4-9d1a01f3151d | -15.02441 | -50.0878 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d5d8f0e6-e653-3309-8eac-e987a8487421 | -15.80077 | -52.25397 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e48125e8-5b95-35a1-893b-3cc62480738b | -17.20229 | -50.15915 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 002e8219-8c23-3f8d-b982-c4a1588dc807 | -13.29895 | -51.71846 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2c27a3bc-cf35-39bd-aa97-e80b0700ef93 | -15.93499 | -50.23632 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87316c6c-c512-3424-aa92-11af50839ee8 | -12.87546 | -62.11567 | 2025-09-10 05:06:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b44ec7f7-1b30-333f-a457-7455332023f6 | -17.74141 | -44.49492 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1480425a-1cae-3610-991e-b9cec479ae09 | -15.6566 | -49.93312 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 654e23e6-b967-3df2-9cc7-181b78679438 | -14.56737 | -48.7608 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8fea1cd-732a-37d4-80a4-9dba6596fb57 | -15.13214 | -52.39027 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcb7ca53-3ea8-3e36-9115-8cb4139b8382 | -17.18273 | -50.15614 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d4f7019-de3c-32bf-bfaa-a7bb175f3069 | -17.74451 | -44.48268 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c37e0600-2d54-3d59-9b34-168f57088339 | -15.08959 | -50.07152 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f737ecec-f537-3ec2-84c3-d80c2d7f494f | -18.4546 | -46.47227 | 2025-09-10 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55b80620-8bab-307b-9614-7a13804b28c4 | -16.62399 | -49.75911 | 2025-09-10 05:06:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 049e7930-d891-352c-b368-77cc5c907205 | -13.29783 | -51.71928 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83f17cb3-f5b6-36e2-bd0c-8ad693cf4056 | -15.5119 | -52.76622 | 2025-09-10 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b002f612-0f19-36ac-a511-264a34722801 | -15.80711 | -52.23844 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8e23100-865b-3c0a-b5c3-96c1c4505fe0 | -15.09794 | -50.08261 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc8a185c-55d0-3b88-a425-59d042c9ce54 | -16.45725 | -51.97132 | 2025-09-10 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c7dcbbb-ff5f-3c66-b437-c066b3e5ad11 | -16.62736 | -49.77349 | 2025-09-10 05:06:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8086d875-bbda-3f78-9567-9a5a6c9f482b | -15.81125 | -52.23935 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2846d1b2-46b1-390e-b23c-957dc3453698 | -14.93397 | -55.93759 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54ae0a6a-eb28-3993-8476-8950cef9dd47 | -15.51666 | -48.39024 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec1f6112-181b-3fc0-8329-f879349dd9a5 | -14.93058 | -55.93695 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc30d8b2-065d-3fd4-8b49-074af61e4b18 | -17.70695 | -44.42745 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24d4867e-f57d-3740-aba4-fc03121622e7 | -15.09496 | -50.06757 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12a79b3e-ab98-3114-84f8-9732ffb8f563 | -13.9403 | -48.26002 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59fe0f1d-4946-3ddf-9d82-b80133c7673f | -15.87645 | -52.20398 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f23bc011-2537-33b3-9cfb-45cad53fd9c5 | -18.00608 | -47.12045 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3247e587-26d8-349a-8806-6c40c0482a35 | -16.46619 | -50.67116 | 2025-09-10 05:06:00 | NOAA-20 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10021054-75c8-3025-93d0-e661b33deb8d | -16.12307 | -55.86465 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 920ac558-bff3-328c-8b79-37bd6b252902 | -12.62586 | -56.96336 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c94704d4-d8c8-3c17-a507-7ec64b2690ae | -15.10332 | -50.07854 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b659f7b4-aaf2-33e1-b848-bda04c492821 | -15.2739 | -53.78465 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91c8ce45-a2e0-313a-9511-242620922391 | -15.01534 | -54.85215 | 2025-09-10 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 338ef012-fdbc-36e1-812a-90a3c9f0a027 | -15.80441 | -52.25854 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| acf23478-3c3e-348a-9b13-709ba5ee9418 | -18.03579 | -47.14964 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 028ed48f-ae0e-38b7-b3dd-15417441e1b3 | -15.10737 | -50.08569 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f12b19b-9257-38cd-b789-39209bee0908 | -12.87152 | -62.11494 | 2025-09-10 05:06:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0664c80c-39f1-3f15-9d94-d7af4a381263 | -13.13126 | -54.92069 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e342fc9-3fbe-3d42-84cf-a04182372ae8 | -13.93994 | -48.263 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b69718d-365f-333c-ad8c-11c7a17911a1 | -12.64662 | -55.95367 | 2025-09-10 05:06:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7961d20c-f83e-3383-905c-366a32aab7a2 | -14.42788 | -52.94883 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ee509fa-564a-3f85-a32f-90fbbe455c11 | -15.02434 | -50.08798 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 334d9938-61ef-38bc-986a-fa4f8ff435ad | -15.90182 | -50.18839 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5be8f76-aa7e-3240-931c-098bad1a7e4b | -18.13288 | -51.72234 | 2025-09-10 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f9f2cf6-9145-3581-a9ee-aa066fb07825 | -15.16449 | -47.9544 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08f5aa93-794f-3346-ab03-566c2277d422 | -13.29477 | -51.71781 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2be934ba-8843-3334-9577-b8d3b5cda707 | -17.30482 | -46.75953 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf8df6b-61ba-3cd5-b1d0-1f463199dbcf | -14.8981 | -50.12313 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8b91a254-afef-3cd9-82c5-92c3848130d8 | -14.61423 | -46.35843 | 2025-09-10 05:06:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce55a89-20c1-37d7-8448-625191608ee5 | -14.55585 | -48.76899 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb9b2826-0b0c-3def-8ed4-80150acdef4f | -15.52562 | -48.38213 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab695906-8360-36d9-9dc4-723279feff71 | -15.80545 | -52.25079 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c1812b7-d7cf-3b58-844f-355b38596014 | -15.85962 | -56.08543 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b96246b1-9558-3352-a2e2-a542786ca235 | -15.13104 | -52.39836 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f35a7b43-3f9f-3acd-b360-e42bd1319644 | -15.96025 | -50.22906 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a492df4-bf4f-3e16-b0e2-54ba6619c68a | -14.89978 | -55.86218 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bf95f31-125d-3a7a-9db1-a508c9ebbe9d | -14.55808 | -48.75006 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed698a70-fc22-3b96-ba1f-07f7fd58d8e6 | -15.10753 | -50.08376 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6b787fa-8888-3fba-9a59-fa0e522b9ec1 | -14.5611 | -48.7692 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9961650c-cd33-3e4d-b39c-24771a2bb3b4 | -14.88555 | -55.86372 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89fa03e3-eeb0-3423-93b6-294eabae26e9 | -15.01154 | -48.02016 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 285ec86d-d694-3664-94a0-422439507d8c | -12.60818 | -56.96773 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b97d99-8aeb-39ef-8ea5-dca1083f9bb9 | -14.89912 | -50.12021 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f97ef87a-465b-3e8e-8db1-9ccf6a10a9e7 | -18.00648 | -47.11653 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ba13689-7e62-3213-a4f5-e48746dcf7cb | -16.57212 | -47.79184 | 2025-09-10 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec519134-cab2-3362-b2b4-8eb268aa59ef | -17.20095 | -50.1705 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17b92c4a-df44-3594-b8ae-c6be6a7d12b5 | -19.64355 | -45.04609 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5ab6b94-7508-350b-bfe7-d930dc99e894 | -15.5236 | -48.37775 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eeb7c1b-40db-3004-a062-b8a470cff4f9 | -13.96615 | -48.22608 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a41f7aec-e122-3cc0-ae12-e7dd0cf8c33f | -15.01112 | -48.02385 | 2025-09-10 05:06:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcd89e93-4367-3f20-82cc-fd548f14d898 | -17.73433 | -44.49496 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c56150f8-d352-3da5-96be-282b52a250d9 | -15.84178 | -52.27373 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85c99778-5819-390c-8439-4f71484d198f | -14.93 | -55.91751 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68cf88eb-e754-3ff9-9b10-6de9c9946d4a | -18.35546 | -49.3408 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4174f92-75ed-3a30-8711-5e76cc7c9adc | -15.25434 | -53.78671 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79f1be5d-5b02-3cd6-84e9-3565b4fd5368 | -13.12662 | -54.92797 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69817e80-71e8-3afe-b33c-92ac30deb2fa | -14.90034 | -55.85839 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dfde944-3b3c-3c5f-a220-3d493becb14a | -13.34447 | -51.69676 | 2025-09-10 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5f1eea6-14e5-3cc4-93d2-a9cb3bc564e5 | -19.6441 | -45.03895 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a31211a5-e30d-37da-96bc-6c268a3856e9 | -17.1582 | -50.15322 | 2025-09-10 05:06:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8906e8f7-6a7c-3066-b2e2-fb9a12376f6c | -16.67004 | -49.13945 | 2025-09-10 05:06:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bdc7857-4187-3d94-8ce4-5c6ab04d2522 | -15.83846 | -48.96151 | 2025-09-10 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 225de34e-8235-3125-8e9c-b4e7a88a8a75 | -18.01343 | -47.12915 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5df7947-28c6-30d0-b31f-4b9283013bb0 | -18.0309 | -47.13738 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5d2342c-ee91-352e-889d-b4636fa32099 | -16.34638 | -52.93856 | 2025-09-10 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ca45f4b-e2bd-3edb-aac8-0821f28bbbe7 | -12.35298 | -63.63642 | 2025-09-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c1a1387-57df-3201-b17b-375f1b103bb6 | -14.46558 | -53.33575 | 2025-09-10 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da026916-a26f-3b46-9928-31e5b3caefc6 | -14.56144 | -48.76632 | 2025-09-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4493e6ae-8270-3410-aedd-8201f278b529 | -18.001 | -47.1106 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README98.md)
