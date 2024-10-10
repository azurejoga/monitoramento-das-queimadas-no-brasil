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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97ecc815-affe-3bc7-9cdc-e16b0da4c390 | -12.01383 | -51.0249 | 2024-10-10 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25c58430-e691-38d8-a1a6-11bd061cfd82 | -11.99461 | -51.91859 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a502993-4477-30a9-b17d-29708b18417b | -11.99406 | -51.92211 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e31638e-c23f-3db7-8795-462ab1259473 | -11.99351 | -51.92563 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1e4d1b3-2e4f-370b-8ed6-4e1363855a73 | -11.9913 | -51.91806 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93be6e3e-6979-354e-98a2-8dbfc2d4b2d0 | -11.99075 | -51.92158 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f090a7-0906-3c63-b11d-cf69bfb6076c | -11.9902 | -51.9251 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a96f7568-e4dd-375d-b13c-8c47957ade10 | -11.98744 | -51.92105 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 953a7e00-1188-3f33-af01-5ccb74caa62e | -11.98689 | -51.92457 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37cf8055-b361-3b8a-bc86-045b73fd5263 | -11.98413 | -51.92052 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 490cbfaa-a6ba-3229-9856-7663adb92835 | -11.98358 | -51.92403 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99521ef2-370d-3859-8f84-ef15942db6ba | -11.98027 | -51.9235 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6ab2302-9d05-3fe7-988e-d528b77d6558 | -11.97696 | -51.92298 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebeda488-667e-3f14-9e57-7f61fa224ed1 | -11.97365 | -51.92245 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb2c30a6-0d90-3195-a83f-0e897172764b | -11.97034 | -51.92192 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd9766e9-e7d0-3e9d-9761-f6d96bcb6fb4 | -11.9582 | -51.91275 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 661769ea-fdd7-3fd9-a0e1-b98c42c31d40 | -12.68412 | -52.61107 | 2024-10-10 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dfb4b57-cf97-3a86-b167-195a8b361087 | -13.19122 | -51.71026 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d42e14b-7c95-3b39-a885-434526c37b4c | -13.18789 | -51.70972 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08330cbc-aade-3661-84a3-bbec2b0ba35d | -13.18347 | -51.71635 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc5ec1fb-ca80-3cc9-a0d9-4643ad23bad2 | -13.18068 | -51.71226 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd98ecdb-0f07-3de0-8daf-01fa803674e8 | -13.18014 | -51.71582 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a42d8e-123a-3328-a2eb-7b32fd40412a | -13.17787 | -51.68614 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e01fe169-fe16-30cb-987a-128e0d9b13b5 | -13.17735 | -51.71173 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 718d205f-4dbd-3c51-a82f-1a511db05e20 | -13.17681 | -51.7153 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 858d1f7a-40e8-3c43-9a2b-81edbd280832 | -13.17454 | -51.68563 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc253c3d-f60d-3d03-83f7-6c16e8bcc9d2 | -13.17403 | -51.71119 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d042ada-1adc-3754-b052-8833f7c308ab | -13.17399 | -51.68921 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5422b6c7-f5ce-30a7-83f9-e68671c9f137 | -13.17348 | -51.71476 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a1219bd-3413-3a84-b1ca-710fd2a77e02 | -13.17344 | -51.69278 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 943f0002-1848-3a17-8c33-604c86565430 | -13.17234 | -51.69992 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db6c6a16-1471-3d41-b3b0-e4019eadcb18 | -13.1712 | -51.68511 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21bf3392-f56e-3172-8276-90fed29ab4f0 | -13.17066 | -51.68869 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e5f7fa3-9dec-34d1-bd65-f301a2f854ed | -13.17015 | -51.71423 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db9a37e8-3b6a-36f3-8261-220e21f5c090 | -13.17011 | -51.69226 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24ef200a-8222-3b32-b14b-5c407fe617fc | -13.16956 | -51.69583 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86af35b0-311d-3d69-a92e-97e788018550 | -13.16901 | -51.6994 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15973806-43a0-3582-864b-4276b4c5ba2a | -13.16787 | -51.68458 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4279d9a-b053-3344-a1d7-34be3b5ab25f | -13.16682 | -51.7137 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38eccc8-d81a-35cc-ab77-c9d384640fa6 | -13.14227 | -51.6767 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfefea83-6b7c-36e9-bf9f-323fb3068abc | -13.13616 | -51.67205 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc8d1e70-b8ee-326c-beef-69a031209e29 | -13.13561 | -51.67562 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc2d4d7e-5c29-3e2a-bef6-6dbf346d7f41 | -13.13284 | -51.67152 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38562f23-b422-3664-9ceb-624bfebc2b55 | -13.13228 | -51.67509 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b00c091a-29c6-3699-9f2a-af2d73033d50 | -13.12618 | -51.67044 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be5d743-0c67-3c6f-9936-c2ef5325ac77 | -13.12506 | -51.65558 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 987f7085-a27a-3988-898b-a8abc09714c9 | -13.1245 | -51.65917 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e4049c7-4228-3bdf-b4bc-d42d70b9d896 | -13.12395 | -51.66276 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1186f96d-7e38-30b1-8bd7-185e5c4db7c8 | -13.1234 | -51.66633 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afda80b2-188e-3200-b505-5df7fd88d261 | -13.12118 | -51.65863 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c416e55-4169-3cba-a57d-65a92366bb98 | -13.12062 | -51.66222 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b3a08d2-035f-3f65-85ff-f58cc0f324cc | -12.73272 | -51.99766 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38659f78-1b23-3a0b-b4fa-bdd996f047b3 | -12.73217 | -52.00119 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49400b14-c324-334e-9612-d2eaf13da4b2 | -12.7294 | -51.99713 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4464743-1fe9-37b0-8b9a-8330b8b07da0 | -12.72886 | -52.00066 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbbe167d-bf08-3630-8a1d-f9e8e9fd7133 | -12.72554 | -52.00013 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b12b946-ff20-30c1-958d-324bf0ac102e | -12.72223 | -51.99959 | 2024-10-10 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a848841-829f-3a93-b088-f6527d973844 | -12.51601 | -51.70881 | 2024-10-10 04:46:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e28e9abe-34ac-3da0-a19c-6fe1ed694e3e | -13.94857 | -52.82144 | 2024-10-10 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2dd8768-d797-3831-b255-84b72e89b8c3 | -13.94801 | -52.82498 | 2024-10-10 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 442f7ab9-96f6-346c-b368-4426d027278e | -16.99024 | -52.88896 | 2024-10-10 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eefcc30e-5cd3-3723-91eb-5908b331d678 | -16.98969 | -52.89258 | 2024-10-10 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ec5943-4a27-3ec9-b224-8d223110c1fc | -16.98555 | -52.8996 | 2024-10-10 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8923661-4711-3ed0-8886-cfc7948ae304 | -11.52344 | -53.86668 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d36679f-dc75-36f6-b990-eb8b24b44d50 | -11.53205 | -53.85667 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7618dd0d-d34d-33a3-b6ed-174bd1f80ca4 | -11.53145 | -53.86037 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6782cc06-b1f5-3352-bec8-ede5e9c5e28d | -11.52805 | -53.85981 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38c39ab7-b49a-344d-b103-c8eebd7d4b81 | -11.52745 | -53.86352 | 2024-10-10 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706b23b0-0cde-3344-a64e-7419eb3d2154 | -12.04952 | -53.52103 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2a77700-780c-361a-bc69-c5c3022304ae | -12.04893 | -53.52466 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1466f938-a704-3c03-8279-74be975fc921 | -11.84962 | -52.5179 | 2024-10-10 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ff7a683-f289-3022-b8c8-945c995ffa7f | -12.74642 | -54.00387 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79ea500b-e368-31d9-b3ef-d5ddfd31333e | -12.72083 | -54.07557 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b67975-737c-321e-80bc-d017601bc931 | -12.71014 | -54.11964 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0840a24-ea96-385f-b3e0-8d6e7ead6db4 | -12.70675 | -54.11905 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83041809-a2fe-3432-9760-7f42c78f9724 | -12.70615 | -54.12278 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b4a77ec-d3ca-39e8-a577-ae66f96dd176 | -12.70337 | -54.11847 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9316cf2c-cb67-3e2a-9583-b35cdb8e0803 | -12.70276 | -54.1222 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d83b7437-7fe3-3039-8f79-190fb2813f22 | -12.69998 | -54.11789 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73bf8bb6-6a65-3a4b-acb2-90cc601210a8 | -12.69937 | -54.12162 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9df9cde-2bb4-3dd1-a89e-a8d13fa76454 | -12.69659 | -54.11731 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99091366-952a-375a-aedc-8a2bb763df51 | -12.69598 | -54.12104 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd11767-b075-3926-9da7-f167b2525ffa | -12.6932 | -54.11674 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bacb705d-232f-34a3-8418-1f62f26cc31e | -12.69103 | -54.10872 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a565c13f-699a-3133-9421-33b245ec6e29 | -12.69042 | -54.11244 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93aea18a-b760-35fc-a775-0c75e22a44ea | -12.68981 | -54.11617 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f2fca8e-06aa-3c90-8026-94624f957f71 | -12.68777 | -54.00156 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b222212e-d6cd-3d28-ab94-869c8e1e57bb | -12.66401 | -54.01313 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9395904b-362c-3d7b-a0e2-38c3c01a4c4b | -12.66062 | -54.01255 | 2024-10-10 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24de8ebe-b4c0-3b8e-8f59-13e666bd168d | -12.6354 | -53.10998 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85ed6e64-ded7-3d41-be9c-5a069359b873 | -12.63483 | -53.11352 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61af4175-4c7e-359f-a367-7782dddce04f | -12.63426 | -53.11707 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76996dd3-51a6-32b9-b4d6-eee558ca2439 | -12.63151 | -53.11298 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec6b975e-339d-33fc-a745-b421457e2c35 | -12.63095 | -53.11652 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7bab8bf-3d60-3853-93a3-33f1db1e2199 | -12.63067 | -53.50196 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acfaeed-8ed9-3b9e-bf86-1de8255269c5 | -12.63038 | -53.12008 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4d8ccaf-437a-3f5c-8566-87f12268285e | -12.6281 | -53.13427 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b65a118c-9d58-38d8-a16f-85c8260a0929 | -12.62706 | -53.11953 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0616884c-78b0-3be1-bee8-0ef9f2ba865e | -12.62307 | -53.14437 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b66ab8-853d-3549-8239-41d6b4c2e7f4 | -12.6225 | -53.14793 | 2024-10-10 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README121.md)
