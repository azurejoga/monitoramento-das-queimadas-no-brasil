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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7898443-691b-38e2-a2ab-de29b46b6e97 | -2.86335 | -50.73496 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db864bc0-629e-356f-a6b3-0e8dc8cc2216 | -3.11294 | -51.20432 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee034cd2-e2e0-3f66-b9f0-5d6807513b8a | -6.4355 | -44.16478 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6fa328b-547f-340e-8358-031a0001fb61 | -4.91512 | -47.32557 | 2025-10-23 04:36:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4173ec08-b417-3283-9581-dc50fef2fa14 | -5.6329 | -50.03009 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d1b5615-f033-3082-a9a3-7f89e944c374 | -7.63006 | -42.19184 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a5a19e3-68c8-339c-a329-3715db665767 | -6.75274 | -44.07545 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb2e2b0d-3b94-3895-b74e-27a7ab7450db | -3.22237 | -49.36172 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c824fd2-bdc2-3e43-a444-17b887ccf562 | -3.11455 | -51.21162 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e758acd9-05b1-37f9-8eb2-1b5828accf1c | -2.80998 | -54.37704 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 384b6545-93b6-35fb-93dd-4c95290368a5 | -6.45479 | -48.74835 | 2025-10-23 04:36:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54adae3-0817-38b2-8af1-55e2a819ad05 | -3.22827 | -49.34717 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67aebeb1-544b-36ac-9ff7-ab4f35824505 | -6.59622 | -44.21841 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d06e3d5a-cb92-3f02-b999-b4870c87acd2 | -7.88814 | -43.55171 | 2025-10-23 04:36:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ec206f7-d0f6-33c8-949a-77bb372e9283 | -6.96139 | -44.01728 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2882e37-4152-3682-a51b-d902a01c850c | -7.33837 | -45.38403 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3163a761-98e5-36c5-9fad-9a8afc4b08bc | -5.77588 | -49.2736 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1bbd86b5-34c8-39cc-a6dc-91d5bc3e3f42 | -7.79288 | -44.00024 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8582b3b1-f56c-3ab4-aa65-569f259b6e08 | -4.29112 | -49.27762 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a234eb4e-a148-3070-8fee-cfe44485abe5 | -6.5545 | -52.80214 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7c6fe5-652d-32fa-8cec-97b96534ce90 | -7.82869 | -45.38449 | 2025-10-23 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d31eaf0b-894b-32b1-9953-3d338813faa9 | -6.30499 | -41.88162 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 78ea89c3-a200-35f3-accc-5c73e6f3bc1d | -3.42073 | -50.36932 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a15fcb49-acd8-32cd-86ec-9349679921a9 | -3.84833 | -48.15993 | 2025-10-23 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56c3b035-d97f-338d-af6c-e996923fb53f | -7.62913 | -44.57216 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b3affa-892f-3460-9968-5b5f511f6049 | -7.35646 | -45.04468 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56167be5-5318-35d2-a7fc-5e05bd31298a | -6.85392 | -46.29262 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f01589c2-2f49-314c-bf33-9e4b843efff9 | -2.80681 | -51.34841 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46eb9ee2-31d4-3741-9176-97f4af55574d | -6.09232 | -46.23373 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b05db312-7271-31f7-9f4c-6285834b046e | -7.32802 | -45.28362 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f77d9ec3-b704-3269-b131-848c3ec80446 | -6.10481 | -46.24311 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61d976c3-bd06-317b-86c3-2b08472564be | -4.93601 | -48.30263 | 2025-10-23 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc103b74-58a6-3871-90f1-14262b256663 | -2.85754 | -50.74757 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b147651c-a809-307b-9202-81f7c119b05e | -6.79181 | -45.44858 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4209ce-0696-32b8-91c6-f5e89c83622a | -3.51989 | -52.82529 | 2025-10-23 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 497f69b6-3770-3bd9-b371-85407737001d | -2.87057 | -50.72109 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c908a6-46c2-3b7b-b345-e1d68d93680f | -3.39505 | -50.27607 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442b6346-69d8-3a17-bbbe-1dc7a77df977 | -3.05388 | -48.71338 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2d008bd-1b2c-3230-b9a0-5c438e558811 | -6.59689 | -44.21406 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdba9577-cf81-3d74-b428-af0a3892e629 | -3.22827 | -49.34716 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a591fe0-9b91-30f9-83bf-0c9931b020c0 | -7.631 | -44.57115 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6b7e90d-ccf4-36aa-accd-99e2ea74b381 | -4.19967 | -48.35868 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 865e0838-3bae-339c-896f-da9b0fc75360 | -3.24972 | -50.133 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bca042f-08e9-3766-bcda-14b371112d93 | -4.78122 | -42.97335 | 2025-10-23 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51347b78-6c04-33c0-90c5-d58cfc990830 | -7.00565 | -46.99948 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7ef30f3-d051-3773-ae9e-2f4ecdd3cf55 | -6.5505 | -52.80149 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 390cdbcc-8845-36db-8555-a264b89148ef | -6.7865 | -45.45978 | 2025-10-23 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc2d251c-a248-3bdc-8dcf-5d2447fb4c4e | -7.62729 | -44.57059 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13618c0c-1d2f-3eb0-b8c2-90e96fd6a963 | -6.79122 | -45.45248 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baa78065-6941-38dd-8701-6d83045cbfd9 | -9.29775 | -45.1977 | 2025-10-23 04:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11933a46-f810-34b9-b61e-ec5e73db0867 | -5.70879 | -46.02948 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5fecde36-225c-3aef-ba27-706426409273 | -3.84712 | -52.28155 | 2025-10-23 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0baa5700-c54c-318e-95cb-df82c3936218 | -6.60128 | -44.21038 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8afab99b-e4e0-3ee4-9dc6-e367d027f2c6 | -4.68195 | -42.72897 | 2025-10-23 04:36:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0c44ad9-f787-3f34-a77a-1ef31ebd8497 | -3.47165 | -50.07539 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4898d9d9-6667-36a3-89f1-f5ef04891fb5 | -3.98654 | -47.88488 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7bc8f4b-af39-3050-bb1c-981461ab2d43 | -4.64033 | -49.53799 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 217e392b-1391-3425-8e63-00ecac32f70a | -4.19409 | -50.11361 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5c353b2-173e-32b5-9a4d-d94f332ba8aa | -5.43682 | -40.88711 | 2025-10-23 04:36:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5518b008-60cc-3897-883b-4d3ebdf3b5d6 | -5.04849 | -46.88311 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c20aa14-5277-3721-9101-63b3e9f2f675 | -6.93815 | -43.57711 | 2025-10-23 04:36:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c1f2fe1-fa50-3708-86c6-e73fa40d432b | -7.0034 | -46.99187 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c2b519d-7c14-3d65-a6b6-ca46f90527f8 | -3.7642 | -48.92483 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee4c89e-29af-3c58-9514-aac82f52b4a6 | -4.71556 | -40.58759 | 2025-10-23 04:36:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22fa3e7e-567f-343b-81d1-8c4ce8bb20a5 | -6.30254 | -41.87984 | 2025-10-23 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 905b8b99-ec1f-335c-89ec-1bb0b6013f5b | -3.0499 | -48.71648 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abede202-8461-3462-943d-baa2c07345e3 | -7.88679 | -43.54764 | 2025-10-23 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f300d4b2-6fe0-32ae-93ff-c87d799e2ef3 | -7.08162 | -46.19461 | 2025-10-23 04:36:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f88958c1-690c-399a-b485-023b619ff1f1 | -3.02549 | -49.48402 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ea36abce-f272-3f40-8829-baba6399c6bd | -4.35397 | -48.72859 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5857a02d-4861-31b0-9dcd-b2e247d21a5c | -3.8477 | -52.27804 | 2025-10-23 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2915e99b-19e5-3a02-ad8c-ee7b1f11fe71 | -4.88767 | -39.80856 | 2025-10-23 04:36:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ae130b76-3e37-37f9-bab3-914d73270127 | -4.32857 | -46.79584 | 2025-10-23 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef48749-81ba-36e5-a874-fa30e791c4ef | -8.20438 | -46.98983 | 2025-10-23 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ed05c9d-03c4-3de2-bf04-cd8a96b10b52 | -3.47815 | -50.08052 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fc22d35-d076-31ca-9551-796d15790d60 | -6.74895 | -44.07491 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d6c4ade-7928-328b-ab57-26b10d97a98d | -3.01993 | -49.45163 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2253d294-9f12-39d1-99df-dc45721289a0 | -6.08414 | -49.37839 | 2025-10-23 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b002086-086a-3d0f-9665-dd9df91da8cc | -4.66943 | -37.81977 | 2025-10-23 04:36:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 957b2c94-ec79-361b-99e3-a1ec04fe1707 | -6.27864 | -47.01357 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e669f271-17fc-31c0-ac39-23c8dd79854d | -6.27698 | -47.01298 | 2025-10-23 04:36:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 209ccc1b-ca73-39b5-a6eb-e4d75c907445 | -7.62913 | -44.57217 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db914bf3-b35c-3b2a-b900-f1700dfd6432 | -6.90016 | -43.59156 | 2025-10-23 04:36:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67d4b5fb-2e30-3550-ac09-0b2d8cd5fe7e | -7.03313 | -45.54301 | 2025-10-23 04:36:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 187655e5-3b63-3c82-ba20-cd653eb5c320 | -5.25287 | -50.8071 | 2025-10-23 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e1f1663-a9ed-316d-af69-bb6f75d7c4d5 | -8.35072 | -46.19001 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 904af381-886f-34fe-b7d2-371f21655a3e | -6.92462 | -48.26828 | 2025-10-23 04:36:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e1d8085-4b99-3bcb-9af8-a3fc5074e460 | -3.15073 | -50.16903 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86465529-5398-3a91-8e95-6864009b06c7 | -3.33248 | -50.75233 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8524c59f-e0eb-3e8a-a0c9-faa670ce1740 | -5.8893 | -43.2002 | 2025-10-23 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05d1a590-e814-39d4-a102-883378c95975 | -7.06489 | -44.10132 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24410e39-d636-3961-9196-c99193ae97c7 | -6.59745 | -44.21649 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4277ec5-de40-3f4e-bc70-cad604bfea75 | -6.60128 | -44.21037 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0ab91ca-d3fd-3fa1-8194-78b764c91657 | -7.88891 | -43.54659 | 2025-10-23 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adfc17d6-1937-3809-8d57-15acb7170603 | -3.46924 | -49.28347 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ff205c-9074-330c-ae47-68ff19757c57 | -2.92983 | -48.30468 | 2025-10-23 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bc4d905-f631-3f8d-871e-d10d0ac68c0e | -2.80556 | -50.27447 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca8ddb5-2407-3b26-9935-2e5ffa6ff5d3 | -6.59689 | -44.21407 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bcd1fc1-f9e2-33b3-9c47-347594f394c0 | -7.51974 | -46.8848 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9714450f-59dc-396e-b261-f232ca58700d | -2.89868 | -49.39776 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
