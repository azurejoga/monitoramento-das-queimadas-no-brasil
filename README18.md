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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b59a3935-445d-307f-a251-fbd41694e068 | -5.61913 | -45.00122 | 2024-12-17 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b846cba-11cf-3ea0-a35c-b6c256701888 | -17.26406 | -51.05724 | 2024-12-17 04:23:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed49dd02-3811-32af-8ddc-bebf54fab5a5 | -17.33396 | -51.19528 | 2024-12-17 04:23:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dc7e2f8-293b-3c93-9a5d-4f5af4496a78 | -6.21647 | -46.21577 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e389e9f5-c8fe-39ea-a4de-5b7944177e7d | -6.01663 | -43.55742 | 2024-12-17 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bb159f3-4755-36aa-984b-6f1faf549af0 | -5.9185 | -43.84275 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87060642-bbc5-3009-93f6-330c72ffeb40 | -6.86526 | -44.77421 | 2024-12-17 04:23:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61c55af9-0978-3c80-89e2-522ff78e43b5 | -10.45875 | -36.95562 | 2024-12-17 04:23:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 285a662e-435f-3a79-b759-da2226e52f9c | -6.95826 | -42.82813 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a509ceb-cca6-31a9-be22-bba11476c9c8 | -10.6615 | -44.48996 | 2024-12-17 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49ca8083-f9c5-3064-87cb-ae7485f0799f | -8.36924 | -44.4821 | 2024-12-17 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b3a4da-9055-3f8d-8c6d-a4d94114cbd7 | -6.2059 | -46.22536 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69998681-f039-3768-ad20-87f5e5bb9907 | -9.2778 | -35.91443 | 2024-12-17 04:23:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12d99440-9510-3138-a225-b34efc7ea99b | -5.62463 | -44.83614 | 2024-12-17 04:23:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ad6155f-6a65-31e2-afec-04043a8dfa42 | -6.9646 | -42.83298 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 819b9bdf-f3e1-38a0-869b-408fe0b4e733 | -6.96862 | -42.82973 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4241feae-ad09-3929-86f4-ba3ecbdbd59d | -7.86208 | -43.08979 | 2024-12-17 04:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5712f8f-b888-354f-b2b7-3a958e1f293d | -6.2087 | -46.22947 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8443a979-39c4-3efd-9ded-db9e91b65955 | -15.09454 | -59.64819 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6e4ac46-3f94-3294-9372-6edf9678f77c | -6.86196 | -44.7737 | 2024-12-17 04:23:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6604f013-b0cf-3328-b389-589871a3569e | -6.49786 | -46.91122 | 2024-12-17 04:23:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c960996c-5f80-34d7-a58f-5af498ea1468 | -6.9313 | -43.51299 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3b5fe9a5-6a0c-3a22-b4aa-273853fd4095 | -10.48859 | -36.84896 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f30d1ca3-b810-369d-843a-f7b19f57717b | -5.93964 | -43.79181 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc9d3046-e690-309d-8b07-9ac4594cbf60 | -12.4144 | -43.80038 | 2024-12-17 04:23:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed080822-c72b-3665-b955-885256c01d92 | -6.63841 | -47.34912 | 2024-12-17 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a3796796-dcb4-3705-8dbe-1209c0ce507b | -5.94341 | -43.76715 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeab5ebd-f73d-3039-9111-4bcbe7833389 | -15.08169 | -59.64516 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ec01c07-55b5-36d4-878e-e90d67ae66cf | -5.94297 | -43.79232 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76f7c2c2-b219-3c55-a857-64b7d4417e35 | -7.90552 | -35.23993 | 2024-12-17 04:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 5c0da83a-15f3-3607-9559-460eb1857a40 | -5.68159 | -46.50252 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e10ddb94-f0d1-3abd-a281-4513dcaa6f0b | -5.94071 | -43.78478 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c4a1f8-b3b7-32a3-8409-9735e05396f4 | -10.18562 | -36.28793 | 2024-12-17 04:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| df1890c1-b1c2-3b94-99a8-abc48cb02db4 | -6.95603 | -42.82478 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a09fa1a-d028-340d-9d1b-4f84393b6e93 | -6.94912 | -42.82375 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aafe6714-a0c4-3c7d-841f-44c85a3df764 | -5.91472 | -42.89255 | 2024-12-17 04:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f54c372e-b9eb-39f7-96a1-8a0d9f64b493 | -6.92566 | -43.50473 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23eda03f-fd98-3d29-814b-0bb8a016ea5a | -6.92515 | -43.53054 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e912227-2928-37d4-9b7c-3775a486229f | -5.31803 | -46.49414 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5198b88c-e074-34ac-a9a7-4ca06b234b55 | -5.70241 | -46.79072 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 895e9a0e-9bb8-377f-b18c-c2136fe8008c | -5.58124 | -46.14503 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3aace4ac-06f0-3083-a3df-8f8bbe1dd0bc | -6.95481 | -42.8276 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 734cad52-1c97-3e0d-a4f1-756c595471be | -5.99063 | -43.48035 | 2024-12-17 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c60aa97a-c8a5-36d3-b8f6-9ed9d0faab8e | -7.00833 | -42.8007 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e4f56c21-67b8-34e1-9b04-ffb616579d04 | -6.97496 | -42.83457 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2e2fd3e3-eca9-3b1f-9e81-dd27fd000ff7 | -6.91896 | -43.5259 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf624317-c946-33e2-ae80-0412c1883335 | -6.2104 | -46.2187 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ab790439-1f6f-3255-9fd2-eaa22987e112 | -19.07047 | -52.85366 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2246360a-09db-3685-b61f-6e63673ed767 | -19.06654 | -52.85284 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53e4193e-9466-3847-996b-d11b6e87bbcc | -25.19025 | -49.327 | 2024-12-17 04:25:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9ab16ba-6017-387e-ac8a-48f54af656a6 | -18.90086 | -56.04571 | 2024-12-17 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0c565764-fc58-3e5d-ba23-754f51bec358 | -22.08685 | -48.94739 | 2024-12-17 04:25:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f355c2df-292e-3050-98be-63c93bd8a682 | -18.89604 | -56.04464 | 2024-12-17 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b3967373-a8a0-3d30-8cb5-b28b0ed5e4ab | -19.0695 | -52.85891 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd6958e9-559d-359b-b620-264395e84e70 | -19.06163 | -52.85727 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1cab8238-26fc-35a1-b2d3-e03b836a4a82 | -19.09312 | -52.86366 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 75a84211-b01f-3434-93a9-574b34d5cd06 | -19.09706 | -52.86446 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1c0cbe25-8ae6-3949-8d5a-0a7649cd6143 | -18.89972 | -56.0513 | 2024-12-17 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| fc392e2f-e3a2-3245-9af0-be374a1857a0 | -23.40569 | -46.55763 | 2024-12-17 04:25:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f3f04fa1-1eab-362b-85c3-b864e27f1f26 | -19.08918 | -52.86287 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8f65931a-3708-3556-827e-2a30713816e5 | -21.32957 | -56.11486 | 2024-12-17 04:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29a6165f-41d7-3bc2-a535-b119c81138c2 | -23.59391 | -47.43841 | 2024-12-17 04:25:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 61a5676e-f078-3519-b162-acbbb09f47b8 | -19.09409 | -52.85839 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5dbbd180-9f85-3054-a78f-61528827e15d | -22.6754 | -42.85427 | 2024-12-17 04:25:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53699bb2-0901-3b3a-b4be-9ecaf4191913 | -23.34012 | -46.77202 | 2024-12-17 04:25:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4159145b-395b-3449-82da-1eef60fe31fd | -21.23053 | -49.27976 | 2024-12-17 04:25:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17bcad19-651e-393f-bf3a-1172468e6ac0 | -14.25095 | -41.75211 | 2024-12-17 04:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 587b4718-eae0-34c3-8d4b-b515459a9b47 | -23.11801 | -48.21675 | 2024-12-17 04:25:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bc59b856-a80b-380e-b43d-05dd8aafb995 | -19.05771 | -52.85641 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98d816e6-3d9d-3668-8295-0d142f7ccc7f | -13.52398 | -52.27854 | 2024-12-17 04:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f091c6f2-0e4b-3cfe-87e8-69ac72bed2aa | -22.53984 | -48.81392 | 2024-12-17 04:25:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0764393-d639-3d17-a81b-172dd92c1399 | -13.61942 | -45.58946 | 2024-12-17 04:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0ac8a8f-e500-3f09-b245-6d33a1e4abcf | -20.76527 | -46.76907 | 2024-12-17 04:25:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9d22150b-53a7-3a2e-b9b4-af2aab34f520 | -20.56788 | -55.09002 | 2024-12-17 04:25:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59bc79af-75f0-371b-beed-f0cee602654d | -19.1657 | -54.83511 | 2024-12-17 04:25:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52bddc41-7618-318b-b40f-7088c417f70a | -13.62051 | -45.58227 | 2024-12-17 04:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 229b622c-8f3e-361b-8ebf-109560359276 | -20.91826 | -56.54979 | 2024-12-17 04:25:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f94dc08d-823a-3c85-bd1d-b16045799a80 | -23.85364 | -50.00631 | 2024-12-17 04:25:00 | NOAA-21 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 947ffab2-13e1-3637-8aab-2501c9a74c63 | -19.09015 | -52.8576 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| baed760f-30f7-317c-889d-a3eb7f6128af | -18.8949 | -56.05024 | 2024-12-17 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| c9c7ca7d-c5f3-35f0-92a9-c557a3704e0b | -23.52137 | -46.97295 | 2024-12-17 04:25:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ed76f846-ff64-3121-b354-eb1b8c32a9a5 | -14.24861 | -41.75086 | 2024-12-17 04:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6df51c0b-4c6a-32e8-aa17-5769a065d058 | -19.06556 | -52.8581 | 2024-12-17 04:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f129852d-dae4-357f-94c1-9ca3ec5064a2 | -23.89314 | -47.89766 | 2024-12-17 04:25:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dafeb283-1b5a-3dce-acc3-f7218ebfe5ad | -30.15256 | -52.02466 | 2024-12-17 04:27:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 288444cc-2ed6-3e50-9f74-ce1e888b7851 | -27.00346 | -48.89027 | 2024-12-17 04:27:00 | NOAA-21 | GASPAR | SANTA CATARINA | Brasil | 4205902 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b32de185-e76d-3055-8e25-b28f84c94c01 | -28.58683 | -49.44379 | 2024-12-17 04:27:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b44e931d-0130-356d-90ab-5e1785894ee7 | -5.0936 | -43.9176 | 2024-12-17 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b8715ea3-0e38-36e5-90ac-f3884f70943c | -5.0938 | -43.8945 | 2024-12-17 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 22ceefad-50af-3c04-848a-1b5e7413f9e1 | -6.9349 | -43.4934 | 2024-12-17 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| be11cdfc-4914-393f-ae60-c0227a48ead6 | -3.2968 | -53.3749 | 2024-12-17 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 662308da-d5fb-3cb0-ad77-2ceeaabb0942 | -6.9346 | -43.5168 | 2024-12-17 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5a8a2eaa-3c66-3bf7-a516-66e1b650bedc | -6.36885 | -35.22777 | 2024-12-17 04:31:00 | AQUA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 98f3a27d-c3dc-300f-865b-0452de7f42ce | -6.36726 | -35.2382 | 2024-12-17 04:31:00 | AQUA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 253.8 |
| a063f576-f801-3fb4-8910-162fee0a6e41 | -5.50295 | -36.83123 | 2024-12-17 04:31:00 | AQUA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 31a7c353-ca5d-33c6-b356-f7de4c65958f | -7.81644 | -35.2351 | 2024-12-17 04:31:00 | AQUA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 41faf9d5-b6c3-3e6c-9a23-26c0ee4c33cb | -7.818 | -35.225 | 2024-12-17 04:31:00 | AQUA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 5bc9757a-e5fa-3d38-a7e3-a5e81270319d | -6.36567 | -35.24858 | 2024-12-17 04:31:00 | AQUA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| bde996e5-60c9-36e5-814e-e2b2dd9029d3 | -5.51375 | -36.8329 | 2024-12-17 04:31:00 | AQUA_M-M | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 11.2 |
| e961c905-6513-3d84-b984-c9c7334301da | -10.4807 | -36.83401 | 2024-12-17 04:33:00 | AQUA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |


[Clique aqui para ver as próximas entradas](README19.md)
