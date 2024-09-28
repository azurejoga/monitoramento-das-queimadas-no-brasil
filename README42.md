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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 944b42d2-848d-386a-83b6-7bfb7d3aecd1 | -7.81783 | -45.52755 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973f9c1f-ec65-3e37-ada9-3b54dc0f0181 | -7.81729 | -45.53101 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4224980-07b0-32a8-9f2b-c0a55cc08093 | -7.81453 | -45.52702 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77207dca-6487-3e63-80ab-231d7c17debf | -7.814 | -45.57321 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd7c91d2-b00a-311e-825c-ac17a07201bc | -7.75137 | -46.16149 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d993940-e4f2-364c-a017-4f056a736091 | -7.75024 | -46.16862 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1aa3e788-b12e-367e-aa9f-b1d6502b092b | -7.74967 | -46.1722 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a6ef1a8-ccb1-36b3-a63e-70891d026cc0 | -7.74455 | -46.20449 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c519e48-7a11-3aea-9585-ab7de34a3b2f | -7.712 | -46.54976 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54c50f1b-c60d-3e5d-bcda-f207b8b2f385 | -7.70862 | -46.54922 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0ac68b8-a8f7-3641-aeeb-d99460340b76 | -7.56392 | -45.79804 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b9bef3c-9b64-306c-9893-18f0a19e0e9d | -7.56337 | -45.80155 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| beb78e5e-c8de-3533-b171-3d67d845e541 | -7.56281 | -45.80507 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a626338-275e-3f06-a7d5-836f307ce822 | -7.51797 | -45.78715 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a45b9658-a41a-311b-a08f-feb87863e493 | -7.51465 | -45.78661 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 796e20a3-2d4b-33a2-a7f7-94e238901d36 | -7.48504 | -45.88649 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ba26b34-d5a5-31dd-9403-7fafdeefe87b | -7.4482 | -46.09464 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48879e92-1297-344b-b007-5d9845d33ca3 | -7.37399 | -46.66061 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93f7f776-1c5b-3573-b678-a47be24186b8 | -7.3601 | -46.54586 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a5313f-dc0c-37e9-ba25-2a976c010eaf | -7.32764 | -46.6837 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fed3da2-80f3-35bd-9493-347167beaa75 | -7.32483 | -46.67945 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaf17b76-f8ae-3fe7-b9a0-7d483881409c | -7.32424 | -46.68313 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6370a5e3-0611-32f1-9def-05ae90da0770 | -7.32365 | -46.68681 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e292d7b-be19-3ea3-ac5e-b7aa8755a954 | -7.32202 | -46.67521 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f5cfd20-0382-3b65-895d-48101cc908d1 | -7.32085 | -46.68256 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ef79b88-2cbf-3a69-afc5-2466ea9d7096 | -7.31523 | -46.67409 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b038d1d-aa5f-3e89-92c0-39672da0bebf | -7.28852 | -46.13807 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6c02828-ee0f-35e8-84a0-24220af8f17f | -7.28795 | -46.14164 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb7f3486-fdc1-3763-9e79-873d3d68d897 | -7.28738 | -46.1452 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72c4909e-0a75-33bd-a38d-a1dee78fd735 | -7.26585 | -46.61311 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 335374e1-b821-3881-acfd-2aa53d744ec6 | -7.26246 | -46.61255 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 056bfd78-a0a7-3671-8448-dc0e8f86bfa0 | -7.26186 | -46.61623 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a694f9b3-47d6-3791-b8d9-67a0abd4308d | -7.15185 | -45.43493 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c19661a-8089-3937-ab60-1bb86bbbd972 | -7.14799 | -45.43787 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f21fa6fe-35fa-3cec-a2dc-0b7e526f9351 | -7.14744 | -45.44136 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8eb2c820-5b93-3b66-a09d-443c91487786 | -7.14413 | -45.44083 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e930ae0d-feeb-3088-9d6e-a923e0dc402b | -7.08273 | -45.46251 | 2024-09-28 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e67a91b-5232-311c-bca3-b7f2413d4826 | -7.03362 | -45.34428 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 308ddf94-cc31-3e6d-8ae5-2b30c49dca32 | -7.03307 | -45.34776 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f21c3c5b-f41c-3206-ae73-997526ff3def | -7.03031 | -45.34376 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28dfc8f8-6d3d-320a-8666-b2da61fcd1f8 | -7.02976 | -45.34723 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8924b2ed-be25-35b7-851f-8862561c582b | -7.02921 | -45.35071 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f245d2c3-d093-35c8-bab4-a5bb6aa2cacc | -7.02645 | -45.34671 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bd0b53f-5465-3850-b737-39e46b770fdc | -7.0259 | -45.35019 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e273f5bd-6061-3ef6-8456-05699b5e07f6 | -7.0237 | -45.34271 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dce5a6e-fcab-3ec9-a2c0-19f39e7fa922 | -7.02315 | -45.34619 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb7f9590-91f9-3ae5-8d48-32c23184bf06 | -7.01986 | -45.34214 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f335ae9e-25d1-33a1-b358-c0d022878e1b | -7.01877 | -45.34909 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df7a14a7-4bb4-363a-874b-efc43ad8e821 | -7.01822 | -45.35256 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c57c7d82-cf52-3fdc-806f-001dbcc5533f | -7.01104 | -45.33363 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aec0a5ff-fdc9-3de4-a145-5d8a7c367221 | -7.00883 | -45.32616 | 2024-09-28 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a68ad750-d931-39a3-bb25-ca45936749d4 | -6.9593 | -45.6829 | 2024-09-28 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed414c3c-d2e7-3dab-a1b0-d7b2386f2325 | -6.93993 | -46.21045 | 2024-09-28 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c74bbd62-9502-3dbe-9783-c6a09de61398 | -6.88209 | -46.22701 | 2024-09-28 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30c840aa-c913-32d3-af21-dccfa3e481f7 | -6.88002 | -46.22692 | 2024-09-28 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd4c6e6e-bb73-383a-bd21-50a2de4913a9 | -6.60523 | -45.72673 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9286a4d7-7c2e-3356-a539-75e133cad38e | -6.59857 | -45.72569 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9755da7d-0451-3df8-8803-53053bb65186 | -6.58304 | -45.71602 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3973a6b0-7bc7-3849-9018-7b53d64e49e0 | -6.58187 | -45.74486 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8048945-d6b7-3e4d-a6f6-d86f678c8909 | -6.57971 | -45.71549 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4558d7a3-f9f3-377b-baec-8f5f570b37cb | -6.57638 | -45.71495 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4041977b-48c5-3836-9109-9f95e47c244e | -6.5664 | -45.71337 | 2024-09-28 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb0811e7-7762-3d4c-bdc0-5a99171d7ac9 | -8.89281 | -47.15463 | 2024-09-28 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b278295c-8e4f-3b9a-a3e9-c7c15ff436ab | -8.40317 | -46.36134 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d6a932-d8d1-30d0-98fb-680ef06f5af3 | -8.40038 | -46.35732 | 2024-09-28 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5868b3ad-82b8-3679-88fb-26e58583e915 | -7.89935 | -46.66572 | 2024-09-28 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24332434-41d5-3965-ba26-f9b129e57d65 | -8.88382 | -45.65261 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e80933fd-c64e-3034-b9c2-025aa958c95c | -8.88162 | -45.64514 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c6d9679-56c9-348c-9338-581b10435427 | -8.88107 | -45.64861 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3201dc28-0982-3c04-8ab9-ac5f911b4f06 | -8.88052 | -45.65209 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 680e14df-33c5-3263-acde-a59739aa9bf2 | -8.87997 | -45.65556 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c88b10b9-f04e-38f1-a958-5ab50f6c4fd7 | -8.87721 | -45.65157 | 2024-09-28 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82d4b44e-1be1-3f83-b9ab-84fc0213697d | -8.08096 | -45.47669 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c23da325-76e6-3cf4-994a-5f381587f651 | -1.76747 | -47.19057 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 561ffd78-91df-32ac-ba07-1106f7b6dafb | -1.76678 | -47.19492 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9dc18530-56cd-31e7-a6d2-f9a92837509c | -1.76379 | -47.19 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce11bb2f-e25a-3435-a5d2-6e58374cd8ef | -1.7631 | -47.19435 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 000fa9c0-ebd4-3537-b274-28c40592b7eb | -1.72879 | -47.12835 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7cb3aa0-3217-32f2-8b2b-f859394eaabd | -1.7287 | -47.12673 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 831383b5-3831-3dc4-9e8f-2e7f79db369e | -1.728 | -47.13106 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f11a7fba-77d7-3a8b-8ecf-51e629a5ebfc | -1.72579 | -47.12344 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6a48efc-d583-396b-9596-73ca7d0c7ffe | -1.72511 | -47.12778 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a985c4da-dedd-34eb-b86d-115b36fdcd09 | -1.72503 | -47.12616 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a35a50c9-c94d-3a30-9e08-4936b57fa4cd | -1.72444 | -47.13211 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 87fb9882-e54d-3656-8636-1b2b7f28c40c | -1.72433 | -47.13049 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 15dddd4d-7694-3ee8-bca8-e36ad2b7d2f7 | -1.72144 | -47.1272 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a219f388-dff4-396d-900b-fac2687c1bcc | -1.72076 | -47.13153 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 21bba985-5f20-3d5b-ad69-ab65a2a072be | -1.71641 | -47.13529 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60bffa9d-bf9e-398c-8dbd-3ed4cf75b2f5 | -2.38008 | -46.53206 | 2024-09-28 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33de54a0-3aa8-3b6d-a351-c2e5482cf7e3 | -2.37944 | -46.53605 | 2024-09-28 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8e8992d-2fd3-3e2e-87ae-a305aad03831 | -2.35591 | -46.45523 | 2024-09-28 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c60156-9c06-39cc-a189-a48f80cb0c45 | -2.35239 | -46.45467 | 2024-09-28 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d3e91df-0559-3daa-925a-eb35442c6f95 | -2.35176 | -46.45862 | 2024-09-28 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c36b6f4-59e8-3265-a9e1-e087b0f44f77 | -2.74763 | -46.73099 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8db784b-2dbb-3e1c-972a-492e04a94b9f | -2.73021 | -46.74891 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee72dd9-25dc-366a-833b-750454fbe46b | -2.72957 | -46.75294 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 351e6ca8-d0de-32cc-868b-019357dc4e6f | -2.72274 | -46.72708 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f2875f7-bb72-36f8-b9b6-0b732e666739 | -2.71918 | -46.72652 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 77e9b7c7-ac7a-34f1-9c5f-d5a90c3a1898 | -2.71854 | -46.73055 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78e5ce5b-7027-395e-8878-ac412664a1e0 | -2.71563 | -46.72595 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README43.md)
