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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30375ce9-e35c-33e8-b8bd-bd8f06bdd60e | -6.30517 | -56.03975 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1497b026-e025-370f-8f1b-09d56a103729 | -6.7468 | -59.44346 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6ed452e-bd3f-3390-8689-ace71ed5f6bc | -5.85763 | -57.5541 | 2026-09-03 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79675dae-897e-3b85-83b5-88344bd404cd | -4.94231 | -47.65789 | 2026-09-03 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bece4a86-b692-31db-85cc-31107641d9e6 | -6.14953 | -55.66919 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37156d0d-1cc8-339d-8edc-fdbd3501ec1b | -6.33009 | -43.81843 | 2026-09-03 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22d5f85c-dfba-36a2-9ed0-b61655959b6e | -8.42842 | -54.69648 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 40ba88af-00de-35ff-b874-d0d5a343829a | -3.24345 | -47.25021 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| e3391e2e-baa1-3d23-b85e-a5a1e781578f | -4.97328 | -55.84943 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 870d7465-0223-33df-918a-79df8a4955a4 | -3.21689 | -48.81278 | 2026-09-03 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e2a2377-143d-318c-ad62-783c8dd75ef8 | -8.08758 | -50.97554 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 68f833e4-1b6f-359b-88ef-a3a964fbe506 | -9.41515 | -45.60963 | 2026-09-03 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c92be530-d91b-3429-b3c1-771d38d24eb2 | -5.25083 | -55.89951 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef02fc18-c9c2-3b6d-8d6e-1e6375b58f33 | -1.62214 | -55.1651 | 2026-09-03 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50c9d5fe-4e46-3797-beda-5c45601df5fd | -8.0807 | -50.96948 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| df82b2f9-62a3-3ae1-b776-85149db7aee4 | -7.48699 | -46.09145 | 2026-09-03 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40e32b1-2bbf-32e8-937b-28bf94c034f7 | -6.77476 | -56.41848 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010a3d0b-2d1c-31fb-a793-4f2840b29989 | -5.94643 | -52.15804 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07f56e69-7cf0-38df-958e-3cb1b8c10668 | -4.14924 | -51.07399 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a2109da-b048-35d1-b13f-a292ae3f5155 | -8.44017 | -54.74404 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91c4ade2-33a4-3264-b6a5-7de10b88fc50 | -3.96751 | -48.12773 | 2026-09-03 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e470d20-2b6a-3c3d-a34f-456c9ff181db | -4.02234 | -47.72609 | 2026-09-03 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f7223bf-3cf7-30f5-9a03-b4e2930005a5 | -4.97458 | -55.84202 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b91aa8d-d97c-3a5a-ad4e-99c365e02ee0 | -2.5562 | -44.14346 | 2026-09-03 04:38:00 | NPP-375D | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f24c707-a83f-3907-b8c5-8e3c0bcc9765 | -6.09191 | -44.90001 | 2026-09-03 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6642bb59-c0e1-3e0a-93d9-df8bff8a962a | -6.58663 | -44.7072 | 2026-09-03 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 851a585c-3fc1-3ea8-bdaf-77d640a1beb5 | -8.70255 | -52.36784 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1dd26d6-9dfe-30be-97e8-11e9d74c0d64 | -6.6825 | -43.4171 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0006393-4b8c-34c3-8ac8-db908efaccda | -1.46635 | -54.81759 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17577412-17f9-36c6-8be9-88c3df660dd4 | -8.07766 | -50.96409 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ca7678c3-af51-315b-bf00-a9fb53b73ca7 | -7.92832 | -44.22566 | 2026-09-03 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d32937-c55d-345b-b566-921f51f93c6d | -3.24627 | -47.25439 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1055b501-2523-389e-aa5e-c37f8296d617 | -4.11982 | -51.03203 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f237ec5-c4b1-3770-b1a2-4db3086e507a | -3.4434 | -56.32418 | 2026-09-03 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c9e1f14-1a89-31cd-baba-cd8427fa00eb | -6.30816 | -56.04665 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 99ca443e-5321-3309-9200-065ae6298d0e | -9.12622 | -40.64493 | 2026-09-03 04:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f14beca6-a5a5-35d8-b1a9-f4cd80c2bfaf | -3.33809 | -42.80172 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bd0f5de-ddc3-33ee-874a-b55820f0c33a | -4.11574 | -51.03131 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81c6795b-f386-36f7-a9dd-529f542374f1 | -8.7199 | -52.36648 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f13d1d37-218f-3996-a25c-63d78f859f37 | -7.04312 | -59.22376 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a6a3559-1843-3bb5-895b-73beb2109a21 | -6.31435 | -43.61405 | 2026-09-03 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f496c874-4f29-363c-bcf5-d9ba4ce69b43 | -3.23946 | -47.25332 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| cf823e99-7201-3699-9abc-fb4623058b2d | -4.17755 | -42.4361 | 2026-09-03 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a90a4e30-dcf1-3f37-a602-2be4a0b4d699 | -5.79237 | -51.7187 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fecd965-8a87-3e33-9e1a-c32734f6d38f | -5.55674 | -60.23177 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12faf4d8-72b2-3c64-929f-5e95d99cbd9f | -6.14494 | -55.66778 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4bcdcdf-e3b5-3f9d-b842-4536c8513956 | -6.6208 | -55.2375 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea5c684-6580-3a7b-b46c-7e4ab1e6789e | -6.65122 | -39.11781 | 2026-09-03 04:38:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99cb7476-4f2b-3513-b108-936fd69e37f6 | -6.76267 | -59.43388 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 395f610c-a9df-3682-b9c5-5c527ceb91a2 | -8.43427 | -54.69193 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b64a2980-e17f-3e64-aa53-5b87fc4a3930 | -8.08837 | -50.97082 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 259a0f15-32a4-3386-b116-d681919ec1bf | -6.31789 | -56.0561 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 40120171-c88d-36b0-8fe5-756259cc6ad6 | -6.62488 | -55.24497 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd4c1199-fcb1-3078-b09f-b81e0d973d85 | -3.67597 | -53.75399 | 2026-09-03 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97339672-d0bc-3b34-be9b-226c146b2e51 | -2.82831 | -48.65337 | 2026-09-03 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c8f122b-8d7e-323b-9c0e-1edd96e193e2 | -6.41983 | -56.18251 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ba803ae-44e5-3460-8e1a-b45c29d88ca7 | -8.43921 | -54.74946 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ccdb485-b01b-3d0a-907f-72f885b21940 | -7.294 | -49.80838 | 2026-09-03 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42edf34-d4a2-3abe-887a-5766a1c9f4b1 | -8.43135 | -54.73676 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d23e813d-3161-3754-a60f-000aeb38e70d | -3.33746 | -42.80575 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 332350cb-8a89-3b21-bd29-1cf9b4ba00a6 | -8.79228 | -47.98507 | 2026-09-03 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 982dab0d-6949-3602-9c0b-1ecc093472ee | -5.80134 | -43.6489 | 2026-09-03 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8461a78-7d23-3c8b-9603-90264621c395 | -8.08678 | -50.98027 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 694d6c5f-19bf-370d-974c-eb27c1e29a9f | -8.70391 | -52.36 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 109663aa-91be-36e2-932b-faaf1d372b9c | -6.76945 | -59.43509 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e35bdec7-d34d-3468-9104-cf5b3c41e2e9 | -3.03776 | -48.41415 | 2026-09-03 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d598aef3-3ffd-33df-a29f-a2588e3bdb02 | -8.46489 | -44.69147 | 2026-09-03 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af7b6af1-33b0-3667-b04f-e0b9a9a83072 | -6.94057 | -45.19856 | 2026-09-03 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39adcac0-3f93-38e5-8355-b5c4a7998e5c | -7.322 | -55.13707 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2330b9dd-1a76-3b94-8181-52b47e1b961d | -9.08721 | -47.81753 | 2026-09-03 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 005ec22a-1b76-350f-a20d-2613d58ed447 | -6.65608 | -46.13377 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906acd37-2835-3c86-b764-371a60cf6448 | -8.44306 | -54.69917 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d188fc28-8504-34c0-9317-6e846ef37a77 | -6.14417 | -55.66788 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 099e77f8-1573-370e-970c-bc515cd7650b | -6.94739 | -46.95756 | 2026-09-03 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79c0aca7-7aaf-312a-87e9-1f54739b857e | -1.02646 | -53.72283 | 2026-09-03 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927e9f4d-074c-3a9f-aeaa-646fc5df7066 | -4.08931 | -51.03872 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d98293-d214-30a3-b835-f67180ba20e3 | -5.46105 | -60.05955 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 050526e7-7c7a-3f5d-a293-15f3304565d7 | -4.11223 | -51.02703 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6323172-092e-346a-9ab3-20aae6fce320 | -6.77314 | -56.41265 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dbf2fc8-3fb4-3c94-827b-19931feb8d60 | -5.20576 | -38.0343 | 2026-09-03 04:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19cf17b4-ae54-3cad-a343-a3097b37f5ca | -3.64716 | -49.96863 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec59117f-d098-3d0a-995a-7ab334e6874e | -2.9368 | -41.73277 | 2026-09-03 04:38:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cce10e9a-d91a-3d69-bdcf-24c294665c32 | -6.94675 | -45.20318 | 2026-09-03 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e1b2db1-b964-3db8-9dd7-fdf47d360170 | -6.75228 | -59.44459 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 954fbfae-b61b-360d-b07d-e9baccf0f755 | -5.24766 | -55.90226 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05a4148e-15bc-3a9c-a506-fe785439295e | -4.50102 | -42.55946 | 2026-09-03 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cce987ec-cda3-3080-aa1f-89821d420d1f | -5.23359 | -49.59934 | 2026-09-03 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f452f0-979a-3e8a-a3c3-df52ae51663a | -8.07989 | -50.97422 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9ef404d-b6b2-3926-adcd-74750c5ca2fd | -8.46431 | -44.69526 | 2026-09-03 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bae947a-9d59-393b-89ce-48fa11012b64 | -3.49072 | -50.58392 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dab7a17-c0d5-3acf-a428-71efd25f8e29 | -8.43623 | -54.7377 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd86faf2-ba45-38ee-b56d-0771acdfb8e0 | -6.6404 | -59.44187 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 58339086-7b7a-3625-a3e9-34bd05a6fbd8 | -8.45462 | -54.66227 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ac0791-0afa-3537-aaf8-e15ce3ad4b85 | -3.96242 | -40.05275 | 2026-09-03 04:38:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6790211f-dd46-3d82-b711-d8e0fcfa15d7 | -6.65886 | -46.13777 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65531c41-99e3-322c-ae1d-1a89bedc27f7 | -8.45365 | -54.66775 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f5fad1d-e0c5-3d0f-9a62-e96ebd515cc2 | -2.48154 | -49.40939 | 2026-09-03 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d534b2a-012e-33c5-96e4-78072586696d | -6.94957 | -45.20727 | 2026-09-03 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe8c94f-542d-32a2-ab4b-685b553db765 | -4.96706 | -55.85203 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b673c25-c930-3b08-81ac-ab75088c34e7 | -6.63289 | -55.22993 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README26.md)
