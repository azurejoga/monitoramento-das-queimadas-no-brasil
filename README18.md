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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69361ee7-288b-365e-81b4-df98cdcb1218 | -7.771 | -42.51803 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c47f4843-f76d-310a-bdf0-d7436cfda193 | -4.70127 | -37.37152 | 2025-10-03 03:42:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e00c887d-b03f-3218-a0ff-7c7451380af1 | -6.12864 | -44.02907 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b6bef5e-d500-3787-a90c-994c2217edfd | -7.7826 | -42.50545 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bf778dfe-ca23-3496-aa1b-23e36bf56a13 | -4.67046 | -45.80993 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 3418123a-5ab9-36c5-b694-1ba10b2ea732 | -6.28166 | -44.05396 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92690aad-01ff-3f5a-add9-5c252f235797 | -5.78359 | -45.75663 | 2025-10-03 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ccb473a-f589-3ed7-83a0-dab51d853fda | -4.66511 | -45.80518 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 0ed29ed5-0c8d-31fa-85c9-6e146355b57e | -4.65456 | -45.7949 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| f526032f-1d46-34a6-8eac-340648fa4778 | -5.23589 | -45.17009 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd2d6c2f-95d3-3096-b5f5-4e78fe3fec8e | -7.06002 | -43.30583 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43e07a1b-c44e-3859-81f8-d9bfeb267060 | -7.75798 | -46.22489 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e321878c-0c7e-33d1-b0f3-fb95731de5d3 | -5.64236 | -43.90153 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 36a21503-ac67-336a-8423-d84a410ed2d2 | -6.94332 | -38.56812 | 2025-10-03 03:42:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2fa8175e-3385-3b07-bca0-9a2b23d1ec91 | -6.23961 | -44.22972 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9235b36b-e24a-3e77-af64-00be84bf0298 | -7.05593 | -43.22433 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f3b3d994-00c8-3b33-8b02-e25fdd136db1 | -6.28086 | -44.05155 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc64323d-fb3d-3d29-8334-31dcadfd592f | -4.61588 | -43.15047 | 2025-10-03 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de89957c-4bb0-3d5d-8c9d-63d640873a92 | -6.32815 | -43.88209 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d67c9a39-27f4-34f7-9f84-e55a95efcea4 | -6.2868 | -44.05519 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8767a306-0d51-352a-bb8f-a056ac85674a | -7.76322 | -42.58943 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ef281e9-df80-3f0e-b4b3-39ebea4d6eac | -6.34493 | -44.30505 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce041430-8858-3466-ab95-11bee0323fc6 | -6.9271 | -44.40882 | 2025-10-03 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a920ac3-dfca-32f7-9cfe-bd90eca6f9ee | -7.66782 | -47.28372 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 273b9e02-60df-3410-9304-e979f4c16044 | -2.24745 | -47.88037 | 2025-10-03 03:42:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1b906eca-ad19-32fe-92a4-d4f77c626a4e | -7.78798 | -42.50154 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e9dd8d53-609b-3f1c-a685-92fa338ad509 | -7.2954 | -44.1901 | 2025-10-03 03:42:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 935ef172-ce62-3a14-a633-04efbe0acd03 | -7.74731 | -46.24982 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f789bf1a-6728-3978-8cf9-6683d1f29568 | -4.65906 | -45.80456 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8936f08c-fb28-375f-9fde-ea24d21d88ce | -4.65303 | -45.80378 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 83d2f22b-0bc1-3b75-8cd2-64e5059ec935 | -6.03536 | -44.6286 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8e6c3b3-902d-3601-8601-af242ca92a24 | -6.87512 | -44.51742 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d73ec1a2-bcd5-39a8-880a-e96aaab161a4 | -6.55798 | -43.89608 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a952987-e5be-366e-8817-c387e1c8c029 | -7.05984 | -43.23066 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5231f983-6f36-3ecd-9495-ca43b1129efc | -6.66369 | -42.81205 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| aed17be9-6fec-318b-b47d-465c8dbc06ef | -5.64131 | -43.90771 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e20ecb6-8cd7-353d-aee4-413624cd2588 | -7.78195 | -42.56326 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfc43c21-9a17-3457-a5d9-ebb2d5d9e594 | -7.24673 | -49.41154 | 2025-10-03 03:42:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e0b0edc-7e98-36c9-8d4b-d74934909365 | -7.80378 | -42.51878 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e23f94c-0b23-30d1-a4cb-d186d25442d5 | -4.66134 | -45.79128 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 31e242a0-01ff-348e-9ff9-eb10ea6dc436 | -8.45394 | -41.89776 | 2025-10-03 03:42:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b492825d-6a77-3851-b59f-71c1e3ca477c | -6.68303 | -43.71175 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79b52990-4b8b-39b4-8f56-36aa8ed4d665 | -4.6649 | -45.78777 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5331bcc7-bde9-3714-9952-b8d3db62fa31 | -6.05651 | -44.63548 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cee4990-ce3e-3124-97dd-9d61af9351ee | -4.8988 | -45.73077 | 2025-10-03 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c799980b-ce80-3585-b0df-fbd9889f758c | -5.19064 | -45.4229 | 2025-10-03 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d683d53-2457-3d41-818b-e56c55994fd6 | -3.84685 | -41.57359 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 67219509-5743-34d5-956f-7738324d4cfb | -7.77489 | -42.57669 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 68815e1a-f90e-3f77-b49a-083948566966 | -6.94807 | -45.44081 | 2025-10-03 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7954cd8f-a0fb-3ae9-bbca-d88809645ae8 | -7.56158 | -42.39333 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ad8b7f6-c0ea-30f2-be62-8fbfeea9b3eb | -7.77801 | -42.50483 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9c296d72-d55c-39db-928a-8fac14815dfe | -7.77154 | -42.59594 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9fc26027-d781-3b55-b439-0174105b9982 | -4.61992 | -43.15709 | 2025-10-03 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ed434603-745d-3642-815c-bd7a5c7c75ea | -7.25027 | -49.41286 | 2025-10-03 03:42:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c7c5f152-0fdb-33a6-8dca-d1a967b34c4f | -6.27706 | -44.04975 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 302dd788-eae1-3e3b-89d9-108b0a498def | -3.09513 | -47.01223 | 2025-10-03 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a49c4e90-27d2-3daf-a3aa-b57a3d2bb779 | -6.38093 | -44.63124 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dac35104-9f85-3e51-a97a-626cfbdf9930 | -6.2407 | -44.25499 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ac62161-e42d-3905-9c25-b5a331a4109e | -4.61538 | -43.15341 | 2025-10-03 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93c89990-3f3f-332b-94d8-910112ca0a9b | -6.29117 | -45.08213 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d9d0e1e-9226-37f3-a81b-3f952c1deac3 | -7.7803 | -42.57273 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a57f0797-a69f-3fdb-a101-d5d347375728 | -7.7457 | -42.58156 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 784f21ec-1e62-317e-bbdc-5b9306f5c785 | -8.54412 | -41.14831 | 2025-10-03 03:42:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed9fb443-0125-36fa-ba34-7d15251453ef | -6.23845 | -44.23648 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c7ea727-60bb-3312-b477-3037133e9893 | -6.41746 | -43.92882 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b577f9-0b8b-398f-8033-76ea826f1bc2 | -6.79825 | -44.74628 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca37dfe1-5360-3b49-b5ef-a2a02aad476e | -6.72528 | -44.14377 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f70ca574-18e6-3d54-a8d1-450e52ae7a54 | -7.19703 | -45.38528 | 2025-10-03 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81265d3d-5d7c-360f-94cd-cf945b883633 | -6.67724 | -42.81854 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13414ae8-b852-3e83-9082-6ecfcc49c195 | -6.37377 | -44.6405 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c806235-7485-307f-9d0f-20fb071beafd | -6.24057 | -44.25363 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e08cf1b-59e4-3012-a3e8-38d24f4828fd | -4.66104 | -45.80933 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 08960739-4c88-3a46-8c72-2bb3ac7635dc | -7.31775 | -42.87615 | 2025-10-03 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8537e6e9-d5bb-35e2-8406-ec3f8b8744ff | -7.71286 | -46.2123 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9f5e8ed4-c906-313a-96ea-6bb70639612f | -4.60221 | -45.13001 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36946a09-349b-313c-88dd-433802733c73 | -7.76237 | -42.59425 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c4289ba8-bccd-36a8-b1ec-0f6983f6d95e | -7.75 | -46.26794 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 069bbe65-495d-3f70-b1bb-4b8dd198711d | -3.84762 | -41.56887 | 2025-10-03 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5a30981c-ad47-3c2b-924f-d4e199862d19 | -5.35107 | -43.74942 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 01d931c3-a7df-3b0d-87a4-935cf7b7013f | -7.30426 | -45.2608 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de8ad3b9-c7be-38ba-a926-be225470b435 | -7.3036 | -45.26446 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 360bd634-acf9-33f9-9db7-35e0c6840645 | -7.7772 | -42.50946 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0ea31619-23df-32be-992a-1cdf537a66a0 | -3.94062 | -47.56785 | 2025-10-03 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5cb37260-80e7-30fc-8958-5a476ed345b1 | -5.40339 | -41.34002 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ec3e132-a707-3c2b-a010-1eb3af71d1ee | -7.7678 | -42.59027 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d667aa44-9d11-3abc-9c4c-fbd2ed9f81d6 | -7.77238 | -42.59109 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| fb595624-9657-3d6a-85e6-a3f981c9d3ca | -4.67267 | -45.79702 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c8fb2746-0c92-341d-bd46-74fa3c615fb8 | -6.66223 | -43.85866 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed86ee35-a5ae-37c0-9955-688b8770b93f | -4.76499 | -45.32626 | 2025-10-03 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b52ceba8-6e88-3b68-bf2e-4cf9e46490e3 | -6.34521 | -44.30787 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f0fccc2-86da-3583-b961-a8f7011377e3 | -7.75363 | -42.56335 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b6efd73a-0a78-39f0-8a46-c61191a26102 | -6.05935 | -44.6289 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4d70a9e-9ddc-35bb-b4c1-65d3b4f7b5e5 | -5.63456 | -43.91594 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7a01358e-b476-3457-a818-896221c4ee6c | -7.76696 | -42.5951 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5baf8245-e5a5-36a2-8152-fefd62649665 | -6.70973 | -42.80618 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 82d26924-f4d6-34bd-8237-a61b915bf313 | -6.73906 | -44.58041 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e8013ef-1e10-3d6e-83a7-ae77e43c3a2a | -7.56075 | -42.39804 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| df3848f2-a590-39d3-9c6f-a9a5b47f1286 | -6.22672 | -44.24162 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb56f797-829f-3f64-86d6-a7a658ff95dc | -6.73368 | -44.57968 | 2025-10-03 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff5d82e0-7cfe-3e9d-9984-8af406d3610f | -6.35145 | -44.29902 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
