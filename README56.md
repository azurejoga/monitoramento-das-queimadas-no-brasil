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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438a84d4-9703-3d90-846e-025092488b51 | -3.5173 | -42.0907 | 2024-11-14 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 156.8 |
| 72e0aebc-3e14-3f70-84bb-8b522923983f | -17.5872 | -57.5328 | 2024-11-14 12:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 6da5d9fe-a53a-3f16-a2af-eeb46a7f3a1e | -3.5173 | -42.0907 | 2024-11-14 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| d103f375-a35c-3db2-a2fd-05b5c67d2a90 | -17.7052 | -57.5392 | 2024-11-14 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| b2cbce36-79b7-3c5c-a536-048a80692439 | -3.5173 | -42.0907 | 2024-11-14 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| bb395069-2d5a-3033-9598-842b7467ff9f | -17.5872 | -57.5328 | 2024-11-14 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 76d73d14-e038-35c1-b9f3-ba6e8dd13034 | -17.6079 | -57.4688 | 2024-11-14 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 8fec4ccb-d62d-3584-b9a5-f99b87681c50 | -17.5872 | -57.5328 | 2024-11-14 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 524b0fc2-55c1-3f47-972d-c750a467d1ae | -17.2543 | -57.4698 | 2024-11-14 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 63002cdf-8ae1-3ef6-8aba-35045757753d | -17.6076 | -57.4893 | 2024-11-14 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 78e06f44-5aec-3dc3-8359-9fa37e11c8a0 | -3.0674 | -42.3718 | 2024-11-14 12:20:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6612864d-7abb-3840-bfe6-4e780110c6ea | -17.7052 | -57.5392 | 2024-11-14 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 11506075-33dc-378e-83df-d85d072c9e4a | -17.6079 | -57.4688 | 2024-11-14 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| b6438898-5c21-35cb-af5c-27ad6c86dd2b | -17.7052 | -57.5392 | 2024-11-14 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 688e93ba-8c30-3e36-bdf3-aa676689ebf3 | -17.5872 | -57.5328 | 2024-11-14 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| a87d3cc4-d8e0-3c2f-a5a2-2f05849fa52f | -17.6076 | -57.4893 | 2024-11-14 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 3ca82803-36a2-315c-930f-36a2dfc3b8c4 | -17.2543 | -57.4698 | 2024-11-14 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 541941e0-1ef9-351a-8981-fcdabe69630d | -17.5872 | -57.5328 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| a6e0c212-baf3-3d2c-b454-fb0d88db4646 | -17.6076 | -57.4893 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 6f2bc0fb-d2e3-346c-94ae-2a1acad0e081 | -17.5879 | -57.4917 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 0003326c-21df-3447-84ef-31412ea384c3 | -17.7052 | -57.5392 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 57670eee-106f-30f6-bee1-1916a761839e | -17.6079 | -57.4688 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 14f78089-5709-3a9a-8f4f-d04fe49ce4e5 | -17.2543 | -57.4698 | 2024-11-14 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| cb71640e-8327-383b-8f9d-e83572cc2adf | -17.5875 | -57.5122 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 10b8a0ea-bd36-3ea5-9a3b-b584a0380878 | -17.6066 | -57.551 | 2024-11-14 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 858741fa-aad7-384d-bc69-2f0f5485bbc2 | -3.7821 | -41.5999 | 2024-11-14 12:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 11810437-70dc-3c7f-b865-759fa6172353 | -17.7052 | -57.5392 | 2024-11-14 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 2900e7fe-d191-3ab2-ad0a-267b3d4c5c3c | -2.4182 | -46.2581 | 2024-11-14 12:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a98eb550-03c8-3d6f-b8e1-128fd411e50b | -17.2543 | -57.4698 | 2024-11-14 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 4fcd2250-5817-3ed8-b68f-956b34b87db6 | -4.6314 | -40.7751 | 2024-11-14 12:50:00 | GOES-16 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 3713a5e8-e154-301c-89f6-3e24b7f2a39a | -17.7055 | -57.5186 | 2024-11-14 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 71f27637-b11b-3a64-8343-6e315ca26187 | -17.7055 | -57.5186 | 2024-11-14 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 9f8d3c1a-aaff-30b4-a63b-7ffd62bcc70c | -17.2543 | -57.4698 | 2024-11-14 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 9abd51e9-cd1c-3c14-be99-03477942e589 | -3.7634 | -41.601 | 2024-11-14 13:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 1bc96ccb-6fee-33fd-9f5f-c50120fdb9be | -3.7821 | -41.5999 | 2024-11-14 13:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| f83f7b4d-1d61-36a0-b9a4-2819f0261ace | -17.7052 | -57.5392 | 2024-11-14 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| b72b553a-f5de-3ab1-bdac-c96d58c0b5da | -4.7805 | -45.8451 | 2024-11-14 13:00:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 711016fc-4451-3092-9563-d347ab389a5d | -17.2963 | -57.3008 | 2024-11-14 13:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| f2e45a8c-f864-3582-87f6-4701dbf9a4fe | -1.3784 | -47.096 | 2024-11-14 13:10:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7e53acfb-6f90-36aa-b580-76d5944ae03c | -17.274 | -57.4675 | 2024-11-14 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 5fa5ec61-65fd-37f9-8cc3-90e36db2eee7 | -4.7805 | -45.8451 | 2024-11-14 13:10:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 5a4f9cd0-f666-3a4b-a081-ace2e8301c99 | -3.7821 | -41.5999 | 2024-11-14 13:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 174.7 |
| 6c41fd30-5a56-3e35-bbfd-4237b78fcd1a | -17.2737 | -57.488 | 2024-11-14 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 9207fdba-eb88-3eec-95be-3c6c4edc564f | -3.7634 | -41.601 | 2024-11-14 13:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| bc8fd02a-8f05-33e0-985a-39fee211cd0e | -17.2543 | -57.4698 | 2024-11-14 13:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| e9171f1d-705b-3612-b5e0-621e628f8fd9 | -3.6945 | -40.6381 | 2024-11-14 13:20:00 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 90.2 |
| c9b3cc87-ca7e-3bdc-a5be-104a4df0227b | -3.7821 | -41.5999 | 2024-11-14 13:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 157.5 |
| f226cd35-7602-3bc7-abce-ad22e4ab172a | -23.9729 | -54.0478 | 2024-11-14 13:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 2eaa0d31-c997-31d8-9573-021974272544 | -17.2543 | -57.4698 | 2024-11-14 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 31a65645-034a-305a-b845-c1a906771403 | -17.2547 | -57.4493 | 2024-11-14 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| a9ffd0ef-b0b8-3c28-bac7-2ac7400edfdb | -17.274 | -57.4675 | 2024-11-14 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 63086da5-b9c7-330d-8e13-5dd1d4c6966b | -3.7634 | -41.601 | 2024-11-14 13:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 86282c01-0213-3140-8cd9-9119f3c993b3 | -17.2737 | -57.488 | 2024-11-14 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| cb772b2d-9bbb-33c9-9776-d91fd4121c7e | -3.7634 | -41.601 | 2024-11-14 13:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| f1929ce3-9798-36fa-aff6-fdce4a0e8055 | -17.2547 | -57.4493 | 2024-11-14 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 138369d2-1839-3fb0-b903-804c81c479bc | -3.7821 | -41.5999 | 2024-11-14 13:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 197.7 |
| 78ae179f-c98b-3925-9a3e-6d206968a9e3 | -4.447 | -42.8889 | 2024-11-14 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 476a3066-a475-3bd9-b5a4-9a1cb86e0481 | -3.6945 | -40.6381 | 2024-11-14 13:30:00 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 158.9 |
| d5bd7230-8053-3c52-aba0-1f26c9298487 | -4.7965 | -43.6595 | 2024-11-14 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| da1f3031-45a4-3363-95f7-a856a6e3a9a7 | -17.2543 | -57.4698 | 2024-11-14 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 3f588826-c1ad-3295-befd-9da46d890176 | -17.274 | -57.4675 | 2024-11-14 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 3167e927-efab-3cf5-ab62-32c0dd3adc3e | -17.2737 | -57.488 | 2024-11-14 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 54636f65-e98a-3a42-a898-652900c464a0 | -17.274 | -57.4675 | 2024-11-14 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 7c51c04c-c739-3dbc-8212-77e2970a9f8e | -4.4513 | -44.9403 | 2024-11-14 13:40:00 | GOES-16 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c183bc79-72c9-3a3a-9026-b0a661cf73b5 | -17.2936 | -57.4652 | 2024-11-14 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| bde4e0ab-b4e1-303d-ba0f-bccedf820b1c | -3.7634 | -41.601 | 2024-11-14 13:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| bef08e65-d8e3-3083-93c6-573483227342 | -17.2737 | -57.488 | 2024-11-14 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| c8a6f7d5-388e-3366-b416-e95d99091ad4 | -3.8884 | -42.5446 | 2024-11-14 13:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 8814a23a-ef80-3ca6-a0f8-1ab60aaefe33 | -3.7821 | -41.5999 | 2024-11-14 13:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 179.2 |
| c61f1944-1a2c-37f2-bd17-aca378cbc24b | -4.4904 | -44.6881 | 2024-11-14 13:40:00 | GOES-16 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| fee1848e-c301-3bdd-bc53-48a6e1fb80df | -17.2543 | -57.4698 | 2024-11-14 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 7c93ea58-c97e-3176-a937-164e7b48be57 | -17.2547 | -57.4493 | 2024-11-14 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 47384f17-8143-3ca1-9ebb-440594477976 | -17.274 | -57.4675 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| e53711c0-efbf-3894-8d2c-b8c5f6fc4a30 | -17.2933 | -57.4857 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 021ce1c3-ac77-32fa-adc8-6f4f06debed2 | -17.2737 | -57.488 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 7eb6d65b-df1c-3f07-89e4-c2d5dbed32f6 | -3.2537 | -42.4581 | 2024-11-14 13:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 25fc5553-e2e5-341e-8cf4-cdc6d6a1d234 | -17.2936 | -57.4652 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 7ac1d0c5-d244-3d20-8e7c-d469b3cc8858 | -3.7634 | -41.601 | 2024-11-14 13:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| b91734f1-a416-3d7f-8ba5-57a1a0e92b33 | -17.2543 | -57.4698 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 871eed5b-3b63-3037-8c2a-47fd58098e87 | -17.2547 | -57.4493 | 2024-11-14 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 88a0f4b7-0a87-317a-bbfe-21fb7014bcb4 | -3.7821 | -41.5999 | 2024-11-14 13:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 181.9 |
| 7da33cf2-95db-3dea-b557-1f7124805463 | -4.0148 | -43.2408 | 2024-11-14 14:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6af955e8-450e-302f-9a9b-9d90fd70aece | -4.4513 | -44.9403 | 2024-11-14 14:00:00 | GOES-16 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 232.0 |
| 37764dcb-3e94-3b67-80d7-8e94506f794d | -3.7634 | -41.601 | 2024-11-14 14:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 165.9 |
| 45c30078-5dc1-3fc5-964e-e015bcd70dbc | -3.2537 | -42.4581 | 2024-11-14 14:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| aa4f9b6c-12b6-3a32-9d16-e3bbfc89ded2 | -3.7821 | -41.5999 | 2024-11-14 14:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 267.2 |
| 4170dd71-b77f-3732-95e5-9f75ce29daae | -4.4515 | -44.9176 | 2024-11-14 14:00:00 | GOES-16 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 85c0684f-2e6b-38fb-83ac-8217cd28e49c | -3.7821 | -41.5999 | 2024-11-14 14:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 251.7 |
| c98ab3e0-f411-32d5-b5ad-7b25418d3604 | -17.8066 | -57.3625 | 2024-11-14 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 7cfbdc62-8a6a-37fa-a043-f20dda06a519 | -23.9729 | -54.0478 | 2024-11-14 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.8 |
| ad81ccbc-1166-3103-8c8f-1d18dcfbd645 | -3.7634 | -41.601 | 2024-11-14 14:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| dd0dad1f-f194-3b12-a6f8-b2cbd17fbc49 | -4.0148 | -43.2408 | 2024-11-14 14:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d0a2779a-ed05-3b9d-b580-31dff280fa70 | -4.4515 | -44.9176 | 2024-11-14 14:10:00 | GOES-16 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 582dd910-8812-3d31-aaaf-cc0a2615a885 | -16.9577 | -57.6473 | 2024-11-14 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 76f71ac5-85de-3e01-a6fd-8b8a233af94e | -4.0148 | -43.2408 | 2024-11-14 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ed526163-c0a7-36c9-8083-ad94cabe9b9d | -17.8066 | -57.3625 | 2024-11-14 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| c8a14051-187e-366a-8e37-4f89ce1752db | -23.9729 | -54.0478 | 2024-11-14 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| 9a28a441-39e9-38c6-8373-e76e3fab1fce | -16.9577 | -57.6473 | 2024-11-14 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 47364c12-5bf8-37bb-8e8c-a6be7f95895c | -16.9577 | -57.6473 | 2024-11-14 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 8f7daa4d-7284-3468-9e44-c849379b83ea | -18.2637 | -56.0603 | 2024-11-14 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |


[Clique aqui para ver as próximas entradas](README57.md)
