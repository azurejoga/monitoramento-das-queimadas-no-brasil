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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 264e30eb-f8a8-3867-ae8f-7e03cccb8e17 | -6.0787 | -35.69136 | 2026-10-05 15:54:00 | NOAA-20 | SERRA CAIADA | RIO GRANDE DO NORTE | Brasil | 2410306 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0261d0d3-0d2e-3f14-9eb1-87f120b3c7de | -7.82744 | -45.3217 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| f659d8eb-59f3-37d4-92a5-20ac1516235d | -6.70014 | -45.23876 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 41569b08-7b10-343a-bfc8-bc4afc933e85 | -7.82786 | -45.30624 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 4e91cdfb-e2ed-3f43-a134-6798f49ae717 | -6.87157 | -40.24023 | 2026-10-05 15:54:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ac250152-3b50-36eb-b5fe-09189669fca8 | -7.48339 | -42.80351 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 34707ac9-1812-3859-b330-2b6b751a0b0f | -6.69246 | -40.9996 | 2026-10-05 15:54:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f6cb26b0-d443-3f49-a6f4-fd7f10f21573 | -8.43317 | -39.54657 | 2026-10-05 15:54:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 699cdaf7-b20a-3240-8498-3605be7cb43c | -7.48803 | -42.80005 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 91b440e9-2c4a-301e-a11e-0ef34cc42201 | -9.82166 | -44.79723 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 227d62cc-d98e-3b74-8be2-a4fe70a66dd4 | -6.60276 | -41.57231 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 4ebd357b-f6b7-3b9f-8449-45afb2a8d9fb | -7.09921 | -42.53994 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8541d299-5a83-34ca-9d15-e46d99c0bf44 | -6.73487 | -44.92227 | 2026-10-05 15:54:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0429177d-78ec-35f4-9384-1a3651a9eb47 | -7.85489 | -44.14276 | 2026-10-05 15:54:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2442ced8-9b7f-37ca-9b4d-a5dd0cc50e1d | -6.3226 | -43.34433 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6cbf6ffa-0056-3229-9bf4-7594f705a27c | -6.60665 | -41.56707 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 4911dee8-61ae-3508-b2ac-7f104d2d6315 | -6.37379 | -43.6373 | 2026-10-05 15:54:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 201f6973-29ff-33e3-b630-75147d0068da | -9.87173 | -44.81308 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dacf7732-b6ee-3a88-acf9-3aa606032607 | -9.94026 | -45.50555 | 2026-10-05 15:54:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a94a968d-9d49-3c89-bd19-ac4750cfeb42 | -6.46388 | -43.47795 | 2026-10-05 15:54:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c029f04a-ed50-3324-bbea-d7df0625f161 | -6.90267 | -43.66971 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| fece3fae-a999-3e9f-83aa-d8246b856a5c | -6.93082 | -43.67922 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f3c292a9-0e32-384a-a35a-d66f2e8667e6 | -6.6159 | -41.76696 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3a4e15c9-40ff-3ec6-8cea-a2f851bf044b | -7.82903 | -45.31486 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e7177f48-84ff-3cf2-8c12-465e2b27a654 | -7.82524 | -45.30446 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2644d204-b563-36fb-bb2c-bebd47a9ac9f | -7.3002 | -43.79261 | 2026-10-05 15:54:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95a45747-43f7-3983-a0fe-a308d0eded36 | -5.00099 | -42.72734 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98faf9e6-dfac-314e-a645-5edd6ac1e678 | -5.93836 | -41.34585 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bc4bed0d-25e0-3558-a9e3-a9a0c2d02686 | -5.44357 | -42.64457 | 2026-10-05 15:56:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| eb5730d0-fae3-394e-99d3-7625796f261a | -3.65276 | -39.43642 | 2026-10-05 15:56:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 768e9df7-0c79-3436-b195-6bae77413401 | -3.28785 | -42.2613 | 2026-10-05 15:56:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6329cced-049c-3489-9e0c-3d3171be49fb | -5.12227 | -43.99269 | 2026-10-05 15:56:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8712ea03-b406-3967-9ca3-5ae33eb6970c | -3.35022 | -42.90703 | 2026-10-05 15:56:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e1d8ddc8-0c7f-3d4d-86c3-98eff5c0dd6f | -5.74461 | -45.05625 | 2026-10-05 15:56:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46abed28-42f7-3206-b940-2888549e1a84 | -6.04186 | -45.22976 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 130f5e35-a944-3422-80c8-973dc7a02737 | -2.05381 | -48.22731 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| dffa8ed0-7a89-3c39-b880-eebd091cc968 | -3.93637 | -40.73288 | 2026-10-05 15:56:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 3809f39c-6a83-3cda-80a7-43f23a24625b | -5.19016 | -37.04581 | 2026-10-05 15:56:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2dd1d0ba-74a7-3387-b7bb-44af587cbf06 | -2.05444 | -48.2219 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8e0ac95f-38e3-3485-ad7c-85a0780d663c | -4.80828 | -42.15016 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 295.7 |
| e8e22f00-bc2a-3d92-85cc-f72115ee0d74 | -3.72361 | -45.40142 | 2026-10-05 15:56:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a82a08a8-275f-3c97-828d-1e25d0759f8b | -3.16817 | -41.40319 | 2026-10-05 15:56:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 63362d80-60ae-36eb-acf6-28862fd0e929 | -4.80302 | -42.14609 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 9bacbff0-34b1-3dbd-add7-e75e06f39f6a | -3.17302 | -41.40652 | 2026-10-05 15:56:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ff6c0ac5-e79f-39a1-9e9a-1ed109645b97 | -5.14309 | -37.4105 | 2026-10-05 15:56:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6d9b68d3-de95-3f84-9392-6c2e0ace5e7d | -3.91615 | -44.14424 | 2026-10-05 15:56:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fd14d1f-48a1-393e-8001-fcc4d0ef7dd8 | -5.19224 | -42.72942 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d0b85d25-96fa-3d23-8f1b-11b46b5fc49b | -3.77117 | -39.84311 | 2026-10-05 15:56:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 79.7 |
| fe4bc360-86ac-3510-9876-b61f72086076 | -1.40613 | -47.22342 | 2026-10-05 15:56:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 93c3693e-1d79-3363-abaf-a41607898a91 | -3.37014 | -42.97673 | 2026-10-05 15:56:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3747d021-ae8b-3734-ab2d-6e35de0aa772 | -3.11697 | -44.28728 | 2026-10-05 15:56:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cc73ef0c-42d5-30a7-89fe-91173ce41e25 | -5.38973 | -42.95499 | 2026-10-05 15:56:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 6d60376f-a347-30ae-ad37-11569fbc45ef | -5.71702 | -40.1245 | 2026-10-05 15:56:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5faba38b-710a-3883-bc58-dd259ca47ffe | -5.84537 | -45.01483 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e47c94c3-9555-3920-a22a-b02e7c1aa316 | -3.36748 | -43.38348 | 2026-10-05 15:56:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8cde0985-bc38-3924-b31f-e599b0bc4109 | -3.16758 | -41.39925 | 2026-10-05 15:56:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 551167aa-f531-3ce2-b389-03790d2fd908 | -4.60033 | -43.48227 | 2026-10-05 15:56:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ec7de55-e8ca-34df-9984-5c351c54baa1 | -1.10546 | -46.64416 | 2026-10-05 15:56:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7028c81-4961-3ca0-b306-aef7bd631683 | -4.57169 | -39.58915 | 2026-10-05 15:56:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 86bcea86-ce55-3649-a0e3-768adc0a8f6b | -4.35374 | -43.82948 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca36042c-45d7-31d6-be2c-0d5a9e20efda | -3.20689 | -42.44021 | 2026-10-05 15:56:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cd8012bc-fc65-3121-9bad-40d9f6742801 | -5.84928 | -45.02372 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7f846fe2-bcbf-331d-9174-6313c23e06ba | -3.74195 | -39.5416 | 2026-10-05 15:56:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 47a3dfd1-2ce6-3044-b887-23cdc139c4b5 | -3.74126 | -39.53694 | 2026-10-05 15:56:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| b2f466ad-cfbb-3e68-bdf9-2a91a5ec3fa9 | -5.24836 | -43.15277 | 2026-10-05 15:56:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f25eb0b3-1569-3dc0-ba97-df1815b491fe | -5.0353 | -43.74907 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42157ae1-4862-3f76-9c4d-e23f640ef2e5 | -2.8952 | -42.39581 | 2026-10-05 15:56:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb5d3cf5-1861-3ecd-a151-e4332b86b50f | -5.84874 | -45.01972 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8a32ba98-abb5-37d3-b1ad-36079666ce60 | -2.93863 | -40.87444 | 2026-10-05 15:56:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f8cd886f-7528-36d3-8700-f87162349559 | -4.80236 | -42.14137 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 631c66bd-b82d-3c83-b0d4-caee4e901759 | -5.03832 | -43.74917 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1a445213-dc80-303c-a934-906cfc207295 | -3.2789 | -43.08704 | 2026-10-05 15:56:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 12a07b5b-741b-319c-ac58-8dc2162edc67 | -5.84648 | -45.0227 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 64830552-0e54-3bda-9e4b-855811b8fee4 | -3.05224 | -44.35893 | 2026-10-05 15:56:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21f664d7-af19-3e40-93dc-2b8824cca68e | -3.57585 | -41.24038 | 2026-10-05 15:56:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 2d456878-4ed2-3338-a02e-84c51d835598 | -4.56781 | -39.58958 | 2026-10-05 15:56:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| f56cb1fd-60f5-3a33-9637-73a45e38effd | -4.15087 | -38.48148 | 2026-10-05 15:56:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d5c9a069-cc1a-3c42-b0c6-3ccaed5488f7 | -6.32901 | -43.81602 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 10193697-091c-30a2-bbcb-d5e823d64891 | -5.83407 | -45.01671 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| febf6f9f-3f84-313b-89a4-cdcf82d2bb6b | -6.2082 | -44.80183 | 2026-10-05 15:56:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17f459fc-1639-362d-96d6-b8f882ebb141 | -4.99689 | -42.73027 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22ede16c-8cf8-383c-a824-fded08f318c0 | -3.34232 | -44.58665 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 69188d47-faf2-38db-980c-56bf09c1b65c | -5.84138 | -45.02756 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 565f01cc-6501-372c-ad6b-e222c13fec95 | -3.72416 | -45.40523 | 2026-10-05 15:56:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bed9cf73-b341-3c96-96f7-45312e0fefd3 | -6.32884 | -43.81738 | 2026-10-05 15:56:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f6863289-943c-36d4-9678-4b83b5bff6f6 | -3.42192 | -42.56361 | 2026-10-05 15:56:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1d181990-7aaa-3511-9405-e880a6fe7e4d | -5.83917 | -45.01183 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 20d205c0-8e16-334b-a3f5-9c51b6e8d4d8 | -4.5205 | -39.08136 | 2026-10-05 15:56:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a625aa21-f60c-38ad-b95b-47042f4233e3 | -3.90922 | -38.66089 | 2026-10-05 15:56:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9908f032-9931-3ff2-ae23-038924c7265d | -3.33839 | -44.5863 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 632f8650-81e4-3acd-ba07-dac1f02b4b25 | -4.24768 | -44.81721 | 2026-10-05 15:56:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39fe3186-00f4-369c-922a-26291607ce92 | -6.1842 | -43.38328 | 2026-10-05 15:56:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9dacbba2-2dcc-3ce8-997c-14ea3a14127f | -5.84593 | -45.01875 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 44d6565e-d053-32bc-9351-d217feb87d1e | -4.8027 | -42.14346 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c52aea93-8167-347d-b399-c141a3ebb578 | -4.80762 | -42.14543 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 1d1c20ba-8082-3ed3-b299-64e128ef8829 | -2.82445 | -43.68671 | 2026-10-05 15:56:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a9badff-4549-3fe6-9a66-ddc659b3a411 | -3.25861 | -44.63512 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4a6c084-97db-36c7-bf11-bdbd51cd3eeb | -3.56075 | -39.91013 | 2026-10-05 15:56:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 796a990c-b9b8-31c7-8948-704e1655d6e0 | -4.29832 | -42.18449 | 2026-10-05 15:56:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1184c6f3-a332-3849-b1f9-df41093e87c0 | -4.36353 | -43.93426 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |


[Clique aqui para ver as próximas entradas](README76.md)
