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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 182ab848-30f1-377e-b8aa-962f0bf5a67b | -23.98588 | -48.9182 | 2025-07-09 04:00:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba4eda8e-9671-348f-a304-7b7657941ad9 | -24.24357 | -50.73988 | 2025-07-09 04:00:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f709ea99-0070-3414-b6f8-04b9e37449f6 | -22.85755 | -42.97923 | 2025-07-09 04:00:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd8de75d-4c84-3429-9acf-e36edd03b72f | -21.18984 | -48.94115 | 2025-07-09 04:00:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dcd989ab-c9a9-3377-b8ab-51c9989ab550 | -21.05043 | -45.27537 | 2025-07-09 04:00:00 | NOAA-21 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5d8c28f4-13d3-3009-aeab-daf3eb2c27fd | -24.17896 | -53.03968 | 2025-07-09 04:00:00 | NOAA-21 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7ea613dd-bef3-35f4-bb71-e1ae0be6780f | -22.74851 | -43.27773 | 2025-07-09 04:00:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 746d9157-3231-3c40-b2c1-705883ae3e39 | -23.0133 | -46.371 | 2025-07-09 04:00:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7898131d-7327-3368-a4ef-b3a159164788 | -23.59302 | -47.43689 | 2025-07-09 04:00:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83968247-2a4f-3407-9c42-8602e35b0f7e | -21.62799 | -43.46614 | 2025-07-09 04:00:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2389f66-b965-35c9-aeab-cbc051a346fa | -21.44217 | -54.57761 | 2025-07-09 04:00:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0a62485-007a-3251-a02e-1ad881db4ed1 | -23.67247 | -46.89243 | 2025-07-09 04:00:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6824423a-1a33-3066-84b0-f3c75c257f37 | -23.00961 | -46.37025 | 2025-07-09 04:00:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61b48707-42f7-3db8-903c-e8384795090d | -21.53485 | -49.52497 | 2025-07-09 04:00:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 32c0b490-fd93-35de-9cf2-0ab848d7b0c8 | -20.40628 | -48.61653 | 2025-07-09 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db97bc3f-77fb-3d00-b3be-95578b6022de | -21.43 | -48.6473 | 2025-07-09 04:00:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e44f08a-8539-3358-b98e-3a655fe607ec | -21.17981 | -43.98288 | 2025-07-09 04:00:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f8fefa3-6391-387a-9145-6b33ca0581f1 | -22.74913 | -43.27394 | 2025-07-09 04:00:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14fd9fbe-8681-3858-b08b-420e9b0e908f | -21.53532 | -49.52324 | 2025-07-09 04:00:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 35245088-d04b-3329-bdc8-3ac601c70e10 | -21.85932 | -46.62626 | 2025-07-09 04:00:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ba75b0eb-7fed-34f3-8903-b8c8a19da8d6 | -23.4498 | -46.70227 | 2025-07-09 04:00:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4de6999-8c9b-35f1-bb58-0c79950fcdd3 | -20.40283 | -48.61323 | 2025-07-09 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d0b439d-c379-36b3-932c-cdf46212c9f7 | -22.54006 | -48.8145 | 2025-07-09 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f6a6b09-efae-3e0b-bb4e-b11bcb7509c1 | -25.19274 | -49.32703 | 2025-07-09 04:00:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aeb607b5-9717-3e9b-98eb-1603d1954934 | -22.62427 | -47.91708 | 2025-07-09 04:00:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8464f78-0011-31a0-b067-d7cf8cd11994 | -20.99591 | -51.79304 | 2025-07-09 04:00:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a81ea255-bebc-31e0-b7bd-2b6f8de57371 | -22.62023 | -47.91617 | 2025-07-09 04:00:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f0b4132-9069-3c0b-a4b3-7e87ce77e435 | -22.62501 | -47.9133 | 2025-07-09 04:00:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bbf816ad-1378-3a0d-a78c-dbe5f3db2d1f | -23.55128 | -47.63664 | 2025-07-09 04:00:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab618277-3058-3d24-af9b-3eae099caa26 | -24.24113 | -50.74132 | 2025-07-09 04:00:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e7903588-784e-31dc-ae12-6e64df14b8b7 | -20.40721 | -48.6142 | 2025-07-09 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0fe202f-5cc0-3aa3-b70b-08cfec3e4f43 | -24.18114 | -53.03993 | 2025-07-09 04:00:00 | NOAA-21 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70a7bfa6-1bad-3d47-b4f0-d6df4a7e01d3 | -19.33741 | -54.43095 | 2025-07-09 04:00:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f294084c-fbef-39f5-9cfa-8d6f391c8a12 | -23.0122 | -46.36821 | 2025-07-09 04:00:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f7be5d6a-0a7d-3fcf-b5ba-6b06247bfa31 | -21.18047 | -43.97896 | 2025-07-09 04:00:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67664632-f85a-3a5c-ac06-212922558c1b | -21.53429 | -49.52823 | 2025-07-09 04:00:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1667fcd6-0239-32d8-825c-06864a6fb1bd | -27.68567 | -48.75237 | 2025-07-09 04:02:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a14d770a-ed7a-3930-ab40-b347c5f1cf5e | -11.4397 | -45.0923 | 2025-07-09 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3f756618-2a2d-30a8-878b-3982fe47b3f0 | -11.4393 | -45.1154 | 2025-07-09 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 2852098e-849a-344a-a0fe-ac75f9d9d7ba | -11.4201 | -45.1181 | 2025-07-09 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ac5922d9-376b-3a73-93ec-e6468d327d46 | -8.5217 | -43.2593 | 2025-07-09 04:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 4215ab5e-5309-3dda-b820-8b40a5467b63 | -8.5214 | -43.2828 | 2025-07-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 9ae7a5cf-62ae-3cb0-a959-363a2a658505 | -11.4584 | -45.1126 | 2025-07-09 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 2dc1c990-9cd7-3cdc-8bc0-44bb6d02fc70 | -8.5025 | -43.285 | 2025-07-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 230.4 |
| 5e44f230-1cef-3745-9e88-91840ccfdde5 | -8.5028 | -43.2614 | 2025-07-09 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| ea645346-8895-318c-9c40-91732e13f3f3 | -11.4205 | -45.095 | 2025-07-09 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1a8410d8-2182-326a-bbff-9af252ef46e9 | -6.1792 | -48.0494 | 2025-07-09 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 89caa953-3ee8-38c6-ab1d-d41ae0c6491d | -8.5217 | -43.2593 | 2025-07-09 04:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 02c4644d-e93c-3e87-a312-cc474e2b3f2e | -8.5214 | -43.2828 | 2025-07-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.3 |
| efeacaf5-9ea1-3f62-9844-2254d3dbd5d5 | -8.5025 | -43.285 | 2025-07-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.8 |
| 96eddd58-e1e9-39af-a583-942051b2d170 | -8.5028 | -43.2614 | 2025-07-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 8a95d0d5-8ff6-321d-8c1b-419e31dfac06 | -11.4397 | -45.0923 | 2025-07-09 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5b60314f-60d8-3b18-9572-40aa56aa9fb9 | -11.4393 | -45.1154 | 2025-07-09 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d1dd841a-31c1-387c-92fe-27dd12a10e78 | -7.23276 | -43.0732 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5b96053d-059d-3527-898a-998a0b57c39d | -11.43453 | -45.09582 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a77d795d-b030-3b5d-8ff2-92829abb1e4a | -8.37956 | -43.94411 | 2025-07-09 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b9c1ec1-8b36-3680-a88d-cd383e4d72b9 | -8.14704 | -47.62829 | 2025-07-09 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 845c48f9-41ca-3c69-8f92-eddbe468f6ef | -8.51058 | -43.2919 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 43bb331d-b0f7-3825-a1d1-71b896a9efef | -11.42843 | -45.11303 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 747b3a67-358b-30be-a7d6-27b72085f71e | -6.3901 | -43.04068 | 2025-07-09 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46231e68-09ae-34e9-9bab-57e0165897eb | -11.41788 | -45.11497 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42eaf6ce-0efc-35a2-89d8-ca4640012fc2 | -8.27527 | -42.27853 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04c40b11-bc6c-3998-afe7-f6d17b40bbb5 | -9.28944 | -44.84012 | 2025-07-09 04:21:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deba9b49-9b65-3309-ac98-62c8f287b320 | -8.50257 | -43.27535 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 86f8a35d-3f0d-3ade-adae-7006644cc559 | -6.97935 | -47.08281 | 2025-07-09 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5e3fd08-17ff-30a7-958c-4f7a2fdcf08a | -11.67542 | -43.77665 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0bbce0ed-96a4-303a-a2f7-f2724641e1c8 | -11.42231 | -45.10842 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a1742c6-0644-3976-a7fb-7d417cb22adc | -8.502 | -43.2791 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| b4bb9491-458c-32b3-abe8-6d863c86b7ce | -8.27884 | -42.27908 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c75b3246-5903-3dff-bc32-3204b1fcb98a | -8.23303 | -44.93036 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c8b8f5b6-78f4-34d0-abe4-23408e36ef92 | -8.31423 | -55.1104 | 2025-07-09 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e82e75-d500-3d85-8964-b5bf2036f3dc | -11.45141 | -45.11293 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea996618-44af-3da8-b566-4ad358efea96 | -8.65312 | -48.49601 | 2025-07-09 04:21:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ae92b1c-18e4-30b8-a1dd-1900892a1912 | -6.68161 | -46.30498 | 2025-07-09 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae09b4c-f700-316c-b3b1-e188ee30b67c | -6.9822 | -47.08721 | 2025-07-09 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7ca0ebc-011e-3fe3-86c5-57a8343d5c44 | -11.43175 | -45.09174 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4aaed968-a805-3418-87ee-85b383163ec4 | -11.41898 | -45.10788 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70bc07a5-722f-37ce-ad43-03e08ce59ad9 | -5.583 | -43.58088 | 2025-07-09 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55481b9f-9de5-3056-a116-7fa7b3d25f32 | -11.43732 | -45.0999 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96e8578b-5607-360a-9dc9-f165b9de6e4a | -11.67485 | -43.78048 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 295f72df-cfc6-3499-9c28-a044ca2267d3 | -6.67879 | -46.3008 | 2025-07-09 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bdf8010-27e6-30ae-a1fb-4c3969504a8b | -5.23058 | -45.21663 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5b68293-5e66-3349-8dc4-1e379a9e7428 | -10.62832 | -51.58942 | 2025-07-09 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb90afd9-f8f4-37e3-b026-9b85a980db6d | -7.23618 | -43.07373 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c7d965e6-fe59-38f6-83ea-1ad0c5ed227e | -11.46197 | -45.11097 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd76f930-67b5-3229-a72d-dda7df31e396 | -11.43697 | -45.11791 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f643eed5-9bba-3363-a4d8-b31d9fbacf20 | -6.93881 | -43.05529 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a810c014-d7d4-3fec-ab7f-d3ef2f453fb0 | -12.06007 | -43.51122 | 2025-07-09 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee5939ec-2a5d-3f8d-9b67-98db9beeb323 | -10.64603 | -44.48908 | 2025-07-09 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c36b018c-fd06-3d4f-b15f-1f5fcbbe5b4b | -8.22916 | -44.93332 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58903239-9f4b-3a22-9287-60172f0ba791 | -6.85782 | -42.78852 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37c6fa0f-78bb-3eb2-bae1-f18e01f5754b | -11.43509 | -45.09227 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2434bd67-5139-3141-b451-26d91849ef7d | -11.44698 | -45.1195 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18f305f0-e99c-3fe9-bf4f-4a27ea3226d1 | -8.23277 | -46.95494 | 2025-07-09 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a812310-dca7-365b-bc45-9323fae5dcbf | -6.62487 | -43.35118 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc7ab886-ff33-37ad-b5cb-ddf4109e81a0 | -5.59381 | -45.03795 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86312412-4ab2-3aee-b34b-f8fe4840036c | -10.18137 | -51.1507 | 2025-07-09 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93be085b-16cc-3aa2-8dfa-6b72f8b9571c | -5.78105 | -43.6111 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d61b12ac-2ce9-3a1d-9cf2-cc75c098b51b | -6.23836 | -43.36571 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c433266-1fb4-3d07-aea1-c3f2c37f4c35 | -7.22991 | -43.06897 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README13.md)
