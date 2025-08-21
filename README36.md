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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac1faec-ad52-3acd-b00c-2d05a27ed65b | -13.181 | -46.90812 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c8f15bf-2c3b-3694-b991-c033b0944cc7 | -12.88647 | -46.06851 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da1ce108-61f8-3021-b182-d0c2d7309be9 | -14.12531 | -45.39617 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfa55bee-3ad8-367c-8dc0-a50b776f23ca | -14.89498 | -48.07086 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59e8ff3d-af41-3122-b503-6e131577bc2c | -14.85995 | -47.94424 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c197001-aa11-33a3-ad29-ba050e0e9f44 | -13.53917 | -47.03709 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 807f9dfa-8f33-3cef-9d44-5f89bbf76fd4 | -12.95097 | -46.24835 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0726df7-ba7f-3b25-99f7-85730085d419 | -12.90008 | -46.07074 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eaa1432f-74a1-3210-a83a-466c81a3328a | -13.81405 | -43.22642 | 2025-08-21 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e31ec45-fd0d-3c22-849f-bdc300390fbe | -13.03938 | -45.16782 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3424e94b-da81-32fd-9eb1-595a68fc534f | -13.58995 | -47.01329 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f94134f2-d07e-3866-9b22-c5ab8888daf4 | -13.14816 | -54.92561 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24d601b2-554b-3fc9-9f04-42a41f80da7c | -14.90223 | -48.07192 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a648109d-6cda-37ae-83eb-1c0f14275a1c | -14.12194 | -45.38433 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f83ac1-1deb-33a1-876b-92f4cea4a99e | -11.80828 | -55.52431 | 2025-08-21 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 99762bf0-2c46-3d0f-bf05-dc7b0bc0c0cc | -13.53567 | -47.03648 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c70b025a-f12e-337f-b8fd-bb0f76ebf413 | -12.95748 | -46.23021 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f182c99d-167b-38b6-be7f-074ea493ec32 | -13.0325 | -45.21071 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a235d466-fbb7-3584-be93-a4c1630573de | -13.38366 | -46.23198 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff7b5725-0379-3db7-8671-d73bc4a3544e | -15.54133 | -42.27029 | 2025-08-21 04:19:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e23753e-f97e-3f54-bc0a-f8318ddc4cc1 | -12.94444 | -46.18164 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f20bfe41-9c6e-3f0c-979d-603054e95a38 | -13.18169 | -46.90397 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a1c48f8-6ec3-3fd2-bcd3-d2cb632e7453 | -14.8813 | -48.06404 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d5c3ee9-7668-367b-ac64-22c7471af865 | -14.12252 | -45.38075 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0cf7c0-e630-3886-a05b-88970ee205c5 | -12.93862 | -46.19562 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4a92696-cbd2-313c-89dc-d15bf6a042e5 | -13.62974 | -46.88222 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45cc49a2-f126-3225-8308-8d8229c4f79f | -13.54065 | -47.04959 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 737e8f56-0fb7-37b8-bb9c-5bd0e2c4986b | -13.49525 | -47.05905 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08342111-4b31-3a97-b894-943f6c58e1cc | -13.15242 | -46.90713 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c037584-b783-3624-b8cf-9cdc60fc066f | -13.32965 | -54.42905 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7afb367b-6f4a-3bca-96ae-c920c04df68a | -13.48608 | -47.0492 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfef887a-6ad7-335e-96cb-4fd58780642a | -13.3348 | -54.40294 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70f86f98-4d9e-3bf1-a166-6e5d86da0b47 | -14.85426 | -47.93424 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b90090cc-283e-31c9-b5aa-9b20fa0e94f3 | -14.84639 | -47.93705 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1a7a2d1-3e60-3b0b-8066-6dff094b46da | -12.89947 | -46.07447 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 59675d50-3bb5-3310-8823-b6e98f3d2c5d | -14.94444 | -44.32136 | 2025-08-21 04:19:00 | NPP-375D | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c428df4-eabb-33c6-a223-6edb248e3563 | -14.84776 | -47.95071 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1f94e3d-4eb7-3a20-b932-c32ed944e863 | -13.02582 | -45.20959 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 67771c43-14b0-3f31-9af9-6a0acfd75450 | -13.03041 | -45.181 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4b3bf933-4ecc-34ae-bdb4-81d449cf4688 | -13.04624 | -46.82875 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c4589c-585b-37ec-8293-b523a0a276d4 | -12.95222 | -46.2408 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06820de4-fb1c-3d40-8a31-a1cecc7638e8 | -14.47036 | -48.36562 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3056ddb1-735c-31d3-91dd-025b3a964eb8 | -13.03604 | -45.16726 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a188ca36-4d72-30f2-b691-f9bbcef7f9db | -13.18447 | -46.90888 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 796a858f-ec9d-3a0b-8c3e-d048b86568a5 | -14.49467 | -45.95901 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b20d2a5b-c776-3e51-a322-2919b563aeb8 | -14.8571 | -47.93923 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 49cdf1db-fe3e-3390-a3f4-6d668f77687c | -13.7391 | -44.96165 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f02fecee-d3cf-395a-a8ea-d27e38e8e6a2 | -13.03698 | -45.20412 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ad3bcbd1-052f-38b4-a0d9-baa563ce11fc | -12.955 | -46.24526 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5bcd213-d6b0-3421-a297-60fbb90d279b | -13.03271 | -45.16669 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5b1f3af4-0630-33a6-be02-1b6472d97be5 | -15.63914 | -41.02451 | 2025-08-21 04:19:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3b1e14fc-fc69-3e7f-a3a7-3a074b7a3174 | -13.04972 | -46.8294 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1212491f-0f5d-3cff-b9ab-fc5168135a22 | -13.0123 | -45.1756 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 81ca6132-a7f7-3f71-adbd-4afaac0a60cc | -8.8551 | -62.4123 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f8593089-4e14-3841-a36c-3b3c1429b70b | -13.0312 | -45.1957 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| abb2e83e-4d75-383e-b671-34e7976c93b6 | -7.0169 | -44.5954 | 2025-08-21 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8552974d-0a6b-3f9d-88af-0e63ff899a31 | -8.8735 | -62.4305 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9123a9b1-7268-3958-8e68-c6df2dbb5063 | -7.0354 | -44.6167 | 2025-08-21 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| c742bdf8-bf64-375b-9d4a-92ac5d962a36 | -14.8538 | -47.9504 | 2025-08-21 04:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b67d21ed-942f-3aad-a6d0-0c9a2fa3bfe2 | -8.8739 | -62.3735 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6f6a524b-b043-3eb4-acb7-5a05b255735e | -8.8552 | -62.3933 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| af913f12-01b4-3765-98f9-e4f75ecc8f30 | -13.0128 | -45.1523 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| bc904aba-4d76-379a-a006-362c8b790a9b | -13.0317 | -45.1724 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 65be133b-4198-3ed6-ab7e-8c0ebf75e37d | -7.0166 | -44.6184 | 2025-08-21 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 337.0 |
| d0060289-ba53-301b-a6af-38c6bbb57950 | -14.8543 | -47.9279 | 2025-08-21 04:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 073093dc-1672-345c-b974-5032b7bd0f43 | -7.0352 | -44.6396 | 2025-08-21 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 98cc4e53-618c-3d81-9737-9f55d6ff4f16 | -13.051 | -45.1693 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 798c2dce-e92c-3363-9cc5-b2de11f8c3f6 | -13.0321 | -45.1492 | 2025-08-21 04:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| bad9731b-9d63-3aa8-80ba-02cd4960f9c2 | -8.8736 | -62.4115 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 4b0637ee-38e6-3fce-8916-67873abd9ced | -7.0164 | -44.6413 | 2025-08-21 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 0cc608a1-5529-3209-941c-e8aaae3b9516 | -8.8737 | -62.3925 | 2025-08-21 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 183.9 |
| d0cb63a2-607a-3543-8d80-84a02577797d | -29.77649 | -51.17699 | 2025-08-21 04:21:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 41a1f85c-6ddc-3346-b3b2-aa2a7ca92369 | -29.66466 | -50.20901 | 2025-08-21 04:21:00 | NPP-375D | MAQUINÉ | RIO GRANDE DO SUL | Brasil | 4311775 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db2b687f-5d37-3b89-9323-5cd7dc5a5923 | -7.0169 | -44.5954 | 2025-08-21 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| be6f0faf-83ef-3e21-b938-f0c3059d24c4 | -7.0352 | -44.6396 | 2025-08-21 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9678b9b4-aeba-3ce0-8e16-c19323740c45 | -7.0354 | -44.6167 | 2025-08-21 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 26e02882-ef24-3060-9add-d7617187b550 | -7.0166 | -44.6184 | 2025-08-21 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 320.5 |
| e46b2107-e24c-3e37-b0bc-9847f9e0e2d4 | -7.0164 | -44.6413 | 2025-08-21 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 61374cdb-9535-34c1-b771-005b16a14654 | -0.75027 | -47.75048 | 2025-08-21 04:36:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39af89e9-e021-3c9f-a17b-e9f4d7748908 | -0.74972 | -47.75393 | 2025-08-21 04:36:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16ab4a0b-dc9a-37d7-b3aa-88fd8ee67c84 | -0.91818 | -50.36381 | 2025-08-21 04:36:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9396ef44-27d5-3dc7-beea-e63c9bc7c5f0 | -9.72586 | -45.62319 | 2025-08-21 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7844b70-0f03-38a4-a92f-302960043051 | -6.96797 | -44.16466 | 2025-08-21 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02a0d8f7-b659-3136-8e21-557fc7d3a0c3 | -9.86805 | -44.69876 | 2025-08-21 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3a92825-8e8a-3831-8baa-187f7c2bacb6 | -7.03123 | -44.61473 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b0af57f-450b-375e-908a-2004d5909c96 | -3.03641 | -49.43134 | 2025-08-21 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af2d9908-829c-3679-b813-3a9a567a9b59 | -5.87813 | -50.15182 | 2025-08-21 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03c85d7c-c42b-3db0-b0d8-28b505c7feab | -2.95414 | -54.49746 | 2025-08-21 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4736735f-5625-39e9-af4c-38b29a081553 | -2.78949 | -49.59612 | 2025-08-21 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ad8baa5-a85a-3ad4-ad0b-182ddde85716 | -8.07019 | -43.67633 | 2025-08-21 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88c1d22d-11df-31f0-9aca-78f454adda47 | -5.96257 | -44.14337 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9ffb673-d19a-3ab3-8aaa-4d1be5791566 | -5.8889 | -46.5094 | 2025-08-21 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddb9c82c-fe0a-31db-8488-6e0ac4ebc08a | -6.98215 | -46.92685 | 2025-08-21 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9932f43-f50a-3314-91bd-db50bd30b355 | -5.96311 | -44.1398 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27449b11-4e9e-3e9e-9288-61ff09178213 | -7.99384 | -47.33725 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc80b22f-8244-3098-93d5-e9319a2340c4 | -4.28822 | -48.27729 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa10d97f-1e65-37a0-be9d-9852a572e964 | -9.52192 | -45.17199 | 2025-08-21 04:38:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92e47344-12d9-3fc7-8a5c-b23459e76c92 | -7.99676 | -47.34168 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 014c0352-0d6a-3bc3-a753-5401f4b6f10a | -6.43089 | -45.48526 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c1498053-d467-3df2-957a-fb4a02d30745 | -6.20367 | -43.57197 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
