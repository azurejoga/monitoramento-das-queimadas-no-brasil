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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9365624d-3c93-38a0-92ed-3721ebca2602 | -17.14145 | -53.89347 | 2025-09-13 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f651a212-573d-3c01-b499-3ac1b0f3a07d | -20.09749 | -46.91063 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37f7ebf0-2755-35d6-a617-63988c16039d | -17.31169 | -48.73038 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97e1be53-ea05-3640-8bdd-516dbbae7ad5 | -22.65826 | -53.10859 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 31f81e27-97d8-3439-ab2d-7b91031d51d6 | -19.07215 | -46.63865 | 2025-09-13 05:01:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3aa09384-a1ae-3629-a4f1-d2ab3be713ba | -17.31803 | -46.66478 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbb6c49c-e5a2-365e-bc7f-71749b13b623 | -16.53469 | -51.7486 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64a74c7-7c89-3ee8-8315-6052d24a985d | -17.41408 | -49.22977 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4795cbc-70b1-3aa9-8aae-fa7888d9aec9 | -16.51015 | -55.18684 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d0ed571-a6d2-3527-906e-fb2f58aa2e6c | -18.15832 | -49.18644 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| be11ea80-96d6-3280-b6db-14c6158d0d3c | -17.28311 | -46.096 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4de7c7f8-41aa-335e-8741-3831c1df6e20 | -21.93502 | -47.57349 | 2025-09-13 05:01:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a06a74cc-872e-34b4-8a8e-21ca1b8e2af8 | -17.34426 | -46.66921 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030e9257-2c24-3a13-98e4-9b7e212cb2c0 | -20.0826 | -46.90797 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0aaa4f6-1212-376e-83d2-4e2efdf9768b | -20.83545 | -56.86988 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f876e3e-5f95-3c73-b185-c54cab55adff | -15.99262 | -55.96045 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 054097b8-76d1-3a94-836f-cfaae0efcce7 | -16.49542 | -55.12296 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ec14fed0-f790-3b88-9d03-0be34322a0c3 | -16.36682 | -51.53518 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6dc25948-88bb-351e-b4f6-fce104aecf6b | -18.34841 | -47.02184 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75ab2326-6b04-3025-83b3-4f0aa3b0e171 | -17.83364 | -50.40993 | 2025-09-13 05:01:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1121f801-3891-38d4-9d8f-e2b4812d8ed1 | -18.14228 | -48.45442 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e71a6ab2-a820-32d6-8679-22e6c86ee3c6 | -20.10487 | -46.91625 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7acb093b-f71d-34f1-90ed-a7ccfcb48902 | -21.58483 | -48.42612 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f08eab94-f787-3de6-a510-f55b5223b985 | -16.50784 | -55.15588 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 36bcb78c-7ddc-3c0b-bf08-c0ba68e2a5de | -22.18033 | -49.6134 | 2025-09-13 05:01:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b0bb53e0-8c1d-3bcf-bc76-0157195bc229 | -18.89797 | -47.05986 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5718b2a-45e9-3b79-a28e-f045a122e9ff | -17.42419 | -49.22541 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97bc35df-c70b-348c-87d7-17296f655af4 | -17.30001 | -48.74554 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6b9bb2e1-b0b3-37cc-8c3c-79e15e3a3740 | -16.49448 | -51.99844 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3f91637-d1b6-3e84-a56d-13c83c32f49a | -20.37596 | -50.12448 | 2025-09-13 05:01:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9cc9a922-08b5-34fb-93e4-7f0080452589 | -17.30189 | -48.72937 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a7c75f7-a62e-3da5-8603-42bff76aca36 | -18.00418 | -46.94299 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe8c3740-39e8-3c8d-8fe4-b8ed3de8dd4e | -16.50665 | -55.11708 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d8a82151-a643-3380-ba78-eb2bd19a170c | -20.64703 | -48.68922 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8a8c8f8-533c-3c35-8339-8b4113df0418 | -16.8794 | -49.34358 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5587baa9-a6d5-30f8-835b-6b56f1f6ebf0 | -17.28102 | -46.11594 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e629b8b7-9a04-3b5f-aaad-d6cfdf16100b | -20.83933 | -56.86681 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50525c4b-dbac-3355-bc4f-79dd6e066637 | -23.10521 | -50.28882 | 2025-09-13 05:01:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 42861738-5a67-3573-824e-e322167a19de | -16.36196 | -51.50962 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7770669c-afa5-3791-a633-132b21293106 | -16.20988 | -55.96234 | 2025-09-13 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 1217b41f-4f55-3179-b110-6ce385264e83 | -16.33749 | -51.52834 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13f26621-63bf-3d5e-bda5-62dbdc353624 | -18.61121 | -48.20523 | 2025-09-13 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93885b58-f110-3125-8171-7ecc883db4ed | -18.97457 | -48.60368 | 2025-09-13 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee4a2cf4-fa07-3e24-a0d9-ccb764326224 | -21.00518 | -44.86201 | 2025-09-13 05:01:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41cc7753-fbfa-3134-833f-7b9288ff319f | -17.28952 | -46.09462 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35769ba3-d0ac-3303-b139-5d182de51ba3 | -17.28993 | -47.25473 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b087d227-d801-3a17-bbc1-33c4c3335753 | -19.98608 | -46.90618 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15894d9c-1dcf-336a-a940-94989238490d | -17.2892 | -46.09395 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf590e5f-6db6-37bc-9225-24ffa173e695 | -23.71047 | -51.69242 | 2025-09-13 05:01:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8eaa085-0926-3547-b226-e1fbd7f54d84 | -17.13994 | -48.50954 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f84c3446-73f6-3eca-9fd2-5955b47e1829 | -20.44638 | -46.45782 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cef6ab8-901a-3e0a-bcab-d69ff11a8d2f | -17.40575 | -48.21672 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce3e6cc1-35b9-32c6-b835-96849f512145 | -18.15298 | -49.19059 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 788539bd-5133-3109-8aad-11f3520bd562 | -19.66965 | -57.00568 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6133e04d-0eeb-3a71-af09-93be96f3598d | -16.52676 | -51.74748 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa72a980-984e-32b2-917b-dd1e467d9a3c | -21.93376 | -47.57298 | 2025-09-13 05:01:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81471864-8c8d-396a-9c2c-0af4767b79d5 | -16.69468 | -49.17413 | 2025-09-13 05:01:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f833d2-84c7-3771-b981-e77d5fed9f13 | -18.89751 | -47.05704 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e79534a7-d57e-332e-a9e9-fbcc866e648a | -20.37073 | -50.12901 | 2025-09-13 05:01:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b47c245-896f-30a3-880c-db1239f307e6 | -20.33922 | -46.66948 | 2025-09-13 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bbfe1e7-59eb-3420-b472-2c6234d5e5f1 | -20.10528 | -46.91191 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 56dd7f88-9089-3945-90a1-e670a6ba522c | -17.28528 | -47.24688 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0eacd1-018e-30a4-99bd-6619a1becb9c | -20.44709 | -46.44985 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a80e94-f2ea-3d61-8158-aee732398baa | -18.88765 | -47.0507 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f62b93d-c820-3f2e-b732-d2bf49bdc971 | -22.16047 | -47.37083 | 2025-09-13 05:01:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d057c9e6-9174-3268-bcf9-07f7084f9de4 | -17.41583 | -48.21841 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f47f9d2-0a2d-3b90-9dd3-26ca99d8d4c9 | -16.36234 | -51.53828 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc43004a-167a-3808-b7f1-932f12062c6b | -20.65149 | -48.69593 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4706277-e659-3958-aceb-8a2e114f59b1 | -17.29255 | -47.25659 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ab8bf4-ec73-3a17-968d-c458234597fb | -22.25954 | -49.57069 | 2025-09-13 05:01:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 057405d4-952c-3971-bce7-1c7b23424e9c | -16.4999 | -55.11599 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 39846234-be48-332b-a44e-e731777ff5aa | -23.25689 | -47.06308 | 2025-09-13 05:01:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6685e812-6baa-311c-be25-f16baba45501 | -23.22927 | -50.99742 | 2025-09-13 05:01:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4dff5f83-0d44-3004-bbc6-7625a934f1a4 | -20.44087 | -46.45291 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a04321f-53be-39ed-b698-918a74516104 | -16.33653 | -51.53541 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc773e0c-00f7-3f17-a9bb-686a932a3733 | -16.49712 | -55.13485 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 662ad6b2-4e2b-3274-aae7-183ecf52e538 | -19.14335 | -48.78498 | 2025-09-13 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b586df8-c1ea-3a8c-81c1-713310a9659d | -22.26205 | -49.56463 | 2025-09-13 05:01:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 284c8d78-8a7a-3691-9af6-8a1659ea856a | -18.0046 | -46.93887 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38efae3c-6cfe-36ba-ae21-860a775020fb | -17.54402 | -44.54547 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4d4545e8-3bd0-3d1c-a4b1-b815047faf3a | -18.07277 | -45.43064 | 2025-09-13 05:01:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efc47c5a-feb5-3efb-adab-8a183640cb4d | -16.52751 | -51.75082 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93590956-b2b3-3dff-9ca6-384976e7394e | -20.64639 | -48.69519 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8999416e-70d7-337d-a3ad-1b7a965d37d3 | -16.49335 | -55.12709 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 02fee2bf-f43b-3fa0-8456-91bd1472ccc5 | -16.53288 | -51.74099 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 609b23da-45d6-3e3a-9b5f-fb281832742b | -17.2772 | -47.24733 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c1a1482-a2b3-3ec2-93ab-7280c408eb36 | -22.25652 | -49.57003 | 2025-09-13 05:01:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c959d544-cd46-38f3-9ad6-56579259cd01 | -18.89232 | -47.05244 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0e3af4f-4c6a-339f-9e36-e86019cfa048 | -16.33559 | -51.54245 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| abd2ba84-99b6-3d0a-b30e-0dbd1c84caa8 | -20.55627 | -45.82745 | 2025-09-13 05:01:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e885a32-59c3-38da-8421-97e01e80b43f | -18.01024 | -46.93859 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26032cf5-f35e-3573-b67f-d0f782bd57fd | -16.79219 | -51.35518 | 2025-09-13 05:01:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95337cf8-3657-3bc0-a808-f433b1f5072d | -16.37084 | -51.53567 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa6d7c7c-a9a9-3105-a631-5660a2fad5b3 | -20.72981 | -56.73671 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddbe6a0-b35a-3495-af97-2154ba2c4d73 | -17.12655 | -48.4834 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d5a75b8-f1de-3ff7-8f63-12f9af0dbd5e | -16.52609 | -51.75269 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97a6ac30-037c-3a6e-affa-d6550a0b71e2 | -16.50947 | -55.12138 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 501f82be-ad19-3344-8c7e-67c622f00d21 | -19.98882 | -46.9034 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4810552-89cb-3b95-803c-efd1f34d2642 | -18.3326 | -50.97248 | 2025-09-13 05:01:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82e3f7bb-cfc1-38d9-a9ba-608006cef407 | -17.29067 | -47.24761 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README97.md)
