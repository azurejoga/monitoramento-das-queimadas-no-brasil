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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d556b32b-6ca7-3f7b-a0f7-f3fb7d322c44 | -2.6683 | -48.7981 | 2024-11-29 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 1c3b2ef2-f59d-388d-8f64-5b5e7b7bc513 | 1.3719 | -50.6205 | 2024-11-29 14:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 007bf5dd-0c3c-31d0-8527-d503df4f6cb4 | -2.6498 | -48.7986 | 2024-11-29 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| cee087ea-9ba4-32a4-a5ee-c890ec45f393 | -2.8426 | -46.7973 | 2024-11-29 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| af8e2c9d-7ccb-3e1d-a43e-5e9509f9586e | -4.0866 | -50.0232 | 2024-11-29 14:30:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ae894c79-710f-3035-8daf-cc31ac664aa4 | -4.7003 | -46.6722 | 2024-11-29 14:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b3f6dbe0-bc58-3b2b-96c7-b81e529529b0 | -1.8324 | -50.6551 | 2024-11-29 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 89e05ebb-2263-37eb-83b6-58f3307090b2 | -1.6181 | -47.5065 | 2024-11-29 14:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ff3f0079-5974-3dca-a31e-bbff6d5dd3d1 | -2.8851 | -45.5073 | 2024-11-29 14:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 433e7378-94c5-36ea-843a-4346f3352c7c | -3.3088 | -50.3671 | 2024-11-29 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| c29576c2-6264-3490-a932-feeb9a68f5e6 | -3.6135 | -41.6328 | 2024-11-29 14:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| b9c17d72-3c9e-3450-af97-e7cd3867de62 | -2.5718 | -50.0103 | 2024-11-29 14:30:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3ea3e60d-83a5-3754-919c-af33142bca56 | -1.5685 | -53.8338 | 2024-11-29 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3ccdfaea-a6eb-309c-87fe-9d77249f42ef | -3.4531 | -43.5474 | 2024-11-29 14:30:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d143d7b8-b7a8-309f-a6a5-3eb29899381c | -1.9698 | -47.4342 | 2024-11-29 14:30:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| a60b1a3f-673b-362e-a657-efec2d2cce0b | -4.8527 | -41.2687 | 2024-11-29 14:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| cddc4d4d-dfda-387d-bddd-b6bc2f147b41 | -3.0673 | -42.3955 | 2024-11-29 14:30:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3fb720d0-61ec-3800-b9ce-0823eea82dba | -3.2903 | -50.3677 | 2024-11-29 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8c57a9b0-0d6d-3387-bce7-c58c1c8c0108 | -17.6453 | -57.5874 | 2024-11-29 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| c0c45928-3fd2-34f8-9b48-af7f9f5ba3ee | 1.3535 | -50.6207 | 2024-11-29 14:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f34832e9-e838-391f-abb9-e3ddaf5348e9 | -3.6584 | -40.4203 | 2024-11-29 14:30:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 94.5 |
| dfcac72d-6c29-30ba-a708-eb5e45c346ad | -3.7128 | -47.1379 | 2024-11-29 14:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 95550ce9-8f32-3180-8d7a-4e7783ac49de | -2.1766 | -46.3975 | 2024-11-29 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| bae49cd8-1daf-3e7f-9ce4-c6d1eafca319 | 1.2171 | -55.9471 | 2024-11-29 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4aca4d8c-fa75-3bb1-aa46-3823a35fed7c | -3.6942 | -47.1387 | 2024-11-29 14:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 353.5 |
| 988b4b0c-912d-344f-83fd-69bf66bf9d45 | -4.6817 | -46.6732 | 2024-11-29 14:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| bc73abec-366e-35fb-bba3-73adbadb3ad2 | -2.8611 | -46.8186 | 2024-11-29 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| fa6def4c-a40c-3a3f-ad53-1b9f57398ff0 | -4.0681 | -50.024 | 2024-11-29 14:30:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4c8e09b4-d05a-31b4-b3a7-516d62eb258b | -1.9742 | -45.8918 | 2024-11-29 14:30:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| b5504a68-1b40-3452-9ba5-041aa9b68f1d | -3.2515 | -46.6065 | 2024-11-29 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 6e43cc65-f22c-3690-9890-51b0d779aa52 | -18.2645 | -56.0184 | 2024-11-29 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| c81502aa-6135-361d-a63b-2b980039d65f | -1.4016 | -54.9558 | 2024-11-29 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7297bc5b-f812-319a-875e-8cb020f00e70 | 1.6476 | -50.929 | 2024-11-29 14:30:00 | GOES-16 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| fd692ba3-65c3-37a0-960b-81694dd797a6 | -4.1761 | -44.2716 | 2024-11-29 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 99942da6-77bc-30bc-a398-47b0e755256e | -3.6027 | -40.3254 | 2024-11-29 14:30:00 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 5b7520a5-aaf4-37bb-951e-3fb8e9e5cf55 | -2.3073 | -46.128 | 2024-11-29 14:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 57374418-8973-3c53-81de-719fc1d0e408 | 1.4917 | -55.964 | 2024-11-29 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 51fa2499-72a2-37fe-92a5-ab132c0fd954 | -3.7406 | -42.269 | 2024-11-29 14:30:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| eadae172-4110-3176-b878-29a0d8193dea | -3.41 | -44.6283 | 2024-11-29 14:30:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 5c6e76aa-71e9-3f50-8946-2ec5206979a8 | -18.2221 | -56.1702 | 2024-11-29 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 130f91f2-5411-31e0-bd11-8bc5c81b4e86 | -0.7446 | -51.7873 | 2024-11-29 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b9058b21-1be5-3131-be0a-dd43d4456318 | -1.7507 | -46.2523 | 2024-11-29 14:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| abc8eadd-db56-3e6e-ac86-0823832a88ec | -3.4102 | -44.6055 | 2024-11-29 14:30:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 414fdd0a-d57f-3773-8a77-dde9eae42226 | -0.616 | -51.7058 | 2024-11-29 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1f21ea2a-0e37-3aa8-9a25-23313459d1b2 | -3.1787 | -46.2995 | 2024-11-29 14:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0134f136-2391-3866-b8cd-05f14ce629cb | -1.9699 | -47.4124 | 2024-11-29 14:30:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 9f831d2d-66d4-32f6-ae71-6620174717b1 | -2.8425 | -46.8193 | 2024-11-29 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| a64849b6-13fe-382a-930f-343bb844d3c0 | -17.6457 | -57.5668 | 2024-11-29 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| c9479d9a-fdd9-3555-9b7f-6cd4f8dd2560 | -1.6235 | -53.8733 | 2024-11-29 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0f4bbf64-edc3-3f59-bfad-ecf6f822f5a4 | -4.164 | -46.1902 | 2024-11-29 14:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4466d0b3-e7f3-3283-8c72-309e58d090a4 | -2.8424 | -46.8413 | 2024-11-29 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 01fd66f8-9f1d-311f-afd5-c9f63bcb6e69 | -1.3834 | -54.9361 | 2024-11-29 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| df9e34de-650c-359b-9819-20118bb80db8 | -3.6133 | -41.6568 | 2024-11-29 14:30:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| b54bf825-d181-30f2-9bf1-7a647fa270b7 | -3.6943 | -47.1168 | 2024-11-29 14:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 167.9 |
| c20773a9-2752-3f19-ab44-c28774e07be4 | -3.2396 | -53.9216 | 2024-11-29 14:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ba9a5e5f-1295-39e7-945e-ae0eb6d80955 | -4.4222 | -43.7516 | 2024-11-29 14:30:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 19cdc123-b75d-3917-975c-890c6e9a3336 | -8.3108 | -44.951 | 2024-11-29 14:30:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5bd9893b-4526-3344-89e7-26f92fa67620 | -1.8139 | -50.6554 | 2024-11-29 14:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 30bece35-2dde-3bf0-84c7-c9b63516c769 | -4.1574 | -44.2726 | 2024-11-29 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 5f2c4724-bd57-3548-89ae-2dfc971193c5 | -6.7782 | -44.0876 | 2024-11-29 14:30:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7d9ea4c5-0ccb-35c1-be56-3dc7be1d7c3b | -2.9399 | -45.7293 | 2024-11-29 14:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fb4cf1b6-a0bb-3b08-937c-2b8ebe207caa | -2.6684 | -48.7767 | 2024-11-29 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| f580f233-323e-3d1e-8053-c31406ff417d | -3.3041 | -43.5078 | 2024-11-29 14:30:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a03b77f0-94ab-3623-b9bf-d3dcd9e879e7 | -0.5608 | -51.7061 | 2024-11-29 14:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.2 |
| add09162-7310-3559-885c-0092d0544c19 | -2.6499 | -48.7772 | 2024-11-29 14:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f853268d-8e05-33c7-b2a7-8681655f0282 | -3.7129 | -47.116 | 2024-11-29 14:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |


