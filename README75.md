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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22c8bb9-58da-394e-b911-e51232e2cdf5 | -3.51072 | -54.65589 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be267583-5b72-348c-b7d4-cf036953d88d | -3.70685 | -57.15696 | 2026-10-07 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ba421ca-4bfe-336b-a4a5-ba9702ad603f | -4.77084 | -55.67434 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb5630af-44d2-3896-add7-50a02f56cb52 | -4.45688 | -47.91685 | 2026-10-07 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| c0f220fd-bb54-3504-9746-b9fa6c8de2b7 | -2.94021 | -54.14661 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d94f448b-b2ad-3c6f-8ff8-32b421691999 | -3.50464 | -54.6514 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1da34d-5940-39ca-8bb2-ce1413f52cdc | -3.49457 | -50.10633 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 605086da-496f-357a-ab1b-e72ff9c43b03 | -3.7362 | -55.98007 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e13ad4e-2a19-301b-bc62-3fb8ac0dc22b | -3.6006 | -50.98257 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57745996-b4fe-33d6-a1ba-60db76229a8e | -2.90336 | -54.07626 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7939d8b5-d82d-364c-ab6d-0085ee40e1e5 | -3.05205 | -57.52159 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae122b1-5d9e-37aa-aa9f-88252c02ac30 | -8.69979 | -45.22301 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0bab431-e196-3b12-a683-037d9a9fb13c | -4.13143 | -54.90837 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 247b0959-c82e-362f-aa29-0832101c721b | -3.16092 | -50.4375 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9982f8b4-1f77-3089-86d1-cd66ae08e975 | -2.98012 | -54.04095 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6ef4ca-9858-3e09-80b1-5cdd817fc043 | -2.88079 | -54.13389 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb868a77-2ee7-35fc-ace5-ce27692e72ac | -3.84982 | -55.84224 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a12facd8-4ad5-302a-b843-917cf074959f | -4.58066 | -54.93223 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ccbcaf60-332e-3798-854b-dea026917e9f | -3.04719 | -53.9391 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60969f54-2804-3298-b9b1-b1718c68e0ed | -3.27826 | -54.0075 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 155286bd-04df-3c61-a10e-b9a0786281df | -3.558 | -59.48207 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b4980ff-ca8c-3a62-929a-db2068beefef | -3.04955 | -54.23139 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d01f5ee4-1a37-3f02-99b2-97d6e6a7e95f | -2.98963 | -51.04907 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 98e8893e-cdb6-380f-8c0d-67e0b17c2c35 | -1.26135 | -54.68105 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8dd394a8-fca6-3689-a1b4-c78beb434292 | -3.08493 | -54.26548 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52c0e0c4-c597-355c-bf4e-d46d0093273a | -6.92822 | -43.66994 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e0af9964-b40a-37e1-badb-1c9fe3fb5723 | -3.07407 | -54.18139 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14c3303b-b5aa-39cd-a191-316302a20251 | -1.19808 | -54.21029 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7800c8ff-1806-36ea-8589-4db59c541e0f | -3.52565 | -54.66882 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 269fbd40-3cd0-3dd4-b077-acf4f7d05f0f | -3.38649 | -58.20824 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8771382-7356-3a40-8d59-3fe998f45e7e | -3.48392 | -59.58334 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96afc87c-c01d-3ef7-be4b-bc5a784b4034 | -3.63908 | -58.88831 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83505da4-ceee-3077-a0c4-e20b86830211 | -2.94364 | -54.19016 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7176f2a5-dedf-35b4-8831-02b112ce0bb5 | -3.61378 | -50.20113 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0c71bd5-cb04-3def-9177-a225ee7c4030 | -3.07623 | -54.16733 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1416d3ad-f560-3bbc-b540-be7eac9ef4a1 | -5.95989 | -55.36024 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce4c573f-0892-37cd-a2f7-ecfb642ba143 | -3.1749 | -54.08167 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72456b46-47e1-3d84-b678-9b67ab4e7224 | -3.27393 | -50.4337 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f56e9e30-6e72-3b92-9f00-a8513b79f46c | -1.4893 | -55.87654 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae574dc-1e92-357a-9ff7-ec7ec726f09a | -5.98579 | -55.36781 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4212ff3-0fe3-33b8-bb1e-95ef8d6aad06 | -3.27611 | -50.79243 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6438c994-b613-3580-8a5a-10f0c34df12f | -1.29428 | -54.55637 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cad95a94-623a-35c4-bbd5-87328d97b6e6 | -3.66402 | -54.2833 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8985f82e-44c8-3e63-a8c8-4d3bcf856d6f | -3.09119 | -57.64834 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 937209c6-05fe-383e-a623-fffa2b444113 | -3.28114 | -54.05505 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 459fbf8a-2f19-3699-ad9b-c5112139a998 | -3.28889 | -54.02725 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e883417b-476c-3605-84f3-de83a1d6635b | -2.93185 | -54.13456 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bbdf868-c99d-3e79-a898-850d14f23ade | -3.09955 | -54.17094 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a03410a-aac3-3459-a18c-e206d6bb6ffc | -2.87197 | -54.14685 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e809c13-514e-38e6-8515-e435a0956eb2 | -3.77609 | -58.52047 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ded8729-78b0-3780-8b72-233952682f2f | -3.26937 | -54.02064 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971ef57b-a40b-3599-8e70-87a74710e951 | -3.49674 | -49.90336 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad3f7a86-b884-3b48-a6ac-689bd57fe65e | -6.89393 | -43.68656 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af777e0b-f140-334b-b1b6-fb8d4fd73511 | -3.08206 | -54.23999 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc13d585-4d6d-35e4-b095-dfecff876035 | -6.16716 | -44.59758 | 2026-10-07 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d5252b5-a8e3-3ba9-bad9-2c1c88666844 | -3.28496 | -54.00853 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ca1dbf7-f3a7-3788-8059-7d4648f67e3a | -3.3574 | -59.49813 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84eed1f0-91ab-3fa5-ad80-87067a2b5ed7 | -4.27158 | -54.86279 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac48323-3d2a-38a2-bf68-f9dd52616f34 | -3.46957 | -50.07998 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f3a6ad94-730e-3823-9f45-e13e7d65e827 | -8.70594 | -45.2236 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2b00d2d-3d57-3a76-a4ca-7d6fcba125f7 | -2.76733 | -54.09797 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 84bec4ec-e27b-3bab-9f03-d579633de3c7 | -3.02356 | -53.86999 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58a709bc-de0d-3013-9a26-8d9967687674 | -1.32781 | -56.40626 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff6b5a67-c92f-34dc-ac06-fed4e6b833ff | -3.04434 | -53.91322 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad5be497-1e76-383c-a02f-acf06e203911 | -3.97361 | -56.05293 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6001591-7419-3dba-8ed6-d42895db263e | -3.07956 | -54.16784 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68dfdc1a-b631-31b5-a0c9-18e543f700db | -3.04769 | -53.91373 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8623ddfd-4946-30c1-a3b9-0fa026d687bf | -3.27335 | -54.06108 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9486e84-ed39-3d15-82a4-540eac04b7e8 | -2.77732 | -54.09951 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 98bb4535-7674-3041-bacf-c4ceac44ae5c | -4.84188 | -45.98643 | 2026-10-07 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6757a90-3a91-319e-84b4-0ebeadb21f19 | -1.34649 | -52.79328 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0efd11b-d53f-335c-84eb-84ccd5f0d281 | -3.03709 | -53.91574 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6fd6056-3b0b-3a13-b920-a9d0a7e49ab2 | -3.28165 | -54.02977 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ddc9795-1697-3597-adca-d676a369bec5 | -3.27996 | -54.01864 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25d47276-bd1c-34bb-899d-f0619ef3fbb7 | -6.00036 | -53.50841 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b34dfd8d-0cb4-3ab5-85db-daa25737641e | -3.52443 | -54.63319 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef7312fa-9eef-3973-aaea-39762acb1030 | -2.91792 | -54.11446 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4da62176-d8d4-3145-b1ab-188172a0bf70 | -4.16226 | -55.14944 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3e0fd63-16c5-3f1a-8a32-4e379924b59b | -3.50303 | -54.66177 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5bebc4a7-9457-3de7-b59c-c2196958c1d9 | -3.99609 | -56.25523 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a7a7a26-e733-3828-9ddc-12f3895882ad | -3.01066 | -57.73937 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dd031b3-87b0-3e47-a7a9-7a44df30fa68 | -2.92967 | -54.14858 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f07a159-8e57-33b3-a92f-36b32e5fb48a | -2.77562 | -54.08849 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a31158c1-32e2-3795-84a0-8eee12a80eb7 | -3.67439 | -55.94221 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b96f802d-ec3e-357b-8321-9bd6628b83f6 | -3.5008 | -54.65435 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad4bf30e-0666-338f-83b0-cd8b0fa5d46b | -3.14454 | -54.36433 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1871095d-f49c-3bdd-924a-e0087a26c362 | -3.48501 | -50.08635 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 79d8c74c-2431-348f-9ab9-738615a1862e | -2.96973 | -54.08623 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4755352-a448-3605-8085-069b50ea3848 | -3.12522 | -53.70258 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca6a13fa-ff07-3515-9297-a0bea5d90dc9 | -1.18902 | -54.13828 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed022bb4-d524-31a2-ae93-66fbd23be31e | -3.28275 | -54.02269 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e5678d5-8143-3d50-800c-abc8001fd3ab | -3.50518 | -54.64794 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb255223-299d-371a-a782-6c53a1e44bd4 | -6.91972 | -47.65985 | 2026-10-07 05:04:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80033b26-05d3-3077-a6d2-16b0e4077276 | -3.68654 | -55.95115 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3441606a-a55b-3102-a5f1-abab848c8ea3 | -3.02478 | -53.90659 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 377ce364-ca02-3197-b6a0-3c3c81020e25 | -3.50634 | -54.66229 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 834e8058-fc7f-3686-ac44-07ec5f228073 | -2.99456 | -54.03596 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4ee43d1-433e-38cb-a41c-c1a603ff2790 | -2.88172 | -54.08372 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5aecbbc-6f7d-339e-84fe-5984cb150828 | -3.16436 | -50.44157 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4ef3cf-c067-3b36-9fb3-5aeb8f39a5ef | -1.50626 | -54.83159 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README76.md)
