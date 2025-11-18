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
| 448bdb2e-0ce6-3568-a1cf-890dce97d44d | -4.70809 | -46.31158 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3699f8e4-e7d2-3866-be17-86a0e15b52f1 | -4.18008 | -44.2294 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 309b8db7-93a6-3611-afdc-bb6aa77dc0b7 | -6.77738 | -41.44017 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 409eccfd-02ac-3bb9-9fb0-a91bccff373d | -6.72175 | -40.80292 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cc823580-3806-348e-a4ee-46a1793f45a4 | -10.34795 | -48.91092 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f90607-9dda-3c99-9cb4-5a7d698c9871 | -7.24569 | -39.38749 | 2025-11-18 04:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0267a95-63e4-3eb8-9726-4716c1bffcb0 | -4.72041 | -50.95137 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09dc21f4-0f5b-317b-8bb0-f00475a64ded | -10.85117 | -44.09873 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edde33f7-6882-322b-a2a2-396e19f6ad1e | -6.44896 | -45.74422 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 728f928a-8f11-3e52-96c6-2e0e2e866e96 | -7.9659 | -38.28182 | 2025-11-18 04:21:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 480c3ca2-9439-398f-9a15-09dc88ece4f2 | -7.61786 | -42.58409 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 146bb627-76c6-38fc-bd94-88c15be85d8e | -6.40799 | -47.20507 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ddd3873-4388-3634-a48b-51cd7fc76f14 | -8.21103 | -46.19718 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0197eccb-4418-3bf1-ac9e-bf4835d1ea69 | -5.79231 | -43.99325 | 2025-11-18 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51045efd-4a64-3bb0-ba35-32a5b82db3b7 | -5.46801 | -40.98666 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 974429d7-b9ba-3255-8e71-9677c74b1e3a | -6.04134 | -45.82155 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632b728d-cd29-3079-9b96-dc81f74e2d74 | -7.8377 | -40.89869 | 2025-11-18 04:21:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c9717f99-f85c-33a1-9443-e8a32ffc996b | -10.85058 | -44.07991 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 933e17d3-6a41-3479-8885-ea8573e8d3d6 | -3.65755 | -50.4381 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fc5ad2b-0d96-37a9-a5de-b10adcde103e | -4.50179 | -45.93402 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed91cf99-2ca5-3592-8db7-9c9a067761f0 | -4.48754 | -46.59722 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a033f37d-8d85-3aaa-a339-b3a8810c110b | -2.33464 | -55.80059 | 2025-11-18 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb3f4c81-f913-30c7-ae23-19c796d577eb | -4.35542 | -44.34892 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a127438b-6974-3c14-975c-7acfc21dc6f8 | -10.85528 | -44.89185 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 044c1919-10f9-33fd-b8e7-fe9f34eecd21 | -8.86206 | -47.32272 | 2025-11-18 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b77434b-7079-3c4f-9d4b-ef0140c42490 | -7.38219 | -39.12311 | 2025-11-18 04:21:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ee54859-a1c7-34ce-ab44-86383d598e31 | -6.67344 | -42.03506 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 13914484-8924-3ae6-aa04-e1746d48001b | -10.50538 | -43.95601 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f8a1714-f7ab-3a47-89d3-637a88001d7b | -10.3758 | -44.25159 | 2025-11-18 04:21:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8473ac23-b7e0-35a5-8d93-386a0f4bf529 | -4.26526 | -46.81143 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5fa01e1-bf79-388e-9b85-f22202098a41 | -8.79446 | -44.38983 | 2025-11-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 508affb6-0cef-3185-8d64-39fc8559b0f5 | -6.94001 | -49.66744 | 2025-11-18 04:21:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0e7a3db-9079-31b5-8b03-c28fd90af6d1 | -3.89887 | -47.93658 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5418f5f7-aca6-3237-b067-da02baa1cf97 | -10.05349 | -54.32019 | 2025-11-18 04:21:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 362214d4-ccb7-374a-8c8c-4a397d4d2d8c | -3.2829 | -51.43106 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8fe9fa-a0b3-3e59-8388-5950a1bd1f41 | -7.43393 | -45.19502 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac9e4af-3f6d-3796-b88e-aa2d0b4670ed | -7.88134 | -42.87926 | 2025-11-18 04:21:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f365ad33-9941-3b0e-bf79-1445ce9d3407 | -9.72507 | -43.97058 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ad9ec923-0e5d-3c3d-a649-5ddaf903adc8 | -7.93125 | -39.14934 | 2025-11-18 04:21:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 881fb282-8634-382d-823d-e5a5bff4514a | -6.65401 | -51.29536 | 2025-11-18 04:21:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84e00ed-e49d-3493-baba-7cb6767b5a14 | -6.15598 | -46.1086 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db73a381-2168-3cec-9b40-d42dffb7b806 | -5.95583 | -44.72958 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7277c1c-3ccc-35c5-bb95-86d0d419c39d | -6.77628 | -43.54522 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d67a32ac-faaa-3d2b-bc5d-71e493f97468 | -10.79595 | -47.63951 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 409c554c-c5c4-3d70-9f36-b193a3775f51 | -6.40863 | -47.20115 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62ada266-d83f-395b-b967-d1aa65611ec7 | -8.57316 | -46.48389 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed0b85bc-92fa-30e5-8b50-a0deefbe240e | -4.6456 | -45.53091 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dc944bf-1e60-3ece-8114-982e90538008 | -5.59362 | -44.89149 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8827dff8-19c9-3ff0-8228-4c339d280c56 | -3.77928 | -47.74428 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18607ee5-239b-30ac-b20e-e85320943a3f | -4.61214 | -41.73235 | 2025-11-18 04:21:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 951debf9-7ec2-3133-9a95-ea97305b9960 | -9.10234 | -47.78171 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1170b9ff-f282-3c9f-a24b-06c30d1cb0a7 | -4.45457 | -44.21655 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23c3ceb9-5cf3-3026-a916-9351a2bf5d8a | -8.10562 | -46.06747 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8cec4dd-4097-3c51-b9f4-75480544f1a4 | -3.67438 | -50.80906 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b449c608-f19c-35d8-8d4b-792b88867b52 | -5.75055 | -45.10504 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 337f4eb1-039d-31c2-92e1-bb2bd80ec2e4 | -9.72191 | -49.13023 | 2025-11-18 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d1afc15-2e74-3320-a44d-ff76ff571264 | -9.51851 | -45.11291 | 2025-11-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 615161a5-d0d7-32cd-9746-68552540e81f | -5.86739 | -35.42067 | 2025-11-18 04:21:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 682c9bbc-3d66-3fe2-a13f-4171fe1715bb | -7.66267 | -40.15053 | 2025-11-18 04:21:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f97f60a-03ea-37c0-97dc-9ab2b86fa98c | -11.20315 | -49.41169 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cadfd292-7c3e-31ee-b32f-ea99e7b300f6 | -11.57431 | -48.14128 | 2025-11-18 04:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 154283c2-e439-34ab-be37-3499294da987 | -10.30778 | -54.20562 | 2025-11-18 04:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 679c8d1e-4309-3cdc-b332-1d045ca3bf66 | -13.85894 | -43.8214 | 2025-11-18 04:23:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06627f61-9377-30c6-93eb-9891ebb221dc | -12.74679 | -45.43205 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c85b05e6-5e83-32c6-b35e-cdd3f2ddb590 | -13.27344 | -47.29188 | 2025-11-18 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff5e3bcd-e7c8-3bba-91c8-7a3a8770e184 | -12.00566 | -43.83495 | 2025-11-18 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85b6b640-92bd-3a3d-8215-23a50405c30c | -12.23743 | -49.38046 | 2025-11-18 04:23:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfe62d2c-f069-34cb-8e7a-980d9fe1d316 | -12.63707 | -48.86729 | 2025-11-18 04:23:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 943bd1d6-bad8-37ed-beaf-9ea4b28dc2b2 | -12.23379 | -49.37981 | 2025-11-18 04:23:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a9dea83-0d95-326c-b45a-a7b58a0b730e | -11.93172 | -44.80995 | 2025-11-18 04:23:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3b058c83-dad3-3461-98ba-d937a262ec10 | -12.89248 | -46.06987 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0da67d14-4dd1-3894-8c58-dda84799af47 | -12.50756 | -49.86758 | 2025-11-18 04:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca0cf882-55ca-33cc-8343-36221f5136a4 | -10.3072 | -54.20877 | 2025-11-18 04:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01d0932d-b2ac-31f2-bdab-9dadcb29fee4 | -11.16148 | -49.45528 | 2025-11-18 04:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8062d02-6f8b-3000-8943-a7661478daf8 | -13.27737 | -47.28879 | 2025-11-18 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 602a4a4c-09d5-3587-a671-5b362e9df59f | -11.52371 | -48.95103 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c94288b-9467-3582-829f-a0e4690375ef | -14.40231 | -48.28119 | 2025-11-18 04:23:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a10d1f7-1956-3c37-a2c4-36d68b5e73cb | -11.52467 | -48.95431 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3561276-eea2-3ff0-9fbb-66b6f5193f54 | -12.86908 | -46.4128 | 2025-11-18 04:23:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23bc8700-3847-3f71-b231-46c37a0fd95e | -12.23305 | -49.38416 | 2025-11-18 04:23:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d037f997-4601-36d2-be66-b6491573fbbd | -13.35668 | -46.47161 | 2025-11-18 04:23:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 634e93f7-a7f0-32ce-aa97-fc69d360efa0 | -12.72797 | -45.40014 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaa00c9f-c92a-3151-bdcb-1c592654c205 | -13.10124 | -42.96641 | 2025-11-18 04:23:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a4d0f60-532b-36d6-a5c4-1abb0e3be878 | -13.532 | -43.01171 | 2025-11-18 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddbde4f8-6d4a-39e0-973b-273ca0ddde7e | -12.74293 | -45.43507 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1381de59-13d4-3cb3-8946-7da53dd7453e | -12.16324 | -47.42133 | 2025-11-18 04:23:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45f3e172-378e-3c7a-b2de-3ea9dd91d244 | -12.34068 | -43.14632 | 2025-11-18 04:23:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 878a3a8a-14ef-308e-9725-2a21adfcce13 | -12.68242 | -46.77449 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d102ef8-3429-3a02-bcd8-bfe254a332cc | -17.9742 | -41.70843 | 2025-11-18 04:23:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 077b659c-298c-39a6-ad7f-c4a150574131 | -11.29051 | -48.51402 | 2025-11-18 04:23:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 591a549b-46e9-383f-a8ab-0772aa0bad88 | -15.30495 | -42.40457 | 2025-11-18 04:23:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9375bb50-b68f-3aa1-933f-4c8331b4c960 | -13.45419 | -40.31539 | 2025-11-18 04:23:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c7a0cc2-6f97-3f46-b769-e0b09d3af6f8 | -13.26193 | -42.52823 | 2025-11-18 04:23:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74861571-b62f-33c0-9547-f39fa4b87e93 | -12.29033 | -46.80114 | 2025-11-18 04:23:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e5f0e2f-b9d7-316e-b4ca-a59adc1fd7b2 | -13.2015 | -48.31451 | 2025-11-18 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a154cd-4c1b-38e1-8255-3215b3f6419b | -12.86549 | -41.4841 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 403944a2-9e9b-3142-9e57-4c9a4a07fb4c | -12.69627 | -46.77312 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cb9f0781-41fc-363d-8848-220c837eb6a9 | -13.48317 | -46.44524 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c84aa0ad-d10e-32bf-859f-fb1bc2844426 | -12.85827 | -41.47894 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 95570306-9d5c-3610-9f2a-c33b7b67af4b | -12.72243 | -45.39198 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README33.md)
