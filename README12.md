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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cddd7ae2-4ecc-3b1b-adb0-8940eed42723 | -6.12345 | -42.95637 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b4b10231-97b7-3939-9f3d-c78c39874a9c | -6.94383 | -46.05884 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3827d600-9546-3e5b-a93a-546fd172b5c0 | -7.25572 | -44.32335 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e20f9fbe-4f62-3b7f-9283-9cb98056eac4 | -3.51423 | -47.22128 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35237633-d176-3734-a039-2f678e79af50 | -9.07415 | -40.48082 | 2025-08-09 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 33dbe03b-51d1-3260-b06d-94eeae02fc17 | -8.88689 | -44.78727 | 2025-08-09 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f638499-4fbf-3a30-b617-97aa7a8475f0 | -6.29252 | -44.98772 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c11d83bc-019c-37ce-a575-c1b3270e8f8c | -6.67512 | -43.34451 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea60d877-79a6-3eac-951b-ab8fa1c82c4e | -7.20952 | -44.6567 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b09bb6f-a9dc-32be-9c60-4dac0ad7509a | -9.65332 | -43.85009 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51684738-1eb2-3902-8811-87b546580c51 | -5.42323 | -41.23293 | 2025-08-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dac41f8e-18c4-3482-a9fd-a5a988cf7d58 | -6.09705 | -42.18519 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13b270b4-d45c-3a72-bfee-14caea9c0ab1 | -5.21695 | -46.07639 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| aa56656a-8294-353b-97cc-621a668deadb | -7.25761 | -44.63496 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45346f9b-5019-316a-a3f6-5df8831fad8e | -4.8187 | -47.31869 | 2025-08-09 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 371e578e-c3ad-3d49-a4a7-4306a2cb0ba9 | -6.0538 | -43.74908 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6100278b-5e6c-3d9d-bd8f-f94298e6389a | -9.38711 | -40.25376 | 2025-08-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2102caf-59dc-3ba9-99ff-ff00181304a9 | -6.55304 | -43.19043 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff19124-33f3-3bcb-a983-2e4f7f43ccd9 | -4.29532 | -48.06216 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ad77675-54ff-3c9c-a12a-5e4c222f1405 | -4.86289 | -43.23066 | 2025-08-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f68514c0-773f-32de-ad4b-569f54c77c29 | -7.42327 | -43.97414 | 2025-08-09 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35acf3d3-16a6-3841-99f2-a13f158dc8f3 | -8.07907 | -46.83991 | 2025-08-09 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da80cf52-f428-3bcf-bce1-99a9096a3cd9 | -7.29372 | -39.64165 | 2025-08-09 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2c1c1fa-21ed-391b-95da-2f5f51770a89 | -6.48612 | -44.41399 | 2025-08-09 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fd84be9-f275-3a00-8eb0-26b6f31047b5 | -6.13522 | -44.54436 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7986e51c-7fe1-319c-993d-cc51f64cecfa | -6.13263 | -42.96493 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bd4692e2-d6c2-3641-9268-6e8290856c3f | -4.74137 | -40.75834 | 2025-08-09 04:14:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d800cbfc-6d08-33be-a763-a1c9fa2b2935 | -9.66047 | -43.84766 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5551d6ec-57a7-377e-aa5c-d789f77a9043 | -4.69004 | -37.39196 | 2025-08-09 04:14:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d6b915e-2987-3445-9958-d7d0d4d48599 | -6.64426 | -41.87197 | 2025-08-09 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 619f8096-2bff-34ce-9a46-14873764fed2 | -6.94324 | -46.05952 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43daef1d-7dca-3e8e-aac4-b58262449a82 | -9.65993 | -43.85114 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad4449ba-5655-34fd-860e-7f2dcde7a71b | -6.64838 | -44.63269 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b40a5bce-3d07-3295-8901-7c3d971b98b4 | -8.05525 | -46.3183 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5f8be7-9c11-324f-9b11-5c09096a1470 | -6.6043 | -43.38245 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1cbaf8d4-3535-34b7-9c48-eeeb0028a19a | -7.08271 | -44.5159 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7574fe5c-88d1-378a-a9a7-e4fe02911912 | -6.57975 | -44.57419 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0aa62ab1-4a71-3668-9dfb-4160eeace2dc | -6.06483 | -43.74369 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04345e4-7bf6-30eb-999c-47f494b49f12 | -7.89679 | -45.56115 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d81a8721-f289-33ba-a730-a75141f331c8 | -7.6057 | -45.29404 | 2025-08-09 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17f83f5a-5879-354b-8813-e4e4e9ea2b56 | -7.08441 | -44.39672 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf3f07e-3eaa-39fa-b1c6-8070c64910e0 | -6.62195 | -47.28814 | 2025-08-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a06d5150-78f6-3992-8b79-e60ffe6a0608 | -7.03752 | -43.55066 | 2025-08-09 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d79bd6ce-4748-32ea-9cf5-70c27a077193 | -6.66851 | -43.34348 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cc709e6a-0e65-3f66-b9af-7deef9055966 | -6.62572 | -47.28872 | 2025-08-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6c52297b-c849-318f-bf59-4a2e0ce4c46d | -7.41996 | -43.97363 | 2025-08-09 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f34f8d6-9cbf-3d26-849f-ef41c4fc3369 | -7.40382 | -47.13775 | 2025-08-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9012d2d2-b405-332e-9fa0-55b18ab60176 | -6.23117 | -44.9743 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 568c01bc-47d5-37ba-bcfa-5ea2ee627353 | -5.5895 | -42.27897 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90e8bb12-ee27-3c94-b2ff-7474b5423fbb | -6.58367 | -44.57118 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b2ed6c5f-7943-34cb-8e07-590ce1f78e22 | -9.6544 | -43.84314 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcace492-8f97-3a4b-8d2d-95dbe4401861 | -6.09159 | -42.2205 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f02807d3-a9b7-3343-ba7b-f1f6f9045cbe | -8.32489 | -45.00013 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ca0ad9-4f57-332d-8395-760797cb81f8 | -8.87526 | -47.47717 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 629e7f96-44a6-3ed5-ae44-c9ea81fb8020 | -6.5781 | -44.56295 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2807c9b-51c4-330f-978b-cdfaba1a1462 | -7.89681 | -45.56084 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f01cf95c-caed-3b47-a7a2-22e5c77ed05c | -6.05341 | -44.70042 | 2025-08-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45c9fee-1291-3025-ad56-3e848009c554 | -5.21339 | -46.07565 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| faf41491-45e7-3437-9b90-0aeb673fccda | -7.39688 | -39.67795 | 2025-08-09 04:14:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bcbe09bf-20f4-3591-bf73-5dd3a7aa3ffa | -6.10039 | -42.18571 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4285f45c-c759-33bc-b4ed-6190bf760c00 | -4.75721 | -38.48083 | 2025-08-09 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2824ef0d-4d4f-34f6-88d0-b765c97dbe88 | -6.48555 | -44.41757 | 2025-08-09 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fc15e45-6b48-3545-9701-5b405bdda861 | -4.1726 | -48.57568 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a094ae-ec28-3209-80b9-641299d8049a | -6.58089 | -44.56706 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fc263312-a3c3-386b-8b1b-d5d8256c4278 | -6.60376 | -43.3859 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 55488dc9-5c2c-32d8-b7f1-92c6938800b2 | -8.86725 | -47.27413 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca8dded1-c3fc-3230-8726-f428f535ef79 | -6.25368 | -44.83226 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b27e9408-d960-3443-9f57-f3e814df4292 | -9.51943 | -45.42898 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1cc709c-0465-3cf3-ad86-89997b727880 | -4.87145 | -47.75834 | 2025-08-09 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3a2440-71fc-39f8-89c6-73c99fddf99b | -4.21298 | -48.16113 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6726efd5-26a2-3146-a78d-4e5e4a09e648 | -6.58032 | -44.57063 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2c960859-60b7-3f62-a986-e65d3d7175ab | -6.23456 | -44.97489 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4c189a2-1852-3728-ad0e-fc5c7ea0c652 | -4.47829 | -48.11724 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81869894-eb82-320a-8e5b-77493f20d526 | -6.94613 | -46.06405 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcf71fca-5001-348a-90ee-44f9fa040f7a | -7.10892 | -44.41193 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20dd467e-b774-3f5a-8f9c-a6ed070d7506 | -5.59004 | -42.27547 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec84d34c-0d4b-37ca-9636-6efa072fd710 | -9.51955 | -45.40664 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efde401a-6158-35b4-8035-43ffdb3aafce | -8.77228 | -46.41893 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbf87832-93a3-3a20-a975-fca680ff6e3c | -8.33102 | -45.00482 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0a86fe29-f72e-3ff2-965f-f39639295979 | -4.4748 | -48.11293 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ed1cd50-2f91-3a6a-96fc-eebfefe07b4c | -6.15926 | -44.0083 | 2025-08-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33a37721-ca47-3b97-9da2-41707afe66ce | -3.82012 | -41.56673 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2aab0888-2a3b-3385-8da7-da9b7eaafcc4 | -7.10955 | -46.10919 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9cc3503-b301-3488-bd25-df98fb3bd97a | -4.02802 | -48.06008 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a5a25dc-07a4-3e3d-8b1d-b96633a97426 | -7.32637 | -44.69327 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d938d4c6-80ab-3839-b2a9-0bda7958f088 | -5.97704 | -44.14849 | 2025-08-09 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a80525a7-9da3-3526-9dd8-d3ef7b9ddf2e | -4.6922 | -37.39087 | 2025-08-09 04:14:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9cd8019-171c-33c4-a684-dfe51c52c09d | -6.55634 | -43.19095 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c62e7ced-1e2e-36c2-8a05-f334da75a64f | -4.62503 | -47.41805 | 2025-08-09 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 427cd8e1-b762-36a6-b38e-ab2b787897b5 | -3.05737 | -41.22104 | 2025-08-09 04:14:00 | NOAA-21 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0fe9ae05-81e8-37ab-8471-9a4fdff906c8 | -8.06177 | -42.04628 | 2025-08-09 04:14:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fb684cf0-6a12-393b-93ee-c7ad42e6252f | -8.32375 | -45.00724 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a79e5f22-5780-3287-aae8-391b8b1a3470 | -6.62498 | -47.29327 | 2025-08-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82744416-cfdf-3374-ae50-bb6a5ef4b517 | -9.65164 | -43.83914 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7f9e45d-7ae8-34b2-bb94-f1de6830793c | -6.5764 | -44.57365 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 666fc25d-41c8-3291-aa39-53f8f0639406 | -8.33159 | -45.00126 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f844294f-d943-3656-91bd-6364ac192536 | -5.42038 | -41.22873 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5ddb6a5-52fe-3af6-a771-7304e9cf7a97 | -6.05284 | -44.70403 | 2025-08-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa75193d-db4c-3fec-9687-54cfa554045c | -3.89118 | -42.22416 | 2025-08-09 04:14:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e0eebc6-9d26-3f1c-a3c6-10e657c22ba8 | -3.84402 | -47.75315 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README13.md)
