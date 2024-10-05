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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cd69467-1308-399e-ad05-8aa955af3dd6 | -18.76309 | -44.69382 | 2024-10-05 04:40:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eef4df80-3f4e-34c9-8d94-8d5a24821c18 | -19.81216 | -43.83962 | 2024-10-05 04:40:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 900a054e-4084-3d85-86fa-6c79eaed319a | -19.81182 | -43.84286 | 2024-10-05 04:40:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fe2bbfb-6467-3123-8365-29a41e264edc | -19.80683 | -43.84184 | 2024-10-05 04:40:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0da8522c-315c-338f-9eee-c3d279008908 | -20.51133 | -44.90044 | 2024-10-05 04:40:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 574cf424-3e37-3940-b0b5-76c0690c0a19 | -21.04156 | -44.80481 | 2024-10-05 04:40:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 077d1c85-d454-322d-828e-82f686f57880 | -14.86448 | -45.13968 | 2024-10-05 04:40:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f0d0f0c-e9ab-36ab-af49-1d247cdd4cfd | -14.48389 | -44.96346 | 2024-10-05 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c57d145-b4fc-38d8-b7a9-951a86243289 | -14.47956 | -44.96283 | 2024-10-05 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b16974d6-f01a-3183-b123-5d08f58ec0c2 | -14.47522 | -44.96219 | 2024-10-05 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efefba7c-4304-386a-b156-b2c11d723cde | -14.32548 | -44.70251 | 2024-10-05 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c03f4ee8-1b74-3c4c-a2ee-c99b1a41dccf | -14.3249 | -44.70689 | 2024-10-05 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a998a0-5724-3059-b39e-f3f1bc396dc3 | -15.85924 | -45.2674 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7df38cd-daad-3e85-906d-ef374ecfa9c1 | -15.85868 | -45.27173 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2225cbd2-d2eb-3178-954c-4331521297e2 | -15.72594 | -44.8339 | 2024-10-05 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f088502d-71f6-3a51-9a0d-3dd289f15ce1 | -18.10364 | -45.60026 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efadf21c-c63d-3fac-93e0-c7f965cc62fd | -18.10279 | -45.60159 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe994b82-4d90-3328-8b75-f9a3d333c737 | -18.10223 | -45.60597 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5e44c60-69e1-3d3d-8547-67d633f309aa | -18.09977 | -45.59543 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f780254-7795-3429-90b1-7b67ecdce581 | -18.09896 | -45.59679 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eac86f36-4553-398c-a635-5a8b842476ec | -18.09872 | -45.60419 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb581a82-662d-334d-94b9-0ef133eed6b2 | -18.09785 | -45.60553 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20890349-3e41-3bfe-8d32-1f4c4b9a6b99 | -18.09538 | -45.59494 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb2156b-2fcd-3efd-a78f-aaf7edb81fd9 | -18.09457 | -45.5963 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4616b41-2f45-371e-a0b2-63295307b780 | -18.091 | -45.59437 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c23eb156-455b-3953-b92d-0b29b3dd20ad | -18.09019 | -45.59572 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 229ffec1-8441-3755-b302-d98a83baa740 | -18.08943 | -45.60755 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f899ca51-fd8a-38eb-b4fc-5d40257f91b3 | -18.08853 | -45.60888 | 2024-10-05 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd0a24a3-8bc1-3d2e-99c6-7761ff651d7d | -19.29603 | -46.21648 | 2024-10-05 04:40:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7d25825-f973-3f2c-9b51-e68f486d3bf7 | -19.29551 | -46.22063 | 2024-10-05 04:40:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f74273dc-df9c-3c62-8bfb-33a4ecf94628 | -19.2928 | -46.20761 | 2024-10-05 04:40:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 390248ac-7d43-350a-ad0e-07ccb3ba9f2d | -19.29227 | -46.21183 | 2024-10-05 04:40:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99a1d33f-949b-370e-a561-754dd9fea1c4 | -19.06576 | -46.33878 | 2024-10-05 04:40:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5f94aa-8abb-372b-82bf-8f83b8344afc | -20.79919 | -45.42976 | 2024-10-05 04:40:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c53c5f0-d9e4-3ae7-b4e7-60ff84647c36 | -20.79871 | -45.43143 | 2024-10-05 04:40:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4252749e-4086-37c9-88d0-34c697bc3f7c | -20.07766 | -45.78689 | 2024-10-05 04:40:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e3e447b-52d3-3d29-8ee5-9fd6157688cc | -20.07374 | -45.78191 | 2024-10-05 04:40:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b13fcdcf-0a52-3021-bad0-21a255afc15e | -20.07321 | -45.78638 | 2024-10-05 04:40:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7926de0-8eec-3285-bd14-b8e18cb8ec6e | -20.07266 | -45.79096 | 2024-10-05 04:40:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a362094-8055-3c76-8a52-34a18eddbfee | -19.80399 | -46.44878 | 2024-10-05 04:40:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 412625d1-c660-34f3-91e9-0223a59d21fb | -19.61703 | -46.26133 | 2024-10-05 04:40:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e20f7da9-55f3-3abc-89fa-cc0e67bfe6ed | -19.60801 | -46.26398 | 2024-10-05 04:40:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5b7837b-004d-31d0-a0e7-81924f108f93 | -21.53785 | -45.43467 | 2024-10-05 04:40:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4e9d57fe-38c7-30ba-8f15-99e30a0cf836 | -21.53726 | -45.43979 | 2024-10-05 04:40:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 343abb33-565f-3940-866e-99791a704890 | -21.53653 | -45.43692 | 2024-10-05 04:40:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e47ae636-f931-3736-bcce-6a535febe566 | -21.44681 | -46.55665 | 2024-10-05 04:40:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 878f1225-98a4-31c8-a616-c8c1a6f5931e | -16.42275 | -49.92031 | 2024-10-05 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7991c658-1508-3405-a020-0bbcd5c94313 | -15.18122 | -45.48534 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 251d40bf-03ac-3593-8c9a-b11f212d13a6 | -15.177 | -45.48464 | 2024-10-05 04:40:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc23c71-8222-3252-887b-f320954360af | -14.20596 | -46.46946 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e11e913-776d-3919-a7c7-63a0d1b6e4de | -14.20343 | -46.45893 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8687f94b-ddb1-3ad3-bb0a-5dcd93d300ff | -14.20273 | -46.46394 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1d517bb-fe76-3082-b33f-e4dec1a9cc7d | -14.20132 | -46.47403 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c228fe1-7072-346d-bc7f-2840814ba4b2 | -14.20061 | -46.47916 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01dcbf1b-d17b-30f9-8fe9-dee4401476f1 | -14.19989 | -46.48426 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 212f970f-c97f-3b92-8e09-7f70096ce330 | -14.19878 | -46.46358 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a07b3a6e-e81b-3454-84f7-96da310a65d5 | -17.62931 | -46.98625 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77af5995-20dd-335d-9b28-c7d59b686b27 | -17.62601 | -46.98051 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1db65f7a-5740-3fb8-96f2-9e85c9f2e21b | -17.624 | -46.99598 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 62e88a87-ac1d-3d74-8b4e-1f062fd7c4fd | -17.62333 | -47.00115 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da38f335-3e18-3a35-94d3-f365d2c84b8e | -17.61947 | -46.96844 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 893d13e6-7b38-3f99-8bba-396f1ae5bcd6 | -17.61273 | -46.98927 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4207b8e9-b794-3f76-9701-ff10d617c816 | -17.60876 | -46.98863 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3da9c45-c381-3eb6-af29-2f1e6109e985 | -17.60811 | -46.99371 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 82242467-a818-3d9b-8efa-5cf0665e628d | -17.60656 | -46.98761 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e97bec6c-6c61-3ce5-8ad9-c6841967677e | -17.60619 | -46.96037 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f42a9608-49bf-325f-8c4a-8c9449a4edab | -17.60587 | -46.99271 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ffaa1d6-4a6a-39ca-b1fb-287ef8f161f6 | -17.6048 | -46.98797 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8cb52bd9-3b2f-3e32-b074-359702c486d7 | -17.60002 | -46.97605 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39d707ed-f923-304f-acb7-f1d4748f1980 | -17.57646 | -46.94002 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8085769e-e506-33c3-b71a-8985bcf5f898 | -17.57576 | -46.94524 | 2024-10-05 04:40:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9d7a30f-1cea-335d-90bb-cff13e6e3549 | -16.94958 | -47.11978 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f1da735e-4640-3a7c-8942-07d833ccc8ea | -16.94891 | -47.12482 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d14b52d6-af47-3e65-ae6c-087ca4f1b9b5 | -16.94567 | -47.11924 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 11fb9e05-4631-334b-a282-a2f8bffa903a | -16.94183 | -47.11695 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6d82c1b-c810-3caa-9bfa-af6cedb84fdb | -16.94176 | -47.11868 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0448853c-a356-3141-ae9a-5d0578de08c8 | -16.94114 | -47.12196 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| df3f9093-7c14-353f-9324-a61bc00acdb6 | -16.9411 | -47.12374 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bf1ad684-ca92-3ff8-a591-bc07a3c0c041 | -16.94044 | -47.12709 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 624e3266-f20f-375b-a536-3cc15aad8ec3 | -16.93719 | -47.1232 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6adb0046-9f02-3712-b98e-cb87de234eca | -16.93622 | -47.15768 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a202643d-7982-3a82-b500-110b847f249f | -16.93251 | -47.15898 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c2aebf4-585e-3add-8f90-c2c710bdf428 | -16.93231 | -47.15719 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 163110ce-3d0b-3f12-a024-7b34ae6371c4 | -16.9286 | -47.15847 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e60e1ebf-b256-3404-8fe4-be89254092f8 | -16.92492 | -47.18206 | 2024-10-05 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a72e836e-e1a9-396c-85e5-41657667f9e8 | -16.92146 | -47.15233 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03350f6e-fd78-349f-9942-520fcf467e20 | -16.92138 | -47.18338 | 2024-10-05 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b484ff5-9e61-33a3-a639-7b1d34b9312d | -16.9213 | -47.15055 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d68f43c-9cc3-3924-a184-5b3b7c2e7b95 | -16.92104 | -47.18148 | 2024-10-05 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1c52f3a-01c7-3409-8099-ffac8e9c2f21 | -16.91672 | -47.15499 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a018307-8c08-395a-a2a7-db3f8b6c160f | -18.03023 | -46.44207 | 2024-10-05 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65518ef7-a955-3a72-8d30-6af3259f0f3a | -18.02974 | -46.44596 | 2024-10-05 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0632609-b5e5-3093-abd5-8ff19e3712f8 | -18.02563 | -46.44518 | 2024-10-05 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c669115b-9230-351f-b9eb-a3a5b968cf1a | -17.41349 | -46.31853 | 2024-10-05 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134249f1-cd13-3738-9a88-1c63ff1142a4 | -17.21017 | -46.38897 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4c69b02-c8b0-3848-9c69-980f31da69fb | -17.20606 | -46.38842 | 2024-10-05 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca24aca4-a749-3017-898f-9dbf601cafb6 | -19.14948 | -46.6252 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19962629-2bd2-3bbc-96c4-0a7bcc7f3ab3 | -19.14898 | -46.62905 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c99a1097-4ae4-3f5e-a144-bd9214874db1 | -19.14849 | -46.63284 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16228201-0383-3268-b1a3-87b5f6eb9ffc | -19.14801 | -46.63659 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README115.md)
