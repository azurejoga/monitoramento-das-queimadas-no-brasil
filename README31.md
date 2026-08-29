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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e78e6674-023e-32f6-bf6f-5aac4fffef82 | -6.94211 | -58.95434 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 903359c9-0717-3557-8a50-a8afa9109d37 | -6.62727 | -43.74083 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0c79bbd0-8d40-3a6d-bfd4-21a68c519b85 | -6.95643 | -58.95736 | 2026-08-29 04:32:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77499e13-0df4-3ad0-940c-14d4094f813a | -8.98904 | -50.78874 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1112c366-ed61-3a7c-b0c1-f49429d7b52d | -7.34165 | -55.16373 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03c74134-44d1-3bd9-a87f-002ee4e91237 | -5.41832 | -43.18888 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c04d4f94-54f5-31dd-9b54-037b5d66af70 | -8.9834 | -50.78775 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5981688c-dfba-351f-a0ea-c6f06323d42d | -7.03953 | -45.54423 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19e64b7-0b88-3043-971a-0d6fea58bd3d | -5.98054 | -43.74572 | 2026-08-29 04:32:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9eca2b1b-2ca3-3ea9-8452-c96e63f2c080 | -6.94985 | -45.23315 | 2026-08-29 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20fe065-869d-3533-8a1a-c337b239d5d3 | -5.41776 | -43.19247 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2c9b61c-edd1-37d2-a025-f8fd178463e0 | -10.33706 | -49.97165 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34c8bbf2-0ce3-3444-a5e5-e06e76abb355 | -3.82392 | -52.41007 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d06f1593-265c-3fa4-b465-aa1b8a4ff469 | -7.29549 | -49.97247 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0183bc48-cf0d-395a-ab65-721aafde0240 | -8.98755 | -50.78841 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0f87e9f-fc29-3a26-aae8-2c81749021d4 | -8.66257 | -49.55154 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d6401cb6-8634-39f6-90df-876ef1d5f6a9 | -8.67319 | -49.54576 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e408d1b5-9261-3178-a5c8-fdff20f4202b | -7.28286 | -45.86062 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c8c48cc-9413-3a2e-ae0c-4d9573da1f59 | -9.20814 | -51.55605 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e0eaa5d-39a7-37db-8cfa-94d4ee4b3e0c | -11.07227 | -47.13258 | 2026-08-29 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3782540-8632-39bc-a31d-63797a9d0bf4 | -8.01743 | -48.00793 | 2026-08-29 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d7d2907-73aa-3845-9d17-f80b07d08956 | -6.91729 | -44.95051 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84526ec1-1125-3df4-ad76-96f1a26745e7 | -4.92453 | -55.7688 | 2026-08-29 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48b53f95-499a-3888-9060-26db56ee6ded | -5.87208 | -43.52592 | 2026-08-29 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6adfd5a-bdb9-30de-8327-7508de126c83 | -7.44369 | -50.91953 | 2026-08-29 04:32:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0d7035-3965-3210-b4e1-fc092b58a9a1 | -4.92371 | -55.77342 | 2026-08-29 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f599e3a1-cde3-3556-b6f6-66599e21fbf3 | -6.57081 | -56.54251 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3dab608-f2fe-32ee-aa3e-14a993276fc5 | -11.36284 | -45.15945 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4fb1eda-bbda-34c1-aafb-0edd1b482948 | -9.26767 | -45.64097 | 2026-08-29 04:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8ffdf55-896e-3165-b9a4-f1ff58b4e82a | -7.27406 | -49.85014 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3ec7a79-1701-3b12-849b-fa6464acfaed | -5.89287 | -57.7504 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5e3b1cfd-faea-3051-a33c-5551b421b73e | -4.97162 | -49.62253 | 2026-08-29 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cee9ecc4-0557-39b7-8d49-72b423b7ca2b | -6.63007 | -43.74491 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d370912e-0a70-3395-8334-45d7502b10bb | -7.07224 | -42.21259 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f93c3acb-2f36-3774-8e9a-215b7e767a4d | -4.3298 | -54.90192 | 2026-08-29 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d4751e9-031c-3940-954c-644f4fc16a2e | -11.24097 | -45.07017 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d53b01dc-e7dd-31fe-a9a8-2e20d046a6dc | -11.38341 | -45.13728 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05c36f29-95f4-3f8b-94f9-8f684d008de8 | -11.82897 | -41.52685 | 2026-08-29 04:32:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| da059d2a-e21a-3b26-b16a-54a35b7b6a05 | -4.64556 | -42.43575 | 2026-08-29 04:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 00446f91-9d9e-33b6-b16a-9ecf667865e9 | -5.88369 | -57.76153 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9d7dbb13-e643-3018-805e-4383f404e070 | -6.75415 | -55.67267 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c726b86c-6f88-3ffe-babf-b7f4ae280fc0 | -6.16972 | -57.78482 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3adf9bca-1e3e-3417-9c27-3ebbbd6c2a81 | -6.78123 | -55.65864 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c12afe38-79af-30a0-b07d-88a2390eefb8 | -6.76845 | -55.66152 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9e31b25b-f5b3-30d5-a452-b16a1539e20c | -7.50229 | -55.2985 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6099410f-f63f-33ca-b4a3-b331bece3416 | -4.28018 | -48.19216 | 2026-08-29 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d6b1aa4-77d2-302a-a9b0-f3bd839af8c0 | -5.8991 | -57.75122 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61794549-61b0-341b-9a5a-94a4b8ab328b | -8.82392 | -49.64359 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54ad47f3-3de9-3a2a-ab56-f8cfddc8cdea | -9.72188 | -47.77227 | 2026-08-29 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51299551-37cb-350a-b02e-8247ec0d93cc | -6.78048 | -55.66276 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 01be1ce3-663f-3bea-a3fe-71acd980a6bf | -11.23478 | -45.07687 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eb6a4c7-fee9-33f2-aa92-2acc1893a783 | -11.23534 | -45.0733 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39420ac1-06b7-3c19-b0f4-ce5959ddf756 | -6.76169 | -55.66497 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e35ce1d-423c-302b-901d-11ee32b25052 | -11.21752 | -45.05581 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee262270-5b03-3201-96bd-06fa46fd2d41 | -6.34014 | -44.08269 | 2026-08-29 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf360f01-a468-34d8-8fc0-6e980d642488 | -7.30233 | -49.53789 | 2026-08-29 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e2a78fa-b617-3b57-85bd-972dedb73f61 | -6.77523 | -55.65795 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 39665dfb-fbc1-3303-8efa-d5e2665e5160 | -9.42628 | -51.69739 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8127561c-5c26-399b-8709-dbda2211d3f5 | -7.34822 | -55.16666 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b326c5b-9819-39ee-8092-068f50f72f95 | -5.98356 | -57.67933 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7f01ad8d-07a5-36eb-ac44-1356ab3223dd | -8.98278 | -50.7914 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 009c5fc1-a19b-3666-8982-03dc7980fdef | -6.75334 | -55.67706 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd562a7d-b65d-3e02-8670-d41e64fcc352 | -5.48987 | -45.62503 | 2026-08-29 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25e5ec37-df33-3599-ba36-c69cdd2e6b95 | -8.59386 | -54.79572 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5252909-007f-3bf2-8da8-6158c54526dd | -11.2521 | -45.06464 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4215d671-2c16-3e86-96b2-b41bc78ce27d | -8.53352 | -55.27261 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a47b85b-a084-33bc-a99d-2512ea6f2280 | -8.59905 | -54.80243 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e3e7395-3597-3bb0-961a-fbcc53563526 | -4.34178 | -55.44192 | 2026-08-29 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d7c90a5-c3a6-35aa-b43a-90643b0d82b8 | -4.05815 | -56.29337 | 2026-08-29 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 598f6ebd-e5a2-3750-a6af-c6d10d8bef22 | -11.0689 | -47.13201 | 2026-08-29 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d6fab459-66fb-3637-beb8-a6a0499dbf88 | -5.1663 | -45.42195 | 2026-08-29 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d9e3a0e-2da2-3359-af91-923243419223 | -7.07518 | -42.21715 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 445a0593-f7ea-3cc2-8ccd-d12cb8d40807 | -9.60861 | -55.12473 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94f5a4a9-16bf-3ef6-9186-f5e4fbba0092 | -5.41213 | -43.18421 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fca48a5-1119-378b-96dd-f70ab0f05141 | -7.34666 | -55.17503 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2409ae1-cad4-37a8-a781-28ecda7ac7ab | -11.38062 | -45.13322 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3646c601-b208-3641-bd7d-4d689e82e816 | -3.87139 | -48.046 | 2026-08-29 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55f08d15-e67e-358a-b428-7bb05de7c5bf | -6.62167 | -43.73268 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9dc0073b-4b58-32b2-8bb8-a3ca02a6e430 | -7.2522 | -45.85929 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a79f70d-3abd-3531-a147-a8cced48436a | -8.53467 | -55.35975 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0af9b564-e782-3984-b3dc-5291bb2dc3b5 | -6.1527 | -57.80053 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26588500-32f9-3621-973f-a18e9a404014 | -11.38007 | -45.13675 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1537195d-c330-3750-b6ac-7dd4b7edf3f7 | -5.27044 | -45.11219 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27857ed5-0449-3a33-9564-c9a151bf361b | -7.60819 | -47.28912 | 2026-08-29 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b46c248-9908-3ef8-84e4-5f2fddb38de5 | -11.25433 | -45.07232 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd6c84be-c055-3cb8-b60d-831c369d617c | -7.49954 | -55.28111 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 258e783b-c126-394d-91da-06a605b06eeb | -6.76249 | -55.66061 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 107fc80a-0323-3ae7-9002-4575160147bf | -4.34099 | -55.44642 | 2026-08-29 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec33a633-5ff6-33ec-9d9b-48f86e4eb396 | -5.2241 | -52.02361 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73fe773b-3976-382f-8a9b-20c86281b1a7 | -3.18358 | -48.02177 | 2026-08-29 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c3d70b9-257f-3ba1-bfcb-30c336f6886a | -8.79577 | -50.49557 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eaad636-2272-3cea-8474-427f94c1c10f | -10.32637 | -49.9648 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35e97416-6968-3c92-b769-f82baaaf987c | -4.16652 | -42.44312 | 2026-08-29 04:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6683d39-5f94-3ad8-a6ea-9da32b2af7cf | -8.58837 | -54.79502 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7c7bc49-8e50-3a47-af22-4c9bde0001d1 | -8.3287 | -47.6292 | 2026-08-29 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 241e5379-684f-3a5f-88da-e27814ff28b1 | -11.36952 | -45.16051 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5bccb5c5-e701-3347-8274-91b7c42f4088 | -9.30788 | -56.80446 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 642aad1c-e516-3316-90cc-8771b9bed839 | -8.79646 | -49.99097 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d3d7d01-2faa-3650-9722-e923a72dfe80 | -7.53382 | -44.45266 | 2026-08-29 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42e65382-cfff-3f70-928c-f813d27130af | -6.77965 | -55.66732 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README32.md)
