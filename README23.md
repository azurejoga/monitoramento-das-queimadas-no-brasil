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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0122c657-2dfe-35c9-ac00-552378bdd28e | -3.31092 | -48.72033 | 2025-09-09 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4495cdf6-b7b3-3824-b60e-44f881d90b53 | -3.59571 | -58.54111 | 2025-09-09 04:32:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ce7c7f-5b73-38d4-bd21-a43f50b50808 | -7.02812 | -44.94448 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc043389-092b-3f1b-aafe-3d22ff09bd2e | -5.36779 | -44.77341 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50e932fb-9b36-35c1-8505-667ac67ff0a1 | -5.82178 | -44.12247 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 698610dc-1557-3498-86d1-6ae819926d37 | -5.53617 | -42.65401 | 2025-09-09 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e82e925-ca93-3c7a-a744-eecf66385124 | -7.247 | -44.45629 | 2025-09-09 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ebaba3d-7674-3a15-8f8a-583606e523f6 | -5.73557 | -45.27938 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2c0428a-bca6-3793-bf53-3bfc2426be49 | -5.91488 | -52.46946 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b83c4cc8-5d5b-3417-b5f0-8c83aa71005d | -5.72232 | -45.39978 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f50a3bc9-0198-3c0c-911b-dd5bfd7cd7a8 | -5.58322 | -42.9019 | 2025-09-09 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1437ec47-6b59-34f7-82cb-6d386c260034 | -5.48142 | -44.12214 | 2025-09-09 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8dc37e39-55ac-3610-b73b-79b1aab8950c | -6.34746 | -43.65443 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f26136b6-70b5-3b6c-a9bf-8552a19dae43 | -5.67459 | -45.39732 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5880e73-25a2-38c5-aee4-7175a1d978a3 | -3.48831 | -48.95442 | 2025-09-09 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e0ddf41-6cf4-3744-b12c-cae959aafdde | -5.93379 | -45.76685 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f583094-6281-3b19-8a75-d6c0c4e7dd14 | -5.85835 | -45.28798 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a987e974-b9b3-367b-9cf5-e6ac404da693 | -4.90062 | -49.92862 | 2025-09-09 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fc5e5cb-9a83-3276-93a0-f79f64b5b302 | -5.66297 | -45.4034 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 888cd5d0-c76f-350f-a0b5-9f6873821504 | -6.37044 | -42.58022 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| add2dc0e-70ee-3167-960a-e5ec908e7102 | -2.51729 | -51.90299 | 2025-09-09 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c85f286-0f66-3ba5-a25f-770c34039379 | -5.27168 | -42.78392 | 2025-09-09 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab15ea3c-b0fb-3742-913f-78f8b01dab12 | -6.40378 | -44.48695 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 140c088b-6841-3838-a09a-4aa932dfd977 | -5.19199 | -43.02771 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e76d5d10-02f0-3c48-803e-f5bf92e83fc3 | -4.62028 | -46.59365 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19bcc218-20eb-339e-8f0f-2b4526759bb6 | -6.19467 | -45.82474 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12cb835b-35c9-321a-b593-9fc3d2c25f7f | -5.70764 | -45.41425 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4beaf7cd-7413-31de-83f7-33a64bd7a27f | -5.89266 | -43.95417 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c0c11d0-5bfd-3a83-9d00-848021aba3f0 | -2.5165 | -51.90805 | 2025-09-09 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c86a3d30-fdb7-360d-a335-1c2695c5df00 | -6.05006 | -44.42659 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 406b4181-bec5-3ab1-8312-dd1aa76d089f | -5.8167 | -43.97458 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4e84ca3-7ab5-3e74-bca5-5a7966108f8a | -6.13646 | -45.47673 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e118d401-cc86-39fe-9759-b51e23d3f004 | -5.5803 | -45.04192 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f0bbfd6e-a07e-3ff6-8a6d-bdf44fbe8dc7 | -6.54474 | -45.92245 | 2025-09-09 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b6af4f6-e166-3fed-98a4-203bb0b64ea7 | -5.43007 | -42.8048 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 299abca0-8bf5-350a-bb00-0b461183dabb | -6.18722 | -44.73579 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80096887-f993-3c03-bc87-4e42aff6d2ea | -5.88758 | -52.09885 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf74974a-fc1d-348c-a376-c3fcb1785aef | -5.98143 | -43.69378 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc0337b-e035-3aeb-8661-e3ffad87b33f | -6.64798 | -44.08389 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57552101-ed72-3794-9b71-496be327cc34 | -6.18548 | -43.39033 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29070131-45fc-3b7d-a5d1-05877a9a15ef | -6.51272 | -44.71195 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a0b0df-4601-3aeb-9fbc-898076b57e55 | -6.77179 | -43.44139 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8d1dc43-e89a-33f9-95d5-5e3d0532fdce | -5.5815 | -45.03394 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| a7069a8e-c391-370a-bd24-3e4e17276630 | -5.67213 | -45.46005 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcd02e06-1095-3185-a1de-6cc4ee34f94b | -6.28326 | -45.61249 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d327f17-13fa-3911-9b38-1b20c63d3fc2 | -6.41909 | -44.48495 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7680887b-ee1c-3f90-8891-21a9d11d03a7 | -6.61803 | -43.99955 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af1d0a2f-f2dc-3a44-a6eb-3e6453b94137 | -5.81549 | -43.97616 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2be5c70f-aa3c-3f5d-9c44-1ee67623d194 | -6.87469 | -45.53166 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d221f41-2766-3a19-8171-334a9086dc8e | -5.44767 | -42.79685 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9cb52196-6d72-33c8-8174-27c51226d5eb | -5.85638 | -44.19613 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1593cb17-4f61-3b0f-b8b0-27960dc89635 | -6.40037 | -44.43314 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66cd5d80-bd75-3432-a7fc-8293133fe35b | -7.29225 | -43.6979 | 2025-09-09 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e74d6c75-351c-3cde-b7ce-cf4a356b3092 | -5.82371 | -49.92897 | 2025-09-09 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7b3f6015-8805-3b08-ac62-4aac6e130775 | -4.89282 | -42.21167 | 2025-09-09 04:32:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5671a960-95ea-3d52-a044-0022a05f5e0e | -5.89453 | -46.04681 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71a994bf-d83d-36bf-a36e-3937cf7a957c | -6.82548 | -44.89709 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9255776-48b2-3ac0-b9f7-20981007a2dc | -7.20057 | -44.8952 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5cd9c78-794b-32ed-a35d-a419edbd6b60 | -5.25225 | -42.71991 | 2025-09-09 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2222516c-3427-3201-ac72-e389f6e7ff9e | -6.21304 | -45.57055 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bc3bd3b-b394-3acf-a316-5d9b3c39e565 | -5.78848 | -45.43362 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7689bc6e-f9a5-3ad2-ba5a-39cec0c1c14a | -6.08522 | -43.36312 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f67940cd-6f65-3c33-b6f6-8fef389328ec | -5.92519 | -45.75396 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba2225a3-fd7b-34bd-8608-8178b0e01a55 | -5.00778 | -43.65513 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90d1dbbf-bca1-327f-ad06-c9d2378b07d6 | -2.43918 | -47.18637 | 2025-09-09 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83d341f5-becf-3f69-abae-7c9e4ec3dc4c | -4.35538 | -50.62674 | 2025-09-09 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44f53e2c-5f8b-37e3-ab0e-c4d3ac54db30 | -6.55799 | -43.90798 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9599ef13-5ab8-375a-98be-8c4731458ee8 | -5.94069 | -45.67518 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 380934c4-b269-3cc3-9513-81e975d92216 | -5.42901 | -42.81184 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f7deb4f-9360-34a2-b503-bbe4e3ea0885 | -5.57911 | -45.04986 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e9da14ce-e348-30b3-abbc-a3983036a3fd | -2.78936 | -49.61709 | 2025-09-09 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24e2bf4e-a98c-3087-af5f-63f824e39fc6 | -5.81361 | -43.83567 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7cec03-5e15-3ca0-b5ce-e74935fba360 | -5.55676 | -45.68788 | 2025-09-09 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5177efb3-7289-300f-8dc8-32559d58be45 | -6.89868 | -45.80749 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 654e86b5-a38e-3f3e-918d-cf6e8fdfaa3c | -5.87762 | -44.18097 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10e29cfc-4a5d-3a30-b4f1-f81e2f04f8b2 | -5.34978 | -44.79559 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8c9831a-f2f5-3c4f-9b64-cbaf23720535 | -6.10167 | -44.77942 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da0bbb35-5271-386f-af09-f5c1b96df5fd | -6.40158 | -44.43026 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 285d8cfe-a753-35da-a598-ae0297817fe7 | -5.87702 | -46.09293 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7aa39d-94ef-3651-9b2e-bd644746e9a9 | -6.4034 | -44.43818 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76720dcb-b003-3b7b-9916-18db60c3c50e | -5.84831 | -44.19943 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1ee1fd9-0554-3ddb-a8c4-875fc33b711a | -6.21592 | -43.50625 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6b9decf-17c8-3668-8a06-92e63889e94f | -2.79223 | -49.62148 | 2025-09-09 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56ea0021-bdf8-3daf-8164-a56259269e67 | -6.40042 | -42.9732 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7888d961-9080-3041-b2fc-b88ab48375b4 | -5.6803 | -43.89783 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3013666-6657-3147-8614-c3351a7aac46 | -6.89521 | -45.80697 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bca35f3-7533-3a80-8388-1ceb1a7902e5 | -5.49784 | -42.99541 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91b498ad-776f-3149-8196-0d3a336a415b | -5.93583 | -46.16911 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77edbb7c-688f-3a09-b4b5-aa7a9c66ec1a | -6.62427 | -44.0097 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3c2d78b-8fae-3d6e-b9e3-3aa20ba32e90 | -6.48105 | -44.00965 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ecdbe7c-227d-30a2-a0fb-1bc1026d75a3 | -6.78092 | -43.62639 | 2025-09-09 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e8e363f-57a2-3ba2-8d5d-5dea92e240b7 | -5.9527 | -45.78133 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab346ed3-dec1-3e59-a3d5-8d7b660899ad | -6.0574 | -45.55145 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 545819db-e240-388e-b286-3118f8eacecc | -5.68269 | -43.90754 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4524fc76-585f-3aea-8e71-ddd784f405c0 | -3.49703 | -49.56512 | 2025-09-09 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f10858ef-bf72-3846-870c-84c4275a6dcf | -5.48625 | -45.64221 | 2025-09-09 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4891a29-a3e4-3121-b724-e828057023fe | -5.7793 | -44.85269 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df113e0f-7f9e-357c-8181-963d629fa393 | -6.25362 | -43.7158 | 2025-09-09 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e57f02b-57e7-3ff8-9838-a8e7d9d6d229 | -5.81828 | -45.64876 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99e5532b-4a9e-343a-ac66-a4478ac0e121 | -6.09753 | -44.13686 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
