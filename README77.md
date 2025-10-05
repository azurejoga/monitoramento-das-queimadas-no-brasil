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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55e705ff-045a-3f40-a94c-873801286a56 | -3.67563 | -41.75799 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 14ebe222-567a-3c2f-9374-bba605176785 | -5.21512 | -46.17954 | 2025-10-05 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2ac6d8d-dbba-32ab-ba08-7507ccc8ce92 | -4.13338 | -47.65659 | 2025-10-05 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b143400-2ffa-3e51-82d6-5afddfa6276c | -6.37086 | -42.87889 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef9b9caa-4759-3d2a-ae09-bfe5f6976f07 | -6.06519 | -42.53318 | 2025-10-05 04:44:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 727c9c54-9607-3024-b9e7-e818b7c8a274 | -5.25237 | -42.64016 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5608b20e-43fc-37ff-a844-3e19f94f0c97 | -6.24436 | -44.21381 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2223f012-871d-397d-977d-ac775cb24c3e | -3.84964 | -41.56343 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ade57733-5b09-30f6-ab1f-7955d711842f | -2.29761 | -47.99265 | 2025-10-05 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81801087-c351-3516-92cb-8c555a0b4bfe | -5.65165 | -43.20189 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e5552db-b6b8-3a81-9f11-6d0ad1702a34 | -5.94194 | -42.87191 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 79600dad-f38d-3218-9b91-affd8adf3410 | -2.69358 | -54.76764 | 2025-10-05 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79d1b959-26f5-3691-972e-d1e24b1c300d | -5.81861 | -45.80589 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ddf68e2-3aed-3120-aaf5-7636484efe24 | -6.66906 | -42.38692 | 2025-10-05 04:44:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4c218b67-e529-3acd-8409-9b45ea2acaa8 | -6.40216 | -42.68963 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2126afb4-39c3-39d4-8a85-f88ec1bab07f | -5.22927 | -42.44073 | 2025-10-05 04:44:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6caae6fa-d99a-388a-8579-3f451dba2b46 | -6.16137 | -44.11057 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2478c84f-acd3-3cca-970e-5a6539458e67 | -5.66664 | -42.75179 | 2025-10-05 04:44:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4dc1295a-68a3-3fd9-868a-edf656c7791c | -5.12736 | -46.23172 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a086e56f-cce7-395c-aa1a-f3d483d00949 | -5.64421 | -43.92078 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 085224f5-4605-31d9-88c9-0bbbc10aa5a9 | -5.84748 | -45.80657 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dadc7c6-2b48-3299-8b3a-837ddcebab75 | -5.77799 | -42.93824 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9ae418ff-f43b-3f70-be29-c07a3c6b04b6 | -5.75161 | -44.59739 | 2025-10-05 04:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c37e23e-29d0-3440-a491-388dc1c37ac6 | -2.90224 | -50.72746 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9cb6f3b-6dbb-3b74-8175-1d04340a5f3b | 0.52822 | -50.78851 | 2025-10-05 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5acef5c0-603a-33cc-9b73-2bda97b607e6 | -4.36418 | -50.86617 | 2025-10-05 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96e13df2-d2aa-3fe7-9293-8be97edd3b69 | -6.13725 | -44.63874 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d34558-da18-3ab1-9bd8-f3f7bad9cb25 | -5.88951 | -42.91053 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 622764e1-e9ac-3214-9767-6bf070ee8df6 | -2.57487 | -48.96467 | 2025-10-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e729d83-3503-341f-8ae6-ce8a807e69b2 | -6.14666 | -44.63585 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49d204ae-7221-3742-8756-9055661ffee8 | -5.84995 | -45.81801 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 317f49ae-ff5f-3471-bbdc-93321ecc9f09 | -5.78666 | -45.79423 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e68440b-118b-39a2-acb6-e4103e3c3fc9 | -5.80524 | -45.75307 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7479f0e6-731e-36bf-bfd5-7a4dbe82f614 | -5.06652 | -40.4746 | 2025-10-05 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1a9462f7-8531-30c9-ae22-ffa176f7fba6 | -2.90196 | -48.07863 | 2025-10-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3aeaad63-87d5-3ec2-8a62-78fc225c94e1 | -5.78292 | -42.93896 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9f3ac9fa-80a0-3ac4-9558-5f7b581244dc | -5.41275 | -41.31573 | 2025-10-05 04:44:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47529173-700f-3c99-aa7b-ba4dc6eab6ef | -4.56826 | -48.60741 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7e2ea66-483f-368f-9a69-a4315084b7bb | -6.40202 | -43.05364 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f728d8ea-ffd7-3172-b062-b51e874b8acd | -2.25532 | -47.87801 | 2025-10-05 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 388b7f28-f35d-3ae0-8c6f-baf627aeca40 | -3.8105 | -51.07473 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf913b8e-0c5f-33e1-bd9c-fde706d35562 | -2.40428 | -49.36075 | 2025-10-05 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02274810-70e6-37ad-91be-b49c09cfe52d | -6.36083 | -42.87773 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3c455eb-1204-3d0c-ba73-df1daabd4a88 | -5.87536 | -42.54097 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 92f63fd5-6433-3738-89bc-22ed25e6ad5c | -5.0661 | -40.47076 | 2025-10-05 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 25190d1c-886f-3d7c-985b-43a701432611 | -3.81818 | -51.07306 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 445323bb-fedb-3e8d-8118-3851e4eeab42 | -4.4468 | -43.24042 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc2fce01-807e-3368-a7b1-44e16fdfbd8f | -2.90062 | -50.73778 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7453cef2-248e-398e-898d-6b7921b0ac5d | -6.08504 | -46.19047 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a26f5b47-8ae4-36bb-9b24-2118c92e18a8 | -4.14048 | -47.65773 | 2025-10-05 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be6f2586-408a-343d-868c-e91759c2ba0a | -5.00051 | -47.21472 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e82913e1-de72-3136-8593-71d3453541cd | -3.43143 | -49.49606 | 2025-10-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42183123-39c2-3731-8f01-e701dbd4621e | -6.67625 | -42.78213 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6bd4413f-5281-3150-bb94-f1a4bf3efcae | -6.15734 | -44.65527 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1be6a3cf-4681-3dad-9e63-98d665a59b8a | -6.12814 | -42.85957 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 33eb5cbd-3f5c-3f4c-b0ea-a50c0446e91e | -6.27906 | -44.0378 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d54d22db-f8b2-3c2b-8d91-8a50eeb61ca0 | -4.25563 | -48.56429 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 87315c29-3d22-33eb-a687-9ee5db1c41a2 | -2.55161 | -45.80379 | 2025-10-05 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd00fdc1-bc34-34de-b4c2-2cf56ccfc4f2 | -6.72658 | -42.16386 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0594818-78be-3fc5-8d94-4905cc7c1d1b | -6.67563 | -42.7807 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99e0ad0b-1de9-300a-bc57-c0af2377b28f | -4.31784 | -48.08827 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e5fe7f4-ae64-305f-abae-b2f6f8c9c5db | -6.12179 | -42.86212 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee7aea3c-6b9b-3253-b7f5-0e19ebeb98b7 | -6.70168 | -41.95037 | 2025-10-05 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4ccd0ceb-b119-3d93-abd6-9e533d84e316 | -3.66428 | -52.12856 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7c9351d-51a8-35d7-b5db-4e41fb2c0921 | -5.81651 | -43.73051 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 557bf9dd-1ccc-309c-8cf0-e005c749bb53 | -5.77957 | -42.92733 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 935e128b-8b0f-38c0-a4ca-c9e96591d874 | -6.14544 | -44.67545 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3138eb91-d5a2-3ca4-91fd-3c63392aaf2a | -6.41028 | -43.06631 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16601865-8f40-3b3b-b97b-a33a2604496c | -5.8004 | -45.78545 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc0eff28-61ae-3811-ac76-ff2adcf25e29 | -6.12663 | -42.87062 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93c52030-11e3-3b9d-b792-fdf51f4b3e46 | -6.44525 | -44.15582 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0b8fcdf-798a-3fef-813f-26da01a24c31 | -6.12312 | -42.85914 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88cbe7b4-eba8-3bda-b5fe-9696a34cd104 | -5.97335 | -45.88451 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae901180-9048-358e-a611-7adab63b3c7c | -6.35746 | -43.91599 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e3d6245-d662-3b60-a01a-d68ad61051d8 | -5.34805 | -45.30232 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 156e4bdb-c5b0-3489-9c15-e5838253da17 | -5.25277 | -42.63734 | 2025-10-05 04:44:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ca37913-548c-3dba-bb12-5650197f7a6f | -3.6747 | -41.76429 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb45103e-ddbc-3413-b6bb-81695a7ccea9 | -5.94613 | -42.87817 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a76bfae7-c126-3a2e-a349-8b5a06c3065f | -6.40765 | -42.68728 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51454573-78bc-39c2-b998-a7a83d1a0195 | -6.72089 | -42.16611 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bdc22355-49ab-33e5-a5fb-b72cb0a53bca | -6.08155 | -44.04337 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10370ff4-b49b-3583-9331-0224be40b5da | -5.55086 | -42.66705 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab60c96a-eaf6-3ea8-abf1-e8f0d5621f1a | -5.65241 | -43.19666 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a69019b9-47fb-3533-8a3e-921306ea82b6 | -6.36584 | -42.87834 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a25c7869-a92b-39b2-a51e-7f4959e463db | -5.18607 | -46.15955 | 2025-10-05 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f004293-b8c9-3a9e-a467-67af14fb5aaa | -5.76661 | -43.98413 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 05bd30eb-940e-3f02-975b-65e6ea09c61a | -2.69093 | -48.39739 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3f8af0-2b36-349e-af35-953ff67ec9d7 | -6.21702 | -44.08009 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c59e75e-b689-3bc8-8feb-5c1677a5051a | -5.82369 | -42.44052 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9eca6ed8-59a0-3d35-a3c6-b6a777057189 | -5.88715 | -44.284 | 2025-10-05 04:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aad57dd-2547-3686-8d99-e3b6221662cb | -4.26781 | -46.74461 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33f1a42b-bba0-35cd-a8dd-1d88656b73fd | -4.64942 | -43.18843 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 94eaac9c-cc52-3a33-a530-f641fa55b53b | -4.1216 | -51.08846 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66d1038e-a16a-30cf-a4a2-c115a766a830 | -6.2451 | -43.04613 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a95fb0b-6b61-3999-9a15-5a2572f464a8 | -1.49071 | -48.69281 | 2025-10-05 04:44:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ee716eb-af73-39e5-b598-1fb08363c00e | -6.127 | -42.86794 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b3fbdbcc-0a98-3002-bcc3-58a1ba985ad5 | -6.63683 | -42.80612 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc227916-ea03-3bc5-bcb5-5c7ab0652045 | -6.08226 | -44.03831 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a77576da-b4a9-31dc-ace1-44e4e78b83bf | -6.66873 | -42.83476 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db60861e-adf9-3c61-a7c0-5c7e70897b30 | -6.14918 | -44.6496 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README78.md)
