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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abca479a-3a3b-36cc-9a88-056b778de98d | -4.45892 | -43.64299 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 356b207b-44df-3ce9-9953-e4df9c78b0e0 | -4.20018 | -50.08999 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4dc5a88-31b6-3b82-bc6b-9adec44914ed | -5.1518 | -45.24858 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e8523d2-9374-3b14-b28a-a55b2abe3805 | -4.34868 | -46.31643 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ce206cc-c1bc-3b5e-9239-7bf0a04c6d23 | -4.92908 | -42.73039 | 2025-10-28 04:12:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25e004c1-2527-3b46-b611-7fc3e95a0e69 | -3.25048 | -50.03922 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cf34ef7-809e-33bb-8cba-e640d21a9140 | -4.28498 | -48.63078 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27fb798a-2bcf-3d9e-b008-bf9daffa3347 | -2.63904 | -44.29144 | 2025-10-28 04:12:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40596d4b-d49b-3e5e-a219-383e3fde3c1f | -4.10114 | -48.02861 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d015acb1-4f2d-323b-a6fa-8f4808f7d3ad | -5.52145 | -43.876 | 2025-10-28 04:12:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b1fb334-ddcc-306d-9ec6-c68a854cf4f2 | -4.88393 | -45.74076 | 2025-10-28 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7a48050e-7604-35f3-958a-648228deba6c | -4.71608 | -46.4276 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a7802a9-c5f9-3fd4-ae77-cf8b7f9a0436 | -2.75885 | -45.39692 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c575a2c-92bc-3cf5-902e-3cb1d315d73c | -3.8959 | -47.32887 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a9edf82-eaa9-314c-88d1-fca90ab8e095 | -5.80928 | -40.81485 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a19dba38-74a5-3efd-b429-361e77cc204f | -5.43142 | -40.87631 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f032ae6b-1fb5-30d7-af93-0ff98fab8ccd | -4.37659 | -49.67322 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ff0984a-0ff1-3539-bf89-8182961eee61 | -6.09738 | -41.78086 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d4a817c-fcae-39ae-883f-d625d03d11ad | -6.08824 | -42.14909 | 2025-10-28 04:12:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 689f63f3-29e3-3ba6-be88-869768cf88eb | -4.91149 | -42.90724 | 2025-10-28 04:12:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6efdf8c9-feef-3af5-8802-7cc07e08b9ee | -5.51812 | -43.87548 | 2025-10-28 04:12:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d32db4a-11c4-3c98-8c7d-ea30429a3368 | -3.86448 | -43.35513 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aeaeffe-ea95-33d6-8d24-791f34bbc054 | -6.0921 | -42.1461 | 2025-10-28 04:12:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29f7724e-318a-3d7f-a6dd-ee9d319195a8 | -4.06969 | -49.44719 | 2025-10-28 04:12:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a9709bf-7e2a-3be7-ba6f-27f17f2483df | -5.84351 | -40.82019 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de6c6e5b-775f-3c9a-96dd-8f3889b0f6f1 | -4.72725 | -46.81108 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a816d98-d41e-37e4-91a6-cc79fedac16e | -2.35245 | -48.29116 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b053f853-54de-30d1-9d25-99386eb3e2db | -3.36965 | -50.17416 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6a95ca-1dae-3ea2-a0d1-a569683e2239 | -4.91203 | -42.9038 | 2025-10-28 04:12:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 419d06da-230a-3f01-acb0-a822317ee043 | -3.57931 | -43.63092 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4b5312f7-4e21-36e3-b583-fd6fb7c6bbcd | -3.44707 | -41.84915 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ff2a2356-f338-3de8-8639-fc7b26bcc807 | -5.22062 | -37.38639 | 2025-10-28 04:12:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5bb4d88d-ecc1-3add-9f88-ef7dcfd4d0ea | -6.18976 | -41.55865 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d0e4d62b-ab40-32c0-a840-cc107e5d4111 | -3.58391 | -41.06055 | 2025-10-28 04:12:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e07bd96-61e9-39db-b015-cffb0fe9f86f | -4.51059 | -42.83687 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0e8dcaf-00cc-321f-a41c-d3f66d70e521 | -3.59916 | -47.51555 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30fbb2bf-a671-3545-a00e-14ffd90d6c14 | -3.71107 | -47.64946 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e162bcda-b15c-3af2-9698-6127fd3e2aa9 | -6.11823 | -41.71178 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c90e5391-5046-353a-8a0c-61ce4a5ec20e | -3.58335 | -41.06411 | 2025-10-28 04:12:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b760bdc-e1be-376e-b8dc-4ca3b12d40c8 | -5.58706 | -45.33978 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6b72576-dcd0-3a69-8e5d-b555827ec482 | -4.25456 | -53.54089 | 2025-10-28 04:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ece4e10-9428-35b0-91b6-2f8eaccbf989 | -4.87057 | -48.52965 | 2025-10-28 04:12:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 253e2962-285a-3b5f-9918-4330e8314413 | -3.58658 | -43.60662 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f6cf564-d686-3413-bd0d-fcb0fb90bfe5 | -4.56803 | -46.88056 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dd19903-a0a5-3639-a8ce-9eca2e35adc1 | -5.79896 | -43.97076 | 2025-10-28 04:12:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c33fc13-39a4-3f2f-b386-4fd6683581a2 | -3.02364 | -45.36725 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| baa18673-c5b2-3b6e-bd6f-6670e37b0dff | -3.11028 | -51.21129 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77bb2666-c179-30c7-8b63-f816d6a5d7a5 | -4.63556 | -48.69382 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86858ce6-e307-35ac-94b0-70d7729df15d | 1.03967 | -51.30965 | 2025-10-28 04:12:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9001ebcd-0ced-3415-8608-04c6113a98b4 | -3.69709 | -43.20766 | 2025-10-28 04:12:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0760f04a-2827-3fb8-a0d7-112bdf48e6c1 | -3.12137 | -51.20959 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db64b742-7b4b-3ab9-a2b6-b299762d2bcc | -4.44375 | -45.98188 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8b4e53f-f6f1-3c70-aefb-a235fd3cbf8c | -4.22848 | -48.36794 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dca723c-9bdd-3c9a-8d0d-41069020ddff | -6.11769 | -41.71533 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a1d5d220-1d7f-3d1a-9631-3600f16bfc69 | -3.12803 | -53.00375 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3790f044-fb5f-3e8b-9c1f-b2efdc438921 | -3.30664 | -42.35812 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde224e1-ee8e-338b-9a78-112d5ec0091c | -5.35503 | -41.19284 | 2025-10-28 04:12:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a582aa1f-ecb4-3d38-806d-acecd814ee61 | -5.60984 | -42.77112 | 2025-10-28 04:12:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a497612-688f-3289-a811-b77a5be12f18 | -3.17223 | -45.65144 | 2025-10-28 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a63840c2-a2cc-3ab6-9c1f-d8656d134504 | -3.15241 | -50.33355 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65a4b33d-b63d-38c6-8fb2-ca861aede62c | -5.60324 | -42.7701 | 2025-10-28 04:12:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b795b551-0cd5-3f1d-b0b7-217573c6d959 | -5.49384 | -42.16683 | 2025-10-28 04:12:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7e3004f9-239e-3916-a278-7acb706f8f25 | -3.82758 | -42.46526 | 2025-10-28 04:12:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8effdaba-92f4-3d0f-a1a0-afaea2f74c6a | -5.96493 | -42.76733 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb63a282-a1da-3770-87bc-51c098614d22 | -5.48843 | -44.10678 | 2025-10-28 04:12:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4446da61-db2b-3088-923e-deb11526fbc7 | -4.25202 | -44.90463 | 2025-10-28 04:12:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de810523-e769-3ed3-a0a0-17aa039cbc6f | -4.25141 | -44.90846 | 2025-10-28 04:12:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 871341b4-9f77-359f-815a-385cddaa2f82 | -4.7548 | -46.42486 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc471350-1447-3ccc-ba38-94b6dbf06007 | -2.83398 | -49.40031 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| c9d04e12-2ad4-3b89-b6e6-68ee5fb96581 | -4.35295 | -46.55433 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ddd865-940e-387b-b444-1b7a22ac51fd | -6.11272 | -41.72541 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 46d24deb-825b-3d0f-ad6a-ad5d2d550853 | -4.20854 | -48.35649 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e36aeaa2-dd58-380d-85b5-d4a6bc3e01fb | -4.22912 | -48.36403 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddcc8ecd-a568-3cf5-abea-404e27267171 | -4.9113 | -47.416 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a729e62-1e33-3542-86d8-bb3c0c2bc69c | -2.95033 | -49.35098 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 44fed2e6-b72d-362d-a44f-38ccf6238f2a | -3.02724 | -45.36781 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e3558a0f-2c69-38fa-b0c9-2ad91cefd759 | -4.30856 | -48.06153 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039db632-9190-3ee0-9376-3248210ef4c2 | -6.15173 | -41.56022 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ff1d91f0-1710-3890-90f8-63b95420dca7 | -4.00858 | -43.21709 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 577ebf7f-c654-3a16-a7e4-f27fbffa4690 | -2.8949 | -43.04881 | 2025-10-28 04:12:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b8e2d31-7550-35ad-973e-bea70aeb1e01 | -3.03084 | -45.36836 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e2858c97-9358-38d7-bdfb-a431a7361924 | -3.36377 | -41.92785 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88b49333-2d1f-3db7-96fb-ae6fc4d9b3f0 | -1.70173 | -53.68991 | 2025-10-28 04:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f36b51c-344f-34f7-b813-97f6a9b945d5 | -4.90281 | -48.56828 | 2025-10-28 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9dc6bed-11ed-30b8-b3d6-de1856b2a903 | -3.08793 | -44.44857 | 2025-10-28 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 720fde33-ae04-3d48-98e4-10cef1fab067 | -4.30547 | -47.53571 | 2025-10-28 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e423e16-e853-38af-bcbf-0740790eb5f4 | -3.23786 | -45.94851 | 2025-10-28 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b01aaf1-02e3-35b7-924f-55607654a8aa | -4.38058 | -43.29777 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc754f63-ba87-34c2-b6d6-bf2b0c89976a | -4.96335 | -48.26041 | 2025-10-28 04:12:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b9411f-2ec2-3424-8920-1dce08f6034c | -6.14316 | -41.83838 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 94872e52-549f-365c-a74d-92101c4f19cd | -4.1997 | -50.09327 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4797107-30c6-33b8-9f42-020a0c939d9f | -4.2298 | -43.1953 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dbb352a-ce31-31a4-bc2a-f2ed3be57c47 | -1.49972 | -53.12321 | 2025-10-28 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba72ed87-60ea-397b-9193-4cac967cfd1f | -5.41822 | -42.67423 | 2025-10-28 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbe5a120-786f-3ef0-9625-d2696fef367a | -3.71048 | -47.65314 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74337305-6b57-397c-b365-90bb4280489f | -4.43282 | -43.44146 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7216444c-1707-3c40-8fdb-5b35ca8fa486 | -3.9817 | -48.98779 | 2025-10-28 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21e3a39f-ef45-3b5c-af2e-c12393fcb824 | -3.72273 | -47.65516 | 2025-10-28 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2ee34cd-443b-38c8-819c-b43861fd3f6d | -5.84093 | -43.27352 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f845be7-9193-37d4-b06f-193bdcfcc9cd | -5.28024 | -45.73308 | 2025-10-28 04:12:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
