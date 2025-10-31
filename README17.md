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
| 25bd7a57-fe55-317b-91dc-9cb040b3f3e0 | -4.57082 | -38.28541 | 2025-10-31 04:06:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a996218-943f-3a9b-a59a-540386a85fd3 | -4.02481 | -43.23148 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c8f9b4f-34cd-3fde-8561-5ad4ada4b5d3 | -5.64026 | -45.02111 | 2025-10-31 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c812b72-b4ef-3199-ae82-27c9a519e6a7 | -4.91797 | -47.32702 | 2025-10-31 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2791a4a8-3aa4-3d79-979c-7089d3418e34 | -5.13469 | -49.69648 | 2025-10-31 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caf0c445-3506-33f0-8b58-572799956007 | -5.6163 | -45.97985 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4a73a58-1f85-3380-b228-94a8e1f0a600 | -7.04915 | -41.47453 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 92e18d76-f6a6-3620-bcf6-1b89d6fada48 | -5.91111 | -45.57456 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d4684b-f62b-345f-b810-adcddbb3568e | -4.99389 | -44.73121 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fced2be2-6a0e-3e4a-83d3-bbab33698f96 | -4.95725 | -45.87961 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f323b50-91cd-3ff5-8d52-3090aa3b84af | -4.66809 | -46.42416 | 2025-10-31 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d33531ad-3148-302a-bc50-5a627c5bd59b | -6.16576 | -41.62461 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 278f822c-99e6-37b1-9205-ff0fab11954e | -3.79077 | -43.89864 | 2025-10-31 04:06:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f21b2820-b196-3889-9774-3b7ec57f1b80 | -3.00824 | -44.96415 | 2025-10-31 04:06:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cdd69f7-94a3-3b52-b38b-14366a76ca3c | -3.519 | -46.00172 | 2025-10-31 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cefb5d55-ae4f-3884-aacf-eff567595ce4 | -4.45373 | -42.59651 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31bcfb13-c4de-34a0-891b-3f7b66e35a3b | -7.39807 | -42.46622 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 76179fb9-34d3-37da-9c0d-19cd45ade3a8 | -7.15914 | -39.45446 | 2025-10-31 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dfbdca52-df37-3258-8c15-83b0a3d2f650 | -5.81161 | -40.83279 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7306038a-fa60-36dd-9089-3cb2c0aee601 | -6.36042 | -40.97241 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c936500a-882e-39da-b52b-429296a815e5 | -5.80143 | -40.83171 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f579f6e9-f6dd-3136-8bd7-3138580e3d89 | -5.44055 | -37.60343 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2df0e122-fa5a-3344-8b63-d900650a0c5c | -5.02981 | -44.81391 | 2025-10-31 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7601c468-2325-31c3-ad47-89f6e5c12421 | -2.04511 | -52.08143 | 2025-10-31 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa88a6cc-2b06-3929-8113-01a9a60b0c16 | -5.52667 | -41.24048 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fdd4e111-42c9-32f2-a6e1-ae72664aa819 | -2.44726 | -49.03523 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64e989c5-046e-379c-bf3a-832d4311b3dc | -6.36373 | -40.97293 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47179591-5b1f-3097-89e4-f7a8d82395dc | -6.16191 | -41.62754 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4743f567-a361-3384-8cdf-22601185def0 | -4.76947 | -43.57568 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f28a3209-df36-398b-bb81-8d1320795c1c | -4.84837 | -42.73375 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 584e8571-3087-30da-9ce4-7a021160cefa | -4.25044 | -45.74734 | 2025-10-31 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91526069-f8da-30e7-bdb5-614d387637bb | -5.78984 | -40.81924 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52f34384-2ad7-3167-b694-910f07aff60d | -4.00887 | -47.41901 | 2025-10-31 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d468d248-ef4a-36ee-aa1e-873dfd8dce8d | -6.15569 | -42.39369 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 43a3b1c5-c5d2-38cf-84a5-75237a8dfd5c | -5.46187 | -40.87328 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c36e4882-4d44-3677-b809-7afe544bdc4f | -6.53015 | -43.70966 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40f516b2-32e4-38a7-9b66-76f44b45cd69 | -6.10526 | -41.72839 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e68ecb8b-6f4e-3d94-a948-e32df4c2dc3f | -5.738 | -45.58288 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7eb38fa-e9e4-3ffd-980b-d40c059ac1f6 | -6.55622 | -44.02316 | 2025-10-31 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad59c43d-9c19-3cb9-aed4-1a97632beea6 | -7.01848 | -38.83464 | 2025-10-31 04:06:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c6bc7866-c5b2-30b6-8790-f62f1b981b11 | -4.15551 | -44.5191 | 2025-10-31 04:06:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fd49782-7aef-39e3-8360-cb71e8942848 | -1.05383 | -47.34864 | 2025-10-31 04:06:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4273d671-9288-3b5f-8962-35ba276b56fd | -3.2873 | -51.91938 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e401dac1-d20e-3742-94bf-ec2c0fd71b67 | -5.91665 | -44.52158 | 2025-10-31 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d103bd22-8e3e-3291-a5a4-cc37d96b1e54 | -5.63914 | -41.08524 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 831671b6-b042-33d5-8929-735dd3835b41 | -1.35992 | -49.03111 | 2025-10-31 04:06:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdac9a8-db2d-3dde-aeea-7b13e4a762db | -7.44532 | -44.24118 | 2025-10-31 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a15ede61-7812-324f-be68-86651bfa3975 | -4.90405 | -42.97912 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ae5c901-7238-3fa5-9658-3429edee7255 | -6.94442 | -41.55714 | 2025-10-31 04:06:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b36a28e-2b92-31f1-baed-3e2e63ffd363 | -2.04594 | -52.07649 | 2025-10-31 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2db040f6-4e70-3580-ab40-0e616f46f58e | -5.44321 | -37.60202 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20e412a0-63b9-35fb-b4c9-9f170016fd79 | -4.93326 | -45.73058 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d31d6d2-48ea-3d26-a2b9-1b5e237c61f3 | -3.29263 | -51.92493 | 2025-10-31 04:06:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab6aa5e5-c75a-3ba4-9521-20e3d9ab2173 | -4.83797 | -40.73595 | 2025-10-31 04:06:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63b11b4e-1f55-31e2-a53f-50a3283b71fb | -3.94445 | -42.46864 | 2025-10-31 04:06:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c42b6a89-d7da-3ec8-9f6f-e0216485b004 | -4.76247 | -43.57455 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63264596-d371-3674-925a-7870316fe314 | -5.95522 | -45.55951 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab5ce488-9e13-3fb2-88a4-bb30cd7d7626 | -6.53361 | -43.71024 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82de858f-3b5b-36ee-b411-3b21accd7783 | -5.4744 | -44.31858 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fb9f54e-2d4a-381b-9710-6fc0a3ee02cf | -5.62499 | -47.11859 | 2025-10-31 04:06:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e37698b-c01e-316f-938c-204e5c7731ef | -4.05437 | -47.50463 | 2025-10-31 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17e6c540-24ed-39c2-9dd4-ccb903895fab | -7.64308 | -42.29443 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8aaacbba-b6b2-3015-8053-84a091e340a4 | -4.30867 | -41.44322 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 512e2525-2989-3945-aae0-013df922a118 | -3.61316 | -40.38181 | 2025-10-31 04:06:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abe7d53c-60bc-3157-96a5-b4470f7733bb | -2.91364 | -48.72828 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d3ba87a-5ae2-3a9b-98ac-4364b18c88f0 | -6.3018 | -42.3303 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41aea33d-e3a9-3c9b-9fd3-03ff0b6469b5 | -3.94246 | -46.972 | 2025-10-31 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d97082a7-53f8-3f47-917c-204c01b264ec | -3.17395 | -45.65769 | 2025-10-31 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90cb2591-727a-3b3c-9542-c33e88005b04 | -4.67137 | -46.51997 | 2025-10-31 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceccd4db-2317-3e5e-944a-16c249ff0784 | -4.13021 | -43.98672 | 2025-10-31 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7ebe71d-6ba9-3d05-b57e-4ee2b70c2dbc | -5.4556 | -37.59498 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24380444-40c8-3a97-9a01-bfc7e9509168 | -7.25279 | -45.5756 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8db47116-a8f8-37a6-a28f-b529362c97b3 | -2.76233 | -45.39172 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 869a417b-788a-3c28-a02e-7e5a6c366dde | -5.23297 | -45.47247 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1d0f911-2f20-3bf7-8697-e97ddfa0e0de | -4.67001 | -45.81187 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10a1de29-a034-377e-84a7-a0171be3d375 | -5.41316 | -41.24687 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6790b60b-e346-3091-a983-5adc2752643a | -2.88836 | -47.85126 | 2025-10-31 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e250caa5-316c-3776-a9a3-4593bf9f89b1 | -5.78762 | -40.81179 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 71271bfb-71d4-3a28-bc24-7c7df9159802 | -5.81329 | -40.84368 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a3ca32f-2b45-3c8a-a6bd-cafcefdc7f81 | -6.19626 | -42.51944 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 10d38b3b-71fe-3197-a412-ae484120fec8 | -3.14285 | -49.41935 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6241bf7e-58ff-3e60-8556-be79e3fdbe0e | -2.32174 | -48.58313 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a3c1348-d146-39a8-96bd-870d23ccbd82 | -5.11278 | -43.29458 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ecff5499-997d-347d-964e-db09604a487a | -5.95983 | -45.55538 | 2025-10-31 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6fa7123-d4bb-37d8-a053-0f15ad236c79 | -6.15682 | -42.38666 | 2025-10-31 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 78473862-e74f-3b3f-a0c7-02a0934de535 | -3.78135 | -42.41028 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64ad1c29-78ce-314b-8cec-dc06c90593bb | -5.62333 | -41.53156 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a65ad83f-acec-3103-8da0-912673c6ed28 | -4.02066 | -44.82062 | 2025-10-31 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea12ee1-ad7b-30c6-81d3-3f7704eb151d | -4.05061 | -47.4995 | 2025-10-31 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8adb89e5-c417-3870-9631-951d380398f0 | -7.44234 | -41.22089 | 2025-10-31 04:06:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| deaae865-6e92-3e44-8378-fa05fad4814b | -3.93813 | -46.97135 | 2025-10-31 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e273ff56-cc27-31b9-920c-b26235f5d6b2 | -5.3038 | -43.52344 | 2025-10-31 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80d42f92-dfa0-3492-b5bc-7bb675d26128 | -3.95767 | -43.26045 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8d25c5d-da9f-3bfe-be1f-d3bc868a5a0f | -7.18255 | -43.79729 | 2025-10-31 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c752dc0a-6107-3570-a193-400b67b6247b | -6.10691 | -41.718 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a519ac21-5517-362f-90f1-c73b6b5926a4 | -4.7689 | -45.99062 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f287980-a381-3e9d-9eb2-4bf3d8026938 | -4.30536 | -41.44272 | 2025-10-31 04:06:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4eed28c7-4589-35e2-a6fb-99c1284c3756 | -4.55678 | -45.64922 | 2025-10-31 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0156f1cb-74f9-3695-98a3-9607ad84542d | -7.31477 | -44.95494 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| aca87291-0d69-3d9d-a686-db1942d69ec3 | -6.80908 | -44.45046 | 2025-10-31 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
