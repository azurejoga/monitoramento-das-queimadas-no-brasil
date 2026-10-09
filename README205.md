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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a38cbed7-b846-3703-8e76-f150e070fe28 | -8.84186 | -61.45628 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0305c99a-8430-37d4-8939-0a840560c0e6 | -1.28675 | -55.4204 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f226767c-83b7-3aac-ab37-0e3002b84561 | -3.34504 | -50.47933 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd62879d-f769-3dfd-94cd-ff76d9faa653 | -2.78259 | -56.50814 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5af5c7c5-4cd4-3c13-9a55-f46a1ef8d366 | -3.07081 | -53.96733 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22f65897-dcf8-39d3-a59e-0ffd8c81a65d | -3.74972 | -59.41952 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b65bb02-156d-30fb-ae40-b297dfb34c9a | -3.1639 | -61.08596 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e4edae0-d920-34a0-88ea-bafe6cf2fba2 | -2.57487 | -57.78722 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e45ea7d-7fea-32e5-95ad-083ca5ca10ba | -3.02089 | -54.08752 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e430c48-6af6-3685-a84c-07b8f09f58db | -1.54706 | -54.5634 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 414e62ff-8252-3a40-938c-04f05d59e5f1 | -3.03145 | -54.14732 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2fa417f-35e6-3b14-ab57-7b50baf6d8da | -3.64157 | -59.30947 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 806d4251-73cc-3c5f-9885-8a8c9519295c | -3.32401 | -50.18158 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8a80df4-a7cc-3537-96fc-821b363a2c65 | -3.49287 | -59.60188 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 235f11e5-08da-3d3e-a3f4-b9a6e5a5ae3a | -3.76968 | -59.50882 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe8ea7ea-ac7f-383b-bd4b-7b862d4f46f8 | -3.02348 | -59.15801 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b18829-c845-36a6-8747-319c79020af3 | -2.84366 | -54.13778 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 164b36b6-75aa-3a6b-bf78-6f31ec357a87 | -3.0947 | -53.94113 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 457dff80-eff5-3559-8628-ab874bc6f204 | -3.69912 | -60.54762 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba04f47a-12d1-35b1-9c0c-e85a22d99cc4 | -3.19042 | -50.58829 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00f08881-899b-3209-9452-7288c1dcc3cc | -3.74137 | -59.45047 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f95baf45-f3d4-302b-89d5-0b9542a864c4 | -3.62992 | -59.31836 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41420545-e102-3168-96b5-57edeacbacd2 | -3.78062 | -58.58425 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0078b40b-c22f-3abb-a68a-f272ea0702fd | -3.21875 | -53.89161 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b21e1ee-f522-35e5-8637-8e73dd870fdc | -3.02596 | -54.05404 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f96f052-06a4-3fd0-b74e-7e6126d4a82f | -3.01164 | -54.08388 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e8ef591-f1ff-3a47-8ca4-17e878e34a28 | -3.03217 | -54.14262 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93d4a2cb-8c8d-3964-b0fa-1c9675163fc2 | -2.50535 | -56.1285 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29b0bdb8-5123-34fa-ad1d-9e25aca28cc5 | -2.98662 | -54.14304 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9f36a5d-1b15-38f6-bf68-2a4cf656fdc8 | -3.43232 | -56.94209 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06671632-5fe5-3c7c-80b2-4656ad29df74 | -3.59007 | -54.56714 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f89bd5e-726d-3943-bbe0-dd259e757eec | -3.71061 | -60.54181 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc959518-efb4-37a6-b0bf-6081c743c432 | -2.47092 | -58.07801 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd8002f2-f416-34e2-b542-7a2b99a53336 | -1.60645 | -55.16224 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbe82674-3c8a-3527-8eb4-2056e0d3c127 | -2.81848 | -59.25116 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfe22b9c-96b2-35ba-a5b5-e00e644ef56b | -3.03757 | -54.23499 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c09ed0b3-f01a-369b-a294-2988ce830b17 | -3.0063 | -54.09277 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbcba3a0-a281-38e6-958e-ae9b2ba7d8ef | -3.19945 | -50.56192 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f83ba240-18ad-3605-a27b-73eab58e327f | -6.49281 | -62.85219 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abd7b125-95a3-3214-99d1-e0b7e33af1b5 | -4.8085 | -54.67278 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e032ceeb-4f1c-31ee-b052-fc49e0ae4bc1 | -3.6664 | -55.54452 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1491b3b3-9265-3926-b557-65883d1a12f4 | -2.94539 | -54.15608 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e179749e-174e-3c20-85e9-3913c21f9868 | -2.99936 | -54.08685 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e564cc1-ba26-3eb3-9e38-c79be9cd62c7 | -3.52323 | -59.34764 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 892785f2-616b-37ed-95a3-0ad0a2dc2478 | -8.25424 | -54.72553 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d40396f-d9cf-3078-ac93-edf75691adb5 | -3.22527 | -57.94969 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0f80839-7078-338a-9459-08c0e1d57599 | -7.9032 | -54.72313 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b0e1294-9f20-3e0a-9b49-90fc00df3975 | -3.54472 | -54.68502 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0dee0c-7eb2-3707-b85b-0c4552ca88c8 | -3.90277 | -58.94973 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b8b3bef-6f76-3c1f-92f0-287a74585bdd | -3.4695 | -59.5765 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ba506c-6821-3e12-9c49-551d53a98d29 | -2.5238 | -56.61818 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 85aa3c75-df5e-3109-9022-f72fae29d66c | -3.7122 | -60.16108 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 278488d8-1873-3c91-9e93-e88675e1ca9a | -4.53657 | -54.98619 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ef75381-c9d7-3740-bf8e-9562698e4665 | -6.48539 | -62.85095 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f49c6fad-e493-306a-aca5-c38fd1c29a38 | -3.26599 | -54.05547 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8581dbc8-308c-3065-9ee3-f57c394befc5 | -3.12979 | -58.76682 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8ec5cbd-2ff6-37d1-98ee-731da4c8a478 | -3.01197 | -54.04213 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c704f976-e90c-3430-a14a-fc9439d5e108 | 0.70326 | -51.4356 | 2026-10-09 05:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d36e6371-3260-3621-bc64-0abb2ba30e10 | -3.71814 | -59.36084 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc4da0d1-021b-3189-aaf6-c248bb3e7e3f | -3.47801 | -59.50207 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e82d9d6e-11f4-3fc4-b344-3220ff17a678 | -3.23627 | -58.73774 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a883c6c-c7e7-3244-8480-34d84a6a4120 | -11.11482 | -47.79115 | 2026-10-09 05:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b71e3024-2032-3226-837e-356c8da69c5a | -2.82765 | -54.14011 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53d8206d-d8b4-3fe3-b290-a133dc252982 | -2.97499 | -54.11697 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 666abb39-9109-313d-8b47-7b61391a31c3 | -3.6434 | -60.63091 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd37e284-5e87-3ea3-8d72-ca8d38c629e1 | -3.07617 | -53.95821 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06bd5cc3-e70b-3a5f-9963-d1d4d6629be9 | -9.8675 | -50.49349 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 252f74f4-56f1-3a5f-b147-5ca4c7cdb59b | -3.34546 | -50.41095 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 176c08c2-777e-3c28-a55b-093e434c6ac2 | -3.22624 | -57.87904 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a0abba0-1d8f-35e0-88c7-26d57f390bc5 | -3.02567 | -54.18514 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4fc775cb-e33f-3559-87c5-0d1e429de6a8 | -2.99173 | -54.77682 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d86a821-b4eb-3555-90f6-dd93334fbf27 | -3.83253 | -59.41143 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24c8b4ad-538d-39ca-ae44-889ba2668fd2 | -2.51048 | -56.14084 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32c1cfbe-d4dc-3c69-ac92-874bfe246c4f | -3.16928 | -54.73741 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5965d98e-1250-3cc5-b041-10f976e424a0 | -9.07566 | -61.14498 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f189d24d-30fd-308d-b303-2e947db2a768 | -4.97968 | -46.04399 | 2026-10-09 05:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82ee2d0c-b568-349c-a462-66abd2c8acb4 | -8.14239 | -64.11761 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f7dfe2c-a5ea-34e7-a2df-d3be74402bc9 | -11.3896 | -46.68039 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a34f301e-db01-3418-969f-d08adf600e45 | -3.16179 | -57.68406 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70aeca37-21af-3fee-9c71-5c9eee4f3174 | -2.52212 | -56.26878 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7838d7dc-e05d-3f7f-9884-8e11bc585fda | -3.54665 | -55.52323 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05edbaac-6117-3ac2-acd0-9c5b7edd5c92 | -8.92745 | -62.4093 | 2026-10-09 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20319583-fe7a-3ab4-a80e-5c2e38b59efe | -3.58433 | -54.68365 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fd8b39f-2999-3755-bbb8-dd1a66596269 | -9.10239 | -48.80607 | 2026-10-09 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38f9bdb1-f1fa-3b5e-8d64-5ca4d9e11cf7 | -4.32672 | -55.01576 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d805855-1a03-3127-9a48-8257d26c45ee | -2.93692 | -54.0578 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d24b20aa-b091-3230-b7d7-4146f8661d74 | -3.73703 | -57.13182 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d03e44-3c2f-33c3-8a38-518282a28a51 | -3.46533 | -60.25683 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7374ad41-cc04-3c6f-8c1c-770a83e91e0a | -2.50294 | -56.16659 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38c47285-ca4b-326d-b3b8-9600c13f276f | -1.80704 | -57.11941 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b69939c9-aace-3ef3-80ad-d3e4c7ef6d87 | -3.11723 | -54.16714 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5cef6ebb-5214-3d8a-b12d-caa0b23bffe4 | -3.57134 | -54.48926 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b759131e-61a5-3f1d-b2ae-bbad06203e4e | -3.54564 | -54.6298 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43b3ef30-4c13-3e60-8208-8cdf6f6a5e21 | -3.06892 | -59.17231 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 825f3ae7-d10a-3685-802b-de46830ed98f | -6.44809 | -59.94875 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea992bf0-f247-3ebd-9901-699e11548d31 | -3.73525 | -59.46745 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c61a1307-2c4f-3d4d-b428-8bd90223af80 | -3.09874 | -54.28924 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a3a600c-9642-3b16-bf69-d5189fcc1936 | -3.93311 | -56.02278 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea322e57-5f00-3283-a29c-96805a1b5f0b | -3.51268 | -59.34956 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5a7919-d3ac-3a3a-a411-4d2369f6ba38 | -3.58862 | -54.57634 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README206.md)
