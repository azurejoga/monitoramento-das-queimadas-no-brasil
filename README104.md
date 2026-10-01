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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11168baa-d05e-3429-8da0-2dd6ab448717 | -14.377 | -44.7534 | 2026-10-01 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 570.4 |
| 28e05832-9e5a-3d7e-9031-76b1de4a8b82 | -14.3574 | -44.7569 | 2026-10-01 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 417.6 |
| 4b4d3741-1dcb-3388-ac5c-c3e2d0f7cc52 | -8.0675 | -44.8158 | 2026-10-01 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cdab1b24-9efd-3b96-ab12-d1f020303e60 | -11.2095 | -45.1478 | 2026-10-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| a50d5fef-5ae7-34b1-b6d2-5d9e48db0314 | -10.7112 | -45.3075 | 2026-10-01 14:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 91a5c64e-d2a2-3eb0-987b-83804d8f2ca5 | -11.3935 | -43.3705 | 2026-10-01 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 78fa545a-3895-3553-8c4e-22b3aa1c7880 | -7.5126 | -47.3358 | 2026-10-01 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 7ea69b35-456c-3df7-871f-8d452bb22c76 | -7.3287 | -55.2356 | 2026-10-01 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 34740a7b-8d04-3341-9648-2684b672d932 | 1.7115 | -55.9221 | 2026-10-01 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| be5c0554-46a1-3bf4-8dfe-516c9440d715 | -10.7302 | -45.305 | 2026-10-01 14:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b74722f3-d217-3c03-9872-f450b0ebb8f3 | 1.8587 | -55.5648 | 2026-10-01 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 73c75d9e-259d-31b7-a2cb-245dec267da5 | -6.3666 | -55.1261 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| dd545735-c85f-3e0f-a818-1dfc95a5bd3d | -5.9887 | -53.5538 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9e9c81a7-a513-31fe-b7ca-a06257ed6d79 | -6.7002 | -55.0493 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ffb54bc7-2fbd-3d95-b234-84d04c473ad8 | -11.3739 | -43.3972 | 2026-10-01 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 07085068-448f-3b6f-992c-4a0a4b424623 | -11.2278 | -45.1913 | 2026-10-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 327ad4d2-9256-3a3a-83ec-221505e94263 | -8.7069 | -49.5336 | 2026-10-01 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| eff54502-663d-38b1-bcc7-efd1200d92e1 | -8.0166 | -42.8681 | 2026-10-01 14:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 18aacdc4-e82f-3523-bf36-134b0d9861de | -5.9152 | -53.4762 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 0bd5b9e0-6344-387d-bff1-b46fc484f3a5 | -7.7221 | -54.7913 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 61381c4e-7af9-31c3-80ae-11e737cc42ce | -11.2438 | -44.2626 | 2026-10-01 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 326.6 |
| 047a7f25-6d12-3305-9b2b-8fdb6878f643 | -12.3163 | -46.4056 | 2026-10-01 14:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7631112e-458d-302d-b794-ca47e0d16221 | -15.243 | -46.1534 | 2026-10-01 14:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| e9575fcb-5336-365b-95cc-358232149880 | -5.8412 | -53.4799 | 2026-10-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 4c368cd7-9b5d-3b58-a0f9-7bca003a1605 | -7.0241 | -47.5294 | 2026-10-01 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f1311de4-9229-38f6-8e0e-d2e08d0ddeae | -6.1949 | -53.177 | 2026-10-01 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| da3871bd-0651-358c-826a-8ecf57e0197a | -13.3272 | -43.9285 | 2026-10-01 15:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 50cb5dba-90f4-3ae7-8152-d54000feb597 | -7.3446 | -55.5943 | 2026-10-01 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fc41fcff-4be5-3017-a65b-5cf4bd710c02 | -10.7112 | -45.3075 | 2026-10-01 15:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0d0590e8-a3d1-3330-b022-7c9ac7e82ff0 | -5.9152 | -53.4762 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 75c7fdbf-2c13-30ff-9b73-b8503d17d4f5 | -11.2278 | -45.1913 | 2026-10-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 1d7508ee-683b-3583-b5eb-c0ed993883a4 | -5.1252 | -56.0143 | 2026-10-01 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ff7b80bb-5f46-3836-9ee8-42ff115257e9 | -7.6271 | -55.0581 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ed786962-9dc3-3325-8ae9-e41f04ff257b | -6.905 | -52.481 | 2026-10-01 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 543a846f-fd5c-31cf-9ac1-17da3f093556 | -7.7222 | -54.7711 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0016cdec-fed9-3493-ae99-03b76a1be26e | -11.2095 | -45.1478 | 2026-10-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| baaf4513-aded-3c50-9326-33befa8545e1 | -6.513 | -55.3585 | 2026-10-01 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0df1a396-2339-3fcd-8362-d9ff493ef7b5 | -7.4791 | -54.9865 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e3bda224-e377-355e-b305-0937ace96a32 | -10.7302 | -45.305 | 2026-10-01 15:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 90bcdecf-1e04-3a1e-aa44-1aa706213f24 | -6.5505 | -55.2768 | 2026-10-01 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fe538dc3-7ad1-3395-a4b9-b1732e17bd0b | -11.2091 | -45.1709 | 2026-10-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 84ec1b3e-2ed8-34e4-a8b9-902f4518e874 | -12.3548 | -46.4 | 2026-10-01 15:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| eebbedf4-6238-32c7-9a5d-2321eba7634c | -6.1949 | -53.177 | 2026-10-01 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9d22518e-674f-351c-aafa-54bd86a83078 | 1.8404 | -55.5651 | 2026-10-01 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 6b0ac422-9297-38e0-a66e-2a3b9b83c5d2 | -11.3935 | -43.3705 | 2026-10-01 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 342c0a7f-a4a1-333b-b1dd-9da2f82e8c7d | 1.7115 | -55.9221 | 2026-10-01 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 157ee318-eb53-329a-9eb2-9e53fc2f56cc | 1.62 | -55.9035 | 2026-10-01 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 192ff719-31cf-3476-b34f-ce90c6d882d9 | -0.4319 | -52.0151 | 2026-10-01 15:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c4d54904-3b78-3af9-b40a-863f25e26532 | -12.904 | -44.7984 | 2026-10-01 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fff35735-beae-3695-8a00-26d1c538c77c | -6.3666 | -55.1261 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1c74ea82-ec5b-3b47-9705-303cafdef785 | -7.7858 | -49.867 | 2026-10-01 15:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 30a47007-401b-3312-803f-2236c13b7ef9 | -14.3574 | -44.7569 | 2026-10-01 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 6dd4d0bd-29d5-37e6-80e6-834624b84550 | -6.6051 | -55.4137 | 2026-10-01 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7108a517-3dc2-3dc0-82ae-11f5c52efd49 | -12.3163 | -46.4056 | 2026-10-01 15:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 35a194ca-6542-3388-abad-58bcb0263066 | -14.377 | -44.7534 | 2026-10-01 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 422.3 |
| 1b5e42e3-a956-35c9-a8bd-d95224a82976 | -7.4977 | -54.9854 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0b7efbe4-d418-35b6-9596-9035f7c7780a | -7.7219 | -54.8114 | 2026-10-01 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 9e8fe543-f365-3116-b1f9-b78c1aaf1311 | -8.53704 | -35.13904 | 2026-10-01 15:09:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| 75b93545-216a-36dc-814b-b0d38f5efcd6 | -8.34569 | -35.28017 | 2026-10-01 15:09:00 | NPP-375 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 662049cd-264d-342b-ae4f-8b670cf934fa | -8.53971 | -35.13745 | 2026-10-01 15:09:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 12a268bf-f892-34cb-a17f-ca5a69270c12 | -8.5326 | -35.13852 | 2026-10-01 15:09:00 | NPP-375 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 483b1b08-2de2-3e15-aa6a-791914ba7e61 | -6.1949 | -53.177 | 2026-10-01 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| d8960344-39b5-3385-801e-052220a711a7 | -7.0238 | -47.5514 | 2026-10-01 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6db0694d-30d3-3d81-baab-3381741caca1 | -15.6481 | -44.7217 | 2026-10-01 15:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 3497c8b2-1304-3fb0-afb7-b9044d895a26 | -6.3666 | -55.1261 | 2026-10-01 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f0484b38-7579-39bb-aa0d-7de1332cf0cd | -11.2278 | -45.1913 | 2026-10-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 0b2a7bc6-a570-3350-8f74-15e5cd0b554d | -5.8412 | -53.4799 | 2026-10-01 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 05633859-af86-3c26-9375-8af5ec1d1e88 | 1.7115 | -55.9221 | 2026-10-01 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e60205ba-3a7d-3c17-bc47-0ed3a4f8e286 | -11.2434 | -44.286 | 2026-10-01 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 2bf5479c-b234-34bd-9ddd-52befe7a0260 | 1.8404 | -55.5651 | 2026-10-01 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 9405d19c-1ceb-3abe-a79b-c38dee88d560 | -6.8863 | -52.5027 | 2026-10-01 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6f8e0ba2-64e5-3293-addf-c31a9422731f | 1.7116 | -55.9024 | 2026-10-01 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 76358d09-0b2c-30c2-8d93-b5a22a1c3e91 | -11.2091 | -45.1709 | 2026-10-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 4ae7f4e6-5adf-37c4-8e8e-79780c5e8201 | -6.5921 | -52.1287 | 2026-10-01 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 790427df-8a33-3e32-99c2-4076fe8804ac | -11.2275 | -45.2143 | 2026-10-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.0 |
| 1edbbee6-87c0-36b6-9c8d-1bef30f72407 | -10.7112 | -45.3075 | 2026-10-01 15:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d5ba6fd7-ac57-34c4-87ba-27c9c173701f | -6.513 | -55.3585 | 2026-10-01 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e7677b86-7dd5-321b-a4e9-f9c6b792e8ba | -11.2095 | -45.1478 | 2026-10-01 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 0960a0c7-4619-39d6-a9f7-8b0d6b8a2917 | -6.3666 | -55.1261 | 2026-10-01 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1a5b516b-e55d-3d7e-80c7-65c27e97c16d | -11.2091 | -45.1709 | 2026-10-01 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 43efb21b-91bd-3be6-b3f2-03c0b5400c15 | 1.7116 | -55.9024 | 2026-10-01 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0a57ded3-1486-32ef-8849-5d8bb6245d55 | 1.6749 | -55.9225 | 2026-10-01 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5fd58aae-62db-3c20-b13d-0f67bba4d2b1 | -6.605 | -55.4337 | 2026-10-01 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f3f450b5-f752-3db5-a535-80f36bd267d3 | -11.2278 | -45.1913 | 2026-10-01 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 520fc952-1ebe-35f6-9715-4521aee2d10e | -6.1949 | -53.177 | 2026-10-01 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 10270e8a-9aa9-3319-b18f-9000d7376380 | -14.3574 | -44.7569 | 2026-10-01 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 193.1 |
| c7e59a34-e0c9-338c-b5a8-1e122d272731 | 1.8404 | -55.5651 | 2026-10-01 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 16d40245-3d10-31be-9970-a764484337b8 | -11.2275 | -45.2143 | 2026-10-01 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| b6c91050-bb4b-3fcb-a47e-70e1a372e355 | -12.4355 | -44.1262 | 2026-10-01 15:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 05fe77f7-87bf-3064-ab91-1c7bcec4e8e0 | -11.2087 | -45.1939 | 2026-10-01 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| af98bd61-01f1-3570-9d5c-cb3c7aca079d | 1.7115 | -55.9221 | 2026-10-01 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 91094e22-97e8-3e55-84e2-6995c3d4eb0c | -1.4672 | -48.9097 | 2026-10-01 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 90d5ae9f-b037-3175-9d1e-99c93b5e8f0d | 1.8769 | -55.6239 | 2026-10-01 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| dd91c572-f06a-3605-92cf-c80cc76ecb20 | 1.6932 | -55.9223 | 2026-10-01 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 736e5b0f-abe5-31e9-b78b-318798e5ad7d | -18.34787 | -40.05239 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 3ff75621-0d1c-30e6-babc-86ba398df9a5 | -18.34071 | -40.05305 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 76636964-1950-3589-8be0-60722e493e0f | -15.96484 | -40.52287 | 2026-10-01 15:26:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.4 |
| 23962fc4-1879-33ad-90aa-807b35480043 | -16.87004 | -39.26337 | 2026-10-01 15:26:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| d86ed86e-c789-3f26-8f89-a795bb09413c | -17.41011 | -39.36705 | 2026-10-01 15:26:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1598fa3a-c488-3796-98d6-4be1be61d7c0 | -18.34424 | -40.06005 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |


[Clique aqui para ver as próximas entradas](README105.md)
