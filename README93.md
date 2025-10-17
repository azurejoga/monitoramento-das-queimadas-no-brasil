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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69cf17f3-594b-3736-97df-7a7b3027a470 | -12.16547 | -45.07077 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba17890f-f60b-3221-9427-e88aeaada344 | -14.15594 | -44.31576 | 2025-10-17 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa18b4b9-efa8-3a65-b80f-31f333a25da8 | -10.18121 | -49.51644 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709c2eb7-c0f5-38c3-8951-1660e53c72b9 | -11.57622 | -48.56765 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 56f0a41d-12ca-37e6-ab30-1639f616402b | -8.25795 | -44.03099 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da5ca878-ef84-3ce6-9299-3096529d516e | -9.33634 | -50.69593 | 2025-10-17 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ed3e23a-ea61-30ef-b20f-60cca6b51337 | -12.4619 | -51.48535 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 659afe39-108c-3408-8bfd-b19b8467e877 | -9.26992 | -45.27426 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6dd1c4d7-466a-32bd-b35f-1a8539e80d40 | -9.26609 | -45.26905 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80a4939f-c21f-3d47-84cc-b66cb05660f5 | -9.2495 | -45.25737 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 331d7090-5f5f-3cea-a8e4-223ae9c19f68 | -14.30975 | -51.44041 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3bf1fa30-92e7-329b-8b0b-fee132c2169a | -10.98069 | -47.89621 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5258c697-eaff-3a8a-859c-81ed43fe69af | -10.10332 | -44.61551 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e08b32b0-4ebe-3112-8f2c-57a3cdd3226a | -13.5743 | -48.48888 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd59ee36-d9bb-3730-8b1b-b33e2ce58bad | -11.41504 | -44.20762 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3b0cd11-e5dd-33df-97a0-9fd02544edcc | -9.88721 | -47.67473 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dfd168c-6e25-3d00-a822-8526103a2dde | -14.32559 | -51.45055 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fde9ff4-287b-3b42-a31a-fb9c093114d9 | -13.82206 | -42.3481 | 2025-10-17 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 10a0bf05-dbc3-3b1e-8021-0a364094c9e3 | -9.14406 | -62.30082 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 045423d6-dd64-3a2d-af0f-7a0000d4beef | -9.87467 | -62.41061 | 2025-10-17 04:51:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99095f7f-bc28-36f9-925f-d7ca87bf80e4 | -11.14229 | -45.84932 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a03306a-d423-30e6-b9e8-85f4a5779673 | -11.14316 | -55.19539 | 2025-10-17 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24719646-2a8f-3a4a-b058-e641b10f5eb6 | -14.31827 | -51.47597 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a912a170-92cd-324c-91d3-cfadd850b6fb | -10.26643 | -44.02975 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01f913cd-bf14-35d3-8648-489371605b95 | -8.50946 | -44.57167 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4095a4-a10a-3092-84b4-3356e31acd8e | -11.46626 | -44.24959 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f047571f-d90d-3f6c-91ac-93a560763c12 | -12.30679 | -47.26004 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02dc41fe-b247-3199-9fd5-0590dac95ad9 | -8.45599 | -46.24075 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 238c3642-21ed-37db-8356-284fbae33c42 | -10.65499 | -45.29155 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a869c367-eb95-36bd-bc3c-d4d78066ab9b | -9.50094 | -47.26709 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff9de1fd-61a8-33fa-8afa-0de86d2b8d3b | -12.44498 | -51.32004 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 333977fa-cf7d-37cf-80b1-60d423663980 | -12.1736 | -45.06886 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a0838ee-856e-352c-9f18-0be208c12a82 | -11.57339 | -48.55585 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720d46e6-1d92-3464-b4ab-56a0d030829b | -12.50833 | -54.38631 | 2025-10-17 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7976f675-7e36-38f3-aef8-0c3b8baab2f2 | -14.15047 | -44.31811 | 2025-10-17 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df975dbe-b224-39fc-8095-d704ab28ea59 | -12.04216 | -54.24288 | 2025-10-17 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da01ea94-ca41-393c-806f-5f1f41ddc338 | -10.61956 | -45.23989 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56fc4494-763f-3eec-b211-e3416f86107d | -14.34425 | -51.44211 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e98e6b8-5414-3be1-b185-81cdeb89f6c2 | -10.27951 | -44.03658 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ccbefde-05d5-398a-9b92-b743c8f420e8 | -10.97734 | -47.91945 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07ff66dd-fc35-351d-864a-499cfcae9f6c | -10.38864 | -57.5014 | 2025-10-17 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74aaf298-f27c-3411-b3e9-7d0a6a8422ef | -10.64638 | -45.25156 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 750dfed1-81ca-3544-a223-3c3d0f25adea | -9.7142 | -44.54364 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab6c908c-a8c9-36c4-9996-50f977231761 | -10.50992 | -43.4096 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeff7cd6-c818-3189-ad36-eec5c7663fc5 | -13.24506 | -47.10415 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cca8e39e-4d8c-3b90-ba11-16a3b3319c15 | -10.64622 | -45.24844 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bbc8083-928a-3b32-acba-0ca583625ca2 | -11.57645 | -48.5609 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0636a77-177f-3b01-90cd-4cae9f3a2ab6 | -14.30185 | -51.44675 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fa3608f-acc9-3ff5-8a00-e92cef97da73 | -10.22513 | -46.73065 | 2025-10-17 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7be2e2f9-c9fb-35bd-b077-e490a006e48b | -14.34312 | -51.44954 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b700c93d-d430-3788-98b5-2a9cd6ea57de | -8.08518 | -45.44327 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95c86432-478c-396d-ac05-6a848156d31f | -14.3335 | -51.4442 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9682d07-abaf-3290-ae3b-ceddff6b2bea | -8.61757 | -50.4493 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23193dfe-1bd4-322e-adea-42f2e5091a7f | -8.12008 | -45.56781 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a82541e3-1068-3767-b7c3-6f2d9b488463 | -15.7899 | -43.64823 | 2025-10-17 04:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3347f4-be91-3ade-8dc4-1f11bb73f779 | -8.96611 | -48.43222 | 2025-10-17 04:51:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51dba7ac-2590-3e96-9a58-55095a2f57e5 | -13.24207 | -47.12602 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78014099-6f1f-3858-8f9e-0db795d9b709 | -10.11752 | -44.61716 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3891105f-650b-3283-8a37-e2b1242fe83e | -11.14553 | -45.85852 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c38af3cd-84cf-377b-9091-de19a0677b75 | -8.40223 | -46.23413 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98582c56-5372-311e-892c-fcb02ad8e1aa | -10.64361 | -45.30022 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90df8c2c-818e-344e-8a99-9064bd7e3b8e | -9.14539 | -46.64467 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b99e335a-5d27-3681-814f-39483c1d0c82 | -10.53527 | -44.50537 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6873e7b7-80ec-359b-8dba-89445e83142b | -9.94706 | -45.7132 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 808eb378-abdb-35e5-bf5a-a52bfd17ad23 | -13.25384 | -48.5576 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84868fc0-ebc6-3eaf-b7dc-4bb7f1e0a4b1 | -8.72677 | -43.87026 | 2025-10-17 04:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19e74253-ceb5-343d-aa28-10dc9c4d18a6 | -8.40021 | -46.21881 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c540bfef-efef-399a-9c74-7f0f51311f4c | -10.65048 | -45.29062 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4dd99067-18e8-33ed-9a2b-d792b6466441 | -11.75766 | -61.0752 | 2025-10-17 04:51:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8be6bfbc-b838-34c5-8e0a-444710657651 | -14.33916 | -51.45271 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 620f89c3-8520-3b53-bd23-03f6e183f37d | -9.14809 | -46.73899 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0ecace9-969e-3778-8d33-b11daa4544d4 | -10.01387 | -45.64925 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad8d6495-e5e3-3198-9e33-c47e26b800c4 | -8.06276 | -45.41416 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e21c7219-a290-3cf0-92d4-c6876fd6954a | -8.38975 | -46.32133 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05d0a580-f400-393a-a397-11d488c67eb3 | -11.14496 | -45.86272 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58183765-6889-3bd8-a134-0fe0278b3553 | -9.09824 | -46.68493 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dce7d901-0e94-30b8-aeb3-b769e6b96f94 | -10.8685 | -59.17353 | 2025-10-17 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c28b36-87a8-30bb-b6c7-9b34c8b708c6 | -8.49491 | -48.50004 | 2025-10-17 04:51:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2744e2eb-e9f0-385c-adfa-2a8d99ff5754 | -11.52016 | -49.14121 | 2025-10-17 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c458b50a-73f8-3c83-86e2-87602d3765fd | -9.26318 | -44.35263 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4095a7c-b992-37da-95e5-1d6ecc902377 | -11.18458 | -57.26529 | 2025-10-17 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fac9b71e-bdaf-313f-a531-b75d355f7317 | -13.75478 | -48.22547 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 732976bb-fcd9-3c3a-b43f-8d17e5b6acc4 | -9.14592 | -46.64108 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dd3f7458-2628-35e9-aabd-13978c443ae7 | -10.50145 | -43.43447 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b2d193e5-e3f9-3150-bbf5-831487e04c95 | -10.11523 | -44.56193 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bbb3a68-b07a-3968-882b-c8d0b9499280 | -10.11369 | -44.56522 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057e554c-140d-374a-9007-8ce55c3273f2 | -9.13676 | -46.64709 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83683210-6bdd-36c0-8022-494ec8f3d08e | -14.34142 | -51.43786 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e947d1da-ba98-344b-905c-b4f5f3b5cd22 | -11.45764 | -44.04033 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dd55fef-0d0e-388c-8156-759c0a73aa34 | -10.95664 | -49.76888 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cafca11e-a2eb-38e3-8f5a-69c9169adce2 | -8.39396 | -46.2331 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ad93dd7-5a70-3cd5-8629-14a3ac77a56e | -9.94763 | -45.70899 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce4527a7-1e47-3640-ab30-7d764b42109b | -8.40733 | -46.28639 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| be5f12e1-eaba-31ed-80f3-efc31f934577 | -10.28539 | -44.03816 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 50a6ecfa-4b12-34ba-b576-c079908a8c25 | -9.34416 | -46.90919 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eeba1463-f979-37c2-ae72-d36518ec2441 | -10.05796 | -43.83618 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a65d1d2a-ee4d-36c1-b577-a3a8f3043213 | -12.90738 | -41.82604 | 2025-10-17 04:51:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac9a4479-f2d3-3435-a262-5470568260bc | -9.24139 | -44.37022 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58fe4e97-9ae9-3c1c-9668-12f24cd03ef0 | -7.9045 | -50.38643 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc37a0cc-a4e8-3b99-bbee-801cb31811fb | -11.75691 | -61.07074 | 2025-10-17 04:51:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README94.md)
