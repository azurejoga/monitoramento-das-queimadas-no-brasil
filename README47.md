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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11de1bcb-9df3-3c49-a34d-146cbadc1b46 | -10.59218 | -47.99818 | 2025-10-18 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d612637-d68e-3c75-8a4f-3b54e6f46148 | -5.53606 | -44.09745 | 2025-10-18 04:29:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d39b2eba-2b86-3d20-b93f-b63c8df02dec | -10.24953 | -44.05225 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4da74a8-e922-39ed-ae18-f7d33c37e074 | -5.15919 | -46.26711 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b9f2529-7760-3a06-80f4-4bb4304b2fb4 | -6.40074 | -41.477 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 114b14d5-8839-35a0-bf92-aaa3e93f5cc4 | -10.42764 | -47.7361 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ef34119-69a3-3ed1-af76-478b9459aca9 | -4.30608 | -48.06319 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6633b2b-4c1a-3e94-9680-2d20e462c349 | -6.99957 | -46.99107 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b74e74-936b-32e3-bff0-73cb57248646 | -8.20395 | -43.96214 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4996ca7c-f6cc-36ad-b2a0-90d3dae2c187 | -4.93832 | -49.7646 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c0d21f2-47d9-3c47-9b85-3915dc678b34 | -7.42812 | -46.99809 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f3849e-27cb-366f-b81e-584522702b4e | -6.39055 | -44.63953 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ddc0c24-7947-3070-b537-b50585fa2c95 | -10.49379 | -43.45272 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 029c070a-2256-3334-afec-a4e1f268f48b | -10.13216 | -44.53846 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77bb4913-1f4c-3ddc-ad65-dbd1de31e9c2 | -10.29979 | -44.03807 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19e1bd3c-f996-389a-8425-e64138a02f35 | -7.58717 | -44.97462 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e424e9e2-8990-3647-827d-8e59087aaadd | -8.65034 | -47.08288 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f301de72-6697-3766-8347-201de870deec | -7.22392 | -41.1642 | 2025-10-18 04:29:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a218f45-8807-3dec-b9af-626d71b8ffc2 | -8.79268 | -40.43998 | 2025-10-18 04:29:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6ab4b7c-4ac4-38a8-a507-9ad671d86758 | -8.56367 | -45.42865 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5891ac75-cb2b-37ce-8f3d-29d8e3a9defb | -8.3956 | -46.23349 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e5f7829-9cff-3088-baf0-5dc5dcbbc1e0 | -4.87992 | -46.70435 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8bb61e1-bbe5-3142-8470-d37e3ace8be5 | -7.19888 | -44.68938 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9184e02b-0203-3433-a390-00c885f4b5d5 | -7.46237 | -42.16869 | 2025-10-18 04:29:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 12c307ef-9a60-3ad3-a458-5bc48d41cdf7 | -6.23892 | -44.14804 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8242422e-ec93-3a2d-8858-c96025040a79 | -6.33539 | -44.00617 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 393a3887-d344-3850-ba0d-8c2352bfc88c | -8.40615 | -46.26713 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a3d5034-506e-3b2c-aa28-50daf685d0df | -8.47968 | -44.18519 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f7082fe-0189-39c3-8f04-f7d1d912e282 | -4.77541 | -45.7457 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed53d763-9333-361a-8a0a-724570115cff | -6.29441 | -44.71873 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 237df5de-cc43-33ca-8240-ea4b52061e10 | -7.36739 | -44.06456 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33f2ba7b-d9ce-39ca-8896-8baee3b89a6a | -7.34461 | -43.85967 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4b4b5d4a-ae6e-33cb-b4cc-c089a192da34 | -6.36282 | -45.75665 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a491efb1-b730-3dfb-bdd2-c84f96fad44d | -9.61982 | -46.31412 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18a0d91a-e0e8-3704-bdc9-750fba25de84 | -10.14877 | -44.52433 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c654c1d-85a2-35b4-bf1a-34c0e99f9a22 | -4.96585 | -44.60184 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fb4868a-4e7c-3f58-a32a-86d9e82e3861 | -8.10993 | -55.08725 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52e126b1-d825-3926-9ea7-e2bb82f8b7cd | -9.28423 | -43.74006 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab71844e-b318-375a-83d4-6e6fd4ff2350 | -8.37491 | -48.70859 | 2025-10-18 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1bf957-73b8-38c5-a87f-1910ec80c588 | -7.18153 | -42.18175 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 850fc52b-3330-3c87-9ccf-0a45920bfdba | -6.58374 | -47.07552 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70094d67-f4f1-3b5b-a656-fc60727a491b | -7.54969 | -37.78984 | 2025-10-18 04:29:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d080e88d-65cf-36dc-8296-3e1ce613586f | -10.23722 | -44.89497 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb0e330f-4a3b-3e64-9a84-98420b0a53b1 | -5.91371 | -44.76515 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 672f28ea-2a58-38d2-8148-8d6d317bb3bf | -9.96858 | -43.96638 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2f8d279-9542-3742-814d-9e96bb05ae1c | -6.88773 | -45.43158 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4824ec5c-3d33-3312-a4b9-fa7c894b7ff2 | -6.40626 | -47.20914 | 2025-10-18 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e539a185-5c25-36ac-891f-34dea852eefd | -7.99016 | -44.15911 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2abbac50-932c-3c78-9138-9e35eb14a91a | -10.10266 | -44.56646 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 894cb390-ca32-3d97-9bc3-1e9335b6add1 | -7.21217 | -45.39013 | 2025-10-18 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2225a430-1723-35f1-bdcd-526a9747043b | -6.30121 | -44.71981 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cbdcce74-d23a-3582-a972-31fdffae396b | -10.62526 | -42.30855 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa483df0-75ae-3550-9f72-c10e55b94fd6 | -8.04429 | -41.10641 | 2025-10-18 04:29:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4dd56c61-7577-321d-8a7b-9b0e4fb0757c | -8.82786 | -49.68206 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca57ae39-6912-3d5f-b25a-b7354ee76474 | -6.23322 | -44.64262 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbfa821f-a483-33b5-aeff-7280f7f32231 | -3.79507 | -51.76381 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e8af2f-d7bb-3b6d-abcb-054fa4fc1d77 | -5.25924 | -50.90674 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db898a4e-3e98-3c53-9082-6f9ea1940eb3 | -9.23159 | -44.37603 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d856f3d4-9ec9-3730-bdf7-fb6a797f3951 | -8.54804 | -44.58205 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f67d268e-5fe6-3c5c-a48e-832d061d772e | -6.99111 | -45.19908 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4531b630-8b29-3d39-9c00-17017a3639cd | -4.82485 | -45.23694 | 2025-10-18 04:29:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 72be2c41-9ccc-3cf8-8113-1f872c5642bc | -6.21036 | -44.42786 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e05575b0-b143-3324-aaeb-8dcb45063730 | -8.34546 | -46.8908 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa8b9af4-a856-3568-a60b-7e54f46214fc | -7.12187 | -44.73436 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a2c1ba3-6117-3576-ab6b-3698a5adbc80 | -5.20732 | -45.75319 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea91c932-2754-3415-ae72-331601e97ca3 | -6.60935 | -44.21475 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad051439-183a-3c09-bde6-29fad179335f | -3.86089 | -51.91017 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 160161d0-0c1d-35d3-afd6-374b530cafee | -8.60819 | -40.19595 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| de98047e-15ca-3f4a-a65c-6c89dc2ef26e | -9.68492 | -47.80363 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90bdb4cd-5735-3b83-96f8-a97d85b97850 | -8.18632 | -47.04071 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e51995b-4a09-3989-939c-ee77463c7e69 | -8.16479 | -47.03024 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df5b927f-12c8-341c-a657-00626ae26142 | -9.17648 | -46.73025 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dcaaaab-6a59-378d-9fd4-79e69ebaf9b6 | -8.39282 | -46.22946 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 235fcf57-c485-3dcc-92bf-5003e38a8193 | -8.54063 | -50.07928 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cffd1b3-44a8-3310-8177-9ec3adf28ff5 | -5.20787 | -45.74972 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 993b35b9-ce9e-3000-809f-3b3ab849fa1a | -10.41986 | -47.7421 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbd4ace3-8339-3111-8912-b82426aca275 | -10.43534 | -45.01457 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10e48d37-c453-3baf-9946-d0b1ebb7a295 | -6.21202 | -45.29388 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d251115a-9971-3c2e-8ae1-51a9aa8746e2 | -6.89391 | -45.45791 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc973328-9e85-3bc7-a9a8-7d7eb24a7e7b | -6.70246 | -40.87123 | 2025-10-18 04:29:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7027646d-80b5-3007-ad22-086b8b184c5e | -10.71428 | -44.53868 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b52823-3fe2-3e9b-a785-b4bc492c3f48 | -5.29702 | -47.93638 | 2025-10-18 04:29:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 291b48e1-9095-3556-a378-ac36ea759fc3 | -4.73084 | -46.15699 | 2025-10-18 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05a7bf1d-abdd-3165-b2a7-b42d8b695c4e | -10.69908 | -44.54966 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 992cbfe8-4d34-3ed1-b257-b2c5e5993749 | -10.42042 | -47.73857 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 977dfb98-29cb-3240-9c31-6d192f943cc7 | -8.21894 | -46.83508 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c087b31-17f9-31d0-85fa-4e765b0b5840 | -8.09342 | -45.44898 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 776bcdf9-f3d8-3c16-808e-50a358cd659a | -10.14814 | -44.52848 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f7b9c0c-c5fb-3a58-bb50-16bc6cd153c4 | -8.3617 | -46.21013 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1583053-27cc-34f5-96df-ecce84101b90 | -6.18304 | -44.33617 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d10be472-0554-3446-bdc3-f9909ab09181 | -7.16781 | -46.52893 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cc1203a-290a-3d2d-ad9d-ba902888f28b | -8.56423 | -45.42503 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f66ef808-c610-38ed-b6e1-6faeebb25445 | -10.25015 | -44.04805 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3979d837-4489-377b-afb6-c76e473c6a1c | -7.92609 | -44.12952 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7721aeca-7884-37d5-b40e-167a2687510b | -8.39172 | -46.23647 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f55f798-03c1-390f-a8ac-25d9bc16e369 | -8.38396 | -46.24241 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e51db6a4-df44-399e-a88e-bf7af3bbb664 | -10.13984 | -44.53553 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6b5857c-cd8b-3ae6-8181-ed78fe7805f9 | -10.46708 | -44.06488 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb8da276-25c2-3787-afd2-0b8457b46839 | -7.43992 | -43.75375 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ea7a61f-7d23-3f48-b9ab-43804030c47a | -9.91225 | -48.14342 | 2025-10-18 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README48.md)
