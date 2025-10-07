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
| 72175095-6811-36da-a6bc-4c2ef03f356b | -8.18797 | -50.30238 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d48dafd8-115f-3e0a-9557-443bfb61fb29 | -8.68416 | -47.07668 | 2025-10-07 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e36c441d-20c4-3ba3-a4dd-a2e541c4a226 | -8.45415 | -47.24687 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d06ae6a-0125-3d12-9e2d-97bd5d49f4d3 | -8.8879 | -47.66825 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 503a7c7f-7e59-39bc-86cd-2439196f4784 | -5.45882 | -45.27828 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c9579f8-1a65-31f9-b847-5699070ec341 | -12.24162 | -47.02275 | 2025-10-07 04:08:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeb33791-669d-3267-9c7e-48f6acaa60d7 | -9.27528 | -48.32183 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c1b236d-9e39-37bd-a367-8ba918fb6543 | -10.44965 | -50.41076 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7018f56-bd99-3213-a620-51e4f2c55ffa | -7.00946 | -42.78969 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 960c7028-b5ca-3954-960b-3f14310c47c1 | -12.61607 | -44.75361 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06440b2f-16f3-3cb9-b032-3853c478f522 | -7.69246 | -42.41102 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8e7b4e21-f055-3d57-8f5c-7812affa0232 | -10.03754 | -48.28991 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5aeb9acc-ec64-3414-8e53-17b7f3989adf | -5.55202 | -42.68164 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 94a9ae41-7faf-3291-aa8d-39660a920a40 | -9.039 | -50.59217 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 72269aae-0c02-343e-93a1-9f6bd02ff799 | -8.5496 | -46.26086 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0faae5a-1328-30a9-b2c2-d824f16056c1 | -6.45337 | -44.57941 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 38a1c389-9933-3ac4-98ce-a73159484a03 | -10.18249 | -45.536 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd9617c3-a8e7-3d2e-8371-91a80571523e | -8.58244 | -35.14371 | 2025-10-07 04:08:00 | NOAA-21 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2cc02ac0-97cf-3860-bb85-6c0157b2e577 | -5.26905 | -44.09355 | 2025-10-07 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36c71758-61e4-3e06-9a47-5f17fe7d979a | -7.52082 | -49.9057 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da99cacd-ce1d-363e-b4a0-589963aecad6 | -11.03014 | -50.92118 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f81f9f6a-c7b3-32a3-bc6e-01c99593277b | -11.71646 | -45.37439 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5de53220-798f-3c01-8039-a31c9461dc06 | -5.49148 | -43.47331 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7014f63-bbfd-3fcb-9bcd-c8d314657420 | -6.07158 | -42.56413 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9bc02b9a-2611-38c5-87e1-60da7d03a5bc | -5.56157 | -42.6649 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8734ba1d-42af-3712-94b2-46e6b8ceb199 | -6.98709 | -42.86595 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d96facc9-138e-3924-89c3-b6b269ac2578 | -10.25938 | -44.37447 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1961da98-667f-329a-bce9-19ebdcf21763 | -6.71652 | -42.85237 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 84e4ec40-0db8-3686-87e8-4e95211a93cd | -10.95585 | -51.18544 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59b06f27-14fc-3d0c-965c-c0760032d267 | -8.50087 | -46.32234 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d2a23db4-5dd9-31eb-9bac-15259e5d95a9 | -6.71729 | -42.80834 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e32c651-7ddc-344c-9d88-db65ce4433f7 | -11.74691 | -43.29026 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e872c321-7359-3c37-aec5-04525ed8b87a | -6.23695 | -43.27449 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0b611b31-405d-35a7-a4dc-f5a22707e4fa | -6.53262 | -55.04125 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e935d110-e6a5-32a7-8e3e-ae341565527e | -6.6987 | -41.38913 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e29a7d0-3406-36e6-9803-1fd8a15049c4 | -10.264 | -44.36752 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0fe2f51-d2c9-3f6b-8d69-2b210eba977d | -5.95905 | -44.33799 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd81f6a7-d410-3845-bc9b-2533209c05da | -6.6517 | -41.97488 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f74914c2-26db-38eb-8954-e33951314524 | -8.17743 | -50.30347 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d237e94-749c-3d73-97d5-b759de7581be | -10.23581 | -52.69908 | 2025-10-07 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5583babe-478f-3ffa-a73b-4e64898d022f | -7.5988 | -37.80549 | 2025-10-07 04:08:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 274c36c0-7799-30c1-9ca3-d9af73819387 | -9.03849 | -50.59497 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 93618bd4-8cec-3c54-b060-8659e00e82c5 | -5.46291 | -42.90311 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7e6324a5-a0fa-3e7e-8b71-5f134ac7288a | -6.6507 | -39.31192 | 2025-10-07 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fb97d8b-2803-3b77-b14d-7793739281bf | -8.27085 | -43.82452 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f460ed1a-b2b9-3d7d-884f-9eeb314674d3 | -7.03172 | -42.757 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7c32ef8-c77d-306f-a2dd-d863bfa9859f | -6.65554 | -41.97195 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c6f3846-b519-3922-aa56-edcbfa6c0d1b | -11.67455 | -45.30254 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be5368c1-b67d-3fe6-9627-3bfc8602fe21 | -5.50194 | -43.08014 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 957ae351-8dc1-3eeb-b41a-2f13a66d0bf5 | -5.49178 | -43.0785 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7e2f6fed-4f7d-3905-ba3c-6fe1b45a8ec9 | -7.29454 | -41.97835 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b43fe3d-d5d1-3111-987f-741b975d594f | -11.22225 | -47.77731 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4c86339-1349-3ba0-9fb9-a1c16377bb5a | -6.64622 | -41.98817 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d96365e2-e6b2-3afa-91f5-96c6c1618b7b | -11.66692 | -45.30528 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17187a9d-7b42-38a1-b951-8a08ed3153f5 | -10.22672 | -48.17913 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c57c5b1-b366-3fb4-bef5-81f10529c5d6 | -11.0468 | -44.78556 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b4da027-7ef0-343a-8fe7-2051f22fc96f | -7.03228 | -42.75348 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23f2fa5e-1c7f-3eac-80c2-6dbf8c1abcea | -8.5418 | -46.24123 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 35442cb6-3eb3-313f-9127-1385845678db | -5.14871 | -49.84653 | 2025-10-07 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4235a89d-76e7-363b-8e29-308829cede28 | -11.15184 | -47.75383 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e496d81-fe8e-39c4-9d09-9ff82a60a8ea | -11.83825 | -44.91108 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d63a399d-f3ca-38cb-ba2b-40d7ead09f34 | -8.50294 | -49.13446 | 2025-10-07 04:08:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8fa9bd3-9812-38ce-b7a7-d5b818e13ebe | -10.27083 | -44.36862 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6233748f-d004-393d-b1d9-75c78b32e900 | -6.66671 | -42.76044 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed5a5994-dfdf-315d-92a0-eb7f19c85695 | -11.64812 | -46.87448 | 2025-10-07 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0905f6b9-cf20-3f8a-8165-b2cf513b9af4 | -6.08308 | -43.46571 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67ecea8d-1192-33c7-804e-eaffee6d0f79 | -8.48508 | -46.27598 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 071f13d7-3c52-33b1-bd51-95e83ae06a9a | -4.87411 | -50.90134 | 2025-10-07 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a839db-653e-33d6-930e-629c7a0d2378 | -11.24509 | -47.91333 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98642528-30f2-3c2c-b2f7-58fb7731f116 | -8.95676 | -44.59879 | 2025-10-07 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcec066d-3004-3d43-b439-c3b5f6b35e72 | -6.32043 | -41.61143 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d65fd8d-afc2-33af-8707-a0f1796aed10 | -8.49381 | -46.341 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f54cdb63-715e-33d7-83c3-de25e93ed945 | -6.36111 | -44.61149 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3333850-66e3-39f0-a98c-4717911b4080 | -6.10395 | -47.30986 | 2025-10-07 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c083eca-aab7-3010-bf98-2a995d8889a6 | -11.71767 | -44.29782 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 287bb8b4-181b-3217-b677-2c1cbe569d99 | -11.71517 | -45.44769 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db64e98-bb93-3ca5-a52d-9e2eadd5b0c4 | -5.77076 | -45.74463 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6eedead-68d4-31e7-b430-cb1209c3ac75 | -5.65258 | -43.18968 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 254f33fc-1a0d-304a-94a2-55b69eb4362e | -5.16759 | -50.64598 | 2025-10-07 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f54f88fe-0daa-3d37-aac7-7c9ee323a615 | -8.27026 | -43.82819 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5a89b3c-c992-3c0d-9a26-77caba1192c2 | -11.49719 | -44.97314 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0987ec09-0326-3a48-948e-68722a6340d4 | -5.49237 | -43.07485 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 176cf0fa-a27a-3aa9-b61a-da301452a138 | -10.87572 | -51.02999 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b83505d-b47c-3b99-8cfc-fe2a4c7641c3 | -10.37239 | -48.14064 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54ffa648-a9df-303b-a6ae-1d9f61680630 | -5.50312 | -43.07281 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e7ea431f-3696-346f-973e-527508273b56 | -5.1538 | -49.84751 | 2025-10-07 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1f7a40d-64ff-3bd5-9d1d-2ec291e4fe18 | -10.41338 | -45.39038 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9b1bd9d-747f-3374-853e-0242580429ab | -8.48283 | -50.21099 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 240b4a0f-7bfa-360d-9e8d-4ce1712bb239 | -10.39766 | -45.37523 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46451ec2-3efd-3149-a2e7-3635fc247ba4 | -11.6734 | -44.26085 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270e180a-fa16-32e2-b1c3-2522be6220d4 | -6.33308 | -41.61693 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 05e98ff4-850d-3759-9415-bd93b22b4865 | -6.65061 | -41.98178 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 57e06821-fa9b-3d8b-a245-99eddbd97ba8 | -10.02764 | -48.29669 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 022acc72-f823-3681-82a5-6e8c4e08a5a6 | -6.70055 | -42.8492 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a5c73d0-eb60-3529-9925-8f3a1d50e1cb | -7.67868 | -42.58378 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49617f4d-1f79-3f9b-925d-2842b4c3786e | -4.55677 | -46.67892 | 2025-10-07 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb96c7a7-af5b-3ca9-a392-65459123037d | -8.48655 | -46.29057 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ea4ee7e-1edf-3995-96ee-adc32aeab0f7 | -7.62258 | -43.06602 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3e27c235-e781-349b-b292-d73d517ed939 | -7.56514 | -43.97317 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48cb044f-02ae-3970-a4f2-3536d18d08ab | -5.70108 | -44.83524 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
