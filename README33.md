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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06fa7014-faa8-310b-b2a8-25dd7d4f8bc3 | -6.59914 | -43.68389 | 2024-10-27 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b251f523-20d6-3a4e-8acb-e1f9433afd85 | -7.42184 | -44.72583 | 2024-10-27 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 817c50f6-1929-3500-80cc-d1346c79dff9 | -7.4179 | -44.72515 | 2024-10-27 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d290e4c7-9787-3994-947e-23c5b86d4b65 | -7.41397 | -44.72446 | 2024-10-27 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b15c3ab0-b611-365f-8ca3-c5a722433bfc | -6.87906 | -44.7594 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 042cbe93-1bcc-3021-a91a-c8106fe03f4e | -6.82025 | -44.46722 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66ce8f37-a11d-3f8d-9507-34276c088b07 | -6.81941 | -44.47224 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1cbc37c6-311c-3445-bff5-277bea393b96 | -6.8155 | -44.47154 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8d7a6a2-5ec1-3935-b092-706625e55a1e | -6.81159 | -44.47085 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fd096ab-4f8d-30d4-b83c-904327bbf7b8 | -6.81075 | -44.47586 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05245e51-b8c4-391c-bd5f-c19555a9195c | -6.72444 | -44.68338 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e9646a3-882a-3abe-8c32-a5a2bc7f7093 | -6.72359 | -44.68853 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f67ba2c4-d494-3084-be43-1fa14f8d047b | -6.72046 | -44.68272 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0384a095-26f2-31d3-9ab5-ad879f43fdf9 | -6.71961 | -44.68786 | 2024-10-27 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77d20732-4012-3c37-8e17-6c5af0270e96 | -6.58988 | -44.69605 | 2024-10-27 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b49ee55c-86f6-38cf-b805-ea2eb31247dc | -8.44728 | -45.08375 | 2024-10-27 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29188bb7-8871-3953-a2c1-8ea279d7feb6 | -7.87695 | -45.37592 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf24fae-b8a7-3ca3-9ae1-4be99a7dfb81 | -7.87286 | -45.37528 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc9f4a07-0fdb-335c-9281-2b4430f102fe | -7.86877 | -45.37461 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 965b1126-27a0-314d-b539-8bad421d76ef | -7.86383 | -45.4036 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ace74124-967f-33f8-8b90-732175c28742 | -7.86321 | -45.40725 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b9f9985-6bfa-3f5a-ae47-212fa71369f4 | -7.86258 | -45.41093 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90e79fd1-eb0a-33e4-8b2e-1cb02fd01d25 | -7.85849 | -45.41021 | 2024-10-27 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52aae7c1-854c-3194-9252-6348a445b2a0 | -8.78979 | -44.71946 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b11def0-7a2b-30ed-8c28-0b05feb56d74 | -8.78899 | -44.72432 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5895429f-03d9-321d-abcb-b1369a389487 | -8.78512 | -44.72365 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75d29377-af84-373d-b5f9-ce53b543a506 | -8.78431 | -44.72852 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c54aae8-fe51-399c-acd3-d0b20d5ed3da | -8.7835 | -44.7334 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bc3c7f8-6040-3495-914b-1143c46f0504 | -8.77517 | -44.71189 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d45baf0-f22f-3fde-a3a7-2447c8cdb3bc | -8.77435 | -44.71675 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76b04091-ae3d-3960-b7c4-a73953d57c69 | -8.77354 | -44.72161 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a577ca8d-467c-3270-887b-d9c755c151bc | -8.77273 | -44.72647 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a7c1cc-a54b-3393-959a-8b870c44b064 | -8.76968 | -44.72094 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df9d69ac-26c8-3f1e-b45d-ea9602566fa9 | -8.76886 | -44.7258 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dcaaf3d-0470-3ebc-8730-58b5d1c53101 | -8.7644 | -44.70501 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bab53f6-f8f6-355c-8ba1-8512a813a126 | -8.76359 | -44.70987 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 757b56bc-876e-36be-8da2-3632171aef75 | -8.76277 | -44.71474 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2deb80f3-9dad-396e-b5c9-d5363278b4fb | -8.76195 | -44.71961 | 2024-10-27 04:00:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8af6ff5-da5f-3b9c-aaa5-230c3f844ff8 | -8.54235 | -44.95384 | 2024-10-27 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa30cbc7-d966-365c-9802-9c767cd385ee | -8.54183 | -44.9502 | 2024-10-27 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c40e9c2-e048-3698-bab8-8f46fef1312f | -8.08564 | -43.93012 | 2024-10-27 04:00:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c55b494-0b42-37b6-a060-68a8c61761ee | -3.60112 | -44.79099 | 2024-10-27 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f96aedf8-efb1-317a-856a-6e8cc9c16132 | -3.60097 | -44.7908 | 2024-10-27 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15bbf8c7-49ad-36e7-8691-f1bfa81d1204 | -3.46564 | -45.66803 | 2024-10-27 04:00:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbf80d4a-b9e7-3e6c-bc50-df25162c158d | -3.45736 | -45.40929 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6600f902-e6db-340b-be9b-90d31627cddc | -3.45667 | -45.41354 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 326ec3d7-f237-3a26-a5cc-c830c8268803 | -3.45597 | -45.41779 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb02f8b6-ea66-3237-9f86-7423483689ad | -3.45528 | -45.42205 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 806b540b-fbc0-375b-b04b-64ea8d672fc4 | -3.45228 | -45.41281 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4e4148b-c6a9-3c05-9c75-823487de4262 | -3.45158 | -45.41706 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c32273f-6b34-3f40-9893-274e73c1f592 | -3.45089 | -45.4213 | 2024-10-27 04:00:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7e20d81-565a-3528-847b-eda4e7711fec | -3.40453 | -44.48528 | 2024-10-27 04:00:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51a334fd-e65e-3db1-aa59-625233c5aaa2 | -3.40043 | -44.98787 | 2024-10-27 04:00:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 579f0fab-085e-3668-9f6d-2d3a99d58d6a | -3.39708 | -44.71895 | 2024-10-27 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f67f44-82eb-34f3-8a33-b4bbeacc612f | -3.18357 | -45.79603 | 2024-10-27 04:00:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5cd2b17-af17-36bc-aec2-c1a7c44e22ee | -3.13086 | -45.31696 | 2024-10-27 04:00:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ffba89a-8b94-39d6-bd1e-706562500539 | -3.12648 | -45.31623 | 2024-10-27 04:00:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aaaef740-2f54-3e12-b0ba-717bd5d78cc9 | -3.08063 | -45.65175 | 2024-10-27 04:00:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f08ec03-3254-3c6c-9308-78616f69dd81 | -3.01056 | -45.12246 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87b339eb-018a-327d-82fb-ce20f390488b | -3.00987 | -45.12659 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad1d5e32-ee22-34f5-a389-8fd54639bad4 | -3.00914 | -45.12364 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d748de93-1e17-3616-a5eb-b7b58a98d2d7 | -3.00622 | -45.12177 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bc868ec-1b23-3814-90f9-027bc2f37914 | -3.00553 | -45.1259 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a72f815d-72c8-3beb-9052-6f867c9dcc15 | -3.0048 | -45.12294 | 2024-10-27 04:00:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cf18089-f1cc-340b-9567-be4b595eb8be | -2.8686 | -44.9973 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af4524a1-ce8d-3a2d-829e-376bcc5956c8 | -2.86794 | -45.00135 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0bc4a6c-8f3c-340c-b085-5bdcdfa55d63 | -2.86429 | -44.99663 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf7451c-881e-3c75-a3d9-4295e02f2c16 | -2.86363 | -45.00066 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff076be8-92df-31f8-9fb2-94e66eb6b564 | -2.86297 | -45.00472 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17bac13d-eae1-315b-8113-afb09f70cb81 | -2.85932 | -44.99997 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e20e0feb-48f7-34ea-a25d-7ebd0722ecf9 | -2.85866 | -45.00402 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c67580ea-681a-3bb5-aabb-f935e7898c06 | -2.85567 | -44.99522 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52ecf223-cbb0-328c-8637-0c8b4b28470e | -2.85501 | -44.99927 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e865e68f-684d-3c40-9e0c-b6dc18b494a6 | -2.85435 | -45.00333 | 2024-10-27 04:00:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c4a80d-250c-3659-854e-e2fca38f773f | -2.72185 | -45.15258 | 2024-10-27 04:00:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce448e00-15b7-36b3-a6ac-8f9e3e4400df | -5.0274 | -45.53691 | 2024-10-27 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25dff377-a155-3178-a451-ee7cc364f8be | -4.92762 | -45.86064 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001b6d2d-216e-39d9-a61d-a53326a463d2 | -4.90872 | -45.70979 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0b423bf-ad8a-321e-a234-b05679788921 | -4.8261 | -45.71938 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 715e806a-50e5-3945-b151-b86aad2a106b | -4.76905 | -45.92717 | 2024-10-27 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ddc0e65-10bf-30c9-ba72-8b828288139f | -4.71079 | -45.79392 | 2024-10-27 04:00:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbf9d9c1-ee1a-329f-bb1a-7cd7b7a4b0af | -4.42671 | -45.95896 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d98932-602e-363d-847f-e700bd962f90 | -4.42598 | -45.96336 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccbef677-eefe-352d-a843-bfc01118a802 | -4.42524 | -45.96777 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18e1ea48-7fc6-3de1-8ef4-ef781f6476e2 | -4.42452 | -45.97213 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edeaf4f2-f700-3f78-bd95-ba5458295031 | -4.42152 | -45.9624 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95ca4638-4359-3a6d-9e51-3bd21089bbe3 | -4.42079 | -45.96681 | 2024-10-27 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d116be40-dd1f-340a-8863-a75c6b1220e6 | -3.74111 | -45.88448 | 2024-10-27 04:00:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b833aa7-ce5c-313e-8513-f0a5f8aa5f9c | -3.73945 | -45.88651 | 2024-10-27 04:00:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 787d0de2-4ef2-36e6-b475-b214b20f4ea6 | -3.72476 | -46.03648 | 2024-10-27 04:00:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed7b2624-e270-397f-bab6-425ecd86551d | -3.67546 | -45.88058 | 2024-10-27 04:00:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18882c35-4761-3637-ace0-a3e89db1ff9e | -3.67471 | -45.88514 | 2024-10-27 04:00:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae3a7fd3-b262-36b9-956b-dcc7b78d146f | -3.62179 | -45.92099 | 2024-10-27 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a15a93e8-b24b-32d7-b60c-fb8efcc11ea3 | -4.25781 | -44.65252 | 2024-10-27 04:00:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42a450fd-9b17-3b36-b7fb-cd1fb386e2ab | -3.90277 | -45.02902 | 2024-10-27 04:00:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69d39d5b-fa85-335b-960d-2dfbb9f1be51 | -3.90212 | -45.03295 | 2024-10-27 04:00:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e78cc292-6660-313f-81b9-3b346dd33bae | -3.89853 | -45.02829 | 2024-10-27 04:00:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3bba8ae7-d6ff-3574-b612-fbd4c1d29060 | -3.78754 | -44.96668 | 2024-10-27 04:00:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 878850f3-d0d4-3dfd-bbe1-003436cc1221 | -6.33284 | -46.33293 | 2024-10-27 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed3a6b21-935b-3797-bb82-7651eb17ba34 | -6.18397 | -45.44254 | 2024-10-27 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README34.md)
