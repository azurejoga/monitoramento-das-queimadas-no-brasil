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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e16c257-7dce-325b-bd2d-3a22747abca2 | -3.25882 | -54.52884 | 2026-09-15 12:04:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 645ad81d-c686-3aad-93ff-c988e37707f6 | -3.53941 | -53.99392 | 2026-09-15 12:04:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 57c30586-d084-3de9-9016-d7c4db0e0636 | -2.66126 | -57.54977 | 2026-09-15 12:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 368adb38-f102-3dbf-b062-7f19dd3e1789 | -2.82735 | -49.22574 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0fcf05a3-9562-3351-9153-b38b4a0b5ab9 | -1.68699 | -47.60509 | 2026-09-15 12:04:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| c43b486f-49c2-343a-87e8-82d738135fd0 | -2.82585 | -49.23627 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fd3bec0b-0db4-31f6-878c-6e97deb35a40 | -3.07915 | -50.56865 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8dc485e9-8089-3b40-8fb9-01ee70580579 | -1.8115 | -48.82321 | 2026-09-15 12:04:00 | TERRA_M-T | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c1577f77-5501-30d5-8721-cea973606d01 | -3.49401 | -50.37449 | 2026-09-15 12:04:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 94249584-ac09-3eb7-a1dd-ab7b7a709860 | -3.33714 | -54.18525 | 2026-09-15 12:04:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6579964c-0d48-3a55-bce4-fec63d99c7f6 | -3.5408 | -53.98418 | 2026-09-15 12:04:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 07f79756-e149-3e67-9d50-8b2b9802dc15 | -2.66376 | -57.53234 | 2026-09-15 12:04:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d5ff01a8-f8db-3775-b8a7-c096e0b9498b | 2.69056 | -51.04369 | 2026-09-15 12:04:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bfc97871-626b-30cc-94e7-3f1a97f4eda5 | -3.46773 | -49.84212 | 2026-09-15 12:04:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fef903d4-bd8c-30db-b7cd-280bcf93f011 | -3.84893 | -51.76842 | 2026-09-15 12:04:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 45223d17-f3fe-3539-9f5b-4bbd78d9ed8e | -2.78546 | -49.45279 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 320ab546-cf6d-35be-bd40-34b277a4e7ec | -3.85151 | -51.87622 | 2026-09-15 12:04:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc62f9e7-50f4-3876-9fb0-6fb8d0624fa3 | -3.54868 | -53.99523 | 2026-09-15 12:04:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a62847d7-a889-3174-b086-aa3225f3429c | -3.48612 | -54.6656 | 2026-09-15 12:04:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 024c964e-980c-3efb-80af-2ab721aff9cf | -1.7602 | -48.74407 | 2026-09-15 12:04:00 | TERRA_M-T | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a6b51f2d-eb8b-38f2-bac6-a4ee33ac7a3d | -3.48457 | -54.67619 | 2026-09-15 12:04:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d1ad7b06-fa6f-3b28-a871-84df9c6cb86b | -1.2284 | -54.13698 | 2026-09-15 12:04:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fdb299c8-3298-3626-b333-2ff2ecfc6483 | -3.08138 | -51.20184 | 2026-09-15 12:04:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2579ceef-de71-39ce-bb5f-a254d1557bd9 | -2.77597 | -49.45152 | 2026-09-15 12:04:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f708ed57-2796-34f2-af98-b7d99b53bea1 | -2.82155 | -51.33671 | 2026-09-15 12:04:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7b00b48e-695a-32ec-bba9-38f342739373 | -9.77316 | -46.11961 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 27a22b7b-f76b-3ce1-beb8-aaeb2008acdb | -4.51805 | -54.97344 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 256c4a32-911c-3cb5-bdca-1864d802c03d | -5.71109 | -51.85019 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a1c58ba9-e758-38f7-b071-dbca0873a423 | -11.50244 | -45.7742 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 09f8d159-a910-3137-9f1d-965050268203 | -9.35596 | -50.0892 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c7dde14d-2a1c-3dcd-9155-e54f66ef9585 | -5.71234 | -51.84129 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 117d5073-1e91-317a-ad80-34701e1d2785 | -7.01519 | -44.6278 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 210.5 |
| bd371e95-5026-324d-98b7-3ac3bb92738b | -7.01233 | -44.66159 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 04c6a41a-0ae8-305a-a651-890e1ad56bf3 | -10.88204 | -46.28942 | 2026-09-15 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| f4df904c-f6f2-3359-b8e6-7c9bb8d2082c | -7.01175 | -44.65487 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| bec94cb8-031e-3b41-af88-084dc506fb50 | -6.7556 | -45.00692 | 2026-09-15 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| db935c32-d20b-3037-a778-7daea510d986 | -6.83338 | -43.51885 | 2026-09-15 12:06:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 08ca8701-5667-3add-a118-3140d485fb30 | -10.98832 | -48.32982 | 2026-09-15 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a80eae8d-59bb-3699-8682-01a7c2e52fb7 | -11.49104 | -45.74627 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 62c7424f-3904-3d13-9b49-66177c6750f7 | -8.48947 | -44.59555 | 2026-09-15 12:06:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d1daf8ea-adfa-36b2-b637-9e025f96ebc2 | -10.42225 | -48.6468 | 2026-09-15 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e833e7eb-26fd-3512-955a-ba66e9f2f943 | -8.50967 | -50.14902 | 2026-09-15 12:06:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cad13dec-d9cd-388f-bd74-f1ef290510d0 | -5.13204 | -55.93606 | 2026-09-15 12:06:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b6b3fda4-dd80-3d09-ae33-5fcea777698e | -7.01558 | -44.63442 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 209.5 |
| cb62af34-5d69-3676-b6b5-4a9b8b237625 | -10.70886 | -47.49419 | 2026-09-15 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a7b464a7-678c-3f09-a1f1-4f84c42c5399 | -9.4808 | -45.45292 | 2026-09-15 12:06:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 43c68640-2214-328d-9e63-d42b430652aa | -10.304 | -54.16775 | 2026-09-15 12:06:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d658f2ff-9d8b-39fe-83c1-785d262af2c4 | -9.76235 | -46.09515 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 983186c6-0045-3f20-b734-dccfd5a00cb0 | -8.2132 | -54.83865 | 2026-09-15 12:06:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5a9ee0a9-61cb-31ee-b620-3b8ec6956f47 | -6.67992 | -50.91597 | 2026-09-15 12:06:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 24f39c1f-ace3-3cd4-9836-64087d4491b4 | -10.57941 | -47.73612 | 2026-09-15 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c6ed3a20-8139-35cd-be4d-15b9e8ccc29b | -8.49136 | -44.589 | 2026-09-15 12:06:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| fcc70667-0818-3e55-83ab-0fae9c189fb2 | -9.76926 | -46.10318 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| ea45bb2b-a139-3ca6-8f4a-9a525f1d87a8 | -10.87947 | -46.31128 | 2026-09-15 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 680d0fd0-ebf1-36b1-aa71-e5c8c2a21a4e | -8.83856 | -45.85238 | 2026-09-15 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| fd21b747-629e-3291-93a3-aff1ab0f292f | -10.53114 | -46.2916 | 2026-09-15 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9f4db5ef-37df-39d2-806b-f7d6191227ae | -9.22658 | -46.185 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 188df5af-991d-3e0f-b3f6-8e3af029fa8f | -12.31149 | -47.97373 | 2026-09-15 12:06:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 080750c5-3773-3e0a-bdde-1485a07052fc | -9.77594 | -46.09738 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e6cabb81-2656-3174-93c0-725e2280600e | -11.88407 | -43.83097 | 2026-09-15 12:06:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 97efc78a-e474-335e-a30a-3c04d9b48806 | -6.15695 | -52.79484 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 756339f9-bc72-392f-9755-9ebf32d18ddd | -10.99022 | -48.31443 | 2026-09-15 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 95d17476-27bb-34fd-b583-42d9bfda3b55 | -8.81247 | -46.90476 | 2026-09-15 12:06:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f5b1fbdc-0a69-3f1e-af88-09e450a90fb0 | -9.35776 | -50.08382 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c8fdb0b3-179a-3b03-9610-6edf5bad3bb1 | -11.51378 | -45.80209 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 11d6d4b4-f068-31e2-bc73-7bdb2da85248 | -4.51965 | -54.96275 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3ce43a67-a4e8-3a72-abdb-4d992963d46a | -9.35478 | -50.1066 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 527d7534-d883-3551-bc51-ba91a566cfd4 | -12.31364 | -47.95573 | 2026-09-15 12:06:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9f6b3db0-5b3c-3466-b218-de0c97967194 | -9.34547 | -50.25417 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 867bc317-d9ea-38a5-8d4e-144c67854b21 | -9.35285 | -50.11192 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| ac20dc02-1a7c-3669-b9cc-68c2d911bb3d | -4.3912 | -55.20486 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 678dd9a5-4e9a-3acb-a892-61cf8e5b5f69 | -11.82225 | -46.58166 | 2026-09-15 12:06:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8e2a8fac-5268-3299-a707-fb1b5122c400 | -7.87304 | -54.70487 | 2026-09-15 12:06:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bde73d98-68bd-3db4-98b4-eab08f98a2e2 | -12.32588 | -47.95717 | 2026-09-15 12:06:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 84cacbd6-68bb-3f85-a4af-529e2a360069 | -11.17416 | -46.36517 | 2026-09-15 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5ab2ae2c-f066-3822-9df5-4dd2da551998 | -7.15401 | -44.24864 | 2026-09-15 12:06:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3cc0be63-7140-38c6-8feb-4bd181433348 | -8.83577 | -45.87517 | 2026-09-15 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6053aee9-0758-3093-92fc-80730eaaadd8 | -6.38101 | -51.6755 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c4123a8c-54b0-3032-be58-21232cef6f9a | -7.15779 | -44.21859 | 2026-09-15 12:06:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 2cd70cb5-cb28-31f4-8cd1-d28f87970425 | -10.80137 | -46.2013 | 2026-09-15 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| deb0566e-b6d7-3099-9975-e4fb1becf2cc | -9.76667 | -46.12535 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 734aa154-9837-39dc-8fb2-78e6fc6f0aba | -10.5869 | -47.73101 | 2026-09-15 12:06:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ea7ae0a4-a652-3325-ae1a-993e4f973d59 | -10.0364 | -52.09163 | 2026-09-15 12:06:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f49b9b5-b684-3983-be0e-48db6bcc646b | -4.39021 | -55.19864 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0e2ca121-ad45-3075-bc29-8ec3297560b5 | -6.02415 | -51.7846 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f8b81fb-ac45-33b1-8bc3-6020d32e59e9 | -7.5707 | -44.92764 | 2026-09-15 12:06:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 83b162d5-aadf-3565-9f13-092422140b0c | -7.56889 | -44.92056 | 2026-09-15 12:06:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 350d9d06-c0e5-3bdf-8cf3-3b1729fdbae9 | -9.35627 | -50.09522 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 19635783-7869-35be-85f3-d42f3684605d | -8.64451 | -44.44402 | 2026-09-15 12:06:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ab9424ee-efc6-3c66-801d-30aaaae61927 | -7.16697 | -44.25602 | 2026-09-15 12:06:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 87c7fcdd-c825-3ea4-9d04-c534bad93f32 | -11.51665 | -45.80796 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ee665f69-f2f7-3800-8a61-d149b497a8cf | -10.86578 | -46.30977 | 2026-09-15 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 429.6 |
| cd539e56-42ed-3b41-9008-08b831cd8ce7 | -8.81021 | -46.92267 | 2026-09-15 12:06:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8c68a55f-b25f-32b7-8594-524f01e7823a | -7.01866 | -44.60046 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 950967d8-bb33-34ca-854a-75f07c1adb68 | -10.86835 | -46.28781 | 2026-09-15 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 2f4919f7-1e15-3dbf-8d6f-3f8f9d3c0274 | -6.75244 | -45.03198 | 2026-09-15 12:06:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6fdbc0a5-0d0a-3373-a55f-cf6c78cff46f | -5.13026 | -55.94792 | 2026-09-15 12:06:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e6e1d7ad-182e-3fa5-8cd4-4efa7fa6c91a | -4.52931 | -54.96414 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f4a046c2-6439-3c7f-96bb-c179ea3c059c | -8.49282 | -44.56677 | 2026-09-15 12:06:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f791949f-d452-30a8-aa31-20551536fc8e | -10.78486 | -46.22306 | 2026-09-15 12:06:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |


[Clique aqui para ver as próximas entradas](README73.md)
