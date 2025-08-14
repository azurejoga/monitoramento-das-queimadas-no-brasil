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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43bfae8a-e676-342f-bc34-fbcd1a5c5466 | -20.09206 | -47.44465 | 2025-08-14 04:23:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c86ad15-d599-305d-bb7a-bd13d10076a5 | -18.61955 | -44.26625 | 2025-08-14 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8e0f55f-339c-363d-af71-6087cc91ccaf | -21.01046 | -51.6563 | 2025-08-14 04:23:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 016ed27e-7de2-3032-ba99-775ec73690ea | -16.28867 | -52.9163 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 23c7edce-3693-3ee2-a356-37086bf9eba8 | -18.53716 | -46.05233 | 2025-08-14 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 494891d1-f9cc-3429-8f81-275d00431dfb | -16.31351 | -52.92925 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85322855-4a1d-3a49-9d11-a934e0203d48 | -16.38603 | -50.90668 | 2025-08-14 04:23:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1ee317a-f352-31eb-bc73-1a43737b3e6e | -18.53659 | -46.05614 | 2025-08-14 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 469ff993-97c0-3180-b7ab-47677f65d78d | -21.36252 | -45.04227 | 2025-08-14 04:23:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eff79631-2b95-3856-84f0-020533448dcb | -20.24833 | -42.30642 | 2025-08-14 04:23:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9cbb0aa5-6a88-34be-9798-8607b6b16c8d | -21.1449 | -48.65402 | 2025-08-14 04:23:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6762ca26-01de-30fb-b5f1-96e8c5d414a7 | -16.30185 | -52.91471 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53d8c146-837d-373d-86b4-b44afee68313 | -16.29772 | -52.91381 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e25d034-9b1c-3e91-8dc4-53208cb2f363 | -19.25836 | -44.17212 | 2025-08-14 04:23:00 | NOAA-21 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e2c526f-e310-355c-8814-46da4f47cf53 | -21.70808 | -44.37103 | 2025-08-14 04:23:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 06f1c45a-c485-3cc1-82a5-f5c149024991 | -16.3094 | -52.92051 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 326043a2-bc22-3e41-86f1-1cf8a1d5aaa7 | -21.39515 | -43.65302 | 2025-08-14 04:23:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97a674e7-ec27-36e7-a1da-fa006e220ba8 | -22.27705 | -48.5045 | 2025-08-14 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cbfe3fdd-b600-32f8-ac4d-576790867ac3 | -16.3159 | -52.91659 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b0f4be4-930e-3928-a35e-e75f8035a41a | -17.61321 | -46.70621 | 2025-08-14 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18be649b-c6c8-3af6-bd55-b95818cd7484 | -20.47914 | -53.67566 | 2025-08-14 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69876d20-1c77-3f0c-b4e0-3a1e33a6a627 | -21.01404 | -48.92025 | 2025-08-14 04:23:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 366f6500-4d96-3036-a727-ea9114038070 | -20.08874 | -47.44406 | 2025-08-14 04:23:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 505b74c6-c26d-3e15-8c65-f36c9245da60 | -16.31433 | -52.91701 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48f4cc9d-5564-314c-bd15-4cb37bb45af9 | -18.06326 | -46.01631 | 2025-08-14 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ca8b2a-311b-357f-8ea6-3ac196bb3aa0 | -19.61113 | -45.98698 | 2025-08-14 04:23:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dba3f5f8-7034-386c-b085-c569a83946bf | -18.54675 | -46.05777 | 2025-08-14 04:23:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 72ba5b52-0d0a-3511-a7f4-2e01274c6f3b | -16.54275 | -47.85839 | 2025-08-14 04:23:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a95e608f-10b4-3b2e-b3db-5ef23c3518de | -16.31204 | -52.92968 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d023946d-cab8-3633-9d39-4eadfdf72b8f | -16.79303 | -49.14209 | 2025-08-14 04:23:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5330993-b276-3a18-a834-c6bd510414db | -20.8831 | -43.06725 | 2025-08-14 04:23:00 | NOAA-21 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e406aeb0-362d-334f-bc47-bae3c542465e | -22.38001 | -45.45829 | 2025-08-14 04:23:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6fc091ac-9d46-3e20-84c9-7a69e3d3fa0a | -22.60391 | -43.62024 | 2025-08-14 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b74ee958-a21c-31f7-a8c3-775540944330 | -16.3143 | -52.92506 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 587b5f36-9196-3934-8835-9699a0868a31 | -16.31174 | -52.91584 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4b62d7c-dcb6-3e14-b1c3-b9be8b92136b | -21.01972 | -48.90605 | 2025-08-14 04:23:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4e013d4-5ddb-3aa6-b67c-c2b2270c5c1b | -20.46459 | -47.40908 | 2025-08-14 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa7f5253-3feb-3cfc-9f23-c1b3931d8fb7 | -20.07194 | -45.37392 | 2025-08-14 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b2ff8ad-39c6-3379-b91c-945d13ebe3bf | -20.09262 | -47.44094 | 2025-08-14 04:23:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1589055-3d8e-3896-a4a6-b3401ccfb3e6 | -19.95861 | -45.30351 | 2025-08-14 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6fde4ab-97b4-3895-b3e1-c5a45f179d51 | -21.65038 | -46.39939 | 2025-08-14 04:23:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0ae98a71-01d2-350c-a938-43fac530d07f | -18.24812 | -47.26256 | 2025-08-14 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a47c252-ab27-3456-85ba-422a76747439 | -16.31094 | -52.92006 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fbe0a77-d5f7-3e37-aa38-2f29a0d1e940 | -20.61975 | -55.48734 | 2025-08-14 04:23:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c55a80e-8630-3236-947c-3e9e2fe6c198 | -16.80931 | -49.25554 | 2025-08-14 04:23:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96dd483e-8294-3309-a640-8c8db50d091a | -21.31903 | -48.56347 | 2025-08-14 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e91d859-abd0-33c6-80c3-1da75ac96a49 | -16.52082 | -49.02373 | 2025-08-14 04:23:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbd4cb03-06a1-34f7-a826-ca9dabc67e5a | -18.24868 | -47.25893 | 2025-08-14 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64a6946b-97ca-3e94-9489-51020cad44af | -18.53377 | -46.05178 | 2025-08-14 04:23:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9642e984-b3a7-313e-9a00-b2823c441e18 | -17.8693 | -52.19692 | 2025-08-14 04:23:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e1b135a2-d150-3cbd-a573-bb4c12bd967c | -21.22631 | -42.56823 | 2025-08-14 04:23:00 | NOAA-21 | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf81e50c-6221-34c2-99d4-489a07105bf6 | -22.48683 | -44.10191 | 2025-08-14 04:23:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf1b4791-9ffe-3799-adb4-ae094f62a47e | -18.9282 | -46.7907 | 2025-08-14 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 645972e6-6c9e-3728-b925-540977059c15 | -21.14176 | -46.62503 | 2025-08-14 04:23:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a3dd9dd1-a63c-3bce-a734-641005bb9a4b | -22.60068 | -46.72366 | 2025-08-14 04:23:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 03e13b18-f3d9-302e-b975-8399fb787194 | -16.31849 | -52.91774 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b35ff92-982f-3a81-80df-5c8f6e82e3f0 | -20.34857 | -45.99117 | 2025-08-14 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7037c896-cd54-3767-985c-20f626c99caf | -16.32006 | -52.91732 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed9734d0-4dfd-309b-ba89-ec1fae9bd2c5 | -16.31695 | -52.92631 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e67dc066-4835-304a-b76b-5caa4463daa3 | -16.30523 | -52.91977 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50eaebfa-6451-3f40-aee6-1c3dd9b91e66 | -19.25529 | -44.16697 | 2025-08-14 04:23:00 | NOAA-21 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a6d5781-3bf3-3450-9fb1-1c7547261faf | -16.30935 | -52.92848 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f882b669-1df4-33e6-bc0f-d654019fb1c5 | -16.31279 | -52.9255 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6749030f-f5a9-3997-837e-4f0ef93933ec | -18.24537 | -47.25837 | 2025-08-14 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 082da91c-3755-3c48-847b-e09a1b06f67b | -17.01503 | -44.4448 | 2025-08-14 04:23:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70e80382-f9de-349b-9620-758d06c0320c | -18.61652 | -44.26123 | 2025-08-14 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af1d6c20-5231-303b-a5fc-ed5f0c38a6ec | -16.31511 | -52.92078 | 2025-08-14 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27f0b724-28b0-39aa-915a-2deb56ff451c | -16.74503 | -48.50786 | 2025-08-14 04:23:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 351fc1bf-b780-3a1a-84e3-5ec70fb56bbf | -21.7074 | -44.3693 | 2025-08-14 04:23:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cab04ec-7205-3531-8458-f50a25e2c957 | -16.26168 | -49.96591 | 2025-08-14 04:23:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37f2bc60-0683-3c38-af4e-90c99de6fcda | -22.60011 | -46.72764 | 2025-08-14 04:23:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c72a3938-b4b6-3048-b2ee-4604bc1bebbc | -16.59728 | -47.03844 | 2025-08-14 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49f0d576-a8b8-3e45-8374-20ba9bc9a218 | -21.31845 | -48.56716 | 2025-08-14 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d43bfe22-c384-3335-a7b7-b57aa407beb6 | -19.78287 | -46.3663 | 2025-08-14 04:23:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1bb2675-d720-33c4-87e1-a944ec8edce5 | -21.31564 | -48.56341 | 2025-08-14 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b8a1da8-c61d-3655-9ecf-60ba28a9a815 | -17.04769 | -51.79278 | 2025-08-14 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 72526e0c-1edc-33f9-9e22-86fc62e52e1c | -19.25897 | -44.16754 | 2025-08-14 04:23:00 | NOAA-21 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74afc0dc-1276-3e23-a8d9-7eb36c7379bd | -22.78157 | -50.19703 | 2025-08-14 04:25:00 | NOAA-21 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b1579f72-f194-3e2f-a818-ae76cda930ed | -22.55754 | -49.77174 | 2025-08-14 04:25:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d25e457d-661c-340e-8c40-8d3fb8f48ca3 | -22.67189 | -47.45317 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 335069ed-4059-3f80-84df-79fdb3bb5e24 | -22.62558 | -47.39412 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0553134b-3eda-338d-a766-04a3bd3640d1 | -26.10437 | -50.17728 | 2025-08-14 04:25:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f087d2c-f21c-39f8-ba1c-05dda8bbbfe3 | -22.93475 | -47.16808 | 2025-08-14 04:25:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7e50187-d8e1-3f46-8ad7-a6d1d0d31341 | -23.35049 | -47.8147 | 2025-08-14 04:25:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c4cee50b-c28e-3fb4-9618-fa759132ac28 | -22.62615 | -47.39028 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d0f2693a-5175-3bbd-a2e3-27fd2e216d11 | -26.04632 | -53.69628 | 2025-08-14 04:25:00 | NOAA-21 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe4497e3-a16e-380b-9309-1092d56f7b99 | -22.5542 | -49.77112 | 2025-08-14 04:25:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7f3de64a-276a-3438-98fe-ee38a5070615 | -26.09243 | -49.45626 | 2025-08-14 04:25:00 | NOAA-21 | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 639932ec-2c21-330f-9e06-bfc9ae60abf9 | -23.79214 | -48.88151 | 2025-08-14 04:25:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff1fc151-ef23-31af-b3d2-cd573dfcfdeb | -23.02708 | -50.37494 | 2025-08-14 04:25:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b7faafb-ba6d-32a4-a2ba-cd4d0c15043e | -23.18926 | -46.59368 | 2025-08-14 04:25:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d796e23a-3918-3df5-8be6-ffc0d5aa8da3 | -23.48408 | -47.38952 | 2025-08-14 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9fb98265-d6ad-3c1f-a920-cfc6d5de56eb | -22.85705 | -49.22516 | 2025-08-14 04:25:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8cda2463-3028-3d2b-89e9-b30c65eaa6fa | -23.1812 | -46.60076 | 2025-08-14 04:25:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5c97ed37-eaa5-3576-a2f7-85a75f28a309 | -24.48079 | -50.64608 | 2025-08-14 04:25:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e6e4e1c0-39fe-3cd9-96e4-21809ad13fd0 | -22.7294 | -47.26145 | 2025-08-14 04:25:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e96aa653-64b6-36a9-b1ac-7b4550ce9ecb | -22.67467 | -47.45758 | 2025-08-14 04:25:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 25.6 |
| acf22867-6cf3-3216-847d-ab041f5201eb | -25.29458 | -49.8577 | 2025-08-14 04:25:00 | NOAA-21 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0fa0a852-47bd-32bd-8197-c05a159bf2c6 | -23.18984 | -46.58952 | 2025-08-14 04:25:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 02bb1030-2c61-339d-9f09-777abef0a2cf | -23.48746 | -47.3901 | 2025-08-14 04:25:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
