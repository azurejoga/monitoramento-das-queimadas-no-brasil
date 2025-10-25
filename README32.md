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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4c93ff8-6b76-3ebd-93aa-bac1005b077c | -6.10288 | -45.85194 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe82d70f-3fa8-30af-9fad-b790e7a936f8 | -2.79924 | -51.36225 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1744386-ec9e-37b7-9dc3-60b1770c4803 | -3.11313 | -51.21601 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da809b55-65b5-37b9-a969-d5ef5b90a6cd | -6.31271 | -40.92244 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 03d8158b-2f38-3155-b184-420475bfce00 | -4.83037 | -50.92781 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 682f9ef9-629f-375b-b723-6b8c50fa405f | -6.36482 | -44.271 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8a5521a-c5ec-3c1b-82d7-2e0610d36ba2 | -3.99849 | -48.31763 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 588a043d-5f12-3f3d-aaf8-5534b72f5659 | -5.30001 | -41.1436 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b89ed8d-5157-3f1c-89d1-f9d797e22e70 | -4.60769 | -47.0194 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 285782f8-adce-3f37-810a-3219e77059d0 | -2.79989 | -54.38332 | 2025-10-25 04:17:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f415eed7-f124-3a0a-9639-47df0a6c40f5 | -2.80428 | -49.14499 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 08dde9fb-8038-35a1-8d22-9f20595d2e24 | -4.55429 | -46.60727 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bedb8d5-220f-323f-86a3-bcad8f156384 | -4.28966 | -48.2646 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ecb9815-7565-3a78-ba0a-088fefe48469 | -4.37205 | -38.88805 | 2025-10-25 04:17:00 | NOAA-20 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 07216529-8410-3239-b5e7-4d8d42e58ccf | -4.5527 | -46.60222 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 926badcd-644b-3cb3-bfef-b0cef605819a | -5.57326 | -46.34856 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a24153-71cc-3a39-b723-263344c741da | -3.9977 | -48.32247 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bcf7cd9-9d8e-35de-8a53-db8a222531d8 | -2.81668 | -49.14695 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b08f9f-5ca1-3872-bf3d-8c8b76497237 | -3.47992 | -49.90097 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e739445-fcf0-3109-9578-527c36492ed3 | -4.96238 | -47.59837 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cb545c0-6464-3cf7-8a1a-45582d8d8427 | -2.7387 | -48.67309 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 951ad9dd-05fc-3a4e-8a78-d8907de53252 | -2.80962 | -49.13813 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b2914f3b-293b-3ddf-9565-1832f0418a66 | -6.54389 | -41.69398 | 2025-10-25 04:17:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 92ae7a96-f690-3c92-905d-573ce0ad21eb | -12.30551 | -45.52498 | 2025-10-25 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d27e851-aeaf-3d59-b64a-d78872a0c57f | -6.89128 | -43.61722 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dd8d4e9-a468-3347-a894-66ee74912397 | -6.97654 | -44.00788 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b19cfae3-8474-34f4-8b17-cb8ca8c037fc | -10.56153 | -47.9869 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b8d3754-060a-3bb9-87ee-8a8c72668423 | -11.00878 | -50.30475 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8600a0cb-a3fc-3127-9431-dba02233fd66 | -10.42162 | -44.49761 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aa5011c-51cf-343d-8147-0e808d0edc14 | -7.44307 | -46.60915 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 96c059d4-1cc5-30b6-9bdf-4aabf61b4c0c | -10.64078 | -45.24656 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b70887c-097e-3f83-8d11-010ae8fcaaab | -10.74062 | -51.6894 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9858ad09-9420-3ca7-8e93-5d225658ac04 | -7.93912 | -47.20119 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2879650d-95f4-3879-b96e-304071049aef | -7.64877 | -44.57368 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6027b4ed-8e12-3aa3-b775-91d92f6ae2a2 | -13.45296 | -44.06973 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71a80806-dbe2-3a48-b7f0-7794eb0d28d1 | -11.54944 | -54.51764 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549f5163-7f4f-36cc-94f5-c3c62eae2fee | -10.95392 | -50.2948 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c1af02e-963b-3197-af28-76bda6e452fb | -11.91863 | -44.17683 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6bdc9fd-5287-3354-84aa-1bf1e08ab98f | -5.81396 | -52.10403 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6482430-829d-3fb9-9fdf-355dc9eb824c | -6.99642 | -42.7941 | 2025-10-25 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea386d23-0161-39ed-9d94-28cc3612ed3a | -7.23758 | -44.96179 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6063483b-9036-31eb-8c48-58f56333e2f8 | -9.61344 | -46.89759 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56c2719b-765e-338e-95ec-0eeb51b8ba02 | -7.24088 | -44.96231 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9cb431e-4532-3c3e-a103-e18773933f69 | -11.10019 | -54.39317 | 2025-10-25 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62a69a23-3c36-37cc-ac78-f567718e46b0 | -12.53883 | -49.60587 | 2025-10-25 04:19:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6285ff9f-1076-37ee-bbb3-a69ed32044ea | -11.0233 | -45.05957 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52b5199e-6f0a-339c-8f37-a105a4817e88 | -6.91684 | -45.16307 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f4a0a9a-063d-33ba-9f51-c02e5ea097ec | -12.05157 | -46.44272 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e97c1ad2-36c4-3ffe-8de1-b7b2e3a26032 | -12.11575 | -47.39435 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92d6b9af-43e7-39c7-b642-14bbe25134b0 | -7.56029 | -47.11819 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d86b2f4-8d59-3253-8faf-e42ce856e862 | -12.7715 | -47.37551 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29d62b76-8352-314a-8fb5-ba13c86b4102 | -9.99553 | -47.09629 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3827817-a1b6-3302-a6ae-a1bad819504c | -6.79234 | -46.46803 | 2025-10-25 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b7491f5-242a-39f4-a138-eb1c224b8447 | -9.4355 | -51.47404 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03453cb7-5358-3562-8b6f-06dc823b5885 | -10.00203 | -47.59483 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 357fab9e-45ff-3b6a-9883-884e396490e5 | -7.64352 | -42.16836 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f2fee6db-87e2-3050-b4d2-3d92209a5312 | -6.92401 | -45.16068 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9ab5b86-8305-34d2-8ffc-58aff425cdf9 | -10.70839 | -44.7497 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef284b06-0a7e-300f-9800-3982ed1c1c5d | 0.36929 | -50.85731 | 2025-10-25 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 781022a2-a734-3ea9-b3fd-70ab592f76d3 | -7.61889 | -45.19306 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b12304-4a60-3b7d-83b8-a7297b970157 | -10.56785 | -49.0848 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6599106-2d28-31d6-a645-5ed9f3684aee | -12.10506 | -46.70327 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 767cd9ab-cf7c-3aac-b777-50f18fcb75f5 | -8.11686 | -55.08583 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d772e48-fa4e-3e4c-9c6b-67056c65b167 | -10.02385 | -45.00081 | 2025-10-25 04:19:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0099db27-e136-3508-9834-03e2f06f1c59 | -6.54832 | -46.6315 | 2025-10-25 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 130314eb-ea3d-3163-8a6a-d8411adcefd1 | -10.65911 | -48.07543 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c792568f-84d2-3b26-956c-1814e0a50fb0 | -13.37961 | -44.32675 | 2025-10-25 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f19e4ce6-f714-312b-ab8c-af6c19da833b | -10.41059 | -44.74202 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a6a343-9c50-3f1e-a341-e0218b6e937b | -12.945 | -48.50272 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14024d61-eafb-3e06-816b-6683aef2e3bd | -11.95766 | -55.26246 | 2025-10-25 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a279c1d0-5666-334c-a1ee-fda584699eea | -10.71171 | -44.75023 | 2025-10-25 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7016d2f4-6575-3184-9922-2c4c635bf56b | -12.86785 | -48.5999 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fab8b9eb-4e68-34ea-9a94-052e2264323d | -7.41885 | -46.6507 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 464b2a0d-6f78-3421-995f-ce3e45401ce1 | -6.45098 | -44.28457 | 2025-10-25 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b46f293-6fee-33d0-bcaa-e570ab92e711 | -9.09098 | -47.82113 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a13b92-56a8-3d5c-ae32-8041634a2c43 | -10.84677 | -48.96837 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36db4e72-97f3-3a45-982b-01a0c3e70c60 | -10.65423 | -48.08312 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8bd1836-6fa8-371b-8887-fede7d0ffb13 | -8.1086 | -44.50053 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491ce539-9b3b-3235-8f9e-08d67e71604b | -6.7649 | -44.20948 | 2025-10-25 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ca02791-29a2-3034-a507-c6725cb4d246 | -13.37638 | -47.45763 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 689e405d-4218-3379-af4c-21bea6522f6b | -12.0622 | -46.39741 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c33d183c-4993-348b-a03b-38a471f3c743 | -9.61285 | -46.90126 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4ab9e67-86ca-317a-9598-284109ef550d | -12.05114 | -46.40281 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf8d89b-64cd-3eb2-aea2-73021f30e349 | -10.62058 | -52.18834 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4eb9476-093b-32ad-a474-0086e516d057 | -12.83387 | -48.6306 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cd470abc-f546-344b-9484-84a59bbe1d52 | -8.44833 | -49.57283 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581fb343-9d87-3b1f-8e50-7752df5014d3 | -7.64313 | -42.16927 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0202c5c6-2e73-38f7-9910-50e4463f2877 | -7.03283 | -43.93083 | 2025-10-25 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a5f17bfd-ab9e-30b0-b0a2-86dce493f74c | -6.07009 | -49.38024 | 2025-10-25 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f724f68-aeaa-33e3-965e-baa5d5abb135 | -10.81982 | -48.00077 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f7554b-7d06-3137-8de0-d321e11d986a | -12.83889 | -48.64352 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 521fecf0-cc03-30b9-bed2-5cfef7a24b29 | -11.57659 | -49.53819 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfa2562b-2948-3e7d-bb8f-3a650821d8bb | -12.06481 | -46.44508 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b24a0f0-413c-303e-9bcc-b7366b863608 | -12.1233 | -46.71728 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73faf145-fd9f-3776-8f62-cd824bacf6e2 | -7.23364 | -44.34049 | 2025-10-25 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91761d7e-849a-3e77-b6dc-321ecff77d3f | 1.63247 | -55.75599 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0ec2daf-6775-3cb5-bb03-323a0656b8b4 | -8.5678 | -48.51257 | 2025-10-25 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98835006-d18f-3759-88c4-335129797d04 | -13.64981 | -44.22791 | 2025-10-25 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d030f556-1ab0-3dc3-afed-0d445355d038 | -12.05445 | -46.40342 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57393500-639a-3ad3-bf92-821014544b3d | -13.35333 | -47.40891 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README33.md)
