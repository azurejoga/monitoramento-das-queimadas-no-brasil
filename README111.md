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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4abfa72-6d4b-38d0-9976-0bb26675a919 | -9.14052 | -46.64928 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a125d725-d400-315f-8aa4-3fa7449103d6 | -8.16303 | -46.06443 | 2025-10-17 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2df5e175-2a81-3486-9e27-4aa396abc936 | -10.15041 | -44.53523 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cca47984-691b-3a69-aa0d-c8fcbeae2039 | -7.17336 | -46.94026 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 626a6fde-aad9-3a56-afce-62a79cda919e | -13.42782 | -47.96325 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1636223e-bc38-397e-9914-27f1b286efdd | -13.38999 | -47.21861 | 2025-10-17 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bd99591-991d-385d-a61a-d6b261685f42 | -13.42692 | -47.95797 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ada14d2c-1dcc-333a-b80d-f214236d2c2f | -9.14109 | -46.64496 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 06abaa9e-0dc1-352a-9406-078a6b647d0d | -9.88231 | -49.12062 | 2025-10-17 05:10:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 050975b1-534d-38ce-b72a-84050fa2f5b7 | -10.11935 | -52.3437 | 2025-10-17 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cecc933-30b9-3f22-883c-57e22b489b47 | -12.71265 | -48.63635 | 2025-10-17 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 073cca1b-ecff-33de-9ccc-809ef0d5592a | -7.95067 | -44.10938 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d74a37f-23ec-3a82-a1f8-6b9c885d00a2 | -12.44542 | -54.50322 | 2025-10-17 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b08e75-383f-36b2-92fa-a3a66a255404 | -12.20061 | -61.83604 | 2025-10-17 05:10:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3c357a2-5207-3a8f-b84e-5c213a209c0a | -9.26622 | -45.27129 | 2025-10-17 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bad25977-cf7a-3803-956e-bf0db5aaa2b1 | -9.14606 | -46.65409 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ebdc630-1c65-3505-8c14-57914a1208eb | -8.82069 | -50.0533 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7de099b-b420-34b6-9d16-8d4e9f7787bd | -11.51811 | -49.14538 | 2025-10-17 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bff2521-f17d-3507-9dc6-54e6df7edfcc | -7.94984 | -44.11615 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 63d16437-c472-3e4b-9b90-3fb39eee12dd | -9.50077 | -47.26948 | 2025-10-17 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c536344-c87b-3540-94b0-01ba646a9d87 | -13.41951 | -48.58305 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b47efb3-f39e-3685-b618-bdb02ba0a155 | -12.16696 | -45.07732 | 2025-10-17 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4728ab8d-1b6f-32f6-8b68-5df632286419 | -10.56763 | -47.42511 | 2025-10-17 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d7a920a-9476-3dbe-a0e6-6fa75216d209 | -10.27896 | -44.04106 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc6c4ab6-639f-3f04-8e82-844c177a3396 | -10.53092 | -49.55058 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 160ed153-ab77-336f-86c4-b9334d984c65 | -9.45253 | -56.65827 | 2025-10-17 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6396238-46e9-318f-952c-70fbec84285b | -9.07304 | -45.91445 | 2025-10-17 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6ac4af3-bf9a-320e-a178-be1eaa2a5c62 | -10.28619 | -44.04164 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bf0ae6d5-a010-37c9-a5de-c4f7a9ceec72 | -9.14376 | -46.63438 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e38b035-cbed-338e-8bb2-5d44f10f9120 | -12.7822 | -44.88669 | 2025-10-17 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0786bdf8-c321-382a-a47f-af78e7aee07f | -10.1379 | -44.57949 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 199cfd10-9b3f-34d3-9fd1-40fe7f5d22c3 | -10.18562 | -58.18569 | 2025-10-17 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1178dc7e-f686-3fc0-893e-817bdf2b9e8e | -11.52385 | -49.14283 | 2025-10-17 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e03b2451-2c43-36d2-9bf6-81ce00240b75 | -9.1365 | -46.64309 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c20a8881-dfe3-3e66-9c3b-48523469b3bc | -12.45333 | -51.33312 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f673e012-3440-30ac-a3e3-207add6f16da | -7.48616 | -47.03449 | 2025-10-17 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2aee775-06a1-3d96-84f0-3867558efd9f | -9.6194 | -49.12291 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb2fb86b-2867-3f4c-8089-4a964880d74f | -12.45501 | -54.49032 | 2025-10-17 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec61e242-f50f-3201-8f0d-b694151c88a8 | -12.41406 | -51.30761 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77eb755a-9604-3b35-84f9-43e09d1dbfa2 | -11.19186 | -51.75105 | 2025-10-17 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97f4cde2-8264-35f3-81ee-2147dad6cae6 | -10.65277 | -45.25526 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28129bd5-db99-32d4-bc5d-9934d8dd9121 | -13.44959 | -47.96923 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b8f2e98-9385-39eb-af76-c00846f0f3e8 | -10.56708 | -47.42953 | 2025-10-17 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8e8d100-ea89-367d-b309-2ecd9210ed02 | -7.20246 | -45.48864 | 2025-10-17 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67f19250-e5f4-3658-963a-1a4eb4be2ecb | -9.71335 | -44.55294 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3571907-b4e7-352f-a7ca-d65d80b8ee2b | -9.06797 | -48.84881 | 2025-10-17 05:10:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 944aff49-0707-3006-802e-6659b61dc614 | -11.43859 | -54.09589 | 2025-10-17 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289abbaf-2fcc-38ac-b663-c10249c2eaca | -10.64674 | -45.24854 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dffd510-4a61-3ce3-bfe3-2033ed7cb583 | -10.17561 | -44.7909 | 2025-10-17 05:10:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f84930c0-5fa5-3fae-97b7-90b884a7ae3d | -8.41269 | -44.72918 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e41c1c1b-8fa8-3b14-9a15-b331b316aebd | -11.57306 | -48.56871 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa2d4dc5-2a68-36c1-a420-681f193db697 | -12.44265 | -51.30649 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a53b72-6d6f-3585-bdd6-1d6530748ab5 | -10.14115 | -44.54178 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1aa4b3b8-7543-30fa-9701-ab02ec8d4b8d | -8.40816 | -46.28513 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c3229e5-9b00-3587-a3b3-0580ba0fe245 | -10.18362 | -49.51257 | 2025-10-17 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f34ffcd8-a29f-3765-96db-0182d623ad41 | -6.94511 | -47.72733 | 2025-10-17 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b33719f9-83ab-3e3e-9221-dd693ac49e79 | -10.94147 | -49.48236 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9e9c778-1733-3f34-998c-b23ffff8c6b2 | -11.75817 | -61.07084 | 2025-10-17 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65c55bd6-4cb1-3985-b13d-6d49045f4b74 | -9.1476 | -46.65297 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c60ae05-bd04-34ff-8465-18819228ea5c | -10.65487 | -45.29466 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1367aa22-16ec-35b0-ace2-ef492da8ef19 | -12.42338 | -51.30888 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ecef30cb-ca04-335b-8973-0a1b7547fa4a | -11.40172 | -44.23857 | 2025-10-17 05:10:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93ee4e4d-4c49-3ba1-8517-52d714e493ec | -8.56315 | -44.5942 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a089a631-6ab3-3d75-8af9-54a8b1f41c60 | -10.26686 | -44.04432 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0ef3559-b16f-3e16-afc3-bcaf48f5561d | -13.43861 | -47.97307 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e46ab76-6b59-3f60-a118-3c1224bc2cf1 | -12.04207 | -54.24692 | 2025-10-17 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7ad745d-dda2-3ec2-af7c-807798dd6555 | -12.77513 | -44.88604 | 2025-10-17 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aa7963a-b49a-31ef-aa28-880cbc37ee64 | -8.38153 | -46.24912 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 19302432-e1c1-3c07-84b8-6dbf255e8767 | -9.10056 | -46.67184 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa6b09fe-76d4-3cd9-bfb6-676b2c124d57 | -13.41385 | -48.58232 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48824b8b-b28c-3f44-80eb-fcfb6f50dd4c | -8.15261 | -47.98407 | 2025-10-17 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27de4f73-b814-3e2f-8e9b-7ad333bdf731 | -13.44913 | -47.97325 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8371167b-b9ea-3711-8fc7-782ccd2d7d99 | -8.62192 | -54.56037 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c00a7606-666a-3240-8b4a-35c36a675285 | -8.45151 | -46.24203 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e6bc7b4-fb47-3186-b0b3-ceb40d1d8ed2 | -10.08795 | -45.34237 | 2025-10-17 05:10:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7da18d5f-c93e-3e7d-a1f7-c99595eed70e | -11.16857 | -59.11695 | 2025-10-17 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9509ac98-b605-3a53-9d95-3bcb35a3c249 | -9.72141 | -48.9187 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f3dfb79-646c-32f0-9039-39d6db47dcf4 | -10.53563 | -49.55433 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49798359-5a88-3e79-8fc2-059423ffe628 | -6.53721 | -55.04647 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4e50129-5e6d-3cae-9a74-95bb397caca2 | -8.46013 | -44.18258 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23d575b8-8291-349b-9f3c-e471c68f0e26 | -7.7217 | -47.84589 | 2025-10-17 05:10:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a4388f-e89c-3576-b68f-eae4e40cde2b | -12.04642 | -51.37488 | 2025-10-17 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cce67e8b-a65d-38e1-9fe0-a42d8aca08fd | -13.42829 | -47.95931 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c5e6b69-bcf7-3cee-a59e-22d92d91a61a | -12.43799 | -51.30584 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af3042b8-594d-32b4-8f05-03b5eb11a5a3 | -12.04657 | -54.24268 | 2025-10-17 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c8b2cf1-3cdc-327d-97a4-6583eb55c26b | -9.33969 | -46.9103 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c50a613a-7fd4-3a6c-8f5f-98c322be20a7 | -8.46165 | -44.18282 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a173ca07-87b5-3820-8da6-9a6e25cd23e5 | -10.53133 | -49.54752 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ac7c59d8-a82a-34ee-94b9-0c2bd54c9602 | -10.94922 | -49.78117 | 2025-10-17 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1d496d8-f665-337a-94e5-184df0b21afa | -9.13045 | -46.64202 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c7ad672-f167-30ea-b768-b4f9ea91828b | -8.1581 | -47.98486 | 2025-10-17 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72aed5c2-f1c1-325b-b30b-cabeabe30b11 | -8.45024 | -46.25152 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c353dd5-65a7-3533-a5aa-e03d9aa69785 | -8.41936 | -44.73082 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef68051c-fcd9-3448-8df5-589555db3e4a | -10.43599 | -45.01848 | 2025-10-17 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a793516d-b5ff-3105-a011-ea02057927ea | -10.118 | -44.55839 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a60797a-ac60-319a-988a-55e1ea7dcedb | -9.14549 | -46.65842 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95963989-7c19-3b56-80eb-de2a1ae43311 | -9.02095 | -46.61872 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9ceab77-deca-3860-84d0-f153187b56da | -9.21062 | -61.54565 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a3afdf8-5938-34f3-a866-25ce1315158c | -9.02911 | -47.72135 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b47dbc1d-c2d6-3aa8-8c89-cc85376103fa | -13.3971 | -47.21954 | 2025-10-17 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README112.md)
