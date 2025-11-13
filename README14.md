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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6015e1ee-bf52-3b94-9ec3-9600a36a013c | -0.753 | -48.52937 | 2025-11-13 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93f37efa-8c5a-3523-857c-44c22d52a737 | -3.22439 | -45.59398 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7248d69d-f02c-34d7-aa5f-4953f794fcad | -5.08303 | -47.93196 | 2025-11-13 04:12:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c752dc7-fbb5-3526-9329-fd516e284772 | -2.45851 | -49.26858 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b76dd207-6ee3-366c-bc6c-db7affb74eb6 | -3.34956 | -48.38505 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81bf4579-631b-3514-a7f2-cbd51d89b67f | -3.43072 | -50.43932 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7f13c17-ee5c-3c94-bc3b-c18c52e03e40 | -4.3685 | -48.70589 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a1d0b8a-5bad-3ddb-8bca-83bb443a63c8 | -5.64966 | -41.07131 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 110eb1a4-9726-3091-8160-194e15bc103d | -4.68045 | -45.8503 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8de800-ed32-374d-a56e-0a8fcd7e27e3 | -4.81408 | -47.35003 | 2025-11-13 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e269773-3202-3b2a-9945-847e16c533ff | -5.60552 | -42.87061 | 2025-11-13 04:12:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c6e7d3d-f7b5-3a9e-a2f0-9c44bb41e15d | -3.29046 | -52.11116 | 2025-11-13 04:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f96ed4db-b1bc-33f3-83ae-57ad9ceb000a | -5.62308 | -41.06348 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2502ce5-cc6a-3bdf-b251-3a1c56a54748 | -3.67277 | -45.93063 | 2025-11-13 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9e8f577-e622-3115-9a64-f2caf7360437 | -4.2464 | -45.93494 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a5e6bfe-031e-3e95-840c-164320318c9b | -3.39909 | -50.17298 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01a59d5d-9524-3a1e-ae8d-105fcbbb6eed | -5.61913 | -41.06658 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7add8a1d-e671-393a-ac61-f8756da700bd | -5.83951 | -38.35325 | 2025-11-13 04:12:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 340d849f-5556-320f-9dc0-6cd4fdf01857 | -2.63365 | -47.3023 | 2025-11-13 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb211da3-b3d2-328c-8b3d-1e308aad9868 | -2.17358 | -48.37336 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56c46e7b-f659-341d-b6d3-b7655ebae237 | -4.24709 | -45.93066 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c559d762-443d-3224-bde4-71eccf308706 | -4.55808 | -45.7508 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff2936a-ca0c-31ff-b6e5-6beaa1899467 | -3.44152 | -42.54654 | 2025-11-13 04:12:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a4b8765-8e14-3c48-838a-7ca7be8ea419 | -3.46621 | -43.18779 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f44e29-2c3d-379f-bb2e-1b2d4ee12de1 | -4.013 | -48.80888 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 98ef9fe6-64d2-3938-95f1-06196fb66bbc | -3.17339 | -45.65557 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b337f1c1-916e-300e-92cd-09a9536d08b7 | -6.08639 | -41.63469 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bbb94199-ba5f-38e2-9c18-bd2116796faa | -3.3459 | -48.38023 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c771e10-b3e7-330c-8a7a-0d9b4b2d079a | -4.14669 | -47.65628 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d67ff829-d83f-334c-bc36-6165621509ee | -4.56742 | -45.67117 | 2025-11-13 04:12:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b776a605-d807-3b4a-8ddb-836380b702b9 | -6.3543 | -39.79483 | 2025-11-13 04:12:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 429b39fb-256d-3050-8d6c-6a600e3471d0 | -3.76374 | -47.72569 | 2025-11-13 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c0fd7e9-c9c9-3376-9394-ee7e2f1534b0 | -4.87179 | -38.38078 | 2025-11-13 04:12:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8892300f-2a19-3ad6-bbe3-a87b680de999 | -5.33306 | -44.78952 | 2025-11-13 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22515f24-d223-3b0e-ad6a-c44be84a6fcc | -2.87179 | -51.47037 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca1f73b3-1f7f-3bd8-a354-e498cf754982 | -4.3633 | -46.14251 | 2025-11-13 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c031af0-5168-3cc0-a931-4890066c9ec2 | -4.84286 | -42.37312 | 2025-11-13 04:12:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc32124d-a699-3262-aaeb-db578455f560 | -3.80719 | -44.06839 | 2025-11-13 04:12:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 390c94dd-6eee-3ecb-8ea0-ae787c0b7265 | -4.2102 | -50.09195 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4ad2c24-9c60-3e5d-92c1-8aa3b05b9c66 | -4.3948 | -43.08205 | 2025-11-13 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b651a885-ab95-386a-999b-0b1b8b1b6fab | -3.23234 | -45.5909 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83147de-dddd-3116-8513-b04b29b4ee42 | -2.55509 | -51.2446 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2036de1-9dd2-3785-ac74-d42c3e494dd4 | -5.41799 | -42.5697 | 2025-11-13 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fd8d4fe-b3d0-3b71-a9f8-56f0561d6af2 | -3.70484 | -49.02913 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eff72ba7-d322-3eba-84d4-448b6b4b4007 | -5.75347 | -42.72857 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 965256b4-7b2e-3433-a9f3-5f1a8a83f296 | -4.21548 | -48.57179 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c6104a65-e817-3b59-97b7-8acda5220982 | -5.26579 | -42.99671 | 2025-11-13 04:12:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4733011-cd72-32d3-8c00-9b6c436109ec | -3.86126 | -49.79235 | 2025-11-13 04:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d3967d7e-07a5-3bec-a69b-c62622409ddd | -4.66891 | -40.48861 | 2025-11-13 04:12:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2514de8-0003-3b9a-802d-13a4c05d3421 | -3.09938 | -49.27078 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc1beada-8f07-3791-a426-49ffcb74c348 | -4.89048 | -48.9682 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3f31646-e381-3932-8b60-eef47d30f2a4 | -6.10128 | -41.58238 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e87ee849-7be2-3368-83a3-b7b2a431c2c5 | -6.09971 | -41.61499 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a66d655-245d-3cd5-8c81-a5580b24105b | -5.44173 | -44.65808 | 2025-11-13 04:12:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71473bf4-1c03-3215-8cb1-3e7088eb93ef | -5.42526 | -44.65168 | 2025-11-13 04:12:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b60a385-1d90-38a3-8165-57bd95570be6 | -5.6491 | -41.07495 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 77cb05ce-fc78-3996-8391-6de03ffc82f6 | -3.16304 | -50.6283 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8c9df8-ddcf-3bf8-bd65-d1400bb2c392 | -3.66838 | -45.93436 | 2025-11-13 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfdb6578-ca29-3115-b372-11b78d021d70 | -4.67285 | -45.80582 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20720413-83ec-3e02-a901-21c956b72693 | -4.21788 | -46.34933 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef78931-1d9f-3183-af04-5f0fb2434bb8 | -5.40377 | -38.17922 | 2025-11-13 04:12:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf1c6b63-7256-357c-82b0-ad17fd0112af | -4.62807 | -42.81119 | 2025-11-13 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13af4687-cc67-3c51-9a56-0a18ffc2043e | -5.32733 | -45.19445 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5dd9a57e-845d-391d-b78e-198f1529aeca | -4.53017 | -46.43576 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| e8c66ee6-cb3f-3309-97e8-ef427a9767dc | -3.46066 | -43.17979 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 816fae01-aa3f-382f-98c3-bd1cd26beb01 | -5.98893 | -41.91619 | 2025-11-13 04:12:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00a09511-5d3a-327d-bc93-de8a0b8987ff | -5.60382 | -41.06791 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33544a09-cb44-3307-a85c-9d723f0a7c5f | -4.00817 | -48.97811 | 2025-11-13 04:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddef0bc4-0fb8-3785-a706-fa3d451cd4f5 | -3.57175 | -44.15869 | 2025-11-13 04:12:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2554d5ee-12d6-305c-872f-8be229a567fe | -2.45082 | -49.2573 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92cbc3eb-ccce-31db-b72f-272c2a3e3e81 | -3.66959 | -45.69407 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b7303bb-6fc6-31d8-94c0-86e40adf8558 | -3.32565 | -45.61729 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5963e615-8d97-3830-94e5-5d1025ffdc5d | -3.36611 | -48.4045 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4de39a91-7d36-3929-8c1e-4ac31a0f9b86 | -4.12727 | -46.84242 | 2025-11-13 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3112bc0-c68b-3d2f-9179-3a6526051c93 | -5.24327 | -42.64054 | 2025-11-13 04:12:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20806029-cd88-3dd9-82a3-aa3dc1f05d43 | -6.09191 | -41.62111 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a84f3dad-5e63-39eb-96fc-1facfde71ea2 | -1.53665 | -47.21809 | 2025-11-13 04:12:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 673a5d5f-d7d4-3abd-94fb-d4dd18e97298 | -5.62363 | -41.05984 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fcee8e3b-0c9a-3145-9899-a533b70d3d49 | -5.6457 | -41.07446 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| effa338a-a9ea-3514-bf74-ae9247a2cb95 | -6.10408 | -41.58648 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 645db901-cfe5-3b14-98b7-1de274a7c0cf | -3.85531 | -42.7492 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d63b259-ec32-3d5a-beea-4093cfcd359c | -5.61073 | -37.94607 | 2025-11-13 04:12:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c1309f6-9373-327b-a385-49f5ad69d77c | -3.09823 | -49.27315 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1133fc92-8014-3631-97f4-16663702856f | -4.21185 | -48.56697 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 02c6c242-391a-34da-816c-d89dd77c0494 | -3.34891 | -48.38911 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b6501881-854e-3490-a7c3-77a2102e7150 | -5.59422 | -41.08507 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b041cea2-8265-3ce3-a99c-c4e40f23d9fe | -5.41415 | -42.57263 | 2025-11-13 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6aecd79-9477-3ed6-bc85-14ff6d40803e | -4.2054 | -50.09121 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d08157e-aa2b-341f-9c2c-f7944ada4da7 | -1.24887 | -47.06042 | 2025-11-13 04:12:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ece434-fb61-3298-ae1a-bda13526e6dc | -4.12189 | -40.57756 | 2025-11-13 04:12:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8ec3b7e5-740c-379c-a2cb-94a336a1aaee | -5.71729 | -42.76527 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f441d1f7-60e9-35a0-badd-8ed9e8ffb652 | -2.4364 | -48.62126 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73255093-dbe4-3d9c-aa00-3ce3c3b67c2d | -2.63676 | -49.22052 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6ebd4b5-349a-324c-a3cc-4653bb46a084 | -5.36134 | -45.40821 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e69bf9a5-b333-3d38-b111-dbb2df515a8e | -4.6425 | -48.74765 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8649e72c-36f2-3b34-9301-d32a4ec102a1 | -4.57835 | -45.7627 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c38fc87-ad4f-3e90-a222-df000d6209fa | -2.63525 | -49.20058 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ed3d3c-4e3e-3ec0-88c8-c0c569b4bfb9 | -4.26675 | -43.65577 | 2025-11-13 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be41094c-a3ea-3f7a-99c5-3c9d5822c7df | -2.94705 | -45.54816 | 2025-11-13 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56e5da2c-346b-3281-9e9b-cdf2532c7436 | -6.79435 | -35.2724 | 2025-11-13 04:12:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
