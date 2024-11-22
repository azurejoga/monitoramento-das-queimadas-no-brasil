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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08794762-d4cd-3dfc-bf39-f38636021299 | -3.4592 | -45.9104 | 2024-11-22 00:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 4b2a6fb7-27e2-30ec-8b09-6dbb697a397d | -3.9494 | -47.9776 | 2024-11-22 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a357afe6-c270-39a7-96db-17b37b44639a | -3.7554 | -46.1204 | 2024-11-22 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| aa321c6b-3ee7-3e7d-8cca-5b9ca4e8eb57 | -3.516 | -53.793 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| eaa2cc92-dba2-3205-8131-cc4a3d03b70e | -14.558 | -54.7205 | 2024-11-22 00:00:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 61d517f3-cb47-30b5-a716-b4e03b3a6ecf | -1.1287 | -53.3951 | 2024-11-22 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| a74edf1a-69bc-38c3-9d77-a058299a9586 | -3.2768 | -53.8199 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7208a5df-31f3-32c6-997b-9799ed5ef0d5 | -2.5012 | -49.0162 | 2024-11-22 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a3efbe53-15bd-30cc-83ba-738423d34dff | -2.5013 | -48.9949 | 2024-11-22 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cbc24b3f-f717-358f-bb01-f48b7a93199d | -2.5198 | -48.9944 | 2024-11-22 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 218561d7-a986-3617-9741-e669c2103650 | -3.3451 | -50.5126 | 2024-11-22 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 731e3985-1cff-35ea-b59a-cd21c5811be4 | -14.5577 | -54.7412 | 2024-11-22 00:00:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1a113ecb-d5dc-3a01-b319-d0cdf600b683 | -1.1103 | -53.3953 | 2024-11-22 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 35c4fc3b-20fa-3f10-ab12-47b3d3671fae | -3.3452 | -50.4917 | 2024-11-22 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| fef0d268-f9d1-3e83-bd4b-e295e7421f3e | -3.6272 | -45.7692 | 2024-11-22 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 2b9aad08-ef1b-37a9-b095-07cd66b1916d | -3.5159 | -53.8132 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| b4426df6-86f0-3572-aeb5-3dc6f3d67831 | -4.401 | -44.1215 | 2024-11-22 00:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4ec999de-758b-3d03-b19c-2879b6d9d83d | -3.4976 | -53.7935 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c4ca17db-57e3-315d-8cce-bbfecbdc24a5 | -3.4591 | -45.9327 | 2024-11-22 00:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| a9e81be7-e1f1-3dd1-aad8-0c7ad1739736 | -1.22 | -53.6969 | 2024-11-22 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| c5179b56-bcac-3601-be0c-75037f066f0a | -2.9776 | -45.6161 | 2024-11-22 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 09cd0c67-29bd-3a37-8f87-d7408817d9bc | -3.3338 | -53.3334 | 2024-11-22 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f28c96ac-fe05-333b-9044-529907075de5 | -2.7006 | -45.2214 | 2024-11-22 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f660cfd5-aeeb-35cb-b6e4-34f579e259db | -3.3126 | -45.4912 | 2024-11-22 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 0cb8cb77-788f-39e0-a714-0c30ececc675 | -4.2424 | -48.6334 | 2024-11-22 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 43b29004-0f72-3048-a087-9d712c4548a0 | -3.1831 | -54.3247 | 2024-11-22 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 6b16caaa-ed6b-3dbf-9628-e6f7dbae96ed | -3.2055 | -48.5885 | 2024-11-22 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7f7765d4-ddd9-3452-8565-b3dec1ef0f9f | -9.9472 | -36.4186 | 2024-11-22 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 184.1 |
| 0a17a5cf-1240-38b5-a6a2-4e381ba67cbd | -3.8535 | -52.3596 | 2024-11-22 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5e4dafaf-35db-377a-9ccc-9b23857ce298 | -4.2238 | -48.6342 | 2024-11-22 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a610478d-0981-36c6-b53d-749479693d60 | -3.6273 | -45.7468 | 2024-11-22 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 115059eb-007f-3357-a1ca-330e96780b88 | -3.2014 | -54.3243 | 2024-11-22 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 47d04ddb-e081-3b71-9f17-13283264403f | -1.2201 | -53.6767 | 2024-11-22 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| bbbdebc5-9299-3aa1-9228-2d37e240013d | -3.4777 | -45.9319 | 2024-11-22 00:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d3fdc403-40a4-3c24-8977-3adf011b7240 | -3.1107 | -53.9853 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 65bc8bb3-76b2-3549-8a94-6f789aa385dc | -3.4975 | -53.8137 | 2024-11-22 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 12e03b82-95b6-32b4-a466-3943716dbc90 | -3.4778 | -45.9096 | 2024-11-22 00:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 1e4c0a88-05f7-34b9-a1d2-24cd5df91951 | -2.504 | -54.1598 | 2024-11-22 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b2dd4e98-063d-324b-9482-a0a37e660f08 | -2.5223 | -54.1594 | 2024-11-22 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b83adcd4-52c2-337e-a855-cfd5a1c35b6b | -6.2672 | -44.5442 | 2024-11-22 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 256431cb-b7a8-33c6-b28a-c7245c03aef2 | -2.7005 | -45.2439 | 2024-11-22 00:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 38de86ea-41d0-39a0-b803-2b90b9bf528d | -1.1287 | -53.4153 | 2024-11-22 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ee8032e3-a88b-3176-ae7d-f1f723a2e5ee | -3.8355 | -52.2576 | 2024-11-22 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| c193cef0-fc28-3cd2-a5ae-b971d103bab3 | -14.5387 | -54.7227 | 2024-11-22 00:00:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bb769137-a2fa-3e52-b704-a3087b4f018f | -1.7892 | -53.6293 | 2024-11-22 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5382cd0a-07b8-3c79-a1fe-51d38b103ccf | -6.2859 | -44.5427 | 2024-11-22 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 69cbebaa-abd3-34cb-810e-2ca635689c81 | -3.23 | -54.19 | 2024-11-22 00:00:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2dcd9ad-fe7f-3dee-9cc3-eeef1d74689f | -3.2 | -54.19 | 2024-11-22 00:00:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d252c40-b6f1-3d2d-9958-44ad682e949a | -3.23 | -54.25 | 2024-11-22 00:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7648375e-f42e-3599-92de-685b50834c0c | -3.2 | -54.25 | 2024-11-22 00:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6cf80a-5a6b-3452-9359-e3ae0ae8ea14 | -2.5198 | -48.9944 | 2024-11-22 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 88bf35ff-6892-371f-be33-4547acc873d3 | -3.4592 | -45.9104 | 2024-11-22 00:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 151.9 |
| b99e68b7-e120-3c8e-b6fd-0bbb1799feed | -3.5159 | -53.8132 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| c9fbad2e-0b6f-390f-9493-a3547c948c2d | -3.1831 | -54.3247 | 2024-11-22 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f4e9877b-e277-3225-808c-7e4df07f70ec | -3.3451 | -50.5126 | 2024-11-22 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| d582e2e5-908f-34ff-a471-5a7bbf4f77dd | -1.1287 | -53.4153 | 2024-11-22 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 9a1547cf-27b8-38a1-a717-130172f8e231 | -6.2672 | -44.5442 | 2024-11-22 00:10:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6e42852a-7514-3d2c-b738-ef78ba367b42 | -2.2846 | -47.4049 | 2024-11-22 00:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 554a1907-e570-3247-817c-e888daf87a26 | -3.6272 | -45.7692 | 2024-11-22 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f5e84039-c837-3a2b-82b2-d818d22c4de3 | -8.7043 | -66.7124 | 2024-11-22 00:10:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6322d3e1-a8a9-378b-9afa-f51920cc6828 | -3.4976 | -53.7935 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7b3a7918-ac0d-3557-99c3-e7a3708e72fd | -3.8355 | -52.2576 | 2024-11-22 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 434f33dd-58b0-36df-a23d-7b538d61c8ee | -2.2846 | -47.3831 | 2024-11-22 00:10:00 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5cfafe63-0afc-37d0-9624-1cfbfcc625a5 | -3.2768 | -53.8199 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b3a69622-4d4d-3a7f-9630-a75808208c5e | -2.504 | -54.1397 | 2024-11-22 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3f202850-bd87-3b2a-957f-96c5b13a9d08 | -9.3005 | -43.1185 | 2024-11-22 00:10:00 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| d29f14e8-7561-302c-ada7-5613adb825bf | -1.7892 | -53.6293 | 2024-11-22 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f5dc8c80-d60d-31eb-baa6-e844a103951b | -3.1107 | -53.9853 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ca98d455-c957-3a5d-bd08-b13f9f1b168e | -3.2014 | -54.3243 | 2024-11-22 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9886b974-9e21-3578-aa16-6e63156fc5da | -3.3452 | -50.4917 | 2024-11-22 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 0d0cab18-9db5-3fc4-ad7c-77f052d761ac | -3.4975 | -53.8137 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 40553a0e-4998-3cfc-968c-3f63bea09d81 | -3.1831 | -54.3047 | 2024-11-22 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b02d105d-a3fb-396b-ac16-904ceb5e0833 | -3.7554 | -46.1204 | 2024-11-22 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 7e6ba330-6334-3aaa-9da4-e9e1490980a7 | -2.5012 | -49.0162 | 2024-11-22 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ecd1c917-dd38-34c7-bc53-a6e11c5958a2 | -4.401 | -44.1215 | 2024-11-22 00:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b54ecc2b-eb97-32e2-9866-921d7ddaa63e | -3.8535 | -52.3596 | 2024-11-22 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 4a79f838-64bd-39a7-aa5b-5b1fcc331a6c | -2.6947 | -51.8597 | 2024-11-22 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3f4915f1-8007-3447-b586-38b4cebe2ff6 | -9.3678 | -35.489 | 2024-11-22 00:10:00 | GOES-16 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| b218f011-222c-304e-995c-e0f6d8c6ac9f | -0.046 | -51.2325 | 2024-11-22 00:10:00 | GOES-16 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 45e28dd9-bf74-3c5b-92e4-75523bd27bf2 | -2.5013 | -48.9949 | 2024-11-22 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4011ee10-0ed9-3359-91a9-a2ea7b7832b3 | -3.4778 | -45.9096 | 2024-11-22 00:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 7641f63c-f1c8-3c96-8665-9a799fba11fe | -1.1103 | -53.3953 | 2024-11-22 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 7ddfbd13-6a65-37e0-a8db-a536dc32a7da | -1.2017 | -53.6769 | 2024-11-22 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| b65f89ee-c4cc-327c-80e3-d798008e56f7 | -3.187 | -48.5892 | 2024-11-22 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 89c1913a-9ce4-3dd2-b936-f1092f1e79c6 | -4.2424 | -48.6334 | 2024-11-22 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 9833974c-a257-36be-95ab-f7cebbe85aca | -2.6965 | -46.2275 | 2024-11-22 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f7706212-5e9f-3610-a587-88eb5cfa7c16 | -1.2017 | -53.6971 | 2024-11-22 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 67379438-6444-3202-90ab-352d4bf3b4b7 | -2.504 | -54.1598 | 2024-11-22 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cf7aac17-f18f-36cf-8c5b-fb6f105fc653 | -2.7131 | -51.8592 | 2024-11-22 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b8b6e650-0a75-346c-bc2a-fe211993ae4d | -3.774 | -46.1196 | 2024-11-22 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 79bc84bf-da08-3a23-9c81-1e0229cc17a2 | -3.516 | -53.793 | 2024-11-22 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| f8044cfc-cf42-357e-b115-e21abca7caa1 | -1.1287 | -53.3951 | 2024-11-22 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 8e98d718-f6b3-3576-af1a-8787af78e661 | -2.5223 | -54.1594 | 2024-11-22 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d901f4ad-debc-34b4-89c6-0aebd9867e08 | -1.2017 | -53.6769 | 2024-11-22 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 04fbb767-69fc-3f96-bcac-75942c71795a | -1.7892 | -53.6293 | 2024-11-22 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b0a3f99b-fcfe-33aa-8cdc-173a51246d7d | -1.2201 | -53.6767 | 2024-11-22 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e1d4d29f-1c0a-37af-a7dc-fac278e39778 | -3.2768 | -53.8199 | 2024-11-22 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 05242535-d6f1-3c29-a105-6a211b40c429 | -3.7554 | -46.1204 | 2024-11-22 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 03e2666c-45d9-3aca-a74c-047f8a74b7d2 | -3.4975 | -53.8137 | 2024-11-22 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| b3f0bbc4-0550-3d50-99f4-eb018228a18b | -1.1103 | -53.3953 | 2024-11-22 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |


[Clique aqui para ver as próximas entradas](README2.md)
