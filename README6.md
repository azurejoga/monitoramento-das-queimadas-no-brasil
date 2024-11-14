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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 793cc132-280d-350e-938e-0b1c1c305a13 | -3.4065 | -44.986198 | 2024-11-14 00:32:00 | METOP-B | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a60f780f-d051-30c0-ac7e-0b1143681d6e | -1.4379 | -47.791698 | 2024-11-14 00:32:00 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8eeb7d-a718-353c-a4ea-6c9cc2668061 | -4.0121 | -44.672901 | 2024-11-14 00:32:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41a0ade8-72b2-3816-a817-147b81d9b2af | -3.6449 | -52.268501 | 2024-11-14 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29b05ee-d094-3a4b-a68f-9bd5885eaf25 | -1.2052 | -51.770901 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c45225d-3d0e-3c6e-868a-fd45f0f95525 | -3.3992 | -50.304001 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4a460e-d5f8-36bd-bc75-1d1cc057a545 | -4.0634 | -50.0051 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5fa0268-2a94-3cd5-a6ca-16e547f1aaca | -1.3932 | -52.376598 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f98b344-6913-310d-95ac-66d985a08a00 | -2.4655 | -45.852001 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35a236df-8cb4-357b-82c5-3dfe6a5df24b | -1.2181 | -51.782398 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 712812aa-7991-3283-bbd7-6d1cf7fd901c | -1.4062 | -52.3885 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 521a83c6-b6ac-32ab-a382-264b23dd1008 | -0.1644 | -51.542801 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c057a923-838b-3564-9adb-76f2847c0adb | -4.3795 | -47.276299 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b724b125-8b08-3cd0-84e9-5a7878d3760b | -4.0335 | -47.206001 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8333d75-104c-39b3-b02a-fe9d0b02ff13 | -3.9097 | -52.255699 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41753679-ceed-3bdb-9f07-c18d5178ddbd | -1.3292 | -51.406601 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d9df9c-090d-3ae5-8306-22bc582408e4 | -4.1512 | -46.2425 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3bb7cc-515f-367d-99d2-c7c8eeadba98 | -0.227 | -51.500401 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 46df29e9-7911-3534-91bd-efb5591c8a44 | -1.2166 | -51.7756 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 960ec49b-1972-3f72-94d8-eb7674891995 | -3.0366 | -45.519402 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 983ad9de-25cc-3bfc-8d7a-eb232fdd557a | -4.3244 | -45.436798 | 2024-11-14 00:32:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b57aa18-94ed-3462-9708-3f545b1e3f54 | -1.4465 | -52.247299 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9c67a8-759a-38a2-a577-84dfbc9ff94a | -2.5306 | -47.120602 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba5b241d-88ce-302b-a51c-a6ae3c9f3a15 | -1.3559 | -52.348 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e92dd31-e3dd-3c75-97a8-49cd3631cf2d | -1.6583 | -52.548199 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0400173f-1822-3339-bf27-0ab66e44a3d8 | -17.583 | -57.435699 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a285afc-683f-379f-aab0-01f03679cc6d | -3.47 | -50.2523 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dff3be1-f10c-39db-81cd-60084f495e0e | -5.3501 | -43.543598 | 2024-11-14 00:32:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62f494a4-b688-335a-82de-4e038717a19e | -1.568 | -52.008801 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12615d74-cac6-300e-8974-cc6e22c89fec | -1.9403 | -52.152901 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eda888a-2c1e-3dbd-81a0-71c1831dd0c4 | -1.2799 | -52.468102 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fe84df-9b10-3097-8255-50c9d89010a8 | -1.384 | -51.101501 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5fa5700-da7a-3534-aa6e-88df04c7d194 | -3.1275 | -45.2901 | 2024-11-14 00:32:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b05057f9-82c0-3c1e-98d4-74c8f6ad6e15 | -3.2635 | -50.570499 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26bc0e3-f459-3fc7-be17-a1cda00f4b6d | -2.7194 | -53.193001 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8606d86d-85e5-382b-aac4-4cec6b6cb7fe | -0.8876 | -51.733398 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3292261d-dd39-3d39-b822-1291961f0055 | -0.3357 | -52.028 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| df99871e-d370-399c-8e24-9069270ab824 | -3.1234 | -50.314999 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a002125f-d53f-3c59-90fb-bd702dfc698b | -3.0392 | -45.530201 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5618d5a8-fca8-31a1-b947-4b919ba03f66 | -1.6807 | -52.693298 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7435b285-3c04-38e9-9602-910aee94d9aa | -0.1862 | -51.5023 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c791edef-d1a0-322a-a55a-f671389b7cb1 | -2.3698 | -45.9725 | 2024-11-14 00:32:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94919b56-650c-3cad-9000-4ea92988206b | -2.6314 | -46.170101 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6482669f-e1a9-346a-9eed-41b1ddb73f67 | -1.3609 | -52.324902 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b51b9fd6-6f71-3ea1-8de4-7100f361bc0b | -3.0653 | -45.421001 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 440e3d31-e8df-3f5b-9e24-f9c971dc3db2 | -5.1782 | -44.337601 | 2024-11-14 00:32:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24cfa358-6d2e-3714-8e57-d543aaa5561b | -3.4163 | -44.984001 | 2024-11-14 00:32:00 | METOP-B | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a807231-a9f4-32dd-af4d-44be862b726f | -3.1223 | -45.2677 | 2024-11-14 00:32:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af23c2ee-8686-3f99-b31d-fae85f5a089c | -5.3378 | -46.028702 | 2024-11-14 00:32:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10644986-7584-38ca-b329-4ea57026b336 | 0.8379 | -51.3936 | 2024-11-14 00:32:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e1f58014-b928-3f9d-b3ef-e3170de9db65 | -1.2897 | -52.877899 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c98d317-548a-3e34-808f-484049c84784 | -1.6823 | -52.700401 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f336029f-a0ed-36d6-804e-51ae2f975732 | -2.2655 | -50.806198 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b36b4c81-43fd-336e-bc85-8c8fa6f0ebfb | -3.1321 | -45.2654 | 2024-11-14 00:32:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1df53c-58fd-3777-a7d6-9ed2369eec3b | -2.6906 | -51.870201 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7820185-98a6-3a7d-9c6d-9c24374f7c9d | -1.4341 | -47.774899 | 2024-11-14 00:32:00 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387aaed5-237c-37fe-a502-ea7af42a8561 | -4.2092 | -50.697102 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4880b5-ba91-38c7-b1a8-6cde03912e8a | -2.8791 | -51.792099 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7630b9-58da-3549-9824-41f9bb13783f | -0.1847 | -51.495499 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 58e24aaf-4d0e-3079-837e-5ad141c1eb6e | -3.0079 | -45.661499 | 2024-11-14 00:32:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3b0d3b5-0296-3610-bbc3-9f968fdc8710 | -6.0183 | -48.037899 | 2024-11-14 00:32:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe05d1d-a75d-3b41-9e15-905dbe747711 | -5.0204 | -46.8377 | 2024-11-14 00:32:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2adb5cd-97c5-39d6-b3e1-6f14dedf57df | -3.151 | -50.574001 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a0f697-0bff-391e-9df5-ff40439043f5 | -3.7398 | -50.443199 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bcb7fd9-d95e-3c6d-be48-0e6525748a06 | -3.0135 | -45.0644 | 2024-11-14 00:32:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfad33a1-fa49-33fa-91d4-3ec9703c7814 | -2.8832 | -46.862301 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bee7d70-2d90-36a8-90df-a174e10b6863 | -2.6666 | -46.815701 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a44b68-8017-3430-8b1d-0b9a5f58c1e2 | -0.1945 | -51.493401 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d185fa4a-8f84-3b71-aa68-8bf4130c8624 | -4.0149 | -44.684799 | 2024-11-14 00:32:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e17f170-de4d-340f-85c1-85066a2f531b | -3.9897 | -45.547199 | 2024-11-14 00:32:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d93b884-2b50-360e-980c-0bf84bec8846 | -0.8928 | -51.710701 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 399f5017-9772-3b21-8d0e-b3121c074bd9 | -1.3871 | -51.115101 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1898ef-5535-33f3-b8ea-3577113726c8 | -1.9383 | -46.242699 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117319dd-86bd-360b-bb3a-d7f456de354c | -1.3963 | -52.390701 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d137a80-1be2-330d-accb-584795fb2abf | -2.7 | -47.726002 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c47825cb-866a-320e-8836-a1e9cf892e33 | -3.2443 | -50.302502 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c89fbd5-8891-3503-a183-8814ca2f4726 | -2.8152 | -46.655899 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f87497-1817-3a34-a0aa-f1654688e79c | -5.0185 | -46.829201 | 2024-11-14 00:32:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18726f58-5e60-31e6-977e-ac0004f40204 | -3.797 | -47.791901 | 2024-11-14 00:32:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ad8a27-16d3-3edb-89a7-1a815eefd4f0 | -4.1533 | -46.251999 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e8200d6-573c-3193-bd41-0b2b6518ec1b | -4.0247 | -44.682598 | 2024-11-14 00:32:00 | METOP-B | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9ae7f73-1c4f-3d82-a97a-7322c5ebe0f0 | -5.3469 | -43.530102 | 2024-11-14 00:32:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6788db1e-9841-3f38-ace7-6df7ff62195a | -3.8704 | -52.264301 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8ea5b5-a738-3b60-9ec8-e9d200d263c4 | -0.9254 | -51.7178 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a2e0ad52-60d8-3dcb-91f1-0a8ca9ef85db | -0.193 | -51.486599 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bc521753-c652-3068-bcf6-e1aa6a9903ea | -2.5111 | -45.3363 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0121ec29-12e8-31c3-bdc0-063e7b6a2c23 | -2.655 | -46.989601 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aca280e-bdbb-3dfa-805b-380c68fe6677 | -1.3856 | -51.108398 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27470a35-805e-3048-a425-493213271e60 | -3.0434 | -50.3256 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48e2379-5652-322e-adeb-95d1cc595964 | -1.7884 | -52.164501 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf376ff-fae9-3abd-9790-588637a828a0 | -11.4567 | -48.010201 | 2024-11-14 00:32:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29e1b8fa-443e-3a4c-ac67-349400efe123 | -1.6599 | -52.555302 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1a31aa6-22c5-3f29-9cb3-4e9885fb1397 | -3.3017 | -44.052502 | 2024-11-14 00:32:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 561f1721-45e3-38e5-80e8-2ce067af9ae3 | -3.3977 | -50.2971 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84944725-6372-33f1-bb59-46edc43a0528 | -2.0122 | -46.924999 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46fd8257-95b9-3f37-afe5-97f60dbae6b1 | -4.7672 | -46.1008 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbed2fa-0431-3ac0-a92f-7ec7dbc06ae5 | -3.1373 | -45.2878 | 2024-11-14 00:32:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c10e152a-afcc-3784-bda5-d0919abced10 | -3.2934 | -50.018002 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 107e1170-0fa7-3b77-af56-63e0721ed9d1 | -2.9849 | -51.0257 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37056256-a42f-362d-bef9-d0953ceb2f5f | -2.813 | -46.6465 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
